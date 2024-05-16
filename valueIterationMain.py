import numpy as np
from valueIteration import BellmanUpdate, ValueIteration, GetPolicy
from drawHeatMapWithWalls import drawFinalMap

def main():

    maxX, maxY=6, 6
    minX, minY=0, 0
    stateSpace=[(x, y) for x in range(maxX+1) for y in range(maxY+1)]
    actionSpace=[(0, 1), (1, 0), (0, -1), (-1, 0)]
    actionSpaceFunction=lambda s: actionSpace

    def transitionFunctionMDPFullWalls(s, a, sPrime, maxX, maxY, goals, walls):
        if s in goals:
            return 1*(s==sPrime)
        x, y=s
        dx, dy=a
        xPrime, yPrime=(x+dx, y+dy) #sPrime?
        if xPrime<minX or xPrime>maxX:
            xPrime=x
        if yPrime<minY or yPrime>maxY:
            yPrime=y
        for wall in walls:
            end1, end2 = wall
            if (end1[0] == end2[0]) and (y == yPrime) and (np.sign(y-end1[1])!=np.sign(y-end2[1])) and (np.sign(x-end1[0]) != np.sign(xPrime-end1[0])):
                xPrime = x
            elif (end1[1] == end2[1]) and (x == xPrime) and (np.sign(y-end1[1])!=np.sign(yPrime-end2[1])) and (np.sign(x-end1[0]) != np.sign(x-end2[0])):
                yPrime = y
        return 1*((xPrime, yPrime)==sPrime)

    walls = [[[-.5,2.5], [2.5,2.5]], [[4.5,-.5], [4.5,2.5]], [[.5,4.5], [5.5,4.5]]]
    goals=[(0, 6), (1, 1), (5, 1), (5, 4)]
    goal = (1, 1)

    transitionFunction=lambda s, a, sPrime: transitionFunctionMDPFullWalls(s, a, sPrime, maxX, maxY, goals, walls)


    navigationCost=-5
    goalReward=100
    trapReward=-100
    def rewardFunctionMDPFull(s, a, sPrime, goal, navigationCost, goalReward, trapReward, goals):
        if s in goals:
            return 0
        elif sPrime==goal:
            return goalReward
        elif sPrime in goals:
            return trapReward
        else:
            return navigationCost

    rewardFunction=lambda s, a, sPrime: rewardFunctionMDPFull(s, a, sPrime, goal, navigationCost, goalReward, trapReward, goals)

    gamma=1
    theta=1e-4

    bellmanUpdate=BellmanUpdate(stateSpace, actionSpaceFunction, transitionFunction, rewardFunction, gamma)
    V={s: 0 for s in stateSpace}
    valueIteration=ValueIteration(stateSpace, theta, bellmanUpdate)
    V=valueIteration(V)

    getPolicy=GetPolicy(stateSpace, actionSpaceFunction, transitionFunction, rewardFunction, gamma, V, theta)

    policy={s: getPolicy(s) for s in stateSpace}

    print(policy)

    drawFinalMap(V, policy, {trap: trapReward for trap in goals if trap!=goal}, {goal:goalReward}, [], navigationCost, walls)



if __name__=="__main__":
    main()