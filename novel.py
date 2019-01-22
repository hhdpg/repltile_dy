import pymysql
db = pymysql.connect('localhost', 'root', 'root', 'big_head', charset = 'utf8')
corsurS = db.cursor()
file = open('C:/usr/test.txt', 'r')
try:
    for lines in file.readlines():
        lines = lines.strip('/n')
        # sql = "UPDATE `novel` SET `txt` = '%s' WHERE `id` = '1'"
        print(lines)
        corsurS.execute("INSERT INTO `noveltest` VALUES ('%s')" % lines)
    db.commit()
    print('存储成功')
except:
    db.rollback()
    print("存储失败")
file.close()
db.close()
