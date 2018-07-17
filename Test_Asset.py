# 用来分类存储文本
class Text:
    Dict_Text = {}
    # 输入
    def Input(self,Texts,No):
        pass
    # 输出
    def Output(self,No):
        pass

# 玩家的说的话存在着这里
class Text_Player(Text):
    Dict_Player = {}

    def Input(self,Texts,No):
        self.Dict_Player[No] = Texts

    def Output(self,No):
        print(self.Dict_Player[No])

# 旁白在这
class Text_Aside(Text):
    Dict_Aside = {}

    def Input(self,Texts,No):
        self.Dict_Aside[No] = Texts
    def Output(self,No):
        print(self.Dict_Aside[No])
    def Change(self,Texts,No,player_name):
        self.Dict_Aside[No] = player_name

# 独白在这（也就是一开始那一段对Jinx的话）
class Text_Monologue(Text):
    Dict_Monologue = {}

    def Input(self,Texts,No):
        self.Dict_Monologue[No] = Texts
    def Output(self,No):
        print(self.Dict_Monologue[No])
