#coding:utf-8
class NPC():
    #实现一个根据剧情调用相应的对话,参数传剧情代码,类似1-11这种
    def __init__(self):
        self.name = ''
        pass
    def invoking_database(self):
        '''
        :param talk_data:调用数据库的对话存储在该属性里
        :return:
        '''
        self.talk_data = '测试文本'
        return self.talk_data
    def __str__(self):
        '''
        :return:返回值为需要获取的人物属性信息 比如name,mood
        '''
        return 'Student object (name: %s)' % self.name

class XieYuYing(NPC):
    def __init__(self,enthusiasm):
        '''

        :param enthusiasm:好感度
        '''
        NPC.__init__(self)
        self.name = '谢雨莹'
        self.enthusiasm = enthusiasm


xie = XieYuYing(80)
print(xie)