# 下面两种方法任选一种
# urllib  可以直接使用，import即可 from urllib import request
# requests 使用要安装第三方库

import requests

class HTTP:
    #url是请求的API的地址
    # get应该是静态方法，给其加上修饰器，此时self参数就不需要了
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        #restful
        #json
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
        # if r.status_code == 200:
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r.text   #不是json格式，只普通的字符串
        # else:
        #     if return_json:
        #         return {}
        #     else:
        #         return ''