from queue import PriorityQueue
import State
import State_string
import Solver

if __name__ == "__main__":
    start1 = "hma"
    goal1 = "ham"
    print("Starting...")
    a = Solver(start1, goal1)
    a.Solve()
    for i in range(len(a.path)):
        print("%d)" % i+a.path[i])
