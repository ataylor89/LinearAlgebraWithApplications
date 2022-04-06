from matplotlib import pyplot as plt
import numpy as np
import math

def plotL(u, v, dimx, dimy, title, filename):
    origin = np.array([[0, 0], [0, 0]])
    V = np.array([u, v])

    fig, ax = plt.subplots()
    ax.quiver(*origin, V[:,0], V[:,1], color=['blue'], angles='xy', scale_units='xy', scale=1)

    plt.xlim(-1*dimx, dimx)
    plt.ylim(-1*dimy, dimy)
    plt.grid()
    
    plt.title(title,fontsize=10)
    plt.savefig(filename, bbox_inches='tight')
    # plot.show()

def main():
    U = np.array([0, 2])
    V = np.array([1, 0])
    angle = math.pi/4
    angle2 = math.pi/2
    angle3 = -1 * math.pi / 2
    transforms = [
        np.array([[0.5, 0], [0, 0.5]]),
        np.array([[0, -1], [1, 0]]),
        np.array([[-1, 0], [0, 1]]),
        np.array([[1, 0], [0, -1]]),
        np.array([[math.cos(angle), -1 * math.sin(angle)], [math.sin(angle), math.cos(angle)]]),
        np.array([[math.cos(angle2), -1 * math.sin(angle2)], [math.sin(angle2), math.cos(angle2)]]),
        np.array([[math.cos(angle3), -1 * math.sin(angle3)], [math.sin(angle3), math.cos(angle3)]])
    ]
    for i in range(len(transforms)):
        transform = transforms[i]
        plotL(np.matmul(transform, U), np.matmul(transform, V), 2, 2, f"Transformation {i}", f"ch2sec2fig{i}.png")

if __name__ == '__main__':
    main()
