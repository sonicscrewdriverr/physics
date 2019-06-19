from vpython import *
#display(width = 1300, height = 1000)
projectile = sphere(pos=vector(-5,0,0),
                   radius = 0.1,
                  color = color.red,
                    make_trail= True)

projectile.speed = 3.2
projectile.angle = 75 * 3.141459 / 180 #initial angle from x axis

projectile.velocity = vector(projectile.speed * cos(projectile.angle),
                             projectile.speed * sin(projectile.angle),
                             0)

projectile.mass = 1.0
grav_acc = 1.0

dt = 0.01
time = 0
while (projectile.pos.y >=0):
    rate(100)
    #calculate the force f=m*a
    grav_force = vector(0,-projectile.mass*grav_acc,0)

    force = grav_force

    #update velocity v=u+at
                    #v=u+(f/m)t
    projectile.velocity = projectile.velocity + (force/projectile.mass) * dt

    #update position
    #s=s + ds
    projectile.pos = projectile.pos + projectile.velocity * dt

    #update time
    time = time + dt
