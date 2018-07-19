from scr import character, Test_Asset, baiduaip, Plot_branch
import time
import re

# 装载函数，就是把文本从文件里读到程序里- -.
def load_Text():
    # 将储存在文件中的文本内容（剧本）读取到程序并储存在一个临时列表并按照行Text01里
    Text = open('对话.txt', 'r+', encoding='gbk')
    Text01 = Text.readlines()
    # 定义用来分类储存对话、旁白、独白等文本的类，文本在类中以字典的形式
    # 保存，所以还有以flag结尾的变量来表示它们对应的键。（如果还需要更多
    # 类型的文本还可以定义）
    return Text01


def Print(start,end,target):
    for each in range(start,end+1):
        target.Output(each)
        time.sleep(1)

def main():

    Text_story = load_Text()

    # 存储剧情分支的类，剧情分支分为主线支线（主线会触发相应的分支，而支线其实没多大影响）
    Plot_branch01 = Plot_branch.Plot_branch01()
    Plot_branch02 = Plot_branch.Plot_branch02()

    # 存储对应文本的类
    Player_Text = Test_Asset.Text_Player()
    Aside_Text = Test_Asset.Text_Aside()
    Monologue_Text = Test_Asset.Text_Monologue()
    NPC_Text = Test_Asset.Text_NPC()

    # 对应文本的键值
    Aside_flag = 0
    Monologue_flag = 0
    Player_flag = 0
    NPC_flag = 0

    # 定义的玩家类，用来接收玩家的名称
    Player = character.Player()

    # 序章，因为需要玩家输入名字...所以这一段直接输出。
    print("I：嗨，Jinx！")
    # 通过输入任意键来触发下一对话！后期会更改为鼠标事件触发和超时多少秒触发！！！！！！
    # input()
    time.sleep(1.5)
    print("I：真是的，老感觉你还在，有时候做梦都会梦见你呢……")
    # input()
    time.sleep(1.5)
    print("I：对不起……")
    # input()
    time.sleep(1.5)
    print("I：对了，明天我就要去做最后一件事了，如果还没有结果的话……我们就永远的再见吧！")
    # input()
    time.sleep(1.5)
    print("I：等等，差点忘了，那张身份证我还没看呢，上面的名字是……")
    # input()
    time.sleep(1.5)
    print("【请输入身份证姓名：name】")
    # 这里让玩家输入名字...
    Player.name = input()
    time.sleep(1)

    # Text02用来储存更新名字后的剧本...
    Text02 = []
    for each in Text_story:
        each = re.sub('name',Player.name,each)
        Text02.append(each)

    # 这里是用来把文本分类的
    for each in Text02:
        if each[0:1] == '【':
            Aside_flag += 1
            Aside_Text.Input(each,Aside_flag)
        if each[0:2] == 'I：':
            Monologue_flag += 1
            Monologue_Text.Input(each,Monologue_flag)
        if each[0:2] == 'P：':
            Player_flag += 1
            Player_Text.Input(each,Player_flag)
        if each[0:2] == 'N：':
            NPC_flag += 1
            NPC_Text.Input(each,NPC_flag)


    # 序章的最后一句话，这里会用到更新后的name...
    Print(6, 6, Monologue_Text)
    print('--------------------------???-----------------------------------')
    Print(7,9,Monologue_Text)
    time.sleep(3)
    Print(10,11,Monologue_Text)
    Print(1,1,Player_Text)

    Print(12,14,Monologue_Text)
    You_say = input()
    Player_Text.Change(2,You_say)
    Print(2,2,Player_Text)
    Print(15,17,Monologue_Text)

    You_say = input()
    Player_Text.Change(3,You_say)
    Print(3, 3, Player_Text)

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
    Player_Text.Change(5,You_say)
    Print(5, 5, Player_Text)

    Print(5, 6, NPC_Text)
    Print(32, 32, Monologue_Text)

    You_say = input()
    Player_Text.Change(6,You_say)
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





















main()










