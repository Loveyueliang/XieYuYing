#coding:utf-8
class NPC():
    def __init__(self):
        pass

class XieYuYing(NPC):
    def __init__(self,enthusiasm):
        NPC.__init__(self)
        self.name = '谢雨莹'
        self.enthusiasm = enthusiasm

