# encoding:utf-8
__author__ = 'alvaro'

print "\n\tPrueba de Huecos"
print "\t----------------\n"

print "Los numeros pseudoaleatorios son leidos del archivo 'ri_huecos.txt' (pueble este archivo antes de ejecutar pruebas sobre ellos...)'\n"

#######################################################
# Manipulando el archivo de texto plano 'ri_huecos.txt'
#######################################################
archivo_txt = open('ri_huecos.txt')
n = int(0)

nums = []
for i in range(1, 100 + 1):
	linea = archivo_txt.readline()
	if linea != '':
		n += 1
		nums.append(float(linea))
print('r = {}'.format(nums))
print('\nen total son {} números pseudoaleatorios'.format(n))

print('\ningrese los valores de las cotas "alfa" y "beta" :')
#alfa = float(raw_input('\talfa : '))
#beta = float(raw_input('\tbeta : '))
alfa = 0.8
beta = 1.0
print('\talfa : {}'.format(alfa))
print('\tbeta : {}'.format(beta))

#
# tomando los numeros de ri, generamos la secuencia de unos y ceros, teniendo en cuenta alfa y beta (cota)
#
S = []
for i in range(0, n):
	if alfa <= nums[i] <= beta:
		S.append(1)
	else:
		S.append(0)
print('\nS : {}'.format(S))

#
# a continuación se cuenta el tamaño de cada hueco entre los unos :
#
tam_hueco_i = []
signal = 0
for i in range(0, n):
	if S[i] == 1:
		if signal == 0:
			aux = i
			signal = 1
		else:
			if S[i] == 1:
				tam_hueco_i.append(i-aux-1)
				aux = i

print('\n Tamaño de los huecos : {}'.format(tam_hueco_i))

#
# h es el numero total de huecos en la muestra
#
h = len(tam_hueco_i)
print '\th : {}'.format(h)

#
# Calculamos las frecuencias observadas y esperadas para cada tamaño de hueco (0, 1, 2 ,3, 4, >=5) :
#
Oi = []
Ei = []
chi_calculado = 0
contador = 0
for i in range(0, max(tam_hueco_i)+1):
	if i < 5:
		Oi.append(tam_hueco_i.count(i))
		Ei.append(h*(beta-alfa)*(1-(beta-alfa))**i)
		aux = (Ei[i] - Oi[i])**2 / Ei[i]
		chi_calculado += aux
	else:
		contador += tam_hueco_i.count(i)

Oi.append(contador)
Ei.append(h*(beta-alfa)*(1-(beta-alfa))**5)
aux = (Ei[5] - Oi[5])**2 / Ei[5]
chi_calculado += aux

print('\nOi : {}'.format(Oi))
print('\nEi : {}'.format(Ei))

print('\nChi calculado : {}'.format(chi_calculado))
