import random

alf = ['А', 'Б', 'В', 'Г', 'Д', 'Е','Ё','Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н',
 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
phr = list('леопард не может изменить своих пятен тчк'.upper().replace(' ', ''))
block = [
         ['C','4','6', '2', 'A', '5', 'B', '9', 'E', '8', 'D', '7', '0', '3', 'F', '1'],
         ['6', '8', '2', '3', '9', 'A', '5', 'C', '1', 'E', '4', '7', 'B', 'D', '0', 'F'],
         ['B', '3', '5', '8', '2', 'F', 'A', 'D', 'E', '1', '7', '4', 'C', '9', '6', '0'],
         ['C', '8', '2', '1', 'D', '4', 'F', '6', '7', '0', 'A', '5', '3', 'E', '9', 'B'],
         ['7', 'F', '5', 'A', '8', '1', '6', 'D', '0', '9', '3', 'E', 'B', '4', '2', 'C'],
         ['5', 'D', 'F', '6', '9', '2', 'C', 'A', 'B', '7', '8', '1', '4', '3', 'E', '0'],
         ['8', 'E', '2', '5', '6', '9', '1', 'C', 'F', '4', 'B', '0', 'D', 'A', '3', '7'],
         ['1', '7', 'E', 'D', '0', '5', '8', '3', '4', 'F', 'A', '6', '9', 'C', 'B', '2']]
b_index = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

def gamma(phr,t,a,c):
    T = []
    T.append(t)
    for i in range(len(phr)):
        T.append((a * T[i] + c) % len(alf))
    T=T[1:]
    return T

def isint(n):
    try:
        n = int(n)
        return n
    except:
        return False

def shennon_crypt(phr):
    crypt = []
    for i in range(len(phr)):
    #    key.append(random.randint(0, len(alf)-1))
        phr[i] = alf.index(phr[i])
    t = isint(input('Введите порождающее число: '))
    while not t or t<0:
        t = isint(input('Введите корректное порождающее число: '))
    a = isint(input('Введите a: '))
    while not a or a<0 or a%4!=1:
        a = isint(input('Введите корректное a: '))
    c = isint(input('Введите c: '))
    while not c or c<0 or c%2==0:
        c = isint(input('Введите корректное c: '))
    key = gamma(phr, t, a, c)
    print('Числовоее представление фразы:',phr)
    crypt = [alf[ord(chr((i + j) % len(alf)))] for i,j in zip(phr,key)]
    print('Гамма:',key)
    return crypt

def shennon_decrypt(phr):
    for i in range(len(phr)):
        phr[i] = alf.index(phr[i])
    t = isint(input('Введите порождающее число: '))
    while not t or t<0:
        t = isint(input('Введите корректное порождающее число: '))
    a = isint(input('Введите a: '))
    while not a or a<0 or a%4!=1:
        a = isint(input('Введите корректное a: '))
    c = isint(input('Введите c: '))
    while not c or c<0 or c%2==0:
        c = isint(input('Введите корректное c: '))
    key = gamma(phr, t, a, c)
    decrypt=[]
    for i in range(len(key)):
        for j in range(len(alf)):
            if((j+key[i]) % len(alf)) == phr[i]:
                decrypt.append(alf[j])
    #s = []
    #print()
    #decrypt = [ord(chr((i + j) % len(alf))) for i,j in zip(phr,key)]
    #print('Числовое представление расшифровки:',decrypt)
    #decrypt = [alf[i] for i in decrypt]
    return decrypt

#s = shennon_crypt(phr)
#print('Шифртекст:',''.join(s),'\n')
#print('Расшифровка:',''.join(shennon_decrypt(s)),'\n')

def get_keys(key, mode):
    keys = []
    for i in range(mode):
        for i in range(8):
            keys.append(key[i%8*8:(i%8+1)*8])
    for i in range(4-mode):
        for i in range(8):
            keys.append(keys[7-i])
    return keys

def replace(r,l,key,mode):
    keys = get_keys(key, mode)
    for i in keys:
        k = int(bin(int(i,16))[2:],2)
        tmp = hex((k + int(r,2)) % 2**32)[2:].zfill(8)
        new_r = ''
        for j in range(len(tmp)):
            new_r+=(block[7-j%8][b_index.index(tmp[j].upper())]).lower()
        bin_new_r=bin(int(new_r, 16))[2:]
        bin_new_r=bin_new_r.zfill(32)
        bin_new_r=bin_new_r[11:]+bin_new_r[:11]
        n12=bin(int(bin_new_r, 2)^int(l, 2))[2:]       
        n12=n12.zfill(32)
        l = r
        r = n12
    return r,l

def gost_gam(phr,key,sync):
    sync +='0'*(16-len(sync))
    for i in range(0,len(sync),16):
        try:
            b=sync[i:i+16]
            bin_b = bin(int(b,16))[2:].zfill(64)
            l=bin_b[:32]
            r=bin_b[32:]
        except:
            b = sync[i:]
            bin_b = bin(int(b,16))[2:].zfill(len(b)*4)
            if len(bin_b)>32:
                l=bin_b[:32]
                r=bin_b[32:].ljust(32, '0')
            else:
                l=bin_b[:32].ljust(32, '0')
                r='0'*32
    n3,n4 = replace(r,l,key,3)
    print('Выходной блок: ',hex(int(n3,2))[2:] + hex(int(n4,2))[2:] )
    return hex(int((n3+n4),2) ^ int(bin(int(phr,16))[2:],2))

def magma_crypt(phr, key, sync):
    hex_phr= ''.join(phr).encode("utf-8").hex()
    crypt=gost_gam(phr, key, sync)
    return crypt[2:]

def magma_decrypt(phr, key, sync):
    hex_phr=gost_gam(phr, key, sync)
    #text = bytearray.fromhex(hex_phr).decode('utf-8')    
    return hex_phr[2:]

key = 'ffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff'
sync = '12345678'
phr='92def06b3c130a59'
print('Фраза: ', phr)
print('Ключ: ', key)
print('Синхропосылка: ', sync)
s = magma_crypt(phr, key, sync)
print('Зашифрованное: ',s)
print('Расшифрованное: ',magma_decrypt(s, key, sync))