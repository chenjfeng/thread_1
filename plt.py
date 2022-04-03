import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,10,0.1)
y=np.sin(x)
plt.plot(x,y,linestyle='--',label='sin')
plt.xlabel('x')
plt.ylabel('y')

plt.title('sin')
plt.legend()
plt.show()