# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: envolvente compleja PM J1A
# Author: Adriana_La_Rotta_Jairo_Sanchez
# Copyright: UIS
# GNU Radio version: 3.10.1.1

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal







class practica4(gr.hier_block2, Qt.QWidget):
    def __init__(self, Ac=0.1, Kp=1):
        gr.hier_block2.__init__(
            self, "envolvente compleja PM J1A",
                gr.io_signature(1, 1, gr.sizeof_float*1),
                gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        Qt.QWidget.__init__(self)
        self.top_layout = Qt.QVBoxLayout()
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)
        self.setLayout(self.top_layout)

        ##################################################
        # Parameters
        ##################################################
        self.Ac = Ac
        self.Kp = Kp

        ##################################################
        # Blocks
        ##################################################
        self.blocks_transcendental_1 = blocks.transcendental('cos', "float")
        self.blocks_transcendental_0 = blocks.transcendental('sin', "float")
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_ff(Kp)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(Ac)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_transcendental_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_transcendental_1, 0))
        self.connect((self.blocks_transcendental_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_transcendental_1, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self, 0), (self.blocks_multiply_const_vxx_1, 0))


    def get_Ac(self):
        return self.Ac

    def set_Ac(self, Ac):
        self.Ac = Ac
        self.blocks_multiply_const_vxx_0.set_k(self.Ac)

    def get_Kp(self):
        return self.Kp

    def set_Kp(self, Kp):
        self.Kp = Kp
        self.blocks_multiply_const_vxx_1.set_k(self.Kp)

