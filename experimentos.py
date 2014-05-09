from ErrorPi import error
import modulo
import pylab as pl
x = [10**-1, 10**-2, 10**-3, 10**-4, 10**-5]

umbral = (0.1, 0.01, 0.001, 0.0001, 0.00001)
y = []
for u in umbral:
  uy = error(2, 10, u)
  y = y + [uy]
  print y

p1 = pl.subplot(211) #Dos filas una columna primer dibujo 
pl.plot (x, y, marker='o', linestyle=':', color='r', label='line 1')
pl.title('Error')
pl.ylabel('Porcentaje de error')
pl.xlabel('Umbral')
pl.legend()
pl.xlim(0.00001, 0.1)
pl.xticks(x)

pl.show()