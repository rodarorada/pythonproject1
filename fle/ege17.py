#
# def odin():
#     kol = 0
#     m = 0
#     with (open("ege17text", "r") as file):
#         data=file.readlines()
#         data=[int(x) for x in data]
#         for i in range(len(data)-1):
#             if data[i]%3==0 or data[i+1] % 3 == 0:
#                 kol=kol+1
#                 m = max(m, data[i]+data[i+1])
#     print(m, kol)
# odin()
#
# def dva():
#     kol = 0
#     m = 0
#     with (open("ege17text", "r") as file):
#         data=file.readlines()
#         data=[int(x) for x in data]
#         for i in range(len(data)-1):
#             for j in range(i+1, len(data)):
#                 if data[i] % 160 != data[j] % 160 and (data[i] % 7 == 0 or data[j] % 7 == 0):
#                     kol = kol + 1
#                     m = max(m, data[i]+data[j])
#     print(m, kol)
# dva()

# def tridchati():
#     m = 0
#     kol = 0
#     with (open("ege17text", "r") as file):
#         data=file.readlines()
#         data=[int(x) for x in data]
#         for i in range(len(data)-2):
#             sp = []
#             sp.append(data[i])
#             sp.append(data[i+1])
#             sp.append(data[i+2])
#             sp.sort()
#             if sp[0]**2+sp[1]**2 == sp[2]**2:
#                 kol = kol + 1
#                 m = max(m, sp[0]+sp[1]+sp[2])
#     print(kol, m)
# tridchati()
#
# def tridchati_odin():
#     kol = 0
#     m = 0
#     with (open("ege17text", "r") as file):
#         data = file.readlines()
#         data = [int(x) for x in data]
#         data2 = [x for x in data if x % 2 == 0]
#         sa = sum(data2)/len(data2)
#         # print(sa)
#         for i in range(len(data)-1):
#             if (data[i] % 3 == 0 or data[i+1] % 3 == 0) and (data[i] < sa or data[i+1] < sa):
#                 kol = kol + 1
#                 m = max(m, data[i]+data[i+1])
#     print(kol, m)
# tridchati_odin()
#
# def tridchati_tri():
#     m=0
#     kol=0
#     sp=[]
# #     mini=999999999999999999999999999999999
# #     with (open("ege17text", "r") as file):
# #         data = file.readlines()
# #         data=[int(x) for x in data]
# #         mini=min([x for x in data if x%21==0])
# #         for i in range(len(data)-1):
# #             if data[i]%mini==0 or data[i+1]%mini==0:
# #                 kol = kol + 1
# #                 m = max(m, data[i]+data[i+1])
# #     print(kol, m)
# # tridchati_tri()
#
import random as ran
#
# def domashka():
#     with (open("ege17text", "w") as file):
#         with (open("ege17text2", "w") as file2):
#             for i in range(1000):
#                 file.write(str(ran.randint(0,100))+"\n")
#                 file2.write(str(ran.randint(0, 100)) + "\n")
# # domashka()
#
# def domashka2():
#     a=0
#     b=0
#     m=0
#     with (open("ege17text", "r") as file):
#         with (open("ege17text2", "r") as file2):
#             data = [int(x) for x in file.readlines()]
#             data2 = [int(x) for x in file2.readlines()]
#             for j in range(len(data)):
#                 for i in range(len(data2)):
#                     sum=data[j]+data2[i]
#                     if sum>m and sum%3==0:
#                         m=sum
#                         a=data[j]
#                         b=data2[i]
#     print(a, b, m)
# # domashka2()
#
# def vdtr():
#     kol=0
#     with (open("ege17text", "r") as file):
#         data=file.readlines()
#         for i in data:
#             sp=[int(x) for x in i.split()]
#             sp.sort()
#             if sp[0]+sp[1]>sp[2]:
#                 kol=kol+1
#     print(kol)
# # vdtr()
#
# def usadaosnh():
#     kol=0
#     with open("ege17text", "r") as file:
#         data=file.readlines()
#         for i in data:
#             sp=[int(x) for x in i.split()]
#             n=[x for x in sp if sp.count(x)==2]
#             ne=[x for x in sp if sp.count(x)==1]
#             if len(n)==2 and len(ne)==4:
#                 if sum(ne)/len(ne)<=sum(n):
#                     kol=kol+1
#     print(kol)
# usadaosnh()
#
# def chet(sp):
#     kolc=0
#     koln=0
#     chett=0
#     neechet=0
#     for i in sp():
#         if i%2==0:
#             kolc=kolc+1
#             chett=chett+i
#         else:
#             koln=koln+1
#             neechet=neechet+i
#     if koln>kolc and chett>neechet:
#         return True
#
# def dvenadcsati():
#     kol=0
#     with open("test3.txt", "r") as file:
#             data=file.readlines()
#             for i in data:
#                 sp=[int(x) for x in i.split()]
#                 for c in sp:
#                     if sp.count(c)==1:
#                         if chet(i):
#                             kol=kol+1
#     print(kol)
# dvenadcsati()
#
# def jkxah():
#     kol=0
#     with open("test3.txt", "r") as file:
#         data=file.readlines()
#         for i in data:
#             sp=[int(x) for x in i.split()]
#             for c in sp:
#                 if sp.count(c)==1:
#                     chet = [x for x in sp if x%2==0]
#                     nechet = [x for x in sp if x%2!=0]
#                     if len(nechet)>len(chet):
#                         if sum(nechet) < sum(chet):
#                             kol=kol+1
#     print(kol)
# jkxah()