#https://developers.kakao.com/docs/restapi/kakaotalk-api#%EB%82%98%EC%97%90%EA%B2%8C-%EB%B3%B4%EB%82%B4%EA%B8%B0-%ED%85%8D%EC%8A%A4%ED%8A%B8-%ED%85%9C%ED%94%8C%EB%A6%BF-%EB%B3%B4%EB%82%B4%EA%B8%B0
def kakao(mss) :
    import requests # http 전송
    import json # json http관련
    mss =mss+ "을 열어야 합니다"
    #https://developers.kakao.com/docs/restapi/tool  토큰 관련 페이지
    token = '9XU5YA4RUEfisU531o5cnNtNC9U5dyNWYxD7HAo9dZoAAAFulIeMCA'
    header = {"Authorization": 'Bearer ' + token}
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    post = {
        "object_type": "text",
        "text": mss,
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },
    }
    data = {"template_object": json.dumps(post)}
    requests.post(url, headers=header, data=data)
    print('open kakao')
    return 

def server_open(url) :
    # 통신 정보 설정
    import socket
    IP = '192.168.1.64'# 5050 포트포워딩 / amiya.asuscomm.com DDNS사용 
    PORT = 5050

    SIZE = 1024
    ADDR = (IP, PORT)


    # 서버 소켓 설정
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(ADDR)  # 주소 바인딩
        server_socket.settimeout(5) # 5초간 소켓에 반응이 없으면 에러

        try :
         
            server_socket.listen()  # 클라이언트의 요청을 받을 준비
            
            client_socket, client_addr = server_socket.accept()  # 수신대기, 접속한 클라이언트 정보 (소켓, 주소) 반환 (10 waiting )
            
            msg = client_socket.recv(SIZE)  # 클라이언트가 보낸 메시지 반환
            print("[{}]-- {} --".format(client_addr,str(msg)))  # 클라이언트가 보낸 메시지 출력       
            client_socket.sendall(url.encode())  # 클라이언트에게 응답        
            client_socket.close()  # 클라이언트 소켓 종료

        except : #에러 발생시 (5초이상 반응이 없으면)
            kakao(url)

                



if __name__ == '__main__' :
   while True :
        url = input('url open : ')
        server_open(url)
