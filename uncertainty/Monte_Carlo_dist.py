import numpy as np
import pandas as pd
#import scipy as sci
import matplotlib.pyplot as plt

# create Monte Carlo normal
# make a random distribution fitted to measured value and uncertanty
def find_nearest_index(array, value):
    array = np.asarray(array)
    array = (np.abs(array - value))
    idx = np.where(array == np.min(array))
    return idx

# make a random distribution fitted to measured value and uncertanty
# args : size(size of distribution to be created) defaults to 10000, 
#          seed(seed of random variable generator (optional))
def distn(value, uncert, **args):
    if(args.get('size')==None):
        step = 100000
    else:
        step = args.get('size')
    np.random.seed(args.get('seed'))
    x = value + uncert * np.random.normal(size=step)
    return x

# args : size(size of distribution to be created) defaults to 10000, 
#          seed(seed of random variable generator (optional)) 
def dist_uniform(value, uncert_plus, uncert_min, **args):
    if(args.get('size')==None):
        step = 100000
    else:
        step = args.get('size')
    np.random.seed(args.get('seed'))
    x = value + np.random.uniform(high=uncert_plus, low=uncert_min, size=step)
    return x


# find the max and min in the 'percentile' specified of a 
# distribution of numbers
def plus_min(mode, arr, percentile):
    arr = np.sort(arr)
    length = np.size(arr)
    index_min = np.floor(length * ((1 - percentile) / 2))
    index_max = length - np.floor(length * ((1 - percentile) / 2))
    max_ = arr[int(index_max)]
    min_ = arr[int(index_min)]
    plus = abs(max_ - mode)
    mins = abs(mode - min_)
    return [plus, mins]


# create Monte Carlo normal dist class
# args: bins(number of bins used to calculate mode)defaults to 1000, 
#        percentile(percentile to calculate confindence inteveral with) defaults to .68
class dist:
    def __init__(self, equation, **args):
        self.pos_ans = equation
        if(args.get('bins') == None):
            bins_ = 1000
        else:
            bins_ = args.get('bins')  
        self.occurance, self.values = np.histogram(equation, bins=bins_)
        y = self.occurance
        x = self.values
        self.mode = np.mean(x[np.where(y == y.max())])
        #self.skew = sci.stats.skew(equation)
        if(args.get('percentile') == None):
            percentile = .68
        else:
            percentile = args.get('percentile')
        self.uncertanty = self.create_uncertanty(self.mode, self.pos_ans, percentile)
    def create_uncertanty(self, mode, pos_ans, percentile):
        return dist.uncertanty(mode, pos_ans, percentile)
    #args bins(int)(bins to plot), filepath(str)(file to store the uncertanty plot),
    #txt(str)(txt to put on plot where uncertanty should be),  txt_location(tuple)(location of plot text),
    #title(str)(plot title), xlabel(str), ylabel(str), fontsize(int),
    #rnd(int)(the number of digits to round the uncertanty to),
    #fig(int)(figure number for uncertanty plot)
    def plot(self, **args):
        if(args.get('rnd')==None):
            rnd = 4
        else:
            rnd = args.get('rnd')  
        if(args.get('bins')==None):
            bins_ = 1000
        else:
            bins_ = args.get('bins')  
        if(args.get('txt')==None):
            txt = str(round(self.mode, rnd)) + ' (+'\
            + str(round(self.uncertanty.plus, rnd)) \
            + ', -' + str(round(self.uncertanty.min, rnd)) + ')'
        else:
            txt = args.get('txt')
        if(args.get('txt_location')==None):
            txt_loc = tuple((0.5, 0.95))
        else:
            txt_loc = args.get('txt_location')
        if(args.get('fontsize')==None):
            ftsize = 10
        else:
            ftsize = args.get('fontsize')
        fig = plt.figure(args.get('fig'))
        ax = fig.subplots()
        plt.hist(self.pos_ans, bins=bins_)
        plt.title(args.get('title'))
        plt.xlabel(args.get('xlabel'))
        plt.ylabel(args.get('ylabel'))
        
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        ax.text(txt_loc[0], txt_loc[1], txt, transform=ax.transAxes, 
                fontsize=ftsize, verticalalignment='top', bbox=props)
        if(args.get('file_path')!=None):
            plt.savefig(args.get('file_path')) 
        
        #args percentile
    class uncertanty:
        def __init__(self, mode, pos_ans, percentile):
            self.pos_ans = pos_ans
            self.mode = mode
            unc = plus_min(mode, pos_ans, percentile)
            self.plus = unc[0]
            self.min = unc[1]
            self.percentile = percentile


# =============================================================================
# i = distn(45,1, size=1000000)
# v = distn(25,2, size=1000000)
# t = (i*v) - pow(i,2)
# a = Monte_Carlo_dist(t)
# a.plot()
# =============================================================================
