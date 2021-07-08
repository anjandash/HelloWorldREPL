import os,sys

def max(a,b):
  if a > b:
    return a
  else:
    return b

if __name__ == "__main__":

  a = int(input('Enter first number: '))
  b = int(input('Enter second number: '))

  max_value = max(a,b)
  print("\n****\n")
  print("The greater number is: ", max_value)
