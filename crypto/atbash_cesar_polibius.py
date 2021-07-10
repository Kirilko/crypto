alf = ['А', 'Б', 'В', 'Г', 'Д', 'Е','Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н',
 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
phr = list('ЛЕОПАРДНЕМОЖЕТИЗМЕНИТЬСВОИХПЯТЕНТЧК')

#атбаш
def atbash(text):
    res = ''
    for i in text:
        res += alf[len(alf)-1-alf.index(i)]
    return res

print('АТБАШ')
s = atbash(phr)    
print(s)
print(atbash(s))
print('\n')

#Цезарь с указанным ключом
def cesar(text): #шифр
    encrypt = ''
    cesar_key = int(input('Ключ шифровки: '))
    for i in text:
        encrypt += alf[(alf.index(i)+cesar_key)%len(alf)]
    return encrypt

def cesar_decr(text): #расшифровка
    decrypt = ''
    cesar_key = int(input('Ключ расшифровки: '))
    for i in text:
        decrypt += alf[(alf.index(i)-cesar_key)]
    return decrypt

print('ЦЕЗАРЬ')
s = cesar(phr)
print(s)
print(cesar_decr(s))
print('\n')

#алфавит-квадрат
key = {
        'А':'11', 'Б':'12', 'В':'13', 'Г':'14', 'Д':'15', 'Е':'16',
        'Ж':'21', 'З':'22', 'И':'23', 'Й':'24', 'К':'25', 'Л':'26',
        'М':'31', 'Н':'32','О':'33', 'П':'34', 'Р':'35', 'С':'36',
        'Т':'41', 'У':'42', 'Ф':'43', 'Х':'44', 'Ц':'45', 'Ч':'46',
        'Ш':'51', 'Щ':'52', 'Ъ':'53', 'Ы':'54', 'Ь':'55', 'Э':'56',
        'Ю':'61', 'Я':'62'
    }

#Полибия
def polybius(text): #шифр
    crypt = ''
    for i in text:
        if i in key:
            crypt += key[i]
    return crypt

def polybius_decr(text): #расшифровка
    decrypt = ''
    for i in range(0,len(text),2):
        tmp = text[i]+text[i+1]
        for i in key:
            if key[i]==tmp:
                decrypt+=i
    return decrypt

print('ПОЛИБИЯ')
s = polybius(phr)
print(s)
print(polybius_decr(s))