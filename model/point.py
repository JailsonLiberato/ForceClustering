class Point:

    def __init__(self):
        self.__charge = -1
        self.__position = None

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
    def charge(self, position):
        self.__position = position
