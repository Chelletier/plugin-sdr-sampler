"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import time
import cmath

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self,mod = 1.75):  # only default arguments here
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
        self.test = 0
        self.count = 1
        self.test2 = 0
        self.reset = 10000
        self.mod = mod
        
    def work(self, input_items, output_items):
        self.test = self.test + 1
        if (0 < np.max(input_items[0])) and (self.index < self.reset):
                self.index = self.index + 1
                if(self.alpha < np.max(input_items[0])) and (self.index < self.reset):
                        self.alpha = np.max(input_items[0])
#                        print(self.alpha.real)
                        self.test2 = np.max(input_items[0]).real + self.test2
                        self.count = self.count + 1
                if(self.index > self.reset - 1) and (self.test2 != 0):
#                        print(self.alpha.real)
#                        print(self.test2/self.count)

#                        self.bigt = (self.alpha.real) + (self.alpha.real) * 0.2 
                        self.bigt = (self.test2/self.count) * self.mod 
                        print(self.bigt)
                        self.index = 0
                        self.test2 = 0
                        self.count = 1
                        self.reset = 10000
                        self.alpha = 0
#                        print(self.bigt)
#                        print('x')
#        if(self.test % 1000 == 0):
#                print(self.index)
#                print(np.max(input_items[0]).real)                
#                print('max ^')
      
#        if (np.max(input_items[0]).real > self.bigt):
#                print(np.max(input_items[0]).real)
#                print(self.bigt)
#                print('^')
                
        if (np.all(input_items[1] == 1)):
                output_items[0][:] = input_items[0]
                
        else: 
                output_items[0][:] = 0
        return len(output_items[0])
        
    def thresh(self):
        return self.bigt
