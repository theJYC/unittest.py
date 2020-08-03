def line_break(x):
    print(str(x) + '---------' + str(x) + '---------' +
          str(x) + '---------' + str(x) + '---------')


lb = line_break

'''
~appendix
* this is the second of the six notes on python unit testing *
~lb(0): optimising the unittest assertEqual() method
~lb(1): writing more test methods per function
~lb(2): changing your original program- did it break the code?
~lb(3): yes, it did break the code
~lb(4): ...did it?

'''
import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)  # refer to line A
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)  # refer to line D
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)  # refer to line E
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)  # refer to line F
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)  # refer to line G


if __name__ == '__main__':
    unittest.main()

lb(0)
# previously, the test_add(self) method was:

'''
def test_add(self):
    result = calc.add(10,5)
    self.assertEqual(result, 15)

'''

# now, to optimise test_add(),
# drop the calc.add(10,5) function directly into the assert statement (refer to line A)

lb(1)
# when unittesting, you usually want to also check some edge cases.
# so, let's copy and paste self.assertEqual(calc.add(10, 5), 15) a couple of times, and test for them.

# one edge case might be one negative number and one positive number.
# let's make sure that the add() function for -1 and 1 equals to 0, (refer to line B)
# and two negative numbers may be another edge case. i.e. adding -1 and -1 to equal to -2 (refer to line C)

# now, once you save and run it, it's saying that it passed, but also saying that it 'Ran 1 test' still.
# n.b. you may have been expecting this to output 'Ran 3 tests',
# but really, these 3 assert methods are just within 1 single test called 'test_add()'.

# even though the output still says it 'Ran 1 test', you still made this test better by adding in these additional tests.
# n.b. it's not your goal to write as many tests as possible,
# but just make sure that you write 'good' tests.

lb(2)
# in order to then write more tests, you just have to add in test methods.
# let's test the rest of your calc functions

# line D: to begin with, writing the test method for the subtract() function
#(copying and pasting the test_add() method and just modifying the second argument of self.assertEqual!)

# line E: test for the multiply() function of calc module similarly to add() and subtract()
# line F: test for the divide() function of the calc module too...

# now, if you save and run it,
# returns:
'''

....
----------------------------------------------------------------------
Ran 4 tests in 0.000s
OK

'''
# notice the four dots on top of the dotted line, and that it 'Ran 4 tests'
# i.e. all four of the tests passed with all of those assertEqual statements.

# you can imagine how useful this is;
# if you have a module with some complicated functions, then once you put in the work to write good test like this
# you can just come back and rerun this test to make sure everything still works


lb(3)
# n.b. so if you change something in your program that you think will work but actually broke some stuff-
#-your test should catch that.

# e.g. if you were to go back to the original calc.py module and within the multiply() function,
# add another asterisk to 'return x * y' (so, 'return x ** y'),

# when you run the unittest again
# returns:
'''

..F.
======================================================================
FAIL: test_multiply (__main__.TestCalc)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/jinyoungchoi/Desktop/self_development/Programming/Python/Corey Schafer Python Beginner Tutorials/Unit Testing Tutorials/test_calc2.py", line 33, in test_multiply
    self.assertEqual(calc.multiply(10, 5), 50)  # refer to line E
AssertionError: 100000 != 50
----------------------------------------------------------------------
Ran 4 tests in 0.001s
FAILED (failures=1)

'''
# notice the '..F.' on top of the dashed line; this means one test(i.e. test_multiply()) failed,
# while the other 3 tests ran successfully.

# and for the test that failed, it says that 10 ** 5 should have been 100000, not 50.
# this gives us the idea of exactly where the problem is,
# and where you can make that change to make the test pass again.

lb(4)
# now, sometimes you might make a change that might not break your test but will unexpectedly break your code.

# e.g. if you go back to the original calc.py module and within the divide() function:
# accidently write an extra '/' to 'return x / y' (so 'return x // y')
#(which will do a floor division instead of regular division)
# fyi-- floor division is almost the same as regular division except that it doesn't give you the remainder

# even though the change occurred, your current test_divide() won't catch this
# because right now, all of the divisions that were checked as edge cases come out to whole numbers anyways.
# so it doesn't matter if you're using floor division or regular division.

# correspondingly, if you save that change and run the unit test again
# returns:
'''

....
----------------------------------------------------------------------
Ran 4 tests in 0.000s
OK

'''
# you can see that currently all of these tests are passing.

# let's say that at some point that floor division broke your program,
# and after some debugging you traced it back to that and found the problem.

# now, in that case, it's always a good practice to go update your test
# with a test that would have caught the problem you just found.
# that way, you can know that you don't revisit the same bugs over and over.

# line G: a test that would have caught this bug would be the assert statement
# whereby 5 divided by 2 would equal to 2.5, and not equal to 2.

# so now, if you run the unit test again (note: not having corrected the floor div. problem in original module)
# returns:
'''

.F..
======================================================================
FAIL: test_divide (__main__.TestCalc)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/jinyoungchoi/Desktop/self_development/Programming/Python/Corey Schafer Python Beginner Tutorials/Unit Testing Tutorials/test_calc2.py", line 41, in test_divide
    self.assertEqual(calc.divide(5, 2), 2.5)  # refer to line G
AssertionError: 2 != 2.5
----------------------------------------------------------------------
Ran 4 tests in 0.001s
FAILED (failures=1)

'''
# you can see that you got an AssertionError using that floor division,
# that 5 / 2 should have been 2 (and that 2 != 2.5)

# # # # # # # # # # # # # # # # continue onto test_calc3.py # # # # # # # # # # # # # # # #
