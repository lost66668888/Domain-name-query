import requests
import json
from tqdm import tqdm
import time
import random

headers = {
    "authority": "gm.mmstat.com",
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "content-type": "text/plain;charset=UTF-8",
    "origin": "https://wanwang.aliyun.com",
    "referer": "https://wanwang.aliyun.com/domain/searchresult/?keyword=1234567&suffix=.xyz",
    "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
}

# 请将你的浏览器Cookie字符串粘贴到这里
cookie_str = "填写在这里"

def parse_cookie_string(cookie_str):
    cookies = {}
    for item in cookie_str.split(';'):
        if '=' in item:
            key, value = item.strip().split('=', 1)
            cookies[key] = value
    return cookies

cookies = parse_cookie_string(cookie_str)

input_file = '查询.txt'
output_file = 'ok.txt'

with open(input_file, 'r', encoding='utf-8') as f:
    numbers = [line.strip() for line in f if line.strip()]

with open(output_file, 'a', encoding='utf-8') as f_out:
    for idx, number in enumerate(tqdm(numbers, desc='查询进度')):
        domain = f"{number}.xyz"
        url = f"https://checkapi.aliyun.com/check/v2/search?umidToken=Y2f5fd3e930532a56a9de1115c75026a5&sceneId=MainCheckPCScene&keyword={domain}"
        try:
            resp = requests.get(url, headers=headers, cookies=cookies, timeout=10)
            data = resp.json()
            domains = data.get('data', {}).get('panels', {}).get('premiums', {}).get('domains', [])
            for d in domains:
                price_info = d.get('extendInfo', {}).get('domainPrice', {})
                if (
                    price_info.get('avail') is True and
                    str(price_info.get('price')) == '7' and
                    price_info.get('productType') == 2
                ):
                    f_out.write(domain + '\n')
                    f_out.flush()
                    tqdm.write(f"OK: {domain}")
                    break
        except Exception as e:
            tqdm.write(f"Error processing {domain}: {e}")
            tqdm.write(f"程序终止，最后处理到的域名是: {domain} (第{idx+1}行)")
            break
        time.sleep(random.uniform(1.5, 3.5))
