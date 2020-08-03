def line_break(x):
    print(str(x) + '---------' + str(x) + '---------' +
          str(x) + '---------' + str(x) + '---------')


lb = line_break

'''
~appendix
* this is the sixth of the six notes on python unit testing *
~lb(0): intro. to mocking
~lb(1): importing patch from the mock library
~lb(2): using patch as context manager
~lb(3): mock objects record call date and call value
~lb(4): using patch as context manager to test for failed response
~lb(5): best practices when unit testing (test-driven dev)

'''
import unittest
from employee import Employee

from unittest.mock import patch  # refer to line A

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('JinYoung', 'Choi', 50000)
        self.emp_2 = Employee('Fredrick', 'Thompson', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'JinYoung.Choi@email.com')
        self.assertEqual(self.emp_2.email, 'Fredrick.Thompson@email.com')

        self.emp_1.first = 'Brian'
        self.emp_2.first = 'Varun'

        self.assertEqual(self.emp_1.email, 'Brian.Choi@email.com')
        self.assertEqual(self.emp_2.email, 'Varun.Thompson@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'JinYoung Choi')
        self.assertEqual(self.emp_2.fullname, 'Fredrick Thompson')

        self.emp_1.first = 'Brian'
        self.emp_2.first = 'Varun'

        self.assertEqual(self.emp_1.fullname, 'Brian Choi')
        self.assertEqual(self.emp_2.fullname, 'Varun Thompson')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):  # refer to line B
        with patch('employee.requests.get') as mocked_get:  # refer to line C
            mocked_get.return_value.ok = True  # refer to line D
            mocked_get.return_value.text = 'Success'  # refer to line E

            schedule = self.emp_1.monthly_schedule('August')  # refer to line F
            mocked_get.assert_called_with(  # refer to line G
                'http://company.com/Choi/August')
            self.assertEqual(schedule, 'Success')  # refer to line H

            mocked_get.return_value.ok = False  # refer to line I

            schedule = self.emp_2.monthly_schedule('June') #refer to line J
            mocked_get.assert_called_with(  # refer to line K
                'http://company.com/Thompson/June')
            self.assertEqual(schedule, 'Bad Response!') #refer to line L

if __name__ == '__main__':
    unittest.main()


lb(0)
# there is just one more thing that covered on unit testing that is important to know.

# sometimes your code relies on certain things that you have no control over.
# e.g. say you have a function that goes to a website and pullsdown some information.
# now, if that website is down, your function will fail and, by default, your test fails.
# this isn't what you want, because you only want your test to fail only when something is wrong with *your* code.
# so if a website is down, there is nothing that you can actually do about that.

# you're going to get around this problem with something called 'mocking'.
# there's a lot that could be looked at with regards to mocking
# but let's take a look at some examples of some basic usage.

# pasted in a sample method into the original employees.py module
# whereby this method goes into a company's website and pulls down an employee's schedule for a given month.

# now, if the response is ok, you want to return the text of that response.
# if the response is not ok, you want to return the text 'Bad Response!':

# # # sample method in employees.py # # #
'''
def monthly_schedule(self, month):
        response = requests.get(
            f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'
'''
# # # end of sample method in employees.py # # #

lb(1)
# so the information from that website is something that you would want to mock
# because you don't want the success of your test to depend on that website being up.

# i.e. you only care that the .get() method was called with the correct URL
# and that your code behaves correctly whether the response is ok or not ok.

# Line A: to do this, you need to import something from mock called 'patch'. (import at the top of module)

lb(2)
# now there are couple of different ways to use patch:
# you can use patch either as a decorator or as a context manager.

# patch will allow you to mock an object during a test
# and then that object is automatically restored after the test is run.

# Line B: let's create a new test for that monthly schedule method.
# in this example, you will use patch as a context manager.
# Line C: you want to mock the request.get method of the employee module, so you pass that into with patch(),
# and then you are setting that equal to mocked_get: .

# you may wander why you didn't just import requests into your test and mock that instead of the employee.requests.
# but you want to mock these objects where they're actually used.
# so, given that, requests is actually used in this employee module,
# employee.requests.get is what we want to mock.

# now, when requests.get is run in the employee.py module,
# it's actually going to use your 'mocked_get' variable here instead of the regular requests.get method.

# you can just assign the return value instead of actually going out to the website.
# if you look back at this sample method within the employee.py module,
# you want that return value to have an '.ok' of True.
# Line D: so you can test a successfull call by saying 'mocked_get.return_value.ok' = True'

# Line E: let's also set the text of that return value (mocked_get.return) equal to something like 'Success'.

# so if you look back at the employee.py module, if it returns ok as True (if response.ok:),
# then you should get your response.text back (return response.text).

# now, within your context manager,
# Line F: let's just run your monthly_schedule method just as you were testing it.

lb(3)
# now, one more awesome thing about these mock objects
# is that they actually record when they were called and with what values.

# so you want to make sure that the .get() method was called with the correct URL.
# Line G: to do this, use assert_called_with() which is just a method of that mocked object
# and test whether it was called with the correct URL.

# given that in the employee.py module, the URL format was 'http://company.com/{self.last}/{month}',
# pass in the expected URL to be called when you check for emp_1 (JinYoung Choi)'s schedule of August

# after you know that the method was called with the correct URL,
# Line H: make sure that it returned the correct text (which you set to 'Success')
# by self.asserting that the response (schedule) was equal to 'Success'.

#after saving and running TestEmployee now,
#returns: (selected last few lines of output)
'''
...
----------------------------------------------------------------------
Ran 4 tests in 0.001s
OK

'''
#you can see that it ran four tests and that they all passed.

lb(4)
#ok now, the last thing is that you want to test the failed response.

#to do this, you can just do the exact same thing (i.e. paste the code from lb(3) or from Lines D to H)
#Line I: except to modify 'True' to 'False' so as to test for a bad response from the website
#and if that ok value isn't True, then your monthly_schedule function should just return the string 'Bad Response'

#Line J: and just to switch up the second test a bit, let's change your emp here to emp_2 (i.e. Fredrick Thompson),
#and change the month to 'September' just to make the test a bit better.

#Line K: now the get() method should be called with the URL of Thompson and September.

#Line L: and lastly, instead of your result equaling 'Success', change it to 'Bad Response'

#and now, if you run Test_Employee,
#returns: (selected last few lines of output)
'''

----------------------------------------------------------------------
Ran 4 tests in 0.002s
OK

'''
#you can see that all of your tests are still passing.

#to conclude, this mocking can be a little bit confusing when you first see it,
#but you don't use it a whole lot, unless you are accessing things like URLs,
# and things that are basically out of your control.

#so you don't use it a lot but whenever you do need it, it's definitely nice to know!

lb(5)
#before ending this note, it's important to cover some best practices when unit testing.

#first of all, Tests should be *isolated*.
#meaning that each test *should not* rely on other tests or affect other tests.
#i.e. you should be able to run any test *by itself*, independent from other tests!

#secondly, in this series of notes, you were adding tests to existing code
# (from test_calc to test_calc3, or from test_employee to test_employee3)

#now you may have heard of something called 'test-driven development',
# and basically what this means is that you write the test before you write the code.
# understandably this might sound a bit strange, but sometimes this can be a useful thing to follow.
#the gist of this type of development is:

# that you should think about what you want to do
#then write a test implementing that behavior,
#then watch the test *fail* (since it doesn't actually have any code to run against)
# and then write the code in a way that gets the test to *pass*.

# # # # # # # # # # # # # # # # end of unit testing notes # # # # # # # # # # # # # # # #
