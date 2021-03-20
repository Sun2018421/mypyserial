from sklearn.metrics import log_loss
import numpy as np
import keras
from keras.datasets import mnist


def getTP():
    return


def getFP():
    return


def getTN():
    return


def getFN():
    return


def evaluate():

    # True Positive : TP
    # False Positive : FP
    # True Negative : TN
    # False Negative : FN
    TP = getTP()
    FP = getFP()
    TN = getTN()
    FN = getFN()
    # TPR , sensitivity
    TPR = TP / (TP + FN)
    # TNR , specificity
    TNR = TN / (TN + FP)
    # FPR
    FPR = FP / (TN + FP)
    # FNR
    FNR = FN / (TP + FN)

    #F1 score

    return


def getdata():
    (_, _), (x_test, y_test) = mnist.load_data()
    x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
    # x_test = x_test / 255
    # y_test = keras.utils.to_categorical(y_test, 10)
    return (x_test, y_test)


def getDataFromText(filename):
    data = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            eachline = line.split()
            read_data = [float(x) for x in eachline[:]]
            data.append(read_data)
            line = f.readline()
    return data


def main():
    y_pred = getDataFromText("lenet_test.txt")
    (x_test, y_test) = getdata()
    y_pred_np = np.array(y_pred)
    print(np.__version__)
    labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    y_test_list = y_test.tolist()
    print(y_test.shape)
    print(y_test)
    print(y_test_list)
    y_test_list_new = [str(x) for x in y_test_list]
    # print(type(y_pred))
    # print(type(y_pred_np))
    # print(type(y_test))
    # print(type(y_test_list))
    sk_log_loss = log_loss(y_test_list_new, y_pred, labels=labels)
    print("Loss by sklearn is:%s." % sk_log_loss)
    evaluate()


if __name__ == "__main__":
    main()
