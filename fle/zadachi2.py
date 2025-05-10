# def dvenadcsati():
#     with open("test2.txt", "r") as file:
#             data=[int(x) for x in file.readlines()]
#             for i in data:
#                 chet=[int(x) for x in data if x%2==0]
#                 nechet = [int(x) for x in data if x % 2 == 1]
#                 sp=[int(x) for x in str(i).split()]
#                 print(chet, nechet)
#                 # if sp.count(i)==1:
# dvenadcsati()
#
# def dvadchatshest():
#     sp2=[]
#     with open("test4.txt", "r") as file:
#         data=file.readlines()
#         S=int(data[0].split()[0])
#         print(S)
#         sp=[int(x) for x in data[1:]]
#         sp.sort()
#         for i in sp:
#             if i+sum(sp2)<=S:
#                 sp2.append(i)
#         for i in sp[::-1]:
#             if i+sum(sp2[:-1])<=S:
#                 sp2[-1]=i
#                 break
#         print(len(sp2), sp2)
# dvadchatshest()

def shestnadchat():
    suma=0
    sp2=[]
    with open("test4.txt", "r") as file:
        data=file.readlines()
        sp = [int(x) for x in data[1:]]
        for i in sp:
            if i>50
                sp2.append(i)
                suma=suma+i
        sp2.sort()
        for i in range(len(sp2)):
            if i<len(sp2)//2: