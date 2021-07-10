
def isInt(string):
    try:
        int(string)
        return True
    except:
        return False

def user_input(param):
    someIn = input(f'Введите {param}: ')
    while (not isInt(someIn)):
        someIn = input(f'Введите число {param}: ')
    return int(someIn)

def Diffie_Hellman_key(a, n, k):
    y = a**k % n
    return y

def Diffie_Hellman_check(y, n, k):
    K = y**k % n
    return K

n = user_input('n')
while n<3:
    n = user_input('n больше 2')
a = user_input('a')
while a<1 or a>=n:
    a = user_input(f'a больше 1 и меньше {n}')
kA = user_input('k первого участника')
while kA<2 or kA>(n-1):
    kA = user_input(f'k больше 1 и меньше {n}')
kB = user_input('k второго участника')
while kB<2 or kB>(n-1):
    kB = user_input(f'k больше 1 и меньше {n}')

yA = Diffie_Hellman_key(a,n,kA)
yB = Diffie_Hellman_key(a,n,kB)
print(f'Ключ yA первого участника: {yA}')
print(f'Ключ yB второго участника: {yB}')

k1 = Diffie_Hellman_check(yA,n,kB)
k2 = Diffie_Hellman_check(yB,n,kA)
print(f'Ключи: k1 = {k1}, k2 = {k2}')
if k1 == k2:
   print ("Общий ключ ", k1)
else:
    print("Ошибка в расчете общего ключа ")