"""
Pixel class for game of life
"""


class Pixel(object):
    """A pixel class for game of life
    """

    def __init__(self, x_i, y_i, live):
        """Constructor of the Pixel class

        @param x_i x-coordinates of the instance
        @param y_i y-coordinates of the instance
        @param live Initial health of the instance
        """

        ## x-coordinates of the instance
        self.x_i = x_i
        ## y-coordinates of the instance
        self.y_i = y_i
        ## current health of the instance
        self.live = live
        ## health of the instance in next iteration
        self.next_live = live

    def is_live(self):
        """Get the health state of the instance

        @cond
        >>> pix = Pixel(0, 0, True)
        >>> pix.is_live()
        True
        >>> pix = Pixel(0, 0, False)
        >>> pix.is_live()
        False

        @endcond
        """
        return self.live

    def get_symbol(self):
        """Get the health state in symbol format, 'O' living, ' ' not living

        @cond
        >>> pix = Pixel(0, 0, True)
        >>> pix.get_symbol()
        'O'
        >>> pix = Pixel(0, 0, False)
        >>> pix.get_symbol()
        ' '

        @endcond
        """
        if self.live:
            return 'O'
        else:
            return ' '

    def step(self):
        """Step to next time instance of the pixel

        @cond
        >>> pix = Pixel(0, 0, True)
        >>> pix.step()
        >>> pix.live
        True
        >>> pix.next_live = False
        >>> pix.step()
        >>> pix.live
        False

        @endcond
        """
        self.live = self.next_live

    def set_next_live(self, next_live):
        """Set the health of the instance for next iteration

        @param next_live Health of the next iteration

        @cond
        >>> pix = Pixel(0, 0, True)
        >>> pix.set_next_live(False)
        >>> pix.next_live
        False

        @endcond
        """
        self.next_live = next_live
