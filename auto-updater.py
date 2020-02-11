import time,requests,os

print('アップデートを確認中...')
if os.path.isfile("index.py"):
    with open("index.py", encoding='utf-8') as f:
        current = f.read()
else:
    github = requests.get("https://raw.githubusercontent.com/gomashio1596/Fortnite-LobbyBot/master/index.py")
    github.encoding = github.apparent_encoding
    github = github.text.encode(encoding='utf-8')
    with open("index.py", 'bw') as f:
        f.write(github)
    with open("index.py", encoding='utf-8') as f:
        current = f.read()
github = requests.get("https://raw.githubusercontent.com/gomashio1596/Fortnite-LobbyBot/master/index.py")
github.encoding = github.apparent_encoding
github = github.text.encode(encoding='utf-8')
if current.replace('\n','').replace('\r','').encode(encoding='utf-8') != github.decode().replace('\n','').replace('\r','').encode(encoding='utf-8'):
    print('アップデートを確認しました! configファイルなどが変更されている可能性があるので手動でチェックしてください')
    print('古いファイルを削除中...')
    try:
        os.remove("index.py")
    except PermissionError:
        print('index.pyを開いているためファイルを削除できません。閉じてから起動してください')
        exit()
    with open("index.py", 'bw') as f:
        f.write(github)
    print('完了しました!')
else:
    print('更新はありません!')
