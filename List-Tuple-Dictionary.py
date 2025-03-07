# kullanıcıdan bir söz öbeği alalım. bu söz öbeğinde ki sesli harflari ve sessiz harflari farklı listelere ekleyelim
# bir eklenen harf bir daha eklenmesin.
# word = input('Please type something: ').lower()
#
# sesli_harfler_listesi = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']
#
# sesli_harf = []
# sessiz_harf = []
# # sample input --> bu_Rak yi?lAz
# for c in word:
#     if c.isalpha():
#         if c in sesli_harfler_listesi:
#             if c not in sesli_harf:
#                 sesli_harf.append(c)
#         else:
#             if c not in sessiz_harf:
#                 sessiz_harf.append(c)
#
# print(f'Sesli Harfler: {sesli_harf}\n'
#       f'Sessiz Harfler: {sessiz_harf}')



# from string import punctuation
# users = ['doğa_ özgür_', '2eren uysal', ' görkem', 'burak yılmaz', 'mete   yaman', 'hakan kagan yılmaz', ' ', '_idil ', 'kerim abdul cabbar hüseyin']
# # burak.yilmaz@outlook.com
# mail_address = []
#
# for user in users:
#     if user not in ' ':
#         user_names = user.split(' ')
#         for item in user_names:
#             if item == '':
#                 user_names.remove(item)
#         if len(user_names) >= 2:
#             for i in range(len(user_names)):
#                 for c in user_names[i]:
#                     if c.isdigit():
#                         user_names[i] = user_names[i].replace('2', '')
#                     if c in punctuation:
#                         user_names[i] = user_names[i].replace('_', '')
#             mail_address.append(f'{user_names[0]}.{user_names[-1]}@outlook.com')
#
# print(f'Mail Address: {mail_address}')



# List Comprehansion
# lst = [i for i in range(10)]
# print(lst)
#
# print([i * i for i in range(10)])
#
# odd_power = [i * i for i in range(10) if i % 2 == 0]
# print(odd_power)



# Tuple (Demetler)

# tuple_1 = ('Fenerbahçe', 'Galatasaray', 'Adana Demirspor', 'Beşiktaş', 'Trabzonspor')
# tuple_2 = ('Eagels', 'Red Skins', 'Sea Hawk', 'Patrios')
# tuple_3 = tuple_1 + tuple_2
# print(tuple_3)
#
# # Dilimleme (Slicing)
# print(tuple_3[0:5])  # output: ('Fenerbahçe', 'Galatasaray', 'Adana Demirspor', 'Beşiktaş', 'Trabzonspor')
# print(tuple_3[2:4])  # output: ('Adana Demirspor', 'Beşiktaş')
# print(tuple_3[::2])  # output: ('Fenerbahçe', 'Adana Demirspor', 'Trabzonspor', 'Red Skins', 'Patrios')
# print(tuple_3[-1])   # output: 'Patrios'
# print(tuple_3[::-1]) # output: ('Patrios', 'Sea Hawk', 'Red Skins', 'Eagels', 'Trabzonspor', 'Beşiktaş', 'Adana Demirspor', 'Galatasaray', 'Fenerbahçe')
# print(tuple_3[::-3]) # output: ('Patrios', 'Eagels', 'Adana Demirspor')
# print(tuple_3[4::-2]) # output: ('Trabzonspor', 'Adana Demirspor', 'Fenerbahçe')
# print(tuple_3[4::2]) # output: ('Trabzonspor', 'Red Skins', 'Patrios')
#
#
# tuple_4 = (
#     'Sarıyer',
#     ('Suadiye', 'Erenköy'),
#     ('Yeniköy', 'Bebek', ('Etiler', 'Ulus'))
# )
# print(tuple_4[2])
# print(tuple_4[1][1])
# print(tuple_4[2][2][0])
#
# my_family = [
#     ('Burak Yılmaz', 36, 'beast'),
#     ('Hakan Yılmaz', 39, 'bear'),
#     ('İpek Yılmaz', 41, 'keko'),
# ]
#
# for name, age, alias in my_family:
#     print(f'Name: {name}\n'
#           f'Age: {age}\n'
#           f'Alias: {alias}')



# Dictionary
# Key-Value mantığında çalışan başka bir yapıdır.

# movie_release_year = {
#     'Fight Club': 1999,
#     'The Matrix': 1999,
#     'Interstaller': 2008,
#     'Inception': 2010,
#     'Dune': 2023
# }
#


# # Read
# print(movie_release_year['Fight Club'])
# print(movie_release_year.get('Fight Club'))
#
# for key in movie_release_year.keys():
#     print(key)
#
# for value in movie_release_year.values():
#     print(value)
#
# for key, value in movie_release_year.items():
#     print(f'Key: {key} - Value: {value}')
#
# # Create
# movie_release_year['Openheimer'] = 2023
# print(movie_release_year)
#
# # Update
# movie_release_year.update({
#     'Interstaller': 2014
# })
# print(movie_release_year)
#
# # delete
# del movie_release_year['Openheimer']
# print(movie_release_year)
#
# # CRUD (Create - Read - Update - Delete)
#
# my_dict = {
#     'Full Name': 'Burak YIlmaz',
#     'Age': 36,
#     'Interestes Sports': ('Boxing', 'Wrestling', 'UFC'),
#     'Favorite Books': {
#         'History': 'Cabmidge War History',
#         'Scientific': {
#             'Karl Poper': ['The Logic of Scientific Discovery']
#         }
#     }
# }


# products = [
#     {'name': 'Apple Iphone Pro Max 16', 'price': 99000},
#     {'name': 'Lenovo x1 Carbon', 'price': 89000},
#     {'name': 'Apple Macbook Pro', 'price': 145000},
#     {'name': 'Asus Zenbook', 'price': 100000},
#     {'name': 'Samsung s25', 'price': 80000},
# ]
#
# # product listesinde ki her bir ürün fiyatının toplamını bulalım
# total = 0
# for item in products:
#     total += item.get('price')
#
# print(f'Total Price: {total}')
#
# # fiyatı 100000'den büyük olan ürünleri listeleyelim
# for product in products:
#     if product['price'] >= 100000:
#         print(f'Name: {product["name"]}\n'
#               f'Price: {product["price"]}')
#
# # ürün adı içerisinde Apple geçen ve price 80000'den büyük olan ürünleri listelelim
# for product in products:
#     if "Apple" in product['name'] and 80000 <= product['price'] <= 150000:
#         print(f'Name: {product["name"]}\n'
#               f'Price: {product["price"]}')

