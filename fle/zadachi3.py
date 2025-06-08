



from itertools import *
from operator import index


# def shestnadchat():
#     st="012345678"
#     kol=0
#     for i in product(st,repeat=12):
#         if i[0]!="0":
#             flag = True
#             for j in range(len(i)-1):
#                 if (i[j]+i[j+1]%2==0 and i[j]<i[j+1]) or (i[j]+i[j+1]%2==1 and i[j]>i[j+1]):
#                     pass
#                 else:
#                     flag=False
#             if flag==True:
#                 kol=kol+1
#     print(kol)
# shestnadchat()

# def vosemnadcat():
#     st="0123456789abcde"
#     bykvi="abcde"
#     kol=0
#     for i in product(st,repeat=8):
#         if i.count("0")==2:
#             kol_bykvi = 0
#             for j in bykvi:
#                 kol_bykvi=kol_bykvi+i.count(j)
#             if kol_bykvi==2:
#                 kol=kol+1
#     print(kol)
# vosemnadcat()
#
# def dvadcat_odin():
#     st="0123456"
#     kol=0
#     for i in product(st,repeat=5):
#         if int(i[0])%2==0:
#             if i[-1]!="2" or i[-1]!="3":
#                 if i.count("1")==2:
#                     kol=kol+1
#     print(kol)
# dvadcat_odin()

# def devetnadcat(n):
#     sp=[]
#     Nn1=int(n[0])+int(n[1])
#     Nn2=int(n[2])+int(n[3])
#     sp.append(Nn1)
#     sp.append(Nn2)
#     sp.sort()
#     Nn=str(sp[0])+str(sp[1])
#     return Nn
#
# kol2=0
# for i in range(1000,10000):
#     kol=0
#     for j in str(i):
#         if int(j)%2==1:
#             kol=kol+1
#     if kol==4:
#         if devetnadcat(str(i))=="616":
#             kol2=kol2+1
# print(kol2)

# def dvadcat(n):
#     sp=[]
#     Nn1=int(n[0])*int(n[1])
#     Nn2=int(n[1])*int(n[2])
#     sp.append(Nn1)
#     sp.append(Nn2)
#     sp.sort()
#     Nn=str(sp[1])+str(sp[0])
#     return Nn
#
# for i in range(100,1000):
#     if dvadcat(str(i))=="205":
#         print(i)
#         break

def ss(a,s):
    b=""
    while a>0:
        b=b+str(a%s)
        a=a//s
    b=b[::-1]
    return b

# def devet():
#     otvet=ss(49**10+7**30-49,7)
#     otvet=otvet.count("6")
#     print(otvet)
# devet()

# def shesdesatchetiri():
#     sp=[0, 0, 0, 0, 0, 0, 0]
#     otvet=ss(5*343**8+4*49**12+7**14-98,7)
#     for i in otvet:
#         sp[int(i)]=sp[int(i)]+1
#     print(sp)
#     print(sp.index(max(sp)))
# shesdesatchetiri()

# def semdesatchetiri():
#     for x in "0123456789abcdefg":
#         a=int("8"+x+"5678",25)
#         b=int("457"+x+"69",25)
#         c=int("145"+x+"1",25)
#         if (a+b+c)%23==0:
#             print((a+b+c)/23)
# semdesatchetiri()

def ss2(a,s):
    b=[]
    while a>0:
        b.append(a%s)
        a=a//s
    b=b[::-1]
    return b
print(ss2(3*289**2024+81*49**81-6011,31))
# a=3*289**2024
# b=81*49**81-6011
# print(b)
# print(sum([i for i in ss2(3*289**2024+81*49**121-9*16**81-6011,31) if i<18]))

def semdesatdevat():
    for i in range(0,2301):
        if ss(7**350+7**150-i,7).count("0")==200:
            print(i,7**350+7**150-i)
semdesatdevat()