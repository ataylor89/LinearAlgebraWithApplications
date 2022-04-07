from transformL import transformL
from transformL import plotL
import math
plotL(1, 2, 'The letter L', 'L.png')
transformL(1, 2, [[0.5, 0], [0, 0.5]], 'Scale L by 0.5', 'Lscalebyhalf.png')
transformL(1, 2, [[0, -1], [1, 0]], 'Rotate L ninety degrees counterclockwise', 'Lrot90.png')
transformL(1, 2, [[-1, 0], [0, 1]], 'Reflect L about the Y axis', 'Lreflecty.png')
transformL(1, 2, [[1, 0], [0, -1]], 'Reflect L about the X axis', 'Lreflectx.png')
transformL(1, 2, [[math.cos(math.pi/4), -1 * math.sin(math.pi/4)], [math.sin(math.pi/4), math.cos(math.pi/4)]], 'Rotate L forty five degrees counterclockwise', 'Lrot45.png')
