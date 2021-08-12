import unittest;

def implement2739():
  n = int(input())

  for i in range(1, 10):
    print(f'{n} * {i} = {n * i}');

class Test2739(unittest.TestCase):
  def test2739(self):
    print(implement2739())

if __name__ == '__main__':
  unittest.main();