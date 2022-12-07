from math import floor


def Algo(num, base):
    temp = floor(num / base)
    rem = []
    rem.append(str(num % base))
    num = temp
    while temp != 0:
        temp = floor(num / base)
        rem.append(str(num % base))
        num = temp


    print(''.join(str(rem[i]) for i in range(0, len(rem))[::-1]))


Algo(50, 2)
Algo(742, 16)
Algo(532, 4)
Algo(234, 3)
Algo(124, 8)