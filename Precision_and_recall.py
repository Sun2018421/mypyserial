from keras.datasets import mnist
import numpy as np
def getdata():
    (_, _), (x_test, y_test) = mnist.load_data()
    x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
    # x_test = x_test / 255
    # y_test = keras.utils.to_categorical(y_test, 10)
    return (x_test, y_test)

def getNumber(filename):
    data = []
    with open(filename) as f:
        line = f.readline()
        while line:
            eachline = line.split()
            read_data = [float(x) for x in eachline[:]]
            data.append(read_data.index(max(read_data)))
            line = f.readline()
    # data = [str(x) for x in data[:]]
    return data


def getAccuracy(y_pre,y_test):
    accuracy = 0.0
    count = 0
    print(y_pre)
    print(y_test)
    if(len(y_pre)!=len(y_test)):
        return accuracy
    for i in range(len(y_pre)):
        if(y_pre[i] == y_test[i]):
            count = count+1
    accuracy = count/len(y_pre)
    return accuracy

def main():
    y_pre = getNumber("lenet_test.txt")
    (_,y_test) = getdata()
    accuary = getAccuracy(np.array(y_pre),y_test)
    print(accuary)
    return


if __name__ == "__main__":
    main()
