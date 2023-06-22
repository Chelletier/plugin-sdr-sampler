#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: NOGUICODE
# GNU Radio version: 3.10.1.1

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
import event  # embedded python module
import time

import argparse


def snipfcn_snippet_0(self):
    with open(self.location + '.txt','a') as f:
                                    f.write(time.strftime('END OF RECORDING: %b %d %Y %H:%M:%S \n', time.localtime()))


def snippets_main_after_stop(tb):
    snipfcn_snippet_0(tb)


class NOGUICODE(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "NOGUICODE", catch_exceptions=True)

        ##################################################
        # Variables
        ##################################################
        
        self.thresh = thresh = 1.0
        self.samp_rate = samp_rate = 2560000
        self.location = location = '/lightning/data' + time.strftime('%b_%d_%Y_%H_%M', time.localtime()) + '/'+ time.strftime('%b_%d_%Y_%H_%M', time.localtime())
        self.Freq = Freq = 55000000

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
        self.soapy_rtlsdr_source_0.set_frequency(0, 55000000)
        self.soapy_rtlsdr_source_0.set_frequency_correction(0, 0)
        self.soapy_rtlsdr_source_0.set_gain(0, 'TUNER', 20)
        self.epy_block_1_0_0_0 = epy_block_1_0_0_0.blk(stall=5000)
        self.epy_block_0_2_0_0_0 = epy_block_0_2_0_0_0.blk()
        self.blocks_wavfile_sink_0_0_0_0 = blocks.wavfile_sink(
            location,
            2,
            samp_rate,
            blocks.FORMAT_WAV,
            blocks.FORMAT_PCM_16,
            False
            )
        self.blocks_threshold_ff_0_0_0_0 = blocks.threshold_ff(thresh * -1, thresh, 0)
        self.blocks_null_sink_0_0_0_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_float_to_char_0_0_0_0 = blocks.float_to_char(1, 1)
        self.blocks_delay_1_0_0_0 = blocks.delay(gr.sizeof_gr_complex*1, 10000000)
        self.blocks_complex_to_float_1_0_0_0 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0_0_0_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_1_0_0_0 = blocks.add_vff(1)
        self.analog_sig_source_x_0_0_0_0_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_SQR_WAVE, 100, -1, 0, 3)
        self.analog_pwr_squelch_xx_0_0_0_0 = analog.pwr_squelch_cc(-60, 1e-4, 0, True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_pwr_squelch_xx_0_0_0_0, 0), (self.blocks_complex_to_float_0_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0_0_0_0_0, 0), (self.blocks_add_xx_1_0_0_0, 1))
        self.connect((self.blocks_add_xx_1_0_0_0, 0), (self.blocks_threshold_ff_0_0_0_0, 0))
        self.connect((self.blocks_complex_to_float_0_0_0_0, 1), (self.blocks_wavfile_sink_0_0_0_0, 1))
        self.connect((self.blocks_complex_to_float_0_0_0_0, 0), (self.blocks_wavfile_sink_0_0_0_0, 0))
        self.connect((self.blocks_complex_to_float_1_0_0_0, 1), (self.blocks_add_xx_1_0_0_0, 0))
        self.connect((self.blocks_complex_to_float_1_0_0_0, 0), (self.blocks_null_sink_0_0_0_0, 0))
        self.connect((self.blocks_delay_1_0_0_0, 0), (self.epy_block_0_2_0_0_0, 0))
        self.connect((self.blocks_float_to_char_0_0_0_0, 0), (self.epy_block_1_0_0_0, 0))
        self.connect((self.blocks_threshold_ff_0_0_0_0, 0), (self.blocks_float_to_char_0_0_0_0, 0))
        self.connect((self.epy_block_0_2_0_0_0, 0), (self.analog_pwr_squelch_xx_0_0_0_0, 0))
        self.connect((self.epy_block_1_0_0_0, 0), (self.epy_block_0_2_0_0_0, 1))
        self.connect((self.soapy_rtlsdr_source_0, 0), (self.blocks_complex_to_float_1_0_0_0, 0))
        self.connect((self.soapy_rtlsdr_source_0, 0), (self.blocks_delay_1_0_0_0, 0))


    def get_thresh(self):
        return self.thresh

    def set_thresh(self, thresh):
        self.thresh = thresh
        self.blocks_threshold_ff_0_0_0_0.set_hi(self.thresh)
        self.blocks_threshold_ff_0_0_0_0.set_lo(self.thresh * -1)

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




def main(top_block_cls=NOGUICODE, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()
        snippets_main_after_stop(tb)
        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()
    snippets_main_after_stop(tb)


# This part needs changes to work as intended.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description="Plugin for sampling RTL-SDR data")

 
    parser.add_argument("--thres",
                        type=float,
                        dest='thres',
                        default=1,
                        help="Amplitude threshold for detecting signals."
                        )
    args = parser.parse_args()

    main()
