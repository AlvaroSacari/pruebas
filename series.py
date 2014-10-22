# encoding:utf-8
__author__ = 'alvaro'
###########################
# por Alvaro Sacari Alanoca
# alvaro.sacari@gmail.com
# #########################

import math

print "\n\tPrueba de Series"
print "\t----------------\n"

print "Los numeros pseudoaleatorios son leidos del archivo 'ri_series.txt' (pueble este archivo antes de ejecutar pruebas sobre ellos...)'\n"

################################################################
# Manipulando el archivo de texto plano 'ri_series.txt'
################################################################
archivo_txt = open('ri_series.txt')
n = int(0)

nums = []
for i in range(1, 100 + 1):
	linea = archivo_txt.readline()
	if linea != '':
		n += 1
		nums.append(float(linea))
print('r = {}'.format(nums))
print('\nen total son {} números pseudoaleatorios'.format(n))

m = int(raw_input('\nm = {} , elija un valor cercano, que sea un cuadrado.. \nm = '.format(math.sqrt(n))))

amplitud = 1.0 / math.sqrt(m)
print('\namplitud : {}'.format(amplitud))

#
# Entonces se generan 'm' cuadrantes, luego se contabilizan los puntos en cada cuadrante (frecuencias observadas)..
#

Oi = []

yi = 0.0
yf = 0.0 + amplitud

for k in range(1, int(math.sqrt(m))+1):
	xi = 0.0
	xf = 0.0 + amplitud
	for l in range(1, int(math.sqrt(m))+1):
		aux = 0
		for j in range(1, n):
			if (xi <= nums[j-1] < xf) and (yi <= nums[j] < yf):
				aux += 1
		Oi.append(aux)
		xi = xf
		xf += amplitud
	yi = yf
	yf += amplitud

print('\nlas frecuencias observadas son Oi : {}'.format(Oi))

#
# las frecuencias esperadas son :
#
Ei = (n-1) / float(m)
print('\nLas frecuencias esperadas son Ei : {}'.format(Ei))

#
# ahora calculamos el error (chi calculado) :
#
chi_calculado = 0.0
for i in range(0, m):
	aux = (Ei - Oi[i])**2 / Ei
	chi_calculado += aux
print('\nEl chi calculado es Xo2 : {}'.format(chi_calculado))
print('\nsi el valor de chi calculado es menor que el valor de tabla X2(a,m-1) FELICIDADES !!, no podemos rechazar la hipotesis de independencia ..')
