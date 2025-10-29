from tkinter.font import names


class employee:
    def __init__(self):
        self.name = "unkonwn"
        self.age = 20
        self.salary = 10000

    def getdata(self):
        self.name = input("enter name")
        self.age = int(input("enter age"))
        self.salary = int(input("enter salary"))

    def showdata(self):
        print(f"{self.name} \t {self.age}\t{self.salary}")

ob = employee()
ob.getdata()
ob.showdata()