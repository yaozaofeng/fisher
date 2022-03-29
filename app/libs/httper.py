# 开发时间： 2022/3/27 $ 12:05

# urllib - python自带
# requests

import requests

class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code  != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
