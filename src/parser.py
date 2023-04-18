import requests


def wb_parser(nm_id: int):
    url_card = f'https://card.wb.ru/cards/detail?nm={nm_id}'
    headers = {'Accept': "*/*",
               'User-Agent': "Chrome/51.0.2704.103 Safari/537.36"}
    response = requests.get(url_card, headers=headers)
    data = response.json()['data']['products']
    if data:
        return data[0]
    return None
