import urllib.request
import urllib
import re
import json
import os
url = "https://webconf.douyucdn.cn/resource/common/fans_medal_web_v2.json"
response = urllib.request.Request(url)
response.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36')
html = urllib.request.urlopen(response, timeout=500).read()
html = bytes.decode(html, encoding='UTF-8')
js = re.search('"data(.*)', html).group()[:-1]
s = "{" + js
json_dict = json.loads(s.replace(")", ""))
print(json_dict)
count = 0
for s in json_dict["data"]:
    print(s['room_id'])
    path = 'C:/usr/fans_medal/'+ str(s['room_id'])
    os.makedirs(path)
    count = 0
    for photo in s['resource']['bg']:
        if photo.endswith('gif'):
            urllib.request.urlretrieve(photo, path + '/'+ str(s['room_id']) + '_' + str(count) + '.gif')
        else:
            urllib.request.urlretrieve(photo, path + '/' + str(s['room_id']) + '_' + str(count) + '.png')
        count +=1
print('下载完毕')