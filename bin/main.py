from scr import character, Test_Asset, baiduaip, Plot_branch
import time#,os
import re
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 装载函数，就是把文本从文件里读到程序里- -.
def load_Text():
    # 将储存在文件中的文本内容（剧本）读取到程序并储存在一个临时列表并按照行Text01里
    Text = open('material/对话.txt', 'r+', encoding='utf-8')
    Text = Text.readlines()
    # 定义用来分类储存对话、旁白、独白等文本的类，文本在类中以字典的形式
    # 保存，所以还有以flag结尾的变量来表示它们对应的键。（如果还需要更多
    # 类型的文本还可以定义）
    return Text

# 把存储在文本类里面的不同类型的对白读出来
def Print(start,end,target):
    for each in range(start,end+1):
        target.Output(each)
        time.sleep(1)

# 把更新了name的玩家的文本（相当于存档）读取到程序。
def Loading_personal_save(Story,Player):
    Text = []
    for each in Story:
        each = re.sub('name',Player.name,each)
        Text.append(each)
    return Text

# 将文本分类存储
def Classification(Text,Aside,Monologue,Player,NPC):
    # 对应文本的键值
    Aside_flag = 0
    Monologue_flag = 0
    Player_flag = 0
    NPC_flag = 0
    for each in Text:
        if each[0:1] == '【':
            Aside_flag += 1
            Aside.Input(each, Aside_flag)
        if each[0:2] == 'I：':
            Monologue_flag += 1
            Monologue.Input(each, Monologue_flag)
        if each[0:2] == 'P：':
            Player_flag += 1
            Player.Input(each, Player_flag)
        if each[0:2] == 'N：':
            NPC_flag += 1
            NPC.Input(each, NPC_flag)



