"""
 ******************************************************************************
 * @author     : Jabed-Akhtar (github)
 * @Created on : 03.09.2022
 ******************************************************************************
 * @file       : closures_example.py
 * @brief      : ---
 ******************************************************************************
 * :Descriptions/Infos:
 *      - ---
 ******************************************************************************
"""

import logging
logging.basicConfig(filename='logs/tmplog.log', level=logging.INFO)

def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function

#my_func = outer_function()
#print(my_func.__name__)

hi_func = outer_function('Hi')
hello_func = outer_function('Hello')

hi_func()
hello_func()

# **********************************************
def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with argument {}'.format(func.__name__, args))
        print(func(*args))
    return log_func

def add(x, y):
    return x+y

def sub(x, y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
sub_logger(10, 5)

if __file__ == "__main__":
    pass


# ****************************** END OF FILE **********************************