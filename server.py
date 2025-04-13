from flask import Flask, render_template, request as re
from graphs import draw_graph
import pandas as pd
from search import search_query

app = Flask('TempName')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST', 'GET'])
def search():
    data = re.args.get('query')
    res = search_query(data)
    return render_template('search.html', data=res)


@app.route('/dash_board')
def dash_board():
    return render_template('dash_board.html')


PERIODS = {
    0: 'Неизвестный период',
    1: '1891 - 1916 гг.',
    2: '1917 - 1940 гг.',
    3: '1941 - 1965 гг.',
    4: '1966 - 1985 гг.',
    5: '1986 - 1992 гг.',
    6: '1993 - 2014 гг.'
}

df = pd.read_csv("final_filtered.csv")

for i in range(7):
    draw_graph(df[df["временной.период"] == PERIODS[i]], 'Страна..откуда.', 'Страна..куда.', PERIODS[i],
               f'static/img/{i}.png')

app.run(debug=True, host='0.0.0.0', port='8080')
