import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You finish breakfast")

def coffee():
    time.sleep(4)
    print("You drank coffee")

def study():
    time.sleep(5)
    print("You finished studying")

x=threading.Thread(target=eat_breakfast,args=())
x.start()

y=threading.Thread(target=coffee,args=())
y.start()

z=threading.Thread(target=study,args=())
z.start()

x.join()
y.join()
z.join()

#eat_breakfast()
#coffee()
#study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())