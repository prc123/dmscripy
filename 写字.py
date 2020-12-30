
import requests
import urllib.parse
import re
from turtle import *

headers = {
    'authority': 'bihua.51240.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac'
                  ' OS X 10_14_0) AppleWebKit/537.36'
                  ' (KHTML, like Gecko) Chrome/84.'
                  '0.4147.105 Safari/537.36',
    'dnt': '1',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://bihua.51240.com/',
    'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
    'cookie': '__gads=ID=658c828707dd0499:T=1595998724:S=ALNI_MZ6bsw6q1nu1qsbMrUf73nv50vfxw; '
              'BAIDU_SSP_lcr=https://www.baidu.com/link?url=SXNjkUiTyzcsX7f1yrBwTjsy8mJmkaLnMv'
              'vfHPMFi7vXJueYvk5Sc1vKwnVXf4Se&wd=&eqid=d9851dee00006859000000055f26ece8; Hm_lv'
              't_fbe0e02a7ffde424814bef2f6c9d36eb=1595998724,1596386543; c_y_g_j=bihua%2Cjing'
              'weidu; Hm_lpvt_fbe0e02a7ffde424814bef2f6c9d36eb=1596386739',
}

def editHeaders(authority,pragma,cache-control,user-agent)：

def gen_url_encode_words(words):
    source = ''
    for i in range(len(words)):
        _data = words[i]
        if i == 0:
            source = urllib.parse.quote(_data).replace("%", '').lower()
        else:
            source = source + '$' + urllib.parse.quote(_data).replace("%", '').lower()
    return source


def setting():  # 参数设置
    pensize(4)
    hideturtle()
    colormode(255)
    color((250, 0, 0), "red")
    speed(1)

def painworld(str):
    target_words = str
    params = (
        ('font', gen_url_encode_words(target_words)),
        ('shi_fou_zi_dong', '0'),
        ('cache_sjs1', '20031908'),
    )

    response = requests.get('https://bihua.51240.com/web_system/51240_com_www/system/file/bihua/get_0/',
                            headers=headers,
                            params=dict(params)
                            )

    content = response.content.decode('utf-8')

    content = content.replace('hzbh.main(', '').split(');document.getElementById')[0]
    content = content.split('{')[-1].split("}")[0]
    pattern = re.compile(r'\w:\[(.+?)\]')
    result1 = re.split(pattern, content)
    print(result1)
    words_order_list = {}
    words_cnt = 0
    for r in result1:
        sec = re.findall(r'\'.+?\'', r)
        if len(sec):
            orders = sec[1].split('#')
            order_xy_routine = []
            for order in orders:
                order_str = re.findall(r'\(\d+,\d+\)', order)
                order_xy = [eval(xy) for xy in order_str]
                order_xy_routine.append(order_xy)
            words_order_list['{}_{}'.format(words_cnt, target_words[words_cnt])] = order_xy_routine
            words_cnt += 1
    setting()  # 画布、画笔设置
    right_shift = 0
    down_shift = 0
    print(words_order_list)
    for k, v in words_order_list.items():
        for lines in v:
            pu()
            for xy in lines:
                x, y = xy
                x, y = x * 0.2 - 400 + right_shift * 200, -y * 0.2 + 250 - down_shift * 200
                goto(x, y)
                pd()
        right_shift += 1
        if right_shift % 4 == 0:
            down_shift += 1
            right_shift = 0
    done()

if __name__ == '__main__':
    
    painworld("求关注")