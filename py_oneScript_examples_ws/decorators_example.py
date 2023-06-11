# !!! to be continued -> see link in description.
"""
 ******************************************************************************
 * @author     : Jabed-Akhtar (github)
 * @Created on : 03.09.2022
 ******************************************************************************
 * @file       : decorators_example.py
 * @brief      : ---
 ******************************************************************************
 * :Descriptions/Infos:
 *      - link: https://youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc
 ******************************************************************************
"""

def outer_function(msg):
    def inner_function():
        print(msg)

    return inner_function # returning without () returns function waiting to be executed later

hi_func = outer_function('Hi')
bye_func = outer_function('Bye')
hi_func() # only now message 'Hi' will be printed
bye_func()

# ***********************************************************
def decorator_func(orig_func):
    def wrapper_func(*args, **kwargs):
        print('wrapper executed this before {}.'.format(orig_func.__name__))
        return orig_func(*args, **kwargs)
    return wrapper_func

@decorator_func
def display():
    print('Display function!')

# The below two lines is same as using @<function-name> before function as above
#decorated_disp = decorator_func(display)
#decorated_disp()
# The below is enough when using decorator
display()

@decorator_func
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Sams', 25)

# Classes as decorator (same as fuction as decorator) *******************
class decorator_class(object):
    def __init__(self, orig_func):
        self.orig_func = orig_func

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.orig_func.__name__))
        return self.orig_func(*args, **kwargs)

@decorator_class
def display():
    print('Display function!')

@decorator_class
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Sam2', 42)

if __file__ == "__main__":
    pass


# ****************************** END OF FILE **********************************