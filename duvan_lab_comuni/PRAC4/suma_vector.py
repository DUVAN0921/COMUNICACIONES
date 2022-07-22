#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2022 PARAM1.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy
import math 
from gnuradio import gr

class suma_vector(gr.sync_block):
    """
    docstring for block suma_vector
    """
    def __init__(self, param2):
        self.param2= param2
        gr.sync_block.__init__(self,
            name="suma_vector",
            in_sig=[(numpy.float32,int(self.param2)) ],
            out_sig=[numpy.float32, ])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        for i in range(len(in0))
                 out[i] = math.fsum(in0[i,:])
        return len(output_items[0])

         
        
