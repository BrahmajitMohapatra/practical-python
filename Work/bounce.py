# bounce.py
#
# Exercise 1.5
inital_h =100
b=1
while b<=10:
  initial_h = 0.6*initial_h  #3/5 = 0.6
  print(b, round(initial_h,4))
  b = b+1
