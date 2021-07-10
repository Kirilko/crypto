alf = ['А', 'Б', 'В', 'Г', 'Д', 'Е','Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н',
 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
phr = list('ЛЕОПАРДНЕМОЖЕТИЗМЕНИТЬСВОИХПЯТЕНТЧК')

def tritemius_crypt(text):
    j=0
    crypt=''
    for i in text:
        crypt+=alf[(alf.index(i)+j)%len(alf)]
        j+=1
    return crypt

def tritemius_decr(text):
    j=0
    decrypt=''
    for i in text:
        decrypt+=alf[(alf.index(i)-j)%len(alf)]
        j+=1
    return decrypt

print("ТРИТЕМИЙ")
s=tritemius_crypt(phr)
print(s)
print(tritemius_decr(s)+'\n')

def belaso_crypt(text):
    key = list(input('Введите ключ: ').replace(' ','').upper())
    for i in key:
        if not i in alf:
            return 'Ключ содержит недопустимые символы'
    crypt = ''
    j=0
    for i in text:
        crypt+=alf[(alf.index(key[j%len(key)]) + alf.index(i)) % len(alf)]
        j+=1
    return crypt

def belaso_decrypt(text):
    key = list(input('Введите ключ: ').replace(' ','').upper())
    for i in key:
        if not i in alf:
            return 'Ключ содержит недопустимые символы'
    crypt = ''
    j=0
    for i in text:
        crypt+=alf[(alf.index(i) - alf.index(key[j%len(key)])) % len(alf)]
        j+=1
    return crypt

print("БЕЛАЗО")
s = belaso_crypt(phr)
print(s)
print(belaso_decrypt(s),'\n')

def vizhener_crypt(text):
    key=[]
    while len(key)!=1:
        key.append( input('Введите ключ длиной 1: ').upper())
    key+=phr[:-1]
    crypt=''
    j=0
    for i in text:
        crypt+=alf[(alf.index(key[j%len(key)]) + alf.index(i)) % len(alf)]
        j+=1
    return crypt

def vizhener_decrypt(text):
    key=[]
    while len(key)!=1:
        key.append( input('Введите ключ длиной 1: ').upper())
    key+=phr[:-1]
    crypt=''
    j=0
    for i in text:
        crypt+=alf[(alf.index(i) - alf.index(key[j%len(key)])) % len(alf)]
        j+=1
    return crypt

print('ВИЖЕНЕР')
s = vizhener_crypt(phr)
print(s)
print(vizhener_decrypt(s))
