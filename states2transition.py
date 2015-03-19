import sys, os
import numpy as na

#FOR SIGE
#wftype = [ 'x3' , 'kp6' ]

#FOR III-V
wftype = [ 'kp8' , 'kp8' ]


#states typically expected in the form: (hole state),(electron state),(amount)
states = [
['1','3',0.25],
['1','4',0.25],
['2','3',0.25],
['2','4',0.25],



#['7','9',0.25],
#['7','10',0.25],
#['8','9',0.25],
#['8','10',0.25],
#
#'7','11',0.25,
#'7','12',0.25,
#'8','11',0.25,
#'8','12',0.25,
#
#'5','11',0.25,
#'5','12',0.25,
#'6','11',0.25,
#'6','12',0.25,
#
#'5','9',0.25,
#'5','10',0.25,
#'6','9',0.25,
#'6','10',0.25,
#
#'3' , '13' ,0.25,
#'3' , '14' ,0.25,
#'4' , '13' ,0.25,
#'4' , '14' ,0.25,
#
#FOR SIGE (electron) (hole) (amount)
#'1_0', '1', 0.25,
#'1_0', '2', 0.25,
#'1_1', '1', 0.25,
#'1_1', '2', 0.25,
#'1_0', '3', 0.25,
#'1_0', '4', 0.25,
#'1_1', '3', 0.25,
#'1_1', '4', 0.25,
#'2_0', '1', 0.25,
#'2_0', '2', 0.25,
#'2_1', '1', 0.25,
#'2_1', '2', 0.25,
#'2_0', '3', 0.25,
#'2_0', '4', 0.25,
#'2_1', '3', 0.25,
#'2_1', '4', 0.25,
#'3_0', '1', 0.25,
#'3_0', '2', 0.25,
#'3_1', '1', 0.25,
#'3_1', '2', 0.25,
#'3_0', '3', 0.25,
#'3_0', '4', 0.25,
#'3_1', '3', 0.25,
#'3_1', '4', 0.25,
]

#nextnano3 wfs order: (electron) (hole) (amount)
wftypeNN3 = '8x8'  #or '1x6'
statesNN3=[
'1', '2', 1.0,
]