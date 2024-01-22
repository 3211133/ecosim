# Purpose: 方向を表すクラス
import enum

#相対的な向き（左右）を表すクラス
class Turn(enum.Enum):
    Left = -1
    Right = 1

#絶対的な向き(東西南北)のクラス
class Direction:
    # 0:北, 1:東, 2:南, 3:西
    # →x
    # ↓y     ↑0(0,-1)
    #3(-1,0)←　→1(1,0)
    #        ↓2(0,1)

    max_direction = 4

    def __init__(self, direction):
        self.direction = direction % self.max_direction
    
    def get_direction(self):
        return self.direction
    
    def turn(self, turn:Turn):
        self.direction = (self.direction + turn.value) % self.max_direction

    #向きと座標の対応
    # 0:北, 1:東, 2:南, 3:西
    #外から操作できないようにする
    toPosition = {(0, -1), (1, 0), (0, 1),(-1, 0)}
    #return (x, y)
    def getForward(self):
        return  self.toPosition[self.direction]

