# from uuid import uuid4
# from pprint import pprint
#
# categories = {
#     '30a838c9-06b8-4729-87a5-728fe0ef6f5a': {
#         'name': 'Boxing Gloves',
#         'description': 'Boxing Gloves'
#     },
#     'a5896084-e737-4356-ba5f-729065f82f90':{
#         'name': 'Hand Wrap',
#         'description': 'Hand Wrap'
#     }
# }

#
# while True:
#     process = input('Type a process name: ')
#
#     match process:
#         case 'create':
#             categories[str(uuid4())] = {
#                 'name': input('Name: '),
#                 'description': input('Desciption: ')
#             }
#             pprint(categories)
#         case 'list':
#             pprint(categories)
#         case 'update':
#             category_id = input('Id: ')
#             name = input('Name: ')
#             description = input('Description: ')
#
#             categories.update({
#                 category_id: {
#                     'name': name,
#                     'description': description
#                 }
#             })
#             pprint(categories)
#         case 'delete':
#             category_id = input('Id: ')
#             del categories[category_id]
#             pprint(categories)
#         case _:
#             print('Please type a vaid process..!')



# from requests import get
# from pprint import pprint
#
# endpoint = 'https://newsapi.org/v2/everything?q=tesla&from=2025-01-23&sortBy=publishedAt&apiKey=47f3419f49864ca889f632677d485de1'
# response = get(url=endpoint)
# data = response.json()
# # pprint(data)
#
# print(f'Author: {data.get("articles")[0].get("author")}')
# print(f'Title: {data.get("articles")[0].get("title")}')
# print(f'Content: {data["articles"][0]["content"]}')
#
# # Kullanıcıdan yazar ismi alalım bu yazarın makalesini ekrana basalım
# author_name = input('Author Name: ')
# for article in data['articles']:
#     if article['author'] == author_name:
#         pprint(article)


# Custom Function
# Declare Function
# def function_name():
    # business logic

# call a function - execute function
# function_name()


# def greeting_people(name: str):
#     print(f'Merhaba {name}')
#
# greeting_people(name='burak')
# greeting_people(name='hakan')
# greeting_people(name=input('Type name: '))


# def sum(x: int, y: int) -> None:
#     """
#     This function sum give two numbers
#     :param x: must be integer
#     :param y: must be integer
#     :return:
#     """
#     print(f'{x} + {y} = {x + y}')
#
# sum(x=5, y=3)
# sum(
#     x=int(input('Sayı: ')),
#     y=int(input('Sayı: '))
# )

# def sum(x: int, y: int) -> int:
#     """
#     This function sum give two numbers
#     :param x: must be integer
#     :param y: must be integer
#     :return: integer
#     """
#     return x + y
#
# result = sum(x=5, y=3)
# print(f'Toplam: {result}')

# Fonksiyon yazarken düşünülmesi gereken hususlar
# SOC - Seperation of Concern
# SRP - Single Responsibilty Principle


# kullanıcıdan alınan 3 tane sayıyı toplayan ve karesini alan fonksiyonları yazın
# from math import pow
# def toplama(s1: int, s2: int, s3: int) -> int:
#     return s1 + s2 + s3
#
# def kuvvet_hesapla(toplam: int, kuvvet: int) -> float:
#     return pow(toplam, kuvvet)
#
# result = toplama(
#     s1=int(input('Sayı: ')),
#     s2=int(input('Sayı: ')),
#     s3=int(input('Sayı: '))
# )
#
# main_result = kuvvet_hesapla(
#     toplam=result,
#     kuvvet=int(input("Kuvvet: "))
# )
#
# print(f'Sonuç: {main_result}')

# lst = [12, 11, 19, 20, 15]
# lst_1 = []
# lst_2 = []
#
# def cift_tek_mi(sayi: int) -> str:
#     if sayi % 2 == 0:
#         return 'çift'
#     else:
#         return 'tek'
#
# def append_list(result: str, sayi: int) -> None:
#     if result == 'çift':
#         lst_1.append(sayi)
#     else:
#         lst_2.append(sayi)
#
# def main():
#     for sayi in lst:
#         sonuc = cift_tek_mi(sayi=sayi)
#         append_list(result=sonuc, sayi=sayi)
#     print(lst_1)
#     print(lst_2)
#
# main()


# rakamlar = [1, 1, 5, 4, 5, 3, 3, 1, 2, 5, 2, 1, 2, 3, 2, 1, 1]
#
# def frequency_count(numbers: list) -> dict:
#     frequnency_dict = {}
#
#     for item in numbers:
#         if item in frequnency_dict:
#             frequnency_dict[item] += 1
#         else:
#             frequnency_dict[item] = 1
#
#     return frequnency_dict
#
# print(frequency_count(numbers=rakamlar))


# kullanıcıdan bir söz öbeği alalım
# sample input --> merhaba ben burak merhaba burak
# sample output --> merhaba ben burak
# def remove_dublicate_word(sentence: str) -> str:
#     temper_lst = []
#     for item in sentence.split(" "):
#         if item not in temper_lst:
#             temper_lst.append(item)
#
#     result = ' '.join(temper_lst)
#
#     return result
#
# print(remove_dublicate_word(sentence='merhaba ben burak merhaba burak'))



from uuid import uuid4
from pprint import pprint

categories = {
    '30a838c9-06b8-4729-87a5-728fe0ef6f5a': {
        'name': 'Boxing Gloves',
        'description': 'Boxing Gloves'
    },
    'a5896084-e737-4356-ba5f-729065f82f90':{
        'name': 'Hand Wrap',
        'description': 'Hand Wrap'
    }
}

def create_category(name: str, description: str) -> dict:
    categories[str(uuid4())] = {
        'name': name,
        'description': description
    }

    return categories

def update_category(category_id: str, name: str, description: str) -> dict:
    categories.update({
        category_id: {
            'name': name,
            'description': description
        }
    })

    return categories

def delete_category(category_id: str) -> dict:
    del categories[category_id]

    return categories

while True:
    process = input('Type a process name: ')

    match process:
        case 'create':
            pprint(create_category(name='UFC Gloves', description='UFC Gloves'))
        case 'list':
            pprint(categories)
        case 'update':
            pprint(update_category(category_id='a5896084-e737-4356-ba5f-729065f82f90', name='Protective Equipment', description='Protective Equipment'))
        case 'delete':
            pprint(delete_category(category_id='a5896084-e737-4356-ba5f-729065f82f90'))
        case _:
            print('Please type a vaid process..!')
