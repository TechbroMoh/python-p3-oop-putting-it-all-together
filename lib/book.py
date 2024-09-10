#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._set_page_count(page_count)
    
    def _set_page_count(self, page_count):
        if not isinstance(page_count, int):
            print("page_count must be an integer")
            self._page_count = None
        else:
            self._page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        self._set_page_count(value)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
