import serial
import serial.tools.list_ports
import sys
import keras
from keras.datasets import mnist
import threading
import builtins


def getdata():
    (_, _), (x_test, y_test) = mnist.load_data()
    x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
    # x_test = x_test / 255
    y_test = keras.utils.to_categorical(y_test, 10)
    return (x_test, y_test)


def received():
    plist = list(serial.tools.list_ports.comports())
    if len(plist) <= 0:
        print("No serial port found")
    else:
        port = serial.Serial('COM5', 115200, timeout=2)
        if port.isOpen():
            line = port.readline()  # 读一行数据
    return line


def myopen():
    port = serial.Serial('COM5', 115200, 8, 'N', 1, timeout=5)
    if port.isOpen():
        return port


def readuart(port):
    while True:
        ch = port.read()
        print(ch.decode(encoding='ascii'), end='')


def main(argv):
    # displaydata()
    port = myopen()
    print(port)
    # ReadUARTThread = threading.Thread(target=ReadUART(port))
    # ReadUARTThread.start()
    # port.write('a'.encode())
    if(sys.argv[1] == 'Lenet'):  # 根据参数来判断使用的数据参数
        x_test, y_test = getdata()
        interactions = 0
        with open("lenet_test.txt", "w") as f:
            for i in range(x_test.shape[0]):
                singletestdata = x_test[i]
                dimension1 = singletestdata.shape[0]
                dimension2 = singletestdata.shape[1]
                dimension3 = singletestdata.shape[2]
                for j in range(dimension1):
                    for k in range(dimension2):
                        for l in range(dimension3):
                            # print((str(singletestdata[j][k][l])).zfill(3))
                            port.write((str(singletestdata[j][k][l])).zfill(
                                3).encode())  # 因为单片机缓冲是3位，所以填充到3位
                data = port.readline()
                data = data.decode().replace("\r", "")  # 去掉回车符
                f.write(data)
                print("the %dth iterations " % i)
                # print(data)
    port.close()


if __name__ == "__main__":
    # main(sys.argv)
    x_test ,y_test = getdata()
    for i in range(y_test.shape[0]):
        print(y_test[i])
    print(sys.argv[1])
