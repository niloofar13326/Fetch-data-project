import mysql.connector
import requests
from bs4 import BeautifulSoup
import re
mydb=mysql.connector.connect(user='root',password='niloofar',host='localhost',database='truecar_all_cars')
cursor=mydb.cursor()
result1=requests.get('https://www.truecar.com/used-cars-for-sale/listings/location-holyrood-ks/')
soup1=BeautifulSoup(result1.text,'html.parser')
value1=soup1.find_all('span',attrs={'class':"vehicle-header-make-model text-truncate"})
value2=soup1.find_all('span',attrs={'class':"vehicle-card-year font-size-1"})
value3=soup1.find_all('div',attrs={'data-test':"vehicleMileage"})
value4=soup1.find_all('div',attrs={'data-test':"vehicleListingPriceAmount"})

id=0
for n in range(0,40):
    if n==0:
        for i in range(0,31):
             Name=value1[i]
             Year=value2[i]
             Mileage=value3[i]
             Mileage=Mileage.text.split()
             Cost=value4[i]
             Cost=Cost.text
             Cost=re.split('\$',Cost)

             id = id+1
             cursor.execute( " INSERT INTO Fetch_data VALUES('{0}','{1}','{2}','{3}','{4}')".format(id,Name.text,Year.text,float(Mileage[0].replace(',','')),float(Cost[1].replace(',','') )))
             mydb.commit()

    elif n>=2:
        result2 = requests.get('https://www.truecar.com/used-cars-for-sale/listings/location-holyrood-ks/'+'?page={}&sort[]=best_match'.format(str(i)))
        soup2 = BeautifulSoup(result2.text, 'html.parser')
        value1 = soup2.find_all('span', attrs={'class': "vehicle-header-make-model text-truncate"})
        value2 = soup2.find_all('span', attrs={'class': "vehicle-card-year font-size-1"})
        value3 = soup2.find_all('div',attrs={'data-test':"vehicleMileage"})
        value4 = soup2.find_all('div', attrs={'data-test': "vehicleListingPriceAmount"})
        for i in range(0, 30):
            Name = value1[i]
            Year = value2[i]
            Mileage = value3[i]
            Mileage = Mileage.text.split()
            Cost = value4[i]
            Cost = Cost.text
            Cost = re.split('\$', Cost)
            id =id +1
            cursor.execute("INSERT INTO Fetch_data VALUES('{0}','{1}','{2}','{3}','{4}')".format(id,Name.text,Year.text,float(Mileage[0].replace(',','')),float(Cost[1].replace(',','') )))
            mydb.commit()
