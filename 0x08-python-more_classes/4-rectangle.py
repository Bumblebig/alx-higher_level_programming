        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ returns the perimeter of a rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * self.width + 2 * self.height


    def __str__(self):
        """ returns the rectangle with # """
        val = ""
        if self.width == 0 or self.height == 0:
            return val

        for i in range(self.height):
            val += '#' * self.width + "\n"
        return val[:-1]

    def __repr__(self):
        """ returns string representation of the instance """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
