import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx


def draw_graph(df, col_sender: str, col_recepient: str, period: str, path: str):
    # Создаём пустой граф
    G = nx.DiGraph()

    # Проходим по каждой строке df
    for _, row in df.iterrows():
        sender = row[col_sender]
        recipient = row[col_recepient]

        # Добавляем узлы
        G.add_node(sender)
        G.add_node(recipient)

        # Добавляем ребро между отправителем и получателем
        G.add_edge(sender, recipient)

    # Визуализация графа
    fig, ax = plt.subplots(figsize=(10, 8))  # Создаём фигуру и оси
    pos = nx.spring_layout(G, k=2.5)  # Позиционируем узлы
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color='lightblue',
        edge_color='gray',
        node_size=1000,
        font_size=8,
        font_weight='bold',
        ax=ax
    )
    ax.set_title(
        f"Связи между странами-отправителями и получателями за {'неопределённый период времени' if period == 'Неизвестный период' else period}",
        fontsize=14)
    # plt.show()
    plt.savefig(path)



