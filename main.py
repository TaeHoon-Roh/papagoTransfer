import naverTransfer
import json


def readText():
    f = open('test.txt', encoding='UTF-8')
    resultBuffer = []
    buffer = f.readlines()
    for line in buffer:
        if line == '\n':
            continue
        text = line.replace('\n', '')
        resultBuffer.append(text)
    print("read Text Len: ", len(resultBuffer))
    print("read Text : ", resultBuffer)
    readHeader = resultBuffer[0].split(' ')
    return readHeader, resultBuffer[1:]


def transResult(readHeader, inputBuffer, setCount):
    langFlag = 0
    transResultBuffer = []
    totalCountBuffer = []
    sendResultBuffer = []

    while 1:
        sourceLang = readHeader[langFlag]
        langFlag += 1
        targetLang = readHeader[langFlag]

        sendBuffer = ''
        transTextResult = ''
        totalCount = 0
        count = 0

        for line in inputBuffer:
            # print("InputBuffer Check : ", inputBuffer, line, len(line))

            count += len(line)
            totalCount += len(line)
            if count < setCount:
                sendBuffer += line + '\n'
            else:
                sendBuffer += line + '\n'
                code, temp = naverTransfer.useTransferRequest(sourceLang, targetLang, sendBuffer)
                if code != 200:
                    print("error", code, temp)
                else:
                    transTextResult += temp['message']['result']['translatedText']
                    transResultBuffer.append(transTextResult)
                    sendResultBuffer.append(sendBuffer)
                    totalCountBuffer.append(totalCount)

                # 10000자가 넘는 경우 error가 발생 -> 유료 모드로 전환하면 사용 가능
                # 유료 모드로 사용하는 경우 break를 주석 처리하고, sendBuffer와 count 부분 주석 해제
                # sendBuffer = ''
                # count = 0
                break

        # 전체 파일의 길이가 2000이 안되는 경우 이부분 한번만 실행됨

        if totalCount < setCount:
            code, temp = naverTransfer.useTransferRequest(sourceLang, targetLang, sendBuffer)
            if code != 200:
                print("error", code, temp)
            else:
                transTextResult += temp['message']['result']['translatedText']
                transResultBuffer.append(transTextResult)
                sendResultBuffer.append(sendBuffer)
                totalCountBuffer.append(totalCount)

        # print("MyCheck : ", sourceLang, targetLang, sendBuffer, transTextResult)
        if langFlag + 1 == len(readHeader):
            break
        else:
            inputBuffer = str(transTextResult + '\n').split('\n')[:len(inputBuffer)]
        # print("Copy InputBuffer Check : ", inputBuffer)

    return totalCountBuffer, sendResultBuffer, transResultBuffer


def myTest():
    code, temp = naverTransfer.useTransferRequest("hi")
    if code == 200:
        print(code, temp['message']['result'])
    else:
        print(code, temp)


if __name__ == '__main__':
    readHeader, inputBuffer = readText()
    print(readHeader)
    print(inputBuffer)
    # 일단 Test 부분, 원하는 번역 길이를 숫자로 넣음, 현재 2000으로 setting
    totalCount, sendBuffer, result = transResult(readHeader, inputBuffer, 100)
    print("total Word Count : ", totalCount)
    print("Send Text \n", sendBuffer)
    print("Transfer Result \n", result)
