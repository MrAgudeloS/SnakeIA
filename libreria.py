from simpleai.search import SearchProblem, astar, depth_first, breadth_first
import math 

COSTS = {
        "up": 1.0,
        "left": 1.0,
        "down": 1.0,
        "right": 1.0
}


class SnakeGame(SearchProblem):

        def __init__(self, initial, goal, listaSnake, direction):
                self.initial = initial
                self.goal = goal
                self.mySnake = listaSnake
                self.direction = direction

                super(SnakeGame, self).__init__(initial_state=self.initial)

        def actions(self, state):
                actions = []
                for action in list(COSTS.keys()):
                        newx, newy = self.result(state, action)
                        collision = self.collisionCheck([newx, newy], self.mySnake)
                        if (newx >= 0) and (newx < 320) and (newy >= 0) and (newy < 320) and not collision:
                                actions.append(action)
                if actions == []:
                    actions = ["right", "right"]
                return actions

        def collisionCheck(self, newPos, listasnake):
            size = len(listasnake)
            for i in range(1,size):
                if newPos == [listasnake[i].rect.x, listasnake[i].rect.y]:
                    return True
            return False

        def result(self, state, action):
                x, y = state
                if action == "up":
                        y -= 16
                if action == "down":
                        y += 16
                if action == "left":
                        x -= 16
                if action == "right":
                        x += 16

                new_state = (x, y)
                return new_state

        def is_goal(self, state):
                return state == self.goal

        def cost(self, state, action, state2):
                return COSTS[action]

        def heuristic(self, state):
                x, y = state
                gx, gy = self.goal
                return math.sqrt((x - gx) ** 2 + (y - gy) ** 2)

def createProblem(listaSnake, food, method, direction):
    problem = SnakeGame((listaSnake[0].rect.x, listaSnake[0].rect.y), (food.rect.x, food.rect.y), listaSnake, direction)
    if method == "astar":
        result = astar(problem, graph_search=True)
    elif method == "dfs":
        result = depth_first(problem, graph_search=True)
    else:
        result = breadth_first(problem, graph_search=True)

    if result == None:
        return False
    moves = result.path()
    moves = moves[1:]
    lm = []

    for i in moves:
        lm.append(i[0])

    lm.reverse()
    return lm
