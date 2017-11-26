import numpy as np
import time
count = 0

r = np.load('Route_path_2.npy')
# print r
prev_x,prev_y = r[0]
print prev_x,prev_y



for x,y in r:
    print x,y
    if (x == prev_x ):
        count = count + 1
    else:
        print 'move ' + str(count) + ' steps and turn'
        prev_x = x
        count = 0

# print 'move ' + str(count) + ' steps and turn'
