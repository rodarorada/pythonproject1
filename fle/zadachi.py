# import math
# #
# #
# # def f1(st):
# #     std=""
# #     for i in st:
# #         r=str(int(i)+1)
# #         print(r)
# #         std=std+r
# #         return std
# #
# # #print(f1("1234"))
# #
# # def f2(st):
# #     flag=True
# #     for i in range(len(st)//2):
# #         if st[i]!=st[-(i+1)]:
# #             flag=False
# #     return flag
# #
# # def f3(st):
# #     stoka=[]
# #     for i in range(len(st)-1):
# #         for j in range(i+1, len(st)):
# #             st2=st[i:j+1]
# #             if f2(st2):
# #                 stoka.append(st2)
# #     return stoka
# #
# # #print(f3("qwqfqqq"))
# #
# # def f4(st):
# #     sl={}
# #     for i in st:
# #         if sl.get(i):
# #             sl[i]=sl[i]+1
# #         else:
# #             sl[i]=1
# #     return sl
# # #print(f4("owjieqrheui vqpa aph sna"))
# #
# # def f5(chislo):
# #     sp=[]
# #     for i in range(1, chislo//2):
# #         if chislo%i==0:
# #             sp.append(i)
# #     return sp
# # # print(f5(77745))
# #
# # def f6(sp):
# #     sl={}
# #     sp=sp.split()
# #     for i in sp:
# #         if sl.get(len(i)):
# #             sl[len(i)].append(i)
# #         else:
# #             sl[len(i)]=[i]
# #     return sl
# # sl=f6("adsjd asgfk eropjsz ;rsmj  ;ka                a dgf  md md            ghjrtgshjkfgchjcgtyuiwrgahgtsruhgauiraysbctjildsh;oiuatyhurisYHDSF:IUgvlhydfuzghskcjfzhtcisulzgczskh")
# #
# # print(max(sl.keys()))
# # for i in range(max(sl.keys())+1):
# #     if i in sl.keys():
# #         print(i, sl.get(i))
#
# # print(ord("s"))
# #
# # print(chr(1160))
# #
# # def kodirovka(sp):
# #     spt=""
# #     for i in sp:
# #         csifr=chr(ord(i)+5)
# #         spt=spt+str(csifr)
# #     return spt
# # print(kodirovka("abobas"))
# #
# # def dekodirovka(sp):
# #     spt=""
# #     for i in sp:
# #         csifr=chr(ord(i)-5)
# #         spt=spt+str(csifr)
# #     return spt
# # print(dekodirovka("fgtgfx"))
# #
# # def f7(sp):
# #     st=sp[0]
# #     k=1
# #     for i in range(len(sp)-1):
# #         if sp[i]==sp[i+1]:
# #             k=k+1
# #         else:
# #             st=st+str(k)
# #             k=1
# #             st=st+sp[i+1]
# #     st=st+str(k)
# #     return st
# # print(f7("aaaassdfffggggghh"))
# #
# # def kodirovka(sp):
# #     jsn={}
# #     spt=""
# #     for i in sp:
# #         csifr=chr(ord(i)*2)
# #         spt=spt+str(csifr)
# #     jsn=spt
# #     return jsn
# # print(kodirovka(" "))
# #
# # def dekodirovka(jsn):
# #     spt=""
# #     for i in jsn:
# #         csifr=chr(ord(i)//2)
# #         spt=spt+str(csifr)
# #     return spt
# # print(dekodirovka("jsn"))
# #
# # def f8(a):
# #     for i in range(5, a):
# #         for j in range(4, a):
# #             for k in range(3, a):
# #                 if k**2+j**2 == i**2:
# #                     print(k, "**2", j, "**2=", i)
# # f8(100)
# #
# # def f12(a):
# #         for j in range(4, a):
# #             for k in range(3, a):
# #                 i=k**2+j**2
# #                 if i**0.5%1==0:
# #                     print(k, "**2", j, "**2=", i)
# # f12(100)
#
# # def f9(st):
# #     sp = []
# #     sl = {}
# #     gl = ["e", "y", "u", "i", "o", "a", "q"]
# #     st = st.split()
# #     for i in st:
# #         for j in gl:
# #             for k in i:
# #                 if j == k:
# #                     sp.append(k)
# #         if sl.get(len(sp)):
# #             sl[len(sp)].append(i)
# #             sp=[]
# #         else:
# #             sl[len(sp)] = [i]
# #             sp=[]
# #
# #     return sl
#
# #print(f9("bb yhwre eee bb wrtplkjhgfdszxcvbnma a aa abba  ddaqeyuioa eyuioqa"))
#
# # def f10(st):
# #     kol=0
# #     sl = {}
# #     gl = "qeyuioa"
# #     st = st.split()
# #     for i in st:
# #         kol=0
# #         for j in i:
# #             if j in gl:
# #                 if sl.get(kol):
# #                     sl[kol].append(i)
# #                 else:
# #                     sl[kol] = [i]
# #                 sp=[]
# #     return sl
# # print(f10("bb yhwre eee bb wrtplkjhgfdszxcvbnma a aa abba  ddaqeyuioa eyuioqa"))
# #
# # def f11(st):
# #     sl = {}
# #     gl = "qeyuioa"
# #     st = st.split()
# #     for i in st:
# #         sp=[x for x in i if x in gl]
# #         kol=len(sp)
# #         for j in i:
# #             if j in gl:
# #                 if sl.get(kol):
# #                     sl[kol].append(i)
# #                 else:
# #                     sl[kol] = [i]
# #                 sp=[]
# #     return sl
# # print(f11("bb yhwre eee bb wrtplkjhgfdszxcvbnma a aa abba  ddaqeyuioa eyuioqa"))
# #
# # def f13(i):
# #     sp=[]
# #     for a in range(2, i):
# #             if i%a==0:
# #                 sp.append(a)
# #     return sp
# #
# # def f15(a):
# #     for i in range(2,a):
# #         if a%i==0:
# #             return False
# #     return True
# #
# # def f14(a, b):
# #     for i in range(a,b+1):
# #         sp=f13(i)
# #         if len(sp)==2:
# #             if f15(sp[0]) and f15(sp[1]):
# #                 print(i, sp)
# # f14(1,1000)
#

