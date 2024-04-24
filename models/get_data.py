from flask import Request


def get_matrix(request: Request):
    matrix = []
    data = request.form.to_dict()
    for i in range(0, 9):
        r = []
        for j in range(0, 9):
            r.append(int(data[f"{i}{j}"]))
        matrix.append(r)
    return matrix


def get_heuristic(request: Request):
    heuristic = []
    data = request.form.to_dict()
    for i in range(0, 9):
        heuristic.append(int(data[f"h{i}"]))
    return heuristic


def get_data_knn(request: Request):
    data_input = []
    data = request.form.to_dict()
    for i in ['ri', 'na', 'mg', 'al', 'si', 'ba', 'fe']:
        data_input.append(float(data[i]))
    return data_input
