#Multvar_propagation of error
import sympy as sym
import numpy as np
import pandas as pd

#used to build a dictionary variables in Multvar_prop
def build_dict(key_arr, value_arr):
    if(len(key_arr) !=len(value_arr)):
        print('key_arr must be same len as value_arr')
    else:
        re = dict()
        for i in range(0, len(key_arr)):
            re[key_arr[i]] = value_arr[i]
    return(re)


class Multvar_prop:
    def __init__(self, symbolic_eq, var_need, uncertanty, values):
        symb = build_dict(var_need, var_need)
        u = dict()
        s = dict()
        K = 0
        for i in symb.keys():
            symb[i] = sym.symbols(str(symb[i]))
            u[symb[i]] = uncertanty[K]
            s[symb[i]] = values[K]
            K = K+1
        part_diff = pd.DataFrame(np.zeros((1,len(symb.keys())))\
                         ,columns=symb.keys())
        for i in part_diff.columns.values:
            solve = sym.diff(symbolic_eq, symb[i])
            part_diff.loc[0, i] = float(solve.subs(s))
            part_diff.loc[0, i] = part_diff.loc[0, i] * u[symb[i]]
        ans = part_diff.pow(2)
        self.part_diff = ans
        ans = ans.sum(axis=1)
        self.uncertanty = np.sqrt(ans[0])
        

# =============================================================================
# x = sym.Symbol('x')
# y = sym.Symbol('y')
# T = sym.cosh(x*y) / y
# L = Multvar_prop(T, np.array([x,y]), np.array([.1,.5]), np.array([1,2]))
# u = L.uncertanty
# z= L.part_diff
# 
# 
# =============================================================================



