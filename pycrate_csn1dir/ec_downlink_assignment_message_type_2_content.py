# -*- coding: UTF-8 -*-
#/**
# * Software Name : pycrate
# * Version : 0.3
# *
# * Copyright 2018. Benoit Michau. P1sec.
# *
# * This library is free software; you can redistribute it and/or
# * modify it under the terms of the GNU Lesser General Public
# * License as published by the Free Software Foundation; either
# * version 2.1 of the License, or (at your option) any later version.
# *
# * This library is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# * Lesser General Public License for more details.
# *
# * You should have received a copy of the GNU Lesser General Public
# * License along with this library; if not, write to the Free Software
# * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, 
# * MA 02110-1301  USA
# *
# *--------------------------------------------------------
# * File Name : pycrate_csn1dir/ec_downlink_assignment_message_type_2_content.py
# * Created : 2018-10-08
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.018 - d80
# section: 9.1.67 EC DOWNLINK ASSIGNMENT TYPE 2
# top-level object: EC Downlink Assignment message Type 2 content



# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

spare_padding = CSN1Val(name='spare_padding', val='L', num=-1)
Spare_padding = spare_padding
Spare_Padding = spare_padding 

ec_downlink_allocation_struct = CSN1List(name='ec_downlink_allocation_struct', list=[
  CSN1Bit(name='timing_advance', bit=6),
  CSN1Bit(name='starting_dl_timeslot', bit=3),
  CSN1Bit(name='downlink_tfi_assignment', bit=5),
  CSN1Bit(name='timeslot_muliplicator', bit=2),
  CSN1Bit(name='starting_ul_timeslot_offset', bit=2),
  CSN1Bit(name='gamma', bit=5),
  CSN1Bit(name='alpha_enable'),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='p0', bit=4),
    CSN1Bit(name='pr_mode')])})])

ec_downlink_assignment_message_type_2_content = CSN1List(name='ec_downlink_assignment_message_type_2_content', list=[
  CSN1Bit(name='message_type', bit=4),
  CSN1Bit(name='used_dl_coverage_class', bit=2),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='ec_page_extension', bit=4)])}),
  CSN1Bit(name='tlli', bit=32),
  CSN1Bit(name='ec_packet_channel_description_type_3', bit=15),
  CSN1Ref(name='ec_downlink_allocation', obj=ec_downlink_allocation_struct),
  CSN1Ref(obj=spare_padding)])

