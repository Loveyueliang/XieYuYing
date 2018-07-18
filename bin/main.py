from scr import character, Test_Asset, baiduaip
import time
import re


# 将储存在文件中的文本内容（剧本）读取到程序并储存在一个临时列表并按照行Text01里
Text = open('dialogue.txt','r+',encoding='gbk')
Text01 = Text.readlines()
# 定义用来分类储存对话、旁白、独白等文本的类，文本在类中以字典的形式
# 保存，所以还有以flag结尾的变量来表示它们对应的键。（如果还需要更多
# 类型的文本还可以定义）
Player_Text = Test_Asset.Text_Player()
Aside_Text = Test_Asset.Text_Aside()
Monologue_Text = Test_Asset.Text_Monologue()
Player_flag = 0
Aside_flag = 0
Monologue_flag = 0

# 定义的玩家类，用来接收玩家的名称
Player = character.Player()


# 序章，因为需要玩家输入名字...所以这一段直接输出。
print("——嗨，Jinx！")
# 通过输入任意键来触发下一对话！后期会更改为鼠标事件触发和超时多少秒触发！！！！！！
# input()
time.sleep(1.5)
print("——真是的，老感觉你还在，有时候做梦都会梦见你呢……")
# input()
time.sleep(1.5)
print("——对不起……")
# input()
time.sleep(1.5)
print("——对了，明天我就要去做最后一件事了，如果还没有结果的话……我们就永远的再见吧！")
# input()
time.sleep(1.5)
print("——等等，差点忘了，那张身份证我还没看呢，上面的名字是……")
# input()
time.sleep(1.5)
print("【请输入身份证姓名：name】")
#这里让玩家输入名字...
Player.name = input()



# Text02用来储存更新名字后的剧本...
Text02 = []
for each in Text01:
    each = re.sub('name',Player.name,each)
    Text02.append(each)



# 这里是用来把文本分类的
for each in Text02:
    if each[0:1] == '【':
        Aside_flag += 1
        Aside_Text.Input(each,Aside_flag)
    if each[0:2] == '——':
        Monologue_flag += 1
        Monologue_Text.Input(each,Monologue_flag)

# 序章的最后一句话，这里会用到更新后的name...
Monologue_Text.Output(6)






