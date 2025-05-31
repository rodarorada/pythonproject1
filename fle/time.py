



import time
import random as ran

# timestamp=time.time()
# print("прошло с 1970 года", timestamp)
#
# local_time=time.localtime()
# print("год", local_time.tm_year)
# print("минут", local_time.tm_min)
# print("секунд", local_time.tm_sec)

# rezimi={
#     1:{
#
#     }
# }

def kalkulator():
    t=""
    zizni=3
    rezim=None
    etaz = 1
    sloznast=10
    sloznast2=1
    print("режим?")
    print("1 - сложение    2 - вычитание\n\n3 - умножение   4 - деление(с округлением)\n")
    rezim = input()
    while True:
        a = ran.randint(sloznast2, sloznast)
        b = ran.randint(sloznast2, sloznast)
        c = my_calc(rezim, a, b, t)
        if c!=0:
            if etaz!=10:
                if zizni!=0:
                    if etaz!=0:
                        print(f"этаж - {etaz}             жизни - {zizni}")
                        start = time.time()
                        rezultat=input()
                        end=time.time()
                        if end-start<=10:
                            if rezultat == str(c):
                                print("правильно!")
                                etaz = etaz + 1
                                time.sleep(2)
                                sloznast=int(sloznast**1.25)
                                sloznast2=int(sloznast2*1.25)
                            else:
                                print(f"неправильно! правильный ответ {c}!")
                                time.sleep(2)
                                etaz=etaz-1
                                sloznast=int(sloznast/4)
                                zizni=zizni-1
                                sloznast2=int(sloznast2/1.25)
                        else:
                            if rezultat == str(c):

                                print("ты прав, но ты не успел!")
                                time.sleep(2)
                                etaz=etaz-1
                                sloznast=int(sloznast/4)
                                zizni=zizni-1
                                sloznast2 = int(sloznast2 / 1.25)
                            else:
                                print(f"ты не успел! правильный ответ {c}")
                                time.sleep(2)
                                etaz=etaz-1
                                sloznast=int(sloznast/4)
                                zizni=zizni-1
                                sloznast2 = int(sloznast2 / 1.25)
                    else:
                        print("ты не смог продержаться очень долго, но ты старался!")
                        return 0
                else:
                    print("у тебя нет жизней!")
                    return 0
            else:
                print("ты победил!")
                return 0
        else:
            return 0


def my_calc(rezim, a, b, t):
    if rezim == "1":
        c = a + b
        print(f"{a}+{b}=")
    elif rezim == "2":
        c = b - a
        print(f"{b}-{a}=")
    elif rezim == "3":
        c = a * b
        print(f"{a}*{b}=")
    elif rezim == "4":
        print("режим времено недоступен.")
        c=0
    else:
        print("нет!")
        c=0
        # c = b // a
        # print(f"{b}//{a}=")
    return c


# kalkulator()












sl = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}

def win_to_igrok(p):
    for line in p:
        if line.count(1)==3:
            return True

    flag=True
    for i in range(3):
        if p[i][0]!=1:
            flag=False
    if flag:
        return True

    flag=True
    for i in range(3):
        if p[i][1]!=1:
            flag=False
    if flag:
        return True

    flag=True
    for i in range(3):
        if p[i][2]!=1:
            flag=False
    if flag:
        return True

    if p[0][0]==1 and p[1][1]==1 and p[2][2]==1: return True
    if p[2][0] == 1 and p[1][1] == 1 and p[0][2]==1: return True
    return False

def win_to_computer(p):
    for line in p:
        if line.count(2)==3:
            return True

    flag=True
    for i in range(3):
        if p[i][0]!=2:
            flag=False
    if flag:
        return True

    flag=True
    for i in range(3):
        if p[i][1]!=2:
            flag=False
    if flag:
        return True

    flag=True
    for i in range(3):
        if p[i][2]!=2:
            flag=False
    if flag:
        return True

    if p[0][0]==2 and p[1][1]==2 and p[2][2]==2: return True
    if p[2][0] == 2 and p[1][1] == 2 and p[0][2]==2: return True
    return False

def player_move(p,sl):
    while True:
        print("ваш ход")
        otvet=input()
        if otvet.isdigit():
            otvet=int(otvet)
            if 0<otvet<10:
                koordinati=sl[otvet]
                if p[koordinati[0]][koordinati[1]]==0:
                    p[koordinati[0]][koordinati[1]]=1
                    return p
                else:
                    print("стоп")
            else:
                print("стоп")
        else:
            print("стоп")

def computer_move(p,sl):
    print("ход противника")
    while True:
        otvet=ran.randint(1,9)
        koordinati = sl[otvet]
        if p[koordinati[0]][koordinati[1]] == 0:
            p[koordinati[0]][koordinati[1]] = 2
            time.sleep(1)
            return p

def krestiki_noliki(sl):
    p=[[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
    ochered=ran.randint(0,1)
    for i in p:
        print(i)
    if ochered:
        p=player_move(p,sl)
        for i in p:
            print(i)

    while True:
        p=computer_move(p,sl)
        for i in p:
            print(i)
        if win_to_computer(p):
            print("компьютор победил")
            return 0
        p=player_move(p,sl)
        for i in p:
            print(i)
        if win_to_igrok(p):
            print("ты победил")
            return 0
# krestiki_noliki(sl)

p=[[1, 0, 2],
    [2, 1, 1],
    [1, 2, 2]]

print(win_to_igrok(p))