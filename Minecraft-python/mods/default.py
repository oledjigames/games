#mod config of all variable
import math
from pyglet.gl import *
TICKS_PER_SEC = 160 #fps

# Size of sectors used to ease block loading.16
SECTOR_SIZE = 50

WALKING_SPEED = 5 #speed of walking
FLYING_SPEED = 15 #fly speed
GRAVITY = 20.0 #gravity simple 20
MAX_JUMP_HEIGHT = 1.0 # About the height of a block.simple 2
# To derive the formula for calculating jump speed, first solve
#    v_t = v_0 + a * t
# for the time at which you achieve maximum height, where a is the acceleration
# due to gravity and v_t = 0. This gives:
#    t = - v_0 / a
# Use t and the desired MAX_JUMP_HEIGHT to solve for v_0 (jump speed) in
#    s = s_0 + v_0 * t + (a * t^2) / 2
JUMP_SPEED = math.sqrt(2 * GRAVITY * MAX_JUMP_HEIGHT)
TERMINAL_VELOCITY = 90

PLAYER_HEIGHT = 2 #height 2 blocks
glFogf(GL_FOG_START, 40.0) #fog start
glFogf(GL_FOG_END, 60.0) # Fog end