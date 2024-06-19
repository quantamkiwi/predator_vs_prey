

class Being:
    """
    The base being class with energy, speed and position.
    """

    direction = 0
    speed = 0
    energy = 10

    def __init__(self, location):
        """
        Initialize the being to a location that has been assigned to it.
        """
        self.loc = location
    

    def move(self):
        """
        Move in the direction its facing at the speed it is currently at. 
        """
        self.loc += self.speed*self.direction
        self.energy -= self.speed



