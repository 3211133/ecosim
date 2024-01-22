# -*- coding: utf-8 -*-
from agent import Agent
import matplotlib.pyplot as plt
"""
    シミュレーション結果を出力する



"""
class View:

    def __init__(self, agentList:list[Agent]):
        self.agentList = agentList

    def plot(self):
        #エージェントの位置を取得
        x = []
        y = []
        for agent in self.agentList:
            x.append(agent.x)
            y.append(agent.y)
        #エージェントの位置をプロット
        plt.scatter(x, y, s=1)
        plt.show()
