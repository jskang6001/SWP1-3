dbfilename = 'test3_2.dat'

def readScoreDB(): #DB파일 읽기
    try: #파일이 존재하지않을 경우를 예외처리
        fH = open(dbfilename)
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []
    else:
        print("Open DB: ", dbfilename)

    scdb = [] #리스트 생성
    for line in fH: #파일 내용을 한줄씩 line으로 접근
        dat = line.strip() #양끝 공백 제거
        person = dat.split(",") #split함수는 구분자를 기준으로 잘라서 리스트의 한 요소로 만듬. 구분자는 소멸. "," 마다 잘라서 리스트의 요소 하나로 저장
        record = {} #사전 생성
        for attr in person: #리스트의 요소를 하나씩 attr로 받음
            kv = attr.split(":") # :를 기준으로 분리해서 리스트의 요소로 저장
            record[kv[0]] = kv[1] #key에 Age, Name, Score를 넣고 value에 그에 해당하는 값을 대입
        scdb += [record] #scdb 리스트에 사전 형태로 person의 정보들을 저장
    fH.close() #파일 닫기
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'w')
    for p in scdb:
        pinfo = []
        for attr in p:
            pinfo += [attr + ":" + p[attr]]
        line = ','.join(pinfo)
        fH.write(line + '\n')
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
            scdb += [record]
        elif parse[0] == 'del':
            for p in scdb:
                if p['Name'] == parse[1]:
                    scdb.remove(p)
                    break
        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)



