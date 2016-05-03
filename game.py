import sys, pygame

class Game:

def process_sprite_group(group, canvas):
        for element in set(group):
            if element.update() == False:
                element.draw(canvas)
            else:
                group.discard(element)


def check_group_collisions(group_1, group_2):
    global explosion_group
    collision = False
    for g1_element in set(group_1):
        for g2_element in set(group_2):
            if g2_element.check_collision(g1_element):
                group_2.discard(g2_element)
                group_1.discard(g1_element)
                explosion_group.add(Sprite(g2_element.get_pos(), [0, 0], 0, 0,
                                       explosion_image_org, explosion_info, explosion_sound))
                collision = True
    return collision

def check_indiv_collisions(group, other_object):
    global explosion_group

    collision = False
    for element in set(group):
        if element.check_collision(other_object):
            group.discard(element)
            explosion_group.add(Sprite(other_object.get_pos(), [0, 0], 0, 0,
                                       explosion_image_alpha, explosion_info, explosion_sound))
            explosion_group.add(Sprite(element.get_pos(), [0, 0], 0, 0,
                                       explosion_image_org, explosion_info, explosion_sound))
            other_object.pos = [WIDTH / 2, HEIGHT / 2]
            collision = True

    return collision


def reset():
    global my_ship, score, lives, game_start, rock_group
    print score
    for rock in set(rock_group):
        rock_group.discard(rock)
    my_ship.pos = [WIDTH / 2, HEIGHT / 2]
    score = 0
    lives = 3
    game_start = False

def draw(canvas):
    global time, score, lives, game_start

    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw ship and sprites
    my_ship.draw(canvas)
    process_sprite_group(rock_group, canvas)
    process_sprite_group(missile_group, canvas)
    process_sprite_group(explosion_group, canvas)

    #check collisions between objects
    if check_indiv_collisions(rock_group, my_ship) == True:
        lives -= 1

    if check_group_collisions(rock_group, missile_group) == True:
        score += 100

    #draw text
    canvas.draw_text("Score: " + str(score), [550, 50], 32, "White")
    canvas.draw_text("Lives: " + str(lives), [50, 50], 32, "White")

    # update ship and sprites
    my_ship.update()

    #set splash screen
    if game_start == False:
        canvas.draw_image(splash_image, splash_info.get_center(),
                          splash_info.get_size(),
                          [WIDTH / 2, HEIGHT / 2],
                          splash_info.get_size())

    if lives <= 0:
        reset()


# timer handler that spawns a rock
def rock_spawner():
    #initialize globals
    global rock_group, my_ship

    if game_start:
        #useful values for determining velocity, angular velocity, and position
        vel_values = [-3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5]
        upper = 0.1
        lower = -0.1

        vel = [(random.choice(vel_values)),(random.choice(vel_values))]
        angle_vel = random.random() * (upper - lower) + lower
        start_pos = [(random.randint(0, WIDTH)), (random.randint(0, HEIGHT))]

        a_rock = Sprite(start_pos, vel, 0, angle_vel, asteroid_image, asteroid_info)
        d = dist(start_pos, my_ship.get_pos())
        r_sum = (my_ship.get_radius() + a_rock.get_radius())
        if len(rock_group) < 12 and d > r_sum:
            rock_group.add(a_rock)


inputs = {"up":(Ship.thrust,True, False), "left":(Ship.rotate_left, -0.05, 0), "right":(Ship.rotate_right, 0.05, 0), "space":(Ship.shoot, True, False)}

def key_down(key):
        for i,j in inputs.items():
            if key == simplegui.KEY_MAP[i]:
                j[0](my_ship, j[1])

def key_up(key):
        for i,j in inputs.items():
            if key == simplegui.KEY_MAP[i]:
                j[0](my_ship, j[2])

def click(pos):
    global game_start, my_ship
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    splash_width = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    splash_height = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)

    if not game_start and splash_width and splash_height:
        my_ship.pos = [WIDTH / 2, HEIGHT / 2]
        my_ship.vel = [0, 0]
        game_start = True