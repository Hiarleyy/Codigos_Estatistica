import statistics
import matplotlib.pyplot as plot
import numpy as np
import scipy.signal as signal

x = np.linspace(-2,2,1000, endpoint= True)
y = 2 * np.sin(2 * np.pi * x) - 4 * np.cos(2 * np.pi * 8 * x) + 2 * np.random.randn(len(x))

plot.plot(x,y)
plot.title('Composto com Ruído')
plot.xlabel('tempo')
plot.ylabel('amplitude')

##mediana
md=statistics.median(y)
print("mediana=","{:.2f}".format(md))
##media harmonica
mh = len(y) / np.sum(1 / y)
print("media Harmonica=","{:.2f}".format(mh))
##media geometrica
mg = np.exp(np.mean(np.log(np.abs(y))))
print("media geometrica=","{:.2f}".format(mg))
## media aritmética
ma = np.mean(y)
print("media aritmetica=","{:.2f}".format(ma))
## variancia
va = statistics.variance(y)
print("variancia=","{:.2f}".format(va))
## Desvio médio
media = np.mean(y)
dm = np.mean(np.abs(np.array(y)- media))
print("Desvio medio=","{:.2f}".format(dm))
##Amplitude
at = max(y)-min(y)
print("Amplitude =","{:.2f}".format(at))
## Desvio padrão
dp = np.std(y);
print("Desvio Padrao =","{:.2f}".format(dp))
plot.show()