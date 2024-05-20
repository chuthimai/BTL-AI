dt = {'Outlook': {'Overcast': 'Yes',
             'Rain': {'Wind': {'Strong': 'No', 'Weak': 'Yes'}},
             'Sunny': {'Humidity': {'High': 'No', 'Normal': 'Yes'}}}}


def fun(t):
    global dt
    d = dt
    """
    d -- decision tree dictionary
    t -- testing examples in form of pandas dataframe
    """
    res = []
    for _, e in t.iterrows():
        res.append(predict(d, e))
        # print(predict(d, e))
    return res


def predict(d, e):
    """
    d -- decision tree dictionary
    e -- a testing example in form of pandas series
    """
    current_node = list(d.keys())[0]
    # print('curent node: ', current_node)
    current_branch = d[current_node][e[current_node]]
    # if leaf node value is string then its a decision
    if isinstance(current_branch, str):
        return current_branch
    # else use that node as new searching subtree
    else:
        return predict(current_branch, e)
