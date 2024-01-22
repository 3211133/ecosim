# -*- coding: utf-8 -*-

"""
    経済シミュレーション
    2次元格子上にランダムに配置されたエージェント
    エージェントは毎thickごとに何か行動を起こす
    行動リスト
    ・前に移動
    ・右、左を向く
    ・前に手持ちの財を与える
    ・前にいるエージェントから財を受け取る
    ・前に地面から財を取る
    ・前に地面に財を置く

    エージェントは
    座標を持つ
    向きを持つ
    財を持つ
    財を生産する

    財は
    種類を持つ
    財は量を持つ
    
"""

from controller import Controller

def main():
    controller = Controller()
    controller.run()

if __name__ == "__main__":
    main()