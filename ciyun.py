import jieba
from wordcloud import WordCloud
import matplotlib
matplotlib.use('Agg')  # 使用非交互式后端
import matplotlib.pyplot as plt

# 加载停用词
stopwords = [line.strip() for line in open('stopwords.txt', encoding='utf-8').readlines()]
stopwords.append("\n")

# 读取文本文件
with open('北京野生动物园.txt', 'r', encoding='utf-8') as f1:
    text = f1.read().strip()

# 分词
words = jieba.lcut(text)

# 统计词频
d = {}
for word in words:
    if word not in stopwords and len(word) > 1:  # 过滤停用词和单字
        d[word] = d.get(word, 0) + 1

# 按词频排序
ls = list(d.items())
ls.sort(key=lambda s: s[-1], reverse=True)

# 输出前20个高频词
print(ls[:20])

# 将高频词写入文件
with open("北京野生动物园.txt", "a", encoding='utf-8') as f:
    for i in range(20):
        f.write(str(ls[i]))
        f.write("\n")

# 生成词云
word_freq = dict(ls)  # 将词频转换为字典
wordcloud = WordCloud(
    font_path='simhei.ttf',  # 设置字体路径（支持中文）
    width=800,
    height=400,
    background_color='white',  # 背景颜色
    max_words=200,  # 最多显示的词数
    stopwords=stopwords  # 设置停用词
).generate_from_frequencies(word_freq)  # 从词频生成词云

# 显示词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # 关闭坐标轴

# 保存词云图
plt.savefig("北京野生动物园.png")
print("词云图已保存为 北京野生动物园.png")