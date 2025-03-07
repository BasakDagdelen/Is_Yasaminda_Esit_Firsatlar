
# Looping
# While - For
# sayac = 0
# while sayac < 10:
#     print(sayac)
#     sayac = sayac + 1


# 0-100 arasında ki sayıların toplamını ekrana yazdıralım.
# sayac = 0
# toplam = 0
# while sayac <= 100:
#     toplam = toplam + sayac # toplam += sayac
#     sayac += 1 # sayac = sayac + 1
#
# print(f'Toplam: {toplam}')


# 0-100 arasında kaç tane çift kaç tane tek sayı varsa bulalım ve ekrana yazdıralım
# sayac = 0
# ciftler = 0
# tekler = 0
# while sayac <= 100:
#     if sayac % 2 == 0:
#         ciftler += 1 # ciftler = ciftler + 1
#     else:
#         tekler += 1  # tekler = tekler + 1
#     sayac += 1
#
# print(f'Cift Sayılar: {ciftler}\n'
#       f'Tek Sayılar: {tekler}')



# while True:
#     try:
#         # '+', '-' etc. yada 'e'
#         process = input('İşlem türü giriniz: ')
#
#         match process:
#             case 'e':
#                 print('Uyguluma kapatılıyor..!')
#                 break  # break deyimi döngüyü durdurur. break altında kalan kodlar çalışmaz
#             case '+':
#                 sayi_1 = int(input('Tam sayı giriniz: '))
#                 sayi_2 = int(input('Tam sayı giriniz: '))
#                 print(f'Toplam: {sayi_1 + sayi_2}')
#             case '-':
#                 sayi_1 = int(input('Tam sayı giriniz: '))
#                 sayi_2 = int(input('Tam sayı giriniz: '))
#                 print(f'Toplam: {sayi_1 - sayi_2}')
#             case '*':
#                 sayi_1 = int(input('Tam sayı giriniz: '))
#                 sayi_2 = int(input('Tam sayı giriniz: '))
#                 print(f'Toplam: {sayi_1 * sayi_2}')
#             case '/':
#                 sayi_1 = int(input('Tam sayı giriniz: '))
#                 sayi_2 = int(input('Tam sayı giriniz: '))
#                 print(f'Toplam: {sayi_1 / sayi_2}')
#             case _:
#                 print(f'Lütfen uygun işlem türünü girin..!')
#     except ZeroDivisionError as err:
#         print(err)
#     except TypeError as err:
#         print(err)
#     except ValueError as err:
#         print(err)



# Kullanıcıdan alınan sayının asal mı değil mi?
# sayi = int(input('Sayı giriniz: '))
#
# if sayi <= 0:
#     print('Negaif tam sayıların asal değeldir..!')
# else:
#     is_prime = True
#
#     if sayi == 1:
#         is_prime = False
#
#     sayac = 2
#     while sayac < sayi:
#         if sayi % sayac == 0:
#             is_prime = False
#             break
#
#         sayac += 1
#
#     if is_prime:
#         print(f'{sayi} asaldır..!')
#     else:
#         print(f'{sayi} asal değildir..!')



# faktoriel hesapla
# sayi = int(input('Sayı giriniz: '))
#
# if sayi < 0:
#     print('Negatif sayıların faktöriyeli hesaplanmaz..!')
# elif sayi == 0 or sayi == 1:
#     print(f"{sayi} faktöriyeli 1'dir")
# else:
#     sonuc = 1
#
#     while sayi > 0:
#         sonuc *= sayi
#         sayi -= 1
#
#     print(f'Sonuc: {sonuc}')



# For Loop
# In & Not In
# print('m' in 'Mike Tyson')
# print('T' in 'Mike Tyson')
#
# # Not In
# print('m' not in 'Mike Tyson')
# print('T' not in 'Mike Tyson')
#
#
# for i in range(10):
#     print(i, end=' ')
# print()
# for i in range(10, 15):
#     print(i, end=' ')
# print()
# for i in range(10, 100, 5):
#     print(i, end=' ')
# print()
# for i in range(10, 1, -1):
#     print(i, end='-')
#
#
# ciftlerin_toplami = 0
# teklerin_toplami = 0
# for sayac in range(100):
#     if sayac % 2 == 0:
#         ciftlerin_toplami += sayac
#     else:
#         teklerin_toplami += sayac
#
# print(f"""
#     Ciftlerin Toplamı: {ciftlerin_toplami}
#     Teklerin Toplamı: {teklerin_toplami}
# """)



# kullanıcıdan başlangıç, bitiş ve adım miktarını alalım. bu aralıkta kalan tam sayıların karesini hesaplayarak ekrana yazdıralım.
# baslangic = int(input('Başlangıç: '))
# bitis = int(input('Bitis: '))
# adim = int(input('Adim: '))
#
# for i in range(baslangic, bitis + 1, adim):
#     print(f'Sonuç: {i ** 2}')



# Nested For
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i} x {j} = {i * j}')
#     print('=======================')

# for i in range(4):
#     for j in range(6):
#         print('X', end=' ')
#     print(' ')

# for i in range(10):
#     for j in range(i):
#         if j <= i:
#             print('X', end=' ')
#     print(' ')



# List
# lst = ['burak', 12, 'b', 23.2, ['hakan', 3, 'i']]
# print(lst[0])
# print(lst[2])
#
# top_boxers = ['Mike Tyson', 'Muhammed Ali', 'Lenox Lewis', 'Evander Holyfiled']
#
# top_boxers.append('George Foreman')
# print(top_boxers)
#
# top_boxers.insert(4, 'Antony Jasua')
# print(top_boxers)
#
# top_boxers.remove('Antony Jasua')
# print(top_boxers)
#
# top_boxers.pop(4)
# print(top_boxers)
#
# current_boxers = ['Antony Jasua', 'Tyson Fury', 'Deantony Wailder']
# top_boxers.extend(current_boxers)
# print(top_boxers)
#
# top_boxers.sort(reverse=True)
# print(top_boxers)


# top_boxers = ['Mike Tyson', 'Muhammed Ali', 'Lenox Lewis', 'Evander Holyfiled']
# for boxer in top_boxers:
#     print(boxer)
# 
# for c in 'burak yılmaz':
#     print(c)

from random import randint

sayilar = []
for i in range(10):
    random_number = randint(0, 100)
    sayilar.append(random_number)

print(sayilar)

