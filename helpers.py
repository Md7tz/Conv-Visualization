import matplotlib.pyplot as plt
import numpy as np
import torch

def visualize_filters(filters):

    fig, subs = plt.subplots(nrows=1, ncols=len(filters), figsize=(10, 5))
    
    for i, ax in enumerate(subs.flatten()):
        ax.imshow(filters[i], cmap='gray')
        ax.set_title('Filters %s' % str(i+1))
        ax.axis("off")
        
        width, height = filters[i].shape
        
        for x in range(width):
            for y in range(height):
                ax.annotate(str(filters[i][x][y]), xy=(y, x), 
                horizontalalignment='center',
                verticalalignment='center',
                color='white' if filters[i][x][y] < 0 else 'black')
