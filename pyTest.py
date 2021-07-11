import unittest
import mainJsonToInsertStatement as testfunction 

class TestJTDC(unittest.TestCase):

    def test_matchAttribute(self):
        jsonFilePath = ".json"
        attributes = '{"dbrank": "rank","dbrankInten": "rankInten","dbrankOldAndNew": "rankOldAndNew","dbmovieCd": "movieCd","dbmovieNm": "movieNm","dbopenDt": "openDt","dbsalesAmt": "salesAmt"}'
        tableName = "movies"
        resultFilePath = ""
        result = testfunction.matchAttribute(jsonFilePath=jsonFilePath, attributes=attributes, tableName=tableName, resultFilePath=resultFilePath)


unittest.main()