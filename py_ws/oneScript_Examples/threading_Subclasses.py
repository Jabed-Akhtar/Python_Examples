"""
 ******************************************************************************
 * @author     : Jabed-Akhtar (github)
 * @Created on : 03.09.2022
 ******************************************************************************
 * @file       : threading_Subclasses.py
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

class MyThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print("----->> Started thread:", self.name)
        print_epoch(self.name, self.delay)
        print("----->> Ended thread:", self.name)

if __name__ == "__main__":
    t1 = MyThread("Thread-1", 1)
    t2 = MyThread("Thread-2", 1)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Threading finished/Done!")


# ****************************** END OF FILE **********************************