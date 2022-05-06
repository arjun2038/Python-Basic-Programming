from threading import *
from time import *
class One(Thread):
    def run(self):
        for i in range(5):
            print(asctime()[11:19],"one")
            sleep(1)
class Two(Thread):
    def run(self):
        for i in range(5):
            print(asctime()[11:19],"two")
            sleep(1)

one=One()
two=Two()

one.start()
sleep(0.2)
two.start()
print(active_count())
one.join()
two.join()
print("done")