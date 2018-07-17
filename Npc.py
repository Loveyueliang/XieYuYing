#coding:utf-8
class NPC():
    #实现一个根据剧情调用相应的对话,参数传剧情代码
    def __init__(self):

        pass

class XieYuYing(NPC):

    def __init__(self,enthusiasm):
        '''

        :param enthusiasm:好感度
        '''
        NPC.__init__(self)
        self.name = '谢雨莹'
        self.enthusiasm = enthusiasm

