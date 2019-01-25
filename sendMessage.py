import requests, time, random
url = 'https://www.douyu.com/lapi/athena/room/barrage?t=1548225225549&roomId=1209&cid=174'
cookie = {'cookie': 'dy_did=fd18a33d558a29adb1a6c22b00021501; sm_did=WC39ZUyXRgdEtogXajguGZNo29M1FLA7byr28VvEuLO%252FBcO1EiJ8YEpIrDT0Qkol2WY25AnSot4QRNhQ%252FO9kB6FKP4pa4eHSn50PsMsektAeDha%252Fjzf4qdHxTAhPA72GQo4sUfxtxrE3rRo7JG2f8p0NI8mX7%252Fmbxgmez5srz5vvLX9aBu0Z5XuZMy%252BGdfjyCjpQOtuy1hKV60It1gOUshHjl26Uiez1TW7fyhQ1rWwo%252F8slNy9spNH0BV8YoNrxx1487577677129; smidV2=20180906212820c0b3f2af56902a5e6966a8fe8dfa030400695f127381c6550; _ga=GA1.2.1607331268.1541250705; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1547619222,1547620227,1547778494,1548222700; _gid=GA1.2.1297169169.1548222708; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1548224198'}

form = {
    'type':'chatmsg',
    'rid':'1209',
    'ct':'1',
    'uid':'22578086',
    'nn':'豆国的苹果',
    'txt':'testtest',
    'cid':'2939cd8d32704c503b1c280000000000',
    'ic':'avanew@Sface@S201712@S23@S19@S416e71e39972d9eab3131ed17406b2a6',
    'level':'29',
}
try:
    requests.post(url, cookies=cookie, data=form)
except:
    print('send fail')
# requests.request('POST',url, data=form,cookies=cookie)