from queue import PriorityQueue

# Base class


class State(object):
    def __init__(self, value_in, parent_in, start=0, goal=0):
        self.children = []
        self.parent = parent_in
        self.value = value_in
        self.dist = 0
        if parent_in:
            self.path = parent_in.path[:]  # [:] is to copy complete list
            self.path.append(value_in)
            self.start = parent_in.start
            self.goal = parent_in.goal
        else:
            self.path = [value_in]
            self.start = start
            self.goal = goal
            self.solver = solver

    # Empty functions will be defined in child class
    def GetDist(self):
        pass

    def CreateChildren(self):
        pass
