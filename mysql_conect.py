import pymysql
db = pymysql.connect('localhost', 'root', 'root', 'dy')
cursor = db.cursor()
#sql = "INSERT INTO `test` VALUES ('1', 'PGAPGA', '123456', '豆国的苹果') ON DUPLICATE KEY UPDATE `nicname` = 'AAAA'"
# sql = "UPDATE `test` SET `nicname` = '苹果啊苹果啊' WHERE `id` = '1'"
# sql = "INSERT INTO `game_cate` (`cate_id`, `game_name`, `short_name`, `game_url`) VALUES (196, 'erciyuan', '1209', 'erciyuan') ON DUPLICATE KEY UPDATE `cate_id` = 196, `game_name` = 'erciyuan', `short_name` = '1209', `game_url` = 'erciyuan'"
# sql = "SELECT img_name, url_png FROM image WHERE img_id = 1235"
sql = "UPDATE `room_hn` SET `hn` = 0"
try:
    cursor.execute(sql)
    db.commit()
except:
    print('插入失败')
    db.rollback()
db.close()

