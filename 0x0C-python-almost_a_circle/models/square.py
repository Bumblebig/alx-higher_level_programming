#!/usr/bin/python3
"""Square"""

from .rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns the size"""
        return super().width

    @size.setter
    def size(self, value):
        """sets the value of size"""
        Rectangle.width.fset(self, value)
        Rectangle.height.fset(self, value)

    def update(self, *args, **kwargs):
        """update"""
        if kwargs and (args is None or len(args) == 0):
            if 'size' in kwargs.keys():
                aux = {'width': kwargs['size'], 'height': kwargs['size']}
                kwargs.update(aux)
            super().update(*args, **kwargs)
        else:
            args_list = list(args)
            if len(args) > 1:
                args_list.insert(1, args[1])
            super().update(*args_list, **kwargs)

    def to_dictionary(self):
        """ to dictionary """
        new_dict = {'id': self.id,
                    'size': self.height,
                    'x': self.x,
                    'y': self.y}
        return new_dict
