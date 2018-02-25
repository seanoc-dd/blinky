import os
import time

import requests

if __name__ == '__main__':
    zone = os.environ['ZONE']
    r = requests.post('http://blinky.seanoc.com/pops/{}/register'.format(zone))
    if r.status_code != 200:
        print r.status_code
        print r.text
        exit(2)

    process_id = r.json()['id']
    while True:
        print "{}|{}".format(zone, process_id)
        time.sleep(30)
