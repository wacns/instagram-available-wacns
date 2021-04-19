import requests
import time
import random
import os
from os import environ
req = requests.session()
token = str(environ['token'])
chatid = str(environ['chatid'])


def start():
    while True:
        letters = 'qwertyuiopasdfghjklzxcvbnm1234567890._'
        amount = int(1)
        length = int(4)
        for password in range(amount):
            password = ''
            for _ in range(length):
                password = ''
            for _ in range(length):
                password += random.choice(letters)
            else:
                def instagram():
                    try:
                        urlinsta = f'https://www.instagram.com/{password}'
                        headerinsta = {
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'ar',
                            'cookie': 'ig_did=08E27925-1200-4E6B-96E3-E9AA60063843; csrftoken=drY4wJ2FsukngNVssEQbMVcuaxFJa0qz; mid=YD95AAALAAHuCfP9LG-YYl5-WyFG; ig_nrcb=1',
                            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-fetch-dest': 'document',
                            'sec-fetch-mode': 'navigate',
                            'sec-fetch-site': 'none',
                            'sec-fetch-user': '?1',
                            'upgrade-insecure-requests': '1',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
                        }
                        send = req.get(urlinsta, headers=headerinsta)
                        if send.status_code == 404:
                            telegram = f"""
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
-️ NEW AVAILABLE *INSTAGRAM*
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
- USER: *{password}*
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
CHANNEL: @wacnss
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
"""
                            urltel = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatid}&text={telegram}&parse_mode=MARKDOWN"
                            send = req.post(urltel)
                        else:
                            pass
                    except:
                        pass
                instagram()

                def snapchat():
                    try:
                        hi = list(password)
                        if hi[0] == '.' or hi[length-1] == '.' or hi[0] == '_' or hi[length-1] == '_':
                            letters = 'qwertyuiopasdfghjklzxcvbnm1234567890'
                            amount = int(1)
                            length = int(4)
                            for password in range(amount):
                                password = ''
                                for _ in range(length):
                                    password = ''
                                for _ in range(length):
                                    password += random.choice(letters)
                            urlsnap = f'https://accounts.snapchat.com/accounts/get_username_suggestions?requested_username={password}&xsrf_token=_W2GHDQLlCXbXPlWAMuOeQ'
                            headersnap = {
                                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
                                "Accept": "/",
                                "Accept-Language": "en-US,en;q=0.5",
                                "Referer": "https://accounts.snapchat.com/",
                                "Cookie": "xsrf_token=_W2GHDQLlCXbXPlWAMuOeQ; sc-cookies-accepted=true; web_client_id=b1e4a3c7-4a38-4c1a-9996-2c4f24f7f956; oauth_client_id=c2Nhbg==",
                                "Connection": "keep-alive",
                                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                            }
                            send = req.post(urlsnap, headers=headersnap)
                            if "TAKEN" in send.text:
                                telegram = f"""
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
-️ NEW AVAILABLE *SNAPCHAT*
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
- USER: *{password}*
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
CHANNEL: @wacnss
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
"""
                                urltel = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatid}&text={telegram}&parse_mode=MARKDOWN"
                                send = req.post(urltel)
                            else:
                                pass
                        else:
                            urlsnap = f'https://accounts.snapchat.com/accounts/get_username_suggestions?requested_username={password}&xsrf_token=_W2GHDQLlCXbXPlWAMuOeQ'
                            headersnap = {
                                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
                                "Accept": "/",
                                "Accept-Language": "en-US,en;q=0.5",
                                "Referer": "https://accounts.snapchat.com/",
                                "Cookie": "xsrf_token=_W2GHDQLlCXbXPlWAMuOeQ; sc-cookies-accepted=true; web_client_id=b1e4a3c7-4a38-4c1a-9996-2c4f24f7f956; oauth_client_id=c2Nhbg==",
                                "Connection": "keep-alive",
                                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                            }
                            send = req.post(urlsnap, headers=headersnap)
                            if "TAKEN" in send.text:
                                telegram = f"""
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
-️ NEW AVAILABLE *SNAPCHAT*
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
- USER: *{password}*
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
CHANNEL: @wacnss
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
"""
                                urltel = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatid}&text={telegram}&parse_mode=MARKDOWN"
                                send = req.post(urltel)
                            else:
                                pass
                    except:
                        pass
                snapchat()

                def tiktok():
                    try:
                        hi = list(password)
                        if hi[0] == '.' or hi[length-1] == '.':
                            letters = 'qwertyuiopasdfghjklzxcvbnm1234567890'
                            amount = int(1)
                            length = int(4)
                            for password in range(amount):
                                password = ''
                                for _ in range(length):
                                    password = ''
                                for _ in range(length):
                                    password += random.choice(letters)
                            urltik = f'https://www.tiktok.com/@{password}?'
                            headertik = {
                                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'ar',
                                'cookie': 'bm_sz=D629F4942531777D6F7147A73605EDCB~YAAQhVQqLrT8ldN3AQAAvY4T+ArC4uvjnuxrV9pt2l0rKHkp1yqSFyVmqphzleo0kRsXlfI+NbB+LOM88S46yTNKJFjRIpTtPq9rKwsrBBAAkfcyq8+RZH7/Zf6msaZJtLNn/zxAtwnratRpub7m5xD5rufF7yyEZj5G5HxIutar/qCFiClDrwMZN4g39vBR; tt_webid_v2=6935404800675710465; tt_webid=6935404800675710465; tt_csrf_token=FHAWXV6vFZXlSM2eXSRS_6r1; MONITOR_WEB_ID=6935404800675710465; R6kq3TV7=AGOZE_h3AQAArT8QptQP5vh_zveCf-y5-BiUgB0w7IMZfUWedXYgJcIz57M8|1|0|75dd6b518f206372e6d404294a187c94b8126b35; s_v_web_id=verify_kltf64da_CijHZlfi_FdX3_4WE8_9Wwj_IAzVIICoeMBw; csrf_session_id=b2c399a35aae464682b040c14d913de2; bm_mi=DA047E87F2170B8EAEED36DFA89B7EEF~bFZTXUHt/x7P3I0BVhrEb4Td9L8oZ2GpyXZfW+xchO9i3D+JVDz88ASSnmIDwoAj9eNBEr2CRBfBybeh1gzxhUQkMpaXPauZmHFnxobirm+t2tUztvSHjRe7wVmEAzher5o6mgZFo3yICvGZj7Gl0DyAKf9IiMHUCT+P8WchaRo1zn2Tw+i7zcYmVNPFfKCWvBcFurSr7yHOl1W8DBZeM4NciHkWUQ4ZfRSnka5nPBc31710HS6gQL31mYIk5MCC2YzSf89SGSJodJGAkp1fZA==; bm_sv=7C1373BFC9FD4E0464B305E04E391F85~zYvKe8AvrP//Bh3yGBkN9hPkGyzM7JmwI5oyhbcxUHmMaMVX7A54ASSE97V9odLFyKW4B+RTI+2G3FqAeKElYXB+bw5DGu2vwRq89tI2ByGHuHWfJNmJPt+MLaUA1zVjxulAySr/HmXVp82syg2Hct0OfKH5FotWYANjWbWlwVU=; ak_bmsc=546A35303DC5B1DC24F699698FF233DC2E2A54854E2B0000EF813F605E1F4B1A~plMbX0Ui2pNYPSS/i1qPeHNc2xCUddsUFoAOF7Gbmm02GwXrVhn+fZfkeLsnlVZk33Fr4MD6SaesEjx/FclzePXXzOhSiJQ2GdQ996OpIB8lX+kjgVtkeQBXxQ139Neumt8jckA7jT81sgEzIDOZmLO6/KSDSaK95vwDjYEALYND6n9oYpmykVu2KGQYzRg6WueWyO0OrXSINNYmdYO7SF8ktYdO0didVcLX8JwAsFOIli2c6Ou6lhvuvoQeJClQQg; _abck=16220A303EE334985E7B40A39E10EC7F~0~YAAQhVQqLgT9ldN3AQAAwyUV+AUdqGmQv3CIqQnIyXwZFxf1lLyDf3M0i4kSrb/oGfOh9haoEWo2QxMzarNFIHPVzvja0C0ozETE+OS5CBaAx9+79ehyau7EX/wo3QgpVs1CS4v3sh0hclzVhl5LlwXtkCE3e3RCdvbNHXJiBpRf/+MD9HGuPlG1Ns83Auxj/eN8lMXLP3lQng/5xGgcDwXlNWO97iimgzB7FFhMa8cvLh5+7ua4P5HQ3T6O2WJAZZHsqK58z/u1W8NjeSUXh0dqrerPIc10L2hIcOpo6dGkFdG/SX/n9oqWpS4O8A3V640cN3rXoCb9JQFJZBrdRV/qJcpLt2ZdHby+/Igbtq1TFf6CD55L6DCvH8Q1pb1qA8z2zv9Rx1xyiXTnsYwY/YxCqyQrMPvK~-1~||-1||~-1',
                                'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-fetch-dest': 'document',
                                'sec-fetch-mode': 'navigate',
                                'sec-fetch-site': 'none',
                                'sec-fetch-user': '?1',
                                'upgrade-insecure-requests': '1',
                                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
                            }
                            send = req.get(urltik, headers=headertik)
                            if send.status_code == 404:
                                telegram = f"""
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
-️ NEW AVAILABLE *TIKTOK*
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
- USER: *{password}*
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
CHANNEL: @wacnss
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
"""
                                urltel = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatid}&text={telegram}&parse_mode=MARKDOWN"
                                send = req.post(urltel)
                            else:
                                pass
                        else:
                            urltik = f'https://www.tiktok.com/@{password}?'
                            headertik = {
                                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'ar',
                                'cookie': 'bm_sz=D629F4942531777D6F7147A73605EDCB~YAAQhVQqLrT8ldN3AQAAvY4T+ArC4uvjnuxrV9pt2l0rKHkp1yqSFyVmqphzleo0kRsXlfI+NbB+LOM88S46yTNKJFjRIpTtPq9rKwsrBBAAkfcyq8+RZH7/Zf6msaZJtLNn/zxAtwnratRpub7m5xD5rufF7yyEZj5G5HxIutar/qCFiClDrwMZN4g39vBR; tt_webid_v2=6935404800675710465; tt_webid=6935404800675710465; tt_csrf_token=FHAWXV6vFZXlSM2eXSRS_6r1; MONITOR_WEB_ID=6935404800675710465; R6kq3TV7=AGOZE_h3AQAArT8QptQP5vh_zveCf-y5-BiUgB0w7IMZfUWedXYgJcIz57M8|1|0|75dd6b518f206372e6d404294a187c94b8126b35; s_v_web_id=verify_kltf64da_CijHZlfi_FdX3_4WE8_9Wwj_IAzVIICoeMBw; csrf_session_id=b2c399a35aae464682b040c14d913de2; bm_mi=DA047E87F2170B8EAEED36DFA89B7EEF~bFZTXUHt/x7P3I0BVhrEb4Td9L8oZ2GpyXZfW+xchO9i3D+JVDz88ASSnmIDwoAj9eNBEr2CRBfBybeh1gzxhUQkMpaXPauZmHFnxobirm+t2tUztvSHjRe7wVmEAzher5o6mgZFo3yICvGZj7Gl0DyAKf9IiMHUCT+P8WchaRo1zn2Tw+i7zcYmVNPFfKCWvBcFurSr7yHOl1W8DBZeM4NciHkWUQ4ZfRSnka5nPBc31710HS6gQL31mYIk5MCC2YzSf89SGSJodJGAkp1fZA==; bm_sv=7C1373BFC9FD4E0464B305E04E391F85~zYvKe8AvrP//Bh3yGBkN9hPkGyzM7JmwI5oyhbcxUHmMaMVX7A54ASSE97V9odLFyKW4B+RTI+2G3FqAeKElYXB+bw5DGu2vwRq89tI2ByGHuHWfJNmJPt+MLaUA1zVjxulAySr/HmXVp82syg2Hct0OfKH5FotWYANjWbWlwVU=; ak_bmsc=546A35303DC5B1DC24F699698FF233DC2E2A54854E2B0000EF813F605E1F4B1A~plMbX0Ui2pNYPSS/i1qPeHNc2xCUddsUFoAOF7Gbmm02GwXrVhn+fZfkeLsnlVZk33Fr4MD6SaesEjx/FclzePXXzOhSiJQ2GdQ996OpIB8lX+kjgVtkeQBXxQ139Neumt8jckA7jT81sgEzIDOZmLO6/KSDSaK95vwDjYEALYND6n9oYpmykVu2KGQYzRg6WueWyO0OrXSINNYmdYO7SF8ktYdO0didVcLX8JwAsFOIli2c6Ou6lhvuvoQeJClQQg; _abck=16220A303EE334985E7B40A39E10EC7F~0~YAAQhVQqLgT9ldN3AQAAwyUV+AUdqGmQv3CIqQnIyXwZFxf1lLyDf3M0i4kSrb/oGfOh9haoEWo2QxMzarNFIHPVzvja0C0ozETE+OS5CBaAx9+79ehyau7EX/wo3QgpVs1CS4v3sh0hclzVhl5LlwXtkCE3e3RCdvbNHXJiBpRf/+MD9HGuPlG1Ns83Auxj/eN8lMXLP3lQng/5xGgcDwXlNWO97iimgzB7FFhMa8cvLh5+7ua4P5HQ3T6O2WJAZZHsqK58z/u1W8NjeSUXh0dqrerPIc10L2hIcOpo6dGkFdG/SX/n9oqWpS4O8A3V640cN3rXoCb9JQFJZBrdRV/qJcpLt2ZdHby+/Igbtq1TFf6CD55L6DCvH8Q1pb1qA8z2zv9Rx1xyiXTnsYwY/YxCqyQrMPvK~-1~||-1||~-1',
                                'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                                'sec-ch-ua-mobile': '?0',
                                'sec-fetch-dest': 'document',
                                'sec-fetch-mode': 'navigate',
                                'sec-fetch-site': 'none',
                                'sec-fetch-user': '?1',
                                'upgrade-insecure-requests': '1',
                                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
                            }
                            send = req.get(urltik, headers=headertik)
                            if send.status_code == 404:
                                telegram = f"""
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
-️ NEW AVAILABLE *TIKTOK*
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
- USER: *{password}*
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
CHANNEL: @wacnss
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
"""
                                urltel = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatid}&text={telegram}&parse_mode=MARKDOWN"
                                send = req.post(urltel)
                            else:
                                pass
                    except:
                        pass
                tiktok()

                def twitter():
                    try:
                        letters = 'qwertyuiopasdfghjklzxcvbnm1234567890_'
                        amount = int(1)
                        length = int(5)
                        for password in range(amount):
                            password = ''
                            for _ in range(length):
                                password = ''
                            for _ in range(length):
                                password += random.choice(letters)
                        urltwit = 'https://tweeterid.com/ajax.php'
                        headertwit = {
                            'Accept': '/',
                            'Accept-Encoding': 'gzip, deflate, br',
                            'Accept-Language': 'ar',
                            'Connection': 'keep-alive',
                            'Content-Length': '9',
                            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'Cookie': '__utma=116903043.1318232014.1614775995.1614775995.1614775995.1; __utmc=116903043; __utmz=116903043.1614775995.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=116903043.1.10.1614775995; __gads=ID=d7647a854bea65be-22c04e79f1a600a4:T=1614776057:RT=1614776057:S=ALNI_Mbf9fK4B3inAKAT1xrr-qkaEx5NEA',
                            'Host': 'tweeterid.com',
                            'Origin': 'https://tweeterid.com',
                            'Referer': 'https://tweeterid.com/',
                            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                            'sec-ch-ua-mobile': '?0',
                            'Sec-Fetch-Dest': 'empty',
                            'Sec-Fetch-Mode': 'cors',
                            'Sec-Fetch-Site': 'same-origin',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
                            'X-Requested-With': 'XMLHttpRequest'
                        }
                        datatwit = {
                            'input': f'{password}'
                        }
                        send = req.post(
                            urltwit, headers=headertwit, data=datatwit)
                        if 'error' in send.text:
                            telegram = f"""
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
-️ NEW AVAILABLE *TWITTER*
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
- USER: *{password}*
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
CHANNEL: @wacnss
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
"""
                            urltel = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatid}&text={telegram}&parse_mode=MARKDOWN"
                            send = req.post(urltel)
                        else:
                            pass
                    except:
                        pass
                twitter()
        time.sleep(180)


start()
