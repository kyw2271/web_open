
def server() :
    # 통신 정보 설정
    import socket
    import time
    import DB
    IP = '192.168.1.64'# 5051 포트포워딩 / amiya.asuscomm.com DDNS사용 
    PORT = 5051

    SIZE = 1024
    ADDR = (IP, PORT)


    # 서버 소켓 설정
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(ADDR)  # 주소 바인딩

       # try :

        wd = [0,0,0,0]

        server_socket.listen()  # 클라이언트의 요청을 받을 준비
            
        client_socket, client_addr = server_socket.accept()  # 수신대기, 접속한 클라이언트 정보 (소켓, 주소) 반환 (10 waiting )


     
        wd[0] = client_socket.recv(SIZE)  # 클라이언트가 보낸 메시지 반환
        wd[1] = client_socket.recv(SIZE)  # 클라이언트가 보낸 메시지 반환
        time.sleep(0.5)
        wd[2] = client_socket.recv(SIZE)  # 클라이언트가 보낸 메시지 반환
        time.sleep(0.5)
        wd[3] = client_socket.recv(SIZE)  # 클라이언트가 보낸 메시지 반환

        print('클라이언트로 부터 아래의 정보를 입력받았습니다.')
        for i in range(4): # 바이너리 파일 문자열 변환
            print(wd[i].decode('utf-8'))
        DB.create_DB() #DB가 없으면 생
        DB.get_DB(wd[0].decode('utf-8'),wd[1].decode('utf-8'),wd[2].decode('utf-8'),wd[3].decode('utf-8'))
        
       
                



if __name__ == '__main__' :    
    while True :
        server()
