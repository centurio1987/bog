import unittest

def impl1003():
  iterN = int(input())
  for _ in range(iterN):
    pivoNs = int(input())
    print(' '.join(pivonacciCount(pivoNs)))

def pivonacciCount(n):
  #ni + ni+1 = ni+2
  if n == 0:
    return ['1', '0']
  if n == 1:
    return ['0', '1']
  zeroCount = 1
  oneCount = 1
  a = 0
  b = 1
  for i in range(n + 1):
    res = a + b
    a = b
    b = res
    if res == 1:
      oneCount = oneCount + 1
  return [str(zeroCount), str(oneCount)]

def pivonacci(N):
  a0 = 0
  a1 = 1
  an = 0
  for i in range(N+1):
    if i == 0:
      continue
    if i == 1:
      continue
    an = a0 + a1
    a0 = a1
    a1 = an
  return an

class Test1003(unittest.TestCase):
  def test1003(self):
    self.assertEqual(pivonacciCount(10), ['1', '2'])
    # self.assertEqual(pivonacci(6), 5)

if __name__ == '__main__':
  impl1003();