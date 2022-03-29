from .database import engine
import pandas as pd
from threading import Thread
import requests


'''#####################################################################################################################
   #########################################                                  ##########################################
   #########################################          TABLE MODELLING         ##########################################
   #########################################                                  ##########################################
   #####################################################################################################################
   '''


def file_modeling():
    # csv 데이터 저장
    tn, df, columns = reload()
    # table 생성
    index = table_modeling(tn=tn, df=df, columns=columns)
    return tn, df, columns, index


# 테이블 작성
def table_modeling(tn="", df=None, columns=None):
    # 테이블 기본 값
    default = 'from .database import Base\nfrom sqlalchemy import Column, Integer, String, Numeric\n\n\n'
    new_table = f'class {tn}(Base):\n\t__tablename__ = "{tn}"\n\n'

    # primary 데이터 가 중복 값이 있다는 경우를 없애기 위해 인덱스 추가
    index = False

    # 각 컬럼에 알맞는 table 컬럼 작성
    for cnt, d in enumerate(columns):
        m = len(str(df[d][0]))
        memory = int(m+(m/2))
        if cnt == 0:
            new_table += f"\tIndex = Column(Integer, primary_key=True, index=True)\n"
            index = True
            new_table += f"\t{d} = Column(String({memory}), unique=False)\n"
        else:
            try:
                memory = int(df[d][0])
                if str(df[d][0]).count('.') >= 1:
                    new_table += f"\t{d} = Column(Numeric, unique=False)\n"
                else:
                    new_table += f"\t{d} = Column(Integer, unique=False)\n"
            except ValueError:
                if d[:7] == "CONVERT":
                    d_ = d[8:]
                    new_table += f"\tCONVERT_{d_[:-12]} = Column(String({memory}), unique=False)\n"
                else:
                    new_table += f"\t{d} = Column(String({memory}), unique=False)\n"

    with open("./app/db/models.py", "w") as model:
        model.write(default + new_table)
        model.close()

    return index


# csv 파일 데이터 로 변환
def reload():
    table_name = next(open("./app/data/filename.txt", "r"))
    df = pd.read_csv(f"./app/data/data.csv", encoding='cp949')
    for i, col in enumerate(df.columns):
        df = df.rename(columns={
            col:
        })
    columns_ = df.columns

    return table_name.lower(), df, columns_


def get_translate(text):
    client_id, client_secret = "LnbkGpZ1FltpJ_Jytof0", "2odQqgaDim" # [ADD] Naver API developer ID

    data = {'text': text,
            'source': 'ko',
            'target': 'en'}


def in_data(tn="", df=None, columns=None, index=None):
    # Thread 최대 4개 병렬 처리 가능
    # ex) 0~1000개의 데이터 -> (0, 250), (250, 500), (500, 750), (750, 1000)
    # 최대 카디널리티 개수 = len(df)
    # 각 최대 카디널리티의 1/4를 하여서 병렬처리
    th1_ = range(0, int(len(df)/4))
    th2_ = range(int(len(df)/4), int(len(df)/4)*2)
    th3_ = range(int(len(df)/4)*2, int(len(df)/4)*3)
    th4_ = range(int(len(df)/4)*3, int(len(df)/4)*4)
    th1 = Thread(target=thread_, args=(th1_, index, columns, df, tn))
    th2 = Thread(target=thread_, args=(th2_, index, columns, df, tn))
    th3 = Thread(target=thread_, args=(th3_, index, columns, df, tn))
    th4 = Thread(target=thread_, args=(th4_, index, columns, df, tn))
    th1.daemon, th2.daemon, th3.daemon, th4.daemon = True, True, True, True
    th1.start(); th2.start(); th3.start(); th4.start()
    th1.join(); th2.join(); th3.join(); th4.join()


# Thread 내용
def thread_(th=None, index=None, columns=None, df=None, tn=""):
    insert = f"INSERT INTO {tn} VALUES"
    conn = engine.connect()
    for v in th:
        dic, index = column_dic(columns=columns, index=index, value=df.values[v], cnt=v)
        ins = (insert + "(" + dic[:-1] + ")")
        print(ins)
        try:
            conn.execute(ins)
        except:
            pass
    conn.close()


# 컬럼 작성
def column_dic(columns=None, index=False, value=None, cnt=0):
    dic = ''
    for x, c in enumerate(columns):
        if x == 0:
            # 앞 column 이 곂칠 때
            if not index == False:
                dic += f'{cnt},'
        try:
            test = int(value[x])
            dic += f'{value[x]},'
        except ValueError:
            dic += f"'{value[x]}',"

    return dic, index
