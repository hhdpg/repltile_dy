import urllib.request
import re
import json
from skimage import io

url = "https://webconf.douyucdn.cn/resource/common/prop_gift_list/prop_gift_config.json"
response = urllib.request.Request(url)
response.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36')
html = urllib.request.urlopen(response, timeout=500).read()
html = bytes.decode(html, encoding='UTF-8')
js = re.search('"data(.*)', html).group()[:-1]
s = "{" + js
json_dict = json.loads(s.replace(")", ""))
print(json_dict)
for s in json_dict["data"]:
    img_src = json_dict['data'][s]['himg']
    image = io.imread(img_src)
    io.imshow(image)
    io.show()
    print(image)
