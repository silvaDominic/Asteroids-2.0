import spritesheet

class SpriteStripAnim(object):
    """
    Joins sprite strips using an iterator (useful for strips that wrap to next row)
    """
    def __int__(self, filename, rect, count, colorkey=None, loop=False, frames=1):
        """
        Constructor for the sprite strip animation obejct

        Args:
            filename(String): the file being processed
            rect(tuple): the rectangle object represented as a tuple of coordinates
            count(int): the number of images in the strip
            colorkey(tuple): color value ('None' by default)
            loop(boolean): indicates whether strip is iterative
            frames(int):
        """
        self.filename = filename
        ss = spritesheet.spritesheet(filename)
        self.images = ss.load_strip(rect, count, colorkey)
        self.i = 0
        self.loop = loop
        self.frames = frames
        self.f = frames

        def iter(self):
            """
            Resets values of frames and iterator; returns self
            """
            self.i = 0
            self.f = self.frames
            return self

        def next(self):
            """
            Returns an image object for each frame in the sprite strip

            Raises:
                StopIteration
            """
            if self.i >= len(self.images):
                if not self.loop:
                    raise StopIteration
                else:
                    self.i = 0

                image = self.images[self.i]
                self.f -= 1

                if self.f == 0:
                    self.i += 1
                    self.f = self.frames
                return image

        def __add__(self, ss):
            self.images.extend(ss.images)
            return self