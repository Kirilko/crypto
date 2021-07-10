import random

alf = ['А', 'Б', 'В', 'Г', 'Д', 'Е','Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н',
 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
phr = list('Леопард не может изменить своих пятен тчк'.upper().replace(' ', ''))

def chk(phr):
    for i in phr:
        if i not in alf:
            return False
    return phr

def vertical_crypt(phr):
    tmp = chk(input('Введите ключ: ').replace(' ','').upper())
    while not tmp:
        tmp = chk(input('Введите корректный ключ: ').replace(' ','').upper())
    tmp = [alf.index(tmp[i]) for i in range(len(tmp))]
    key=[0 for i in tmp]
    while len(phr)%len(key)!=0:
        phr.append(random.choice(alf))
    t = 1
    for i in range(len(key)):
        for j in range(len(tmp)):
            if tmp[j] == min(tmp) and tmp[j]!=99:              
                key[tmp.index(tmp[j])] = t
                tmp[tmp.index(tmp[j])] = 99
                t+=1
    print('Ключ: ',key)
    array=[[0]*len(key) for i in range(round(len(phr)/len(key)))]
    for i in range(round(len(phr)/len(key))):
        for j in range(len(key)):
            if (i+1)%2==0:
                array[i][-1-j] = phr[j + i*len(key)]
            else:
                array[i][j] = phr[j + i*len(key)]
    crypto = []
    for i in array:
        print(i)
    for i in key:
        for j in range(round(len(phr)/len(key))):
            crypto.append(array[j][i-1])
    return crypto

def vertical_decrypt(phr):
    tmp = chk(input('Введите ключ: ').replace(' ','').upper())
    while not tmp:
        tmp = chk(input('Введите корректный ключ: ').replace(' ','').upper())
    tmp = [alf.index(tmp[i]) for i in range(len(tmp))]
    key=[0 for i in tmp]
    t = 1
    for i in range(len(key)):
        for j in range(len(tmp)):
            if tmp[j] == min(tmp) and tmp[j]!=99:              
                key[tmp.index(tmp[j])] = t
                tmp[tmp.index(tmp[j])] = 99
                t+=1
    t=0
    decrypt = [[0]*len(key) for i in range(round(len(phr)/len(key)))]
    for i in key:
        for j in range(round(len(phr)/len(key))):
            decrypt[j][i-1] = phr[t]
            t+=1
    #for i in range(len(decrypt)):
    #    if (i+1)%2==0:
    #        for j in range(len(decrypt[i])):
    #            decrypt[i] = decrypt[i].reverse()
    decr = []    
    for i in range(len(decrypt)):
        for j in range(len(decrypt[i])):
            if (i+1)%2==0:
                decr.append(decrypt[i][len(decrypt[i])-1-j])
            else:
                decr.append(decrypt[i][j])
    return decr

#s=vertical_crypt(phr)
#print('Зашифрованное: ',''.join(s))
#print('Расшифрованное: ',''.join(vertical_decrypt(s)), '\n')

def mirror(key):
    k = [[0,0] for i in range(len(key))]
    t=0 
    for i,j in key:
        k[t] = [i,9-j]
        t+=1
    for i in range(len(k)):
        for j in range(len(k)-1):
            if k[j][0]==k[j+1][0] and k[j][1]>k[j+1][1]:
                t=k[j][1]
                k[j][1] = k[j+1][1]
                k[j+1][1]=t
    return(k)

def rotate_180(key):
    k = [[0,0] for i in range(len(key))]
    t=0 
    for i,j in key:
        k[t] = [5-i,9-j]
        t+=1
    k = rev(k)
    return k

def rev(key):
    k = []
    for i in range(len(key)):
        k.append(key[len(key)-1-i])
    return k

def kardano_crypt(phr):
    k_key = [ (0,1), (1,0), (1,4), (1,6), (1,7), (2,1), (2,5), (2,9), (3,3), (3,7), (4,1), (5,2), (5,5), (5,6), (5,9)]
    crypt=[[0]*10 for i in range(6)]
    t=0
    for i,j in k_key:
        crypt[i][j] = phr[t]
        t+=1
    k_key = rotate_180(k_key)
    for i,j in k_key:
        crypt[i][j] = phr[t]
        t+=1
    k_key = mirror(k_key)
    for i,j in k_key:
        try:
            crypt[i][j] = phr[t]
            t+=1
        except:
            crypt[i][j] = random.choice(alf)
    for i in range(len(crypt)):
        for j in range(len(crypt[i])):
            if crypt[i][j]==0:
                crypt[i][j]= random.choice(alf)
    return crypt

def kardano_decrypt(crypt):
    k_key = [ (0,1), (1,0), (1,4), (1,6), (1,7), (2,1), (2,5), (2,9), (3,3), (3,7), (4,1), (5,2), (5,5), (5,6), (5,9)]
    decrypt = []
    for i,j in k_key:
        decrypt.append(crypt[i][j])
    k_key = rotate_180(k_key)
    for i,j in k_key:
        decrypt.append(crypt[i][j])
    k_key = mirror(k_key)
    for i,j in k_key:
        try:
            decrypt.append(crypt[i][j])
        except:
            print('s')
    return decrypt

s = kardano_crypt(phr)
t=[]
for i in s:
    for j in i:
        t.append(j)
    print(i)
print('Зашифрованное: ',''.join(t))
print('Расшифрованное: ',''.join(kardano_decrypt(s)))