from flask import Flask, render_template, request
import numpy as np
import sklearn
import pandas as pd
import joblib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from algorithms.dfs import dfs_algorithms
from algorithms.ida_star import ida_star_algorithms
from models.draw_point import draw_point
from models.get_data import get_matrix, get_heuristic, get_data_knn
from models.point import print_route

app = Flask(__name__)

matrix = [
    [0, 2, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 0, 0, 0],
    [0, 0, 0, 3, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 3, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

heu = [6, 4, 4, 3, 4, 1, 1, 0, 0]

knn_input = (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/dfs', methods=["POST", "GET"])
def dfs():
    global matrix
    image = "../static/images/init.png"
    result = ""
    if request.method == "POST":
        image = "../static/images/dfs.png"
        matrix = get_matrix(request)
        plt.close()
        draw_point(plt=plt)
        result = print_route(dfs_algorithms(matrix), plt=plt)
        plt.savefig("./static/images/dfs.png")

    return render_template(
        'dfs.html',
        image=image,
        result=result,
        matrix=matrix,
    )


@app.route('/ida*', methods=["POST", "GET"])
def ida_star():
    global matrix, heu
    image = "../static/images/init.png"
    result = ""
    if request.method == "POST":
        image = "../static/images/ida_star.png"
        matrix = get_matrix(request)
        plt.close()
        heu = get_heuristic(request)
        result = ida_star_algorithms(matrix, heu)
        print(result)

    return render_template(
            'ida_star.html',
            image=image,
            result=result,
            matrix=matrix,
            h=heu
        )


@app.route('/knn', methods=["POST", "GET"])
def knn():
    global knn_input
    train_data = pd.read_csv("./data/knn/train_data.csv")
    test_data = pd.read_csv("./data/knn/test_data.csv")
    result = [None]

    if request.method == "POST":
        cols = ['RI', 'Na', 'Mg', 'Al', 'Si', 'Ba', 'Fe']

        # Load mô hình và scaler
        loaded_model = joblib.load('./data/knn/knn_model.pkl')
        loaded_scaler = joblib.load('./data/knn/scaler.pkl')
        knn_input = get_data_knn(request)
        data_input = pd.DataFrame(data=[knn_input], columns=cols)
        data_input_scaled = loaded_scaler.transform(data_input)
        result = loaded_model.predict(data_input_scaled)

    return render_template(
        'knn.html',
        train_data=train_data.to_html(classes="table table-hover"),
        test_data=test_data.to_html(classes="table table-hover"),
        result=result[0],
        knn_input=knn_input,
    )


#-------------------------------------------------------------#


@app.route('/bfs')
def bfs():
    return render_template(
        'bfs.html',
        matrix=matrix,
    )


@app.route('/a*')
def a_star():
    return render_template(
        'a_star.html',
        matrix=matrix,
        h=heu,
    )


@app.route('/id3')
def id3():
    return render_template('id3.html')


if __name__ == "__main__":
    app.run(debug=True)