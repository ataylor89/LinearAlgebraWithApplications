from matplotlib import pyplot as plt
import numpy as np
import math

def plotL(u, v, dimx, dimy):
    origin = np.array([[0, 0], [0, 0]])
    V = np.array([u, v])

    fig, ax = plt.subplots()
    ax.quiver(*origin, V[:,0], V[:,1], color=['blue'], angles='xy', scale_units='xy', scale=1)

    plt.xlim(-1*dimx, dimx)
    plt.ylim(-1*dimy, dimy)
    plt.grid()
    plt.show()

def main():
    U = np.array([0, 2])
    V = np.array([1, 0])
    # transform = [[0.5, 0], [0, 0.5]]
    # transform = [[0, -1], [1, 0]]
    # transform = [[-1, 0], [0, 1]]
    # transform = [[1, 0], [0, -1]]
    # angle = math.pi/4
    angle = -1 * math.pi / 2
    transform = np.array([[math.cos(angle), -1 * math.sin(angle)], [math.sin(angle), math.cos(angle)]])
    U = np.matmul(transform, U)
    V = np.matmul(transform, V)
    print(U)
    print(V)

    plotL(U, V, 2, 2)

if __name__ == '__main__':
    main()
