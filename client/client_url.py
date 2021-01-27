
# 접속 정보 설정


def open_client() :
    import socket

    SERVER_IP = 'amiya.asuscomm.com' #ddns연결
    SERVER_PORT = 5050 # 포트 설정
    SIZE = 1024 
    SERVER_ADDR = (SERVER_IP, SERVER_PORT)

    while True :
        # 클라이언트 소켓 설정
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            try:
                client_socket.connect(SERVER_ADDR)  # 서버에 접속
                    
                client_socket.send('ok'.encode())  # 서버에 메시지 전송
                url = client_socket.recv(SIZE)  # 서버로부터 응답받은 메시지 반환
                open_url(url)
            except :
                print('')# 연결오류 처리 - 더 좋은 방법은 없는지?
                
               

            
        
def open_url(url) : #웹으로 url을 여는 함수
    import webbrowser
    url  = url.decode('utf-8')
    print(f'open {url}!')
    webbrowser.open(url)



if __name__ == '__main__' :

    open_client()