# def deliteli(a):
#     sp=[]
#     for i in range(2, a):
#         if a%i==0:
#             if iskatel(i)==5:
#                 sp.append(i)
#     return sp
#
# def iskatel(a):
#     a=str(a)
#     sum=0
#     for i in a:
#         sum=sum+int(i)
#     return sum
#
# def perebor(a, b):
#     for i in range(a, b+1):
#         if len(deliteli(i))==3:
#             print(i, deliteli(i))
#
#
# print(perebor(1, 100000000))

# def EG10():
#     sp=[]
#     for i in range(174457,174506):
#         sp=EG11(i)
#         if len(sp) == 2:
#             print(i, sp)
#
# def EG11(i):
#     sp=[]
#     for a in range(2,i):
#         if i%a==0:
#             sp.append(a)
#     return sp
# print(EG10())

# def EG20():
#     nomer=0
#     for i in range(245690,245757):
#         nomer=nomer+1
#         if EG21(i):
#             print(nomer, i)
#
# def EG21(i):
#     for a in range(2,i):
#         if i%a==0:
#             return False
#     return True
# EG20()
#
# def M(a):
#     sp=[]
#     for i in range(2,a):
#         if a%i==0:
#             sp.append(i)
#     if len(sp)==0:
#         m=0
#     else:
#         m=sp[0]+sp[-1]
#     return m
#
# def perebor1():
#     for i in range(452022, 10**10):
#         if M(i)%7==3:
#             print(i, M(i))
# # perebor1()
#
# def M1(a):
#     sp=[]
#     for i in range(2,a//2):
#         if a%i==0:
#             sp.append(i)
#     if len(sp)<2:
#         m=0
#     else:
#         m=sp[-1]+sp[-2]
#     return m
#
# def perebor2():
#     for i in range(11250, 112551):
#         if str(M1(i))[-4:]=="1214":
#             print(i, M1(i))
# perebor2()

# def D(a,b,c):
#     d=b*b-4*a*c
#     x1=(-b+d**0.5)/(2*a)
#     x2=(-b-d**0.5)/(2*a)
#     return [x1, x2]
# print(D(4,7,3))
#
# def avtomat(a):
#     s = int(str(a)[0]) + int(str(a)[1])
#     d = int(str(a)[1]) + int(str(a)[2])
#     if s>d:
#         n=int(str(s) + str(d))
#     else:
#         n=int(str(d) + str(s))
#     return n
#
# for i in range(100,1000):
#     if avtomat(i)==1412:
#         print(i)
#         break

