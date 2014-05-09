import time
import ErrorPi
import modulo
import pylab as pl

x = [10**-1, 10**-2, 10**-3, 10**-4, 10**-5]


umbral = (0.1, 0.01, 0.001, 0.0001, 0.00001)
y = []
for u in umbral:
  start = time.clock()
  uy = ErrorPi.error(2, 10, u)
  y = y + [uy]
  finish = time.clock() - start  
print "Tiempo: %20.19f" %finish

nro_test = (10, 100, 1000, 5000, 10000)
for nt in nro_test:
  start1 = time.clock()
  t = ErrorPi.error(2, nt, 0.1)
  finish1 = time.clock() - start1
print "Tiempo: %20.19f" %finish1

nro_intervalos = (100, 1000, 10000, 100000, 1000000)
tiempo = []
for i in nro_intervalos:
  start2 = time.clock()
  s = ErrorPi.error(i, 2, 0.1)
  finish2 = time.clock() - start2
  tiempo = tiempo + [finish2]
print "Tiempo: %20.19f" %finish2

p1 = pl.subplot(211) #Dos filas una columna primer dibujo 
pl.plot (x, finish1, marker='o', linestyle=':', color='r', label='line 1')
pl.plot (x, nt, marker='*', linestyle='--', color='b', label='line 2')
pl.title('Error percentage')
pl.ylabel('Y axis')
pl.legend()
pl.xlim(0, 6)
pl.xticks(x)

p2 = pl.subplot(212)
pl.plot (x, y, marker='+', linestyle='-', color='c', label='line 4')
pl.xlabel('Intervals')
pl.ylabel('Seconds')
pl.legend()

pl.show()