# 第一章
def Chapter_01(xieyuying, Aside_Text, Monologue_Text, Player_Text, NPC_Text, Plot_branch01, Plot_branch02):
    # 第一章
    print('--------------------------???-----------------------------------')
    Print(7, 9, Monologue_Text)
    time.sleep(3)
    Print(10, 11, Monologue_Text)
    Print(1, 1, Player_Text)

    Print(12, 14, Monologue_Text)
    Your_select = input()
    Player_Text.Change(2, Your_select)
    Print(2, 2, Player_Text)
    Print(15, 17, Monologue_Text)
    res = baiduaip.client.sentimentClassify(Your_select)["items"][0]['sentiment']
    print("-----------当前谢雨潆好感度为:", xieyuying.adjustImpression(res))

    Your_select = input()
    Player_Text.Change(3, Your_select)
    Print(3, 3, Player_Text)
    res = baiduaip.client.sentimentClassify(Your_select)["items"][0]['sentiment']
    print("-----------当前谢雨潆好感度为:", xieyuying.adjustImpression(res))

    Print(18, 19, Monologue_Text)
    Print(2, 2, NPC_Text)
    Print(20, 22, Monologue_Text)
    print('--------------------------高伟达-----------------------------------')
    Print(23, 26, Monologue_Text)
    Print(3, 3, NPC_Text)
    Print(27, 29, Monologue_Text)

    Print(4, 4, Player_Text)
    No = int(input('你要怎么做呢？\n'))
    Your_select = Plot_branch02.Plot_branch02_Dict01[No]

    Player_Text.Change(4, Your_select)
    Print(4, 4, Player_Text)

    Print(30, 31, Monologue_Text)
    Print(4, 4, NPC_Text)

    You_say = input()
    Player_Text.Change(5, You_say)
    Print(5, 5, Player_Text)

    Print(5, 6, NPC_Text)
    Print(32, 32, Monologue_Text)

    You_say = input()
    Player_Text.Change(6, You_say)
    Print(6, 6, Player_Text)

    Print(33, 35, Monologue_Text)

    Print(7, 7, Player_Text)
    No = int(input('你要怎么做呢？\n'))
    Your_select = Plot_branch01.Plot_branch01_Dict01[No]
    Player_Text.Change(7, Your_select)
    Print(7, 7, Player_Text)

    if No == 1:
        print('------------------------------支线1_1_a--------------------------')
        Print(36, 36, Monologue_Text)
        Print(7, 7, NPC_Text)
        Print(37, 37, Monologue_Text)

        Print(8, 8, Player_Text)
        No = int(input('你要怎么做呢？\n'))
        Your_select = Plot_branch02.Plot_branch02_Dict02[No]
        Player_Text.Change(8, Your_select)
        Print(8, 8, Player_Text)
        NPCs_select = Plot_branch02.Plot_branch02_Dict03[No]
        NPC_Text.Change(8, NPCs_select)
        Print(8, 8, NPC_Text)

        Print(9, 9, NPC_Text)

        Print(9, 9, Player_Text)
        No = int(input('你要怎么做呢？'))
        Your_select = Plot_branch02.Plot_branch02_Dict04[No]
        Player_Text.Change(9, Your_select)
        Print(9, 9, Player_Text)
        NPCs_select = Plot_branch02.Plot_branch02_Dict05[No]
        NPC_Text.Change(10, NPCs_select)
        Print(10, 10, NPC_Text)

        Print(10, 10, Player_Text)
        No = int(input('你要怎么做呢？\n'))
        if No == 1:
            you_say = input('你要说点啥...\n')
            Plot_branch02.Plot_branch02_Dict06[No] = you_say
        Your_select = Plot_branch02.Plot_branch02_Dict06[No]
        Player_Text.Change(9, Your_select)
        Print(9, 9, Player_Text)
        Aside_select = Plot_branch02.Plot_branch02_Dict07[No]
        Aside_Text.Change(38, Aside_select)
        Print(38, 38, Aside_Text)

        Print(39, 42, Monologue_Text)

        print('-----------------------------------------------谢雨莹----------------------------------------------')

    elif No == 2:
        print('------------------------------支线1_1_b--------------------------')
        Print(43, 46, Monologue_Text)

        You_say = input()
        Player_Text.Change(11, You_say)

        Print(11, 11, Player_Text)

        Print(11, 11, NPC_Text)

        Print(47, 49, Monologue_Text)
        time.sleep(2)
        Print(50, 52, Monologue_Text)

        Print(12, 12, NPC_Text)

        You_say = input()
        Player_Text.Change(12, You_say)
        Print(12, 12, Player_Text)

        Print(53, 53, Monologue_Text)
        Print(13, 13, NPC_Text)

        You_say = input()

        Player_Text.Change(12, You_say)
        Print(12, 12, Player_Text)

        Print(54, 56, Monologue_Text)
        print('-----------------------------------------------秦妍----------------------------------------------')


def main():

    Text_story = Test_Asset.Text.Text

    # 存储剧情分支的类，剧情分支分为主线支线（主线会触发相应的分支，而支线其实没多大影响）
    Plot_branch01 = Plot_branch.Plot_branch01()
    Plot_branch02 = Plot_branch.Plot_branch02()

    # 存储对应文本的类
    Player_Text = Test_Asset.Text_Player()
    Aside_Text = Test_Asset.Text_Aside()
    Monologue_Text = Test_Asset.Text_Monologue()
    NPC_Text = Test_Asset.Text_NPC()

    # 定义的玩家类，用来接收玩家的名称
    Player = character.Player()
    xieyuying = character.XieYuYing()

    #序章
    #Prologue() #序章已经整理到界面上了..
    Player.name = input()
    time.sleep(1)

    # 正篇
    # Text02用来储存更新名字后的剧本...
    Text02 = Loading_personal_save(Text_story,Player)

    # 这里是用来把文本分类的
    Classification(Text02, Aside_Text, Monologue_Text, Player_Text, NPC_Text)

    # 序章的最后一句话，这里会用到更新后的name...
    Print(6, 6, Monologue_Text)
    Chapter_01(xieyuying, Aside_Text, Monologue_Text, Player_Text, NPC_Text, Plot_branch01, Plot_branch02)
main()
