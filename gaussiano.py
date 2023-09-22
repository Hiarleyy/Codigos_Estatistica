import statistics
from scipy import signal
import matplotlib.pyplot as plot
import numpy as np
from scipy.stats import norm

media = 0
dp = 0.5


x = np.linspace(-1,1,2000)
y = norm.pdf(x,media,dp)
plot.plot(x,y)
plot.xlabel("X")
plot.ylabel("Y")
plot.title("Gaussiano")


##mediana
md = statistics.median(y)
print("mediana=","{:.2f}".format(md))
##media harmonica
mh = len(x) / np.sum(1 / y)
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