from matplotlib import pyplot as plt
import numpy as np
import math
import sys
import ast

def transformL(width, height, transform, title, filename):
    dim = max(width, height)
    origin = np.array([[0, 0], [0, 0]])

    V1 = np.array([width, 0])
    V2 = np.array([0, height])
    transform = np.array(transform)
    V1 = np.matmul(transform, V1)
    V2 = np.matmul(transform, V2)

    V = np.array([V1, V2])

    fig, ax = plt.subplots()
    ax.quiver(*origin, V[:,0], V[:,1], color=['blue'], angles='xy', scale_units='xy', scale=1)

    plt.xlim(-1*dim, dim)
    plt.ylim(-1*dim, dim)
    plt.grid()
    
    plt.title(title,fontsize=10)
    plt.savefig(filename, bbox_inches='tight')
    plt.show()

def main():
    if len(sys.argv) < 6:
        print("Usage: %s <width> <height> <transform> <title> <filename>" %sys.argv[0])
        return

    width = int(sys.argv[1])
    height = int(sys.argv[2])
    transform = ast.literal_eval(sys.argv[3])
    title = sys.argv[4]
    filename = sys.argv[5]
    transformL(width, height, transform, title, filename)

if __name__ == '__main__':
    main()

# Example usage 
# python transformL.py 1 2 "[[0, -1], [1, 0]]" rot90 rot90.png
