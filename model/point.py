class Point:
    """Point Model"""

    def __init__(self, position):
        self.__charge = -1
        self.__position = position

    def __str__(self):
        return "Point: " + self.__position

    @property
    def charge(self):
        return self.__charge

    @charge.setter
    def charge(self, charge):
        self.__charge = charge

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position
