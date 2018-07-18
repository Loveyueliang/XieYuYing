#coding:utf-8
#author:SiJinHui
from math import e
class People():
    #实现一个根据剧情调用相应的对话,参数传剧情代码,类似1-11这种
    def __init__(self):
        self.name = '对不起,名字未定义.'
    def invoking_database(self):
        '''
        参数用name 和剧情代码一起
        :param talk_data:调用数据库的对话存储在该属性里
        :return:返回需要获取的对话内容
        '''
        self.talkData = '测试文本'
        return self.talkData
    def __str__(self):
        '''
        :return:返回值为需要获取的人物属性信息 比如name,mood
        '''
        return 'Student object (name: %s)' % self.name

class Impression():
    '''
    定义一个好感度的类,需要参数用执行的动作,返回值是对应的好感度,值分 正负.
    '''
    def __init__(self):
        self.impression = 0
        self.impressionIndex = 0
        self.algorithmic = (1 / (e ** (- x - 8)) for x in range(1 * 100))
    def addImpression(self):
        '''
        :return:返回值暂时定为操作后的好感度
        '''
        #print("-------------------", self.impression)
        self.impressionIndex = self.alg().index(self.impression)
        self.impression = self.alg()[self.impressionIndex+1]
        #print("-------------------", self.impression)
        return self.impression
    def subImpression(self):
        '''
        :return:
        '''
        self.impressionIndex = self.alg().index(self.impression)
        self.impression = self.alg()[self.impressionIndex - 1]
        return self.impression

    def alg(self):
        '''
        该函数为生成器,,生成器不行,改列表了
        :return: 用next调用来返回下一次的好感度
        '''
        x = 0
        impressionList = []
        while x < 100:
            if x <= 20:
                y = (x * x / 20) + (3 * x) / 2
                impressionList.append(round(y))
            if x > 20:
                y = 110 - 1000 / x
                impressionList.append(round(y))
            x += 1
        #print(impressionList)
        return impressionList

class XieYuYing(People, Impression):
    #谢雨莹的好感度,还需要亲密度:好感度另外创建类,亲密度写该类里面
    def __init__(self):
        '''
        :param impression:谢雨莹的初始好感度,固定值,暂时设定为调用70次的next(alg())不知道行不行
        '''
        People.__init__(self)
        Impression.__init__(self)
        self.name = '谢雨莹'
        self.impressionIndex = 20
        self.impression = 50
        #self.impression = n
        #print("--------------------------------------",n)
    def adjustImpression(self):
        '''
        调整谢雨莹的好感度
        :return:
        '''
        pass
    def printNarration(self):
        '''
        调用 一 旁白
        :return:
        '''
        pass

class FatBoss(People, Impression):
    def __init__(self):
        People.__init__(self)
        Impression.__init__(self)


class Player(People):
    def __init__(self):
        """
        :param name:玩家名字,需要玩家自定义所以用装饰器,限制命名条件
        :param gold:记录玩家金币,后续考虑做成私有__gold属性,然后用方法修改该值;后期可以考虑弱加密,类似gold*2+1
        """
        People.__init__(self)
        self.gold = 0
    @property
    def name(self):
        return self._name
    #装饰器用来确认输出的是汉字,调用的时候用赋值语句
    @name.setter
    def name(self, value):
        if not '\u4e00' <= value <= '\u9fff':
            raise ValueError("请输入中文名字")
        self._name = value
    def getGold(self):
        '''
        玩家金币增加,当调用的时候,增加1000元
        :return:
        '''
        self.gold += 1000
    def spendMoney(self,commodity):
        '''
        commodity 商品名称 需要在数据库中调用商品价格
        玩家金币减少,
        :param
        :return:
        '''
        price = commodity #后面换成数据库方法,遍历商品列表的时候直接调用数据库就行了.
        self.gold -= price

    # def invoking_database(self):
    #     print("玩家的话,输入或者输出")
    #     talk = input("某些语句")
    #     #判断输入的语句的好感度,跟数据库里的某些好语句 和 坏语句做对比,然后决定调用,增/删好感度
    #     #但是好感度模块做好后,现在玩家的话暂时不需要单独区分


pl = XieYuYing()
print("初始好感度:",pl.impression)
print("增加一次好感度:",pl.addImpression())
#print(pl.impression)
print("增加一次好感度:",pl.addImpression())
print("减少一次好感度:",pl.subImpression())
