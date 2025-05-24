# def dvenadcsati():
# #     with open("test2.txt", "r") as file:
# #             data=[int(x) for x in file.readlines()]
# #             for i in data:
# #                 chet=[int(x) for x in data if x%2==0]
# #                 nechet = [int(x) for x in data if x % 2 == 1]
# #                 sp=[int(x) for x in str(i).split()]
# #                 print(chet, nechet)
# #                 # if sp.count(i)==1:
# # dvenadcsati()
# #
# # def dvadchatshest():
# #     sp2=[]
# #     with open("test4.txt", "r") as file:
# #         data=file.readlines()
# #         S=int(data[0].split()[0])
# #         print(S)
# #         sp=[int(x) for x in data[1:]]
# #         sp.sort()
# #         for i in sp:
# #             if i+sum(sp2)<=S:
# #                 sp2.append(i)
# #         for i in sp[::-1]:
# #             if i+sum(sp2[:-1])<=S:
# #                 sp2[-1]=i
# #                 break
# #         print(len(sp2), sp2)
# # dvadchatshest()
#
# def shestnadchat():
#     ch=0
#     suma=0
#     sp2=[]
#     with open("test4.txt", "r") as file:
#         data=file.readlines()
#         sp = [int(x) for x in data[1:]]
#         for i in sp:
#             if i>50:
#                 sp2.append(i)
#             else:
#                 suma=suma+i
#         sp2.sort()
#         for i in range(len(sp2)):
#             if i<len(sp2)//2:
#                 ch=sp2[i]
#                 suma=suma+sp2[i]*0.75
#             else:
#                 suma=suma+sp2[i]
#     print(sp2,suma,ch)
# shestnadchat()

# def semnadchat():
#     ch=0
#     suma=0
#     sp2=[]
#     with open("test4.txt", "r") as file:
#         data=file.readlines()
#         sp = [int(x) for x in data[1:]]
#         for i in sp:
#             if i>100:
#                 sp2.append(i)
#             else:
#                 suma=suma+i
#         sp2.sort()
#         for i in range(len(sp2)):
#             if i<len(sp2)//2:
#                 ch=sp2[i]
#                 suma=(suma+sp2[i])/100*30
#             else:
#                 suma=suma+sp2[i]
#     print(sp2,suma,ch)

from threading import Timer

# def repeater(interval, function):
#     Timer(interval, repeater, [interval, function]).start()
#     function()

# def Timer():
#     kol=0
#

# def semnadchat():
#     with open("test4.txt", "r") as file:
#         data=file.readlines()
#         print("введите скидку")
#         procent = int(input())
# 
#         (sp2, suma, ch) = semnadchatint(data,procent)
#         print(sp2, suma, ch)

# def semnadchatint(data,procent):
#     ch = 0
#     suma = 0
#     sp2 = []
#     sp = [int(x) for x in data[1:]]
#     for i in sp:
#         if i > 100:
#             sp2.append(i)
#         else:
#             suma = suma + i
#     sp2.sort()
#     for i in range(len(sp2)):
#         if i < len(sp2) // 2:
#             ch = sp2[i]
#             suma = (suma + sp2[i]) / 100 * procent
#         else:
#             suma = suma + sp2[i]
#     my_tuple = (sp2, suma, ch)
#     return my_tuple

# semnadchat()

from itertools import *

# def vosem():
#     kol=0
#     shifr=""
#     for i1 in range(1,5):
#         for i2 in range(1, 5):
#             for i3 in range(1, 5):
#                 for i4 in range(1, 5):
#                     for i5 in range(1, 5):
#                         shifr=str(i1)+str(i2)+str(i3)+str(i4)+str(i5)
#                         if shifr.count("1")==2:
#                             kol=kol+1
#     print(kol)
# vosem()

# def vosem2():
#     st="1234"
#     kol=0
#     for i in product(st, repeat=5):
#         if i.count("1")==2:
#             kol=kol+1
#     print(kol)
# vosem2()

# def chetiri():
#     st="0123456"
#     kol=0
#     for i in product(st, repeat=4):
#         if int(i[0])>int(i[1])>int(i[2])>int(i[3]):
#             kol=kol+1
#     print(kol)
# chetiri()

# def vosem():
#     st="0123456789"
#     kol=0
#     for i in permutations(st,4):
#         if i[0]!="0":
#             flag = True
#             for j in range(len(i)-1):
#                 if int(i[j])%2==int(i[j+1])%2:
#                     flag=False
#                     break
#             if flag==True:
#                 kol=kol+1
#     print(kol)
# vosem()
#
# def chetirnadchat():
#     st="012345678"
#     kol=0
#     for i in product(st,repeat=5):
#         if i[0]!="0":
#             if i.count("5")==1:
#                 if i.index("5")==0:
#                     if int(i[1])%2==0:
#                         kol=kol+1
#                 elif i.index("5") == 4:
#                     if int(i[-2])%2==0:
#                         kol=kol+1
#                 else:
#                     if int(i[i.index("5")-1])%2==0 and int(i[i.index("5")+1])%2==0:
#                         kol=kol+1
#     print(kol)
# chetirnadchat()

def shestnadchat():
    st="012345678"
    kol=0
    for i in product(st,repeat=12):
        if i[0]!="0":
            flag = True
            for j in range(len(i)-1):
                if (i[j]+i[j+1]%2==0 and i[j]<i[j+1]) or (i[j]+i[j+1]%2==1 and i[j]>i[j+1]):
                    pass
                else:
                    flag=False
            if flag==True:
                kol=kol+1
    print(kol)
shestnadchat()