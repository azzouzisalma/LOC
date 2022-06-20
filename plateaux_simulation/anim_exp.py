import numpy as np
import torch
import matplotlib.pyplot as plt
import matplotlib.animation as animation

L = torch.load('const_2_2.pt') 

fig , ax = plt.subplots(figsize= (5,5))
constellations, = plt.plot([],[],'*',markersize= 10)
ax.set_xlim([-2,2])
ax.set_ylim([-2,2])
#print(len(L_x))
def animate(k):
    x = L[k].detach().numpy() #Matrice de taille M*n
    x_l = x[:,0::2]
    x_c = x[:,1::2]
    constellations.set_data(x_l[:] ,x_c[:])   
    return constellations

ani = animation.FuncAnimation(fig = fig, func=animate, frames=range(len(L)) ,interval= 1000, repeat= False)
plt.grid()
plt.show()
