import matplotlib.pyplot as plt
import numpy as np


Fs = 100
f = 40
sample_min = -80
sample_max = 80
x = np.arange(sample_min, sample_max)
y = Fs * np.sin((2 * np.pi / f) * (x))
plt.stem(x,y, 'r', )
plt.plot(x, y)
plt.xlabel('Positon(n)')
plt.ylabel('Pulse Width Modulation(PWM)')
plt.show()