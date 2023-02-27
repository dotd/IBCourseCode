import threading
import numpy as np
import time


def random_number_generator():
    for a in range(5):
        print(np.random.randint(1, 1000))
        time.sleep(1)


thr2 = threading.Thread(target=random_number_generator)  # creating a separate thread to execute the randNumGen function
thr2.start()  # start execution of randNumGen function on the parallel thread


def greeting():
    for i in range(5):
        print("Hello")
        time.sleep(1)


greeting()
