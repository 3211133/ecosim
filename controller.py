#controler

import pygame
import sys
from view import View
from pygame.locals import K_SPACE, K_RETURN

class Controller:

    def __init__(self):
        #画面処理クラスのインスタンス
        self.view = View()
        #キーの状態
        self.key_state = pygame.key.get_pressed()


    def update(self):
        pass

    def run(self):
        while True:
            #スペースキーで一時停止
            if self.key_state[K_SPACE]:
                self.time_stop()
            
            #シミュレーションの単位時間ごとの処理
            self.update()

            #画面更新
            self.view.plot()


    #一時停止時の処理
    def time_stop(self):
        #ログ出力
        print("一時停止")
        while True:
            #スペースキーで再開
            if self.key_state[K_SPACE]:
                print("再開")
                break
            #エンターキーで終了
            if self.key_state[K_RETURN]:
                print("終了")
                sys.exit()