import matplotlib.pyplot as plt

def create_pie_chart(sentiment_counts: dict) -> None:
    """
    Функция для создания круговой диаграммы.
    Вход: словарь sentiment_counts, где ключи — это настроения, а значения — их количество.
    """
    labels = ["Позитивные", "Нейтральные", "Негативные"]
    sizes = [sentiment_counts["позитивное"], sentiment_counts["нейтральное"], sentiment_counts["негативное"]]
    colors = ["#4CAF50", "#FFC107", "#F44336"]
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=140)
    plt.axis("equal")
    plt.savefig("sentiment_pie_chart.png")
    plt.close()
