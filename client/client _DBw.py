
# 접속 정보 설정


def open_client() :
    import socket
    import time
    import datetime
    now = time.localtime()

    SERVER_IP = 'amiya.asuscomm.com' #ddns연결
    SERVER_PORT = 5051 # 포트 설정
    SIZE = 1024 
    SERVER_ADDR = (SERVER_IP, SERVER_PORT)

    while True :


        

                


        
        # 클라이언트 소켓 설정
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            # client 구분 위한 고유번호 할당 = ID (자동으로 부여됨)

            mn = int(now.tm_mon)
            url = input('url을 입력하세요 :  ')
            d = input('일 입력(0:오늘  // 1~31) : ')
            if d == '0' :
                d = now.tm_mday
            elif int(d) < now.tm_mday : # 만약 오늘보다 전날이면
                 mn = mn + 1    # 다음달로 저장
                
            h = input('시간 입력(24시간) : ')
            m = input('분 입력           : ') 
            day = input('반복(0 = 없음, 1= 매주, 2=매월 3=매년) :')

            if(day =='1' or day =='2' or day =='3') :
                re = input('얼마나 반복하겠습니까? (1회 ~~) :')
            else:
                re = '0'

            
            s = "%04d-%02d-%02d %02d:%02d" % (now.tm_year, mn, int(d), int(h), int(m))



            
            try:
                client_socket.connect(SERVER_ADDR)  # 서버에 접속for i in range(4):
                client_socket.send(s.encode())  # 서버에 메시지 전송
                client_socket.send(url.encode())  # 서버에 메시지 전송
                time.sleep(0.5)
                client_socket.send(day.encode())  # 서버에 메시지 전송
                time.sleep(0.5)
                client_socket.send(re.encode())  # 서버에 메시지 전송
                
               # url = client_socket.recv(SIZE)  # 서버로부터 응답받은 메시지 반환
                
            except :
                print('')# 연결오류 처리 - 더 좋은 방법은 없는지?
                
               


if __name__ == '__main__' :

    open_client()
