import random
from being import Being

class Prey:
    """ 
    Prey class. They have a one in five chance of reproducing every second
    after they have been alive for five seconds. 

    The plan is to add a reinforcement network in here that the prey will give 
    to their offspring as the simulation goes on?
    """
 
    def __init__(self, d):

        # Initializing variables.
        self.counter = 0
        self.dead = False
        self.action = False
        self.chances = [1, 2, 3, 4, 5]
        self.d = d

        # Initializing location on the map.
        self.starting_loc = self.random_location()

        # Initialize a being to the starting location.
        self.b = Being(self.starting_loc)


    def tick(self, map):
        """ 
        Called every second to add itself to the map and 
        potentially reproduce.
        """
        self.map = map
        self.vision()

        # Check if meets the criteria to reproduce.
        if self.counter > 5:
            self.reproduce()
            
        else:
            self.counter += 1 
    

    def reproduce(self):
        """ 
        Reproduce function to execute the random chance of 
        reproducing.
        """
        num = random.choice(self.chances)
        if num == 1:
            self.action = True


    def vision(self):
        """
        Uses the current location of the being and the map 
        to see all of the predators and prey around it.
        """

        a = self.b.loc[1] - 4 
        if a < 0:
            a = 0

        b = self.b.loc[1] + 5 
        if b > self.d[-1]:
            b = self.d[-1]
        
        c = self.b.loc[0] - 4 
        if c < 0:
            c = 0

        d = self.b.loc[0] + 5 
        if d > self.d[-1]:
            d = self.d[-1]

        self.see_prey = self.map.t1[a:b, c:d]
        self.see_pred = self.map.t2[a:b, c:d]


    def recover(self):
        """ 
        Reset if the prey has just reproduced.
        """
        self.action = False
        self.counter = 0
    

    def random_location(self):
        """  
        Compute a random location for the prey to sit itself down on 
        the map.
        """
        return (int(random.choice(self.d)), 
                int(random.choice(self.d)))
    

class Predator:
    """  
    Predator class. A little more complicated, it wants to eat the prey to reproduce
    but if it has been alive for too long without eating then it will die.

    The plan is to create another reinforcement network here.
    """

    def __init__(self, d):

        # Initialize variables.
        self.counter = 0 
        self.action = False
        self.dead = False
        self.d = d

        # Initialize a random location on the map on creation.
        self.starting_loc = self.random_location()

        # Initialize a being to the starting location.
        self.b = Being(self.starting_loc)


    def tick(self, map):
        """
        Called every second to see whether the predator should die or not.
        """
        self.map = map
        self.vision()

        if self.counter > 10:
            self.death()
            self.counter = 0

    def vision(self):
        """
        Uses the current location of the being and the map 
        to see all of the predators and prey around it.
        """

        a = self.b.loc[1] - 4 
        if a < 0:
            a = 0

        b = self.b.loc[1] + 5 
        if b > self.d[-1]:
            b = self.d[-1]
        
        c = self.b.loc[0] - 4 
        if c < 0:
            c = 0

        d = self.b.loc[0] + 5 
        if d > self.d[-1]:
            d = self.d[-1]

        self.see_prey = self.map.t1[a:b, c:d]
        self.see_pred = self.map.t2[a:b, c:d]    
    
    def death(self):
        """ 
        Upon death, boolean variables need to be changed to let the rest of 
        the team know.
        """
        self.dead = True
        self.action = True


    def recover(self):
        """  
        Reset the action variable after a recent death so it doesnt repeatedly die
        and use up CPU.
        """
        self.action = False


    def random_location(self):
        """  
        Calculate a random location to spawn on the map.
        """
        return (int(random.choice(self.d)), 
                int(random.choice(self.d)))
