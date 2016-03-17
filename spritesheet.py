# Code used from the Pygame wiki pages

import pygame

class spritesheet(object):
    """
    Used for processing a spritesheet or sprite strip
    """
    def __init__(self, filename):

        """
        Constructor for spritesheet object

        Args:
            filename(String): the file being used for the spritesheet

        Raises:
            SystemExit: if file is not found
        """
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error, message:
            print "Unable to load spritesheet image:", filename
            raise SystemExit, message


        def image_at(self, rectangle, colorkey = None):
            """
            Loads a specifc image from a specific rectangle

            Args:
                rectangle(tuple): the rectangle object represented as a tuple of coordinates
                colorkey(tuple): color value ('None' by default)

            Returns:
                image(Surface object): the image object
            """
            # Loads image from x, y, x+offset, y+offset
            rect = pygame.Rect(rectangle)
            image = pygame.Surface(rect.size).convert()
            image.blit(self.sheet, (0, 0), rect)

            if colorkey is not None:
                if colorkey is -1: # If colorkey is a null value
                    colorkey = image.get_at((0, 0)) # Set it to (0, 0)
                image.set_colorkey(colorkey, pygame.RLEACCEL)
            return image


        def images_at(self, rects, colorkey = None):
            """
            Loads multiple images and returns the corresponding coordinated as a list

            Args:
                rects(list): a list of rect coordinates (tuples)
                colorkey(tuple): color value ('None' by default)

            Returns:
                rects(list): a list of rect objects
            """
            return [self.image_at(rect, colorkey) for rect in rects]


        def load_strip(self, rect, image_count, colorkey = None):
            """
            Loads a sprite strip and returns the corresponding coordinates
            """
            # Loads a strip of images and returns them as a list
            tups = [(rect[0] + rect[2] * x, rect[1], rect[2], rect[3])
                    for x in range(image_count)]
            return self.images_at(tups, colorkey)