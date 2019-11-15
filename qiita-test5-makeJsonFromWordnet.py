import pandas as pd
csvFile = "qiita-dictionalyFromWordnet000.csv"
hoge = pd.read_csv(csvFile,
                   parse_dates=[1],  # 対象のカラムインデックス
                   names=['test_id', 'name'],
                   dtype={2: str}  # カラムインデックスと型の dict
                   )
# 重複を削除するために先にソート
sorted_hoge = hoge.sort_values(['test_id', 'name'],  # カラム名
                               ascending=[1, 0])  # desc か asc か

# 重複削除
no_duplicated_hoge = sorted_hoge.drop_duplicates('test_id',  # このカラムで重複していると、
                                                 keep='first')  # 最初を残すようにする

# csv 出力
no_duplicated_hoge.to_csv("qiita-dictionalyFromWordnet001_s.csv", index=False,columns=['test_id','name'])