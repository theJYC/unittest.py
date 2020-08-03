def line_break(x):
    print(str(x) + '---------' + str(x) + '---------' +
          str(x) + '---------' + str(x) + '---------')


lb = line_break

'''

~appendix
~lb(0): intro. to unittesting

'''

'''
testing will help you save a lot of time and headache down the road.
when you write good tests for your code,
it gives you more confidence that your updates and refactoring
won't have any unintended consequences or break your code in any way

e.g. if you update your function in your project,
those changes may have broken several sections of your code even if that function itself is still working.

a good unit test will show that everything is working as it should,
and if not, it will show you exactly what is broken.

in this repository you're going to learn everything you need to know
to get started with the built-in unittest module.
'''

# we have a script below of some simple functions:
# they are intentionally simple so that you can focus on what their tests look like.


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y


lb(0)
# typically, people just use print() statements to check if the function is working:
# print(add(5, 10))
# returns: 15 , i.e. your add() function is working as it should, since the output (15) looks right.

# but testing your code this way is not easy to automate and its also hard to maintain.
# if you're testing a lot of different functions,
# there is no way for you to see at a glance what failed and what succeeded.

# that's where unit testing comes in.

# to do unit tests, you need to create a test module (i.e. new file dedicated to unittesting a given function).
#(test_calc.py file was created and will be referenced side-by-side)
