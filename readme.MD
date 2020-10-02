# papago Transfer Module

## 사용 방법

### naver Developer
naverDev폴더 -> readme.md 확인

### visualStudio code 
vscode폴더 -> readme.md 확인

### Dir Script

* 프로젝트 구조는 다음과 같음
    * papagoTransfer
        * main.py
        * naverTransfer.py
        * naverKey
        * test.txt
    
* main.py
    * __name__ == '__main__' script
        * 64번째 라인이 실제 실행되는 부분
        * 67번째 라인의 가장 끝부분에 번역하고 싶은 길이를 입력해야 함
        * 초기 세팅은 2000자임
        * 68번째 라인은 총 번역한 길이를 나타냄
        * 69번째 라인은 번역 요청한 원문을 나타냄
        * 70번째 라인은 번역한 결과를 나타냄
    * def readText() function
        * 4번째 라인이 원문을 읽는 부분
        * test.txt파일 내용을 줄 단위로 읽고 있음
        * 파일을 바꾸고 싶으면, 현재 폴더안에 파일을 넣고 파일 명을 f = open('filename') 바꿀 수 있음
        * 파일을 넣을때는 항상 txt 파일로 바꿔서 넣을 것, doc, hwp 는 읽을 수 없음
        * 그 외 다른 부분은 변경 x
    * def transResult() function
        * 실제 번역이 실행되는 부분
        * 유료 모듈을 사용하는 경우, 39번째 줄 참조
        
* naverTransfer.py
    * def readNaverKey() function
        * naverKey file을 읽는 module
    * def useTransferRequest() function
        * 21번째 줄에 "source=en&target=ko&text=" 부분이 있음
        * source => 번역을 해야하는 언어의 종류
        * target => 번역 결과물 언어의 종류
        * text => 보내는 내용
        * en ko 외 다른부분 절때 변경하지 말 것
        * 띄어쓰기, 연산자 하나만 잘못 들어가도 오류남
    * def useTransfer() function
        * 소스 원본 사용 x

* naverKey.txt
    * naver developer에서 받은 api key를 넣는 곳
    * key 관리 정책때문에 올릴 수 없음
    * 홈페이지에서 복사 붙여넣기해서 키 저장 할 것
    
* test.txt
    * test용 
  
         
    

    