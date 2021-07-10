import random
import math
import numpy as np
from numpy import matrix
from numpy import linalg

alf = ['А', 'Б', 'В', 'Г', 'Д', 'Е','Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н',
 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
phr = list('леопард не может изменить своих пятен тчк'.upper().replace(' ', ''))

def isinst(n):
    try:
        n = int(n)
        return n
    except:
        return False

def minor(array,i,j):
    c = array
    c = c[:i] + c[i+1:]
    for k in range(0,len(c)):
        c[k] = c[k][:j]+c[k][j+1:]
    return c

def det(array,n):
    if n == 1 :return array[0][0]
    if n == 2 :return array[0][0]*array[1][1] - array[0][1]*array[1][0]
    sum = 0
    for i in range(0,n):
        m = minor(array,0,i)
        sum =sum + ((-1)**i)*array[0][i] * det(m,n-1)
    return sum

def matrix_crypt(phr):
    n = isinst(input('Введите размер матрицы:'))
    while not n or n<1:
        n = isinst(input('Введите корректный размер матрицы:'))
    key = []
    print('Введите элементы ключа') 
    for i in range(n):
        row = input(f'Введите строку {i+1}: ').split()
        while len(row)!=n:
            row = input(f'Введите строку {i+1} размером {n}: ').split()
        for i in row:
           key.append(int(i))
    array=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            array[i][j] = key[i * n + j]
    tmp = det(array, n)
    while tmp==0:
        print('У введенный матрицы нет обратной')
        key = []
        print('Введите элементы ключа') 
        for i in range(n):
            row = input(f'Введите строку {i+1}: ').split()
            while len(row)!=n:
                row = input(f'Введите строку {i+1} размером {n}: ').split()
            for i in row:
                key.append(int(i))
        tmp = det(array,n)
    while len(phr)%n!=0:
        phr.append(random.choice(alf))
    phr_arr = [(alf.index(i)+1) for i in phr]
    vec = []
    for i in range(0,len(phr_arr),n):
        vec.append([phr_arr[j] for j in range(i,i+n)])
    crypto=[]
    for i in vec:
        for j in range(0,len(key),n):
            cr=0
            l=n-1
            while l>-1:
                cr+=key[j+l]*i[l]
                #print(cr, l)
                l-=1
            crypto.append(cr)
    return crypto

def matrix_decrypt(phr):
    n = isinst(input('Введите размер матрицы:'))
    while not n or n<1:
        n = isinst(input('Введите корректный размер матрицы:'))
    key = []
    print('Введите элементы ключа') 
    for i in range(n):
        row = input(f'Введите строку {i+1}: ').split()
        while len(row)!=n:
            row = input(f'Введите строку {i+1} размером {n}: ').split()
        for i in row:
           key.append(int(i))
    array=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            array[i][j] = key[i * n + j]
    #d = det(array,n)
    a = np.array(array)
    a = np.linalg.inv(a)
    vec=[[0] for i in range(len(phr)//n)]
    tmp = 0
    for i in range(0,len(phr),n):
        vec[tmp]=[]
        for j in range(i,i+n):
            vec[tmp].append(phr[j])
        tmp+=1
    decr=[]
    decrypt=[]
    for i in vec:
        decr.append(np.dot(a,np.array(i)))
    for i in decr:
        for j in range(n):
            decrypt.append(alf[round(i[j])-1])
    return decrypt

s = matrix_crypt(phr)
print(s)
print(matrix_decrypt(s), '\n')

alf_p = ['А', 'Б', 'В', 'Г', 'Д',
         'Е','Ж', 'З', 'И',
         'К', 'Л', 'М', 'Н', 'О',
         'П', 'Р', 'С', 'Т', 'У', 
         'Ф', 'Х', 'Ц', 'Ч', 'Ш', 
         'Щ', 'Ь', 'Ы', 'Э', 'Ю', 'Я']

def chk(key):
    for i in range(len(key)):
        if key[i] == 'ё'.upper():
            key[i] = 'Е'
        elif key[i] == 'Ъ'.upper():
            key[i] = 'Ь' 
        elif key[i] == 'й'.upper():
            key[i] = 'И'   
        if key[i] not in alf_p:
            return False 
    return key

def playfer_crypt(phr):
    n=6
    #phr = chk(phr)
    key = chk(list(input('Введите ключ: ').upper()))
    while not key:
        key = chk(list(input('Введите корректный ключ: ').upper()))
    new_alf=[]
    for i in key:
        if i not in new_alf:
            new_alf.append(i)
    for i in alf_p:
        if i not in new_alf:
            new_alf.append(i)
    crypto = []
    new_phr=[]
    for i in range(0,len(phr),2):
        new_phr.append(phr[i])
        try:
            if phr[i]==phr[i+1]:
                new_phr.append('Ф')
            new_phr.append(phr[i+1])
        except:
            break
    phr = new_phr
    print(phr)
    while len(phr)%2!=0:  
        phr.append(random.choice(new_alf))
    array=[[0]*n for i in range(n-1)]
    for i in range(n-1):
        for j in range(n):
            array[i][j] = new_alf[i * n + j] 
    for i in array:
        print(i)
    temp=[[0]*(n-1) for i in range(n)]
    for i in range(n):
        for j in range(n-1):
            temp[i][j] = array[j][i]
    for l in range(0,len(phr),2):
        w = [phr[l],phr[l+1]]
        tmp=True
        for i in array:
            if w[0] in i and w[1] in i:
                crypto.append(i[(i.index(w[0])+1)%n])
                crypto.append(i[(i.index(w[1])+1)%n])
                tmp=False
        if tmp:
            for i in temp:
                if w[0] in i and w[1] in i:
                    crypto.append(i[(i.index(w[0])+1)%(n-1)])
                    crypto.append(i[(i.index(w[1])+1)%(n-1)])
                    tmp=False
        if tmp:
            d1 = new_alf.index(w[0])% n
            d2 = new_alf.index(w[1])% n
            if d1>d2:
                crypto.append(new_alf[new_alf.index(w[0])-(d1-d2)])
                crypto.append(new_alf[new_alf.index(w[1])+(d1-d2)])
            else:
                crypto.append(new_alf[new_alf.index(w[0])+(d2-d1)])
                crypto.append(new_alf[new_alf.index(w[1])-(d2-d1)])
        print(crypto)
    return crypto
        
def playfer_decrypt(phr):
    n=6
    key = chk(list(input('Введите ключ: ').upper()))
    while not key:
        key = chk(list(input('Введите корректный ключ: ').upper()))
    new_alf=[]
    for i in key:
        if i not in new_alf:
            new_alf.append(i)
    for i in alf_p:
        if i not in new_alf:
            new_alf.append(i)
    crypto = []
    array=[[0]*n for i in range(n-1)]
    for i in range(n-1):
        for j in range(n):
            array[i][j] = new_alf[i * n + j] 
    temp=[[0]*(n-1) for i in range(n)]
    for i in range(n):
        for j in range(n-1):
            temp[i][j] = array[j][i]
    for l in range(0,len(phr),2):
        w = [phr[l],phr[l+1]]
        tmp=True
        for i in array:
            if w[0] in i and w[1] in i:
                crypto.append(i[(i.index(w[0])-1)])
                crypto.append(i[(i.index(w[1])-1)])
                tmp=False
        if tmp:
            for i in temp:
                if w[0] in i and w[1] in i:
                    crypto.append(i[i.index(w[0])-1])
                    crypto.append(i[i.index(w[1])-1])
                    tmp=False
        if tmp:
            d1 = new_alf.index(w[0])% n
            d2 = new_alf.index(w[1])% n
            if d1>d2:
                crypto.append(new_alf[new_alf.index(w[0])-(d1-d2)])
                crypto.append(new_alf[new_alf.index(w[1])+(d1-d2)])
            else:
                crypto.append(new_alf[new_alf.index(w[0])+(d2-d1)])
                crypto.append(new_alf[new_alf.index(w[1])-(d2-d1)])
    return crypto

#s = playfer_crypt(phr)
#print(s)
#print(playfer_decrypt(s))