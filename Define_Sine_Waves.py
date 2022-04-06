import matplotlib.pyplot as plt
import numpy as np


max_speed = int(100)
end_pos = int(40)
sample_min = -80
sample_max = 80
x = np.arange(sample_min, sample_max)
y = max_speed * np.sin((2 * np.pi / end_pos) * (x))
plt.stem(x,y, 'r', )
plt.plot(x, y)
plt.xlabel('Positon(n)')
plt.ylabel('Pulse Width Modulation(PWM)')
plt.show()