

class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    # overloading addition
    # two vectors
    def __add__(self, vec):
        self.x = self.x + vec.x
        self.y = self.y + vec.y
        self.z = self.z + vec.z



    def __eq__(self, vec):
        if self.x == vec.x and self.y == vec.y and self.z == vec.z:
            return True
        else:
            return False

