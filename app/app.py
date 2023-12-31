#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: NOGUICODE
# GNU Radio version: 3.10.1.1
#test

from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import soapy
import epy_block_0_2_0_0_0  # embedded python block
import epy_block_1_0_0_0  # embedded python block
import time
import os
#import matplotlib.pyplot as plt
#import numpy as np
#import scipy.signal
#from scipy.io import wavfile 

import argparse

from waggle.plugin import Plugin, get_timestamp


def snipfcn_snippet_0(self):
    with open(self.txt,'a') as f:
                                    f.write(time.strftime('END OF RECORDING: %b %d %Y %H:%M:%S \n \n \n', time.localtime()))


def snippets_main_after_stop(tb):
    snipfcn_snippet_0(tb)


class NOGUICODE(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "NOGUICODE", catch_exceptions=True)

        ##################################################
        # Variables
        ##################################################
        
        self.samp_rate = samp_rate = 2560000
        self.location = location = '/lightning/'
        self.freq = freq = args.freq
        self.txt = self.location + 'event_times.txt'
        self.wav = self.location + time.strftime('%H_%M_%S', time.localtime()) + '.wav'

        if(os.path.exists(self.location)==False):
             os.mkdir(self.location)
        
        with open(self.txt,'a') as f:
             f.write(time.strftime( '\n Center Frequency: ' + str(args.freq)+ '\n Threshold Modifier: ' + str(args.mod) + '\n \n ' + 'BEGIN RECORDING: %b %d %Y %H:%M:%S \n', time.localtime()))
#' Threshold: ' + str(self.thresh)+
        ##################################################
        # Blocks
        ##################################################
        self.soapy_rtlsdr_source_0 = None
        dev = 'driver=rtlsdr'
        stream_args = ''
        tune_args = ['']
        settings = ['']

        self.soapy_rtlsdr_source_0 = soapy.source(dev, "fc32", 1, '',
                                  stream_args, tune_args, settings)
        self.soapy_rtlsdr_source_0.set_sample_rate(0, samp_rate)
        self.soapy_rtlsdr_source_0.set_gain_mode(0, False)
        self.soapy_rtlsdr_source_0.set_frequency(0, self.freq)
        self.soapy_rtlsdr_source_0.set_frequency_correction(0, 0)
        self.soapy_rtlsdr_source_0.set_gain(0, 'TUNER', 20)
        self.epy_block_1_0_0_0 = epy_block_1_0_0_0.blk(stall=2500,local=self.location)
        self.epy_block_0_2_0_0_0 = epy_block_0_2_0_0_0.blk(mod = args.mod)
        self.thresh = self.epy_block_0_2_0_0_0.bigt
        self.blocks_wavfile_sink_0_0_0_0 = blocks.wavfile_sink(
            self.wav,
            2,
            samp_rate,
            blocks.FORMAT_WAV,
            blocks.FORMAT_PCM_16,
            False
            )

        self.blocks_threshold_ff_0_0_0_0 = blocks.threshold_ff(.01, self.thresh, 0)
        self.blocks_null_sink_0_0_0_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_float_to_char_0_0_0_0 = blocks.float_to_char(1, 1)
        self.blocks_delay_1_0_0_0 = blocks.delay(gr.sizeof_gr_complex*1, 4000000)
        self.blocks_complex_to_float_1_0_0_0 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0_0_0_0 = blocks.complex_to_float(1)
        self.analog_pwr_squelch_xx_0_0_0_0 = analog.pwr_squelch_cc(-60, 1e-4, 0, True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_pwr_squelch_xx_0_0_0_0, 0), (self.blocks_complex_to_float_0_0_0_0, 0))
        self.connect((self.blocks_complex_to_float_0_0_0_0, 1), (self.blocks_wavfile_sink_0_0_0_0, 1))
        self.connect((self.blocks_complex_to_float_0_0_0_0, 0), (self.blocks_wavfile_sink_0_0_0_0, 0))
        self.connect((self.blocks_complex_to_float_1_0_0_0, 0), (self.blocks_threshold_ff_0_0_0_0, 0))
        self.connect((self.blocks_complex_to_float_1_0_0_0, 1), (self.blocks_null_sink_0_0_0_0, 0))
        self.connect((self.blocks_delay_1_0_0_0, 0), (self.epy_block_0_2_0_0_0, 0))
        self.connect((self.blocks_float_to_char_0_0_0_0, 0), (self.epy_block_1_0_0_0, 0))
        self.connect((self.blocks_threshold_ff_0_0_0_0, 0), (self.blocks_float_to_char_0_0_0_0, 0))
        self.connect((self.epy_block_0_2_0_0_0, 0), (self.analog_pwr_squelch_xx_0_0_0_0, 0))
        self.connect((self.epy_block_1_0_0_0, 0), (self.epy_block_0_2_0_0_0, 1))
        self.connect((self.soapy_rtlsdr_source_0, 0), (self.blocks_complex_to_float_1_0_0_0, 0))
        self.connect((self.soapy_rtlsdr_source_0, 0), (self.blocks_delay_1_0_0_0, 0))


    def get_thresh(self):
        return self.epy_block_0_2_0_0_0.bigt

    def set_thresh(self, thresh, epy_block_0_2_0_0_0):
        self.thresh = self.epy_block_0_2_0_0_0.bigt
        self.blocks_threshold_ff_0_0_0_0.set_hi(self.thresh)
        self.blocks_threshold_ff_0_0_0_0.set_lo(.01)
        print('test')

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0_0_0_0_0_0_0.set_sampling_freq(self.samp_rate)
        self.soapy_rtlsdr_source_0.set_sample_rate(0, self.samp_rate)

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location
        self.blocks_wavfile_sink_0_0_0_0.open(self.location)

    def get_Freq(self):
        return self.Freq

    def set_Freq(self, Freq):
        self.Freq = Freq




