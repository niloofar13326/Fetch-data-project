import csv
from sklearn import tree
from sklearn import preprocessing
x=[]
y=[]
new_data=input("Enter your car, First Name of the car with the Model, Second Year, Third The Mileage that the car works >>>(Ex:Nissan Altima,2017,43999):\n")
with open('ML.csv','r') as csvfile:
    data= csv.reader(csvfile)
    next(data)
    for line in data:

        le = preprocessing.LabelEncoder()
        le.fit(line[1:2])
        x.append(line[1:4])
        for item in x:
            item.remove((item[0]))
            item.insert(0,le.transform(line[1:2]))
        y.append(line[4:5])
clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)


new_data=new_data.split(',')
print(new_data)
new_data_1=[]
le = preprocessing.LabelEncoder()
le.fit(new_data[0:1])
new_data_1.append(new_data[0:3])
for item in new_data_1:
    item.remove((item[0]))
    item.insert(0,le.transform(new_data[0:1]))


answer=clf.predict(new_data_1)
print(answer[0])

