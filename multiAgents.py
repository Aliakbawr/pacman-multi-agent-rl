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


def scoreEvaluationFunction(currentGameState: GameState):
    

    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    def __init__(self, evalFn="scoreEvaluationFunction", depth="2", time_limit="6"):
        super().__init__()
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)
        self.time_limit = int(time_limit)


class AIAgent(MultiAgentSearchAgent):
    def getAction(self, gameState: GameState):
        def maxValue(gameState, depth, agentIndex, alpha, beta):
            if gameState.isWin() or gameState.isLose() or depth == self.depth:
                return self.evaluationFunction(gameState)
            value = -float("inf")
            for action in gameState.getLegalActions(agentIndex):
                value = max(value, minValue(gameState.generateSuccessor(agentIndex, action),
                                            depth, agentIndex + 1, alpha, beta))
                if value > beta:
                    return value
                alpha = max(alpha, value)
            return value

        def minValue(gameState, depth, agentIndex, alpha, beta):
            if gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)
            value = float("inf")
            for action in gameState.getLegalActions(agentIndex):
                if agentIndex == gameState.getNumAgents() - 1:
                    value = min(value, maxValue(gameState.generateSuccessor(agentIndex, action),
                                                depth + 1, 0, alpha, beta))
                else:
                    value = min(value, minValue(gameState.generateSuccessor(agentIndex, action),
                                                depth, agentIndex + 1, alpha, beta))
                if value < alpha:
                    return value
                beta = min(beta, value)
            return value

        alpha = -float("inf")
        beta = float("inf")
        bestScore = -float("inf")
        bestAction = Directions.STOP
        for action in gameState.getLegalActions(0):
            pacmanValue = maxValue(gameState.generateSuccessor(0, action), 0, 0, alpha, beta)
            print(f'action = {action}   value = {pacmanValue}')
            if pacmanValue > bestScore:
                bestScore = pacmanValue
                bestAction = action
            if bestScore > beta:
                return bestAction
            alpha = max(alpha, bestScore)
        return bestAction
        # util.raiseNotDefined()
