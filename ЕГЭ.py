

# x="9"*127
# while "333" in x or "999" in x:
#     if "333" in x:
#         x=x.replace("333", "9", 1)
#     else:
#         x=x.replace("999","3",1)
# print(x)



x="1"+"9"*98
while "19" in x or "299" in x or "3999" in x:
    x=x.replace("19","2",1)
    x = x.replace("299", "3",1)
    x = x.replace("3999", "1",1)

print(x)