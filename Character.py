#coding:utf-8
class People():
    #实现一个根据剧情调用相应的对话,参数传剧情代码,类似1-11这种
    def __init__(self):
        self.name = '对不起,名字未定义.'
    def invoking_database(self,):
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

class XieYuYing(People):
    def __init__(self,enthusiasm):
        '''
        :param enthusiasm:好感度
        '''
        People.__init__(self)
        self.name = '谢雨莹'
        self.enthusiasm = enthusiasm

    def printNarration(self):
        '''
        调用 一 旁白
        :return:
        '''
        pass

class Player(People):
    def __init__(self):
        """
        :param gold:记录玩家金币,后续考虑做成私有__gold属性,然后用方法修改该值;后期可以考虑弱加密,类似gold*2+1
        """
        People.__init__(self)
        self.name = '玩家名:稍后再考虑是加个自定义名字,还是'
        self.gold = 0
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