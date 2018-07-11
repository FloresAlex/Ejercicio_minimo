def derivada(x):
 """ Funcion para calcular la derivada en el punto x """
 res = (4/3)*(evaluar(x+0.5) - evaluar(x-0.5)) - (1/4)*(evaluar(x+0.25) - evaluar(x-0.25))/.5 
 return res

def evaluar(x):
 """ Calcula el valor de la funcion en el punto x """
 resultado = eval(funcion)
 return resultado

# Valores iniciales inferior y superior

funcion = input("Funcion: ")
val_i = float(input("Valor inicial inferior de x: "))
val_s = float(input("Valor inicial superior de x: "))


d_i = derivada(val_i)
d_s = derivada(val_s)
n = 0

# Bucle que calculara nuevas derivadas en puntos cada vez mas cercanos
while (d_i != 0 and d_s != 0):
 n = n+1
 if (d_i*d_s < 0):
  d = derivada((val_i + val_s)/2)
  if (d*d_i > 0):
   val_i = (val_i + val_s)/2
   d_i = derivada(val_i)
  else:
   val_s = (val_i + val_s)/2
   d_s = derivada(val_s)
 else:
  val_i = val_i - 1000
  val_s = val_s + 1000
  d_i = derivada(val_i)
  d_s = derivada(val_s)

if(d_i == 0):
 print "El minimo se encuentra en f("+str(val_i)+") =",evaluar(val_i)
 print "Las iteraciones fueron:", n
else:
 print "El minimo se encuentra en f("+str(val_s)+") =",evaluar(val_s)
 print "Las iteraciones fueron:", n


