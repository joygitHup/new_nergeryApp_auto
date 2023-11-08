import itchat
itchat.auto_login()
friend_names = ['Zero']
message = '你们好，这是一条自动发送的消息！'
for friend_name in friend_names:
    friend = itchat.search_friends(nickName=friend_name)[0]
    itchat.send(message, toUserName=friend['UserName'])
