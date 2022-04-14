from plotL import transformL
from plotL import plotL
import math

transformL(1, 2, [[0, 1], [1, 0]], 2, r'$T_{A}(x) = [[0, 1], [1, 0]]\, x$ applied to L', 'Lreflectyeqx.png')
transformL(1, 2, [[-1, 0], [0, 1]], 2, r'$T_{B}(x) = [[-1, 0], [0, 1]]\, x$ applied to L', 'Lreflectxeq0.png')
transformL(1, 2, [[0, -1], [1, 0]], 2, r'$T_{BA}(x) = [[0, -1], [1, 0]]\, x$ applied to L', 'Lrot90ccw.png')
transformL(1, 2, [[0, 1], [-1, 0]], 2, r'$T_{AB}(x) = [[-1, 0], [0, 1]]\, x$ applied to L', 'Lrot90cw.png')
