import fractions
import numpy as np
alf = ['А', 'Б', 'В', 'Г', 'Д', 'Е','Ж', 'З', 'И',  'К', 'Л', 'М', 'Н',
 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
phr = list('ДЕВА'.replace(' ','').upper())

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
    #return tmp , s, ost
    return tmp

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
#--------------------------------------------------------------------------------------------------------
def ecc(tmp,c):
    ans = [0 for i in range(c+1)]
    ans[1] = tmp
    i = 1
    while i<c:
        try:
            if i*2<=c:
                l_n = (3*ans[i][0]**2 + a)
                l_d = (2*ans[i][1])
                x_d = l_d**2
                x_n = l_n**2 - 2*ans[i][0]*x_d
                x = ans_d(euclidian(p, x_d), x_n, p)
                y_n = l_n * (ans[i][0] - x) - ans[i][1]*l_d
                y = ans_d(euclidian(p, l_d), y_n, p)
                i*=2
                ans[i]=[x,y]
            else:
                l_n = ans[i][1] - ans[1][1]
                l_d = ans[i][0] - ans[1][0]
                x_d = l_d**2
                x_n = l_n**2 - (ans[i][0] + ans[1][0]) * x_d
                x = ans_d(euclidian(p, x_d), x_n, p)
                y_n = l_n*(ans[i][0] - x) - ans[i][1]*l_d
                #y = ans_d(euclidian(p, l_d), y_n, p)
                y = int(y_n / l_d % p)
                i+=1
                ans[i]=[x,y]
        except:
            i+=1
    print(f'[{i}]({g[0]},{g[1]}) = {ans[-1]}')
    return ans[-1]

def hash(phr):
    h=[0]
    index=1
    p=11
    for i in phr:
        t=((h[index-1]+alf.index(i)+1)**2) % p
        h.append(t)
        index+=1
    return(h)

def table():
    tmp = np.array([i**2 % p for i in range(p)])
    y = np.array([(i**3 + a*i + b) % p for i in range(p)])
    points=[]
    e=1
    s=[]
    for i in range(p):
        if(y[i] in tmp):
            t=np.where(tmp == y[i])[0]
            points.append(t)
            e+=len(t)
            s.append([i,t[0]])
            try: s.append([i,t[1]])
            except: continue
        else:
            points.append('-')
        print(i, y[i], points[i])
    return e, s

#print(''.join(phr))
#a = user_input('a')
#b = user_input('b')
#p = user_input('p')
#while p<=3:
#    p = user_input('p больше 3')
##a = 1
##b = 3
##p = 7
#e, points = table()
#print(f'#E={e}')
#print(f'Точки: {points}')
#g=[]
#for i in range(2):
#    tmp = input(f'Введите G[{i}]: ')
#    while(not isInt(tmp)):
#        tmp = input(f'Введите число G[{i}]: ')
#    g.append(int(tmp))
#for i in range(2,7):
#    ecc(g,i)
#---------------------------------------------------------------------------------------
#g=[5,7]
#Cb=6
#k = 5
#phr = ((10,3), 6)
#print(f'a = {a}\nb = {b}\np = {p}\nG = {g}\nCb = {Cb}\nk = {k}\nШифртекст = {phr}')
#
#e, points = table()

#q = e/2
#print(f'q = {q}')
#print(points)
#Db = ecc(g,Cb)
#R = ecc(g,k)
##P = ecc(Db,k)
#g = [0,6]
#print(f'[{2}]{g} = {ecc([0,6],2)}')
#for i in points:
#print(ecc([1,13], 40))
#for i in points:
#    print(ecc(i, p))
#x = user_input('x')
#while x>=q or x<0:
#    x = user_input(f'x меньше {q} и больше 0')
#k = user_input('k')
#while k>=q or k<0:
#    k = user_input(f'k меньше {q} и больше 0')



#for i in range(2):
#    tmp = input(f'Введите G[{i}]: ')
#    while(not isInt(tmp)):
#        tmp = input(f'Введите число G[{i}]: ')
#    g.append(int(tmp))

#Y = ecc(g, x)
#c = user_input('C')
#while (c<1):
    #с = user_input(f'C больше 1 и меньше {q}')
#for i in range(len(phr)):
#    phr[i] = alf.index(phr[i])
def ECC_sign(phr):
    global k
    h = hash(phr)[-1]
    print('h:',h)
    P = ecc(g, k)
    print('P:',P)   
    r = P[0] % q
    print('r:',r)
    while r==0:
        k = user_input(f'k меньше {q}')
        P = ecc(g, k)
        r = p[0] % q
    s = (k*h + r*x) % q
    print('s:',s)
    return (phr,r,s)

def ECC_check(s):
    h = hash(s[0])[-1]
    print('h:',h)
    if s[1]>0 and s[2]<q:
        u1 = int(ans_d(euclidian(q, h), s[2], q))
        u2 = int(ans_d(euclidian(q, h), -(s[1]), q))
        print(f'u1 = {u1}, u2 = {u2}')
        t1 = ecc(g, u1)
        t2 = ecc(Y, u2)
        l_n = t1[1] - t2[1]
        l_d = t1[0] - t2[0]
        x_d = l_d**2
        x_n = l_n**2 - (t1[0] + t2[0]) * x_d
        x = ans_d(euclidian(p, x_d), x_n, p)
        y_n = l_n*(t1[0] - x) - t2[1]*l_d
        #y = ans_d(euclidian(p, l_d), y_n, p)
        y = int(y_n / l_d % p)
        ans=[x,y]
        print('P:',ans)
        if ans!=[0,0] and x % q == s[1]:
            print('x mod q:',x%q)
            return 'Подпись принята'
        else:
            return 'Подпись неверна' 
    else:
        return 'Подпись неверна'    

def ECC_crypt(phr):
    d = ecc(g,c)
    print('d:',d)
    #m = user_input('m')
    r = ecc(g,k)
    print('r:',r)
    P = ecc(d,k)
    print('p:',P)
    ans = []
    for m in phr:
        e = (m * P[0]) % p
        ans.append(((r[0],r[1]),e))
    #print('e:',e)
    #return ((r[0],r[1]),e)
    return ans

def ECC_decrypt(phr, s):
    ans = []
    for i in s:
        q = ecc([i[0][0],i[0][1]], c)
        m = ans_d(euclidian(p, q[0]), i[1], p)
        ans.append(m)
    return ans



#s = ECC_crypt(phr)
#print('Шифр:',s)
#print('Расшифр:',''.join([alf[i] for i in phr]))
#''.join([alf[i] for i in ECC_decrypt(phr, s)])

#s = ECC_sign(phr)
#print(s)
#print(ECC_check(s))
x=16
p=23

a=14
b=2
#print(11**x % p)
print(2*18*8*13 % 23)

#print(3**814 % 11)
#print(9*3*9*4*9*5 % 11)