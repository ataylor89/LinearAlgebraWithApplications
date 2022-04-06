from transformL import transformL
transformL(1, 2, [[0.5, 0], [0, 0.5]], 'Scale by 0.5', 'Lscalebyhalf.png')
transformL(1, 2, [[0, -1], [1, 0]], 'Rotate ninety degrees counterclockwise', 'Lrot90.png')
transformL(1, 2, [[-1, 0], [0, 1]], 'Reflect about the Y axis', 'Lreflecty.png')
transformL(1, 2, [[1, 0], [0, -1]], 'Reflect about the X axis', 'Lreflectx.png')
