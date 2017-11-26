import numpy as np
import time
count = 0
count2 = 0

r = np.load('Route_path_2.npy')
# print r
prev_x,prev_y = r[0]
print prev_x,prev_y



for x,y in r:
    print x,y
    if (x == prev_x ):
        count = count + 1
    else:
        if (count != 0 ):
            print 'move ' + str(count) + ' steps and turn'
        if (y == prev_y ):
            count2 = count2 + 1
            print 'move ' + str(count2) + ' steps horizontally'
        elif  (y != prev_y ):
            print 'move ' + str(count2) + ' steps and turn'
        prev_x = x
        prev_y = y
        count = 0
        count2 = 0


# print 'move ' + str(count) + ' steps and turn'
