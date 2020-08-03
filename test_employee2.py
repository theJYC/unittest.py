def line_break(x):
    print(str(x) + '---------' + str(x) + '---------' +
          str(x) + '---------' + str(x) + '---------')


lb = line_break

'''
~appendix
* this is the fifth of the six notes on python unit testing *
~lb(0): exploring the tearDown() method
~lb(1): exploring the @classmethods: setUpClass and tearDownClass

'''
import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod  # refer to line B
    def setUpClass(cls):
        print('setUpClass')

    @classmethod  # refer to line C
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')  # refer to line A
        self.emp_1 = Employee('JinYoung', 'Choi', 50000)
        self.emp_2 = Employee('Fredrick', 'Thompson', 60000)

    def tearDown(self):
        print('tearDown\n')  # refer to line A

    def test_email(self):
        print('test_email')  # refer to line A
        self.assertEqual(self.emp_1.email, 'JinYoung.Choi@email.com')
        self.assertEqual(self.emp_2.email, 'Fredrick.Thompson@email.com')

        self.emp_1.first = 'Brian'
        self.emp_2.first = 'Varun'

        self.assertEqual(self.emp_1.email, 'Brian.Choi@email.com')
        self.assertEqual(self.emp_2.email, 'Varun.Thompson@email.com')

    def test_fullname(self):
        print('test_fullname')  # refer to line A
        self.assertEqual(self.emp_1.fullname, 'JinYoung Choi')
        self.assertEqual(self.emp_2.fullname, 'Fredrick Thompson')

        self.emp_1.first = 'Brian'
        self.emp_2.first = 'Varun'

        self.assertEqual(self.emp_1.fullname, 'Brian Choi')
        self.assertEqual(self.emp_2.fullname, 'Varun Thompson')

    def test_apply_raise(self):
        print('test_apply_raise')  # refer to line A
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


if __name__ == '__main__':
    unittest.main()

lb(0)
# up until this point, you were not making use of the tearDown() method,
# but say that you wanted to test some functions that added files to a directory or to a database

# in your setUp() method, you could create the test directory or the test datatbase to hold those files,
# and in your tearDown method, you can delete all of those so you have a clean slate for the next test.

# note: for demonstration of tearDown() method,
# Line A: the test_employee module has been modified to include print statements (e.g. print('setUp'/tearDown/test_email))
# throughout your code.
# so if you go ahead and run test_employee2.py:
# returns:
'''
setUp
test_apply_raise
tearDown

setUp
test_email
tearDown

setUp
test_fullname
tearDown

...
----------------------------------------------------------------------
Ran 3 tests in 0.000s
OK

'''
# you can see that you have setUp, then the test, then the tearDown.
# and it does this for every single test.

# n.b. another thing to note here is that the tests *don't necessarily run in order*
# so never assume that the tests run straight down through the script.
# and that's why you need to keep all of your tests isolated from one another.

lb(1)
# now, sometimes it's also useful to have some code run at the very beginning of the testfile,
# and then have some cleanup code that runs after all the tests have been run.

# so, unlike the setUp() and tearDown() that runs after every single test,
# it'd be nice if you have something that ran once before anything and once after everything.

# now you can do this using two @classmethods:
# Line B: setUpclass(cls):
# Line C: and tearDownclass(cls):.

#now, if you save and run this program:
#returns:
'''

setUpClass
setUp
test_apply_raise
tearDown

setUp
test_email
.tearDown

.setUp
test_fullname
tearDown

tearDownClass

'''

#you can see that it runs setUpClass first,
#and then setUp's and tearDown's for each test,
#and finally it runs the tearDownClass.

#i.e. these setUpClass and tearDownClass are very useful if you just want to do something once,
#and it's too costly to do each test.

#e.g. maybe you want to populate a database to run tests against.
#now, as long as you're just reading from the database,
#it might be appropriate to just set this up once in the setUpClass method,
#and then you can tear it down in the tearDownClass method.

# # # # # # # # # # # # # # # # continue onto test_employee3.py # # # # # # # # # # # # # # # #
