# x = 2
# print(x)
# print(type(x))
#
# x = 'burak yılmaz'
# print(x)
# print(type(x))
#
# sayi_1 = int(input('Birinci Sayıyı Giriniz: '))
# sayi_2 = int(input('İkinci Sayı Giriniz: '))
#
# toplam = sayi_1 + sayi_2

# print(f'Toplam: {toplam}')
# print('{} + {} = {}'.format(sayi_1, sayi_2, toplam))
# print('Toplam: ', toplam)



# Dikdörtgenin alanını ve çevresini hesaplayalım
# kisa_kenar = float(input('Kısa Kenar: '))
# uzun_kenar = float(input('Uzun Kenar: '))
#
# print(f'Alan: {kisa_kenar * uzun_kenar}')
# print(f'Çevre: {2 * (kisa_kenar + uzun_kenar)}')

# üçgenin alanını hesaplayan kod bloğunu yazalım
# taban = int(input('Taban: '))
# yukseklik = int(input('Yukseklik: '))
#
# alan = (taban * yukseklik) / 2
#
# print(f'Alan: {alan}')



# Karar Mekanizmaları

# Kullanıcıdan 2 adet tam sayı alalım büyük olanı ekrana yazdıralım
# x = int(input('Tam sayı: '))
# y = int(input('Tam sayı: '))
#
# if x > y:
#     print(f'{x} büyüktür..!')
# elif y > x:
#     print(f'{y} büyüktür..!')
# elif y == x:
#     print(f'{x} ve {y} bir birine eşit..!')

# kullanıcıdan alınan sayı çift mi tek mi?
# x = int(input('Tam sayı: '))
#
# if x % 2 == 0:
#     print(f'{x} çifttir..!')
# else:
#     print(f'{x} tektir..!')



# kullanıcıdan aradığı ürün ismini alalım.
# aradığı ürün eğer telefon, tablet, monitör ise teknoloji reyonuna
# eğer domates, salatalık, muz ise sebze reyonuna yönlendirilim
# eğer şampuan, sabun, ruj ise kozmetik reyonuna yönlendirelim
# product = input('Aradığınız ürünü girin: ')
#
# if product == 'telefon' or product == 'tablet' or product == 'monitor':
#     print('Teknoloji reyonuna git..!')
# elif product == 'domates' or product == 'salatalık' or product == 'muz':
#     print('Sebze reyonuna git..!')
# elif product == 'şampuan' or product == 'sabun' or product == 'ruj':
#     print('Kozmetik reyonuna git..!')
# else:
#     print('Aradığınız ürün bulunmamaktadır..!')

# kullanıcıdan username ve password alalım.
# eğer kullanıcı adı burak, şifresi 123 ise hoşgeldiniz değilse hatalı bilgiler girdiniz çıktısı veren kodu yazınız
# user_name = input('User Name: ')
# password = input('Password: ')
#
# if user_name == 'burak' and password == '123':
#     print('Hoşgeldiniz..!')
# else:
#     print('Hatalı bilgiler girdiniz..!')



# Nested If
# eğer araç türü otomobil, hız 60 ve üzeri ise cezalı değilse ceza yok
# araç türü kamyon, hız 40 ve üzeri ise cezalı değilse ceza yok
# motorsiklet ise, hız 70 ve üzeri ise cezalı değilse ceza yok
# vehicle = input('Araç türü giriniz: ')
# speed = int(input('Hız: '))
#
# if speed > 0:
#     if vehicle == 'otomobil':
#         if speed >= 60:
#             print('Cezalısın..!')
#         else:
#             print('Ceza yok..!')
#     elif vehicle == 'kamyon':
#         if speed >= 40:
#             print('Cezalısın..!')
#         else:
#             print('Ceza yok..!')
#     elif vehicle == 'motorsiklet':
#         if speed >= 70:
#             print('Cezalısın..!')
#         else:
#             print('Ceza yok..!')
#     else:
#         print('Lütfen doğru araç türü giriniz..!')
# else:
#     print('Araç hızı sıfırdan küçük olamaz..!')


# kullanıcıdan satın aldığı kitap miktarını alalım
# bir kitap 5 TL.
# eğer 1-10 kitap alırsa yüzde 10 iskonto
# 11-15 kirap alırsa yüzde 15 iskonto
# 16-20 kitap alırsa yüzde 20 iskonto
# 21-25 kitap alırsa yüzde 25 iskonto uyguluyarak ödeyeceği toplam tutarı ekrana yazdıralım
# kitap_sayisi = int(input('Kitap Sayısı: '))
#
# if 1 <= kitap_sayisi <= 10: # kitap_sayisi >= 1 and kitap_sayisi <= 10
#     print(f'Ödenecek toplam tutar: {kitap_sayisi * 5 * 0.90}')
# elif 11 <= kitap_sayisi <= 15:
#     print(f'Ödenecek toplam tutar: {kitap_sayisi * 5 * 0.85}')
# elif 16 <= kitap_sayisi <= 20:
#     print(f'Ödenecek toplam tutar: {kitap_sayisi * 5 * 0.80}')
# elif 21 <= kitap_sayisi <= 25:
#     print(f'Ödenecek toplam tutar: {kitap_sayisi * 5 * 0.75}')
# else:
#     print('Lütfen doğru kitap sayısını giriniz..!')



# kullanıcıdan username, password alalım.
# kilosunu ve boy bilgilerini alalım. bmi hesaplayarak ilgli aralıklara göre durumunu kullanıcıya bildirelim
# username = input('User Name: ')
# password = input('Password: ')
#
# if username == 'beast' and password == '123':
#     print(f'{username} welcome..!')
#
#     weight = float(input('Weight: '))
#     height = float(input('Height: '))
#
#     bmi = weight / height ** 2
#
#     if 0 <= bmi < 18.5:
#         print(f'{username}, {bmi} is lean')
#     elif 18.6 <= bmi <= 24.9:
#         print(f'{username}, {bmi} is normal')
#     elif 25 <= bmi <= 29.9:
#         print(f'{username}, {bmi} is overweighted')
#     else:
#         print('incorrenct information..!')
# else:
#     print('Invalid credentials..!')



# kullanıcıdan mevsim bilgisi alalım.
# ayları ekrana yazdıralım
# mevsim = input('Mevsim: ')
#
# match mevsim:
#     case 'kış':
#         print('Aralık-Ocak-Şubat')
#     case 'ilkbahar':
#         print('Mart-Nisan-Mayıs')
#     case 'yaz':
#         print('Haziran-Temmuz-Ağustos')
#     case 'sonbahar':
#         print('Eylül-Ekim-Kasım')
#     case _:
#         print('böyle bir mevsim yok. uzaylı mmısın?')

# try:
#     age = int(input('Age: '))
#     print(age)
# except ValueError as err:
#     print(err)

# Exeption Handling
#try:
#   bolunen = int(input('Bolünen: '))
##     bolen = int(input('Bolen: '))
#
#     sonuc = bolunen / bolen
#
#   print(f'Sonuç: {sonuc}')
#except ZeroDivisionError as err:
#    print('Tam sayılar sıfıra bölünmez..!')
#else:
#    print('Except çalışmazsa else çalışır.')
#finally:
#    print(f'Hata olsada olmasa da ben çalışırım..!')

