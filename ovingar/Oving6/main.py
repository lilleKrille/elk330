from elk320.funksjoner import gauss_curve #Eiga funksjoner-fil
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 24, 100)
A = 800
mu = 12
sigma = 3
g = gauss_curve(t, A, mu, sigma)

plt.plot(t, g)
plt.xlabel('Tid (t)')
plt.ylabel('G(t)')
plt.title('Gauss-kurve for solstråling G(t)')
plt.show()
