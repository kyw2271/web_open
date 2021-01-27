

from multiprocessing import Process

def main_fnc():
		import server_url
        import DB
        import time      
        print('scan start')
        
        while True :
            url = DB.Paer_DB()

            if str(url) != 'None' :
        
                print(url)
                server_url.server_open(url)
            time.sleep(5)

def get_data() :
    import server_DBw
    
    while True :
        server_DBw.server()
 

if __name__ == '__main__' :

    Process(target=main_fnc).start()
    Process(target=get_data).start()