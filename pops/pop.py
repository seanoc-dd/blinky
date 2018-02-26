import datetime
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
        pickup_response = requests.post('http://blinky.seanoc.com/tests/client/{}/pickup'.format(process_id))

        if pickup_response.status_code != 200:
            print r.status_code
            print r.text
            time.sleep(30)
            continue

        task = pickup_response.json()
        start = datetime.datetime.now()
        target_response = requests.get(task['target'], timeout=30)
        duration = datetime.datetime.now() - start

        drop_off_response = requests.post(
            'http://blinky.seanoc.com/tests/tasks/{}/drop-off'.format(task['task_id']),
            data={
                'result_ms': duration.total_seconds() * 1000,
                'result_status_code': target_response.status_code,
            }
        )

        if drop_off_response.status_code != 200:
            time.sleep(30)
