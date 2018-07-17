#coding:utf-8

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
    def addImpression(self):
        '''
        增加好感度,需要读取一个相应动作和要增加的好感度对应的字典.
        :return:
        '''
        pass
    def subImpression(self):
        '''
        减少好感度,需要读取一个相应动作和要减少的好感度对应的字典.
        :return:
        '''

class XieYuYing(People, Impression):
    #谢雨莹的好感度,还需要亲密度:好感度另外创建类,亲密度写该类里面
    def __init__(self, impression):
        '''
        :param impression:好感度
        '''
        People.__init__(self)
        self.name = '谢雨莹'
        self.impression = impression

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
    pass

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

# pl = Player()
#
# pl.name = 'value'
# print(pl.name)
# print(pl)