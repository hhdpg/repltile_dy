# -*- coding:utf-8 -*-
import matplotlib
import socket
import re
import time
import struct
import threading
import pymysql
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
from scipy import misc

db = pymysql.connect('localhost', 'root', 'root', 'dy')
cursor = db.cursor()
def connect():
    '''
    第三方客户端通过 TCP 协议连接到弹幕服务器(依据指定的 IP 和端口);
    第三方接入弹幕服务器列表:
    IP 地址:openbarrage.douyutv.com 端口:8601
    '''
    print ('-----*-----DouYu_Spider-----*-----\n')
    host = socket.gethostbyname("openbarrage.douyutv.com")
    port = 8601
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))

def send_msg(msg):
    data_length = len(msg) + 8
    code = 689
    msgHead = struct.pack('<i',data_length) \
          + struct.pack('<i',data_length) + struct.pack('<i',code)
    s.send(msgHead)
    sent = 0
    while sent < len(msg):
        tn = s.send(msg[sent:])
        sent = sent + tn

def danmu(room_id):
    '''
    1.客户端向弹幕服务器发送登录请求
    2.客户端收到登录成功消息后发送进入弹幕分组请求给弹幕服务器
    '''
    login = 'type@=loginreq/roomid@=%s/\0'%room_id
    login = login.encode('utf-8')
    send_msg(login)
    joingroup = 'type@=joingroup/rid@=%s/gid@=-9999/\0'%room_id
    joingroup = joingroup.encode('utf-8')
    send_msg(joingroup)
    while True:
        content = s.recv(2048)
        # print('全部code：'+content.decode('utf-8', 'ignore'))
        con = content.decode('utf-8', 'ignore')
        pattern = re.compile(r'type@=(.*)/rid@')
        data_type = pattern.findall(con)
        try:
            if data_type[0] == 'chatmsg':
                chat_msg(con)
            elif data_type[0] == 'dgb':
                dgb(con)
            else:
                pass
        except:
            pass

def keep_alive():
    '''
    客户端每隔 45 秒发送心跳信息给弹幕服务器
    '''
    while True:
        msg = 'type@=keeplive/tick@=%s/\0'%str(int(time.time()))
        send_msg(msg.encode('utf-8'))
        time.sleep(45)

def chat_msg(content):
    '''
    弹幕消息：
    type@=chatmsg/rid@=301712/gid@=-9999/uid@=123456/nn@=test /txt@=666/level@=1/
    判断type，弹幕消息为chatmsg，txt为弹幕内容，nn为用户昵称,level为用户等级
    '''
    nn_pat = re.compile(r'nn@=(.*)/txt@')
    nick_name = nn_pat.findall(content)[0]

    level_pat = re.compile(r'level@=(.*)/sahf@')
    level = 0
    try:
        level = level_pat.findall(content)[0]
    except:
        print('该用户等级为0')
        pass

    msg_pat = re.compile(r'txt@=(.*)/cid@')
    chatmsg = msg_pat.findall(content)[0]
    print('%s[%s] : %s'%(nick_name, level, chatmsg))

def dgb(content):
    '''
        弹幕消息：
          type@=dgb/rid@=485503/gfid@=824/gs@=1/uid@=15889060/nn@=aaa/ic@=avatar_v3@S201811@Sff3fe2fedc21c4615927c6182a626b7d/eid@=0/level@=9/
          dw@=0/gfcnt@=15/hits@=15/
        判断type，弹幕消息为dgb，gfid为礼物ID，nn为用户昵称,level为用户等级,hits 为礼物个数
        '''
    nn_pat = re.compile(r'nn@=(.*)/ic@')
    nick_name = nn_pat.findall(content)[0]

    level_pat = re.compile(r'level@=(.*)/dw@')
    '''
       有些用户从其他地方观看直播，并发言，但斗鱼对这一部分观众没有记录等级，所level可能返回空
       需要做抛异常处理，并初始化等级为0级
       '''
    level = 0
    try:
        level = level_pat.findall(content)[0]
    except:
        print('该用户等级为0')
        pass

    gfcnt_pat = re.compile(r'gfcnt@=(.*)/hits@')
    gfcnt = gfcnt_pat.findall(content)[0]

    gfid_pat = re.compile(r'gfid@=(.*)/gs@')
    gfid = gfid_pat.findall(content)[0]
    try:
        sql = "SELECT img_name, url_png FROM image WHERE img_id = '%s'" % (gfid)
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    result = cursor.fetchone()
    gift_name = result[0]
    lena = mpimg.imread(result[1])  # 读取和代码处于同一目录下的 lena.png
    # 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
    lena.shape
    # lena_new = misc.imresize(lena, (10, 10, 10))
    plt.imshow(lena)  # 显示图片
    plt.axis('off')  # 不显示坐标轴
    plt1 = plt.figure(figsize=(4, 2))
    # print('%s[%s]赠送礼物%s' % (nick_name, level, gift_name), plt1, '%s连击' % (gfcnt))
    print('%s[%s]赠送礼物%s%s连击' % (nick_name, level, gift_name, gfcnt))
if __name__ == '__main__':
    connect()
    # print('请输入房间ID: ', end='')
    # t1 = threading.Thread(target=danmu,args=(input(),))
    t1 = threading.Thread(target=danmu,args=(99999,))
    t2 = threading.Thread(target=keep_alive)
    t1.start()
    t2.start()