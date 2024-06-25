from races import Prey, Predator
import random


class Team:
    """ 
    Team Class.
    Currently it is made so both preditors and prey will use the same
    team class. This might need a lot of case statements in the 
    future. 
    """

    # Initializations.
    race: int
    name: str
    pop: int
    members: dict
    dead: list
    born: dict

    def __init__(self, race, initial_population, d):
        self.race = race 
        self.pop = initial_population
        self.d = d
        self.members = dict()
        self.dead = list()
        self.born = dict()
        self.create_team()

    def create_team(self):
        """ 
        Creates team members depending on the team race and
        the population. 
        """
        
        match self.race:
            case 0:
                self.name = "prey"
                for i in range(self.pop):
                    self.members[i] = Prey(self.d)
            
            case 1: 
                self.name = "predator"
                for i in range(self.pop):
                    self.members[i] = Predator(self.d)
    

    def tick(self, map):
        """ 
        Every second this function runs to update the
        team members.
        """
        for member in self.members.values():

            # Tick each member.
            member.tick(map)

            if member.action:
                # When prey reproduces or predator dies.
                match self.race:
                    case 0:
                        self.add_member()

                # Clear member.action
                member.recover()

        # Add the born members to the members dictionary.
        self.members.update(self.born)

        # Clear the born dictionary.
        self.born = dict()
    

    def add_member(self):
        """ 
        Adding a membor to the team woohoo.
        """
        self.pop += 1
        match self.race:
            case 0:
                self.born[self.pop] = Prey(self.d)
            
            case 1: 
                self.born[self.pop] = Predator(self.d)
    





            
        
