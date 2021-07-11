import json
import sys

#db 항목 매칭 
class MatchAttribute():
    def __init__(self): 
        print('Attribute 별 항목 리스트')

    def setAttr(self, attributes):
        print('')
        #딱히 할일이 없네
        #csv파일이면 할일이 있을지도.. 


#json 형식으로 만들기
class convertJsonToDBInsert():
    def __init__(self, attributes, tableName):
        self.attributes = json.loads(attributes)
        self.tableName = tableName

    #json 불러오기 data:[{'':''}]
    def jsonOpen(self, jsonFilePath):
        try:
            with open(jsonFilePath, 'r', encoding='UTF-8') as json_file:
                json_data = json.load(json_file)
                return json_data
        except Exception as e :
            print(e)
    #이부분 람다나 뭐 다른걸로 바꿀 방법 생각
    #key, value = next(iter(d.items()))
    #key, value = next((str(k), str(v)) for k, v in d.items())
    def matchValue(self, json_data):
        attrDicList = []
        for i, data in enumerate(json_data): #이중구조
            for item in json_data[data]: #실제값 1set
                keyList = item.keys()
                attrDic = {} 
                for key in keyList: #값에서 사용하는 key
                    for attr in self.attributes: #db매칭 dictionary
                        if (self.attributes[attr] == key):
                            attrDic[attr] = item.get(key,"매칭불가")
                attrDicList.append(attrDic)
        return attrDicList

    def createInsertStatement(self, attrDicList):
        insertStatements = ''
        for attrDic in attrDicList:
            insertStatement = 'INSERT INTO '+self.tableName + ' (\n'
            for key in attrDic.keys():
                insertStatement += key+', '
            insertStatement = insertStatement[:-2]
            insertStatement += ') \n    value ('
            for attr in attrDic:
                insertStatement += attrDic[attr]+', '
            insertStatement = insertStatement[:-2]
            insertStatement += ');'
            insertStatements += insertStatement + '\n\n'
        return insertStatements
    
    def fileWrite(self, insertStatement, resultFilePath):
        try:
            f = open(resultFilePath+self.tableName+'_insert.txt', 'w')
            f.writelines(insertStatement)
            f.close()
        except Exception as e:
            print(e) 
            f.write(str(e))
            f.close()
        

