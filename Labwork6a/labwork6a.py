import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 400)
y = 2 * x + np.sin(x)**2 + 3

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = 2x + sin^2(x) + 3', color='purple')
plt.grid(True)
plt.title("hello, po!")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

plt.savefig('po.pdf')
plt.close()
print("Saved labwork6a plot to po.pdf")