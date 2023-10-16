import configuration
import requests
import data

def post_products_kits(body):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


response = post_new_user(data.user_body);
print(response.status_code)

response = post_products_kits(data.product_ids);
print(response.status_code)
print(response.json())
