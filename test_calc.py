def line_break(x):
    print(str(x) + '---------' + str(x) + '---------' +
          str(x) + '---------' + str(x) + '---------')


lb = line_break

'''
~appendix
* this is the first of the six notes on python unit testing *
~lb(0): import unittest module and module-to-test
~lb(1): running unitttest through the command line
~lb(2): pedantics of unittest nomenclature (ran 0 test)
~lb(3): what if unittest fails?

'''

# n.b. the naming convention for when creating unit testing modules is 'test_<name of module to test>'

# first, import the unittest module
# (which does not need additional install since it's included in the standard library)
import unittest

# also import the module you want to test (which is named 'calc.py'):
import calc

# n.b. you can import calc here since the test_calc.py and calc.py are in the same directory.

lb(1)
# now you need to create some test cases for the functions you want to test.
# in order to create those test cases, you first need to create a test class that inherits from unittest.testcase

# you can name the class whatever you want it to, though keep it as descriptive as possible:

# inheriting from the unittest.TestCase will give you a lot of different capabilities within that class. (refer to line D)
class TestCalc(unittest.TestCase):

    def test_add(self):  # refer to line A, line B
        result = calc.add(10, 5)  # refer to line C
        self.assertEqual(result, 15)  # refer to line E


if __name__ == '__main__':  # refer to line F
    unittest.main()
# line A: to write your first test, write a method. n.b. naming convention 'test_' is required*
# *when you run this method, the 'test_' nomenclature sets apart which methods represent tests.
# i.e. if the method does not start with 'test_', it won't be run

# line B: first, you'll just test the add function of the unittest_module.
# like any method, you will pass in the self argument.

# line C: you can run the add() function of the calc module by setting it to the e.g. 'result' variable
# and you would expect the 'result' variable to equal 15. (since the add function will add 10 and 5 together)

# line D: *since you inherited from unittest.TestCase, you have access to all the assert methods
# you're going to use assert.equal() method inherited from unittest.TestCase to test the add function.

# line E: to test whether the add() function did set the 'result' variable to 15,
# use self.assertEqual(result, 15), which means you are asserting whether 'result' is indeed 15 or not.


lb(1)
# now, how do you run this test?
# you could do it from the command line;
# once you are sure that you are in the same current directory as calc.py and test_calc.py,
# (a shortcut to this is to go to the directory (e.g. Unit Testing Tutorials), right-click, select 'New Terminal at Folder'

# type 'python -m unittest test_calc.py' to run unittest as your main module and pass in test_calc
# returns:
'''

/Users/jinyoungchoi/Desktop/self_development/Programming/Python/Corey Schafer Python Beginner Tutorials/Unit Testing Tutorials
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

'''

# this output interprets to 'everything passed'.
# now it would be nice if you could run your test typing 'python test_calc.py' and just running the module,
# instead of using the longer command, 'python -m unittest test_calc.py' .

# and setting it up to run that way instead would allow you to run your test from directly within your editor.
# to do this, refer to line F.
# FYI- if you want to understand what '__main__' is doing; this is not related to unittesting at all.
# basically it's just saying that if you run this directly, it should run the code unittest.main() in the conditional
# that unittest.main() should run all of our tests!

# once you save the new codes (on line F), build, and you can return to the command line,
# and run 'python test_calc.py' directly.
# n.b. this also means that you can now run the test directly from the editor! :-)

lb(2)
# OK- so, as the output indicates, you are only running 1 test.

# remember that the test has to start with the nomenclature 'test_'?
# see what happens when you modify the name of the test to something that does not follow this rule
# e.g. just 'add(self)' or 'add_test(self)'.

# returns:
'''
----------------------------------------------------------------------
Ran 0 tests in 0.000s
OK

'''
# now, when you run this, you will not notice right off the bat that anything is wrong,
# because, after all, you didn't get any Errors or warnings.
# but if you look at how many tests ran, it says '0'.
# n.b. you have to be careful that all of your tests are named properly and start with the word 'test_'

lb(3)
# now, what happens if your test fails?
# change the value within self.assertEqual() (referred to in line E) to 14 instead of 15
# so that your test of adding 10 and 5 fails.

# returns:
'''
F
======================================================================
FAIL: test_add (__main__.TestCalc)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_calc.py", line 43, in test_add
    self.assertEqual(result, 14)  # refer to line E
AssertionError: 15 != 14
----------------------------------------------------------------------
Ran 1 test in 0.001s
FAILED (failures=1)

'''

# # # # # # # # # # # # # # # # continue onto test_calc2.py # # # # # # # # # # # # # # # #
