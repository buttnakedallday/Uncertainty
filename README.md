# Uncertainty


This is a package that was created to calculate uncertanty in lab calculations for ME labs. Fell free to use.
Improvements are welcome. 

dependents:
    numpy
    sympy
    pandas
    matplotlib

Multivariable_Propagation:
Uses the method of multivariable propagetion (seen here) to calculate uncertanty in calculations
here = http://www.pa.uky.edu/~kwng/fall2010/phy335/lecture/lecture%202.pdf

Classes:
  Multivar_prop:
    required(symbolic_eq, var_need, uncertanty, values)
      symbolic_eq   - equation created using sympy 
      var_need      - all variables in equation type(numpy.array)
      (numpy.array)
      uncertanty    - uncertanty in each value corasponding to the variables in "var_need" 
      type(numpy.array)          ! be certian "uncertanty" is indexed in th same order as "var_need"
      values        - measured value of each variable in "var_need" 
      type(numpy.array)          ! be certian "values" is indexed in th same order as "var_need" & "uncertanty"
      
    Objects
      self.part_diff - partial differential of "symbolic_eq" with respect to each variable in "var_need"
      type(numpy.array)          to the power of 2
      self.uncertanty - uncertanty calcualated using the multivariable propigation method
      type(float) 

Monte_carlo_dist:
Used to create a randomly sampled distribution of numbers based on the uncertanty in the measurment made
and evaluate the equation using element-wise operators. The result is a distribution representing uncertanty
of the calculated value. Method seen in video here (All credit for this video goes to Dr. Robert Fithen of ATU).
here = https://www.youtube.com/watch?v=jrakrV4rcQk&list=PLEE6E3258670938BE&index=1

Functions:
  distn(value, uncert, size=size):
    used to create an array of posible values randomly sampled from a NORMAL distribution
    required(value, uncert,  size=size):
      value  - measured value
      type(float or int)
      uncert - uncertanty in measured value
      type(float or int)
    optional:
      size   - size of array to be created (default=100000)
      type(int)   ! make sure all distributions are the same size
   dist_uniform(value, uncert_plus, uncert_min, size=size):
      used to create an array of posible values randomly sampled from a UNIFORM distribution
      required(value, uncert_plus, uncert_min)
        value       - measured value
        type(float or int)
        uncert_plus - uncertanty in the positive direction
        type(float or int)
        uncert_min  - uncertanty in the negatve direction
        type(float or int)
      optional:
        size        - size of array to be created (default=100000)
        type(int)   ! make sure all distributions are the same size
        
Classes:
  dist(equation, bins=bins, percentile=confidence interval)
  creates Monte_carlo_distribution class to analyse
    required:
      equation - array created by running calculation using elementwise operators
      type(numpy.array)
    optional:
      bins     - number of bins to use when chreating histogram used to find mode of "equaiton"
      type(int)
      percentile - confidence interval desired (default=.68) (between 0 and 1)
      type(float)
    Objects
      self.values    - x values of historagram of "equation" generated
      type(numpy.array)
      self.occurance -  y values of historagram of "equation" generated
      type(numpy.array)
    Functions:
      plot():
      plots Monte carlo distribution using matplotlib
        reqired(None):
        optional(filepath=filepath, bins=bins, title=title, xlabel=xlabel, ylabel=ylabel fontsize=fontsize,
                  rnd=rnd, fig=fig, density=density):
          filepath     -  file to store the uncertanty plot (default=None)
          type(str)
          bins         - bins to plot(default=1000)
          type(int)
          title        - title of plot (default=None)
          type(str)
          xlabel       - x label of plot (default=none)
          type(str)
          ylabel       - y label of plot (default=none)
          type(str)
          fontsize     - size of font displaying mode (mostlikley value) and uncertanty
          type(int)
          rnd          - how many decimal places to round the displayed mode (mostlikley value) and uncertanty to
          type(int)
          fig          - specify figure to plot the distribution on
          type(int)
          density      - If true a PDF distribution will be plotted (default=False)
          type(bool)
    subClasses:
      uncertanty():
      auto generated to find uncertanty from "equation" using specified cinfidence interval
        objects:
          self.pos_ans    - same as input "equation"
          self.mode       - same as dist.mode
          type(float)
          self.plus       - uncertanty of answer(mode) in the positive direction
          type(float)
          self.min        - uncertanty of answer(mode) in the negative direction
          type(float)
          self.percentile - confidence interval used to calulate uncertanty (input when dist is created)
          type(float)
         
      
