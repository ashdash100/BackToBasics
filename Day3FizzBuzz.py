# Day 3 - 4/2
def FizzBuzz(n):
  """ Given an integer n, return a string array of length n
  :param n: Input parameter for length of array
  :return: Array of length n
  :rtype: List[str]
  """
  A = []
  for i in range(n):
    i = i + 1
    if (i % 5 == 0) & (i % 3 == 0):
      A.append("FizzBuzz")
    elif i % 5 == 0:
      A.append("Buzz")
    elif i % 3 == 0:
      A.append("Fizz")
    else:
      istr = str(i)
      A.append(istr)
  return A

test1 = FizzBuzz(9)
test2 = FizzBuzz(16)
test3 = FizzBuzz(1)
print(test1)
print(test2)
print(test3)
