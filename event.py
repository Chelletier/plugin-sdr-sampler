# this module will be imported in the into your flowgraph
import time
import os

os.mkdir('/lightning/data' + time.strftime('%b_%d_%Y_%H_%M', time.localtime()))
folder = '/lightning/data' + time.strftime('%b_%d_%Y_%H_%M', time.localtime())
store = folder + '/'+ time.strftime('%b_%d_%Y_%H_%M', time.localtime()) + '.txt'

with open(store,'a') as f:
        f.write(time.strftime('BEGIN RECORDING: %b %d %Y %H:%M:%S \n', time.localtime()))
