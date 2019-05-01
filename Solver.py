from queue import PriorityQueue
import State
import State_string


class Solver:
    def __init__(self, start, goal):
        self.path = []
        self.visitedQ = []
        self.priorityQ = PriorityQueue()
        self.start = start
        self.goal = goal

    def Solve(self):
        startState = State_string(self.start, 0, self.start, self.goal)
        count = 0
        self.priorityQ.put((0, count, startState))
        while(not self.path and self.priorityQ.qsize()):
            closestChild = self.priorityQ.get()[2]
            closestChild.CreateChildren()
            visitedQ.append(closestChild.value)
            for child in closestChild.children:
                if child.value not in self.visitedQ:
                    count += 1
                    if not child.dist:
                        self.path = child.path
                        break
                    self.priorityQ.put((child.dist, count, child))
        if not self.path:
            print("Goal of "+self.goal+" is not possible")
            return self.path
