# # # append insert extend clear pop remove sort reverse
# # # for while
# # name = ["2", "4","s"]
# # n = [x+"2" for x in name]
# # print(n[1:2])
# # nums = [ i for i in range(1,11)]
# # ch =[num for num in nums if num  % 2 == 0]
# # nch= [num for num in nums if num % 2 != 0]
# # print(ch,nch)
# names = ['Pavel', 'Sahsa', 'jordan', 'Ppashsa']
# answer = [el[0] for el in names]
# print(answer)
# nums = [i for i in range(1,21)]
# nums2 = [el for el in nums if el % 2 == 0]
# print(nums2)
names = []
# while True:
#     name = input("Введите имя: ")
#     if name.lower() in [i.lower() for i in names]:
#         print("Имя занято")
#     else:
#         names.append(name)
#         print(f"{name} добавлен в список")
#         print(names)


# num1 = float(input("enter num1: "))
# math = input("Enter symbol: + - * / ")
# num2 = float(input("enter num2: "))
#
# if math == '+':
#      print(num1 + num2)
# elif math == "-":
#     print(num1 - num2)
# elif math =="*":
#     print(num1 * num2)
# elif math == "/":
#     if num2 == 0:
#         print("ERROR")
#     else:
#         print(num1 / num2)

# num1 = input()
# num2 = input()
# if num1 == "k"  and num2 == "k":
#     print("draw")
# elif num1 == "n" and num2 == "n":
#     print ("draw")
# elif num1 == "b"  and num2 == "b":
#     print("draw")
# elif num1 == "k" and num2 == "b":
#     print("2 WON")
# elif num1 == "b" and num2 == "k":
#     print("1 WON")
# elif num1 == "n" and num2 == "b":
#     print("1 WON")
# elif num1 == "b" and num2 == "n":
#     print("2 WON")
# elif num1 == "k" and num2 == "n":
#     print("1 WON")
# else:
#     print("2 WON")
#
# names =[]
# n = input("enter name")
# names.append(n.lower())
# names2 = [name.lower() for name in names if name[0] == "t"]
# print(names2)

# x = {'Name': "Pasha", 'Job': "Tgbot creator"}
# if 'Name' in x: keys по умолчанию, items ищет все, values значения
# print("da est")
# print(list(x.values()))
# print(x.items())
# print(x.key())

# m_dict = {'song': 'Godzilla', 'singer': "Eminem"}
# m_dict.pop("song")
# print(m_dict)
# m_dict.popitem()
# print(m_dict)
# print(m_dict.get("vantus"))

# Metod set
# a = {1, 2, 3, 4 ,5 ,6 ,1,1,1}
# print(a)
# b= set([1, 2, 4, 4])
# print(b)

# insttructor = dict(name = 3, age =32, job = 33)
# for k,v in insttructor.items():
#     print(k,v)
# sklad = {"Продукты": {}}
# while True:
#     a = input("Выберите действие \n"
#               "1 = Добавить\n"
#               "2 - Посмотреть\n")
#     if a == "1":
#         b = input("Какой продукт вы хотите добавить?")
#         c = int(input("Задайте значение"))
#         sklad["Продукты"][b] = c
#     elif a == "2":
#        print(sklad)
#     else:
#         print("error!")
#
a = [1,2, 4, 5]
# def spam(a,b):
#     print (a+b)
#     return spam
# spam(2,3)
# def spam1(*args):
#     for a in args:
#         return args
# print(spam1(12,32))
#
# def spam2(**kwargs):
#     return kwargs
# print(spam2(name ="Anton", age = 23))

# def an(**kwargs):
# #     for k, v in kwargs.items():
# #         return k,v
# # print(an(name = "PAsha", age =23))
# def rr():
# #     while True:
# #         a = int(input("Введите число "))
# #         if a%2==0:
# #             print(f"Число {a} четное")
# #         elif a%2 != 0:
# #             print(f"Число {a} нечетное")
# #         if b%2==0:
# #             print(f"Число {b} четное")
# #         elif b%2 != 0:
# #             print(f"Число {b} нечетное")
# #     print(a, b)
# #     return a, b
# # rr()
# def rr(*args):
#     while True:
#         args = int(input("Введите число "))
#         if args%2==0:
#             print(f"Число {args} четное")
#         elif args%2 != 0:
#             print(f"Число {args} нечетное")
#
#       print(args)
# rr()
#
# class Gun:
#     def shoot(self,s):
#         print(s)
# class pistol(Gun):
#     def defolt_fire(self,c):
#         print("стреляет по одному")
#     def burst_fire(self,m):
#         print("стрельба очередью")
#     def auto_fire(self,n):
#         print("стрельба автоматом")
#     pass
#
# class car:
#     def __init__(self,model,color):
#         self.model = model
#         self.color = color
# class supercar(car):
#     def __init__(self,model,color,year):
#         super().__init__(model,color)
#         self.year = year;
#
# class myclass:
#     @classmethod
#     def class_info(cls):
#         return f"this is the {cls.__name__} class."
# print(myclass.class_info())
#
# class Player:
#     def run(self):
#         print("игрок бежит")
#     def kick(self):
#         print("игрок пинает мяч")
#     def __init__ (self,speed):
#         self.speed = speed
# class Nap(Player):
#     def __init__(self,speed, goli):
#         super().__init__(speed)
#         self.goli = goli
# class Zash(Player):
#     def __init__ (self,speed,otbor):
#         super().__init__(speed)
#         self.otbor = otbor
# class Poluzash(Player):
#     def __init__(self, speed, pasi):
#         super().__init__(speed)
#         self.pasi = pasi
# class Vratar(Player):
#     def __init__(self, speed, save):
#         super().__init__(speed)
#         self.save = save



