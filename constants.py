class GameConstants:

    #resolution
    WIDTH = 800
    HEIGHT = 600

    #display support
    SCORE_PREFIX = "Score: "
    SCORE_LOCATION = (600, 40)
    LIVES_PREFIX = "Lives: "
    LIVES_LOCATION = (50, 40)
    FRAME_RATE = 10

    #movement support
    SCALE_COEF_SHIP = 0.1
    SCALE_COEF_MISS = 6

class GameObjConstants:
    #image_support

    #nebula
    NEBULA_CENTER = [400, 400]
    NEBULA_SIZE = [800, 600]

    #debris
    DEBRIS_CENTER = [320, 240]
    DEBRIS_SIZE = [640, 480]

    #splash image
    SPLASH_CENTER = [200, 150]
    SPLASH_SIZE = [400, 300]

    #ship
    SHIP_CENTER = [45, 45]
    SHIP_SIZE = [90, 90]
    SHIP_RADIUS = 35

    #missile
    MISSILE_CENTER = [5, 5]
    MISSILE_SIZE = [10, 10]
    MISSILE_RADIUS = 3
    MISSILE_LIFESPAN = 60

    #asteroid
    ASTEROID_CENTER = [45, 45]
    ASTEROID_SIZE = [90, 90]
    ASTEROID_RADIUS = 40

    #explosion
    EXPLOSION_CENTER = [64, 64]
    EXPLOSION_SIZE = [128, 128]
    EXPLOSION_RADIUS = 17
    EXPLOSION_LIFESPAN = 24
    EXPLOSION_ANIMATE = True

    #sprite support
    SPRITE_DRAW_OFFSET = 128
    ROCK_VEL = [-3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5]