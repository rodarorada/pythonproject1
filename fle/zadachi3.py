



from itertools import *
#
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