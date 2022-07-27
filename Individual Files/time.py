import time

def sleep():
    time.sleep(2)

start = time.time()
sleep()
end = time.time()
t = end-start
print(t)
