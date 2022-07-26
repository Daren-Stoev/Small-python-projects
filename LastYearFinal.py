import datetime
from abc import ABC, abstractclassmethod, abstractmethod

class Client(ABC):
    def __init__(self,name,startDate):
        self.name = name
        self.startDate = startDate

    @abstractmethod
    def printValues(self):
        pass

class Person(Client):
    def __init__(self,name,city,date_of_birth,number):
        super().__init__(name,date_of_birth)
        self.city = city
        self.number = number

    def printValues(self):
         print("Client: ",self.name,"; ",self.city,"; роден на: ", self.startDate,"; ",self.number)


class Firm(Client):
    def __init__(self,name,type,date_of_registration,adress):
        super().__init__(name,date_of_registration)
        self.type = type
        self.adress = adress

    def printValues(self):
          print("Company: ", self.name,"; ",self.type,"; регистрирана на: ",self.startDate,"; ",self.adress)


def inputData(arr):
    while True:
        try:
            type_of_client = input("Enter what type of client you will be entering(P/C): ")
            if(type_of_client.lower() == "P".lower()):
                print("P1")
                name = input("Enter Name(1-30 characters): ")
                if len(name) > 30 or len(name) == 0:
                    raise ValueError
                city = input("Enter City(3-15 characters): ")
                if len(city) > 15 or len(city) < 3:
                    raise ValueError
                date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
                if not validateDate(date_of_birth):
                    raise ValueError
                number = input("Enter Phone number (6-10 characters): ")
                if len(number) > 10 or len(number) < 6 or not int(number):
                    raise ValueError
                if(len(arr)) >= 1500:
                    raise Exception()
                else:
                    arr.append(Person(name,city,date_of_birth,number))
                break
            elif(type_of_client.lower() == "C".lower()):
                print("C1")
                Fname = input("Enter Firm Name(1-30 characters): ")
                if len(Fname) > 30 or len(Fname) == 0:
                    raise ValueError
                type_of_firm = input("Enter Type(2-4 characters): ")
                if len(type_of_firm) > 4 or len(type_of_firm) < 2:
                    raise ValueError
                date_of_registration = input("Enter date of registration (YYYY-MM-DD): ")
                if not validateDate(date_of_registration):
                    raise ValueError
                adress = input("Enter Adress (max 30 characters): ")
                if len(adress) > 30:
                    raise ValueError
                if(len(arr)) >= 1500:
                    raise Exception()
                else:
                    arr.append(Firm(Fname,type_of_firm,date_of_registration,adress))
                print(arr[0])
                break
            else:
                int("Fsssddfd")
        except ValueError:
            print("Sorry, that is not a valid input")
            continue
        except Exception:
            print('Items exceeds the maximum allowed length of 1500')
        else:
            print("Fail")
            break



def PrintContent(arr):
    for client in arr:
       client.printValues()
           
def validateDate(date_text):

    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
       # raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        return False

def Swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def CheckFirms(clients,date,typeOfClient):
    valid = []

    for client in clients:
        if type(client) == typeOfClient  and client.startDate < date:
            valid.append(client)

    PrintContent(valid)

def CompareDates(clients):
    pCount = 0
    CCount = 0
    for i in range(len(clients) - 1):
        for j in range(len(clients) - (i+1)):
            if clients[j].startDate < clients[j+1].startDate:
                Swap(clients,j,j+1)
            elif clients[j].startDate == clients[j+1].startDate and type(clients[j+1]) == Person:
                Swap(clients,j,j+1)
    
    for client in clients:
        if type(client) == Person:
            pCount += 1
        elif type(client) == Firm:
            CCount += 1

    print("People: ",pCount)
    print("Companies: ",CCount)

    return clients




content = []


inputData(content)


p1 = Person("Ivan","Plovdiv","2001-12-25","08874512369")
f1 = Firm("Firma","OOD","1998-07-30","Alen Mak 21")


content.append(f1)
content.append(p1)
content.append(Person("Petar","Pleven","2000-02-21","0887444469"))
content.append(Person("Dimitar","Pleven","1985-06-13","0888888869"))
content.append(Person("Stoyan","Sofia","1945-11-01","77777777"))

content.append(Firm("MCDonalds","NPO","1948-04-24","Macedonia"))
content.append(Firm("MD","XD","2005-05-15","Romania"))
content.append(Firm("PU1","OOD","2005-06-15","Plovdiv"))

CompareDates(content)

PrintContent(content)
print("------------")
PrintContent(CompareDates(content))
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
CheckFirms(content,"2005-06-15",Firm)