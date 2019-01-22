import urllib.request
import urllib
import re
import json
import os
import pymysql
from concurrent.futures import ThreadPoolExecutor
import time
def game_cate():
    url = 'http://open.douyucdn.cn/api/RoomApi/game'
    header = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
    response = urllib.request.Request(url)
    response.add_header('User-Agent', header)
    html = urllib.request.urlopen(url, timeout=500).read()
    html = bytes.decode(html, encoding='UTF-8')
    js = re.search('"data(.*)', html).group()[:-1]
    s = "{" + js +"}"
    json_dict = json.loads(s)
    #connect mysql database
    db = pymysql.connect('localhost', 'root', 'root', 'dy')
    cursor = db.cursor()
    game_cate_data = []
    for s in json_dict['data']:
        # print(s)
        cate_id = s['cate_id']
        game_name = s['game_name']
        short_name = s['short_name']
        game_url = s['game_url']
        sql = "INSERT INTO `game_cate` (`cate_id`, `game_name`, `short_name`, `game_url`, `room_num`) VALUES ('%s', '%s', '%s', '%s', 0) ON DUPLICATE KEY UPDATE `cate_id` = '%s', `game_name` = '%s', `short_name` = '%s', `game_url` = '%s', `room_num` = 0" % (cate_id, game_name, short_name, game_url, cate_id, game_name, short_name, game_url)
        try:
            cursor.execute(sql)
            db.commit()
            game_cate_data.append(cate_id)
        except:
            print('it is faild to insert into game_cate')
            db.rollback()
    db.close()
    return game_cate_data
def room(game_cate_id):
    room_num = 0
    for i in range(0, 10000, 100):
        url = 'http://open.douyucdn.cn/api/RoomApi/live/' + str(game_cate_id) + '?limit=100&offset=' + str(i)
        header = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
        response = urllib.request.Request(url)
        response.add_header('User-Agent', header)
        html = urllib.request.urlopen(url, timeout=500).read()
        html = bytes.decode(html, encoding='UTF-8')
        js = re.search('"data(.*)', html).group()[:-1]
        s = "{" + js + "}"
        json_dict = json.loads(s)
        if json_dict['data'] == None:
            break
        # connect mysql database
        db = pymysql.connect('localhost', 'root', 'root', 'dy')
        cursor = db.cursor()
        for s in json_dict['data']:
            # print(s)
            game_cate_data = ()
            # print('当前' + s['nickname'] + '的房间' + str(s['room_id']) + '的' + '热度为' + str(s['hn']))
            room_id = s['room_id']
            hn = s['hn']
            nickname = s['nickname']
            room_name = s['room_name']
            url = s['url']
            sql = "INSERT INTO `room_hn` (`room_id`, `nickname`, `room_name`, `hn`, `url`, `game_cate_id`) VALUES('%s', '%s', '%s', '%s', '%s', '%s') ON DUPLICATE KEY UPDATE `room_id` = '%s', `nickname` =  '%s', `room_name` = '%s', `hn` = '%s', `url` = '%s', `game_cate_id` = '%s'" % (
            room_id, nickname, room_name, hn, url, game_cate_id, room_id, nickname, room_name, hn, url, game_cate_id)
            try:
                cursor.execute(sql)
                db.commit()
                room_num += 1
            except:
                print('it is faild to insert to room_hn')
                db.rollback()
    print(str(room_num) + '   ' + str(game_cate_id))
    if room_num == 0:
        pass
    else:
        sql = "UPDATE `game_cate` SET `room_num` = '%s' WHERE `cate_id` = '%s'" % (room_num, game_cate_id)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print('it is faild to update the number of room')
        db.close()
#将每个房间的热度重置为0
def reset_hn():
    db = pymysql.connect('localhost', 'root', 'root', 'dy')
    cursor = db.cursor()
    sql = "UPDATE `room_hn` SET `hn` = 0"
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print('it is faild to update hn')
        db.rollback()
    db.close()
if __name__ == '__main__':
    # while True:
    start = time.clock()
    game_cate()
    reset_hn()
    # use threadPool to improve speed
    # open 20 thread pools
    p = ThreadPoolExecutor(20)
    for game_cate_id in game_cate():
        p.submit(room, game_cate_id)
    p.shutdown()
    print('时间为：')
    print(time.clock() - start)
    # time.sleep(600)