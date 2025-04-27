import matplotlib.pyplot as plt 
import numpy as np
from matplotlib.animation import FuncAnimation

i = 0
u = np.linspace(-np.pi, np.pi, 100)
x = np.linspace(-2.5, 2.5, 200)
k = -np.pi
y = np.zeros(200)

fig, ax = plt.subplots()
graph = ax.plot(x,y,color = 'r')[0]
ax.axis('equal')
ax.set(xlim=[-5, 5], ylim=[-4, 2])

def f(x, k):
    return np.abs(x) ** (2 / 3) + 0.9 * np.sqrt((3 - x ** 2)) * np.sin(10 * (k * x - 2 * np.sin(k))) - 1.5

def update(frame):
    global k, u, i
    
    k = u[i % 100]
    i = i + 1
    y = f(x - np.sin(k), k) 
    graph.set_ydata(y)
    
anim = FuncAnimation(fig = fig, func = update, frames = 100, interval = 30)  

plt.show()