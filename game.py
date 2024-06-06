import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as anim
from teams import Team


class MoreThanTwoTeamsException(Exception):
    pass

class Game:
    """ 
    Grapher class, responsible for holding the map. Plotting the map
    and updating it. Currently not able to get this to work. It is 
    definitely the biggest roadblock atm.
    """

    def __init__(self, size):

        # Initializing variables.
        self.size = size
        self.d = np.linspace(-size, size, size*2 + 1)
        self.xs = self.d.copy()
        self.ys = self.d.copy()
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
        t1 = self.ax.scatter(0,0, color='g')
        t2 = self.ax.scatter(0,0)

        def animation_frame(i):
            """
            Main Loop of the program.
            """
            
            # Specify to the teams that one period of time has passed.
            self.tick()

            # Load in all of the location data for each unit in each team.
            self.t1_xs = np.array(
                [unit.loc[0] for unit in self.teams[0].members.values()]
            )
            self.t1_ys = np.array(
                [unit.loc[1] for unit in self.teams[0].members.values()]
            )
            t1.set_offsets(np.c_[self.t1_xs, self.t1_ys])

            if len(self.teams) > 1:
                self.t2_xs = np.array(
                    [unit.loc[0] for unit in self.teams[1].members.values()]
                )
                self.t2_ys = np.array(
                    [unit.loc[1] for unit in self.teams[1].members.values()]
                )
                t2.set_offsets(np.c_[self.t1_xs, self.t1_ys])

            # Updates the user on time and population.
            print(f'Time: {i} Seconds, Population: {self.teams[0].pop}')
            
            return t1

        # Creates the animation and runs the loop.
        animation = anim.FuncAnimation(self.fig, func=animation_frame, frames=np.arange(0, 100, 1), interval=1000)

        # Show the animation.
        plt.show()

    def set_prey(self, loc):
        """  
        The prey call this themselves to add themselves to the mapper.
        Not sure how well this is doing...
        """
        self.prey_xs = np.append(self.prey_xs, loc[0])
        self.prey_ys = np.append(self.prey_ys, loc[1])

    def set_predator(self, loc):
        """  
        The predators call this themselves to add themselves to the mapper.
        Not sure how well this is doing...
        """
        self.predator_xs = np.append(self.predator_xs, loc[0])
        self.predator_ys = np.append(self.predator_ys, loc[1])


    def create_team(self, race, initial_population):
        """
        Creates a team to add to the game.
        Race: 0 - Prey, 1 - Predator
        Initial Population - Integer
        """
        if len(self.teams) == 2:
            raise MoreThanTwoTeamsException("You tried to create a third team!")
        else:
            self.teams.append(Team(race, initial_population, self.d))


    def tick(self):
        """
        Specifies to the team that one period of time has passed.
        """
        for t in self.teams:
            t.tick()

            
        



# Testers.

# m = Map()
# print(m.xs)
# g = Graph(m.xs, m.ys)
# g.draw()