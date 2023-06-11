"""
 ******************************************************************************
 * @author     : Jabed-Akhtar (github)
 * @Created on : 03.09.2022
 ******************************************************************************
 * @file       : threading_ThreadSynchronizationUsingLocks.py
 * @brief      : ---
 ******************************************************************************
 * :Descriptions/Infos:
 *      - ---
 ******************************************************************************
"""

# Imports =====================================================================
import threading

x = 0

def thread_task(lock):
    global x
    for i in range(100000): # when 10->100000 -> lead to problem
        lock.acquire() # locking for not allowing anotehr trhead to do anything
        x += 1
        lock.release() # releasing to let another thread do the task

def main_task():
    lock = threading.Lock()

    t1 = threading.Thread(target=thread_task, args=(lock, ))
    t2 = threading.Thread(target=thread_task, args=(lock, ))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__":
    main_task()
    print("{0}".format(x))


# ****************************** END OF FILE **********************************