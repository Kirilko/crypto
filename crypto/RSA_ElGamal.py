from math import gcd as bltin_gcd
alf = ['А', 'Б', 'В', 'Г', 'Д', 'Е','Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н',
 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
phr = list('ЛЕОПАРДНЕМОЖЕТИЗМЕНИТЬСВОИХПЯТЕНТЧК'.replace(' ','').upper())

def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

def hash(phr):
    h=[0]
    index=1
    p=33
    for i in phr:
        t=((h[index-1]+alf.index(i)+1)**2) % p
        h.append(t)
        index+=1
    return(h)

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

def euclidian(tmp1,tmp2):
    tmp=[]
    ost=[]
    s = []
    #if tmp1>tmp2:
    #    t=tmp2
    #    tmp2=tmp1
    #    tmp1=t
    while tmp1>0:
        tmp.append(tmp1//tmp2)
        s.append((tmp1//tmp2) * tmp2)
        t=tmp2
        tmp2 = tmp1%tmp2
        ost.append(tmp2)
        
        if tmp2 == 0:
            break  
        tmp1=t
    return tmp , s, ost

    #return tmp

print(euclidian(107,177))

def ans_d(tmp, y, p):
    tmp1=1
    mas=[]
    mas.append(tmp1)
    for j in range(len(tmp)-1):
        tmp1*=tmp[j]
        if j>0:
            tmp1+=mas[j-1]
        mas.append(tmp1)
    d=(((-1)**(len(tmp)-1)) * mas[-1] * y) % p
    return d

print(ans_d(euclidian(107,177)[0],-3,177))

def crypt_rsa(phr,p,q,e,n):
    crypt=list()
    for i in phr:
        crypt.append((alf.index(i)+1)**e % n)
    return crypt

def decrypt_rsa(crypt,p,q,d,n):
    decrypt = crypt
    for i in range(len(decrypt)):
        decrypt[i] = alf[int(decrypt[i]**d % n)-1]
    return decrypt
    
def RSA(phr):
    print(''.join(phr))
    p = user_input('p')
    q = user_input('q')
    n=p*q
    f=(p-1)*(q-1)
    e = user_input('e')
    while(bltin_gcd(f,e)!=1):
        e = user_input(f'e взаимнопростое с f - {f}')
    d = ans_d(euclidian(f,e),1,f)
    print(f'p = {p}, q = {q}, e={e}, n={n}, d={d}')
    #s = crypt_rsa(phr,p,q,e,n)
    #print(''.join(['0'*(3-len(str(i)))+str(i) for i in s]))    
    #print(''.join(decrypt_rsa(s,p,q,d,n)))
    s = RSA_sign(hash(phr), d, n)
    print('S = ', s)
    if RSA_check(s, e, n):
        print('Подпись прошла')

def RSA_sign(m,d,n):
    s = (m[-1]**d) % n
    return s

def RSA_check(s,e,n):
    m2 = s**e % n
    print('m = ', m2)
    return m2 == hash(phr)[-1]

#RSA(phr)
#m = hash(phr)
#print(m)
#s = (m[-1]**d) % n
#print(s)
#m2 = s**e % n
#print(m2)
#print(f"p={p}, q={q}, e={e} \nn=p*q={n}, d={d} \nm={m[-1]}, s={s}")
#
##print(f"p={p}, q={q}, e={e} \nn=p*q={n}, d={d}")
#print(f"Зашифрованное: {crypt}")
from random import randint

def decrypt_ElGamal(crypt,p,x):
    decrypt=[]
    for i in crypt:
        eu = euclidian(i[0]**x,p)
        decrypt.append(ans_d(eu, i[1], p))
    for i in range(len(decrypt)):
        decrypt[i] = alf[int(decrypt[i])-1]
    return decrypt

def crypt_ElGamal(M,p,g,y):
    k = [3,11,13]
    crypt=[]
    for i in M:
       rnd=randint(0,2)
       a=g**k[rnd] % p
       b=((y**k[rnd]) * i) % p 
       crypt.append((a,b))
    return crypt


def ElGamal(phr):
    print(''.join(phr))
    p=user_input('p')
    while(not isPrime(p)):
        print(' p должно быть простым')
        p=user_input('p')
    x=user_input('x')
    while(x>=p or x<=1):
        print(' x должен быть меньше p и больше 1')
        x=user_input('x')
    g=user_input('g')
    while(g>=p or g<=1):
        print(' g должна быть меньше p и больше 1')
        g=user_input('g')
    y=(g**x) % p
    print('y = ', y)
    M=[]
    for i in phr:
        M.append(alf.index(i)+1)
    #s = crypt_ElGamal(M,p,g,y)
    #print(s)
    #print(''.join(decrypt_ElGamal(s,p,x)))
    s = ElGamal_sign(phr, 13, g, p, x)
    print('S = ', s)
    if ElGamal_check(phr, s[0], s[1], p, y, g):
        print('Подпись прошла')

def ElGamal_sign(phr, k, g, p, x):
    a=(g**k) % p
    b = ans_d(euclidian(p-1, k), -(x*a-hash(phr)[-1]), p-1)
    return (a,b)

def ElGamal_check(phr, a, b, p, y, g):
    m = hash(phr)[-1]
    a1 = ans_d(euclidian(p,1), (y**a) * (a**b), p)
    print('A1 = ',a1)
    #((y**a) * (a**b)) % p
    #g**m % p
    a2 = ans_d(euclidian(p,1), g**m, p)
    print('A2 = ',a2)
    return a1==a2

#ElGamal(phr)