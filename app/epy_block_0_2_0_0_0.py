"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import time


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Binary Gate',   # will show up in GRC
            in_sig=[np.complex64,np.byte],
            out_sig=[np.complex64]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.index = 0
        self.alpha = 0
        self.bigt = 1
        
    def work(self, input_items, output_items):
        if (0 < np.max(input_items[0])):
                self.index = self.index + 1
                if(self.alpha < np.max(input_items[0])) and (self.index < 100):
                        self.alpha = np.max(input_items[0])
                        self.index = self.index + 1
                if(self.index > 99):
                        self.bigt = self.alpha + self.alpha * .01 
        
        if (np.all(input_items[1] == 1)):
                output_items[0][:] = input_items[0]
                
        else: 
                output_items[0][:] = 0
        return len(output_items[0])
