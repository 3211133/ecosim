
# エージェントのクラス
import random
from direction import Direction, Turn
from agent import Agent


class Agent:
    def __init__(self, x, y, direction:Direction):
        self.x = x
        self.y = y
        self.direction = direction
        #財のリスト
        self.goodsList = []

    ###実行
    #行動を起こす
    def action(self):

        ###他に何かすることがない時移動する
        self.move()

    ###移動
    def move(self):
        if self.isFrontEmpty():
            #前に何もない時前進する
            self.moveForward()
        else:
            #前に何かある時曲がる
            self.turn(random.choice([Turn.Left, Turn.Right]))
    
    #前に移動
    def __moveForward(self):
        (self.x, self.y) += self.direction.getForward()

    #左右を向く
    def __turn(self, turn:Turn):
        self.direction.turn(turn)
    
    ###財のやりとり
    #前に財を与える
    def give(self, agent: Agent):
        agent.receive()

    #前から財を受け取る
    def receive(self):
        pass

#財を生産する
    def produce(self):
        pass
