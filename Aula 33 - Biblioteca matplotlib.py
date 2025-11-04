import matplotlib.pyplot as plt
import numpy as np

plt.plot([1, 2, 3], [1, 2, 3])
plt.ylabel('Eixo Y - Números')
plt.xlabel('Eixo X - Nùmeros')

plt.show()

from pylab import plot, show
eixoX = [1,2,3,4,5,]
eixoY = [1,2,3,4,5,]

plot(eixoX, eixoY)
plot(eixoX, eixoY, marker= 'o')

show()

from matplotlib.pyplot import ylabel
from pylab import plot,show, legend, title, xlabel, ylabel,axis

meses = ['Jan', 'Fev','Mar','Abr','Mai','Jun','jul',
         'Ago','Set','Out','Nov','Dez']
Tmax = [38,32,29,25,36,24,29,20,27,25,31,38]
Tmin = [23,23,22,21,19,16,12,10,16,21,22,23]

plot(meses, Tmax, meses, Tmin)
title('Temperatura Máxima e minima do ano')
xlabel('Mês')
ylabel('Temperatura')
legend(['Tmax','Tmin'])
axis(ymin=0, ymax=41)
show()

