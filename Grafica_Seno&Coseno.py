
import numpy as np #libreria de funciones matemáticas
import matplotlib.pyplot as plt #librería de graficar

#------------------GRAFICA DE SENO--------------------------------------------------------------#
def f(x):                                                                                       #
    return sum([(((-1)**n)/np.math.factorial(2*n + 1))*x**(2*n+1) for n in range(0, 10)])       #
                                                                                                #
x= np.linspace(-2*np.pi, 2*np.pi, 1000)                                                         #
                                                                                                #
plt.plot( x, np.sin(x), color = 'red', linestyle=':', linewidth=3)                              #
plt.plot( x, f(x), color = 'green', linestyle='-', linewidth=1.5)                               #
plt.ylim([-1, 1])                                                                               #
plt.show()                                                                                      #
                                                                                                #
#----------------------GRAFICA DE COSENO--------------------------------------------------------#            
def h(x):                                                                                       #
    return   sum([ ((-1)**n/np.math.factorial(2*n))*x**(2*n)  for n in range(0, 10)])           #
                                                                                                #
x= np.linspace(-2*np.pi, 2*np.pi, 1000)                                                         #
                                                                                                #
plt.plot( x ,np.cos(x) ,color = 'red', linestyle=':', linewidth=3)                              #
plt.plot( x ,h(x) ,color = 'green', linestyle='-', linewidth=1.5)                               #
plt.ylim([-1, 1])                                                                               #
plt.show()                                                                                      #
#-----------------------------------------------------------------------------------------------#