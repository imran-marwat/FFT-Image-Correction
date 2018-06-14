#Final_TestClass: Script to run Final_FFTClass

from FFTClass import FFT
from scipy import misc
import matplotlib.pylab as plt
import numpy as np
import sys

#Creates instance of FFT class
pic = FFT(sys.argv[1])

if len(sys.argv)!= 3:
    print("Error: 3 arguments required. 3rd arg should be 0 for Index_Method or 1 for Shift_Method")

#If user wants to see a plot of the auto-correlation between any 2 lines eg line 5&6
elif sys.argv[2] == '0':
    AutoCorr = FFT.Auto_Corr(pic.im[4],pic.im[5])
    plt.plot(pic.position,AutoCorr.real)
    plt.show()

    shift = pic.Find_Shift(4,5)
    print(shift)

#If user wants to run Index engine
elif sys.argv[2] == '1':
    pic.Index_Engine(0)

#If user wants to run Shift engine
elif sys.argv[2] == '2':
    pic.Shift_Engine()

else: print("Error: 3rd argument does not correspond to any method. Enter 1 for Index_Method or 2 for Shift_Method")
