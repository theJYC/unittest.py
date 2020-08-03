def line_break(x):
    print(str(x) + '---------' + str(x) + '---------' +
          str(x) + '---------' + str(x) + '---------')


lb = line_break

'''
~appendix
* this is the third of the six notes on python unit testing *
~lb(0): testing for exceptions via manual argument input
~lb(1): testing for exceptions via context manager

'''
import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        self.assertRaises(ValueError, calc.divide, 10, 0)  # refer to line A

        with self.assertRaises(ValueError):  # refer to line B
            calc.divide(10, 0)  # refer to line C


if __name__ == '__main__':
    unittest.main()

lb(0)
# now, there is one more thing within your calc.py file that you can see--
# that within the divide() method:
'''
def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y
'''

# that you are checking if the number you are dividing by is 0 ('if y == 0'),
# and if so, you are raising a ValueError with the message 'Can not divide by zero!'

# so you'll likely want to check that this expectation is working aswell.
# but this is done a little differently than other assertions.

# in fact there are two ways (note a) and b)) you can implement this test:

# line A: a)type in self.assertRaises(x,y,a,b) whereby x= ValueError (i.e. exception that you expect),
# and y=calc.divide (i.e. the function you want to test),
# and a,b= 10, 0 (i.e. arguments to this assertRaisesmethod)

# told again- the first arg is the exception you expect to be thrown;
#           - the second arg is the function you want to run (leave off the parentheses since you're not passing args)
#           - the third and fourth args are each args you want to pass into the divide function separately

# now the reason that you have to do it this way, instead of running your function normally,
# is because the function will actually throw the ValueError (as you would expect),
# and your test would think something failed.

# when the test is saved and run,
# returns:
'''

....
----------------------------------------------------------------------
Ran 4 tests in 0.000s\
OK

'''
# you can see that this is currently passing, because 10/0 did throw in the ValueError.
# i.e. if you passed in instead 10 / 2, it would NOT have thrown in the ValueError and correspondingly failed the test:
# returns:
'''

.F..
======================================================================
FAIL: test_divide (__main__.TestCalc)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/jinyoungchoi/Desktop/self_development/Programming/Python/Corey Schafer Python Beginner Tutorials/Unit Testing Tutorials/test_calc3.py", line 44, in test_divide
    self.assertRaises(ValueError, calc.divide, 10, 2)  # refer to line A
AssertionError: ValueError not raised by divide
----------------------------------------------------------------------
Ran 4 tests in 0.001s
FAILED (failures=1)

'''
# note: 'AssertionError: ValueError not raised by divide'

lb(1)
# now, the above lb(0) method of testing exceptions is not preferred
# because you would just want to call the function that you test normally,
# instead of passing in all the arguments (x, y, a, b) separately like you're doing here.

# now, you can just call the function that you test normally,
# if you test the exceptions using a context manager.
# context manager would allow you to handle and check the exception properly, while calling your function normally.

# line B: using the backbone of line A, get rid of all arguments apart from the exception to be tested: ValueError
# and write in 'with' before self.assertRaises(), and add the semicolon (:),
# line C: and simply call the function with its arguments- calc.divide(10, 0)
# returns:
'''

....
----------------------------------------------------------------------
Ran 4 tests in 0.000s
OK

'''

# i.e. you can choose whichever lb(0) or lb(1) method you prefer to test exceptions,
# though lb(1) (using context manager) is clearly the winner given its simplicity.

# # # # # # # # # # # # # # # # continue onto test_employee.py # # # # # # # # # # # # # # # #
