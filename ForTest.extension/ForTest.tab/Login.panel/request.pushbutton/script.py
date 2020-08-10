#! python3

import requests
r = requests.get('https://github.com/user', auth=('user', 'pass'))
print(r.status_code)