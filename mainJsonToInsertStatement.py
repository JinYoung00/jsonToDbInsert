import jsonToInsertStatement as jtis

#input : jsonFilePath="", attributes={'dbArrt':'jsonArrt'}, tableName=""
#다건일 경우 tuple 로 받게처리 *rest

def matchAttribute(**kwargs):
    #attr = MatchAttribute()
    #attr.setAttr(kwargs.attributes)

    print(kwargs)

    cJtis = jtis.convertJsonToDBInsert(kwargs['attributes'], kwargs['tableName'])
    json_data = cJtis.jsonOpen(kwargs['jsonFilePath'])
    attrDicList = cJtis.matchValue(json_data)

    insertStatement = cJtis.createInsertStatement(attrDicList)
    print(insertStatement)
    cJtis.fileWrite(insertStatement, kwargs['resultFilePath'])
    #디비에 입력할지 묻기 (파일 분리)