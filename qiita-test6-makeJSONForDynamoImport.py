
# output : qiita-dictionalyFromWardnet004_s.json
# {"name":{"s":"(1) それをする、またはそれであるさま"},"test_id":{"s":"-風"}}
# {"name":{"s":"(1) 全体に対する比率（通常、百分率）"},"test_id":{"s":"%"}}
# {"name":{"s":"(1) それをする、またはそれであるさま"},"test_id":{"s":"-様"}}


import pandas as pd
csvFile = "qiita-dictionalyFromWardnet001_s.csv"
hoge = pd.read_csv(csvFile,
                   parse_dates=[1],  # 対象のカラムインデックス
                   names=['test_id', 'name'],
                   dtype={2: str}  # カラムインデックスと型の dict
                   )

path_w = 'qiita-dictionalyFromWardnet004_s.json'
with open(path_w, mode='w', encoding="utf_8") as f:
    debugMax = 599999999999
    debugNo  = 0
    item00 = ""
    item01 = ""
    tmpStr = ""
    for index,item in hoge.iterrows():
        if debugNo == debugMax:
            break
        else:
            debugNo += 1
        if debugNo == 1:
            item00 = item['test_id']
            item01 = item['name']
        else:
            tmpStr+= "{"
            tmpStr+= "\"" + item01 + "\":{\"s\":\"" + str(item['name']) + "\"}"
            tmpStr+= ","
            tmpStr+= "\"" + item00 + "\":{\"s\":\"" + str(item['test_id']) + "\"}"
            tmpStr+= "}\n"
            f.write( tmpStr )
            tmpStr = ""