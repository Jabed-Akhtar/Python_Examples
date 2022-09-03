"""
 ******************************************************************************
 * @author     : Jabed-Akhtar (github)
 * @Created on : 03.09.2022
 ******************************************************************************
 * @file       : thread_example.py
 * @brief      : ---
 ******************************************************************************
 * :Steps      :
 *      1. ---
 * :Descriptions/Infos:
 *      - ---
 ******************************************************************************
"""

# Imports =====================================================================
import _thread
import time


#Integers =====================================================================
def print_epoch(nameThread1, delayTh):
    var_cou = 0
    while var_cou<3:
        time.sleep(delayTh) # delay in second
        var_cou += 1
        print("--->", nameThread1, "----------", time.time())

_thread.start_new_thread(print_epoch, ("thread-1", 1))
_thread.start_new_thread(print_epoch, ("thread-2", 3))

# way to wait for thread
#input()
# anotehr way to wait for thread
while 1:
    pass


# ****************************** END OF FILE **********************************