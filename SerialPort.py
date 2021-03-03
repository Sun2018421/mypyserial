import serial
import serial.tools.list_ports
# import keras
# from keras.datasets import mnist
import threading
import builtins


def displaydata():
    (_, _), (x_test, y_test) = mnist.load_data()
    x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
    # x_test = x_test / 255
    y_test = keras.utils.to_categorical(y_test, 10)
    print(x_test[0])
    return


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


def main():
    # displaydata()
    port = myopen()
    print(port)
    # ReadUARTThread = threading.Thread(target=ReadUART(port))
    # ReadUARTThread.start()
    # port.write('a'.encode())
    n = port.inWaiting()
    data = port.read(10)
    print(data.decode('gbk'))
    port.close()


main()
