"""
Universe class for game of life

"""
import pixel
import random
from random import randint

## Default width of the universe
DIMX = 40
## Height of the universe
DIMY = 20
## Default health rate of initial generation of universe (default = 20)
RATE = 20
## Default value of flag that indicates if the universe is wrapped around
WRAP = True


class Universe(object):
    """A universe class for game of life
    """

    def __init__(self, rate=RATE, seed=0, dim_x=DIMX, dim_y=DIMY, wrap=WRAP):
        """Constructor of the Universe class

        @param seed The random seed to generate the universe (default = 0)
        @param rate Health rate of generation of universe (default = #RATE)
        @param dim_x Width of the universe (default = #DIMX)
        @param dim_y Height of the universe (default = #DIMY)
        @param wrap State if the universe is wrapped around (default = #WRAP)
        """
        random.seed(seed)

        ## Width of the universe
        self.dim_x = dim_x
        ## Height of the universe
        self.dim_y = dim_y
        ## Flag that indicates if the universe is wrapped around at edges
        self.wrap = wrap
        ## 2D array of Pixel elements in the universe
        self.pixels = [[0 for y_i in range(self.dim_y)]
                       for x_i in range(self.dim_x)]

        for y_i in range(self.dim_y):
            for x_i in range(self.dim_x):
                if randint(0, 99) < rate:
                    self.pixels[x_i][y_i] = pixel.Pixel(x_i, y_i, True)
                else:
                    self.pixels[x_i][y_i] = pixel.Pixel(x_i, y_i, False)

    def set_universe(self, pixels):
        """Set the pixels in the universe

        @param pixels A 2D array stating how the universe should be set
        @cond
        >>> pixels = [['O',' ','O',' '], \
                       [' ','O',' ','O'], \
                       ['O',' ','O',' '], \
                       [' ','O',' ','O']]
        >>> uni = Universe(0, 20, 4, 4, True)
        >>> uni.set_universe(pixels)
        >>> print uni.display() #doctest: +REPORT_NDIFF +NORMALIZE_WHITESPACE
        ------\
        |O O |\
        | O O|\
        |O O |\
        | O O|\
        ------

        @endcond
        """
        for y_i in range(self.dim_y):
            for x_i in range(self.dim_x):
                if pixels[y_i][x_i] == 'O':
                    self.pixels[x_i][y_i].set_next_live(True)
                    self.pixels[x_i][y_i].step()
                else:
                    self.pixels[x_i][y_i].set_next_live(False)
                    self.pixels[x_i][y_i].step()

    def step(self):
        """Step to next time instance of the universe
        @cond
        >>> pixels = [['O',' ','O',' '], \
                       [' ','O',' ','O'], \
                       ['O',' ','O',' '], \
                       [' ','O',' ','O']]
        >>> uni = Universe(0, 20, 4, 4, True)
        >>> uni.set_universe(pixels)
        >>> uni.step()
        >>> print uni.display() #doctest: +REPORT_NDIFF +NORMALIZE_WHITESPACE
        ------\
        |    |\
        |    |\
        |    |\
        |    |\
        ------

        @endcond
        """
        ## Check the input to determine the state of a pixel
        for y_i in range(self.dim_y):
            for x_i in range(self.dim_x):
                neigb = self.get_neigbour(x_i, y_i)
                number_of_live = 0
                for i in range(8):
                    if neigb[i]['x'] >= 0 and neigb[i]['x'] < self.dim_x \
                       and neigb[i]['y'] >= 0 and neigb[i]['y'] < self.dim_y:
                        if self.pixels[neigb[i]['x']][neigb[i]['y']].is_live():
                            number_of_live = number_of_live + 1
                if number_of_live == 2:
                    self.pixels[x_i][y_i].set_next_live(
                        self.pixels[x_i][y_i].is_live())
                elif number_of_live == 3:
                    self.pixels[x_i][y_i].set_next_live(True)
                else:
                    self.pixels[x_i][y_i].set_next_live(False)

        ## Update the pixels in the universe
        for y_i in range(self.dim_y):
            for x_i in range(self.dim_x):
                self.pixels[x_i][y_i].step()

    def get_neigbour(self, x_i, y_i):
        """Get the coordinates of the neigbours at coodrinates (x,y)

        @param x_i x-coordinates of the pixel to get neigbours from
        @param y_i y-coordinates of the pixel to get neigbours from

        @cond
        >>> uni = Universe(0, 20, 4, 4, True)
        >>> uni.get_neigbour(2, 2) #doctest:+REPORT_NDIFF +NORMALIZE_WHITESPACE
        [{'y': 1, 'x': 1}, {'y': 2, 'x': 1}, {'y': 3, 'x': 1},
        {'y': 1, 'x': 2}, {'y': 3, 'x': 2}, {'y': 1, 'x': 3},
        {'y': 2, 'x': 3}, {'y': 3, 'x': 3}]

        @endcond
        """
        neigbour = []
        x_min_1 = x_i - 1
        if x_min_1 < 0:
            if self.wrap:
                x_min_1 = self.dim_x - 1

        x_add_1 = x_i + 1
        if x_add_1 >= self.dim_x:
            if self.wrap:
                x_add_1 = 0

        y_min_1 = y_i - 1
        if y_min_1 < 0:
            if self.wrap:
                y_min_1 = self.dim_y - 1

        y_add_1 = y_i + 1
        if y_add_1 >= self.dim_y:
            if self.wrap:
                y_add_1 = 0

        neigbour.append({'x': x_min_1, 'y': y_min_1})
        neigbour.append({'x': x_min_1, 'y': y_i})
        neigbour.append({'x': x_min_1, 'y': y_add_1})
        neigbour.append({'x': x_i, 'y': y_min_1})
        neigbour.append({'x': x_i, 'y': y_add_1})
        neigbour.append({'x': x_add_1, 'y': y_min_1})
        neigbour.append({'x': x_add_1, 'y': y_i})
        neigbour.append({'x': x_add_1, 'y': y_add_1})

        return neigbour

    def display(self):
        """Return a string represents the health of the universe
        @cond
        >>> pixels = [['O',' ','O',' '], \
                       [' ','O',' ','O'], \
                       ['O',' ','O',' '], \
                       [' ','O',' ','O']]
        >>> uni = Universe(0, 20, 4, 4, True)
        >>> uni.set_universe(pixels)
        >>> print uni.display() #doctest: +REPORT_NDIFF +NORMALIZE_WHITESPACE
        ------\
        |O O |\
        | O O|\
        |O O |\
        | O O|\
        ------

        @endcond
        """
        ret_string = '-' * (self.dim_x + 2) + '\n'
        for y_i in range(self.dim_y):
            temp = "|"
            for x_i in range(self.dim_x):
                temp += self.pixels[x_i][y_i].get_symbol()
            ret_string = ret_string + temp + '|' + '\n'
        ret_string = ret_string + '-' * (self.dim_x + 2)
        return ret_string
