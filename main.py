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

def transResult(inputBuffer, setCount):
    sendBuffer = ''
    transResult = ''
    totalCount = 0
    count = 0
    for line in inputBuffer:
        # print(len(line))

        count += len(line)
        totalCount += len(line)
        if count < setCount:
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

            # 10000자가 넘는 경우 error가 발생 -> 유료 모드로 전환하면 사용 가능
            # 유료 모드로 사용하는 경우 break를 주석 처리하고, sendBuffer와 count 부분 주석 해제
            # sendBuffer = ''
            # count = 0
            break

    # 전체 파일의 길이가 2000이 안되는 경우 이부분 한번만 실행됨

    if totalCount < setCount:
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
    #일단 Test 부분, 원하는 번역 길이를 숫자로 넣음, 현재 2000으로 setting
    totalcount, sendBuffer, result = transResult(inputBuffer, 2000)
    print("total Word Count : " , totalcount)
    print("Send Text \n", sendBuffer)
    print("Transfer Result \n", result)



