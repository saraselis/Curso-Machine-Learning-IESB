"""
Meu primeiro Grafico
"""

import matplotlib.pylab as plt
from matplotlib import style
style.use('ggplot')

box = {
    'facecolor' : '.75',
    'boxstyle' : 'round',
}

#convenção usar maisculos
X=range(10)
Y=[val ** 2 for val in X]
Z=[val ** 3 for val in X]
W=[val ** 4 for val in X]

plt.plot(X,Y, 'g-.', label='Quadrado')
plt.plot(X,W, 'r:', label='4 potencia')
plt.plot(X,Z, 'bD', label='Cubos') #'bD' b=blue =ouros do baralho
plt.grid(True, lw=1,ls='--')
plt.legend() #precisa da legend p funcionar as labels
plt.title('Curvas de Potência')
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.text(50, max(W),'Meu melhor texto',bbox=box)
plt.grid(True, lw=1,ls='--')
plt.show()


