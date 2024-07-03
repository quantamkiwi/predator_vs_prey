import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as anim
from teams import Team


class MoreThanTwoTeamsException(Exception):
    pass

class Map:
    """
    Map class to hold the locations of all the members. This means
    the entire map can be passed to each member and the members can access
    their vision through indexing. This increases the speed of the code.
    """

    def __init__(self, xs, ys):

        # Initializing variables.
        self.xs = xs
        self.ys = ys
        self.map = np.zeros((len(self.xs), len(self.ys)))
        self.t1 = self.map.copy()
        self.t2 = self.map.copy()


    def update(self, t1, t2):
        """
        Update the locations of members within the map. 
        """
        self.t1 = self.map.copy()
        self.t2 = self.map.copy()
        for location in t1:
            self.t1[location[1]][location[0]] += 1 
        for location in t2:
            self.t2[location[1]][location[0]] += 1 


class Game:
    """ 
    Grapher class, responsible for holding the map. Plotting the map
    and updating it. Currently not able to get this to work. It is 
    definitely the biggest roadblock atm.
    """

    def __init__(self, size):

        # Initializing variables.
        self.size = size
        self.d = np.linspace(0, size * 2, size*2 + 1)
        self.xs = self.d.copy()
        self.ys = self.d.copy()
        self.map = Map(self.xs, self.ys)
        self.prey_xs = np.array([])
        self.prey_ys = np.array([])
        self.predator_xs = np.array([])
        self.predator_ys = np.array([])
        self.teams = []


    def start(self):
        """
        Function to start the game. 

        The loop is the animation_frame() function. The period of this loop is the interval
        set in the FuncAnimation class initialization.

        """
        # Initializing axes.
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1,1,1)
        self.ax.set_xlim(self.xs[0], self.xs[-1])
        self.ax.set_ylim(self.ys[0], self.ys[-1])
        t1 = self.ax.scatter(0,0, color='g', label="Prey")
        t2 = self.ax.scatter(0,0, color='r', label="Predator")
        self.ax.legend()
        self.ax.grid()

        def animation_frame(i):
            """
            Main Loop of the program.
            """

            # Load in all of the location data for each unit in each team.
            self.t1_xs = np.array(
                [unit.b.loc[0] for unit in self.teams[0].members.values()]
            )
            self.t1_ys = np.array(
                [unit.b.loc[1] for unit in self.teams[0].members.values()]
            )
            t1.set_offsets(np.c_[self.t1_xs, self.t1_ys])
            
            # if len(self.teams) > 1:
            self.t2_xs = np.array(
                [unit.b.loc[0] for unit in self.teams[1].members.values()]
            )
            self.t2_ys = np.array(
                [unit.b.loc[1] for unit in self.teams[1].members.values()]
            )
            t2.set_offsets(np.c_[self.t2_xs, self.t2_ys])

            print([unit.see_prey for unit in self.teams[1].members.values()])
            # print(self.map.t1)
            # Updates the user on time and population.
            print(f'Time: {i} Seconds, Population: {self.teams[0].pop}')

            # Specify to the teams that one period of time has passed.
            self.tick()
            
            return t1, t2

        # Creates the animation and runs the loop.
        animation = anim.FuncAnimation(self.fig, func=animation_frame, frames=np.arange(0, 100, 1), interval=1000)

        # Show the animation.
        plt.show()

    # def set_prey(self, loc):
    #     """  
    #     The prey call this themselves to add themselves to the mapper.
    #     Not sure how well this is doing...
    #     """
    #     self.prey_xs = np.append(self.prey_xs, loc[0])
    #     self.prey_ys = np.append(self.prey_ys, loc[1])

    # def set_predator(self, loc):
    #     """  
    #     The predators call this themselves to add themselves to the mapper.
    #     Not sure how well this is doing...
    #     """
    #     self.predator_xs = np.append(self.predator_xs, loc[0])
    #     self.predator_ys = np.append(self.predator_ys, loc[1])


    def create_team(self, race, initial_population):
        """
        Creates a team to add to the game.
        Race: 0 - Prey, 1 - Predator
        Initial Population - Integer
        """
        if len(self.teams) == 2:
            raise MoreThanTwoTeamsException("You tried to create a third team!")
        else:
            print(f"Team Created. Race: {race}")
            team = Team(race, initial_population, self.d)
            self.teams.append(team)


    def tick(self):
        """
        Specifies to the team that one period of time has passed.
        """
        self.t1_locs = [(self.t1_xs[i], self.t1_ys[i]) for i in range(len(self.t1_xs))]
        if len(self.teams) > 1:
            self.t2_locs = [(self.t2_xs[i], self.t2_ys[i]) for i in range(len(self.t2_xs))]
        else:
            self.t2_locs = []
        
        self.map.update(self.t1_locs, self.t2_locs)

        for t in self.teams:
            t.tick(self.map)

            