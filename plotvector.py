from matplotlib import pyplot as plt
import numpy as np

def plotvector(x, y, a, b, c, d, title, filename):
    ax = plt.axes()
    ax.arrow(0, 0, x, y, head_width=0.2, head_length=0.2, linewidth=2, color='lightblue')
    plt.grid()
    plt.xlim(a, b)
    plt.ylim(c, d)
    plt.title(title, fontsize=10)
    plt.savefig(filename, bbox_inches='tight')
    plt.show()
    plt.close()

def main():
    plotvector(4, 3, 0, 5, 0, 5, 'The vector [4, 3]', 'vector43.png')

if __name__ == '__main__':
    main()
