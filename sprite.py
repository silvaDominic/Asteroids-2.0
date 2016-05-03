import pygame

class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()


    def get_radius(self):
        return self.radius


    def get_pos(self):
        return self.pos


    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

        if self.animated:
            step = 0
            for frame in range(self.age):
                canvas.draw_image(self.image, [self.image_center[0] + step, self.image_center[1]], self.image_size, self.pos, self.image_size, self.angle)
                step += 128


    def update(self):
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        self.angle += self.angle_vel

        self.age += 1
        if self.age >= self.lifespan:
            return True
        else:
            return False


    def check_collision(self, other_object):
        d = dist(self.get_pos(), other_object.get_pos())
        r_sum = self.get_radius() + other_object.get_radius()
        if d <= r_sum:
            return True
        else:
            return False