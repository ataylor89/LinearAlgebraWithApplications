from transformL import transformL
from transformL import plotL
import math
plotL(1, 2, 'The letter L', 'L.png')
transformL(1, 2, [[0.5, 0], [0, 0.5]], 2, 'Scale L by 0.5', 'Lscalebyhalf.png')
transformL(1, 2, [[0, -1], [1, 0]], 2, 'Rotate L ninety degrees counterclockwise', 'Lrot90.png')
transformL(1, 2, [[-1, 0], [0, 1]], 2, 'Reflect L about the Y axis', 'Lreflecty.png')
transformL(1, 2, [[1, 0], [0, -1]], 2, 'Reflect L about the X axis', 'Lreflectx.png')
transformL(1, 2, [[math.cos(math.pi/4), -1 * math.sin(math.pi/4)], [math.sin(math.pi/4), math.cos(math.pi/4)]], 2, 'Rotate L forty five degrees counterclockwise', 'Lrot45.png')
transformL(1, 2, [[1, 0], [0, 0]], 2, 'Orthogonal projection of L onto the X axis', 'Lorthogonalprojx.png')
transformL(1, 2, [[0, 0], [0, 1]], 2, 'Orthogonal projection of L onto the Y axis', 'Lorthogonalprojy.png')
transformL(1, 2, [[math.cos(math.pi/3), -1 * math.sin(math.pi/3)], [math.sin(math.pi/3), math.cos(math.pi/3)]], 2, 'Rotate L sixty degrees counterclockwise', 'Lrot60.png')
transformL(1, 2, [[3, -4], [4, 3]], 10, 'Multiply by the rotation matrix [[3, -4], [4, 3]]', 'Lrotscale345.png')
transformL(1, 2, [[3, 1], [1, 2]], 4, 'L under T(x) = [[3, 1], [1, 2]] x', 'L3112.png')