# def avtomat1(a):
#     sp=[]
#     a = str(a)
#     s = int(a[0]) + int(a[1])
#     d = int(a[1]) + int(a[2])
#     f = int(a[2]) + int(a[3])
#     sp.append(s)
#     sp.append(d)
#     sp.append(f)
#     sp.sort()

# for i in range(100,1000):
#     if avtomat1(i)==1412:
#         print(i)
#         break

# sp=[34,1,55,2]
# sp.sort()
# print(sp)
#
# def ddf(a):
#     ch=0
#     sp = []
#     a = str(a)
#     g = int(a[0]) + int(a[1])
#     f = int(a[1]) + int(a[2])
#     x = int(a[2]) + int(a[3])
#     sp.append(g)
#     sp.append(f)
#     sp.append(x)
#     sp.sort()
#     ch = int(str(sp[1])+str(sp[2]))
#     return ch
# # print(ddf(9575))
# for i in range(1000,10000):
#     if ddf(i)==1517:
#         print(i)
#
# def dd1f5(a):
#     sp = []
#     a = str(a)
#     g = int(a[0]) + int(a[1])
#     f = int(a[1]) + int(a[2])
#     x = int(a[2]) + int(a[3])
#     sp.append(g)
#     sp.append(f)
#     sp.append(x)
#     sp.sort()
#     ch = int(str(sp[1])+str(sp[2]))
#     return ch
#
# for i in range(1000,10000):
#     if dd1f5(i)==1418:
#         print(i)
#         break
#
# def polindrom():
#     data=""
#     for god in range(1998, 2026):
#         for mesihc in range(1,13):
#             if mesihc < 10:
#                 mesihc = "0" + str(mesihc)
#             for deni in range(1, 32):
#                 if deni<10:
#                     deni="0"+str(deni)
#                 data=str(deni)+str(mesihc)+str(god)
#                 if data==data[::-1]:
#                     print(str(deni)+"."+str(mesihc)+"."+str(god))
# polindrom()
#
# def shivrovka(st):
#     sp=[]
#     for i in st:
#         sim=ord(i)-96
#         sp.append(sim)
#     return sp
# print(shivrovka("shdcfbtkyuastrgfureayigcsfljdagyigAW"))
#
# def deshivrovka(a):
#     st=""
#     for i in a:
#         sim=chr(i+96)
#         st=st+sim
#     return st
# a = shivrovka("shdcfbtkyuastrgfureayigcsfljdagyigAW")
# print(deshivrovka(a))

# def diapozon():
#     for god in range(1000,4001):
#         for meshichi in range(1,13):
#             for deni in range(1,31):
#                 f = True
#                 data=str(deni)+str(meshichi)+str(god)
#                 for i in range(len(data)-1):
#                     if int(data[i])>int(data[i+1]):
#                         f=False
#                         break
#                 if f:
#                     print(str(deni)+"."+str(meshichi)+"."+str(god))
# diapozon()
#
import random as ran

# def generator():
#     st=""
#     for i in range(10000):
#         st=st+str(ran.randint(0,9))
#     print(st)
#     for i in range(len(st)-7):
#         data=st[i:i+8]
#         if 00<int(data[0:2])<32:
#             if 00<int(data[2:4])<13:
#                 print(str(data[0:2])+"."+str(data[2:4])+"."+str(data[4:8]))
# generator()

# def kvadratnie_polindromi():
#     for i in range(10000000):
#         i=str(i)
#         if int(i==i[::-1]) and  str(int(i)**2)==str(int(i)**2)[::-1]:
#             i=int(i)
#             print(i," ", i**2)
# kvadratnie_polindromi()

