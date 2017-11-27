import numpy as np
import time
import rospy
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





# -------------------------------Ros Control
rospy.init_node('control', anonymous=False)

pub_wheel_l = rospy.Publisher('/path_planner/left_wheel_controller/command', Float64 , queue_size=1,latch=True )
pub_wheel_r = rospy.Publisher('/path_planner/right_wheel_controller/command', Float64 , queue_size=1,latch=True)

pub_wheel_l.publish(Float64(10))
pub_wheel_r.publish(Float64(10))
