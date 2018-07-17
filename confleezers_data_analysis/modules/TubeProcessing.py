# by Joh Schoeneberg 2018
# All rights reserved

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


def get_tube_length(vesiclePoint,beadPoint):
    return np.linalg.norm(np.array(beadPoint)-np.array(vesiclePoint))


def get_tube_midpoint(vesiclePoint,beadPoint):
    return np.array([beadPoint[0]+int((vesiclePoint[0]-beadPoint[0])/2),beadPoint[1]+int((vesiclePoint[1]-beadPoint[1])/2)])



#----------------------------------------------------------------------------------------
# tube fitting to a gaussian

def gaussian(B,x):
    ''' Returns the gaussian function for B=m,stdev,max,offset '''
    return B[3]+B[2]/(B[1]*np.sqrt(2*np.pi))*np.exp(-((x-B[0])**2/(2*B[1]**2)))

def errfunc(p,x,y):
    return y-gaussian(p,x)





def fitGaussian(data,p0=[9,3,150,20],verbose=False):
    # p0 = [mean,variance,amplitude,yShift]
    # parameters of our gaussian




    y = data
    x = range(0,len(data))

    # initial estimate of parameters

    fit = optimize.leastsq(errfunc,p0,args=(x,y));


    if(verbose):
        plt.plot(x,y,'k-',lw=3)
        plt.plot(x,gaussian(fit[0],x),'r-')
        plt.show()


    mean = fit[0][0]
    stdev = np.absolute(fit[0][1])
    offset = fit[0][3]
    FWHM = 2.355 * np.absolute(stdev)
    maxx = gaussian(fit[0],mean)
    fitconvergence = fit[1]
    #estimate the background by using the median
    background_medianOfData = np.median(y)

    if(verbose):
        print("mean:",mean,"stdev:", stdev,"max:", maxx,"FWHM:",FWHM,"offset:",offset, "maxx:",maxx)
        print("fit parameters: mean: {} variance: {} amplitude: {} yshift: {}".format(fit[0][0],fit[0][1],fit[0][2],fit[0][3]))
    return(np.array([mean,stdev,fit[0][2],offset,maxx,maxx-offset,FWHM,fitconvergence,background_medianOfData,maxx-background_medianOfData]))
