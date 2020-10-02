import naverTransfer
import json

def readText():
    f = open('test.txt')
    resultBuffer = []
    buffer = f.readlines()
    for line in buffer:
        if line == '\n':
            continue
        text = line.replace('\n','')
        resultBuffer.append(text)
    print("read Text Len: ", len(resultBuffer))
    print("read Text : ", resultBuffer)
    return resultBuffer

def transResult(inputBuffer):
    sendBuffer = ''
    transResult = ''
    totalCount = 0
    count = 0
    for line in inputBuffer:
        # print(len(line))

        count += len(line)
        totalCount += len(line)
        if count < 2000:
            sendBuffer += line + '\n'
            print("Check number : ", count, line)
        else:
            sendBuffer += line + '\n'
            print("Check number : ", count, line)
            code, temp = naverTransfer.useTransferRequest(sendBuffer)
            if code != 200:
                print("error", code, temp)
            else:
                transResult += temp['message']['result']['translatedText']

            # sendBuffer = ''
            # count = 0
            break

    if totalCount < 2000:
        code, temp = naverTransfer.useTransferRequest(sendBuffer)
        if code != 200:
            print("error", code, temp)
        else:
            transResult += temp['message']['result']['translatedText']

    return totalCount, sendBuffer, transResult

def myTest():
    code, temp = naverTransfer.useTransferRequest("hi")
    if code == 200:
        print(code, temp['message']['result'])
    else:
        print(code, temp)


if __name__ == '__main__':
    inputBuffer = readText()
    totalcount, sendBuffer, result = transResult(inputBuffer)
    print("total Word Count : " , totalcount)
    print("Send Text \n", sendBuffer)
    print("Transfer Result \n", result)



