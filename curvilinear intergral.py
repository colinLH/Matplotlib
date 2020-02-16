from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from matplotlib.ticker import FuncFormatter
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as col
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib as mpl
import pandas as pd
import numpy as np
data = [0.23,0.69,1.43,3.62,5.76,7.21,7.03,5.82,7.56,5.99,1.78]
year = [1975,1980,1987,1994,2000,2005,2010,2015,2020,2025,2030]
years = ['1975','1980','1987','1994','2000','2005','2010','2015','2020','2025','2030']
fig,ax = plt.subplots(figsize=(10,10))
plt.plot(year,data,color = 'r',marker ='o')
plt.title('The annual growth of plastic waste')
a = 2000
b = 2020
ix = np.linspace(a,b,5)
iy = data[4:10]
ixy=zip(ix,iy)
verts=[(a,0)]+list(ixy)+[(b,0)]
poly = Polygon(verts,facecolor='0.9',edgecolor='0.5')
ax.add_patch(poly)
plt.ylim(0)
plt.text(2005,4,'$\int_a^b (Waste Total)dx$')
plt.hlines(5.76,1975,2000,linestyle='dashed',color='navy')
plt.hlines(7.56,1975,2020,linestyle='dashed',color='navy')
y_pos =[5.76,7.56]
labels =['5.76','7.56']
plt.yticks(y_pos,labels)