def main(args,top_block_cls=NOGUICODE, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()
        snippets_main_after_stop(tb)
        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)


    tb.start()
#    print(tb.epy_block_0_2_0_0_0.bigt)
#    while (tb.epy_block_1_0_0_0.events < 1):
#            time.sleep(3)
#            print('while 1')
    while tb.epy_block_1_0_0_0.ends == 0:
         time.sleep(1)
#         print(tb.epy_block_0_2_0_0_0.bigt)
#         print(tb.epy_block_0_2_0_0_0.bigt)
         tb.blocks_threshold_ff_0_0_0_0.set_hi(tb.epy_block_0_2_0_0_0.bigt)


    if (tb.epy_block_1_0_0_0.events > tb.epy_block_1_0_0_0.ends):
            time.sleep(2)
#    print(tb.epy_block_0_2_0_0_0.bigt)
    tb.stop()
    tb.wait()
    snippets_main_after_stop(tb)
    
    meta = {'sdr_events':str(tb.epy_block_1_0_0_0.events),
            'sdr_threshold_mod':str(args.mod),
            'sdr_frequency':str(args.freq)
    }
    if(tb.epy_block_1_0_0_0.events > 0):
            with Plugin() as plugin:
                 plugin.upload_file(tb.txt, meta=meta)
                 plugin.upload_file(tb.wav, meta=meta)
                 plugin.publish('sdr.events', tb.epy_block_1_0_0_0.events, meta=meta)
#         fs, data = wavfile.read('/media/waggle/Seagate Por/Lightning Data/poop/whoops')
#         please = data[:,0] + 1j*data[:,1]
#         please = np.trim_zeros(please)
#         please = please[~np.isnan(please)]

#         plt.specgram(please, NFFT=1024, Fs=fs, Fc=55000000)
#         plt.title("PSD of 'signal' loaded from file")
#         plt.xlabel("Time")
#         plt.ylabel("Frequency")
#         plt.savefig(tb.location + 'specgram.png')
#            plugin.upload_file(tb.location + 'specgram.png', meta=meta)

#         plt.psd(please, NFFT=1024, Fs=256000)
#         plt.title("PSD of 'signal' loaded from file")
#         plt.savefig(tb.location + 'PSD.png')
#            plugin.upload_file(tb.location + 'PSD.png', meta=meta)

# This part needs changes to work as intended.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description="Plugin for sampling RTL-SDR data")

    parser.add_argument("--tmod",
                        type=float,
                        dest='mod',
                        default=2.75,
                        help="tunes the threshold"
                        )
    parser.add_argument("--frequency",
                        type=int,
                        dest='freq',
                        default=25000000,
                        help="Center frequency scanned (Hz)."
                        )
    args = parser.parse_args()

    main(args)
