from wsgiref import headers

import requests

def get():
    for i in range(1, 50):
        cena = 30000
        otvet = ''
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Origin': 'https://www.wildberries.ru',
            'Referer': f'https://www.wildberries.ru/catalog/0/search.aspx?page={i}&sort=popular&search=4060+rtx&xsubject=3274',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        params = {
            'TestGroup': 'no_test',
            'TestID': 'no_test',
            'appType': '1',
            'curr': 'rub',
            'dest': '-1257786',
            'page': '1',
            'query': '4060 rtx',
            'resultset': 'catalog',
            'sort': 'popular',
            'spp': '29',
            'suppressSpellcheck': 'false',
            'xsubject': '3274',
        }

        response = requests.get('https://search.wb.ru/exactmatch/ru/common/v4/search', params=params, headers=headers).json()

    print(response)

    for product in response['data']['products']:
        if product['salePriceU'] > cena:
            if product['salePriceU'] > 4.5:

                cena = product['salePriceU']

                otvet = str(product['salePriceU']) + '|' + str(product['name']) + '|' + str(product['id'])

    return otvet

print(get())
