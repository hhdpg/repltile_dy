import urllib.request
import urllib
import re
import json
import pymysql
url = "https://webconf.douyucdn.cn/resource/common/prop_gift_list/prop_gift_config.json"
response = urllib.request.Request(url)
response.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36')
html = urllib.request.urlopen(response, timeout=500).read()
html = bytes.decode(html, encoding='UTF-8')
js = re.search('"data(.*)', html).group()[:-1]
s = "{" + js
json_dict = json.loads(s.replace(")", ""))
print(json_dict)
count = 0
db = pymysql.connect('localhost', 'root', 'root', 'dy')
cursor = db.cursor()
for s in json_dict["data"]:
    img_src_gif = json_dict['data'][s]['himg']
    img_src_png = json_dict['data'][s]['pc_full_icon']
    img_name = json_dict['data'][s]['name']
    png = './image/png/' + img_name + '(' + s + ')' + '.png'
    gif = './image/gif/' + img_name + '(' + s + ')' + '.gif'
    print('aaa'+img_src_png)
    if len(img_src_png) > 3:
        urllib.request.urlretrieve(img_src_png, png)
    else:
        pass
    urllib.request.urlretrieve(img_src_gif, gif)
    try:
        sql = "INSERT INTO `image` VALUES ('%s', '%s', '%s', '%s') ON DUPLICATE KEY UPDATE img_id = '%s', img_name = '%s', url_gif = '%s', url_png = '%s'" % (s, img_name, gif, png, s, img_name, gif, png)
        cursor.execute(sql)
        db.commit()
    except:
        print('it is faild to insert')
        db.rollback()
    count = count + 1
db.close()
print('下载完毕')
print(count)