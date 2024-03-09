import random

# button states
forwardButton = True
backwardButton = True

# motor status
# 0 equals no rotation
# 1 equals motor rotation FW
# 2 equals motor rotation BW

# generating motor status
motorStatus = random.randint(0, 2)
print('Motor status', motorStatus)

# verifying the status
if motorStatus == 1 and forwardButton:
    print('The car is moving forward')

elif motorStatus == 2 and backwardButton:
    print('The car is moving backwards')

else:
    print('The car is not moving')
