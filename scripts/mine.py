import sys
import time

import requests

from app.conf.config import NODE_NUMBER

while True:
    time.sleep(10)
    url = 'http://localhost:500' + str(NODE_NUMBER) + '/mine'
    res = requests.get(url)
    print(res.status_code)

    ok_state_codes = [200, 201, 304]

    if res.status_code not in ok_state_codes:
        print(res.status_code)
        sys.exit()
