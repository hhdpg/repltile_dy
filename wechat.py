import itchat
itchat.login()
friends = itchat.get_friends(update=True)[0:]
print(friends)