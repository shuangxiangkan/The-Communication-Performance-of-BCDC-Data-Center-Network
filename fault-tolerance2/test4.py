import time


try:
    while True:
        time.sleep(1)
        print("1")
except KeyboardInterrupt:
    print("2")
