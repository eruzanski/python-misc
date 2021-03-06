# -*- coding: utf-8 -*-
"""Computing Running Statistics from STDIN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18XZ5vEJ_la98Wz5pkQWXrlLUScJ0RGFu

Hello,

Thank you for completing the assessments.

The next step is to complete the coding challenge for Robert, our lead Instructor, to review.

Coding Challenge

Write a program that reads a list of numbers and for each number outputs an estimate of the running mean, running standard deviation, and running median.  The input should be read from standard in, with one number per line.  For each line of input, the program should print to standard out the estimated running mean, running standard deviation, and running median.  That is, given the input

1

2

3

137.036

 

the program should output values close to

 

1,0,1

1.5,0.5,1.5

2,0.816,2

35.759,58.477,2.5

 

Some notes:

Using either the biased or unbiased estimate of the standard deviation is fine, but you should report a number even for the first step.
There are several ways to define the median for an even number of samples; you may use any of these definitions.
Output numbers at a reasonable precision.
 

You will probably have to strike a balance between the accuracy of the results and  resources your program requires.  Choose a sensible tradeoff.  Better yet, allow this to be configurable.

 

Ideally, this program should be able to handle arbitrarily long lists of inputs.  It would be nice for it to output results as soon as possible, instead of needing to wait for all of standard in to be read.  You do not have to worry about malicious input (there won’t be 10 GB on a single line), but gracefully handling malformed input lines is a plus.

 

Upload your solution to the public DVCS host of your choice, and send us a link to the repository.  You may use any programming language or packages you like, but if you use anything outside of Python 3, Pandas, or Numpy, please include instructions to help us run your code.

 

Thank you,
"""

from collections import deque
import math
import numpy as np

class RunningStatistics:

    def __init__(self, max_med_samples=10000, sd_type='unbiased'):
        self.n = 0
        self.old_mean = 0
        self.new_mean = 0
        self.old_std = 0
        self.new_std = 0
        self.med_q = deque(maxlen=max_med_samples)
        self.sd_type = sd_type
    
    def clear(self):
        self.n = 0
        self.med_q.clear()
    
    def push(self, x):
        self.n += 1
    
        # For mean and standard deviation
        if self.n == 1:
            self.old_mean = self.new_mean = x
            self.old_std = 0
        else:
            self.new_mean = self.old_mean + (x - self.old_mean) / self.n
            self.new_std = self.old_std + (x - self.old_mean) * (x - self.new_mean)
        
            self.old_mean = self.new_mean
            self.old_std = self.new_std
        
        # For median
        self.med_q.append(x)

    def mean(self):
        return self.new_mean if self.n else 0.0

    def standard_deviation(self):
        if self.sd_type=='unbiased':
          return math.sqrt(self.new_std / (self.n - 1)) if self.n > 1 else 0.0
        else:
          return math.sqrt(self.new_std / (self.n)) if self.n > 1 else 0.0

    def median(self):
        return np.median(self.med_q)

rs = RunningStatistics(1000,'biased')
display_dec_places = 4

while True:

  # Prompt and get user input (one value at a time)
  input_val = input("Enter a numeric value (or type q to exit): ")
  
  # Break on specified input value
  if input_val=='q':
    break

  # Check input value for proper type, ignore if not  
  try:
    input_num = float(input_val)
  except:
    continue
  
  # Check input value for NaN or +/-Inf, ignore if so
  if math.isnan(input_num) or math.isinf(input_num):
    continue
  
  # Do the computations
  rs.push(input_num)

  # Return the result
  print(np.round(rs.mean(), display_dec_places),
         np.round(rs.standard_deviation(), display_dec_places),
         np.round(rs.median(), display_dec_places))

