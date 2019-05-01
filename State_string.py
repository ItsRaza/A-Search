from queue import PriorityQueue
import State


class State_string(State):
    def __init__(self, value_in, parent_in, start=0, goal=0):
        super(State_string, self).__init__(
            value_in, parent_in, start, goal)
        self.dist = self.GetDist()

    def GetDist(self):
        if self.value_in == self.goal:
            return 0
        dist = 0
        for i in range(len(self.goal)):
            letter = self.goal[i]
            dist += abs(i-self.value.index(letter))
            return dist

    def CreateChildren(self):
        if not self.children:
            for i in range(len(self.goal)-1):
                val = self.value
                val = val[:i]+val[i+1]+val[i]+val[i+2:]
                child = State_string(val, self)
                self.children.append(child)
