alf = ['А', 'Б', 'В', 'Г', 'Д', 'Е','Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н',
 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
phr = 'леопард не может изменить своих пятен тчк'.upper().replace(' ', '')
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
        #print(f'G[{i}] = '+hex(int(l,2))[2:], hex(int(r,2))[2:])
    return r,l

def crypt(phr,key):
    #phr = bytes(phr, 'utf-8').hex()
    for i in range(0,len(phr),16):
        try:
            b=phr[i:i+16]
            bin_b = bin(int(b,16))[2:].zfill(64)
            l=bin_b[:32]
            r=bin_b[32:]
        except:
            b = phr[i:]
            bin_b = bin(int(b,16))[2:].zfill(len(b)*4)
            if len(bin_b)>32:
                l=bin_b[:32]
                r=bin_b[32:].ljust(32, '0')
            else:
                l=bin_b[:32].ljust(32, '0')
                r='0'*32
    n1,n2 = replace(r,l,key,3)
    return hex(int(n1,2))[2:] + hex(int(n2,2))[2:]

def decrypt(phr, key):
    #phr = bytes(phr, 'utf-8').hex()
    for i in range(0,len(phr),16):
        b=phr[i:i+16]
        bin_b = bin(int(b,16))[2:].zfill(64)
        l=bin_b[:32]
        r=bin_b[32:]
        n1, n2 = replace(r,l,key,1)
    return hex(int(n1,2))[2:] + hex(int(n2,2))[2:] 

key='ffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff'
phr='92def06b3c130a59' 
print('Фраза: ', phr)
print('Ключ: ', key)
s = crypt(phr,key)
print('Шифр: ',s)
#print('--------------------------------')
print('Расшифр: ',decrypt(s,key))