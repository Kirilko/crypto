block = [
         ['C','4','6', '2', 'A', '5', 'B', '9', 'E', '8', 'D', '7', '0', '3', 'F', '1'],
         ['6', '8', '2', '3', '9', 'A', '5', 'C', '1', 'E', '4', '7', 'B', 'D', '0', 'F'],
         ['B', '3', '5', '8', '2', 'F', 'A', 'D', 'E', '1', '7', '4', 'C', '9', '6', '0'],
         ['C', '8', '2', '1', 'D', '4', 'F', '6', '7', '0', 'A', '5', '3', 'E', '9', 'B'],
         ['7', 'F', '5', 'A', '8', '1', '6', 'D', '0', '9', '3', 'E', 'B', '4', '2', 'C'],
         ['5', 'D', 'F', '6', '9', '2', 'C', 'A', 'B', '7', '8', '1', '4', '3', 'E', '0'],
         ['8', 'E', '2', '5', '6', '9', '1', 'C', 'F', '4', 'B', '0', 'D', 'A', '3', '7'],
         ['1', '7', 'E', 'D', '0', '5', '8', '3', '4', 'F', 'A', '6', '9', 'C', 'B', '2']]
temp = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
alf = ['А', 'Б', 'В', 'Г', 'Д', 'Е','Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н',
 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
phr = 'леопард не может изменить своих пятен тчк'.upper().replace(' ', '')

def convert_base(num, to_base=10, from_base=10):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]

if len(phr) % 2 != 0:
    phr+='А'

def crypt(phr):
    crypt = []
    hexed = []
    for i in phr:
        hexed.append(i.encode("utf-8").hex().upper())
    for i in range(len(hexed)):
        tmp=''
        for j in range(len(hexed[i])):
            t = j
            if (i+1)%2==0:
                t+=4
            tmp += block[t][int(convert_base(hexed[i][j],10,16))]
        crypt.append(tmp)
    return crypt

def decrypt(phr):
    decrypt = []
    decr=''
    for i in range(len(phr)):
        for j in range(len(phr[i])):
            t=j
            if (i+1)%2==0:
                t+=4
            decrypt.append(temp[block[t].index(phr[i][j])])
    return decrypt

s=crypt(phr)
print(''.join(s),'\n')
print(bytearray.fromhex(''.join(decrypt(s))).decode('utf-8'))