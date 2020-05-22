import matplotlib.pyplot as plt
import numpy as np

def Peaks(Sample):
    """ This functions takes the y-value and returns all peaks for an oscilating measurment """
    if not isinstance(Sample, (list,tuple)):
        raise TypeError("The Input in maximums is of the wrong type, requires a list or tuple")
    peaks=[]
    index=[]
    for i in range(1,len(Sample)):
        if i == len(Sample):
            break
        else:
            if Sample[i]>Sample[i+1] and Sample[i]>Sample[i-1]:
                peaks.append(Sample[i])
                index.append(i)
    return peaks, index 

def Intersection(Sample1, Sample2, epsilon = None, Samplex = None):
    """ This method takes the intersection of two data-sets. A error can be specified for correlationdata. The third and forth
    entry are optional, if one have spaced data or want to plot the function. """
    if not isinstance((Sample1, Sample2, Samplex), (list,tuple)):
        raise TypeError("The input of the Intersection method needs to be of list, or tuple.")
    intersection = []
    index = []
    try:
        for i in range(len(Sample1)):
            if abs(Sample1[i]-Sample2[i])<=epsilon:
                intersection.append(Sample1[i])
                index.append(i)
        return intersection, index
    except:
        raise ValueError("An Error occured in the Intersection method, email the maintainer if the problem presists.")
    try:
        if Samplex != None:
            plt.plot(Samplex, Sample1, 'r')
            plt.plot(Samplex, Sample2, 'b')
            plt.show()
    except:
        if len(Samplex)!=len(Sample1):
            print("The list shapes are not equal.")

def PartialDerivitive(func, x, y, h=1e-9):
    """ Takes the partial derivitive of function f(x,y), and return it as an array """
    if not callable(func):
        raise KeyError(f"The function {func} is not callable.")
    Jacobian = (1/h)*np.array([func(x+h,y)-func(x,y),func(x,y+h)-func(x,y)])
    return Jacobian