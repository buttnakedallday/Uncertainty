
import uncertainty.Monte_Carlo_dist as m

#input measurments as randomly seeded distributions
k = m.dist_uniform(164,3,1, size=100000)
h = m.distn(2,.01)
w = m.distn(2,.01)
A = h*w
t2 = m.distn(50,1)
t1 = m.distn(120, 1, size=100000)
x1 = 0
x2 = m.distn(1, .01)

# calculate possible answers using measurment distributions
q = -k * A *((t2-t1)/(x2-x1))

#create Monte_Carlo_dist object
q = m.dist(q, bins=1000, percentile=.68)
# finding properties of the Monte_Carlo_dist distribution 
q_value = q.uncertanty.mode
q_confidence_interval = q.uncertanty.percentile
plus = q.uncertanty.plus
minus = q.uncertanty.min
#plot monte_carlo uncertanty ditstibution
txt_loc = (0.5, 0.96)
q.plot(bins=50, file_path='C:/Users/rjw3/OneDrive/Desktop/Test_pic',txt_location=txt_loc, fontsize=11,
       title='Q Uncertainty distribution', xlabel='Q', ylabel='Probability Density',
       density=True)


import uncertainty.Multivariable_Propagation as m
import sympy as sym
import numpy as np

# create variables using sympy
u = sym.Symbol('u')
d = sym.Symbol('d')
v = sym.Symbol('v')
# create equation using variables made with sympy
Re_sym = (u * d) / v
#create numpy array of variables made with sympy
var = np.array([u, d, v])
#create numpy array of the uncertanty of variables
# make sure to create array in same order as var(var_need) array
uncert = np.array([.1, .005, 2.44*pow(10,-8)])
#create numpy array of the measure values of variables
# make sure to create array in same order as var(var_need) array
val = np.array([.5, .01, 2.44*pow(10,-5)])
# create Multvar_prop object
Re_sym = m.Multvar_prop(Re_sym, var, uncert, val)
# use self.part_diff to find pow((d var_dif / d symbolic_eq),2)
# this will show which uncertanties are causing the most uncertanty\
# in the lab answer (in this case Re)
p_diff = Re_sym.part_diff
uncert = Re_sym.uncertanty

#printed self.part_diff and self.uncertanty to console
print(p_diff)
print('\n')
print('uncertanty=' + '\n+-' + 
      str(round(uncert, 2)))












