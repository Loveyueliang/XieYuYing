import time
class Plot_branch():
    pass
# 触发剧情分支的选择
class Plot_branch01():
    Plot_branch01_Dict01 = {1:'观察高伟达的脸色',
                        2:'去搀扶女子'}


# 这里是触发那个事件难易程度的 选项。
class Plot_branch02():
    Plot_branch02_Dict01 = {1: '1.领导，您好。',
                          2: '2.不好意思领导，我记错时间了。'}
    Plot_branch02_Dict02 = {1: '1.我需要在外面等着吗？',
                          2: '2.好的'}
    Plot_branch02_Dict03 = {1: 'N：不需要。',
                          2: 'pass'}
    Plot_branch02_Dict04 = {1: '1.大概等多久呢？',
                          2: '2.再见'}
    Plot_branch02_Dict05 = {1: 'N：不用等了，你不符合我们公司的要求。',
                          2: 'pass'}
    Plot_branch02_Dict06 = {1: '1.******',
                          2: '2.pass'}
    Plot_branch02_Dict07 = {1: '当他用冰冷的眼神看我的时候，我从里面读到了：我最好立刻走出去，不然将再也没有任何机会进入这个公司',
                          2: 'pass'}

# 序章内容
def Prologue():
    # 序章，因为需要玩家输入名字...所以这一段直接输出。
    list_text = ("I：嗨，Jinx！","I：真是的，老感觉你还在，有时候做梦都会梦见你呢……","I：对不起……","I：对了，明天我就要去做最后一件事了，如果还没有结果的话……我们就永远的再见吧！","I：等等，差点忘了，那张身份证我还没看呢，上面的名字是……","【请输入身份证姓名：name】")
    print()
    # 通过输入任意键来触发下一对话！后期会更改为鼠标事件触发和超时多少秒触发！！！！！！
    generator = (x for x in list_text)
    # 这里让玩家输入名字...
    #print(next(list_text))
    return generator

#Prologue()