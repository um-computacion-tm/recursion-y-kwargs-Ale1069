import unittest
def fibonacci(n):
    if n in (0,1):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_1(self):
        resultado = fibonacci(1)
        self.assertEqual(resultado, 1)

    def test_fibonacci_2(self):
        resultado = fibonacci(2)
        self.assertEqual(resultado, 1)
    
    def test_fibonacci_3(self):
        resultado = fibonacci(3)
        self.assertEqual(resultado, 2)

    def test_fibonacci_4(self):
        resultado = fibonacci(4)
        self.assertEqual(resultado, 3)
    
    def test_fibonacci_5(self):
        resultado = fibonacci(5)
        self.assertEqual(resultado, 5)
    
    def test_fibonacci_6(self):
        resultado = fibonacci(6)
        self.assertEqual(resultado, 8)
    
    def test_fibonacci_7(self):
        resultado = fibonacci(7)
        self.assertEqual(resultado, 13)

unittest.main()


