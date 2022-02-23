import unittest
print("Jan Thierry B Enriquez")

def multiply(x,y):

    return x*y

class TestMultiply(unittest.TestCase):

    def test(self):
        self.assertEqual(multiply(3,2), 8)

if __name__== '__main__':

    unittest.main()

