# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random
import util
from game import Agent
from pacman import GameState


# Evaluates the score for Pacman agent
def scoreEvaluationFunction(currentGameState: GameState):
    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    numFood = currentGameState.getNumFood()
    newGhostPositions = currentGameState.getGhostPositions()
    score = currentGameState.getScore()

    # Run away from ghost
    if min([manhattanDistance(newPos, ghost) for ghost in newGhostPositions]) < 3:
        score -= 10

    # If ghosts are away and there is food, run to the food
    if all(manhattanDistance(newPos, ghost) > 5 for ghost in newGhostPositions):
        distancesToFood = [manhattanDistance(newPos, food) for food in newFood]
        if distancesToFood:
            score -= 1 / (numFood * min(distancesToFood) + 1)
        else:
            score += 1000

    return score


class MultiAgentSearchAgent(Agent):
    def __init__(self, evalFn="scoreEvaluationFunction", depth="2", time_limit="6"):
        super().__init__()
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)
        self.time_limit = int(time_limit)


class AIAgent(MultiAgentSearchAgent):
    def maxValue(self, gameState: GameState, depth, agentIndex, alpha, beta):
        if gameState.isWin() or gameState.isLose() or depth == self.depth:
            return self.evaluationFunction(gameState)
        value = -float("inf")
        for action in gameState.getLegalActions(agentIndex):
            value = max(value, self.minValue(gameState.generateSuccessor(agentIndex, action),
                                             depth, agentIndex + 1, alpha, beta))
            if value > beta:
                return value
            alpha = max(alpha, value)
        return value

    def minValue(self, gameState: GameState, depth, agentIndex, alpha, beta):
        if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)
        value = float("inf")
        for action in gameState.getLegalActions(agentIndex):
            if agentIndex == gameState.getNumAgents() - 1:
                value = min(value, self.maxValue(gameState.generateSuccessor(agentIndex, action),
                                                 depth + 1, 0, alpha, beta))
            else:
                value = min(value, self.minValue(gameState.generateSuccessor(agentIndex, action),
                                                 depth, agentIndex + 1, alpha, beta))
            if value < alpha:
                return value
            beta = min(beta, value)
        return value

    def getAction(self, gameState: GameState):
        alpha = -float("inf")
        beta = float("inf")
        bestScore = -float("inf")
        bestActions = []  # This will hold all the best actions

        for action in gameState.getLegalActions(0):
            pacmanValue = self.maxValue(gameState.generateSuccessor(0, action), 0, 0, alpha, beta)
            print(f'action = {action}   value = {pacmanValue}')
            if action == Directions.STOP:
                pacmanValue -= 4
            if pacmanValue > bestScore:
                bestScore = pacmanValue
                bestActions = [action]  # Start a new list of best actions
            elif pacmanValue == bestScore:
                bestActions.append(action)  # Add action to the list of best actions
            if bestScore > beta:
                return random.choice(bestActions)  # Choose randomly among the best actions
            alpha = max(alpha, bestScore)

        return random.choice(bestActions)  # Choose randomly among the best actions

        # util.raiseNotDefined()