# def shift8(st):
#     st2=""
#     for i in st:
#         n=ord(i)
#         st2=st2+"*"*(n-96)+" "
#     return st2[:-1]
# print(shift8("abcd"))
#
# def shift28(st):
#     st=st.split()
#     st2=""
#     for i in st:
#         count = i.count("*")
#         st2=st2+chr(count+96)
#     return st2
# st = shift8("abcd")
# print(shift28(st))
#
# def milion():
#     n=""
#     with open("milion", "w") as file:
#         for i in range(1000000):
#             n=n+chr(ran.randint(97, 122))
#         file.write(n)
#
# def milion_read_legendarnoe_vozroshenie():
#     ms=""
#     m=0
#     kol=1
#     with open("milion", "r") as file:
#         data=file.read()
#         for i in range(len(data)-1):
#             if data[i]==data[i+1]:
#                 kol = kol+1
#             else:
#                 kol = 1
#             if kol > m:
#                 m = kol
#                 ms=data[i]
#     print(m, ms)
# milion_read_legendarnoe_vozroshenie()
#
# def milion_poisk():
#     ms=""
#     m=0
#     dikt={}
#     with open("milion", "r") as file:
#         data=file.read()
#         for i in range(len(data)-1):
#             if data[i]=="a":
#                 if data[i+1] in dikt:
#                     dikt[data[i + 1]]=dikt[data[i + 1]]+1
#                 else:
#                     dikt[data[i + 1]]=1
#         for i,j in dikt.items():
#             if j>m:
#                 m=j
#                 ms=i
#     print(dikt)
#     print(ms,m)
# milion_poisk()
#
# def milion_neznau():
#     ms=""
#     m=0
#     with open("milion", "r") as file:
#         data = file.read()
#         data = data.split("a")
#         for i in range(len(data)-1):
#             if len(data[i]+"a"+data[i+1])>m:
#                 m = len(data[i]+"a"+data[i+1])
#                 ms = data[i]+"a"+data[i+1]
#     print(m, ms)
#
# milion_neznau()
#
# def milion_neznau2():
#     ms=""
#     m=0
#     with open("milion", "r") as file:
#         data = file.read()
#         data = data.split("a")
#         for i in range(len(data)-5):
#             if len(data[i]+"a"+data[i+1]+"a"+data[i+2]+"a"+data[i+3])>m:
#                 m = len(data[i]+"a"+data[i+1]+"a"+data[i+2]+"a"+data[i+3])
#                 ms = data[i]+"a"+data[i+1]+"a"+data[i+2]+"a"+data[i+3]
#     print(m, ms)
# milion_neznau2()
#
# def milion2():
#     n = ""
#     with open("milion2", "w") as file:
#         for i in range(1000000):
#             n = n + str(ran.randint(1, 9))
#         file.write(n)
#
# def milion2_neponimau2():
#     kol = 0
#     with open("milion2", "r") as file:
#         data = file.read()
#         for i in range(len(data)-4):
#             flag = True
#             chislo = int(data[i:i+4])
#             if chislo == 8128:
#                 kol=kol+1
#     print("8128 встречается", str(kol), "раз(а)")
# milion2_neponimau2()

# def milion2_neponimau3():
#     sp = []
#     kol = 1
#     chislo = ""
#     maks = 0
#     with open("milion2", "r") as file:
#         data = file.read()
#         for i in range(len(data)-1):
#             if int(data[i])<int(data[i+1]):
#                 chislo = chislo + data[i]+data[i+1]
#                 kol = kol+1
#             else:
#                 if kol > 1:
#                     sp.append(chislo)
#                 chislo = ""
#                 kol = 1
#     print(sp)
# milion2_neponimau3()
#
# def milion_neponimau():
#     sp=[]
#     with open("milion2", "r") as file:
#         data = file.read()
#         for i in range(len(data)-4):
#             flag = True
#             chislo = int(data[i:i+4])
#             for j in range(2, chislo):
#                 if chislo % j==0:
#                     flag = False
#                     break
#             if flag == True:
#                 sp.append(chislo)
#     print(sp)
# milion_neponimau()
#
# def treygoliniki():
#     kol=0
#     with (open("ege17text", "r") as file):
#         data=file.readlines()
#         for i in data:
#             sp=[int(x) for x in i.split()]
#             sp.sort()
#             if sp[0]+sp[1]>sp[2]:
#                 kol=kol+1
#     print(kol)
# treygoliniki()

# def AAAAAAAAAAAAAAAAA():
#     kol=0
#     with open("test2.txt", "r") as file:
#         data=file.readlines()
#         for i in data:
#             sp=[int(x) for x in i.split()]
#             x=[x for x in sp if sp.count(x)==2]
#             y=[x for x in sp if sp.count(x)==1]
#             if len(x)==2 and len(y)==4:
#                 if sum(y)/len(y)<=sum(x):
#                     kol=kol+1
#     print(kol)
# AAAAAAAAAAAAAAAAA()

def dvenadcsati():
    with open("test2.txt", "r") as file:
            data=[int(x) for x in file.readlines()]
            for i in data:
                chet=[int(x) for x in data if x%2==0]
                nechet = [int(x) for x in data if x % 2 == 1]
                sp=[int(x) for x in str(i).split()]
                print(chet, nechet)
                # if sp.count(i)==1:
dvenadcsati()