"""
 ******************************************************************************
 * @author     : Jabed-Akhtar (github)
 * @Created on : 03.09.2022
 ******************************************************************************
 * @file       : threading_example.py
 * @brief      : ---
 ******************************************************************************
 * :Steps      :
 *      1. ---
 * :Descriptions/Infos:
 *      - ---
 ******************************************************************************
"""

# Imports =====================================================================
import threading
import time


def print_epoch(nameThread1, delayTh):
    var_cou = 0
    while var_cou<3:
        time.sleep(delayTh) # delay in second
        var_cou += 1
        print("--->", nameThread1, "----------", time.time())

def print_square(num):
    print("Square = {}".format(num*num))

def print_cube(num):
    print("Square = {}".format(num*num*num))

if __name__ == "__main__":
    t1 = threading.Thread(target=print_epoch, args=("thread-1", 0.5))
    t2 = threading.Thread(target=print_epoch, args=("thread-2", 1))
    t3 = threading.Thread(target=print_square, args=(2, )) # here comma must be pu to make it tuple
    t4 = threading.Thread(target=print_cube, args=(2, )) # here comma must be pu to make it tuple

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print("Threading finished/Done!")


# ****************************** END OF FILE **********************************