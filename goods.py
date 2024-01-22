# -*- coding: utf-8 -*-

# 商品クラス
#IDを持つ
#IDを管理するクラスを作る
import random
from .goods import goods

class goods(object):
    #256個のIDを持つ
    MAX_GOODS = 256
    goodsList = [None for i in range(MAX_GOODS)]

    def __init__(self):
        #未使用のIDを探す
        ID = goods.goodsList.index(None)
        #IDを附番する
        goods.goodsList[ID] = self
        self.__ID = ID
    
    def getID(self) -> int:
        return self.__ID
    def __eq__(self, __value: goods) -> bool:
        return self.__ID == __value.getID()
    
#財を生産する
#財を生産するロジックを書く
#材料となる財のリストと成果物となる財のリストを持つ
class goodsProducer(object):

    def __init__(self, inputGoodsSet:set(goods), outputGoodsSet:set(goods)):
        #引数が妥当か確認する
        if inputGoodsSet == None or outputGoodsSet == None:
            raise Exception("引数が不正です")
        self.__inputGoodsSet = inputGoodsSet
        self.__outputGoodsSet = outputGoodsSet

    #生産可能か確認する
    #引数:所有財
    def isProducable(self, inputGoodsList:list(goods)) -> bool:
        return self.__inputGoodsSet.issubset(inputGoodsList)    

    #生産する
    #引数:所有財;引数から材料を消費し、成果物を追加する
    #返り値:生産に成功したか
    def produce(self, GoodsList:list(goods)) -> bool:
        #材料が足りているか確認する
        if not self.isProducable(GoodsList):
            return False

        #材料を消費する
        for inputGoods in self.__inputGoodsSet:
            GoodsList.remove(inputGoods)
        #成果物を増やす
        GoodsList.extend(self.__outputGoodsSet)
        return True
