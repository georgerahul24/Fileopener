import json
import os.path
import pickle
import sys
import time
from threading import Thread

currenttime = None


def reload(path, mode):
    global currenttime
    while True:
        if os.path.getmtime() != currenttime:
            os.system('cls' if os.name == 'nt' else 'clear')
            if mode == 'json':
                with open(path, 'r') as f:
                    print(json.load(f))
            elif mode == 'pickle':
                with open(sys.argv[1], 'rb') as f:
                    print(pickle.load(f))
            else:
                print(open(sys.argv[1], 'r').read())
            currenttime = os.path.getmtime()
        time.sleep(30)
        print('Reloading...')


try:
    with open(sys.argv[1], 'rb') as f:
        print(pickle.load(f))
        currenttime = os.path.getmtime(sys.argv[1])
        t = Thread(target=reload, args=(sys.argv[1], 'pickle'))
        t.daemon = True
        t.start()
except:
    try:
        with open(sys.argv[1], 'r') as f:
            print(json.load(f))
            currenttime = os.path.getmtime(sys.argv[1])
            t = Thread(target=reload, args=(sys.argv[1], 'json'))
            t.daemon = True
            t.start()
    except:
        print(open(sys.argv[1], 'r').read())
        currenttime = os.path.getmtime(sys.argv[1])
        t = Thread(target=reload, args=(sys.argv[1], 'text'))
        t.daemon = True
        t.start()

input("Press 'Enter' key to exit:")
