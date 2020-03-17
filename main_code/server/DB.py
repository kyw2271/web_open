
def create_DB () : # DB가 존재하지 않으면 새로 여는 함수
    import sqlite3
    conn= sqlite3.connect('urlDB.db')
    cursor = conn.cursor()

    cursor.execute(''' CREATE TABLE IF NOT EXISTS openlist(date text,url text,day int,repeat int)''')
    # db안에 openlist테이블이 없으면 테이블 생성
    res = cursor.fetchall()
    #print(res)test 용  
    conn.commit()
    conn.close()
    

def save_DB() : # 키보드를 통해 값을 받아 저장하는 함수
    import datetime
    import time
    import sqlite3
    now = time.localtime()
    

    mn = int(now.tm_mon)
    url = input('url을 입력하세요 :  ')
    d = input('일 입력(0:오늘  // 1~31) : ')
    if d == '0' :
        d = now.tm_mday
    elif int(d) < now.tm_mday : # 만약 오늘보다 전날이면
        mn = mn + 1 # 다음달로 저장
        
    h = input('시간 입력(24시간) : ')
    m = input('분 입력           : ') 
    day = input('반복(0 = 없음, 1= 매주, 2=매월 3=매년) :')

    if(day =='1' or day =='2' or day =='3') :
        re = input('얼마나 반복하겠습니까? (1회 ~~) :')
    else:
        re = '0'

    
    s = "%04d-%02d-%02d %02d:%02d" % (now.tm_year, mn, int(d), int(h), int(m))
    #입력받은 시간을 년-월-일 시:분 형식으로 합쳐 저장
    
    conn= sqlite3.connect('urlDB.db')
    cursor = conn.cursor()
    
    sql = 'INSERT INTO openlist (date,url,day,repeat) VALUES(?,?,?,?)'
    data = (s,url,day,re)
    cursor.execute(sql,data)
     # 입력받은 정보를 가공히여 db에 저장
     
    conn.commit()
    conn.close()
    

def get_DB(s,url,day,re) :
# 클라이언트를통해 입력받은 값을 서버를통해 불러와 저장할때 쓸 함수
    import sqlite3
    # 기존 키보드에서 입력받는 함수에서 입력받는 부분이 빠지고, 매개변수로 들어감
    conn= sqlite3.connect('urlDB.db')
    cursor = conn.cursor()
    
    sql = 'INSERT INTO openlist (date,url,day,repeat) VALUES(?,?,?,?)'
    data = (s,url,day,re)

    cursor.execute(sql,data)
    conn.commit()
    conn.close()

    
def show_DB() : # DB저장값을 보여주는 함수

    import sqlite3

    
    conn= sqlite3.connect('urlDB.db')
    cursor = conn.cursor()

    # urlDB.db안에있는 테이블 openlist 에있는 모든값을 출력
    sql = 'SELECT*FROM openlist'
    cursor.execute(sql)
    res = cursor.fetchall()

    for row in res :    
        print(row)
    
    conn.commit()
    conn.close()
    


def Paer_DB(): # 현재 시간과 비교하는 함수
    import sqlite3
    import time
    import datetime
    import dateutil.relativedelta # 윤년을 포함한 월 계산 가능
    
    now = time.localtime()
    s = "%04d-%02d-%02d %02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
    
    print(s)
    conn= sqlite3.connect('urlDB.db')
    cursor = conn.cursor()
    sql = 'SELECT*FROM openlist WHERE date = ?'

    da = datetime.datetime.strptime(wd[0], '%Y-%m-%d %H:%M')
    
    cursor.execute(sql,(s,))

    
    
    for row in cursor :
        
        
        if row[2] == 0 :
            print(row)
            sql = 'DELETE FROM openlist WHERE date= ? AND url = ? AND day = ? '
            cursor.execute(sql,(row[0],row[1],row[2]))
            conn.commit()
            # 삭제하고
            return str(row[1])

        if row[2] == 1 : #  주반복
            if row[3] !=0 :

                old = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M')
                add = dateutil.relativedelta.relativedelta(days=7)
                new = old + add

                
                sql = 'INSERT INTO openlist (date,url,day,repeat) VALUES(?,?,?,?)'
                data = (new,row[1],row[2],row[3]-1)
                cursor.execute(sql,data)
                conn.commit()
                

            print(row)
            sql = 'DELETE FROM openlist WHERE date= ? AND url = ? AND day = ? '
            cursor.execute(sql,(row[0],row[1],row[2]))
            conn.commit()
            # 삭제하고
            return str(row[1])
                        
                

        elif row[2] == 2 : # 월 반복
            if row[3] !=0 :
                old = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M')
                add = dateutil.relativedelta.relativedelta(months=1) #모듈을 사용한 월 계산 (윤년 마지막날 계산 가능)
                new = old + add

                sql = 'INSERT INTO openlist (date,url,day,repeat) VALUES(?,?,?,?)'
                data = (new,row[1],row[2],row[3]-1)
                cursor.execute(sql,data)
                conn.commit()

            print(row)
            sql = 'DELETE FROM openlist WHERE date= ? AND url = ? AND day = ? '
            cursor.execute(sql,(row[0],row[1],row[2]))
            conn.commit()
            # 기존 출력할 것을 삭제하고
            return str(row[1]) # url 반

                
                
        elif row[2] == 3 : # 년 반복
            if row[3] !=0 :
                old = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M')
                add = dateutil.relativedelta.relativedelta(year=1) 
                new = old + add

                sql = 'INSERT INTO openlist (date,url,day,repeat) VALUES(?,?,?,?)'
                data = (new,row[1],row[2],row[3]-1)
                cursor.execute(sql,data)
                conn.commit()

            print(row)
            sql = 'DELETE FROM openlist WHERE date= ? AND url = ? AND day = ? '
            cursor.execute(sql,(row[0],row[1],row[2]))
            conn.commit()
            # 기존 출력할 것을 삭제하고
            return str(row[1]) # url 반

            
        
        

    
    #return url

if __name__ == '__main__' :
    create_DB()
    # test로 값을 5회 입력받아 입력받은값이 제대로 저장되어있는지
    #db의 테이블값을 불러와 확인하기
    print('test 5번 입력\n')
    for i in range(5) :
        print(f'{i+1}번째 입력')
        save_DB()
        print('\n')
    show_DB()
