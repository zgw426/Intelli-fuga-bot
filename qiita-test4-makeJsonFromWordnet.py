import sqlite3
conn = sqlite3.connect("wnjpn.db")

def SearchSimilarWords2(wordid):
    cur = conn.execute("select wordid,lemma from word where wordid='%s'" % wordid)
    for row in cur:
        word_id = row[0]
        word = row[1]

    if word != "":
        cur = conn.execute("select synset from sense where wordid='%s'" % word_id)
        synsets = []
        for row in cur:
            synsets.append(row[0])

        no = 1
        for synset in synsets:
            cur2 = conn.execute("select def from synset_def where (synset='%s' and lang='jpn')" % synset)
            sub_no = 1
            tmpStr = ""
            for row2 in cur2:
                tmpStr += "("+ str(sub_no) + ") " + row2[0] + "";
                sub_no += 1
            outStr = ""
            outStr = "\"" + word + "\"" + "," + "\"" + tmpStr + "\"" + "\n"
        return(outStr)

path_w = 'qiita-dictionalyFromWordnet000.csv'

with open(path_w, mode='w', encoding="utf_8") as f:
    # 全ての wordid を取得
    wdid = conn.execute("select wordid from word")
    debugMax = 9999999
    debugNo  = 0
    f.write("\"test_id\",\"name\"\n")
    for row in wdid:
        if debugNo >= debugMax:
            print("break")
            break
        else:
            debugNo += 1
        word_id = row[0]
        f.write( SearchSimilarWords2(word_id) )