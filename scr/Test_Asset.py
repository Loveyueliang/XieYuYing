# 用来分类存储文本
class Text:
    Dict_Text = {}
    # 输入
    def Input(self,Texts,No):
        pass
    # 输出
    def Output(self,No):
        pass

# 玩家的对白存储在着这里 P:
class Text_Player(Text):
    Dict_Player = {}
    def Input(self,Texts,No):
        self.Dict_Player[No] = Texts
    def Output(self,No):
        print(self.Dict_Player[No])

    # 可以根据键取修改对应的文本，因为后面会有一些选项需要选择，所以在你选择其中一个选项后会进行相应的更新
    def Change(self,No,player_say):
        self.Dict_Player[No] = player_say

# 旁白在这 I:
class Text_Aside(Text):
    Dict_Aside = {}
    def Input(self,Texts,No):
        self.Dict_Aside[No] = Texts
    def Output(self,No):
        print(self.Dict_Aside[No])

    # 可以根据键取修改对应的文本，因为后面会有一些选项需要选择，所以在你选择其中一个选项后会进行相应的更新
    def Change(self,No,player_name):
        self.Dict_Aside[No] = player_name

# 独白在这（也就是一开始那一段对Jinx的话） 【:
class Text_Monologue(Text):
    Dict_Monologue = {}
    def Input(self,Texts,No):
        self.Dict_Monologue[No] = Texts
    def Output(self,No):
        print(self.Dict_Monologue[No])

# NPC的对话在这 N：
class Text_NPC(Text):
    Dict_NPC = {}
    def Input(self,Texts,No):
        self.Dict_NPC[No] = Texts
    def Output(self,No):
        print(self.Dict_NPC[No])

    # 可以根据键取修改对应的文本，因为后面会有一些选项需要选择，所以在你选择其中一个选项后会进行相应的更新
    def Change(self,No,NPC_select):
        self.Dict_NPC[No] = NPC_select
