import pygame

class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()

    def get_radius(self):
        return self.radius

    def get_pos(self):
        return self.pos

    def draw(self,canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        c = 0.1

        self.angle += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        """
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        if self.pos[0] >= WIDTH:
            self.pos[0] = 0

        elif self.pos[0] <= 0:
            self.pos[0] = WIDTH

        elif self.pos[1] >= HEIGHT:
            self.pos[1] = 0

        elif self.pos[1] <= 0:
            self.pos[1] = HEIGHT
        """

        if self.thrust == True:
            acc = angle_to_vector(self.angle)
            self.vel[0] += acc[0] * c
            self.vel[1] += acc[1] * c

        self.vel[0] *= 0.99
        self.vel[1] *= 0.99

    def thrust(self, status):
        if status == True:
            self.thrust = status
            ship_thrust_sound.play()
            self.image_center[0] = 135
        else:
            self.thrust = status
            ship_thrust_sound.pause()
            ship_thrust_sound.rewind()
            self.image_center[0] = 45

    def rotate_right(self, angle_vel):
        self.angle_vel = angle_vel
        self.angle += angle_vel

    def rotate_left(self, angle_vel):
        self.angle_vel = angle_vel
        self.angle -= angle_vel


    def shoot(self, status):
        global missile_group

        # scaling coefficient
        c = 6

        if status == True:
            acc = angle_to_vector(self.angle)

            missile_pos_x = self.pos[0] + (self.radius * math.cos(self.angle))
            missile_pos_y = self.pos[1] + (self.radius * math.sin(self.angle))
            missile_pos = [missile_pos_x, missile_pos_y]


            missile_vel_x = self.vel[0] + (acc[0] * c)
            missile_vel_y = self.vel[1] + (acc[1] * c)
            missile_vel = [missile_vel_x, missile_vel_y]

            missile_group.add(Sprite(missile_pos, missile_vel, 0, 0, missile_image, missile_info, missile_sound))