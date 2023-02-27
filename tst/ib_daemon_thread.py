import threading
import time


def number_generator():
    for a in range(30):
        print(a)
        time.sleep(1)


def greeting():
    for i in range(4):
        print("Hello")
        time.sleep(1)


thr2 = threading.Thread(target=number_generator)  # creating a separate thread to execute the NumGen function
thr2.daemon = True  # defining the thread as daemon
thr2.start()  # start execution of NumGen function on the parallel thread
greeting()
