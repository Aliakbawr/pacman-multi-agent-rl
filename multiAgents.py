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
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    """

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
        """
        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether the game state is a winning state

        gameState.isLose():
        Returns whether the game state is a losing state
        """

        # TODO: Your code goes here
        def maxValue(gameState, depth, agentIndex, alpha, beta):
            if gameState.isWin() or gameState.isLose() or depth == self.depth:
                return self.evaluationFunction(gameState)
            value = -float("inf")
            for action in gameState.getLegalActions(agentIndex):
                if action == "Stop":
                    continue
                print(f'action={action}')
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
                if action == "Stop":
                    continue
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
            if action == "Stop":
                continue
            ghostValue = minValue(gameState.generateSuccessor(0, action), 0, 1, alpha, beta)
            if ghostValue > bestScore:
                bestScore = ghostValue
                bestAction = action
            if bestScore > beta:
                return bestAction
            alpha = max(alpha, bestScore)
        return bestAction
        # util.raiseNotDefined()
