"""
Multithreading: One process run in multiple pieces called threads

In python Multithreading is NOT PARALLEL

Python implements lock called GLOBAL INTERPRETER LOCK
which will take care of executing one code at a time

If it is not-parallel or if it is sequential then what is the
use of multithreading in python
- suppose if some thread is waiting for some resource then
during that waiting time, it will execute another thread.
This is advantage of using multithreading
"""

print("Without Using MultiThreading Example-1")
print("-"*20)
# -------------

import time

start_time = time.time()

def squares(my_list):
    for i in my_list:
        print("Square Is:", i*i)


def cube(my_list):
    for i in my_list:
        print("Cube Is:", i*i*i)


L = [10, 20, 30, 40]
squares(L)
cube(L)

end_time = time.time()

print("Time Taken:", end_time-start_time, " seconds")

print("#"*40, end="\n\n")
#########################

print("MultiThreading Example-1")
print("-"*20)
# -------------

import time

start_time = time.time()

def squares(my_list):
    for i in my_list:
        print("Square Is:", i*i)


def cube(my_list):
    for i in my_list:
        print("Cube Is:", i*i*i)


L = [10, 20, 30, 40]

from threading import Thread
my_thread_1= Thread(target=squares, args=(L,))
my_thread_2= Thread(target=cube, args=(L,))

my_thread_1.start()
# It will not wait for my_thread_1 to complete instead
# It will call start() and goto next line
my_thread_2.start()
# It will not wait for my_thread_1 to complete instead
# It will call start() and goto next line

# Make each thread to wait till it completes so that we can find end_time
my_thread_1.join() # wait here till execution of my_thread_1 complete
my_thread_2.join() # wait here till execution of my_thread_2 complete

end_time = time.time()

print("Time Taken:", end_time-start_time, " seconds")

print("#"*40, end="\n\n")
#########################

print("WITH DELAY: Without Using MultiThreading Example-2")
print("-"*20)
# -------------

import time

start_time = time.time()

def squares(my_list):
    for i in my_list:
        print("Square Is:", i*i)
        time.sleep(0.1)


def cube(my_list):
    for i in my_list:
        print("Cube Is:", i*i*i)
        time.sleep(0.1)


L = [10, 20, 30, 40]
squares(L)
cube(L)

end_time = time.time()

print("Time Taken:", end_time-start_time, " seconds")

print("#"*40, end="\n\n")
#########################

print("WITH DELAY: MultiThreading Example-2")
print("-"*20)
# -------------

import time

start_time = time.time()

def squares(my_list):
    for i in my_list:
        print("Square Is:", i*i)
        time.sleep(0.1)


def cube(my_list):
    for i in my_list:
        print("Cube Is:", i*i*i)
        time.sleep(0.1)


L = [10, 20, 30, 40]

from threading import Thread
my_thread_1= Thread(target=squares, args=(L,))
my_thread_2= Thread(target=cube, args=(L,))

my_thread_1.start()
# It will not wait for my_thread_1 to complete instead
# It will call start() and goto next line
my_thread_2.start()
# It will not wait for my_thread_1 to complete instead
# It will call start() and goto next line

# Make each thread to wait till it completes so that we can find end_time
my_thread_1.join() # wait here till execution of my_thread_1 complete
my_thread_2.join() # wait here till execution of my_thread_2 complete

end_time = time.time()

print("Time Taken:", end_time-start_time, " seconds")

print("#"*40, end="\n\n")
#########################