import unittest

print("Jan Thierry B Enriquez")

def fun(x):

    return x+1

class MyTest(unittest.TestCase):

    def test(self):
        self.assertEqual(fun(4),5)

if __name__== '__main__':

    unittest.main()

