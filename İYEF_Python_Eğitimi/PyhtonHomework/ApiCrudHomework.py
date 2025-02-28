import requests 
from pprint import pprint

endpoint = "http://localhost:3000/result"



# listeleme fonksiyonu
def getList(): 
    response = requests.get(endpoint)            # json-server --watch data.json   
    return response.json()

for record in getList():
    print(f'id: {record["_id"]}\n'
          f'hat_no: {record["HAT_NO"]}\n'
          f'hat_adı: {record["HAT_ADI"]}\n'
          f'güzergah_açıklama: {record["GUZERGAH_ACIKLAMA"]}\n'
          f'hat_başlangıç: {record["HAT_BASLANGIC"]}\n'
          f'hat_bitiş: {record["HAT_BITIS"]}\n'
          )



# parametreli listeleme fonksiyonu
def get_by_id(_id):    
    response = requests.get(endpoint+ "?_id="+ str(_id))  
    return response.json()

for record in get_by_id(103):
    print(f'hat_no: {record["HAT_NO"]}\n'
          f'hat_adı: {record["HAT_ADI"]}\n'
          f'güzergah_açıklama: {record["GUZERGAH_ACIKLAMA"]}\n'
          f'hat_başlangıç: {record["HAT_BASLANGIC"]}\n'
          f'hat_bitiş: {record["HAT_BITIS"]}\n'
          )
    
 

# yeni kayıt ekleme fonksiyonu
def createRecord(line):
    response = requests.post(endpoint, json=line)
    return response.json()

recordToCreate = {
    "_id": 102,
    "HAT_NO": 996,
    "HAT_ADI": "KONAK - FOÇA",
    "GUZERGAH_ACIKLAMA": "KONAK İSKELE -ESKİ FOÇA",
    "ACIKLAMA": "",
    "HAT_BASLANGIC": "KONAK İSKELE",
    "HAT_BITIS": "FOÇA"
}  
createRecord(recordToCreate)



# kayıt güncelleme fonksiyonu
def updateRecord(_id, record):    
    response = requests.patch(endpoint+ "/"+ str(_id), json = record)  
    return response.json()


recordToUpdate = {
    "HAT_ADI": "KONAK - URLA",
    "GUZERGAH_ACIKLAMA": "KONAK İSKELE - URLA",
    "HAT_BITIS": "URLA"
}
updateRecord(101, recordToUpdate)



# silme fonskiyonu
def delete_category(_id): 
    response = requests.delete(endpoint+ "_id="+ str(_id))
    return response.json()

delete_category(101)
    