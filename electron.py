from vpython import *

electron = sphere(pos=vector(0,0,0),
                   radius = 0.1,
                  color = color.red,
                    make_trail= True)

electron.charge = 2
electric_field = vector(1,0,0)
electron.velocity = vector(0,0,0)
#electron.mass = 9.11 * (10**-31)
electron.mass=2

dt = 0.01
time = 0

while (electron.pos.x>=0):
    rate(100)
    #calculate the force f=m*a
    electric_force = electron.charge * electric_field
    #electric_force = vector(20, 0 , 0)

    force = electric_force

    #update velocity v=u+at
                    #v=u+(f/m)t
    electron.velocity = electron.velocity + (force/electron.mass) * dt

    #update position
    #s=s + ds
    electron.pos = electron.pos + electron.velocity * dt

    #update time
    time = time + dt

    print (electron.pos)
