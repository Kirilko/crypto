import copy

def registers(key): #загружает регистры
	x = []
	y = []
	z = []
	#e = []
	for i in range(64):
		if i<19:
			x.append(int(key[i]))
		elif i<41:
			y.append(int(key[i]))
		else:
			z.append(int(key[i]))
	#for i in range(17): 
	#	e.append(int(key[i])) 
	#print(''.join([str(i) for i in x]),''.join([str(i) for i in y]),''.join([str(i) for i in z]))
	return x,y,z

def str_to_bin(plain): #переводит строку в бинарный формат
	bin_phr= bin(int(plain.encode("utf-8").hex(),16))[2:]
	while len(bin_phr) % 8 !=0:
		bin_phr='0'+bin_phr
	bin_phr = [int(i) for i in bin_phr]
	return bin_phr#byte_list

def major(x,y,z): #управление тактированием
	if(x + y + z > 1):
		return 1
	else:
		return 0

def stream(length, x, y, z): #XOR битов регистра a5/1
	x_temp = copy.deepcopy(x)
	y_temp = copy.deepcopy(y)
	z_temp = copy.deepcopy(z)
	keystream = []
	i = 0
	while i < length:
		majority = major(x_temp[8], y_temp[10], z_temp[10])
		if x_temp[8] == majority: 
			new = x_temp[13] ^ x_temp[16] ^ x_temp[17] ^ x_temp[18]
			x_temp_two = copy.deepcopy(x_temp)
			j = 1
			while(j < len(x_temp)):
				x_temp[j] = x_temp_two[j-1]
				j = j + 1
			x_temp[0] = new
		if y_temp[10] == majority:
			new_one = y_temp[20] ^ y_temp[21]
			y_temp_two = copy.deepcopy(y_temp)
			k = 1
			while(k < len(y_temp)):
				y_temp[k] = y_temp_two[k-1]
				k = k + 1
			y_temp[0] = new_one
		if z_temp[10] == majority:
			new_two = z_temp[7] ^ z_temp[20] ^ z_temp[21] ^ z_temp[22]
			z_temp_two = copy.deepcopy(z_temp)
			m = 1
			while(m < len(z_temp)):
				z_temp[m] = z_temp_two[m-1]
				m = m + 1
			z_temp[0] = new_two
		keystream.insert(i, x_temp[18] ^ y_temp[21] ^ z_temp[22])
		i = i + 1
	return keystream

def stream_2(length, x, y, z, e): #XOR битов регистра a5/2 
	x_temp = copy.deepcopy(x)
	y_temp = copy.deepcopy(y)
	z_temp = copy.deepcopy(z)
	e_temp = copy.deepcopy(e)
	keystream = []
	i = 0
	while i < length:
		majority = major(e_temp[3], e_temp[7], e_temp[10])
		if e_temp[10] == majority: 
			new = x_temp[13] ^ x_temp[16] ^ x_temp[17] ^ x_temp[18]
			x_temp_two = copy.deepcopy(x_temp)
			j = 1
			while(j < len(x_temp)):
				x_temp[j] = x_temp_two[j-1]
				j = j + 1
			x_temp[0] = new
		if e_temp[3] == majority:
			new_one = y_temp[20] ^ y_temp[21]
			y_temp_two = copy.deepcopy(y_temp)
			k = 1
			while(k < len(y_temp)):
			    y_temp[k] = y_temp_two[k-1]
			    k = k + 1
			y_temp[0] = new_one
		if e_temp[7] == majority:
			new_two = z_temp[7] ^ z_temp[20] ^ z_temp[21] ^ z_temp[22]
			z_temp_two = copy.deepcopy(z_temp)
			m = 1
			while(m < len(z_temp)):
			    z_temp[m] = z_temp_two[m-1]
			    m = m + 1
			z_temp[0] = new_two
		keystream.insert(i, x_temp[18] ^ y_temp[21] ^ z_temp[22] ^ major(x_temp[12],x_temp[14],x_temp[15]) ^ major(y_temp[9],y_temp[13],y_temp[16]) ^ major(z_temp[13],z_temp[16],z_temp[18]))
		new_three = e_temp[11] ^ e_temp[16]
		e_temp_two = copy.deepcopy(e_temp)
		h=1
		while(h < len(e_temp)):
			e_temp[h] = e_temp_two[h-1]
			h = h + 1
		e_temp[0] = new_three
		i = i + 1
	return keystream


def bin_to_str(binary): #бинарный формат в текст
    return bytearray.fromhex(hex(int(binary,2))[2:]).decode('utf-8')
    
def encrypt(plain, key,t): #процесс шифрования
	s = ""
	binary = str_to_bin(plain)
	x,y,z = registers(key)
	if t!=1:
		e = user_input_r4()
		keystream = stream_2(len(binary), x, y, z, e)
	else:
		keystream = stream(len(binary), x, y, z)
	#keystream = stream(len(binary),t, x, y, z, e)
	for i in range(len(binary)):
		s += str(binary[i] ^ keystream[i])
	return s

