import os
import time

if __name__ == '__main__':
    while True:
        print "{}|{}".format(os.environ['ZONE'], os.environ['LOCATION_NAME'])
        time.sleep(30)
