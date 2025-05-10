
# # #
# # # with open("my_text_fle1.txt","r",encoding="utf-8") as file:
# # #     Content=file.read()
# # #     print(Content)
# # #
# # # file.close()
# #
# #
# #
# #
# #
# # # with open("fle/massiv.txt","r",encoding="utf-8") as file:
# # #     mass=[]
# # #     for i in file:
# # #         i=int(i)
# # #         mass.append(i)
# # #     mass.sort()
# # # with open("fle/ch1.txt","w",encoding="utf-8") as file:
# # #     file.write(str(mass[-1]))
# #
# #
# # string="1 2 3 4 5 6 8 4 6"
# # mass=[int(x) for x in string.split()]
# # print(mass)
#
#
# with ]
#     mass=[]
#     for line in file:
#       open("fle/rtvtrtbum","r",encoding="utf-8") as file:
# # # #     rs=[  mass=[int(x) for x in line.split()]
#         mass.sort()
#         rs.append(mass[-1])
#     print(rs)
# with open("fle/ch2","w",encoding="utf-8") as file:
#     for i in range(len(rs)):
#         file.write(str(rs[i])+"\n")

# with open("fle/aa","r",encoding="utf-8") as file:
#     count=0
#     mass=[]
#     for line in file:
#         mass=[x for x in line.split()]
#         count=count+len(mass)
#     print(count)
#
with open("fle/dthc","r",encoding="utf-8") as file:
    summ=0
    for line in file:
        summ=summ+int(line)
    print(summ)

# with open("fle/dthc","w",encoding="utf-8") as file:
#     mass=[]
#     for line in file:
#         mass=[x for x in line.split()]
#     print(mass)