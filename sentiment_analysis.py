import matplotlib.pyplot as plt
from snownlp import SnowNLP

# 设置支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为 SimHei
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题


def analyze_sentiment(text):
    """
    对文本进行情感分析，返回情感得分（0-1之间，越接近1表示越正面，越接近0表示越负面）
    """
    s = SnowNLP(text)
    return s.sentiments


def visualize_sentiment_bar(sentiment_scores):
    """
    使用柱状图可视化情感分析结果
    """
    plt.figure(figsize=(15, 6))

    # 使用渐变色
    colors = plt.cm.viridis(sentiment_scores)  # viridis 是一种美观的渐变色
    bars = plt.bar(range(len(sentiment_scores)), sentiment_scores, color=colors)

    # 添加颜色条
    sm = plt.cm.ScalarMappable(cmap='viridis', norm=plt.Normalize(vmin=0, vmax=1))
    sm.set_array([])

    # 显式指定颜色条的位置
    cbar = plt.colorbar(sm, ax=plt.gca(), label="情感得分")

    plt.title("情感分析结果（柱状图）", fontsize=16, pad=20)
    plt.xlabel("句子编号", fontsize=12)
    plt.ylabel("情感得分", fontsize=12)
    plt.axhline(y=0.5, color='r', linestyle='--', label="中性阈值")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.savefig("鸟巢评论情感趋势.png", dpi=300, bbox_inches='tight')  # 保存柱状图
    plt.close()


def visualize_sentiment_pie(sentiment_scores):
    """
    使用饼图可视化情感分布
    """
    # 统计情感分布
    positive_count = sum(1 for score in sentiment_scores if score > 0.6)
    neutral_count = sum(1 for score in sentiment_scores if 0.4 <= score <= 0.6)
    negative_count = sum(1 for score in sentiment_scores if score < 0.4)

    # 饼图数据
    labels = ['正面', '中性', '负面']
    sizes = [positive_count, neutral_count, negative_count]

    # 使用更美观的颜色
    colors = ['#66c2a5', '#8da0cb', '#fc8d62']  # 绿色、蓝色、橙色
    explode = (0.05, 0.05, 0.05)  # 突出显示每一部分

    # 绘制饼图
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', startangle=90,
            textprops={'fontsize': 12}, wedgeprops={'edgecolor': 'white', 'linewidth': 1.5})
    plt.title("情感分布（饼图）", fontsize=16, pad=20)
    plt.savefig("鸟巢评论情感分布.png", dpi=300, bbox_inches='tight')  # 保存饼图
    plt.close()


def main():
    # 读取文本文件
    with open('鸟巢.txt', 'r', encoding='utf-8') as f:
        text = f.read().strip()

    # 对每个句子进行情感分析
    sentences = text.split('。')  # 按句号分割文本
    sentiment_scores = [analyze_sentiment(sentence) for sentence in sentences if sentence.strip()]

    # 输出情感分析结果
    print("情感分析结果：")
    for i, score in enumerate(sentiment_scores):
        print(f"句子 {i + 1}: 情感得分 = {score:.4f}")

    # 可视化情感分析结果
    visualize_sentiment_bar(sentiment_scores)  # 柱状图
    visualize_sentiment_pie(sentiment_scores)  # 饼图


if __name__ == "__main__":
    main()