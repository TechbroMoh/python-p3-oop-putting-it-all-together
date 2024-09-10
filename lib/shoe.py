#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._set_size(size)
        self.condition = 'New'

    def _set_size(self, size):
        if not isinstance(size, int):
            print("size must be an integer")
            self._size = None
        else:
            self._size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._set_size(value)

    def cobble(self):
        print("Your shoe is as good as new!")  
        self.condition = 'New'
