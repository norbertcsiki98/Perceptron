import numpy as np #kulso library

def main():
    #input
    dataset =  np.array([
      [0, 0, 0],
      [0, 0, 1],
      [0, 1, 0],
      [0, 1, 1],
      [1, 0, 0],
      [1, 0, 1],
      [1, 1, 0],
      [1, 1, 1]
    ])
    #tomb amihez hasolit
    carray = [1,1,1]
    #bias megadas
    bias = -2
    weights = np.array(carray)
    value = np.array([ perceptron(weights, datum, bias) for datum in dataset ])
    #kiiras
    printResult(dataset, value)


def printResult(dataset, value):
    print("AND")
    print("X0\tX1\tX2\tY")
    toPrint = ["{1}\t{2}\t{3}\t{0}".format(output, *datas) for datas, output in zip(dataset, value)]
    for i in toPrint:
        print(i)


def perceptron(weights, inputs, bias):

    model = np.add(np.dot(inputs, weights), bias)
    logit = activation_function(model, type="sigmoid")
    return np.round(logit)


def activation_function(model, type="sigmoid"):

    return {
        "sigmoid": 1 / (1 + np.exp(-model))
    }[type]

#fo foggveny meghivas
main()
