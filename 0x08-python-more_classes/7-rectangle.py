

    def __str__(self):
        """ returns the rectangle with # """
        val = ""
        if self.width == 0 or self.height == 0:
            return val

        for i in range(self.height):
            val += '#' * self.width + "\n"
        return val[:-1]

    def __repr__(self):
        """returns string representation of the instance"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """prints a message when an instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

