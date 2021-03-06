import requests as re

from src.settings import API_URL
import json


def create_tg_user(user):
    print("qwe")
    url = API_URL + f"user/"
    print("qwe")
    data = {
        "user_id": user.id,
        "user_name": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
    }
    response = re.post(url, data=data)
    print("postuser", response.json())
    return response.json()['item']


def create_announce(user, user_id):
    url = API_URL + f"announce/"
    data = {
        "fullname": user["fio"],
        "region": user["reg_id"],
        "phone_number": user['contact'],
        "price": json.dumps(user['price']),
        "description": user['desc'],
        "user": user_id,
        "is_active": True
    }
    response = re.post(url, data=data)
    return response.json()['item']


def create_cat_announce(an, user):
    url = API_URL + f"announce_cat/"
    data = {
        "resume": an['id'],
        "category": user['cat_id']
    }
    response = re.post(url, data=data)
    return response.json()['item']

def edit_announce(id, data):
    url = API_URL + f"announce_edit/{id}"
    response = re.put(url, data)
    print("RESPONSE", response.json()["item"])
    return response.json()["item"]

def get_announce(id):
    url = API_URL + f"announce_one/{id}"
    response = re.get(url)
    return response.json()['item']

def delete_announce(announce_id):
    url = API_URL + f"del_announce/{announce_id}"
    responce = re.delete(url)

    return responce


def search_announcer(id):
    url = API_URL + f"announce/{id}/"
    response = re.get(url)
    print("getu", response)
    return response.json()['item']

def get_user(user_id):
    url = API_URL + f"user/{user_id}/"
    response = re.get(url)
    print("getu", response)
    return response.json()['item']


def get_user_log(user_id):
    url = API_URL + f"log/{user_id}/"
    response = re.get(url)
    print("USER_DATA", response.json())
    return response.json()['item']


def create_log(user_id):
    url = API_URL + f"log/{user_id}/"
    response = re.post(url, data={"user_id": user_id})
    print("post", response)
    return response.json()['item']

def get_user_announce(user_id, page=1):
    url = API_URL + f"announces/{user_id}?page={page}"
    response = re.get(url)
    print('salom1', response)
    return response.json()


def change_log(user_id, log):
    url = API_URL + f"log/{user_id}/"
    response = re.put(url, data={"messages": json.dumps(log)})
    return response.json()['item']


def tgChangeLang(user_id, lang):
    url = API_URL + f"user/{user_id}/"
    data = {
        "lang": lang
    }
    response = re.put(url, data=data)
    print("lang_put", response)
    return response.json()['item']


def userChangeMenu(user_id, menu):
    url = API_URL + f"user/{user_id}/"
    print('url', url)
    data = {
        "menu_log": menu
    }
    response = re.put(url, data=data)
    print("menu_put", response)
    return response.json()['item']


def getRegions():
    url = API_URL + f"g/regions/"
    response = re.get(url)
    response = response.json()['items']
    return response


def getCategory():
    url = API_URL + f"g/category/"
    response = re.get(url)
    return response.json()['items']


def searchCategory(category_name, parent_id=None):
    if parent_id:
        pass
    else:
        url = API_URL + f"g/category/{category_name}"
        response = re.get(url)
        try:
            response = response.json()['item']
        except:
            response = None
        return response


def searchRegion(region_name, region_id=None):
    url = API_URL + f"g/regions/{region_name}"
    response = re.get(url)
    return response.json()['item']

def searchAnnounceMoney(summa):
    url = API_URL + f"announse/data/{summa}"
    response = re.get(url)
    print('qaniku', response)
    return response.json()['items']

def Districts(region_id):
    pass


def district_by_name(name):
    pass
