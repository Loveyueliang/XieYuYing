from aip import AipNlp
#情感倾向分析
""" 你的 APPID AK SK """
APP_ID = '11553722'
API_KEY = 'oibkBOpvGpuSHCbRqv3W2AjN'
SECRET_KEY = '1GpZltLF6kod3dkleGEChq5Aqe999PFo'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

# text = "今天很失败"
# res = client.sentimentClassify(text)
# print(type(res),res)




'''
参数	是否必须	类型	说明
text	是	string	输入的文本内容
items	是	array	输入的词列表
+sentiment	是	number	表示情感极性分类结果, 0:负向，1:中性，2:正向
+confidence	是	number	表示分类的置信度
+positive_prob	是	number	表示属于积极类别的概率
+negative_prob	是	number	表示属于消极类别的概率

'''