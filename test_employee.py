def line_break(x):
    print(str(x) + '---------' + str(x) + '---------' +
          str(x) + '---------' + str(x) + '---------')


lb = line_break

'''
~appendix
* this is the fourth of the six notes on python unit testing *
~lb(0): unittesting a more complicated program (class Employee)
~lb(1): how did test_employee do?
~lb(2): is DRY compatible with unit testing?
~lb(3): setUp() and .tearDown() methods
~lb(4): looking through setUp() once more.

'''
lb(0)
# now you'll proceed to how you would write some tests for a more complicated program-
# the Employee class from OOP notes (refer to employee.py within this directory!).

# similarly with the unittest for calc, begin by importing unittest module and by importing employee!
# note, in employee.py, specifically import the Employee class
# (unlike calc whereby the module had public functions (instead of being encapsulated within a Calc class))

import unittest
from employee import Employee

# then create your test case that inherits from unittest.testcase

class TestEmployee(unittest.TestCase):

    def setUp(self):  # refer to line G
        self.emp_1 = Employee('JinYoung', 'Choi', 50000)  # refer to line I
        self.emp_2 = Employee('Fredrick', 'Thompson', 60000)

    def tearDown(self):  # refer to line H
        pass

    def test_email(self):  # refer to line A
        # refer to line B
        self.assertEqual(self.emp_1.email, 'JinYoung.Choi@email.com')
        self.assertEqual(self.emp_2.email, 'Fredrick.Thompson@email.com')

        self.emp_1.first = 'Brian'  # refer to line C
        self.emp_2.first = 'Varun'

        # refer to line D
        self.assertEqual(self.emp_1.email, 'Brian.Choi@email.com')
        self.assertEqual(self.emp_2.email, 'Varun.Thompson@email.com')

    def test_fullname(self):  # refer to line E
        self.assertEqual(self.emp_1.fullname, 'JinYoung Choi')
        self.assertEqual(self.emp_2.fullname, 'Fredrick Thompson')

        self.emp_1.first = 'Brian'
        self.emp_2.first = 'Varun'

        self.assertEqual(self.emp_1.fullname, 'Brian Choi')
        self.assertEqual(self.emp_2.fullname, 'Varun Thompson')

    def test_apply_raise(self):  # refer to line F
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


if __name__ == '__main__':
    unittest.main()

# Line A: your first test is called test_email, which creates two employees, emp_1 and emp_2.
# and when these emp_s are created you should immediately be able to access the email property

# Line B: so you check both of their emails to check that you are getting both of the expected values.

# Line C: and then you are changing their first names

# Line D: and checking their email again since their email properties should have changed accordingly.

# Line E: now you are testing the fullname() function similar to the above test for email().

# Line F: lastly, you have a test for testing the apply_raise() function here, whereby you are creating the two emp's
# and then running the function on them (i.e. applying a raise that is, by default, 5%),
# and testing to make sure that the pay was raised by 5% for each emp.

lb(1)
# so this is basically just a slightly more complicated test than your test_calc,
# and there isn't anything here that you haven't seen yet.
# after all, you just have three different tests, and have some assertEqual's in here,
# to make sure that things have the values that you expect.

# so if you run this test_employee.py module:
# returns:
'''

...
----------------------------------------------------------------------
Ran 3 tests in 0.000s
OK

'''

lb(2)
# now, one thing that you might notice is that at the beginning of every one of these tests,
# you are creating two emp's [emp_1 = Employee('JinYoung', 'Choi', 50000); emp_2 = Employee('Fredrick', 'Thompson')]

# anytime you see the same code over and over,
# there should be something that pops out to you because usually programmers try to make their code DRY*
#*DRY: Do not Repeat Yourself.

# the reason for keeping it DRY is that if anything ever changes with these two setup emp's here,
# then you'll need to make changes to every single test where you created these employees.

# now, this might not be a big deal when we have three test like this,
# but if you have hundreds, it could be a pain to maintain.

lb(3)
# i.e. it would be nice if you could create these from scratch in one place and reuse them for every test.
# that's what the setup() and teardown() methods are for!

# so at the top of your TestEmployee class,
# Line G: let's create two new methods, setUp()
# Line H: and tearDown().
# n.b. these methods are camelcased, with the uppercase U and uppercase D, so be sure to type correctly.

# the setUp() method will run its code *before* every single test.
# and the tearDown() method will run its code *after* every single test.

# e.g. you wanted to create the employees *before* every single test.
# so grab the [emp_1 = Employee('JinYoung', 'Choi', 50000); emp_2 = Employee('Fredrick', 'Thompson', 60000)]
# Line I: and paste it here within the setUp() method.
# in order to access these from within your other tests, set emp_1 and emp_2 as instance attributes
# (i.e. self.emp_1 and self.emp_2)

# now that you have these within your setUp() method,
# you can delete the creation of these emp's from the beginning of all three of these tests.

# since those are instance attributes, everywhere you reference emp_1 and emp_2,
# *you need to add the self to the beginning.*

lb(4)
# now, one more time, let's go ahead and look through what you did with the setUp() method.
# within the setUp, you're creating emp_1 and emp_2, and it's going to create these emps before every single test.

# e.g. so now, here within your test_email(self), you're saying self.assertEqual equals--
# and make sure that this emp you created up in the setUp()-- this email ('JinYoung.Choi@email.com')
# and you can reuse the same emp_s for every single one of these tests,
# whereby the emp_s get created anew for every single one of these tests.

# # # # # # # # # # # # # # # # continue onto test_employee2.py # # # # # # # # # # # # # # # #
