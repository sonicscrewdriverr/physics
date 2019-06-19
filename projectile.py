#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation

fig = plt.figure(figsize=(20, 20))
ax = plt.gca()

def grav(x, y):
    return 0, -9.8

ax.set_xlim( (-10, 10) )
ax.set_ylim( (-10, 10) )

ground = -10
right_wall=10
left_wall = -10

balls = { Circle( (-9, 0), .2 ) : [4, 4], Circle((-9,0), .2): [8,8] }

for ball in balls.keys():
    ax.add_patch(ball)

dt = 0.01

def update(frame, balls):
    for ball, velocity in balls.items():

        x, y = ball.center

        Gx, Gy = grav(x, y)

        velocity[0] += Gx*dt
        velocity[1] += Gy*dt

        if y <= ground:
        	velocity[1] *= -1

        if x >=right_wall:
            velocity[0] *= -1

        if x<= left_wall:
            velocity[0] *= -1




        ball.center = (x + velocity[0] * dt, y + velocity[1] * dt)


    return balls.keys()

ani = FuncAnimation( fig, update, fargs=(balls,), frames = 60 * 20, interval = 1000/60 )

ani.save("projectile.mp4")
