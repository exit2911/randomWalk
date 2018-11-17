import matplotlib.pyplot as plt

from randomwalk import RandomWalk

while True:
    
    rw = RandomWalk(200)
    
    rw.fill_walk()
    
    #set the size of the plotting window
    
    plt.figure(dpi=128,figsize = (10,6)) # dpi = resolution of the figure
    
    point_numbers = list(range(rw.num_points)) 
    plt.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolor = 'none', s = 1)
    
    #graph first and last points bigger
    
    plt.scatter(0,0, c= 'green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors = 'none',s=100)
    
    #remove the axes
    
    
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()
    
    
    
    keep_running = input("continue running? y/n ")
    if keep_running == 'n':
        break