def decrypt(cipher, key,t): #процесс расшифрования
	s = ""
	binary = []
	x,y,z = registers(key)
	if t!=1:
		e = user_input_r4()
		keystream = stream_2(len(cipher), x, y, z, e)
	else:
		keystream = stream(len(cipher), x, y, z)
	#keystream = stream(len(cipher),t, x, y, z, e)
	for i in range(len(cipher)):
		binary.append(int(cipher[i]))
		s += str(binary[i] ^ keystream[i])
	return bin_to_str(str(s))

allowed = '0123456789abcdef'
def user_input_key():
	tha_key = str(input('Введите ключ: ')).lower()
	if len(tha_key)==len([e for e in tha_key if e in allowed]) and len(bin(int(''.join([e for e in tha_key if e in allowed]),16))[2:])<=64:
		tha_key_bin = bin(int(tha_key,16))[2:]
		return '0'*(64-len(tha_key_bin))+''.join([i for i in ('0'*(17-len(tha_key_bin))+tha_key_bin)])
	else:
		while(len(tha_key)!=len([e for e in tha_key if e in allowed]) or len(bin(int(''.join([e for e in tha_key if e in allowed]),16))[2:])>64):
			error=f' Ключ должен состоять из {allowed} и длинною до 64 бит'
			print(error)
			if len(tha_key)==len([e for e in tha_key if e in allowed]) and len(bin(int(''.join([e for e in tha_key if e in allowed]),16))[2:])<=64:
				tha_key_bin = bin(int(tha_key,16))[2:]
				return '0'*(64-len(tha_key_bin))+''.join([i for i in ('0'*(17-len(tha_key_bin))+tha_key_bin)])
			tha_key = str(input('Введите корректный ключ: '))
	tha_key_bin = bin(int(tha_key,16))[2:]
	return '0'*(64-len(tha_key_bin))+''.join([i for i in ('0'*(17-len(tha_key_bin))+tha_key_bin)])

def user_input_r4():
	r4 = str(input('Введите r4: ')).lower()
	if len(r4)==len([e for e in r4 if e in allowed]) and len(bin(int(''.join([e for e in r4 if e in allowed]),16))[2:])<=17:
		r4_bin = bin(int(r4,16))[2:]
		return [int(i) for i in ('0'*(17-len(r4_bin))+r4_bin)]
	else:
		while (len(r4)!=len([e for e in r4 if e in allowed]) or len(bin(int(''.join([e for e in r4 if e in allowed]),16))[2:])>17):
			error=f' R4 должен состоять из {allowed}, длинною до 17 бит'
			print(error)
			if len(r4)==len([e for e in r4 if e in allowed]) and len(bin(int(''.join([e for e in r4 if e in allowed]),16))[2:])<=17:
				r4_bin = bin(int(r4,16))[2:]
				return [int(i) for i in ('0'*(17-len(r4_bin))+r4_bin)]
			r4 = str(input('Введите корректный r4: ')).lower()
	r4_bin = bin(int(r4,16))[2:]	
	return [int(i) for i in ('0'*(17-len(r4_bin))+r4_bin)]

def user_input_choice():
	someIn = str(input('[1]: A5/1\n[2]: A5/2\nНажмите 1 или 2: '))
	if (someIn == '1' or someIn == '2'):
		return int(someIn)
	else:
		while(someIn != '1' or someIn != '2'):
			if (someIn == '1' or someIn == '2'):
				return someIn
			someIn = str(input('[1]: A5/1\n[2]: A5/2\nНажмите 1 или 2: '))
	return someIn

def main(): #тест
	choice = user_input_choice()
	print(f'A5/{choice}')
	print('---------------')
	#key = '0101001000011010110001110001100100101001000000110111111010110111'
	#key = 521ac71929037eb7
	key = user_input_key()
	#phr = 'леопард не может изменить своих пятен тчк'..replace(' ', '')
	phr = 'л'.upper()
	print('Фраза: ',phr,str_to_bin(phr))
	#print('Ключ в HEX:',hex(int(key,2))[2:])
	print('Ключ: ',key)
	s = encrypt(phr, key,choice)
	#print('Шифр в HEX: ',hex(int(s,2))[2:])
	print('Шифр: ', s)
	#print('Расшифр: ',decrypt(s, key,choice))
	#print('---------------\n')
	#	
	#print('A5/2')
	#print('---------------')
	#print('Фраза: ',phr)
	#print('Ключ в HEX:',hex(int(key,2))[2:])
	#s = encrypt(phr, key,2)
	#print('Шифр: ', hex(int(s,2))[2:])
	#print('Расшифр: ',decrypt(s, key,2))
	#print('---------------')
	#for i in range(len(x)):
	#	x[i] = str(x[i])
	#for i in range(len(y)):
	#	y[i] = str(y[i])
	#for i in range(len(z)):
	#	z[i] = str(z[i])
main()
