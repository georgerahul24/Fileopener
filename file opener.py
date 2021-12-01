import json
import os.path
import pickle
import sys
import time
from threading import Thread

currenttime = None
print("HI")

def reload(path, mode):
    global currenttime
    while True:
        if os.path.getmtime(sys.argv[1]) != currenttime:
            os.system('cls' if os.name == 'nt' else 'clear')
            if mode == 'json':
                with open(path, 'r') as f:
                    print(json.load(f))
            elif mode == 'pickle':
                with open(sys.argv[1], 'rb') as f:
                    print(pickle.load(f))
            else:
                print(open(sys.argv[1], 'r').read())
            currenttime = os.path.getmtime(sys.argv[1])
            print("Press 'Enter' key to exit:")
        time.sleep(5)




try:
    with open(sys.argv[1], 'rb') as f:
        print(pickle.load(f))
        currenttime = os.path.getmtime(sys.argv[1])
        t = Thread(target=reload, args=(sys.argv[1], 'pickle'))

except:
    try:
        with open(sys.argv[1], 'r') as f:
            print(json.load(f))
            currenttime = os.path.getmtime(sys.argv[1])
            t = Thread(target=reload, args=(sys.argv[1], 'json'))

    except:
        print(open(sys.argv[1], 'r').read())
        currenttime = os.path.getmtime(sys.argv[1])
        t = Thread(target=reload, args=(sys.argv[1], 'text'))

finally:
    t.daemon = True
    t.start()

input("Press 'Enter' key to exit:")
