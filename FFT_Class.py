#Final_FFTClass

#Import relevant libraries
import numpy as np
import imageio
from numpy import fft
import matplotlib.pylab as plt
from scipy import ndimage as ndi

#FFT Class which synchronizes the horizontal positions of lines in an image using the convolution theorem
class FFT(object):
    
    #Constructor for FFT class. Takes an image file as an argument and initializes it as a 2d np array. Creates a position list with the index of each pixel in a line. Shows the uncorrected image.
    def __init__(self,filename):
        self.file = filename
        self.im = imageio.imread(self.file)
        self.position = [(i) for i in range(len(self.im[0]))]
        plt.imshow(self.im,cmap=plt.cm.gray)
        plt.show()
        """
        self.im = ndi.gaussian_filter(self.im,sigma=0.8)
        plt.imshow(self.im,cmap=plt.cm.gray)
        plt.show()
        """

#Static method which returns the discrete fourier transform of a list using numpy.fft
    @staticmethod
    def FFT(list):
        return fft.fft(list)

#Static method which returns the complex conjugate of a list
    @staticmethod
    def Conj(list):
        return np.conj(list)

#Static method which returns the auto correlation between two lists. Finds the FT of both, conjugates the first one and multiplies them. Returns inverse FT of the product.
    @staticmethod
    def Auto_Corr(list1,list2):
        FT_autocorr = FFT.Conj(FFT.FFT(list1))*FFT.FFT(list2)
        return fft.ifft(FT_autocorr)

#Instance method to synchronize the horizontal position of two lines in the image by Auto correlating them to find the relative shift. Shifts the second line to a synchronised position
    def Find_Shift(self,i,j):
        AutoCorr = FFT.Auto_Corr(self.im[i],self.im[j])
        index = np.argmax(AutoCorr.real)
        index1 = int(len(self.position)) - index
        return index1
    
    
    #Instance method to shift a row in the instance image by an int "shift"
    def Fix_Row(self,j,shift):
        shift_func = lambda l,n: np.concatenate((l[-n:],l[:-n]))
        self.im[j] = shift_func(self.im[j],shift)
        
    #Engine to correct an instance image with the condition that if the shifts between successive pairs of rows is the same, the latter set is not corrected. 2nd arg is the known shift in the first row of an image
    def Index_Engine(self,index):
        last_index = index
        
        for i in range(len(self.im[:,0])-1):
            next_index = self.Find_Shift(i,i+1)
            if (next_index == last_index)==False:
                self.Fix_Row(i+1,next_index)
            last_index = next_index

        plt.imshow(self.im,cmap=plt.cm.gray)
        plt.show()
    
    #Engine which corrects an instance image by shifting all successive pairs of lines according to the shift between them.Then corrects the whole image for a crude avg shift
    def Shift_Engine(self):
        record_shift=[]
        for i in range(len(self.im[:,0])-1):
            index = self.Find_Shift(i,i+1)
            self.Fix_Row(i+1,index)
            record_shift.append(index)
        median_shift = int(np.median(record_shift))
        self.Shift_Image(-median_shift)

    #Instance method to shift an instance image
    def Shift_Image(self,shift):
        self.im = np.roll(self.im,shift,axis=1)
        plt.imshow(self.im,cmap=plt.cm.gray)
        plt.show()
