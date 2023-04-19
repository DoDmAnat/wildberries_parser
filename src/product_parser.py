import requests


def wb_parser(nm_id: int):
    url_card = f'https://card.wb.ru/cards/detail?nm={nm_id}'
    headers = {'Accept': "*/*",
               'User-Agent': "Chrome/51.0.2704.103 Safari/537.36"}
    response = requests.get(url_card, headers=headers)
    data = response.json()['data']['products']
    if data:
        data = data[0]
        card = {
            "nm_id": nm_id,
            "name": data['name'],
            "brand": data['brand'],
            "brand_id": data['brandId'],
            "site_brand_id": data['siteBrandId'],
            "supplier_id": data['supplierId'],
            "sale": data['sale'],
            "price": data['priceU'],
            "sale_price": data['salePriceU'],
            "rating": data['rating'],
            "feedbacks": data['feedbacks'],
            "colors": data['colors'][0]['name'] if data['colors'] else None
        }
        return card
    return None
