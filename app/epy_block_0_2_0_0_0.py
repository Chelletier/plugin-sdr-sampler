"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import time
import wave


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
        self.x=0
        self.mid='i'
    
    def work(self, input_items, output_items):
        if (np.all(input_items[1] == 1)):
                output_items[0][:] = input_items[0][:]

                with wave.open('/home/waggle/' + self.mid + '.wav', 'w') as f:
                        # 2 Channels.
                        f.setnchannels(2)
                        # 2 bytes per sample.
                        f.setsampwidth(2)
                        f.setframerate(2560000)
                        f.writeframes(input_items[0])


        else: 
                self.x=self.x+1
                self.mid=str(self.x)
                
                output_items[0][:] = 0
        return len(output_items[0])
