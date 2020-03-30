# -*- coding: utf-8 -*-
try:
    from crayons import cyan, green, magenta, red, yellow
    from fortnitepy import ClientPartyMember
    from functools import partial
    from threading import Thread
    from threading import Timer
    from flask import Flask
    import fortnitepy.errors
    import unicodedata
    import fortnitepy
    import threading
    import traceback
    import datetime
    import requests
    import aiohttp
    import asyncio
    import logging
    import jaconv
    import random
    import json
    import time
    import sys
    import os
except ModuleNotFoundError as e:
    try:
        import traceback
        print(f'{traceback.format_exc()}')
    except ModuleNotFoundError:
        pass
    try:
        import sys
        print(f'Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}\n')
    except ModuleNotFoundError:
        pass
    print(e)
    print('モジュールの読み込みに失敗しました。INSTALL.bat を実行してください。問題が修正されない場合はこちらまで連絡をください\nTwitter @gomashioepic\nDiscord gomashio#4335')
    exit()

if os.getcwd().startswith('/app'):
    app=Flask(__name__)
    @app.route("/")
    def index():
        return "<h1>Bot is running</h1>"
    Thread(target=app.run,args=("0.0.0.0",8080)).start()

storedlog=[]
kill=False

def dstore(username, content):
    global storedlog
    content=str(content)
    if data['hide-email'] is True:
        for email in data['fortnite']['email'].split(','):
            content=content.replace(email,len(email)*"X")
    if data['hide-password'] is True:
        for password in data['fortnite']['password'].split(','):
            content=content.replace(password,len(password)*"X")
    if data['hide-webhook'] is True:
        for webhook in data['webhook'].split(','):
            content=content.replace(webhook,len(webhook)*"X")
    if data['hide-api-key'] is True:
        for apikey in data['api-key'].split(','):
            content=content.replace(apikey,len(apikey)*"X")
    if data['discord-log'] is True:
        if len(storedlog) > 0:
            if list(storedlog[len(storedlog)-1].keys())[0] == username:
                if len(list(storedlog[len(storedlog)-1].values())[0]) + len(content) > 2000:
                    storedlog.append({username: content})
                else:
                    storedlog[len(storedlog)-1][username]+=f'\n{content}'
            else:
                storedlog.append({username: content})
        else:
            storedlog.append({username: content})

def dprint():
    global storedlog
    global kill
    while True:
        if kill is True:
            exit()
        if data['discord-log'] is True:
            if len(storedlog) != 0:
                for send in storedlog:
                    username=list(send.keys())[0]
                    content=list(send.values())[0]
                    if len(content) > 2000:
                        text=[content[i: i+2000] for i in range(0, len(content), 2000)]
                        for text_ in text:
                            r=requests.post(
                            data['webhook'],
                            json={
                                'username': username,
                                'content': text_
                            }
                        )
                    else:
                        r=requests.post(
                            data['webhook'],
                            json={
                                'username': username,
                                'content': content
                            }
                        )
                    if data['loglevel'] == 'debug':
                        print(yellow(f'[{r.status_code}] {username}: {content}'))
                    if r.status_code == 204:
                        storedlog.remove(send)
                    if r.status_code == 429:
                        break
            time.sleep(5)

def get_device_auth_details():
    if os.path.isfile(filename):
        with open(filename, 'r') as fp:
            return json.load(fp)
    return {}

def store_device_auth_details(email, details):
    existing = get_device_auth_details()
    existing[email] = details
    with open(filename, 'w') as fp:
        json.dump(existing, fp)

def now_():
    return datetime.datetime.now().strftime('%H:%M:%S')

def platform_to_str(platform):
    if platform is fortnitepy.Platform.WINDOWS:
        return 'Windows'
    elif platform is fortnitepy.Platform.MAC:
        return 'Mac'
    elif platform is fortnitepy.Platform.PLAYSTATION:
        return 'PlayStation'
    elif platform is fortnitepy.Platform.XBOX:
        return 'Xbox'
    elif platform is fortnitepy.Platform.SWITCH:
        return 'Switch'
    elif platform is fortnitepy.Platform.IOS:
        return 'IOS'
    elif platform is fortnitepy.Platform.ANDROID:
        return 'Android'
    else:
        return None

def inviteaccept(client):
    if data['no-logs'] is False:
        print(f'[{now_()}] [{client.user.display_name}] 招待を承諾に設定')
    dstore(client.user.display_name, '招待を承諾に設定')
    client.acceptinvite=True

def inviteinterval(client):
    if data['no-logs'] is False:
        print(f'[{now_()}] [{client.user.display_name}] 招待の受付を再開します')
    dstore(client.user.display_name, '招待の受付を再開します')
    client.acceptinvite_interval=True

def reload_configs(client):
    global data
    global commands
    try:
        try:
            with open('config.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.decoder.JSONDecodeError:
            with open('config.json', 'r', encoding='utf-8-sig') as f:
                data = json.load(f)
        if data['loglevel'] == 'debug':
            print(yellow(f'\n{data}\n'))
            dstore('ボット',f'\n{data}\n')
        keys=["['fortnite']","['fortnite']['email']","['fortnite']['password']","['fortnite']['owner']","['fortnite']['platform']","['fortnite']['cid']","['fortnite']['bid']","['fortnite']['pickaxe_id']","['fortnite']['eid']","['fortnite']['playlist']","['fortnite']['banner']","['fortnite']['banner_color']","['fortnite']['level']","['fortnite']['tier']","['fortnite']['xpboost']","['fortnite']['friendxpboost']","['fortnite']['status']","['fortnite']['privacy']","['fortnite']['partychat']","['fortnite']['joinmessage']","['fortnite']['randommessage']","['fortnite']['joinmessageenable']","['fortnite']['randommessageenable']","['fortnite']['skinmimic']","['fortnite']['emotemimic']","['fortnite']['acceptinvite']","['fortnite']['acceptfriend']","['fortnite']['addfriend']","['fortnite']['inviteinterval']","['fortnite']['interval']","['fortnite']['waitinterval']","['no-logs']","['ingame-error']","['discord-log']","['hide-email']","['hide-password']","['hide-webhook']","['hide-api-key']","['webhook']","['caseinsensitive']","['api-key']","['loglevel']","['debug']"]
        for key in keys:
            exec(f"errorcheck=data{key}")
        try:
            errorcheck=requests.get('https://fortnite-api.com/cosmetics/br/search?name=API-KEY-CHECK',headers={'x-api-key': data['api-key']}).json()
        except UnicodeEncodeError:
            if os.path.isfile('allen.json') is False or os.path.isfile('allja.json') is False:
                print(red('APIキーが無効です。正しい値を入力してください。'))
                dstore('ボット',f'>>> APIキーが無効です。正しい値を入力してください')
                return None
            else:
                print(red('APIキーが無効です。最新のアイテムデータをダウンロードできませんでした。正しい値を入力してください。'))
                dstore('ボット',f'>>> APIキーが無効です。最新のアイテムデータをダウンロードできませんでした。正しい値を入力してください')
        if errorcheck['status'] == 401:
            if os.path.isfile('allen.json') is False or os.path.isfile('allja.json') is False:
                print(red('APIキーが無効です。正しい値を入力してください。'))
                dstore('ボット',f'>>> APIキーが無効です。正しい値を入力してください')
                return None
            else:
                print(red('APIキーが無効です。最新のアイテムデータをダウンロードできませんでした。正しい値を入力してください。'))
                dstore('ボット',f'>>> APIキーが無効です。最新のアイテムデータをダウンロードできませんでした。正しい値を入力してください')
        if errorcheck['status'] == 503:
            if os.path.isfile('allen.json') is False or os.path.isfile('allja.json') is False:
                print(red('APIがダウンしているため、アイテムデータをダウンロードできませんでした。しばらく待ってからもう一度起動してみてください。'))
                dstore('ボット',f'>>> APIがダウンしているため、アイテムデータをダウンロードできませんでした。しばらく待ってからもう一度起動してみてください')
                return None
            else:
                print(red('APIがダウンしているため、最新のアイテムデータをダウンロードできませんでした。'))
                dstore('ボット',f'>>> APIがダウンしているため、最新のアイテムデータをダウンロードできませんでした。')
    except KeyError as e:
        print(red(traceback.format_exc()))
        print(red('config.json ファイルの読み込みに失敗しました。キーの名前が間違っていないか確認してください。'))
        print(red(f'{str(e)} がありません。'))
        dstore('ボット',f'>>> {traceback.format_exc()}')
        dstore('ボット',f'>>> config.json ファイルの読み込みに失敗しました。キーの名前が間違っていないか確認してください')
        dstore('ボット',f'>>> {str(e)} がありません')
        return None
    except json.decoder.JSONDecodeError as e:
        print(red(traceback.format_exc()))
        print(red('config.json ファイルの読み込みに失敗しました。正しく書き込めているか確認してください。'))
        print(red(str(e).replace('Expecting ','不明な',1).replace('Invalid control character at','無効なコントロール文字: ').replace('value','値',1).replace('delimiter','区切り文字',1).replace('line','行:',1).replace('column','文字:').replace('char ','',1)))
        dstore('ボット',f'>>> {traceback.format_exc()}')
        dstore('ボット',f'>>> config.json ファイルの読み込みに失敗しました。正しく書き込めているか確認してください')
        dstore('ボット',f'>>> {str(e).replace("Expecting ","不明な",1).replace("Invalid control character at","無効なコントロール文字: ").replace("value","値",1).replace("delimiter","区切り文字",1).replace("line","行:",1).replace("column","文字:").replace("char ","",1)}')
        return None
    except FileNotFoundError:
        print(red(traceback.format_exc()))
        print(red('config.json ファイルが存在しません。'))
        dstore('ボット',f'>>> {traceback.format_exc()}')
        dstore('ボット',f'>>> config.json ファイルが存在しません')
        return None
    threading.Thread(target=get_item_info,args=()).start()
    if data['loglevel'] not in ('normal', 'info', 'debug'):
        data['loglevel']='normal'
    if data['fortnite']['privacy'] not in ('public', 'friends_allow_friends_of_friends', 'friends', 'private_allow_friends_of_friends', 'private'):
        data['fortnite']['privacy']='public'
    data['fortnite']['privacy']=eval(f"fortnitepy.PartyPrivacy.{data['fortnite']['privacy'].upper()}")
    client.joinmessageenable=data['fortnite']['joinmessageenable']
    client.randommessageenable=data['fortnite']['randommessageenable']
    client.skinmimic=data['fortnite']['skinmimic']
    client.emotemimic=data['fortnite']['emotemimic']
    client.acceptinvite=data['fortnite']['acceptinvite']
    client.acceptfriend=data['fortnite']['acceptfriend']

    try:
        try:
            with open('commands.json', 'r', encoding='utf-8') as f:
                commands=json.load(f)
        except json.decoder.JSONDecodeError:
            with open('commands.json', 'r', encoding='utf-8-sig') as f:
                commands=json.load(f)
        keys=["['true']","['false']","['me']","['prev']", "['eval']", "['exec']","['restart']","['relogin']","['reload']","['get']","['friendcount']","['pendingcount']","['blockcount']","['skinmimic']","['emotemimic']","['partychat']","['acceptinvite']","['acceptfriend']","['joinmessageenable']","['randommessageenable']","['wait']","['join']","['joinid']","['leave']","['invite']","['message']","['partymessage']","['status']","['banner']","['level']","['bp']","['privacy']","['privacy_public']","['privacy_friends_allow_friends_of_friends']","['privacy_friends']","['privacy_private_allow_friends_of_friends']","['privacy_private']","['getuser']","['getfriend']","['getpending']","['getblock']","['info']","['info_party']","['info_item']","['pending']","['removepending']","['addfriend']","['removefriend']","['acceptpending']","['declinepending']","['blockfriend']","['unblockfriend']","['chatban']","['promote']","['kick']","['ready']","['unready']","['sitout']","['skinlock']","['baglock']","['picklock']","['emotelock']","['stop']","['allskin']","['allemote']","['setstyle']","['addstyle']","['setenlightenment']","['addvariant']","['skinasset']","['bagasset']","['pickasset']","['emoteasset']"]
        for key in keys:
            exec(f"errorcheck=commands{key}")
        if data['caseinsensitive'] is True:
            commands=dict((k.lower(), jaconv.kata2hira(v.lower())) for k,v in commands.items())
        for checks in commands.items():
            ignore=['ownercommands','true','false','me']
            if checks[0] in ignore:
                continue
            if commands['ownercommands'] == '':
                break
            for command in commands['ownercommands'].split(','):
                try:
                    errorcheck=commands[command.lower()]
                except KeyError as e:
                    print(red(traceback.format_exc()))
                    print(red('所有者コマンドの設定に失敗しました。キーの名前が間違っていないか確認してください。'))
                    print(red(f'{str(e)} がありません。'))
                    dstore('ボット',f'>>> {traceback.format_exc()}')
                    dstore('ボット',f'>>> 所有者コマンドの設定に失敗しました。キーの名前が間違っていないか確認してください')
                    dstore('ボット',f'>>> {str(e)} がありません')
                    return None
        if data['loglevel'] == 'debug':
            print(yellow(f'\n{commands}\n'))
            dstore('ボット',f'\n{commands}\n')
    except KeyError as e:
        print(red(traceback.format_exc()))
        print(red('commands.json ファイルの読み込みに失敗しました。キーの名前が間違っていないか確認してください。'))
        print(red(f'{str(e)} がありません。'))
        dstore('ボット',f'>>> {traceback.format_exc()}')
        dstore('ボット',f'>>> commands.json ファイルの読み込みに失敗しました。キーの名前が間違っていないか確認してください')
        dstore('ボット',f'>>> {str(e)} がありません')
        return None
    except json.decoder.JSONDecodeError as e:
        print(red(traceback.format_exc()))
        print(red('commands.json ファイルの読み込みに失敗しました。正しく書き込めているか確認してください。'))
        print(red(str(e).replace('Expecting ','不明な',1).replace('Invalid control character at','無効なコントロール文字: ').replace('value','値',1).replace('delimiter','区切り文字',1).replace('line','行:',1).replace('column','文字:').replace('char ','',1)))
        dstore('ボット',f'>>> {traceback.format_exc()}')
        dstore('ボット',f'>>> commands.json ファイルの読み込みに失敗しました。正しく書き込めているか確認してください')
        dstore('ボット',f'>>> {str(e).replace("Expecting ","不明な",1).replace("Invalid control character at","無効なコントロール文字: ").replace("value","値",1).replace("delimiter","区切り文字",1).replace("line","行:",1).replace("column","文字:").replace("char ","",1)}')
        return None
    except FileNotFoundError:
        print(red(traceback.format_exc()))
        print(red('commands.json ファイルが存在しません。'))
        dstore('ボット',f'>>> {traceback.format_exc()}')
        dstore('ボット',f'>>> commands.json ファイルが存在しません')
        return None

    try:
        try:
            with open('replies.json', 'r', encoding='utf-8') as f:
                replies=json.load(f)
        except json.decoder.JSONDecodeError:
            with open('replies.json', 'r', encoding='utf-8-sig') as f:
                replies=json.load(f)
        if data['loglevel'] == 'debug':
            print(yellow(f'\n{replies}\n'))
            dstore('ボット',f'\n```\n{replies}\n```\n')
        if data['caseinsensitive'] is True:
            replies=dict((jaconv.kata2hira(k.lower()), v) for k,v in replies.items())
    except json.decoder.JSONDecodeError as e:
        print(red(traceback.format_exc()))
        print(red('replies.json ファイルの読み込みに失敗しました。正しく書き込めているか確認してください。'))
        print(red(str(e).replace('Expecting ','不明な',1).replace('Invalid control character at','無効なコントロール文字: ').replace('value','値',1).replace('delimiter','区切り文字',1).replace('line','行:',1).replace('column','文字:').replace('char ','',1)))
        dstore('ボット',f'>>> {traceback.format_exc()}')
        dstore('ボット',f'>>> replies.json ファイルの読み込みに失敗しました。正しく書き込めているか確認してください')
        dstore('ボット',f'>>> {str(e).replace("Expecting ","不明な",1).replace("Invalid control character at","無効なコントロール文字: ").replace("value","値",1).replace("delimiter","区切り文字",1).replace("line","行:",1).replace("column","文字:").replace("char ","",1)}')
        return None
    except FileNotFoundError:
        print(red(traceback.format_exc()))
        print(red('replies.json ファイルが存在しません。'))
        dstore('ボット',f'>>> {traceback.format_exc()}')
        dstore('ボット',f'>>> replies.json ファイルが存在しません')
        return None

    return 'Success'

def get_item_info():
    global headers
    try:
        headers={'x-api-key': data['api-key']}
        req=requests.get('https://fortnite-api.com/cosmetics/br?language=en', headers=headers)
        if data['loglevel'] == 'debug':
            print(yellow(f'\n[{req.status_code}] {req.url}\n{req.text[:100]}'))
            dstore('ボット',f'```\n[{req.status_code}] {req.url}\n{req.text[:100]}\n```')
        allcosmen=req.json()
        if req.status_code == 200:
            with open('allen.json', 'w') as f:
                json.dump(allcosmen, f)
        req=requests.get('https://fortnite-api.com/cosmetics/br?language=ja', headers=headers)
        if data['loglevel'] == 'debug':
            print(yellow(f'[{req.status_code}] {req.url}\n{req.text[:100]}'))
            dstore('ボット',f'```\n[{req.status_code}] {req.url}\n{req.text[:100]}\n```')
        allcosmja=req.json()
        if req.status_code == 200:
            with open('allja.json', 'w') as f:
                json.dump(allcosmja, f)
    except Exception:
        print(red(traceback.format_exc()))

async def is_itemname(lang, itemname):
    ignoretype=[
        "banner",
        "contrail",
        "glider",
        "wrap",
        "loadingscreen",
        "music",
        "spray"
    ]
    itemlist=[]
    TF='False'
    if lang == 'en':
        with open('allen.json', 'r', encoding='utf-8') as f:
            alldata = json.load(f)
    if lang == 'ja':
        with open('allja.json', 'r', encoding='utf-8') as f:
            alldata = json.load(f)
    try:
        for item in alldata['data']:
            if item['type'] in ignoretype:
                continue
            if data['caseinsensitive'] is True:
                itemname=jaconv.hira2kata(itemname.lower())
                itemname_=jaconv.hira2kata(item['name'].lower())
            else:
                itemname_=item['name']
            if itemname in itemname_:
                itemlist.append([item['id'],item['name'],item['type'],item['description'],item['displayRarity']])
                TF='True'
        if data['loglevel'] == 'debug':
            print(yellow(f'{lang}: {itemname}\n{TF} {itemlist}'))
            dstore('ボット',f'```\n{lang}: {itemname}\n{TF} {itemlist}\n```')
        return TF, itemlist
    except Exception:
        print(red(traceback.format_exc()))
        dstore('ボット',f'>>> {traceback.format_exc()}')
        return TF

async def search_item_with_type(lang, itemname, itemtype):
    ignoretype=[
        "banner",
        "contrail",
        "glider",
        "wrap",
        "loadingscreen",
        "music",
        "spray"
    ]
    itemlist=[]
    TF='False'
    if lang == 'en':
        with open('allen.json', 'r', encoding='utf-8') as f:
            alldata = json.load(f)
    if lang == 'ja':
        with open('allja.json', 'r', encoding='utf-8') as f:
            alldata = json.load(f)
    try:
        for item in alldata['data']:
            if item['type'] in ignoretype:
                continue
            if item['type'] in itemtype.split(','):
                if data['caseinsensitive'] is True:
                    itemname=jaconv.hira2kata(itemname.lower())
                    itemname_=jaconv.hira2kata(item['name'].lower())
                else:
                    itemname_=item['name']
                if itemname in itemname_:
                    itemlist.append([item['id'],item['name'],item['type'],item['description'],item['displayRarity']])
                    TF='True'
        if data['loglevel'] == 'debug':
            print(yellow(f'{TF} {lang}: {itemtype} {itemname}\n{TF} {itemlist}'))
            dstore('ボット',f'```\n{lang}: {itemtype} {itemname}\n{TF} {itemlist}\n```')
        return TF, itemlist
    except Exception:
        print(red(traceback.format_exc()))
        dstore('ボット',f'>>> {traceback.format_exc()}')
        return TF

async def search_set_item(lang, setname):
    ignoretype=[
        "banner",
        "contrail",
        "glider",
        "wrap",
        "loadingscreen",
        "music",
        "spray"
    ]
    itemlist=[]
    TF='False'
    if lang == 'en':
        with open('allen.json', 'r', encoding='utf-8') as f:
            alldata = json.load(f)
    if lang == 'ja':
        with open('allja.json', 'r', encoding='utf-8') as f:
            alldata = json.load(f)
    try:
        for item in alldata['data']:
            if item['type'] in ignoretype:
                continue
            if not item['set'] is None:
                if data['caseinsensitive'] is True:
                    setname=jaconv.hira2kata(setname.lower())
                    setname_=jaconv.hira2kata(item['set'].lower())
                else:
                    setname_=item['set']
                if setname in setname_:
                    itemlist.append([item['id'],item['name'],item['type'],item['description'],item['displayRarity']])
                    TF='True'
        if data['loglevel'] == 'debug':
            print(yellow(f'{TF} {lang}: {setname}\n{TF} {itemlist}'))
            dstore('ボット',f'```\n{lang}: {setname,e}\n{TF} {itemlist}\n```')
        return TF, itemlist
    except Exception:
        print(red(traceback.format_exc()))
        dstore('ボット',f'>>> {traceback.format_exc()}')
        return TF

async def search_item_with_id(lang, itemid):
    ignoretype=[
        "banner",
        "contrail",
        "glider",
        "wrap",
        "loadingscreen",
        "music",
        "spray"
    ]
    itemlist=[]
    TF='False'
    if lang == 'en':
        with open('allen.json', 'r', encoding='utf-8') as f:
            alldata = json.load(f)
    if lang == 'ja':
        with open('allja.json', 'r', encoding='utf-8') as f:
            alldata = json.load(f)
    try:
        for item in alldata['data']:
            if item['type'] in ignoretype:
                continue
            if itemid.lower() in item['id']:
                itemlist.append([item['id'],item['name'],item['type'],item['description'],item['displayRarity']])
                TF='True'
        if data['loglevel'] == 'debug':
            print(yellow(f'{TF} {lang}: {itemid}\n{TF} {itemlist}'))
            dstore('ボット',f'```\n{lang}: {itemid}\n{TF} {itemlist}\n```')
        return TF, itemlist
    except Exception:
        print(red(traceback.format_exc()))
        dstore('ボット',f'>>> {traceback.format_exc()}')
        return TF

async def search_style(lang, stylename, itemid):
    ignoretype=[
        "banner",
        "contrail",
        "glider",
        "wrap",
        "loadingscreen",
        "music",
        "spray"
    ]
    if lang == 'en':
        with open('allen.json', 'r', encoding='utf-8') as f:
            alldata = json.load(f)
    if lang == 'ja':
        with open('allja.json', 'r', encoding='utf-8') as f:
            alldata = json.load(f)
    try:
        for item in alldata['data']:
            if item['type'] in ignoretype:
                continue
            itemid=jaconv.hira2kata(itemid.lower())
            itemid_=jaconv.hira2kata(item['id'].lower())
            if itemid in itemid_:
                if not item['variants'] is None:
                    variants=[]
                    for variant in item['variants']:
                        for option in variant['options']:
                            if data['caseinsensitive'] is True:
                                stylename=jaconv.hira2kata(stylename.lower())
                                stylename_=jaconv.hira2kata(option['name'].lower())
                            else:
                                stylename_=option['name']
                            if stylename in stylename_:
                                variants.append({'item': item['backendType'], 'channel': variant['channel'], 'variant': option['tag']})
                else:
                    return None
        if data['loglevel'] == 'debug':
            print(yellow(f'{itemid}: {stylename} {variants}'))
            dstore('ボット',f'```\n{itemid}: {stylename} {variants}\n```')
        if variants == []:
            return None
        else:
            return variants
    except Exception:
        print(red(traceback.format_exc()))
        dstore('ボット',f'>>> {traceback.format_exc()}')
        return None

async def invitation_accept(invitation):
    client=invitation.client
    try:
        await invitation.accept()
        if not client.owner is None:
            if invitation.sender.id == client.owner.id:
                client.acceptinvite_interval=False
                try:
                    client.timer.cancel()
                except Exception:
                    pass
                client.timer=Timer(data['fortnite']['interval'], inviteinterval, [client])
                client.timer.start()
                if data['loglevel'] == 'normal':
                    if data['no-logs'] is False:
                        print(f'[{now_()}] [{client.user.display_name}] {str(invitation.sender.display_name)} からの招待を承諾')
                    dstore(client.user.display_name, f"{str(invitation.sender.display_name)} からの招待を承諾")
                else:
                    if data['no-logs'] is False:
                        print(f'[{now_()}] [{client.user.display_name}] {str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待を承諾')
                    dstore(client.user.display_name, f"{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待を承諾")
        else:
            client.acceptinvite_interval=False
            try:
                client.timer.cancel()
            except Exception:
                pass
            client.timer=Timer(data['fortnite']['interval'], inviteinterval, [client])
            client.timer.start()
            if data['loglevel'] == 'normal':
                if data['no-logs'] is False:
                    print(f'[{now_()}] [{client.user.display_name}] {str(invitation.sender.display_name)} からの招待を承諾')
                    dstore(client.user.display_name, f"{str(invitation.sender.display_name)} からの招待を承諾")
            else:
                if data['no-logs'] is False:
                    print(f'[{now_()}] [{client.user.display_name}] {str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待を承諾')
                    dstore(client.user.display_name, f"{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待を承諾")
    except KeyError:
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    except fortnitepy.PartyError:
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] 既にパーティーのメンバーです。'))
        dstore(client.user.display_name,f'>>> 既にパーティーのメンバーです')
    except fortnitepy.HTTPException:
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] メンバーが見つかりません。'))
        dstore(client.user.display_name,f'>>> メンバーが見つかりません')
    except fortnitepy.Forbidden:
        if data['ingame-error'] is True:
            await invitation.sender.reply('以前に参加したプライベートパーティーに参加しようとしています。(Epicサービス側のバグです)')
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] 以前に参加したプライベートパーティーに参加しようとしています。(Epicサービス側のバグです)'))
        dstore(client.user.display_name,f'>>> 以前に参加したプライベートパーティーに参加しようとしています。(Epicサービス側のバグです)')
    except fortnitepy.HTTPException:
        if data['ingame-error'] is True:
            await invitation.sender.reply('パーティー招待の承諾リクエストを処理中にエラーが発生しました')
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] パーティー招待の承諾リクエストを処理中にエラーが発生しました。'))
        dstore(client.user.display_name,f'>>> パーティー招待の承諾リクエストを処理中にエラーが発生しました')
    except Exception:
        if data['ingame-error'] is True:
            await invitation.sender.send('エラー')
        print(red(traceback.format_exc()))
        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

async def invitation_decline(invitation):
    client=invitation.client
    try:
        await invitation.decline()
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(f'[{now_()}] [{client.user.display_name}] {str(invitation.sender.display_name)} からの招待を拒否')
            dstore(client.user.display_name,f'{str(invitation.sender.display_name)} からの招待を拒否')
        else:
            if data['no-logs'] is False:
                print(f'[{now_()}] [{client.user.display_name}] {str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待を拒否')
            dstore(client.user.display_name,f'{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待を拒否')
    except fortnitepy.PartyError:
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] 受信したnet_clとクライアントのnet_clが一致しません。'))
        dstore(client.user.display_name,f'>>> 受信したnet_clとクライアントのnet_clが一致しません')
    except fortnitepy.HTTPException:
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] パーティー招待の拒否リクエストを処理中にエラーが発生しました。'))
        dstore(client.user.display_name,f'>>> パーティー招待の拒否リクエストを処理中にエラーが発生しました')
    except Exception:
        if data['ingame-error'] is True:
            await invitation.sender.send('エラー')
        print(red(traceback.format_exc()))
        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

async def invitation_decline_interval(invitation):
    client=invitation.client
    try:
        await invitation.decline()
        await invitation.sender.send(f"招待を承諾してから{str(data['fortnite']['interval'])}秒間は招待を拒否します")
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(f"[{now_()}] [{client.user.display_name}] {str(invitation.sender.display_name)} からの招待を{str(data['fortnite']['interval'])}秒拒否")
            dstore(client.user.display_name,f'{str(invitation.sender.display_name)} からの招待を{str(data["fortnite"]["interval"])}秒拒否')
        else:
            if data['no-logs'] is False:
                print(f"[{now_()}] [{client.user.display_name}] {str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待を{str(data['fortnite']['interval'])}秒拒否")
            dstore(client.user.display_name,f'{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待を{str(data["fortnite"]["interval"])}秒拒否')
    except fortnitepy.PartyError:
        if data['ingame-error'] is True:
            await invitation.sender.send('受信したnet_clとクライアントのnet_clが一致しません')
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] 受信したnet_clとクライアントのnet_clが一致しません。'))
        dstore(client.user.display_name,f'>>> 受信したnet_clとクライアントのnet_clが一致しません')
    except fortnitepy.HTTPException:
        if data['ingame-error'] is True:
            await invitation.sender.send('パーティー招待の拒否リクエストを処理中にエラーが発生しました')
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] パーティー招待の拒否リクエストを処理中にエラーが発生しました。'))
        dstore(client.user.display_name,f'>>> パーティー招待の拒否リクエストを処理中にエラーが発生しました')
    except Exception:
        if data['ingame-error'] is True:
            await invitation.sender.send('エラー')
        print(red(traceback.format_exc()))
        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

async def invitation_decline_owner(invitation):
    try:
        await invitation.decline()
        await invitation.sender.send('所有者がパーティーにいるため招待を拒否します')
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(f"[{now_()}] [{client.user.display_name}] {str(invitation.sender.display_name)} からの招待を{str(data['fortnite']['interval'])}秒拒否")
            dstore(client.user.display_name,f'{str(invitation.sender.display_name)} からの招待を{str(data["fortnite"]["interval"])}秒拒否')
        else:
            if data['no-logs'] is False:
                print(f"[{now_()}] [{client.user.display_name}] {str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待を{str(data['fortnite']['interval'])}秒拒否")
            dstore(client.user.display_name,f'{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待を{str(data["fortnite"]["interval"])}秒拒否')
    except fortnitepy.PartyError:
        if data['ingame-error'] is True:
            await invitation.sender.send('受信したnet_clとクライアントのnet_clが一致しません')
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] 受信したnet_clとクライアントのnet_clが一致しません。'))
        dstore(client.user.display_name,f'>>> 受信したnet_clとクライアントのnet_clが一致しません')
    except fortnitepy.HTTPException:
        if data['ingame-error'] is True:
            await invitation.sender.send('パーティー招待の拒否リクエストを処理中にエラーが発生しました')
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] パーティー招待の拒否リクエストを処理中にエラーが発生しました。'))
        dstore(client.user.display_name,f'>>> パーティー招待の拒否リクエストを処理中にエラーが発生しました')
    except Exception:
        if data['ingame-error'] is True:
            await invitation.sender.send('エラー')
        print(red(traceback.format_exc()))
        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

try:
    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.decoder.JSONDecodeError:
        with open('config.json', 'r', encoding='utf-8-sig') as f:
            data = json.load(f)
    if data['loglevel'] == 'debug':
        print(yellow(f'\n{data}\n'))
        dstore('ボット',f'\n```\n{data}\n```\n')
    keys=["['fortnite']","['fortnite']['email']","['fortnite']['password']","['fortnite']['owner']","['fortnite']['platform']","['fortnite']['cid']","['fortnite']['bid']","['fortnite']['pickaxe_id']","['fortnite']['eid']","['fortnite']['playlist']","['fortnite']['banner']","['fortnite']['banner_color']","['fortnite']['level']","['fortnite']['tier']","['fortnite']['xpboost']","['fortnite']['friendxpboost']","['fortnite']['status']","['fortnite']['privacy']","['fortnite']['partychat']","['fortnite']['joinmessage']","['fortnite']['randommessage']","['fortnite']['joinmessageenable']","['fortnite']['randommessageenable']","['fortnite']['skinmimic']","['fortnite']['emotemimic']","['fortnite']['acceptinvite']","['fortnite']['acceptfriend']","['fortnite']['addfriend']","['fortnite']['inviteinterval']","['fortnite']['interval']","['fortnite']['waitinterval']","['no-logs']","['ingame-error']","['discord-log']","['hide-email']","['hide-password']","['hide-webhook']","['hide-api-key']","['webhook']","['caseinsensitive']","['api-key']","['loglevel']","['debug']"]
    for key in keys:
        exec(f"errorcheck=data{key}")
    try:
        errorcheck=requests.get('https://fortnite-api.com/cosmetics/br/search?name=API-KEY-CHECK',headers={'x-api-key': data['api-key']}).json()
    except UnicodeEncodeError:
        if os.path.isfile('allen.json') is False or os.path.isfile('allja.json') is False:
            print(red('APIキーが無効です。正しい値を入力してください。'))
            dstore('ボット',f'>>> APIキーが無効です。正しい値を入力してください')
            exit()
        else:
            print(red('APIキーが無効です。最新のアイテムデータをダウンロードできませんでした。正しい値を入力してください。'))
            dstore('ボット',f'>>> APIキーが無効です。最新のアイテムデータをダウンロードできませんでした。正しい値を入力してください')
    if errorcheck['status'] == 401:
        if os.path.isfile('allen.json') is False or os.path.isfile('allja.json') is False:
            print(red('APIキーが無効です。正しい値を入力してください。'))
            dstore('ボット',f'>>> APIキーが無効です。正しい値を入力してください')
            exit()
        else:
            print(red('APIキーが無効です。最新のアイテムデータをダウンロードできませんでした。正しい値を入力してください。'))
            dstore('ボット',f'>>> APIキーが無効です。最新のアイテムデータをダウンロードできませんでした。正しい値を入力してください')
    if errorcheck['status'] == 503:
        if os.path.isfile('allen.json') is False or os.path.isfile('allja.json') is False:
            print(red('APIがダウンしているため、アイテムデータをダウンロードできませんでした。しばらく待ってからもう一度起動してみてください。'))
            dstore('ボット',f'>>> APIがダウンしているため、アイテムデータをダウンロードできませんでした。しばらく待ってからもう一度起動してみてください')
            exit()
        else:
            print(red('APIがダウンしているため、最新のアイテムデータをダウンロードできませんでした。'))
            dstore('ボット',f'>>> APIがダウンしているため、最新のアイテムデータをダウンロードできませんでした。')
    credentials={}
    try:
        for count,mail in enumerate(data['fortnite']['email'].split(',')):
            credentials[mail]=data['fortnite']['password'].split(',')[count]
    except IndexError:
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
        print(red('メールアドレスの数に対しパスワードの数が足りません。'))
        dstore('ボット',f'>>> メールアドレスの数に対しパスワードの数が足りません')
except KeyError as e:
    print(red(traceback.format_exc()))
    print(red('config.json ファイルの読み込みに失敗しました。キーの名前が間違っていないか確認してください。アップデート後の場合は、最新のconfig.jsonファイルを確認してください。'))
    print(red(f'{str(e)} がありません。'))
    dstore('ボット',f'>>> {traceback.format_exc()}')
    dstore('ボット',f'>>> config.json ファイルの読み込みに失敗しました。キーの名前が間違っていないか確認してください。アップデート後の場合は、最新のconfig.jsonファイルを確認してください')
    dstore('ボット',f'>>> {str(e)} がありません')
    exit()
except json.decoder.JSONDecodeError as e:
    print(red(traceback.format_exc()))
    print(red('config.json ファイルの読み込みに失敗しました。正しく書き込めているか確認してください。'))
    print(red(str(e).replace('Expecting ','不明な',1).replace('Invalid control character at','無効なコントロール文字: ').replace('value','値',1).replace('delimiter','区切り文字',1).replace('line','行:',1).replace('column','文字:').replace('char ','',1)))
    dstore('ボット',f'>>> {traceback.format_exc()}')
    dstore('ボット',f'>>> config.json ファイルの読み込みに失敗しました。正しく書き込めているか確認してください')
    dstore('ボット',f'>>> {str(e).replace("Expecting ","不明な",1).replace("Invalid control character at","無効なコントロール文字: ").replace("value","値",1).replace("delimiter","区切り文字",1).replace("line","行:",1).replace("column","文字:").replace("char ","",1)}')
    exit()
except FileNotFoundError:
    print(red(traceback.format_exc()))
    print(red('config.json ファイルが存在しません。'))
    dstore('ボット',f'>>> {traceback.format_exc()}')
    dstore('ボット',f'>>> config.json ファイルが存在しません')
    exit()

try:
    try:
        with open('commands.json', 'r', encoding='utf-8') as f:
            commands=json.load(f)
    except json.decoder.JSONDecodeError:
        with open('commands.json', 'r', encoding='utf-8-sig') as f:
            commands=json.load(f)
    if data['loglevel'] == 'debug':
        print(yellow(f'\n{commands}\n'))
        dstore('ボット',f'\n```\n{commands}\n```\n')
    keys=["['true']","['false']","['me']","['prev']", "['eval']", "['exec']","['restart']","['relogin']","['reload']","['get']","['friendcount']","['pendingcount']","['blockcount']","['skinmimic']","['emotemimic']","['partychat']","['acceptinvite']","['acceptfriend']","['joinmessageenable']","['randommessageenable']","['wait']","['join']","['joinid']","['leave']","['invite']","['message']","['partymessage']","['status']","['banner']","['level']","['bp']","['privacy']","['privacy_public']","['privacy_friends_allow_friends_of_friends']","['privacy_friends']","['privacy_private_allow_friends_of_friends']","['privacy_private']","['getuser']","['getfriend']","['getpending']","['getblock']","['info']","['info_party']","['info_item']","['pending']","['removepending']","['addfriend']","['removefriend']","['acceptpending']","['declinepending']","['blockfriend']","['unblockfriend']","['chatban']","['promote']","['kick']","['ready']","['unready']","['sitout']","['skinlock']","['baglock']","['picklock']","['emotelock']","['stop']","['allskin']","['allemote']","['setstyle']","['addstyle']","['setenlightenment']","['addvariant']","['skinasset']","['bagasset']","['pickasset']","['emoteasset']"]
    for key in keys:
        exec(f"errorcheck=commands{key}")
    if data['caseinsensitive'] is True:
        commands=dict((k.lower(), jaconv.kata2hira(v.lower())) for k,v in commands.items())
    for checks in commands.items():
        ignore=['ownercommands','true','false','me', 'privacy_public', 'privacy_friends_allow_friends_of_friends', 'privacy_friends', 'privacy_private_allow_friends_of_friends', 'privacy_private']
        if checks[0] in ignore:
            continue
        if commands['ownercommands'] == '':
            break
        for command in commands['ownercommands'].split(','):
            try:
                errorcheck=commands[command.lower()]
            except KeyError as e:
                print(red(traceback.format_exc()))
                print(red('所有者コマンドの設定に失敗しました。キーの名前が間違っていないか確認してください。'))
                print(red(f'{str(e)} がありません。'))
                dstore('ボット',f'>>> {traceback.format_exc()}')
                dstore('ボット',f'>>> 所有者コマンドの設定に失敗しました。キーの名前が間違っていないか確認してください')
                dstore('ボット',f'>>> {str(e)} がありません')
                exit()
except KeyError as e:
    print(red(traceback.format_exc()))
    print(red('commands.json ファイルの読み込みに失敗しました。キーの名前が間違っていないか確認してください。アップデート後の場合は、最新のcommands.jsonファイルを確認してください。'))
    print(red(f'{str(e)} がありません。'))
    dstore('ボット',f'>>> {traceback.format_exc()}')
    dstore('ボット',f'>>> commands.json ファイルの読み込みに失敗しました。キーの名前が間違っていないか確認してください。アップデート後の場合は、最新のcommands.jsonファイルを確認してください')
    dstore('ボット',f'>>> {str(e)} がありません')
    exit()
except json.decoder.JSONDecodeError as e:
    print(red(traceback.format_exc()))
    print(red('commands.json ファイルの読み込みに失敗しました。正しく書き込めているか確認してください。'))
    print(red(str(e).replace('Expecting ','不明な',1).replace('Invalid control character at','無効なコントロール文字: ').replace('value','値',1).replace('delimiter','区切り文字',1).replace('line','行:',1).replace('column','文字:').replace('char ','',1)))
    dstore('ボット',f'>>> {traceback.format_exc()}')
    dstore('ボット',f'>>> commands.json ファイルの読み込みに失敗しました。正しく書き込めているか確認してください')
    dstore('ボット',f'>>> {str(e).replace("Expecting ","不明な",1).replace("Invalid control character at","無効なコントロール文字: ").replace("value","値",1).replace("delimiter","区切り文字",1).replace("line","行:",1).replace("column","文字:").replace("char ","",1)}')
    exit()
except FileNotFoundError:
    print(red(traceback.format_exc()))
    print(red('commands.json ファイルが存在しません。'))
    dstore('ボット',f'>>> {traceback.format_exc()}')
    dstore('ボット',f'>>> commands.json ファイルが存在しません')
    exit()

try:
    try:
        with open('replies.json', 'r', encoding='utf-8') as f:
            replies=json.load(f)
    except json.decoder.JSONDecodeError:
        with open('replies.json', 'r', encoding='utf-8-sig') as f:
            replies=json.load(f)
    if data['loglevel'] == 'debug':
        print(yellow(f'\n{replies}\n'))
        dstore('ボット',f'\n```\n{replies}\n```\n')
    if data['caseinsensitive'] is True:
        replies=dict((jaconv.kata2hira(k.lower()), v) for k,v in replies.items())
except json.decoder.JSONDecodeError as e:
    print(red(traceback.format_exc()))
    print(red('replies.json ファイルの読み込みに失敗しました。正しく書き込めているか確認してください。'))
    print(red(str(e).replace('Expecting ','不明な',1).replace('Invalid control character at','無効なコントロール文字: ').replace('value','値',1).replace('delimiter','区切り文字',1).replace('line','行:',1).replace('column','文字:').replace('char ','',1)))
    dstore('ボット',f'>>> {traceback.format_exc()}')
    dstore('ボット',f'>>> replies.json ファイルの読み込みに失敗しました。正しく書き込めているか確認してください')
    dstore('ボット',f'>>> {str(e).replace("Expecting ","不明な",1).replace("Invalid control character at","無効なコントロール文字: ").replace("value","値",1).replace("delimiter","区切り文字",1).replace("line","行:",1).replace("column","文字:").replace("char ","",1)}')
    exit()
except FileNotFoundError:
    print(red(traceback.format_exc()))
    print(red('replies.json ファイルが存在しません。'))
    dstore('ボット',f'>>> {traceback.format_exc()}')
    dstore('ボット',f'>>> replies.json ファイルが存在しません')
    exit()

threading.Thread(target=dprint,args=()).start()
threading.Thread(target=get_item_info,args=()).start()

if data['debug'] is True:
    logger = logging.getLogger('fortnitepy.http')
    logger.setLevel(level=logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter('\u001b[36m %(asctime)s:%(levelname)s:%(name)s: %(message)s \u001b[0m'))
    logger.addHandler(handler)

    logger = logging.getLogger('fortnitepy.xmpp')
    logger.setLevel(level=logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter('\u001b[35m %(asctime)s:%(levelname)s:%(name)s: %(message)s \u001b[0m'))
    logger.addHandler(handler)

filename = 'device_auths.json'

if data['loglevel'] not in ('normal', 'info', 'debug'):
    data['loglevel']='normal'
if data['fortnite']['privacy'] not in ('public', 'friends_allow_friends_of_friends', 'friends', 'private_allow_friends_of_friends', 'private'):
    data['fortnite']['privacy']='public'
data['fortnite']['privacy']=eval(f"fortnitepy.PartyPrivacy.{data['fortnite']['privacy'].upper()}")

print(cyan('ロビーボット: gomashio\nクレジット\nライブラリ: Terbau'))
dstore('ボット','ロビーボット: gomashio\nクレジット\nライブラリ: Terbau')
if data['loglevel'] == 'normal':
    print(green('\nログレベル: ノーマル'))
    dstore('ボット','\nログレベル: ノーマル')
elif data['loglevel'] == 'info':
    print(green('\nログレベル: 詳細'))
    dstore('ボット','\nログレベル: 詳細')
elif data['loglevel'] == 'debug':
    print(green('\nログレベル: デバッグ'))
    dstore('ボット','\nログレベル: デバッグ')
if data['debug'] is True:
    print(green('デバッグ: オン'))
    dstore('ボット','デバッグ: オン')
else:
    print(green('デバッグ: オフ'))
    dstore('ボット','デバッグ: オフ')
print(green(f'\nPython {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}\nFortnitepy {fortnitepy.__version__}\n'))
if data['debug'] is True:
    print(red(f'[{now_()}] デバッグが有効です!(エラーではありません)'))
    dstore('ボット','>>> デバッグが有効です!(エラーではありません)')
if data['no-logs'] is False:
    print('ボットを起動中...')
dstore('ボット','ボットを起動中...')

async def event_device_auth_generate(details, email):
    store_device_auth_details(email, details)

async def event_ready(client):
    if data['loglevel'] == 'normal':
        if data['no-logs'] is False:
            print(green(f'[{now_()}] ログイン: {client.user.display_name}'))
        dstore('ボット',f'ログイン: {client.user.display_name}')
    else:
        if data['no-logs'] is False:
            print(green(f'[{now_()}] ログイン: {client.user.display_name} / {client.user.id}'))
        dstore('ボット',f'ログイン: {client.user.display_name} / {client.user.id}')
    client.isready=True

    try:
        client.owner=None
        owner=await client.fetch_profile(data['fortnite']['owner'])
        if owner is None:
            print(red(f'[{now_()}] [{client.user.display_name}] 所有者が見つかりません。正しい名前/IDになっているか確認してください。'))
            dstore(client.user.display_name,'>>> 所有者が見つかりません。正しい名前/IDになっているか確認してください')
        else:
            client.owner=client.get_friend(owner.id)
            if client.owner is None:
                if data['fortnite']['addfriend'] is True:
                    try:
                        await client.add_friend(owner.id)
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                        print(red(f'[{now_()}] [{client.user.display_name}] フレンド申請の送信リクエストを処理中にエラーが発生しました。'))
                        dstore(client.user.display_name,f'>>> フレンド申請の送信リクエストを処理中にエラーが発生しました')
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                print(red(f"[{now_()}] [{client.user.display_name}] 所有者とフレンドではありません。フレンドになってからもう一度起動するか、[{commands['reload']}] コマンドで再読み込みしてください。"))
                dstore(client.user.display_name,f'>>> 所有者とフレンドではありません。フレンドになってからもう一度起動するか、[{commands["reload"]}] コマンドで再読み込みしてください')
            else:
                if data['loglevel'] == 'normal':
                    if data['no-logs'] is False:
                        print(green(f'[{now_()}] [{client.user.display_name}] 所有者: {client.owner.display_name}'))
                    dstore(client.user.display_name,f'所有者: {client.owner.display_name}')
                else:
                    if data['no-logs'] is False:
                        print(green(f'[{now_()}] [{client.user.display_name}] 所有者: {client.owner.display_name} / {client.owner.id}'))
                    dstore(client.user.display_name,f'所有者: {client.owner.display_name} / {client.owner.id}')
    except fortnitepy.HTTPException:
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
        dstore(client.user.display_name,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
    except Exception:
        print(red(traceback.format_exc()))
        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    
    if not client.owner is None:
        await client.owner.send('ここをクリックして招待')

    if data['fortnite']['acceptfriend'] is True:
        pendings=[]
        for pending in client.pending_friends.values():
            if pending.direction == 'INBOUND':
                pendings.append(pending)
        for pending in pendings:
            if client.acceptfriend is True:
                try:
                    await pending.accept()
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                    try:
                        await pending.decline()
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            else:
                try:
                    await pending.decline()
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

async def event_restart():
    if data['no-logs'] is False:
        print(green(f'[{now_()}] 正常に再ログインが完了しました'))
    dstore('ボット',f'>>> 正常に再ログインが完了しました')

async def event_party_invite(invitation):
    if invitation is None:
        return
    client=invitation.client
    if client.isready is False:
        return
    if not client.owner is None:
        if invitation.sender.id == client.owner.id:
            await invitation_accept(invitation)
            return
    if data['loglevel'] == 'normal':
        if data['no-logs'] is False:
            print(f'[{now_()}] [{client.user.display_name}] {str(invitation.sender.display_name)} からのパーティー招待')
        dstore(client.user.display_name,f'{str(invitation.sender.display_name)} からのパーティー招待')
    else:
        if data['no-logs'] is False:
            print(f'[{now_()}] [{client.user.display_name}] {str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待')
        dstore(client.user.display_name,f'{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待')

    if not client.owner is None:
        if not client.owner.id in client.user.party.members.keys():
            if client.acceptinvite is True:
                if client.acceptinvite_interval is True:
                    await invitation_accept(invitation)
                    return
                else:
                    await invitation_decline_interval(invitation)
                    return
            else:
                await invitation_decline(invitation)
        else:
            await invitation_decline_owner(invitation)
    else:
        if client.acceptinvite is True:
            if client.acceptinvite_interval is True:
                await invitation_accept(invitation)
            else:
                await invitation_decline_interval(invitation)
        else:
            await invitation_decline(invitation)

async def event_friend_request(request):
    if request is None:
        return
    client=request.client
    if client.isready is False:
        return
    if request.direction == 'OUTBOUND':
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(f'[{now_()}] [{client.user.display_name}] {str(request.display_name)} にフレンド申請を送信')
            dstore(client.user.display_name,f'{str(request.display_name)} にフレンド申請を送信')
        else:
            if data['no-logs'] is False:
                print(f'[{now_()}] [{client.user.display_name}] {str(request.display_name)} / {request.id} にフレンド申請を送信')
            dstore(client.user.display_name,f'{str(request.display_name)} / {request.id} にフレンド申請を送信')
        return
    if data['loglevel'] == 'normal':
        if data['no-logs'] is False:
            print(f'[{now_()}] [{client.user.display_name}] {str(request.display_name)} からのフレンド申請')
        dstore(client.user.display_name,f'{str(request.display_name)} からのフレンド申請')
    else:
        if data['no-logs'] is False:
            print(f'[{now_()}] [{client.user.display_name}] {str(request.display_name)} / {request.id} からのフレンド申請')
        dstore(client.user.display_name,f'{str(request.display_name)} / {request.id} からのフレンド申請')
    if client.acceptfriend is True:
        try:
            await request.accept()
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            print(red(f'[{now_()}] [{client.user.display_name}] フレンド申請の承諾リクエストを処理中にエラーが発生しました。'))
            dstore(client.user.display_name,f'>>> フレンド申請の承諾リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    elif client.acceptfriend is False:
        try:
            await request.decline()
            if data['loglevel'] == 'normal':
                if data['no-logs'] is False:
                    print(f'[{now_()}] [{client.user.display_name}] {str(request.display_name)} からのフレンド申請を拒否')
                dstore(client.user.display_name,f'{str(request.display_name)} からのフレンド申請を拒否')
            else:
                if data['no-logs'] is False:
                    print(f'[{now_()}] [{client.user.display_name}] {str(request.display_name)} / {request.id} からのフレンド申請を拒否')
                dstore(client.user.display_name,f'{str(request.display_name)} / {request.id} からのフレンド申請を拒否')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            print(f'[{now_()}] [{client.user.display_name}] フレンド申請の拒否リクエストを処理中にエラーが発生しました。')
            dstore(client.user.display_name,f'>>> フレンド申請の拒否リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))

async def event_friend_add(friend):
    if friend is None:
        return
    client=friend.client
    if client.isready is False:
        return
    if friend.direction == 'OUTBOUND':
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(f'[{now_()}] [{client.user.display_name}] {str(friend.display_name)} がフレンド申請を承諾')
            dstore(client.user.display_name,f'{str(friend.display_name)} がフレンド申請を承諾')
        else:
            if data['no-logs'] is False:
                print(f'[{now_()}] [{client.user.display_name}] {str(friend.display_name)} / {friend.id} がフレンド申請を承諾')
            dstore(client.user.display_name,f'{str(friend.display_name)} / {friend.id} がフレンド申請を承諾')
    else:
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(f'[{now_()}] [{client.user.display_name}] {str(friend.display_name)} をフレンドに追加')
            dstore(client.user.display_name,f'{str(friend.display_name)} をフレンドに追加')
        else:
            if data['no-logs'] is False:
                print(f'[{now_()}] [{client.user.display_name}] {str(friend.display_name)} / {friend.id} をフレンドに追加')
            dstore(client.user.display_name,f'{str(friend.display_name)} / {friend.id} をフレンドに追加')

async def event_friend_remove(friend):
    if friend is None:
        return
    client=friend.client
    if client.isready is False:
        return
    if data['loglevel'] == 'normal':
        if data['no-logs'] is False:
            print(f'[{now_()}] [{client.user.display_name}] {str(friend.display_name)} がフレンドから削除')
        dstore(client.user.display_name,f'{str(friend.display_name)} がフレンドから削除')
    else:
        if data['no-logs'] is False:
            print(f'[{now_()}] [{client.user.display_name}] {str(friend.display_name)} / {friend.id} [{platform_to_str(friend.platform)}] がフレンドから削除')
        dstore(client.user.display_name,f'{str(friend.display_name)} / {friend.id} [{platform_to_str(friend.platform)}] がフレンドから削除')

async def event_party_member_join(member):
    if member is None:
        return
    client=member.client
    if client.isready is False:
        return
    client_user_display_name=str(client.user.display_name)
    member_joined_at_most=[]
    for member_ in client.user.party.members.values():
        if member_joined_at_most != []:
            if member_.id in [i.user.id for i in clients]:
                if member_.id != client.user.id:
                    client_user_display_name+=f"/{str(member_.display_name)}"
                if member_.joined_at < member_joined_at_most[1]:
                    member_joined_at_most=[member_.id, member_.joined_at]
        else:
            member_joined_at_most=[client.user.id, client.user.party.me.joined_at]
    if member_joined_at_most == []:
        member_joined_at_most=[client.user.id]
    if client.user.id == member_joined_at_most[0]:
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [パーティー] [{client_user_display_name}] {str(member.display_name)} がパーティーに参加\n人数: {member.party.member_count}'))
            dstore(client_user_display_name,f'[パーティー] {str(member.display_name)} がパーティーに参加\n人数: {member.party.member_count}')
        else:
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [パーティー/{member.party.id}] [{client_user_display_name}] {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] がパーティーに参加\n人数: {member.party.member_count}'))
            dstore(client_user_display_name,f'[パーティー/{member.party.id}] {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] がパーティーに参加\n人数: {member.party.member_count}')
    
    if data['fortnite']['addfriend'] is True:
        for member in member.party.members.keys():
            try:
                await client.add_friend(member)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            except Exception:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

    await asyncio.sleep(0.1)

    if client.joinmessageenable is True:
        try:
            await client.user.party.send(data['fortnite']['joinmessage'])
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    if client.randommessageenable is True:
        try:
            randommessage=random.choice(data['fortnite']['randommessage'].split(','))
            if data['no-logs'] is False:
                print(f'[{now_()}] [{client.user.display_name}] ランダムメッセージ: {randommessage}')
            dstore(client.user.display_name,f'ランダムメッセージ: {randommessage}')
            await client.user.party.send(randommessage)
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

    if not client.user.party.me.emote is None:
        if client.user.party.me.emote.lower() == client.eid.lower():
            await client.user.party.me.clear_emote()
    try:
        await client.user.party.me.set_emote(asset=client.eid)
    except Exception:
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

    if client.user.party.leader.id == client.user.id:
        try:
            await client.user.party.set_playlist(data['fortnite']['playlist'])
            await client.user.party.set_privacy(data['fortnite']['privacy'])
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

async def event_party_member_leave(member):
    if member is None:
        return
    client=member.client
    if client.isready is False:
        return
    client_user_display_name=str(client.user.display_name)
    member_joined_at_most=[]
    for member_ in client.user.party.members.values():
        if member_joined_at_most != []:
            if member_.id in [i.user.id for i in clients]:
                if member_.id != client.user.id:
                    client_user_display_name+=f"/{str(member_.display_name)}"
                if member_.joined_at < member_joined_at_most[1]:
                    member_joined_at_most=[member_.id, member_.joined_at]
        else:
            member_joined_at_most=[client.user.id, client.user.party.me.joined_at]
    if member_joined_at_most == []:
        member_joined_at_most=[client.user.id]
    if client.user.id == member_joined_at_most[0]:
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [パーティー] [{client_user_display_name}] {str(member.display_name)} がパーティーを離脱\n人数: {member.party.member_count}'))
            dstore(client_user_display_name,f'[パーティー] {str(member.display_name)} がパーティーを離脱\n人数: {member.party.member_count}')
        else:
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [パーティー/{member.party.id}] [{client_user_display_name}] {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] がパーティーを離脱\n人数: {member.party.member_count}'))
            dstore(client_user_display_name,f'[パーティー/{member.party.id}] {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] がパーティーを離脱\n人数: {member.party.member_count}')

    if data['fortnite']['addfriend'] is True:
        for member in member.party.members.keys():
            try:
                await client.add_friend(member)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                continue
            except Exception:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

async def event_party_member_kick(member):
    if member is None:
        return
    client=member.client
    if client.isready is False:
        return
    client_user_display_name=str(client.user.display_name)
    member_joined_at_most=[]
    for member_ in client.user.party.members.values():
        if member_joined_at_most != []:
            if member_.id in [i.user.id for i in clients]:
                if member_.id != client.user.id:
                    client_user_display_name+=f"/{str(member_.display_name)}"
                if member_.joined_at < member_joined_at_most[1]:
                    member_joined_at_most=[member_.id, member_.joined_at]
        else:
            member_joined_at_most=[client.user.id, client.user.party.me.joined_at]
    if member_joined_at_most == []:
        member_joined_at_most=[client.user.id]
    if client.user.id == member_joined_at_most[0]:
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [パーティー] [{client_user_display_name}] {str(member.party.leader.display_name)} が {str(member.display_name)} をパーティーからキック\n人数: {member.party.member_count}'))
            dstore(client_user_display_name,f'[パーティー] {str(member.party.leader.display_name)} が {str(member.display_name)} をパーティーからキック\n人数: {member.party.member_count}')
        else:
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [パーティー/{member.party.id}] [{client_user_display_name}] {str(member.party.leader.display_name)} / {member.party.leader.id} [{platform_to_str(member.party.leader.platform)}/{member.input}] が {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] がパーティーからキック\n人数: {member.party.member_count}'))
            dstore(client_user_display_name,f'[パーティー/{member.party.id}] {str(member.party.leader.display_name)} / {member.party.leader.id} [{platform_to_str(member.party.leader.platform)}/{member.input}] が {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] がパーティーからキック\n人数: {member.party.member_count}')

async def event_party_member_promote(old_leader,new_leader):
    if old_leader is None or new_leader is None:
        return
    client=new_leader.client
    if client.isready is False:
        return
    client_user_display_name=str(client.user.display_name)
    member_joined_at_most=[]
    for member_ in client.user.party.members.values():
        if member_joined_at_most != []:
            if member_.id in [i.user.id for i in clients]:
                if member_.id != client.user.id:
                    client_user_display_name+=f"/{str(member_.display_name)}"
                if member_.joined_at < member_joined_at_most[1]:
                    member_joined_at_most=[member_.id, member_.joined_at]
        else:
            member_joined_at_most=[client.user.id, client.user.party.me.joined_at]
    if member_joined_at_most == []:
        member_joined_at_most=[client.user.id]
    if client.user.id == member_joined_at_most[0]:
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [パーティー] [{client_user_display_name}] {str(old_leader.display_name)} から {str(new_leader.display_name)} にリーダーが譲渡'))
            dstore(client_user_display_name,f'[パーティー] {str(old_leader.display_name)} から {str(new_leader.display_name)} にリーダーが譲渡')
        else:
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [パーティー/{new_leader.party.id}] [{client_user_display_name}] {str(old_leader.display_name)} / {old_leader.id} [{platform_to_str(old_leader.platform)}/{old_leader.input}] から {str(new_leader.display_name)} / {new_leader.id} [{platform_to_str(new_leader.platform)}/{new_leader.input}] にリーダーが譲渡'))
            dstore(client_user_display_name,f'[パーティー/{new_leader.party.id}] {str(old_leader.display_name)} / {old_leader.id} [{platform_to_str(old_leader.platform)}/{old_leader.input}] から {str(new_leader.display_name)} / {new_leader.id} [{platform_to_str(new_leader.platform)}/{new_leader.input}] にリーダーが譲渡')
    if new_leader.id == client.user.id:
        try:
            await client.user.party.set_playlist(data['fortnite']['playlist'])
            await client.user.party.set_privacy(data['fortnite']['privacy'])
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

async def event_party_member_update(member):
    if member is None:
        return
    client=member.client
    if client.isready is False:
        return
    client_user_display_name=str(client.user.display_name)
    member_joined_at_most=[]
    for member_ in client.user.party.members.values():
        if member_joined_at_most != []:
            if member_.id in [i.user.id for i in clients]:
                if member_.id != client.user.id:
                    client_user_display_name+=f"/{str(member_.display_name)}"
                if member_.joined_at < member_joined_at_most[1]:
                    member_joined_at_most=[member_.id, member_.joined_at]
        else:
            member_joined_at_most=[client.user.id, client.user.party.me.joined_at]
    if member_joined_at_most == []:
        member_joined_at_most=[client.user.id]
    if client.user.id == member_joined_at_most[0]:
        if not data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [パーティー/{member.party.id}] [{client_user_display_name}] {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] パーティーメンバー更新'))
            dstore(client_user_display_name,f'[パーティー/{member.party.id}] {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] パーティーメンバー更新')
    if member.id == client.user.id:
        return
    if not member.outfit == client.prevoutfit or not member.outfit_variants == client.prevoutfitvariants:
        if not data['loglevel'] == 'normal':
            if client.user.id == member_joined_at_most[0]:
                if data['no-logs'] is False:
                    print(str(member.outfit))
                dstore(client_user_display_name,str(member.outfit))
        if client.skinmimic is True:
            if member.outfit is None:
                try:
                    await client.user.party.me.set_outfit(asset='CID_NONE')
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            else:
                try:
                    await client.user.party.me.set_outfit(asset=member.outfit.upper(),variants=member.outfit_variants)
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    if not member.backpack == client.prevbackpack or not member.backpack_variants == client.prevbackpackvariants:
        if not data['loglevel'] == 'normal':
            if client.user.id == member_joined_at_most[0]:
                if data['no-logs'] is False:
                    print(str(member.backpack))
                dstore(client_user_display_name,str(member.backpack))
        if client.skinmimic is True:
            if member.backpack is None:
                try:
                    await client.user.party.me.set_backpack(asset='BID_NONE')
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            else:
                try:
                    await client.user.party.me.set_backpack(asset=member.backpack.upper(),variants=member.backpack_variants)
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    if not member.pickaxe == client.prevpickaxe or not member.pickaxe_variants == client.prevpickaxevariants:
        if not data['loglevel'] == 'normal':
            if client.user.id == member_joined_at_most[0]:
                if data['no-logs'] is False:
                    print(str(member.pickaxe))
                dstore(client_user_display_name,str(member.pickaxe))
        if client.skinmimic is True:
            if member.pickaxe is None:
                try:
                    await client.user.party.me.set_pickaxe(asset='PICKAXE_ID_NONE')
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            else:
                try:
                    await client.user.party.me.set_pickaxe(asset=member.pickaxe.upper(),variants=member.pickaxe_variants)
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    client.prevoutfit=member.outfit
    client.prevoutfitvariants=member.outfit_variants
    client.prevbackpack=member.backpack
    client.prevbackpackvariants=member.backpack_variants
    client.prevpickaxe=member.pickaxe
    client.prevpickaxevariants=member.pickaxe_variants

    if not member.emote is None:
        if not data['loglevel'] == 'normal':
            if client.user.id == member_joined_at_most[0]:
                if data['no-logs'] is False:
                    print(str(member.emote))
                dstore(client_user_display_name,str(member.emote))
        if client.emotemimic is True:
            if member.emote.upper() == client.user.party.me.emote.upper():
                try:
                    await client.user.party.me.clear_emote()
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            try:
                await client.user.party.me.set_emote(asset=member.emote.upper())
            except Exception:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

async def event_party_member_disconnect(member):
    if member is None:
        return
    client=member.client
    if client.isready is False:
        return
    client_user_display_name=str(client.user.display_name)
    member_joined_at_most=[]
    for member_ in client.user.party.members.values():
        if member_joined_at_most != []:
            if member_.id in [i.user.id for i in clients]:
                if member_.id != client.user.id:
                    client_user_display_name+=f"/{str(member_.display_name)}"
                if member_.joined_at < member_joined_at_most[1]:
                    member_joined_at_most=[member_.id, member_.joined_at]
        else:
            member_joined_at_most=[client.user.id, client.user.party.me.joined_at]
    if member_joined_at_most == []:
        member_joined_at_most=[client.user.id]
    if client.user.id == member_joined_at_most[0]:
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [パーティー] [{client_user_display_name}] {str(member.display_name)} の接続が切断'))
            dstore(client_user_display_name,f'[パーティー] {str(member.display_name)} の接続が切断')
        else:
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [パーティー/{member.party.id}] [{client_user_display_name}] {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] の接続が切断'))
            dstore(client_user_display_name,f'[パーティー/{member.party.id}] {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] の接続が切断')

async def event_party_member_chatban(member, reason):
    if member is None:
        return
    client=member.client
    if client.isready is False:
        return
    client_user_display_name=str(client.user.display_name)
    member_joined_at_most=[]
    for member_ in client.user.party.members.values():
        if member_joined_at_most != []:
            if member_.id in [i.user.id for i in clients]:
                if member_.id != client.user.id:
                    client_user_display_name+=f"/{str(member_.display_name)}"
                if member_.joined_at < member_joined_at_most[1]:
                    member_joined_at_most=[member_.id, member_.joined_at]
        else:
            member_joined_at_most=[client.user.id, client.user.party.me.joined_at]
    if member_joined_at_most == []:
        member_joined_at_most=[client.user.id]
    if client.user.id == member_joined_at_most[0]:
        if data['loglevel'] == 'normal':
            if reason is None:
                if data['no-logs'] is False:
                    print(magenta(f'[{now_()}] [パーティー] [{client_user_display_name}] {str(member.party.leader.display_name)} が {str(member.display_name)} をチャットバン'))
                dstore(client_user_display_name,f'[パーティー] {str(member.party.leader.display_name)} が {str(member.display_name)} をチャットバン')
            else:
                if data['no-logs'] is False:
                    print(magenta(f'[{now_()}] [パーティー] [{client_user_display_name}] {str(member.party.leader.display_name)} が {str(member.display_name)} をチャットバン | 理由: {reason}'))
                dstore(client_user_display_name,f'[パーティー] {str(member.party.leader.display_name)} が {str(member.display_name)} をチャットバン | 理由: {reason}')
        else:
            if reason is None:
                if data['no-logs'] is False:
                    print(magenta(f'[{now_()}] [パーティー/{member.party.id}] [{client_user_display_name}] {str(member.party.leader.display_name)} / {member.party.leader.id} [{platform_to_str(member.party.leader.platform)}/{member.party.leader.input}] が {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] をチャットバン'))
                dstore(client_user_display_name,f'[パーティー/{member.party.id}] {str(member.party.leader.display_name)} / {member.party.leader.id} [{platform_to_str(member.party.leader.platform)}/{member.party.leader.input}] が {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] をチャットバン')
            else:
                if data['no-logs'] is False:
                    print(magenta(f'[{now_()}] [パーティー/{member.party.id}] [{client_user_display_name}] {str(member.party.leader.display_name)} / {member.party.leader.id} [{platform_to_str(member.party.leader.platform)}/{member.party.leader.input}] が {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] をチャットバン | 理由: {reason}'))
                dstore(client_user_display_name,f'[パーティー/{member.party.id}] {str(member.party.leader.display_name)} / {member.party.leader.id} [{platform_to_str(member.party.leader.platform)}/{member.party.leader.input}] が {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] をチャットバン | 理由: {reason}')

async def event_party_update(party):
    if party is None:
        return
    client=party.client
    if client.isready is False:
        return
    client_user_display_name=str(client.user.display_name)
    member_joined_at_most=[]
    for member_ in client.user.party.members.values():
        if member_joined_at_most != []:
            if member_.id in [i.user.id for i in clients]:
                if member_.id != client.user.id:
                    client_user_display_name+=f"/{str(member_.display_name)}"
                if member_.joined_at < member_joined_at_most[1]:
                    member_joined_at_most=[member_.id, member_.joined_at]
        else:
            member_joined_at_most=[client.user.id, client.user.party.me.joined_at]
    if member_joined_at_most == []:
        member_joined_at_most=[client.user.id]
    if client.user.id == member_joined_at_most[0]:
        if not data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [パーティー/{party.id}] [{client_user_display_name}] パーティー更新'))
            dstore(client_user_display_name,f'[パーティー/{party.id}] パーティー更新')

#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================

async def event_friend_message(message):
    if message is None:
        return
    client=message.client
    if client.isready is False:
        return
    content=message.content
    if data['caseinsensitive'] is True:
        args = jaconv.kata2hira(content.lower()).split()
    else:
        args = content.split()
    rawargs = content.split()
    rawcontent = ' '.join(rawargs[1:])
    rawcontent2 = ' '.join(rawargs[2:])
    user=None
    if rawcontent in commands['me'].split(','):
        rawcontent=str(message.author.display_name)
    if data['loglevel'] == 'normal':
        if data['no-logs'] is False:
            print(f'[{now_()}] [{client.user.display_name}] {str(message.author.display_name)} | {content}')
        dstore(message.author.display_name,content)
    else:
        if data['no-logs'] is False:
            print(f'[{now_()}] [{client.user.display_name}] {str(message.author.display_name)}/ {message.author.id} [{platform_to_str(message.author.platform)}] | {content}')
        dstore(f'{message.author.display_name} / {message.author.id}',content)

    if not client.owner is None:
        if not client.owner.id == message.author.id:
            for checks in commands.items():
                ignore=['ownercommands','true','false','me', 'privacy_public', 'privacy_friends_allow_friends_of_friends', 'privacy_friends', 'privacy_private_allow_friends_of_friends', 'privacy_private', 'info_party', 'info_item']
                if checks[0] in ignore:
                    continue
                if commands['ownercommands'] == '':
                    break
                for command in commands['ownercommands'].split(','):
                    if args[0] in commands[command.lower()].split(','):
                        await message.reply('このコマンドは管理者しか使用できません')
                        return

    if args[0] in commands['prev'].split(','):
        if client.prevmessage.get(message.author.id) is None:
            client.prevmessage[message.author.id]='None'
        content=client.prevmessage.get(message.author.id)
        if data['caseinsensitive'] is True:
            args = jaconv.kata2hira(content.lower()).split()
        else:
            args = content.split()
        args = jaconv.kata2hira(content.lower()).split()
        rawargs = content.split()
        rawcontent = ' '.join(rawargs[1:])
        rawcontent2 = ' '.join(rawargs[2:])
    client.prevmessage[message.author.id]=content

    for key,value in replies.items():
        if args[0] in key:
            try:
                await message.reply(value)
            except Exception:
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                await message.reply('エラー')
            return

    if args[0] in commands['eval'].split(','):
        try:
            if rawcontent == "":
                await message.reply(f"[{commands['eval']}] [式]")
                return
            variable=globals()
            variable.update(locals())
            if rawcontent.startswith("await "):
                if data['loglevel'] == "debug":
                    print(f"await eval({rawcontent.replace('await ','',1)})")
                result = await eval(rawcontent.replace("await ","",1), variable)
                await message.reply(str(result))
            else:
                if data['loglevel'] == "debug":
                    print(f"eval {rawcontent}")
                result = eval(rawcontent, variable)
                await message.reply(str(result))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['exec'].split(','):
        try:
            if rawcontent == "":
                await message.reply(f"[{commands['exec']}] [文]")
                return
            variable=globals()
            variable.update(locals())
            variable_prev=variable
            if rawcontent.startswith("await "):
                if data['loglevel'] == "debug":
                    print(f"await exec({rawcontent.replace('await ','',1)})")
                result = await exec(rawcontent.replace("await ","",1), variable)
                await message.reply(str(result))
                for key, value in variable.items():
                    if key not in variable_prev.keys():
                        exec(f"global {key}")
                        exec(f"{key} = {value}")
            else:
                if data['loglevel'] == "debug":
                    print(f"exec {rawcontent}")
                result = exec(rawcontent, variable)
                await message.reply(str(result))
                for key, value in variable.items():
                    if key not in variable_prev.keys():
                        exec(f"global {key}")
                        exec(f"{key} = {value}")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['restart'].split(','):
        try:
            if client.acceptinvite is False and client.owner is None:
                await message.reply('招待が拒否に設定されているので実行できません')
            elif client.acceptinvite is False and not message.author.id == client.owner.id:
                await message.reply('招待が拒否に設定されているので実行できません')
            else:
                await message.reply('プログラムを再起動します...')
                os.chdir(os.getcwd())
                os.execv(os.sys.executable,['python','index.py'])
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['relogin'].split(','):
        try:
            await message.reply('アカウントに再ログインします...')
            await client.restart()
        except fortnitepy.AuthException:
            print(red(traceback.format_exc()))
            print(red(f'[{now_()}] [{client.user.display_name}] メールアドレスまたはパスワードが間違っています。'))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            dstore(client.user.display_name,f'>>> メールアドレスまたはパスワードが間違っています')
            kill=True
            exit()
        except Exception:
            print(red(traceback.format_exc()))
            print(red(f'[{now_()}] [{client.user.display_name}] アカウントの読み込みに失敗しました。もう一度試してみてください。'))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            dstore(client.user.display_name,f'>>> アカウントの読み込みに失敗しました。もう一度試してみてください')
            kill=True
            exit()

    elif args[0] in commands['reload'].split(','):
        result=reload_configs(client)
        try:
            if result == 'Success':
                await message.reply('正常に読み込みが完了しました')
            else:
                await message.reply('エラー')
                return
            client.owner=None
            try:
                owner=await client.fetch_profile(data['fortnite']['owner'])
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
                dstore(client.user.display_name,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if owner is None:
                print(red(f'[{now_()}] [{client.user.display_name}] 所有者が見つかりません。正しい名前/IDになっているか確認してください。'))
                dstore(client.user.display_name,f'>>> 所有者が見つかりません。正しい名前/IDになっているか確認してください')
                return
            client.owner=client.get_friend(owner.id)
            if client.owner is None:
                if data['fortnite']['addfriend'] is True:
                    try:
                        await client.add_friend(owner.id)
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                        print(red(f'[{now_()}] [{client.user.display_name}] フレンド申請の送信リクエストを処理中にエラーが発生しました。'))
                        dstore(client.user.display_name,f'>>> フレンド申請の送信リクエストを処理中にエラーが発生しました')
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] 所有者とフレンドではありません。フレンドになってからもう一度起動してください。'))
                dstore(client.user.display_name,f'>>> 所有者とフレンドではありません。フレンドになってからもう一度起動してください')
                return
            if data['loglevel'] == 'normal':
                print(green(f'[{now_()}] [{client.user.display_name}] 所有者: {client.owner.display_name}'))
                dstore(client.user.display_name,f'所有者: {client.owner.display_name}')
            else:
                print(green(f'[{now_()}] [{client.user.display_name}] 所有者: {client.owner.display_name} / {client.owner.id}'))
                dstore(client.user.display_name,f'所有者: {client.owner.display_name} / {client.owner.id}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['get'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['get']}] [ユーザー名/ユーザーID]")
                return
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            if not user.id in client.user.party.members.keys():
                await message.reply('ユーザーがパーティーにいません')
                return
            member=client.user.party.members.get(user.id)
            if data['no-logs'] is False:
                print(f'{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{member.backpack} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{member.emote}')
            dstore(client.user.display_name,f'{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{member.backpack} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{member.emote}')
            await message.reply(f'{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{member.backpack} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{member.emote}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['friendcount'].split(','):
        try:
            if data['no-logs'] is False:
                print(f'フレンド数: {len(client.friends)}')
            dstore(client.user.display_name,f'フレンド数: {len(client.friends)}')
            await message.reply(f'フレンド数: {len(client.friends)}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['pendingcount'].split(','):
        try:
            outbound = []
            inbound = []
            for pending in client.pending_friends.values():
                if pending.direction == 'OUTBOUND':
                    outbound.append(pending)
                elif pending.direction == 'INBOUND':
                    inbound.append(pending)
            if data['no-logs'] is False:
                print(f'保留数: {len(client.pending_friends)}\n送信: {len(outbound)}\n受信: {len(inbound)}')
            dstore(client.user.display_name,f'保留数: {len(client.pending_friends)}\n送信: {len(outbound)}\n受信: {len(inbound)}')
            await message.reply(f'保留数: {len(client.pending_friends)}\n送信: {len(outbound)}\n受信: {len(inbound)}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['blockcount'].split(','):
        try:
            if data['no-logs'] is False:
                print(f'ブロック数: {len(client.blocked_users)}')
            dstore(client.user.display_name,f'ブロック数: {len(client.blocked_users)}')
            await message.reply(f'ブロック数: {len(client.blocked_users)}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['friendlist'].split(','):
        try:
            text=''
            for friend in client.friends.values():
                text+=f'{friend}\n'
            if data['no-logs'] is False:
                print(f'{text}')
            dstore(client.user.display_name,f'{text}')
            await message.reply(f'{text}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['pendinglist'].split(','):
        try:
            outbound=''
            inbound=''
            for pending in client.pending_friends.values():
                if pending.direction == 'OUTBOUND':
                    outbound+=f'{pending}\n'
                elif pending.direction == 'INBOUND':
                    inbound+=f'{pending}\n'
            if data['no-logs'] is False:
                print(f'送信: {outbound}\n受信: {inbound}')
            dstore(client.user.display_name,f'送信: {outbound}\n受信: {inbound}')
            await message.reply(f'送信: {outbound}\n受信: {inbound}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['blocklist'].split(','):
        try:
            text=''
            for block in client.blocked_users.values():
                text+=f'{block}\n'
            if data['no-logs'] is False:
                print(f'{text}')
            dstore(client.user.display_name,f'{text}')
            await message.reply(f'{text}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['skinmimic'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.skinmimic=True
                await message.reply('スキンミミックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.skinmimic=False
                await message.reply('スキンミミックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['skinmimic']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['emotemimic'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.emotemimic=True
                await message.reply('エモートミミックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.emotemimic=False
                await message.reply('エモートミミックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['emotemimic']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['partychat'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.partychat=True
                await message.reply('パーティーチャットからのコマンド受付をオンに設定')
            elif args[1] in commands['false'].split(','):
                client.partychat=False
                await message.reply('パーティーチャットからのコマンド受付をオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['party']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['acceptinvite'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.acceptinvite=True
                await message.reply('招待を承諾に設定')
            elif args[1] in commands['false'].split(','):
                client.acceptinvite=False
                await message.reply('招待を拒否に設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['acceptinvite']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['acceptfriend'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.acceptfriend=True
                await message.reply('フレンド申請を承諾に設定')
            elif args[1] in commands['false'].split(','):
                client.acceptfriend=False
                await message.reply('フレンド申請を拒否に設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['acceptfriend']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['joinmessageenable'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.joinmessageenable=True
                await message.reply('パーティー参加時のメッセージをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.joinmessageenable=False
                await message.reply('パーティー参加時のメッセージをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['joinmessageenable']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['randommessageenable'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.randommessageenable=True
                await message.reply('パーティー参加時のランダムメッセージをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.randommessageenable=False
                await message.reply('パーティー参加時のランダムメッセージをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['randommessageenable']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['wait'].split(','):
        try:
            if client.owner is None:
                client.acceptinvite=False
                try:
                    client.timer_.cancel()
                except AttributeError:
                    pass
                client.timer_=Timer(data['fortnite']['waitinterval'], inviteaccept, [client])
                client.timer_.start()
                await message.reply(f"{str(data['fortnite']['waitinterval'])}秒間招待を拒否します")
            else:
                if client.owner.id in client.user.party.members.keys() and not message.author.id == client.owner.id:
                    await message.reply('現在利用できません')
                    return
                client.acceptinvite=False
                try:
                    client.timer_.cancel()
                except AttributeError:
                    pass
                client.timer_=Timer(data['fortnite']['waitinterval'], inviteaccept, [client])
                client.timer_.start()
                await message.reply(f"{str(data['fortnite']['waitinterval'])}秒間招待を拒否します")             
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['join'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['join']}] [ユーザー名/ユーザーID]")
                return
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            friend=client.get_friend(user.id)
            if friend is None:
                await message.reply('ユーザーとフレンドではありません')
            else:
                await friend.join_party()
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('既にパーティーのメンバーです')
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティーが見つかりません')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティーがプライベートです')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティーの参加リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['joinid'].split(','):
        try:
            await client.join_to_party(party_id=args[1])
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('既にこのパーティーのメンバーです')
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティーが見つかりません')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティーがプライベートです')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['join']}] [パーティーID]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['leave'].split(','):
        try:
            await client.user.party.me.leave()
            await message.reply('パーティーを離脱')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティー離脱のリクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['invite'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['invite']}] [ユーザー名 / ユーザーID]")
                return
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            friend=client.get_friend(user.id)
            if friend is None:
                await message.reply('ユーザーとフレンドではありません')
                return
            await friend.invite()
            if data['loglevel'] == 'normal':
                await message.reply(f'{str(friend.display_name)} をパーティーに招待')
            else:
                await message.reply(f'{str(friend.display_name)} / {friend.id} をパーティー {client.user.party.id} に招待')
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティーが満員か、既にパーティーにいます')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティー招待の送信リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['message'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['message']}] [ユーザー名 / ユーザーID] : [内容]")
                return
            send=rawcontent.split(' : ')
            try:
                user=await client.fetch_profile(send[0])
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            friend=client.get_friend(user.id)
            if friend is None:
                await message.reply('ユーザーとフレンドではありません')
                return
            await friend.send(send[1])
            if data['loglevel'] == 'normal':
                await message.reply(f'{str(friend.display_name)} にメッセージ {send[1]} を送信')
            else:
                await message.reply(f'{str(friend.display_name)} / {friend.id} にメッセージ {send[1]} を送信')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['message']}] [ユーザー名 / ユーザーID] : [内容]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['partymessage'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['partymessage']}] [内容]")
                return
            await client.user.party.send(rawcontent)
            if data['loglevel'] == 'normal':
                await message.reply(f'パーティーにメッセージ {rawcontent} を送信')
            else:
                await message.reply(f'パーティー {client.user.party.id} にメッセージ {rawcontent} を送信')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['status'].split(','):
        try:
            await client.set_status(rawcontent)
            await message.reply(f'ステータスを {rawcontent} に設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['status']}] [内容]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['banner'].split(','):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_banner,args[1],args[2],client.user.party.me.banner[2]))
            await message.reply(f'バナーを {args[1]}, {args[2]}に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('バナー情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['banner']}] [バナーID] [バナーの色]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['level'].split(','):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_banner,client.user.party.me.banner[0],client.user.party.me.banner[1],int(args[1])))
            await message.reply(f'レベルを {args[1]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('レベルの設定リクエストを処理中にエラーが発生しました')
        except ValueError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('数字を入力してください')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['level']}] [レベル]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['bp'].split(','):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_battlepass_info,True,args[1],args[2],args[3]))
            await message.reply(f'バトルパス情報を ティア: {args[1]} XPブースト: {args[2]} フレンドXPブースト: {args[3]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('バトルパス情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['bp']}] [ティア] [XPブースト] [フレンドXPブースト]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['privacy'].split(','):
        try:
            if args[1] in commands['privacy_public'].split(','):
                await client.user.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)
                await message.reply('プライバシーを パブリック に設定')
            elif args[1] in commands['privacy_friends_allow_friends_of_friends'].split(','):
                await client.user.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS_ALLOW_FRIENDS_OF_FRIENDS)
                await message.reply('プライバシーを フレンド(フレンドのフレンドを許可) に設定')
            elif args[1] in commands['privacy_friends'].split(','):
                await client.user.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS)
                await message.reply('プライバシーを フレンド に設定')
            elif args[1] in commands['privacy_private_allow_friends_of_friends'].split(','):
                await client.user.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE_ALLOW_FRIENDS_OF_FRIENDS)
                await message.reply('プライバシーを プライベート(フレンドのフレンドを許可) に設定')
            elif args[1] in commands['privacy_privacte'].split(','):
                await client.user.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE)
                await message.reply('プライバシーを プライベート に設定')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティーリーダーではありません')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['privacy']}] [[{commands['privacy_public']}] / [{commands['privacy_friends_allow_friends_of_friends']}] / [{commands['privacy_friends']}] / [{commands['privacy_private_allow_friends_of_friends']}] / [{commands['privacy_privacte']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー') 

    elif args[0] in commands['getuser'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['getuser']}] [ユーザー名 / ユーザーID]")
                return
            user=await client.fetch_profile(rawcontent)
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            if data['no-logs'] is False:
                print(f'{str(user.display_name)} / {user.id}')
            dstore(client.user.display_name,f'{str(user.display_name)} / {user.id}')
            await message.reply(f'{str(user.display_name)} / {user.id}')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['getfriend'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['getfriend']}] [ユーザー名 / ユーザーID]")
                return
            user=await client.fetch_profile(rawcontent)
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            friend=client.get_friend(user.id)
            if friend is None:
                await message.reply('ユーザーとフレンドではありません')
                return
            if friend.nickname is None:
                if data['no-logs'] is False:
                    print(f'{str(friend.display_name)} / {friend.id}')
                dstore(client.user.display_name,f'{str(friend.display_name)} / {friend.id}')
                await message.reply(f'{str(friend.display_name)} / {friend.id}')
            else:
                if data['no-logs'] is False:
                    print(f'{friend.nickname}({str(friend.display_name)}) / {friend.id}')
                dstore(client.user.display_name,f'{friend.nickname}({str(friend.display_name)}) / {friend.id}')
                await message.reply(f'{friend.nickname}({str(friend.display_name)}) / {friend.id}')
            if not friend.last_logout is None:
                await message.reply('最後のログイン: {0.year}年{0.month}月{0.day}日 {0.hour}時{0.minute}分{0.second}秒'.format(friend.last_logout))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['getpending'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['getpending']}] [ユーザー名 / ユーザーID]")
                return
            user=await client.fetch_profile(rawcontent)
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            pending=client.get_pending_friend(user.id)
            if pending is None:
                await message.reply('ユーザーからのフレンド申請がありません')
                return
            if data['no-logs'] is False:
                print(f'{str(pending.display_name)} / {pending.id}')
            dstore(client.user.display_name,f'{str(pending.display_name)} / {pending.id}')
            await message.reply(f'{str(pending.display_name)} / {pending.id}')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['getblock'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['getblock']}] [ユーザー名 / ユーザーID]")
                return
            user=await client.fetch_profile(rawcontent)
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            block=client.get_blocked_user(user.id)
            if block is None:
                await message.reply('ユーザーをブロックしていません')
                return
            if data['no-logs'] is False:
                print(f'{str(block.display_name)} / {block.id}')
            dstore(client.user.display_name,f'{str(block.display_name)} / {block.id}')
            await message.reply(f'{str(block.display_name)} / {block.id}')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['info'].split(','):
        try:
            if args[1] in commands['info_party'].split(','):
                if data['no-logs'] is False:
                    print(f'{client.user.party.id}\n人数: {client.user.party.member_count}')
                dstore(client.user.display_name,f'{client.user.party.id}\n人数: {client.user.party.member_count}')
                await message.reply(f'{client.user.party.id}\n人数: {client.user.party.member_count}')
                for member in client.user.party.members.values():
                    if data['loglevel'] == 'normal':
                        print(str(member.display_name))
                        dstore(client.user.display_name,str(member.display_name))
                        await message.reply(str(member.display_name))
                    else:
                        print(f'{str(member.display_name)} / {member.id}')
                        dstore(client.user.display_name,f'{str(member.display_name)} / {member.id}')
                        await message.reply(f'{str(member.display_name)} / {member.id}')
            elif args[1] in commands['info_item'].split(','):
                if rawcontent2 == '':
                    await message.reply(f"[{commands['info']}] [{commands['info_item']}] [アイテム名]")
                    return
                items=await is_itemname('ja', rawcontent2)
                if items[0] == 'True':
                    client.itemdata=items
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                        return
                    for item in items[1]:
                        await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    return
                items=await is_itemname('en', rawcontent2)
                if items[0] == 'True':
                    client.itemdata=items
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                        return
                    for item in items[1]:
                        await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    return
                await message.reply('見つかりません')
            elif args[1] in commands['id'].split(','):
                if rawcontent2 == '':
                    await message.reply(f"[{commands['info']}] [{commands['id']}] [ID]")
                    return
                items=await search_item_with_id('ja', rawcontent2)
                if items[0] == 'True':
                    client.itemdata=items
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                        return
                    for item in items[1]:
                        await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    return
                items=await search_item_with_id('en', rawcontent2)
                if items[0] == 'True':
                    client.itemdata=items
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                        return
                    for item in items[1]:
                        await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    return
                await message.reply('見つかりません')
            elif args[1] in commands['skin'].split(','):
                if rawcontent2 == '':
                    await message.reply(f"[{commands['info']}] [{commands['skin']}] [スキン名]")
                    return
                items=await search_item_with_type('ja', rawcontent2, 'outfit')
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                        return
                    for item in items[1]:
                        await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    return
                items=await search_item_with_type('en', rawcontent2, 'outfit')
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                        return
                    for item in items[1]:
                        await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    return
                await message.reply('見つかりません')
            elif args[1] in commands['bag'].split(','):
                if rawcontent2 == '':
                    await message.reply(f"[{commands['info']}] [{commands['bag']}] [バッグ名]")
                    return
                items=await search_item_with_type('ja', rawcontent2, 'backpack,pet')
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                        return
                    for item in items[1]:
                        await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    return
                items=await search_item_with_type('en', rawcontent2, 'outfit')
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                        return
                    for item in items[1]:
                        await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    return
                await message.reply('見つかりません')
            elif args[1] in commands['pickaxe'].split(','):
                if rawcontent2 == '':
                    return await message.reply(f"[{commands['info']}] [{commands['pickaxe']}] [ツルハシ名]")
                items=await search_item_with_type('ja', rawcontent2, 'pickaxe')
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                        return
                    for item in items[1]:
                        await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    return
                items=await search_item_with_type('en', rawcontent2, 'outfit')
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                        return
                    for item in items[1]:
                        await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    return
                await message.reply('見つかりません')
            elif args[1] in commands['emote'].split(','):
                if rawcontent2 == '':
                    return await message.reply(f"[{commands['info']}] [{commands['emote']}] [エモート名]")
                items=await search_item_with_type('ja', rawcontent2, 'emote,emoji,toy')
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                        return
                    for item in items[1]:
                        await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    return
                items=await search_item_with_type('en', rawcontent2, 'outfit')
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                        return
                    for item in items[1]:
                        await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    return
                await message.reply('見つかりません')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['info']}] [[{commands['info_party']}] / [{commands['info_item']}] / [{commands['id']}] / [{commands['skin']}] / [{commands['bag']}] / [{commands['pickaxe']}] / [{commands['emote']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['pending'].split(','):
        try:
            pendings=[]
            for pending in client.pending_friends.values():
                if pending.direction == 'INBOUND':
                    pendings.append(pending)
            if args[1] in commands['true'].split(','):
                for pending in pendings:
                    try:
                        await pending.accept()
                        if data['loglevel'] == 'normal':
                            await message.reply(f'{str(pending.display_name)} をフレンドに追加')
                        else:
                            await message.reply(f'{str(pending.display_name)} / {pending.id} をフレンドに追加')
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                        if data['loglevel'] == 'normal':
                            await message.reply(f'{str(pending.dispaly_name)} のフレンド申請の承認リクエストを処理中にエラーが発生しました')
                        else:
                            await message.reply(f'{str(pending.display_name)} / {pending.id} のフレンド申請の承認リクエストを処理中にエラーが発生しました')
                        continue
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                        await message.reply('エラー')
                        continue
            elif args[1] in commands['false'].split(','):
                for pending in pendings:
                    try:
                        await pending.decline()
                        if data['loglevel'] == 'normal':
                            await message.reply(f'{str(pending.display_name)} のフレンド申請を拒否')
                        else:
                            await message.reply(f'{str(pending.display_name)} / {pending.id} のフレンド申請を拒否')
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                        if data['loglevel'] == 'normal':
                            await message.reply(f'{str(pending.display_name)} のフレンド申請の拒否リクエストを処理中にエラーが発生しました')
                        else:
                            await message.reply(f'{str(pending.display_name)} / {pending.id} のフレンド申請の拒否リクエストを処理中にエラーが発生しました')
                        continue
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                        await message.reply('エラー')
                        continue
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['pending']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['removepending'].split(','):
        try:
            pendings=[]
            for pending in client.pending_friends.values():
                if pending.direction == 'OUTBOUND':
                    pendings.append(pending)
            for pending in pendings:
                try:
                    await pending.decline()
                    if data['loglevel'] == 'normal':
                        await message.reply(f'{str(pending.display_name)} へのフレンド申請を解除')
                    else:
                        await message.reply(f'{str(pending.display_name)} / {pending.id} へのフレンド申請を解除')
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                    if data['loglevel'] == 'normal':
                        await message.reply(f'{str(pending.display_name)} へのフレンド申請を解除リクエストを処理中にエラーが発生しました')
                    else:
                        await message.reply(f'{str(pending.display_name)} / {pending.id} へのフレンド申請を解除リクエストを処理中にエラーが発生しました')
                    continue
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                    await message.reply('エラー')
                    continue
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['addfriend'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['addfriend']}] [ユーザー名 / ユーザーID]")
                return
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            if client.has_friend(user.id) is True:
                await message.reply('既にユーザーとフレンドです')
                return
            await client.add_friend(user.id)
            if data['loglevel'] == 'normal':
                await message.reply(f'{str(user.display_name)} にフレンド申請を送信')
            else:
                await message.reply(f'{str(user.display_name)} / {user.id} にフレンド申請を送信')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('フレンド申請の送信リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['removefriend'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['removefriend']}] [ユーザー名 / ユーザーID]")
                return
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            if client.has_friend(user.id) is False:
                await message.reply('ユーザーとフレンドではありません')
                return
            await client.remove_or_decline_friend(user.id)
            if data['loglevel'] == 'normal':
                await message.reply(f'{str(user.display_name)} をフレンドから削除')
            else:
                await message.reply(f'{str(user.display_name)} / {user.id} をフレンドから削除')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('フレンドの削除リクエストを処理中にエラーが発生しました')    
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['acceptpending'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['acceptpending']}] [ユーザー名 / ユーザーID]")
                return
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            if client.is_pending(user.id) is False:
                await message.reply('ユーザーからのフレンド申請がありません')
                return
            await client.accept_friend(user.id)
            if data['loglevel'] == 'normal':
                await message.reply(f'{str(user.display_name)} をフレンドに追加')
            else:
                await message.reply(f'{str(user.display_name)} / {user.id} をフレンドに追加')       
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('フレンドの追加リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['declinepending'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['declinepending']}] [ユーザー名 / ユーザーID]")
                return
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            if client.is_pending(user.id) is False:
                await message.reply('ユーザーからのフレンド申請がありません')
                return
            await client.remove_or_decline_friend(user.id)
            if data['loglevel'] == 'normal':
                await message.reply(f'{str(user.display_name)} のフレンド申請を拒否')
            else:
                await message.reply(f'{str(user.display_name)} / {user.id} のフレンド申請を拒否')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('フレンド申請の拒否リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['blockfriend'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['blockfriend']}] [ユーザー名 / ユーザーID]")
                return
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            if user.id in client.blocked_users.keys():
                await message.reply('既にユーザーをブロックしています')
                return
            await client.block_user(user.id)
            if user.display_name is None:
                await message.reply(f'None / {user.id} をブロック')
            if data['loglevel'] == 'normal':
                await message.reply(f'{str(user.display_name)} をブロック')
            else:
                await message.reply(f'{str(user.display_name)} / {user.id} をブロック')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('フレンドのブロックリクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['unblockfriend'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['unblockfriend']}] [ユーザー名 / ユーザーID]")
                return
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            if not user.id in client.blocked_users.keys():
                await message.reply('ユーザーをブロックしていません')
                return
            await client.unblock_user(user.id)
            if data['loglevel'] == 'normal':
                await message.reply(f'{str(user.display_name)} をブロック解除')
            else:
                await message.reply(f'{str(user.display_name)} / {user.id} をブロック解除')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('ブロックしたユーザーのブロック解除リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['chatban'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['chatban']}] [ユーザー名 / ユーザーID] : [理由(任意)]")
                return
            reason=rawcontent.split(' : ')
            try:
                user=await client.fetch_profile(reason[0])
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            if not user.id in client.user.party.members.keys():
                await message.reply('ユーザーがパーティーにいません')
                return
            member=client.user.party.members.get(user.id)
            try:
                await member.chatban(reason[1])
            except IndexError:
                await member.chatban()
            if data['loglevel'] == 'normal':
                await message.reply(f'{str(user.display_name)} をバン')
            else:
                await message.reply(f'{str(user.display_name)} / {user.id} をバン')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティーリーダーではありません')
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('メンバーが見つかりません')
        except ValueError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('既にバンされています')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['promote'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['promote']}] [ユーザー名 / ユーザーID]")
                return
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            if not user.id in client.user.party.members.keys():
                await message.reply('ユーザーがパーティーにいません')
                return
            member=client.user.party.members.get(user.id)
            await member.promote()
            if data['loglevel'] == 'normal':
                await message.reply(f'{str(user.display_name)} に譲渡')
            else:
                await message.reply(f'{str(user.display_name)} / {user.id} に譲渡')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティーリーダーではありません')
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('既にパーティーリーダーです')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティーリーダーの譲渡リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['kick'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['kick']}] [ユーザー名 / ユーザーID]")
                return
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            if not user.id in client.user.party.members.keys():
                await message.reply('ユーザーがパーティーにいません')
                return
            member=client.user.party.members.get(user.id)
            await member.kick()
            if data['loglevel'] == 'normal':
                await message.reply(f'{str(user.display_name)} をキック')
            else:
                await message.reply(f'{str(user.display_name)} / {user.id} をキック')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティーリーダーではありません')
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('自分をキックすることはできません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティーメンバーのキックリクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['ready'].split(','):
        try:
            await client.user.party.me.set_ready(fortnitepy.ReadyState.READY)
            await message.reply('準備状態を 準備OK に設定')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['unready'].split(','):
        try:
            await client.user.party.me.set_ready(fortnitepy.ReadyState.NOT_READY)
            await message.reply('準備状態を 準備中 に設定')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['sitout'].split(','):
        try:
            await client.user.party.me.set_ready(fortnitepy.ReadyState.SITTING_OUT)
            await message.reply('準備状態を 欠場中 に設定')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['skinlock'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.skinlock=True
                await message.reply('スキンロックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.skinlock=False
                await message.reply('スキンロックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['skinlock']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['baglock'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.baglock=True
                await message.reply('バッグロックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.baglock=False
                await message.reply('バッグロックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['skinlock']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['picklock'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.picklock=True
                await message.reply('ツルハシロックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.picklock=False
                await message.reply('ツルハシロックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['skinlock']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['emotelock'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.emotelock=True
                await message.reply('エモートロックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.emotelock=False
                await message.reply('エモートロックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['skinlock']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['stop'].split(','):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.emotelock is True:
                    await message.reply('エモートロックが有効です')
                    return
            elif client.emotelock is True:
                await message.reply('エモートロックが有効です')
                return
            client.stopcheck=True
            await client.user.party.me.clear_emote()
            await message.reply('停止しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['allskin'].split(','):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.skinlock is True:
                    await message.reply('スキンロックが有効です')
                    return
            elif client.skinlock is True:
                await message.reply('スキンロックが有効です')
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allskin = json.load(f)
            for item in allskin['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type'] == 'outfit':
                    if 'banner' not in item['id']:
                        await client.user.party.me.set_outfit(item['id'])
                    else:
                        await client.user.party.me.set_outfit(item['id'],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner'))
                    await asyncio.sleep(2)
            await message.reply('全てのスキンを表示し終わりました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['allemote'].split(','):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.emotelock is True:
                    await message.reply('エモートロックが有効です')
                    return
            elif client.emotelock is True:
                await message.reply('エモートロックが有効です')
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allemote = json.load(f)
            for item in allemote['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type'] == 'emote':
                    await client.user.party.me.set_emote(item['id'])
                    await asyncio.sleep(5)
            else:
                await message.reply('全てのエモートを表示し終わりました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['setstyle'].split(','):
        if rawcontent2 == '':
            await message.reply(f"[{commands['setstyle']}] [[{commands['skin']}] / [{commands['bag']}] / [{commands['pickaxe']}]] [スタイル名]")
            return
        try:
            if args[1] in commands['skin']:
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.skinlock is True:
                        await message.reply('スキンロックが有効です')
                        return
                elif client.skinlock is True:
                    await message.reply('スキンロックが有効です')
                    return
                variants=await search_style("ja", rawcontent2, client.user.party.me.outfit)
                if variants is None:
                    variants=await search_style("en", rawcontent2, client.user.party.me.outfit)
                if not variants is None:
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.user.party.me.outfit,variants=variants))
                else:
                    await message.reply('見つかりません')
            elif args[1] in commands['bag']:
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.baglock is True:
                        await message.reply('バッグロックが有効です')
                        return
                elif client.baglock is True:
                    await message.reply('バッグロックが有効です')
                    return
                variants=await search_style("ja", rawcontent2, client.user.party.me.backpack)
                if variants is None:
                    variants=await search_style("en", rawcontent2, client.user.party.me.backpack)
                if not variants is None:
                    if client.user.party.me.backpack.lower().startswith('bid_'):
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.user.party.me.backpack,variants=variants))
                    elif client.user.party.me.backpack.lower().startswith('petcarrier_'):
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.user.party.me.backpack,variants=variants))
                else:
                    await message.reply('見つかりません')
            elif args[1] in commands['pickaxe']:
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.picklock is True:
                        await message.reply('ツルハシロックが有効です')
                        return
                elif client.picklock is True:
                    await message.reply('ツルハシロックが有効です')
                    return
                variants=await search_style("ja", rawcontent2, client.user.pickaxe)
                if variants is None:
                    variants=await search_style("en", rawcontent2, client.user.party.me.pickaxe)
                if not variants is None:
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.user.party.me.pickaxe,variants=variants))
                else:
                    await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['setstyle']}] [[{commands['skin']}] / [{commands['bag']}] / [{commands['pickaxe']}]] [スタイル名]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['addstyle'].split(','):
        if rawcontent2 == '':
            await message.reply(f"[{commands['addstyle']}] [[{commands['skin']}] / [{commands['bag']}] / [{commands['pickaxe']}]] [スタイル名]")
            return
        try:
            if args[1] in commands['skin']:
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.skinlock is True:
                        await message.reply('スキンロックが有効です')
                        return
                elif client.skinlock is True:
                    await message.reply('スキンロックが有効です')
                    return
                variants=await search_style("ja", rawcontent2, client.user.party.me.outfit)
                if variants is None:
                    variants=await search_style("en", rawcontent2, client.user.party.me.outfit)
                if not variants is None:
                    for val in client.user.party.me.outfit_variants:
                        variants.append({'item': val['item'], 'channel': val['channel'], 'variant': val['variant']})
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.user.party.me.outfit,variants=variants))
                else:
                    await message.reply('見つかりません')
            elif args[1] in commands['bag']:
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.baglock is True:
                        await message.reply('バッグロックが有効です')
                        return
                elif client.baglock is True:
                    await message.reply('バッグロックが有効です')
                    return
                variants=await search_style("ja", rawcontent2, client.user.party.me.backpack)
                if variants is None:
                    variants=await search_style("en", rawcontent2, client.user.party.me.backpack)
                for val in client.user.party.me.backpack_variants:
                    variants.append({'item': val['item'], 'channel': val['channel'], 'variant': val['variant']})
                if not variants is None:
                    if client.user.party.me.backpack.lower().startswith('bid_'):
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.user.party.me.backpack,variants=variants))
                    elif client.user.party.me.backpack.lower().startswith('petcarrier_'):
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.user.party.me.backpack,variants=variants))
                else:
                    await message.reply('見つかりません')
            elif args[1] in commands['pickaxe']:
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.picklock is True:
                        await message.reply('ツルハシロックが有効です')
                        return
                elif client.picklock is True:
                    await message.reply('ツルハシロックが有効です')
                    return
                variants=await search_style("ja", rawcontent2, client.user.pickaxe)
                if variants is None:
                    variants=await search_style("en", rawcontent2, client.user.party.me.pickaxe)
                if not variants is None:
                    for val in client.user.party.me.pickaxe_variants:
                        variants.append({'item': val['item'], 'channel': val['channel'], 'variant': val['variant']})
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.user.party.me.pickaxe,variants=variants))
                else:
                    await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['addstyle']}] [[{commands['skin']}] / [{commands['bag']}] / [{commands['pickaxe']}]] [スタイル名]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['setenlightenment'].split(','):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.skinlock is True:
                    await message.reply('スキンロックが有効です')
                    return
            elif client.skinlock is True:
                await message.reply('スキンロックが有効です')
                return
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.user.party.me.outfit,variants=client.user.party.me.outfit_variants,enlightenment=(args[1],args[2])))
            await message.reply(f'{args[1]}, {args[2]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['setenlightenment']}] [数値] [数値]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['id'].split(','):
        if rawcontent == '':
            await message.reply(f"[{commands['id']}] [ID]")
            return
        try:
            isitem = await search_item_with_id("ja", rawcontent)
            if isitem[0] == 'True':
                client.itemdata=isitem
                if len(client.itemdata[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.itemdata[1])))
                    return
                for count,item in enumerate(client.itemdata[1]):
                    if item[2] == 'outfit':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'スキン: {item[0]}: {item[1]}')
                        else:
                            await message.reply(f'{count+1} スキン: {item[0]}: {item[1]}')
                    if item[2] == 'backpack':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'バッグ: {item[0]}: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[0]}: {item[1]}')
                    if item[2] == 'pet':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'バッグ: {item[0]}: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[0]}: {item[1]}')
                    if item[2] == 'pickaxe':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'ツルハシ: {item[0]}: {item[1]}')
                        else:
                            await message.reply(f'{count+1} ツルハシ: {item[0]}: {item[1]}')
                    if item[2] == 'emote':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[0]}: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[0]}: {item[1]}')
                    if item[2] == 'emoji':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[0]}: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[0]}: {item[1]}')
                    if item[2] == 'toy':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[0]}: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[0]}: {item[1]}')
                if len(client.itemdata[1]) == 1:
                    if not data['loglevel'] == 'normal':
                        if data['no-logs'] is False:
                            print(client.itemdata[1][0][0])
                        dstore(client.user.display_name,client.itemdata[1][0][0])
                    if client.itemdata[1][0][2] == 'outfit':
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.skinlock is True:
                                await message.reply('スキンロックが有効です')
                                return
                        elif client.skinlock is True:
                            await message.reply('スキンロックが有効です')
                            return
                        if 'banner' not in client.itemdata[1][0][0]:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.itemdata[1][0][0]))
                        else:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.itemdata[1][0][0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                    if client.itemdata[1][0][2] == 'backpack':
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.baglock is True:
                                await message.reply('バッグロックが有効です')
                                return
                        elif client.baglock is True:
                            await message.reply('バッグロックが有効です')
                            return
                        if 'banner' not in client.itemdata[1][0][0]:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.itemdata[1][0][0]))
                        else:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.itemdata[1][0][0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                    if client.itemdata[1][0][2] == 'pet':
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.baglock is True:
                                await message.reply('バッグロックが有効です')
                                return
                        elif client.baglock is True:
                            await message.reply('バッグロックが有効です')
                            return
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.itemdata[1][0][0]))
                    if client.itemdata[1][0][2] == 'pickaxe':
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.picklock is True:
                                await message.reply('ツルハシロックが有効です')
                                return
                        elif client.picklock is True:
                            await message.reply('ツルハシロックが有効です')
                            return
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.itemdata[1][0][0]))
                        if not client.user.party.me.emote is None:
                            if client.user.party.me.emote.lower() == 'eid_iceking':
                                await client.user.party.me.clear_emote()
                        await client.user.party.me.set_emote('EID_IceKing')
                    if client.itemdata[1][0][2] == 'emote':
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.emotelock is True:
                                await message.reply('エモートロックが有効です')
                                return
                        elif client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            return
                        if not client.user.party.me.emote is None:
                            if client.user.party.me.emote.lower() == client.itemdata[1][0][0].lower():
                                await client.user.party.me.clear_emote()
                        await client.user.party.me.set_emote(client.itemdata[1][0][0])
                        client.eid=client.itemdata[1][0][0]
                    if client.itemdata[1][0][2] == 'emoji':
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.emotelock is True:
                                await message.reply('エモートロックが有効です')
                                return
                        elif client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            return
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}'
                    if client.itemdata[1][0][2] == 'toy':
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.emotelock is True:
                                await message.reply('エモートロックが有効です')
                                return
                        elif client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            return
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}'
                if len(client.itemdata[1]) > 1:
                    await message.reply('数字を入力することでそのアイテムに設定します')
            else:
                await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['skin'].split(','):
        if rawcontent == '':
            await message.reply(f"[{commands['skin']}] [スキン名]")
            return
        try:
            isitem = await search_item_with_type("ja", rawcontent, "outfit")
            if isitem[0] == 'True':
                client.itemdata=isitem
                if len(client.itemdata[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.itemdata[1])))
                    return
                for count,item in enumerate(client.itemdata[1]):
                    if len(client.itemdata[1]) == 1:
                        await message.reply(f'{item[1]}')
                    else:
                        await message.reply(f'{count+1}: {item[1]}')
                if len(client.itemdata[1]) == 1:
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.skinlock is True:
                            await message.reply('スキンロックが有効です')
                            return
                    elif client.skinlock is True:
                        await message.reply('スキンロックが有効です')
                        return
                    if not data['loglevel'] == 'normal':
                        if data['no-logs'] is False:
                            print(client.itemdata[1][0][0])
                        dstore(client.user.display_name,client.itemdata[1][0][0])
                    if 'banner' not in client.itemdata[1][0][0]:
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.itemdata[1][0][0]))
                    else:
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.itemdata[1][0][0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                if len(client.itemdata[1]) > 1:
                    await message.reply('数字を入力することでそのアイテムに設定します')
                return
            isitem = await search_item_with_type("en", rawcontent, "outfit")
            if isitem[0] == 'True':
                client.itemdata=isitem
                if len(client.itemdata[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.itemdata[1])))
                    return
                for count,item in enumerate(client.itemdata[1]):
                    if len(client.itemdata[1]) == 1:
                        await message.reply(f'{item[1]}')
                    else:
                        await message.reply(f'{count+1}: {item[1]}')
                if len(client.itemdata[1]) == 1:
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.skinlock is True:
                            await message.reply('スキンロックが有効です')
                            return
                    elif client.skinlock is True:
                        await message.reply('スキンロックが有効です')
                        return
                    if not data['loglevel'] == 'normal':
                        if data['no-logs'] is False:
                            print(client.itemdata[1][0][0])
                        dstore(client.user.display_name,client.itemdata[1][0][0])
                    if 'banner' not in client.itemdata[1][0][0]:
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.itemdata[1][0][0]))
                    else:
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.itemdata[1][0][0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                if len(client.itemdata[1]) > 1:
                    await message.reply('数字を入力することでそのアイテムに設定します')
                return
            await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['bag'].split(','):
        if rawcontent == '':
            await message.reply(f"[{commands['bag']}] [バッグ名]")
            return
        try:
            isitem = await search_item_with_type("ja", rawcontent, "backpack,pet")
            if isitem[0] == 'True':
                client.itemdata=isitem
                if len(client.itemdata[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.itemdata[1])))
                    return
                for count,item in enumerate(client.itemdata[1]):
                    if len(client.itemdata[1]) == 1:
                        await message.reply(f'{item[1]}')
                    else:
                        await message.reply(f'{count+1}: {item[1]}')
                if len(client.itemdata[1]) == 1:
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.baglock is True:
                            await message.reply('バッグロックが有効です')
                            return
                    elif client.baglock is True:
                        await message.reply('バッグロックが有効です')
                        return
                    if not data['loglevel'] == 'normal':
                        if data['no-logs'] is False:
                            print(client.itemdata[1][0][0])
                        dstore(client.user.display_name,client.itemdata[1][0][0])
                    if client.itemdata[1][0][2] == 'backpack':
                        if 'banner' not in client.itemdata[1][1][0]:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.itemdata[1][0][0]))
                        else:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.itemdata[1][0][0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                    if client.itemdata[1][0][2] == 'pet':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.itemdata[1][0][0]))
                if len(client.itemdata[1]) > 1:
                    await message.reply('数字を入力することでそのアイテムに設定します')
                return
            isitem = await search_item_with_type("en", rawcontent, "backpack,pet")
            if isitem[0] == 'True':
                client.itemdata=isitem
                if len(client.itemdata[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.itemdata[1])))
                else:
                    for count,item in enumerate(client.itemdata[1]):
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'{item[1]}')
                        else:
                            await message.reply(f'{count+1}: {item[1]}')
                    if len(client.itemdata[1]) == 1:
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.baglock is True:
                                await message.reply('バッグロックが有効です')
                                return
                        elif client.baglock is True:
                            await message.reply('バッグロックが有効です')
                            return
                        if not data['loglevel'] == 'normal':
                            if data['no-logs'] is False:
                                print(client.itemdata[1][0][0])
                            dstore(client.user.display_name,client.itemdata[1][0][0])
                        if client.itemdata[1][0][2] == 'backpack':
                            if 'banner' not in client.itemdata[1][0][0]:
                                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.itemdata[1][0][0]))
                            else:
                                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.itemdata[1][0][0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                        if client.itemdata[1][0][2] == 'pet':
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.itemdata[1][0][0]))
                    if len(client.itemdata[1]) > 1:
                        await message.reply('数字を入力することでそのアイテムに設定します')
                return
            await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['pickaxe'].split(','):
        if rawcontent == '':
            await message.reply(f"[{commands['pickaxe']}] [ツルハシ名]")
            return
        try:
            isitem = await search_item_with_type("ja", rawcontent, "pickaxe")
            if isitem[0] == 'True':
                client.itemdata=isitem
                if len(client.itemdata[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.itemdata[1])))
                    return
                for count,item in enumerate(client.itemdata[1]):
                    if len(client.itemdata[1]) == 1:
                        await message.reply(f'{item[1]}')
                    else:
                        await message.reply(f'{count+1}: {item[1]}')
                if len(client.itemdata[1]) == 1:
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.picklock is True:
                            await message.reply('ツルハシロックが有効です')
                            return
                    elif client.picklock is True:
                        await message.reply('ツルハシロックが有効です')
                        return
                    if not data['loglevel'] == 'normal':
                        if data['no-logs'] is False:
                            print(client.itemdata[1][0][0])
                        dstore(client.user.display_name,client.itemdata[1][0][0])
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.itemdata[1][0][0]))
                    if not client.user.party.me.emote is None:
                        if client.user.party.me.emote.lower() == 'eid_iceking':
                            await client.user.party.me.clear_emote()
                    await client.user.party.me.set_emote('EID_IceKing')
                if len(client.itemdata[1]) > 1:
                    await message.reply('数字を入力することでそのアイテムに設定します')
                return
            isitem = await search_item_with_type("en", rawcontent, "pickaxe")
            if isitem[0] == 'True':
                client.itemdata=isitem
                if len(client.itemdata[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.itemdata[1])))
                    return
                for count,item in enumerate(client.itemdata[1]):
                    if len(client.itemdata[1]) == 1:
                        await message.reply(f'{item[1]}')
                    else:
                        await message.reply(f'{count+1}: {item[1]}')
                if len(client.itemdata[1]) == 1:
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.picklock is True:
                            await message.reply('ツルハシロックが有効です')
                            return
                    elif client.picklock is True:
                        await message.reply('ツルハシロックが有効です')
                        return
                    if not data['loglevel'] == 'normal':
                        if data['no-logs'] is False:
                            print(client.itemdata[1][0][0])
                        dstore(client.user.display_name,client.itemdata[1][0][0])
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.itemdata[1][0][0]))
                    await client.user.party.me.set_emote('EID_IceKing')
                if len(client.itemdata[1]) > 1:
                    await message.reply('数字を入力することでそのアイテムに設定します')
                return
            await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['emote'].split(','):
        if rawcontent == '':
            await message.reply(f"[{commands['emote']}] [エモート名]]")
            return
        try:
            isitem = await search_item_with_type("ja", rawcontent, "emote,emoji,toy")
            if isitem[0] == 'True':
                client.itemdata=isitem
                if len(client.itemdata[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.itemdata[1])))
                    return
                for count,item in enumerate(client.itemdata[1]):
                    if len(client.itemdata[1]) == 1:
                        await message.reply(f'{item[1]}')
                    else:
                        await message.reply(f'{count+1}: {item[1]}')
                if len(client.itemdata[1]) == 1:
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            return
                    elif client.emotelock is True:
                        await message.reply('エモートロックが有効です')
                        return
                    if not data['loglevel'] == 'normal':
                        if data['no-logs'] is False:
                            print(client.itemdata[1][0][0])
                        dstore(client.user.display_name,client.itemdata[1][0][0])
                    if client.itemdata[1][0][2] == 'emote':
                        await client.user.party.me.set_emote(client.itemdata[1][0][0])
                        client.eid=client.itemdata[1][0][0]
                    if client.itemdata[1][0][2] == 'emoji':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}'
                    if client.itemdata[1][0][2] == 'toy':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}'
                if len(client.itemdata[1]) > 1:
                    await message.reply('数字を入力することでそのアイテムに設定します')
                return
            isitem = await search_item_with_type("en", rawcontent, "emote,emoji,toy")
            if isitem[0] == 'True':
                client.itemdata=isitem
                if len(client.itemdata[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.itemdata[1])))
                    return
                for count,item in enumerate(client.itemdata[1]):
                    if len(client.itemdata[1]) == 1:
                        await message.reply(f'{item[1]}')
                    else:
                        await message.reply(f'{count+1}: {item[1]}')
                if len(client.itemdata[1]) == 1:
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            return
                    elif client.emotelock is True:
                        await message.reply('エモートロックが有効です')
                        return
                    if not data['loglevel'] == 'normal':
                        if data['no-logs'] is False:
                            print(client.itemdata[1][0][0])
                        dstore(client.user.display_name,client.itemdata[1][0][0])
                    if client.itemdata[1][0][2] == 'emote':
                        await client.user.party.me.set_emote(client.itemdata[1][0][0])
                        client.eid=client.itemdata[1][0][0]
                    if client.itemdata[1][0][2] == 'emoji':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}'
                    if client.itemdata[1][0][2] == 'toy':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}'
                if len(client.itemdata[1]) > 1:
                    await message.reply('数字を入力することでそのアイテムに設定します')
                return
            await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['set'].split(','):
        if rawcontent == '':
            await message.reply(f"[{commands['set']}] [セット名]]")
            return
        try:
            isitem = await search_set_item("ja", rawcontent)
            if isitem[0] == 'True':
                client.itemdata=isitem
                for count,item in enumerate(client.itemdata[1]):
                    if not data['loglevel'] == 'normal':
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    if item[2] == 'outfit':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'スキン: {item[1]}')
                        else:
                            await message.reply(f'{count+1} スキン: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.skinlock is True:
                                await message.reply('スキンロックが有効です')
                                continue
                        elif client.skinlock is True:
                            await message.reply('スキンロックが有効です')
                            continue
                        if 'banner' not in item[0]:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,item[0]))
                        else:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,item[0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                    if item[2] == 'backpack':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.baglock is True:
                                await message.reply('バッグロックが有効です')
                                continue
                        elif client.baglock is True:
                            await message.reply('バッグロックが有効です')
                            continue
                        if 'banner' not in item[0]:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,item[0]))
                        else:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,item[0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                    if item[2] == 'pet':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.baglock is True:
                                await message.reply('バッグロックが有効です')
                                continue
                        elif client.baglock is True:
                            await message.reply('バッグロックが有効です')
                            continue
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,item[0]))
                    if item[2] == 'pickaxe':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'ツルハシ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} ツルハシ: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.picklock is True:
                                await message.reply('ツルハシロックが有効です')
                                continue
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,item[0]))
                        await client.user.party.me.set_emote('EID_IceKing')
                    if item[2] == 'emote':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.emotelock is True:
                                await message.reply('エモートロックが有効です')
                                continue
                        elif client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            continue
                        await client.user.party.me.set_emote(item[0])
                        client.eid=item[0]
                    if item[2] == 'emoji':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.emotelock is True:
                                await message.reply('エモートロックが有効です')
                                continue
                        elif client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            continue
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{item[0]}.{item[0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{item[0]}.{item[0]}'
                    if item[2] == 'toy':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.emotelock is True:
                                await message.reply('エモートロックが有効です')
                                continue
                        elif client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            continue
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{item[0]}.{item[0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{item[0]}.{item[0]}'
                return
            isitem = await search_set_item("en", rawcontent)
            if isitem[0] == 'True':
                client.itemdata=isitem
                for count,item in enumerate(client.itemdata[1]):
                    if not data['loglevel'] == 'normal':
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    if item[2] == 'outfit':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'スキン: {item[1]}')
                        else:
                            await message.reply(f'{count+1} スキン: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.skinlock is True:
                                await message.reply('スキンロックが有効です')
                                continue
                        elif client.skinlock is True:
                            await message.reply('スキンロックが有効です')
                            continue
                        if 'banner' not in item[0]:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,item[0]))
                        else:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,item[0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                    if item[2] == 'backpack':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.baglock is True:
                                await message.reply('バッグロックが有効です')
                                continue
                        elif client.baglock is True:
                            await message.reply('バッグロックが有効です')
                            continue
                        if 'banner' not in item[0]:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,item[0]))
                        else:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,item[0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                    if item[2] == 'pet':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.baglock is True:
                                await message.reply('バッグロックが有効です')
                                continue
                        elif client.baglock is True:
                            await message.reply('バッグロックが有効です')
                            continue
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,item[0]))
                    if item[2] == 'pickaxe':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'ツルハシ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} ツルハシ: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.picklock is True:
                                await message.reply('ツルハシロックが有効です')
                                continue
                        elif client.picklock is True:
                            await message.reply('ツルハシロックが有効です')
                            continue
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,item[0]))
                        await client.user.party.me.set_emote('EID_IceKing')
                    if item[2] == 'emote':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.emotelock is True:
                                await message.reply('エモートロックが有効です')
                                continue
                        elif client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            continue
                        await client.user.party.me.set_emote(item[0])
                        client.eid=item[0]
                    if item[2] == 'emoji':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.emotelock is True:
                                await message.reply('エモートロックが有効です')
                                continue
                        elif client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            continue
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{item[0]}.{item[0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{item[0]}.{item[0]}'
                    if item[2] == 'toy':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.emotelock is True:
                                await message.reply('エモートロックが有効です')
                                continue
                        elif client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            continue
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{item[0]}.{item[0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{item[0]}.{item[0]}'
                return
            await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['setvariant'].split(','):
        try:
            variantdict={}
            for count,text in enumerate(args[2:]):
                if count % 2 != 0:
                    continue
                try:
                    variantdict[text]=args[count+3]
                except IndexError:
                    break
            if args[1].startswith('cid_'):
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.skinlock is True:
                        await message.reply('スキンロックが有効です')
                        return
                elif client.skinlock is True:
                    await message.reply('スキンロックが有効です')
                    return
                if 'banner' not in args[1]:
                    variants=client.user.party.me.create_variants(item='AthenaCharacter',**variantdict)
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,asset=args[1],variants=variants))
                else:
                    variantdict['profile_banner']='ProfileBanner'
                    variants=client.user.party.me.create_variants(item='AthenaCharacter',**variantdict)
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,asset=args[1],variants=variants))
                await message.reply(f'スキンを {args[1]} {variants} に設定')
            elif args[1].startswith('bid_'):
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.baglock is True:
                        await message.reply('バッグロックが有効です')
                        return
                elif client.baglock is True:
                    await message.reply('バッグロックが有効です')
                    return
                if 'banner' not in args[1]:
                    variants=client.user.party.me.create_variants(item='AthenaBackpack',**variantdict)
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,asset=args[1],variants=variants))
                else:
                    variantdict['profile_banner']='ProfileBanner'
                    variants=client.user.party.me.create_variants(item='AthenaBackpack',**variantdict)
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,asset=args[1],variants=variants))
                await message.reply(f'バッグを {args[1]} {variants} に設定')
            elif args[1].startswith('petcarrier_'):
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.baglock is True:
                        await message.reply('バッグロックが有効です')
                        return
                elif client.baglock is True:
                    await message.reply('バッグロックが有効です')
                    return
                variants=client.user.party.me.create_variants(item='AthenaBackpack',**variantdict)
                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,asset=args[1],variants=variants))
                await message.reply(f'バッグを {args[1]} {variants} に設定')
            elif args[1].startswith('pickaxe_id_'):
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.picklock is True:
                        await message.reply('ツルハシロックが有効です')
                        return
                elif client.picklock is True:
                    await message.reply('ツルハシロックが有効です')
                    return
                variants=client.user.party.me.create_variants(item='AthenaPickaxe',**variantdict)
                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,asset=args[1],variants=variants))
                await client.user.party.me.set_emote('EID_IceKing')
                await message.reply(f'ツルハシを {args[1]} {variants} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['setvariant']}] [ID] [variant] [数値]\nvariantと数値は無限に設定可能")
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['addvariant'].split(','):
        try:
            variantdict={}
            for count,text in enumerate(args[2:]):
                if count % 2 != 0:
                    continue
                try:
                    variantdict[text]=args[count+3]
                except IndexError:
                    break
            if args[1].startswith('cid_'):
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.skinlock is True:
                        await message.reply('スキンロックが有効です')
                        return
                elif client.skinlock is True:
                    await message.reply('スキンロックが有効です')
                    return
                if 'banner' not in args[1]:
                    variants=client.user.party.me.create_variants(item='AthenaCharacter',**variantdict)
                    for val in client.user.party.me.outfit_variants:
                        variants.append({'item': val['item'], 'channel': val['channel'], 'variant': val['variant']})
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,asset=args[1],variants=variants))
                else:
                    variantdict['profile_banner']='ProfileBanner'
                    variants=client.user.party.me.create_variants(item='AthenaCharacter',**variantdict)
                    for val in client.user.party.me.outfit_variants:
                        variants.append({'item': val['item'], 'channel': val['channel'], 'variant': val['variant']})
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,asset=args[1],variants=variants))
                await message.reply(f'スキンを {args[1]} {variants} に設定')
            elif args[1].startswith('bid_'):
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.baglock is True:
                        await message.reply('バッグロックが有効です')
                        return
                elif client.baglock is True:
                    await message.reply('バッグロックが有効です')
                    return
                if 'banner' not in args[1]:
                    variants=client.user.party.me.create_variants(item='AthenaBackpack',**variantdict)
                    for val in client.user.party.me.backpack_variants:
                        variants.append({'item': val['item'], 'channel': val['channel'], 'variant': val['variant']})
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,asset=args[1],variants=variants))
                else:
                    variantdict['profile_banner']='ProfileBanner'
                    variants=client.user.party.me.create_variants(item='AthenaBackpack',**variantdict)
                    for val in client.user.party.me.backpack_variants:
                        variants.append({'item': val['item'], 'channel': val['channel'], 'variant': val['variant']})
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,asset=args[1],variants=variants))
                await message.reply(f'バッグを {args[1]} {variants} に設定')
            elif args[1].startswith('petcarrier_'):
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.baglock is True:
                        await message.reply('バッグロックが有効です')
                        return
                elif client.baglock is True:
                    await message.reply('バッグロックが有効です')
                    return
                variants=client.user.party.me.create_variants(item='AthenaBackpack',**variantdict)
                for val in client.user.party.me.backpack_variants:
                    variants.append({'item': val['item'], 'channel': val['channel'], 'variant': val['variant']})
                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,asset=args[1],variants=variants))
                await message.reply(f'バッグを {args[1]} {variants} に設定')
            elif args[1].startswith('pickaxe_id_'):
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.picklock is True:
                        await message.reply('ツルハシロックが有効です')
                        return
                elif client.picklock is True:
                    await message.reply('ツルハシロックが有効です')
                    return
                variants=client.user.party.me.create_variants(item='AthenaPickaxe',**variantdict)
                for val in client.user.party.me.pickaxe_variants:
                    variants.append({'item': val['item'], 'channel': val['channel'], 'variant': val['variant']})
                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,asset=args[1],variants=variants))
                await client.user.party.me.set_emote('EID_IceKing')
                await message.reply(f'ツルハシを {args[1]} {variants} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['addvariant']}] [variant] [数値]\nvariantと数値は無限に設定可能")
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['skinasset'].split(','):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.skinlock is True:
                    await message.reply('スキンロックが有効です')
                    return
            elif client.skinlock is True:
                await message.reply('スキンロックが有効です')
                return
            if 'banner' not in args[0]:
                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,rawcontent))
            else:
                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,rawcontent,variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['skinasset']}] [アセットパス]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['bagasset'].split(','):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.baglock is True:
                    await message.reply('バッグロックが有効です')
                    return
            elif client.baglock is True:
                await message.reply('バッグロックが有効です')
                return
            if 'banner' not in args[0]:
                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,rawcontent))
            else:
                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,rawcontent,variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['bagasset']}] [アセットパス]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['pickasset'].split(','):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.picklock is True:
                    await message.reply('ツルハシロックが有効です')
                    return
            elif client.picklock is True:
                await message.reply('ツルハシロックが有効です')
                return
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,rawcontent))
            await client.user.party.me.set_emote('EID_IceKing')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['pickasset']}] [アセットパス]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['emoteasset'].split(','):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.emotelock is True:
                    await message.reply('エモートロックが有効です')
                    return
            elif client.emotelock is True:
                await message.reply('エモートロックが有効です')
                return
            await client.user.party.me.clear_emote()
            await client.user.party.me.set_emote(args[1])
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['emoteasset']}] [アセットパス]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0].lower().startswith('cid_'):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.skinlock is True:
                    await message.reply('スキンロックが有効です')
                    return
            elif client.skinlock is True:
                await message.reply('スキンロックが有効です')
                return
            if not data['loglevel'] == 'normal':
                if data['no-logs'] is False:
                    print(args[0])
                dstore(client.user.display_name,args[0])
            if 'banner' not in args[0].lower():
                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,args[0]))
            else:
                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,args[0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
            await message.reply(f'スキンを {args[0]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0].lower().startswith('bid_'):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.baglock is True:
                    await message.reply('バッグロックが有効です')
                    return
            elif client.baglock is True:
                await message.reply('バッグロックが有効です')
                return
            if not data['loglevel'] == 'normal':
                if data['no-logs'] is False:
                    print(args[0])
                dstore(client.user.display_name,args[0])
            if 'banner' not in args[0].lower():
                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,args[0]))
            else:
                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,args[0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
            await message.reply(f'バッグを {args[0]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0].lower().startswith('pet_carrier'):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.baglock is True:
                    await message.reply('バッグロックが有効です')
                    return
            elif client.baglock is True:
                await message.reply('バッグロックが有効です')
                return
            if not data['loglevel'] == 'normal':
                if data['no-logs'] is False:
                    print(args[0])
                dstore(client.user.display_name,args[0])
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,args[0]))
            await message.reply(f'バッグを {args[0]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0].lower().startswith('pickaxe_id'):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.picklock is True:
                    await message.reply('ツルハシロックが有効です')
                    return
            elif client.picklock is True:
                await message.reply('ツルハシロックが有効です')
                return
            if not data['loglevel'] == 'normal':
                if data['no-logs'] is False:
                    print(args[0])
                dstore(client.user.display_name,args[0])
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,args[0]))
            await client.user.party.me.set_emote('EID_IceKing')
            await message.reply(f'ツルハシを {args[0]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0].lower().startswith('eid_'):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.emotelock is True:
                    await message.reply('エモートロックが有効です')
                    return
            elif client.emotelock is True:
                await message.reply('エモートロックが有効です')
                return
            if not data['loglevel'] == 'normal':
                if data['no-logs'] is False:
                    print(args[0])
                dstore(client.user.display_name,args[0])
            if not client.user.party.me.emote is None:
                if client.user.party.me.emote.lower() == args[0].lower():
                    await client.user.party.me.clear_emote()
            await client.user.party.me.set_emote(args[0])
            await message.reply(f'エモートを {args[0]} に設定')
            client.eid=args[0]
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0].lower().startswith('shout_'):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.emotelock is True:
                    await message.reply('エモートロックが有効です')
                    return
            elif client.emotelock is True:
                await message.reply('エモートロックが有効です')
                return
            if not data['loglevel'] == 'normal':
                if data['no-logs'] is False:
                    print(args[0])
            if not client.user.party.me.emote is None:
                if client.user.party.me.emote.lower() == args[0].lower():
                    await client.user.party.me.clear_emote()
            await client.user.party.me.set_shout(args[0])
            await message.reply(f'エモートを {args[0]} に設定')
            client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Shouts/{args[0]}.{args[0]}'
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0].lower().startswith('emoji_'):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.emotelock is True:
                    await message.reply('エモートロックが有効です')
                    return
            elif client.emotelock is True:
                await message.reply('エモートロックが有効です')
                return
            if not data['loglevel'] == 'normal':
                if data['no-logs'] is False:
                    print(args[0])
                dstore(client.user.display_name,args[0])
            if not client.user.party.me.emote is None:
                if client.user.party.me.emote.lower() == args[0].lower():
                    await client.user.party.me.clear_emote()
            await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{args[0]}.{args[0]}')
            await message.reply(f'エモートを {args[0]} に設定')
            client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{args[0]}.{args[0]}'
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0].lower().startswith('toy_'):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.emotelock is True:
                    await message.reply('エモートロックが有効です')
                    return
            elif client.emotelock is True:
                await message.reply('エモートロックが有効です')
                return
            if not data['loglevel'] == 'normal':
                if data['no-logs'] is False:
                    print(args[0])
                dstore(client.user.display_name,args[0])
            if not client.user.party.me.emote is None:
                if client.user.party.me.emote.lower() == args[0].lower():
                    await client.user.party.me.clear_emote()
            await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{args[0]}.{args[0]}')
            await message.reply(f'エモートを {args[0]} に設定')
            client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{args[0]}.{args[0]}'
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0].lower().startswith('playlist_'):
        try:
            await client.user.party.set_playlist(args[0])
            await message.reply(f'プレイリストを {args[0]} に設定')
            data['fortnite']['playlist']=args[0]
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティーリーダーではありません')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    else:
        if ': ' in message.content:
            return
        try:
            if args[0].isdigit() and client.itemdata[0] == 'True':
                if not data['loglevel'] == 'normal':
                    if data['no-logs'] is False:
                        print(client.itemdata[1][int(args[0])-1][0])
                    dstore(client.user.display_name,client.itemdata[1][int(args[0])-1][0])
                if client.itemdata[1][int(args[0])-1][2] == 'outfit':
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.skinlock is True:
                            await message.reply('スキンロックが有効です')
                            return
                    elif client.skinlock is True:
                        await message.reply('スキンロックが有効です')
                        return
                    if 'banner' not in client.itemdata[1][int(args[0])-1][0]:
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.itemdata[1][int(args[0])-1][0]))
                    else:
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.itemdata[1][int(args[0])-1][0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                if client.itemdata[1][int(args[0])-1][2] == 'backpack':
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.baglock is True:
                            await message.reply('バッグロックが有効です')
                            return
                    elif client.baglock is True:
                        await message.reply('バッグロックが有効です')
                        return
                    if 'banner' not in client.itemdata[1][int(args[0])-1][0]:
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.itemdata[1][int(args[0])-1][0]))
                    else:
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.itemdata[1][int(args[0])-1][0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                if client.itemdata[1][int(args[0])-1][2] == 'pet':
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.baglock is True:
                            await message.reply('バッグロックが有効です')
                            return
                    elif client.baglock is True:
                        await message.reply('バッグロックが有効です')
                        return
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.itemdata[1][int(args[0])-1][0]))
                if client.itemdata[1][int(args[0])-1][2] == 'pickaxe':
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.picklock is True:
                            await message.reply('ツルハシロックが有効です')
                            return
                    elif client.picklock is True:
                        await message.reply('ツルハシロックが有効です')
                        return
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.itemdata[1][int(args[0])-1][0]))
                    await client.user.party.me.set_emote('EID_IceKing')
                if client.itemdata[1][int(args[0])-1][2] == 'emote':
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            return
                    elif client.emotelock is True:
                        await message.reply('エモートロックが有効です')
                        return
                    if not client.user.party.me.emote is None:
                        if client.user.party.me.emote.lower() == client.itemdata[1][int(args[0])-1][0].lower():
                            await client.user.party.me.clear_emote()
                    await client.user.party.me.set_emote(client.itemdata[1][int(args[0])-1][0])
                    client.eid=client.itemdata[1][int(args[0])-1][0]
                if client.itemdata[1][int(args[0])-1][2] == 'emoji':
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            return
                    elif client.emotelock is True:
                        await message.reply('エモートロックが有効です')
                        return
                    await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.itemdata[1][int(args[0])-1][0]}.{client.itemdata[1][int(args[0])-1][0]}')
                    client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.itemdata[1][int(args[0])-1][0]}.{client.itemdata[1][int(args[0])-1][0]}'
                if client.itemdata[1][int(args[0])-1][2] == 'toy':
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            return
                    elif client.emotelock is True:
                        await message.reply('エモートロックが有効です')
                        return
                    await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{client.itemdata[1][int(args[0])-1][0]}.{client.itemdata[1][int(args[0])-1][0]}')
                    client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{client.itemdata[1][int(args[0])-1][0]}.{client.itemdata[1][int(args[0])-1][0]}'
                return
        except AttributeError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('有効な数字を入力してください')
            return
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')
            return

        try:
            isitem = await is_itemname("ja", content.replace('\\',''))
            if isitem[0] == 'True':
                client.itemdata = isitem
                if len(client.itemdata[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.itemdata[1])))
                    return
                for count,item in enumerate(client.itemdata[1]):
                    if item[2] == 'outfit':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'スキン: {item[1]}')
                        else:
                            await message.reply(f'{count+1} スキン: {item[1]}')
                    if item[2] == 'backpack':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                    if item[2] == 'pet':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                    if item[2] == 'pickaxe':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'ツルハシ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} ツルハシ: {item[1]}')
                    if item[2] == 'emote':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                    if item[2] == 'emoji':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                    if item[2] == 'toy':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                if len(client.itemdata[1]) == 1:
                    if not data['loglevel'] == 'normal':
                        if data['no-logs'] is False:
                            print(client.itemdata[1][0][0])
                        dstore(client.user.display_name,client.itemdata[1][0][0])
                    if client.itemdata[1][0][2] == 'outfit':
                        if 'banner' not in client.itemdata[1][0][0]:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.itemdata[1][0][0]))
                        else:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.itemdata[1][0][0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                    if client.itemdata[1][0][2] == 'backpack':
                        if 'banner' not in client.itemdata[1][0][0]:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.itemdata[1][0][0]))
                        else:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.itemdata[1][0][0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                    if client.itemdata[1][0][2] == 'pet':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.itemdata[1][0][0]))
                    if client.itemdata[1][0][2] == 'pickaxe':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.itemdata[1][0][0]))
                        await client.user.party.me.set_emote('EID_IceKing')
                    if client.itemdata[1][0][2] == 'emote':
                        if not client.user.party.me.emote is None:
                            if client.user.party.me.emote.lower() == client.itemdata[1][0][0].lower():
                                await client.user.party.me.clear_emote()
                        await client.user.party.me.set_emote(client.itemdata[1][0][0])
                        client.eid=client.itemdata[1][0][0]
                    if client.itemdata[1][0][2] == 'emoji':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}'
                    if client.itemdata[1][0][2] == 'toy':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}'
                if len(client.itemdata[1]) > 1:
                    await message.reply('数字を入力することでそのアイテムに設定します')
                return
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
            return
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')
            return

        try:
            isitem = await is_itemname("en", content.replace('\\',''))
            if isitem[0] == 'True':
                client.itemdata = isitem
                if len(client.itemdata[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.itemdata[1])))
                    return
                for count,item in enumerate(client.itemdata[1]):
                    if item[2] == 'outfit':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'スキン: {item[1]}')
                        else:
                            await message.reply(f'{count+1} スキン: {item[1]}')
                    if item[2] == 'backpack':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                    if item[2] == 'pet':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                    if item[2] == 'pickaxe':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'ツルハシ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} ツルハシ: {item[1]}')
                    if item[2] == 'emote':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                    if item[2] == 'emoji':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                    if item[2] == 'toy':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                if len(client.itemdata[1]) == 1:
                    if not data['loglevel'] == 'normal':
                        if data['no-logs'] is False:
                            print(client.itemdata[1][0][0])
                        dstore(client.user.display_name,client.itemdata[1][0][0])
                    if client.itemdata[1][0][2] == 'outfit':
                        if 'banner' not in client.itemdata[1][0][0]:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.itemdata[1][0][0]))
                        else:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.itemdata[1][0][0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                    if client.itemdata[1][0][2] == 'backpack':
                        if 'banner' not in client.itemdata[1][0][0]:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.itemdata[1][0][0]))
                        else:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.itemdata[1][0][0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                    if client.itemdata[1][0][2] == 'pet':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.itemdata[1][0][0]))
                    if client.itemdata[1][0][2] == 'pickaxe':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.itemdata[1][0][0]))
                        await client.user.party.me.set_emote('EID_IceKing')
                    if client.itemdata[1][0][2] == 'emote':
                        if not client.user.party.me.emote is None:
                            if client.user.party.me.emote.lower() == client.itemdata[1][0][0].lower():
                                await client.user.party.me.clear_emote()
                        await client.user.party.me.set_emote(client.itemdata[1][0][0])
                        client.eid=client.itemdata[1][0][0]
                    if client.itemdata[1][0][2] == 'emoji':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}'
                    if client.itemdata[1][0][2] == 'toy':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}'
                if len(client.itemdata[1]) > 1:
                    await message.reply('数字を入力することでそのアイテムに設定します')
                return
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
            return
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')
            return

#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================

async def event_party_message(message):
    if message is None:
        return
    client=message.client
    if client.isready is False:
        return
    content=message.content
    if data['caseinsensitive'] is True:
        args = jaconv.kata2hira(content.lower()).split()
    else:
        args = content.split()
    rawargs = content.split()
    rawcontent = ' '.join(rawargs[1:])
    rawcontent2 = ' '.join(rawargs[2:])
    user=None
    if not client.owner is None:
        if client.partychat is False and not message.author.id == client.owner.id:
            return
    else:
        if client.partychat is False:
            return
    if rawcontent in commands['me'].split(','):
        rawcontent=str(message.author.display_name)
    client_user_display_name=str(client.user.display_name)
    member_joined_at_most=[client.user.id, client.user.party.me.joined_at]
    for member_ in client.user.party.members.values():
        if member_joined_at_most != []:
            if member_.id in [i.user.id for i in clients]:
                if member_.id != client.user.id and member_.id != message.author.id:
                    client_user_display_name+=f"/{str(member_.display_name)}"
                if member_.joined_at < member_joined_at_most[1]:
                    member_joined_at_most=[member_.id, member_.joined_at]
        else:
            member_joined_at_most=[client.user.id, client.user.party.me.joined_at]
    if client.user.id == member_joined_at_most[0]:
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(f'[{now_()}] [パーティー] [{client_user_display_name}] {message.author.display_name} | {content}')
            dstore(message.author.display_name,f'[{client_user_display_name}] [パーティー] {content}')
        else:
            if data['no-logs'] is False:
                print(f'[{now_()}] [パーティー/{client.user.party.id}] [{client_user_display_name}] {message.author.display_name} / {message.author.id} [{platform_to_str(message.author.platform)}/{message.author.input}] | {content}')
            dstore(f'{message.author.display_name} / {message.author.id} [{platform_to_str(message.author.platform)}/{message.author.input}]',f'[{client_user_display_name}] [パーティー/{client.user.party.id}] {content}')

    if not client.owner is None:
        if not client.owner.id == message.author.id:
            for checks in commands.items():
                ignore=['ownercommands','true','false','me', 'privacy_public', 'privacy_friends_allow_friends_of_friends', 'privacy_friends', 'privacy_private_allow_friends_of_friends', 'privacy_private', 'info_party', 'info_item']
                if checks[0] in ignore:
                    continue
                if commands['ownercommands'] == '':
                    break
                for command in commands['ownercommands'].split(','):
                    if args[0] in commands[command.lower()].split(','):
                        await message.reply('このコマンドは管理者しか使用できません')
                        return

    if args[0] in commands['prev'].split(','):
        if client.prevmessage.get(message.author.id) is None:
            client.prevmessage[message.author.id]='None'
        content=client.prevmessage.get(message.author.id)
        if data['caseinsensitive'] is True:
            args = jaconv.kata2hira(content.lower()).split()
        else:
            args = content.split()
        args = jaconv.kata2hira(content.lower()).split()
        rawargs = content.split()
        rawcontent = ' '.join(rawargs[1:])
        rawcontent2 = ' '.join(rawargs[2:])
    client.prevmessage[message.author.id]=content

    for key,value in replies.items():
        if args[0] in key:
            try:
                await message.reply(value)
            except Exception:
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                await message.reply('エラー')
            return

    if args[0] in commands['eval'].split(','):
        try:
            if rawcontent == "":
                await message.reply(f"[{commands['eval']}] [式]")
                return
            variable=globals()
            variable.update(locals())
            if rawcontent.startswith("await "):
                if data['loglevel'] == "debug":
                    print(f"await eval({rawcontent.replace('await ','',1)})")
                result = await eval(rawcontent.replace("await ","",1), variable)
                await message.reply(str(result))
            else:
                if data['loglevel'] == "debug":
                    print(f"eval {rawcontent}")
                result = eval(rawcontent, variable)
                await message.reply(str(result))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['exec'].split(','):
        try:
            if rawcontent == "":
                await message.reply(f"[{commands['exec']}] [文]")
                return
            variable=globals()
            variable.update(locals())
            variable_prev=variable
            if rawcontent.startswith("await "):
                if data['loglevel'] == "debug":
                    print(f"await exec({rawcontent.replace('await ','',1)})")
                result = await exec(rawcontent.replace("await ","",1), variable)
                await message.reply(str(result))
                for key, value in variable.items():
                    if key not in variable_prev.keys():
                        exec(f"global {key}")
                        exec(f"{key} = {value}")
            else:
                if data['loglevel'] == "debug":
                    print(f"exec {rawcontent}")
                result = exec(rawcontent, variable)
                await message.reply(str(result))
                for key, value in variable.items():
                    if key not in variable_prev.keys():
                        exec(f"global {key}")
                        exec(f"{key} = {value}")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['restart'].split(','):
        try:
            if client.acceptinvite is False and client.owner is None:
                await message.reply('招待が拒否に設定されているので実行できません')
            elif client.acceptinvite is False and not message.author.id == client.owner.id:
                await message.reply('招待が拒否に設定されているので実行できません')
            else:
                await message.reply('プログラムを再起動します...')
                os.chdir(os.getcwd())
                os.execv(os.sys.executable,['python','index.py'])
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['relogin'].split(','):
        try:
            await message.reply('アカウントに再ログインします...')
            await client.restart()
        except fortnitepy.AuthException:
            print(red(traceback.format_exc()))
            print(red(f'[{now_()}] [{client.user.display_name}] メールアドレスまたはパスワードが間違っています。'))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            dstore(client.user.display_name,f'>>> メールアドレスまたはパスワードが間違っています')
            kill=True
            exit()
        except Exception:
            print(red(traceback.format_exc()))
            print(red(f'[{now_()}] [{client.user.display_name}] アカウントの読み込みに失敗しました。もう一度試してみてください。'))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            dstore(client.user.display_name,f'>>> アカウントの読み込みに失敗しました。もう一度試してみてください')
            kill=True
            exit()

    elif args[0] in commands['reload'].split(','):
        result=reload_configs(client)
        try:
            if result == 'Success':
                await message.reply('正常に読み込みが完了しました')
            else:
                await message.reply('エラー')
                return
            client.owner=None
            try:
                owner=await client.fetch_profile(data['fortnite']['owner'])
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
                dstore(client.user.display_name,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if owner is None:
                print(red(f'[{now_()}] [{client.user.display_name}] 所有者が見つかりません。正しい名前/IDになっているか確認してください。'))
                dstore(client.user.display_name,f'>>> 所有者が見つかりません。正しい名前/IDになっているか確認してください')
                return
            client.owner=client.get_friend(owner.id)
            if client.owner is None:
                if data['fortnite']['addfriend'] is True:
                    try:
                        await client.add_friend(owner.id)
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                        print(red(f'[{now_()}] [{client.user.display_name}] フレンド申請の送信リクエストを処理中にエラーが発生しました。'))
                        dstore(client.user.display_name,f'>>> フレンド申請の送信リクエストを処理中にエラーが発生しました')
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] 所有者とフレンドではありません。フレンドになってからもう一度起動してください。'))
                dstore(client.user.display_name,f'>>> 所有者とフレンドではありません。フレンドになってからもう一度起動してください')
                return
            if data['loglevel'] == 'normal':
                print(green(f'[{now_()}] [{client.user.display_name}] 所有者: {client.owner.display_name}'))
                dstore(client.user.display_name,f'所有者: {client.owner.display_name}')
            else:
                print(green(f'[{now_()}] [{client.user.display_name}] 所有者: {client.owner.display_name} / {client.owner.id}'))
                dstore(client.user.display_name,f'所有者: {client.owner.display_name} / {client.owner.id}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['get'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['get']}] [ユーザー名/ユーザーID]")
                return
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            if not user.id in client.user.party.members.keys():
                await message.reply('ユーザーがパーティーにいません')
                return
            member=client.user.party.members.get(user.id)
            if data['no-logs'] is False:
                print(f'{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{member.backpack} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{member.emote}')
            dstore(client.user.display_name,f'{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{member.backpack} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{member.emote}')
            await message.reply(f'{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{member.backpack} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{member.emote}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['friendcount'].split(','):
        try:
            if data['no-logs'] is False:
                print(f'フレンド数: {len(client.friends)}')
            dstore(client.user.display_name,f'フレンド数: {len(client.friends)}')
            await message.reply(f'フレンド数: {len(client.friends)}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['pendingcount'].split(','):
        try:
            outbound = []
            inbound = []
            for pending in client.pending_friends.values():
                if pending.direction == 'OUTBOUND':
                    outbound.append(pending)
                elif pending.direction == 'INBOUND':
                    inbound.append(pending)
            if data['no-logs'] is False:
                print(f'保留数: {len(client.pending_friends)}\n送信: {len(outbound)}\n受信: {len(inbound)}')
            dstore(client.user.display_name,f'保留数: {len(client.pending_friends)}\n送信: {len(outbound)}\n受信: {len(inbound)}')
            await message.reply(f'保留数: {len(client.pending_friends)}\n送信: {len(outbound)}\n受信: {len(inbound)}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['blockcount'].split(','):
        try:
            if data['no-logs'] is False:
                print(f'ブロック数: {len(client.blocked_users)}')
            dstore(client.user.display_name,f'ブロック数: {len(client.blocked_users)}')
            await message.reply(f'ブロック数: {len(client.blocked_users)}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['friendlist'].split(','):
        try:
            text=''
            for friend in client.friends.values():
                text+=f'{friend}\n'
            if data['no-logs'] is False:
                print(f'{text}')
            dstore(client.user.display_name,f'{text}')
            await message.reply(f'{text}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['pendinglist'].split(','):
        try:
            outbound=''
            inbound=''
            for pending in client.pending_friends.values():
                if pending.direction == 'OUTBOUND':
                    outbound+=f'{pending}\n'
                elif pending.direction == 'INBOUND':
                    inbound+=f'{pending}\n'
            if data['no-logs'] is False:
                print(f'送信: {outbound}\n受信: {inbound}')
            dstore(client.user.display_name,f'送信: {outbound}\n受信: {inbound}')
            await message.reply(f'送信: {outbound}\n受信: {inbound}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['blocklist'].split(','):
        try:
            text=''
            for block in client.blocked_users.values():
                text+=f'{block}\n'
            if data['no-logs'] is False:
                print(f'{text}')
            dstore(client.user.display_name,f'{text}')
            await message.reply(f'{text}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['skinmimic'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.skinmimic=True
                await message.reply('スキンミミックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.skinmimic=False
                await message.reply('スキンミミックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['skinmimic']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['emotemimic'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.emotemimic=True
                await message.reply('エモートミミックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.emotemimic=False
                await message.reply('エモートミミックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['emotemimic']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['partychat'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.partychat=True
                await message.reply('パーティーチャットからのコマンド受付をオンに設定')
            elif args[1] in commands['false'].split(','):
                client.partychat=False
                await message.reply('パーティーチャットからのコマンド受付をオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['party']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['acceptinvite'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.acceptinvite=True
                await message.reply('招待を承諾に設定')
            elif args[1] in commands['false'].split(','):
                client.acceptinvite=False
                await message.reply('招待を拒否に設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['acceptinvite']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['acceptfriend'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.acceptfriend=True
                await message.reply('フレンド申請を承諾に設定')
            elif args[1] in commands['false'].split(','):
                client.acceptfriend=False
                await message.reply('フレンド申請を拒否に設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['acceptfriend']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['joinmessageenable'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.joinmessageenable=True
                await message.reply('パーティー参加時のメッセージをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.joinmessageenable=False
                await message.reply('パーティー参加時のメッセージをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['joinmessageenable']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['randommessageenable'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.randommessageenable=True
                await message.reply('パーティー参加時のランダムメッセージをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.randommessageenable=False
                await message.reply('パーティー参加時のランダムメッセージをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['randommessageenable']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['wait'].split(','):
        try:
            if client.owner is None:
                client.acceptinvite=False
                try:
                    client.timer_.cancel()
                except AttributeError:
                    pass
                client.timer_=Timer(data['fortnite']['waitinterval'], inviteaccept, [client])
                client.timer_.start()
                await message.reply(f"{str(data['fortnite']['waitinterval'])}秒間招待を拒否します")
            else:
                if client.owner.id in client.user.party.members.keys() and not message.author.id == client.owner.id:
                    await message.reply('現在利用できません')
                    return
                client.acceptinvite=False
                try:
                    client.timer_.cancel()
                except AttributeError:
                    pass
                client.timer_=Timer(data['fortnite']['waitinterval'], inviteaccept, [client])
                client.timer_.start()
                await message.reply(f"{str(data['fortnite']['waitinterval'])}秒間招待を拒否します")             
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['join'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['join']}] [ユーザー名/ユーザーID]")
                return
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            friend=client.get_friend(user.id)
            if friend is None:
                await message.reply('ユーザーとフレンドではありません')
            else:
                await friend.join_party()
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('既にパーティーのメンバーです')
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティーが見つかりません')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティーがプライベートです')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティーの参加リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['joinid'].split(','):
        try:
            await client.join_to_party(party_id=args[1])
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('既にこのパーティーのメンバーです')
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティーが見つかりません')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティーがプライベートです')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['join']}] [パーティーID]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['leave'].split(','):
        try:
            await client.user.party.me.leave()
            await message.reply('パーティーを離脱')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティー離脱のリクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['invite'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['invite']}] [ユーザー名 / ユーザーID]")
                return
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            friend=client.get_friend(user.id)
            if friend is None:
                await message.reply('ユーザーとフレンドではありません')
                return
            await friend.invite()
            if data['loglevel'] == 'normal':
                await message.reply(f'{str(friend.display_name)} をパーティーに招待')
            else:
                await message.reply(f'{str(friend.display_name)} / {friend.id} をパーティー {client.user.party.id} に招待')
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティーが満員か、既にパーティーにいます')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティー招待の送信リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['message'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['message']}] [ユーザー名 / ユーザーID] : [内容]")
                return
            send=rawcontent.split(' : ')
            try:
                user=await client.fetch_profile(send[0])
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            friend=client.get_friend(user.id)
            if friend is None:
                await message.reply('ユーザーとフレンドではありません')
                return
            await friend.send(send[1])
            if data['loglevel'] == 'normal':
                await message.reply(f'{str(friend.display_name)} にメッセージ {send[1]} を送信')
            else:
                await message.reply(f'{str(friend.display_name)} / {friend.id} にメッセージ {send[1]} を送信')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['message']}] [ユーザー名 / ユーザーID] : [内容]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['partymessage'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['partymessage']}] [内容]")
                return
            await client.user.party.send(rawcontent)
            if data['loglevel'] == 'normal':
                await message.reply(f'パーティーにメッセージ {rawcontent} を送信')
            else:
                await message.reply(f'パーティー {client.user.party.id} にメッセージ {rawcontent} を送信')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['status'].split(','):
        try:
            await client.set_status(rawcontent)
            await message.reply(f'ステータスを {rawcontent} に設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['status']}] [内容]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['banner'].split(','):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_banner,args[1],args[2],client.user.party.me.banner[2]))
            await message.reply(f'バナーを {args[1]}, {args[2]}に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('バナー情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['banner']}] [バナーID] [バナーの色]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['level'].split(','):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_banner,client.user.party.me.banner[0],client.user.party.me.banner[1],int(args[1])))
            await message.reply(f'レベルを {args[1]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('レベルの設定リクエストを処理中にエラーが発生しました')
        except ValueError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('数字を入力してください')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['level']}] [レベル]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['bp'].split(','):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_battlepass_info,True,args[1],args[2],args[3]))
            await message.reply(f'バトルパス情報を ティア: {args[1]} XPブースト: {args[2]} フレンドXPブースト: {args[3]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('バトルパス情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['bp']}] [ティア] [XPブースト] [フレンドXPブースト]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['privacy'].split(','):
        try:
            if args[1] in commands['privacy_public'].split(','):
                await client.user.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)
                await message.reply('プライバシーを パブリック に設定')
            elif args[1] in commands['privacy_friends_allow_friends_of_friends'].split(','):
                await client.user.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS_ALLOW_FRIENDS_OF_FRIENDS)
                await message.reply('プライバシーを フレンド(フレンドのフレンドを許可) に設定')
            elif args[1] in commands['privacy_friends'].split(','):
                await client.user.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS)
                await message.reply('プライバシーを フレンド に設定')
            elif args[1] in commands['privacy_private_allow_friends_of_friends'].split(','):
                await client.user.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE_ALLOW_FRIENDS_OF_FRIENDS)
                await message.reply('プライバシーを プライベート(フレンドのフレンドを許可) に設定')
            elif args[1] in commands['privacy_privacte'].split(','):
                await client.user.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE)
                await message.reply('プライバシーを プライベート に設定')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティーリーダーではありません')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['privacy']}] [[{commands['privacy_public']}] / [{commands['privacy_friends_allow_friends_of_friends']}] / [{commands['privacy_friends']}] / [{commands['privacy_private_allow_friends_of_friends']}] / [{commands['privacy_privacte']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー') 

    elif args[0] in commands['getuser'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['getuser']}] [ユーザー名 / ユーザーID]")
                return
            user=await client.fetch_profile(rawcontent)
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            if data['no-logs'] is False:
                print(f'{str(user.display_name)} / {user.id}')
            dstore(client.user.display_name,f'{str(user.display_name)} / {user.id}')
            await message.reply(f'{str(user.display_name)} / {user.id}')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['getfriend'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['getfriend']}] [ユーザー名 / ユーザーID]")
                return
            user=await client.fetch_profile(rawcontent)
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            friend=client.get_friend(user.id)
            if friend is None:
                await message.reply('ユーザーとフレンドではありません')
                return
            if friend.nickname is None:
                if data['no-logs'] is False:
                    print(f'{str(friend.display_name)} / {friend.id}')
                dstore(client.user.display_name,f'{str(friend.display_name)} / {friend.id}')
                await message.reply(f'{str(friend.display_name)} / {friend.id}')
            else:
                if data['no-logs'] is False:
                    print(f'{friend.nickname}({str(friend.display_name)}) / {friend.id}')
                dstore(client.user.display_name,f'{friend.nickname}({str(friend.display_name)}) / {friend.id}')
                await message.reply(f'{friend.nickname}({str(friend.display_name)}) / {friend.id}')
            if not friend.last_logout is None:
                await message.reply('最後のログイン: {0.year}年{0.month}月{0.day}日 {0.hour}時{0.minute}分{0.second}秒'.format(friend.last_logout))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['getpending'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['getpending']}] [ユーザー名 / ユーザーID]")
                return
            user=await client.fetch_profile(rawcontent)
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            pending=client.get_pending_friend(user.id)
            if pending is None:
                await message.reply('ユーザーからのフレンド申請がありません')
                return
            if data['no-logs'] is False:
                print(f'{str(pending.display_name)} / {pending.id}')
            dstore(client.user.display_name,f'{str(pending.display_name)} / {pending.id}')
            await message.reply(f'{str(pending.display_name)} / {pending.id}')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['getblock'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['getblock']}] [ユーザー名 / ユーザーID]")
                return
            user=await client.fetch_profile(rawcontent)
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            block=client.get_blocked_user(user.id)
            if block is None:
                await message.reply('ユーザーをブロックしていません')
                return
            if data['no-logs'] is False:
                print(f'{str(block.display_name)} / {block.id}')
            dstore(client.user.display_name,f'{str(block.display_name)} / {block.id}')
            await message.reply(f'{str(block.display_name)} / {block.id}')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['info'].split(','):
        try:
            if args[1] in commands['info_party'].split(','):
                if data['no-logs'] is False:
                    print(f'{client.user.party.id}\n人数: {client.user.party.member_count}')
                dstore(client.user.display_name,f'{client.user.party.id}\n人数: {client.user.party.member_count}')
                await message.reply(f'{client.user.party.id}\n人数: {client.user.party.member_count}')
                for member in client.user.party.members.values():
                    if data['loglevel'] == 'normal':
                        print(str(member.display_name))
                        dstore(client.user.display_name,str(member.display_name))
                        await message.reply(str(member.display_name))
                    else:
                        print(f'{str(member.display_name)} / {member.id}')
                        dstore(client.user.display_name,f'{str(member.display_name)} / {member.id}')
                        await message.reply(f'{str(member.display_name)} / {member.id}')
            elif args[1] in commands['info_item'].split(','):
                if rawcontent2 == '':
                    await message.reply(f"[{commands['info']}] [{commands['info_item']}] [アイテム名]")
                    return
                items=await is_itemname('ja', rawcontent2)
                if items[0] == 'True':
                    client.itemdata=items
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                        return
                    for item in items[1]:
                        await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    return
                items=await is_itemname('en', rawcontent2)
                if items[0] == 'True':
                    client.itemdata=items
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                        return
                    for item in items[1]:
                        await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    return
                await message.reply('見つかりません')
            elif args[1] in commands['id'].split(','):
                if rawcontent2 == '':
                    await message.reply(f"[{commands['info']}] [{commands['id']}] [ID]")
                    return
                items=await search_item_with_id('ja', rawcontent2)
                if items[0] == 'True':
                    client.itemdata=items
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                        return
                    for item in items[1]:
                        await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    return
                items=await search_item_with_id('en', rawcontent2)
                if items[0] == 'True':
                    client.itemdata=items
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                        return
                    for item in items[1]:
                        await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    return
                await message.reply('見つかりません')
            elif args[1] in commands['skin'].split(','):
                if rawcontent2 == '':
                    await message.reply(f"[{commands['info']}] [{commands['skin']}] [スキン名]")
                    return
                items=await search_item_with_type('ja', rawcontent2, 'outfit')
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                        return
                    for item in items[1]:
                        await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    return
                items=await search_item_with_type('en', rawcontent2, 'outfit')
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                        return
                    for item in items[1]:
                        await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    return
                await message.reply('見つかりません')
            elif args[1] in commands['bag'].split(','):
                if rawcontent2 == '':
                    await message.reply(f"[{commands['info']}] [{commands['bag']}] [バッグ名]")
                    return
                items=await search_item_with_type('ja', rawcontent2, 'backpack,pet')
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                        return
                    for item in items[1]:
                        await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    return
                items=await search_item_with_type('en', rawcontent2, 'outfit')
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                        return
                    for item in items[1]:
                        await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    return
                await message.reply('見つかりません')
            elif args[1] in commands['pickaxe'].split(','):
                if rawcontent2 == '':
                    return await message.reply(f"[{commands['info']}] [{commands['pickaxe']}] [ツルハシ名]")
                items=await search_item_with_type('ja', rawcontent2, 'pickaxe')
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                        return
                    for item in items[1]:
                        await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    return
                items=await search_item_with_type('en', rawcontent2, 'outfit')
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                        return
                    for item in items[1]:
                        await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    return
                await message.reply('見つかりません')
            elif args[1] in commands['emote'].split(','):
                if rawcontent2 == '':
                    return await message.reply(f"[{commands['info']}] [{commands['emote']}] [エモート名]")
                items=await search_item_with_type('ja', rawcontent2, 'emote,emoji,toy')
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                        return
                    for item in items[1]:
                        await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    return
                items=await search_item_with_type('en', rawcontent2, 'outfit')
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                        return
                    for item in items[1]:
                        await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    return
                await message.reply('見つかりません')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['info']}] [[{commands['info_party']}] / [{commands['info_item']}] / [{commands['id']}] / [{commands['skin']}] / [{commands['bag']}] / [{commands['pickaxe']}] / [{commands['emote']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['pending'].split(','):
        try:
            pendings=[]
            for pending in client.pending_friends.values():
                if pending.direction == 'INBOUND':
                    pendings.append(pending)
            if args[1] in commands['true'].split(','):
                for pending in pendings:
                    try:
                        await pending.accept()
                        if data['loglevel'] == 'normal':
                            await message.reply(f'{str(pending.display_name)} をフレンドに追加')
                        else:
                            await message.reply(f'{str(pending.display_name)} / {pending.id} をフレンドに追加')
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                        if data['loglevel'] == 'normal':
                            await message.reply(f'{str(pending.dispaly_name)} のフレンド申請の承認リクエストを処理中にエラーが発生しました')
                        else:
                            await message.reply(f'{str(pending.display_name)} / {pending.id} のフレンド申請の承認リクエストを処理中にエラーが発生しました')
                        continue
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                        await message.reply('エラー')
                        continue
            elif args[1] in commands['false'].split(','):
                for pending in pendings:
                    try:
                        await pending.decline()
                        if data['loglevel'] == 'normal':
                            await message.reply(f'{str(pending.display_name)} のフレンド申請を拒否')
                        else:
                            await message.reply(f'{str(pending.display_name)} / {pending.id} のフレンド申請を拒否')
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                        if data['loglevel'] == 'normal':
                            await message.reply(f'{str(pending.display_name)} のフレンド申請の拒否リクエストを処理中にエラーが発生しました')
                        else:
                            await message.reply(f'{str(pending.display_name)} / {pending.id} のフレンド申請の拒否リクエストを処理中にエラーが発生しました')
                        continue
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                        await message.reply('エラー')
                        continue
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['pending']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['removepending'].split(','):
        try:
            pendings=[]
            for pending in client.pending_friends.values():
                if pending.direction == 'OUTBOUND':
                    pendings.append(pending)
            for pending in pendings:
                try:
                    await pending.decline()
                    if data['loglevel'] == 'normal':
                        await message.reply(f'{str(pending.display_name)} へのフレンド申請を解除')
                    else:
                        await message.reply(f'{str(pending.display_name)} / {pending.id} へのフレンド申請を解除')
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                    if data['loglevel'] == 'normal':
                        await message.reply(f'{str(pending.display_name)} へのフレンド申請を解除リクエストを処理中にエラーが発生しました')
                    else:
                        await message.reply(f'{str(pending.display_name)} / {pending.id} へのフレンド申請を解除リクエストを処理中にエラーが発生しました')
                    continue
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                    await message.reply('エラー')
                    continue
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['addfriend'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['addfriend']}] [ユーザー名 / ユーザーID]")
                return
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            if client.has_friend(user.id) is True:
                await message.reply('既にユーザーとフレンドです')
                return
            await client.add_friend(user.id)
            if data['loglevel'] == 'normal':
                await message.reply(f'{str(user.display_name)} にフレンド申請を送信')
            else:
                await message.reply(f'{str(user.display_name)} / {user.id} にフレンド申請を送信')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('フレンド申請の送信リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['removefriend'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['removefriend']}] [ユーザー名 / ユーザーID]")
                return
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            if client.has_friend(user.id) is False:
                await message.reply('ユーザーとフレンドではありません')
                return
            await client.remove_or_decline_friend(user.id)
            if data['loglevel'] == 'normal':
                await message.reply(f'{str(user.display_name)} をフレンドから削除')
            else:
                await message.reply(f'{str(user.display_name)} / {user.id} をフレンドから削除')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('フレンドの削除リクエストを処理中にエラーが発生しました')    
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['acceptpending'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['acceptpending']}] [ユーザー名 / ユーザーID]")
                return
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            if client.is_pending(user.id) is False:
                await message.reply('ユーザーからのフレンド申請がありません')
                return
            await client.accept_friend(user.id)
            if data['loglevel'] == 'normal':
                await message.reply(f'{str(user.display_name)} をフレンドに追加')
            else:
                await message.reply(f'{str(user.display_name)} / {user.id} をフレンドに追加')       
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('フレンドの追加リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['declinepending'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['declinepending']}] [ユーザー名 / ユーザーID]")
                return
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            if client.is_pending(user.id) is False:
                await message.reply('ユーザーからのフレンド申請がありません')
                return
            await client.remove_or_decline_friend(user.id)
            if data['loglevel'] == 'normal':
                await message.reply(f'{str(user.display_name)} のフレンド申請を拒否')
            else:
                await message.reply(f'{str(user.display_name)} / {user.id} のフレンド申請を拒否')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('フレンド申請の拒否リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['blockfriend'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['blockfriend']}] [ユーザー名 / ユーザーID]")
                return
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            if user.id in client.blocked_users.keys():
                await message.reply('既にユーザーをブロックしています')
                return
            await client.block_user(user.id)
            if user.display_name is None:
                await message.reply(f'None / {user.id} をブロック')
            if data['loglevel'] == 'normal':
                await message.reply(f'{str(user.display_name)} をブロック')
            else:
                await message.reply(f'{str(user.display_name)} / {user.id} をブロック')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('フレンドのブロックリクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['unblockfriend'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['unblockfriend']}] [ユーザー名 / ユーザーID]")
                return
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            if not user.id in client.blocked_users.keys():
                await message.reply('ユーザーをブロックしていません')
                return
            await client.unblock_user(user.id)
            if data['loglevel'] == 'normal':
                await message.reply(f'{str(user.display_name)} をブロック解除')
            else:
                await message.reply(f'{str(user.display_name)} / {user.id} をブロック解除')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('ブロックしたユーザーのブロック解除リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['chatban'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['chatban']}] [ユーザー名 / ユーザーID] : [理由(任意)]")
                return
            reason=rawcontent.split(' : ')
            try:
                user=await client.fetch_profile(reason[0])
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            if not user.id in client.user.party.members.keys():
                await message.reply('ユーザーがパーティーにいません')
                return
            member=client.user.party.members.get(user.id)
            try:
                await member.chatban(reason[1])
            except IndexError:
                await member.chatban()
            if data['loglevel'] == 'normal':
                await message.reply(f'{str(user.display_name)} をバン')
            else:
                await message.reply(f'{str(user.display_name)} / {user.id} をバン')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティーリーダーではありません')
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('メンバーが見つかりません')
        except ValueError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('既にバンされています')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['promote'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['promote']}] [ユーザー名 / ユーザーID]")
                return
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            if not user.id in client.user.party.members.keys():
                await message.reply('ユーザーがパーティーにいません')
                return
            member=client.user.party.members.get(user.id)
            await member.promote()
            if data['loglevel'] == 'normal':
                await message.reply(f'{str(user.display_name)} に譲渡')
            else:
                await message.reply(f'{str(user.display_name)} / {user.id} に譲渡')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティーリーダーではありません')
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('既にパーティーリーダーです')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティーリーダーの譲渡リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['kick'].split(','):
        try:
            if rawcontent == '':
                await message.reply(f"[{commands['kick']}] [ユーザー名 / ユーザーID]")
                return
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
                return
            if not user.id in client.user.party.members.keys():
                await message.reply('ユーザーがパーティーにいません')
                return
            member=client.user.party.members.get(user.id)
            await member.kick()
            if data['loglevel'] == 'normal':
                await message.reply(f'{str(user.display_name)} をキック')
            else:
                await message.reply(f'{str(user.display_name)} / {user.id} をキック')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティーリーダーではありません')
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('自分をキックすることはできません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティーメンバーのキックリクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['ready'].split(','):
        try:
            await client.user.party.me.set_ready(fortnitepy.ReadyState.READY)
            await message.reply('準備状態を 準備OK に設定')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['unready'].split(','):
        try:
            await client.user.party.me.set_ready(fortnitepy.ReadyState.NOT_READY)
            await message.reply('準備状態を 準備中 に設定')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['sitout'].split(','):
        try:
            await client.user.party.me.set_ready(fortnitepy.ReadyState.SITTING_OUT)
            await message.reply('準備状態を 欠場中 に設定')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['skinlock'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.skinlock=True
                await message.reply('スキンロックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.skinlock=False
                await message.reply('スキンロックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['skinlock']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['baglock'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.baglock=True
                await message.reply('バッグロックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.baglock=False
                await message.reply('バッグロックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['skinlock']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['picklock'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.picklock=True
                await message.reply('ツルハシロックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.picklock=False
                await message.reply('ツルハシロックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['skinlock']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['emotelock'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.emotelock=True
                await message.reply('エモートロックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.emotelock=False
                await message.reply('エモートロックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['skinlock']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['stop'].split(','):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.emotelock is True:
                    await message.reply('エモートロックが有効です')
                    return
            elif client.emotelock is True:
                await message.reply('エモートロックが有効です')
                return
            client.stopcheck=True
            await client.user.party.me.clear_emote()
            await message.reply('停止しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['allskin'].split(','):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.skinlock is True:
                    await message.reply('スキンロックが有効です')
                    return
            elif client.skinlock is True:
                await message.reply('スキンロックが有効です')
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allskin = json.load(f)
            for item in allskin['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type'] == 'outfit':
                    if 'banner' not in item['id']:
                        await client.user.party.me.set_outfit(item['id'])
                    else:
                        await client.user.party.me.set_outfit(item['id'],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner'))
                    await asyncio.sleep(2)
            await message.reply('全てのスキンを表示し終わりました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['allemote'].split(','):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.emotelock is True:
                    await message.reply('エモートロックが有効です')
                    return
            elif client.emotelock is True:
                await message.reply('エモートロックが有効です')
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allemote = json.load(f)
            for item in allemote['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type'] == 'emote':
                    await client.user.party.me.set_emote(item['id'])
                    await asyncio.sleep(5)
            else:
                await message.reply('全てのエモートを表示し終わりました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['setstyle'].split(','):
        if rawcontent2 == '':
            await message.reply(f"[{commands['setstyle']}] [[{commands['skin']}] / [{commands['bag']}] / [{commands['pickaxe']}]] [スタイル名]")
            return
        try:
            if args[1] in commands['skin']:
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.skinlock is True:
                        await message.reply('スキンロックが有効です')
                        return
                elif client.skinlock is True:
                    await message.reply('スキンロックが有効です')
                    return
                variants=await search_style("ja", rawcontent2, client.user.party.me.outfit)
                if variants is None:
                    variants=await search_style("en", rawcontent2, client.user.party.me.outfit)
                if not variants is None:
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.user.party.me.outfit,variants=variants))
                else:
                    await message.reply('見つかりません')
            elif args[1] in commands['bag']:
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.baglock is True:
                        await message.reply('バッグロックが有効です')
                        return
                elif client.baglock is True:
                    await message.reply('バッグロックが有効です')
                    return
                variants=await search_style("ja", rawcontent2, client.user.party.me.backpack)
                if variants is None:
                    variants=await search_style("en", rawcontent2, client.user.party.me.backpack)
                if not variants is None:
                    if client.user.party.me.backpack.lower().startswith('bid_'):
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.user.party.me.backpack,variants=variants))
                    elif client.user.party.me.backpack.lower().startswith('petcarrier_'):
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.user.party.me.backpack,variants=variants))
                else:
                    await message.reply('見つかりません')
            elif args[1] in commands['pickaxe']:
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.picklock is True:
                        await message.reply('ツルハシロックが有効です')
                        return
                elif client.picklock is True:
                    await message.reply('ツルハシロックが有効です')
                    return
                variants=await search_style("ja", rawcontent2, client.user.pickaxe)
                if variants is None:
                    variants=await search_style("en", rawcontent2, client.user.party.me.pickaxe)
                if not variants is None:
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.user.party.me.pickaxe,variants=variants))
                else:
                    await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['setstyle']}] [[{commands['skin']}] / [{commands['bag']}] / [{commands['pickaxe']}]] [スタイル名]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['addstyle'].split(','):
        if rawcontent2 == '':
            await message.reply(f"[{commands['addstyle']}] [[{commands['skin']}] / [{commands['bag']}] / [{commands['pickaxe']}]] [スタイル名]")
            return
        try:
            if args[1] in commands['skin']:
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.skinlock is True:
                        await message.reply('スキンロックが有効です')
                        return
                elif client.skinlock is True:
                    await message.reply('スキンロックが有効です')
                    return
                variants=await search_style("ja", rawcontent2, client.user.party.me.outfit)
                if variants is None:
                    variants=await search_style("en", rawcontent2, client.user.party.me.outfit)
                if not variants is None:
                    for val in client.user.party.me.outfit_variants:
                        variants.append({'item': val['item'], 'channel': val['channel'], 'variant': val['variant']})
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.user.party.me.outfit,variants=variants))
                else:
                    await message.reply('見つかりません')
            elif args[1] in commands['bag']:
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.baglock is True:
                        await message.reply('バッグロックが有効です')
                        return
                elif client.baglock is True:
                    await message.reply('バッグロックが有効です')
                    return
                variants=await search_style("ja", rawcontent2, client.user.party.me.backpack)
                if variants is None:
                    variants=await search_style("en", rawcontent2, client.user.party.me.backpack)
                for val in client.user.party.me.backpack_variants:
                    variants.append({'item': val['item'], 'channel': val['channel'], 'variant': val['variant']})
                if not variants is None:
                    if client.user.party.me.backpack.lower().startswith('bid_'):
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.user.party.me.backpack,variants=variants))
                    elif client.user.party.me.backpack.lower().startswith('petcarrier_'):
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.user.party.me.backpack,variants=variants))
                else:
                    await message.reply('見つかりません')
            elif args[1] in commands['pickaxe']:
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.picklock is True:
                        await message.reply('ツルハシロックが有効です')
                        return
                elif client.picklock is True:
                    await message.reply('ツルハシロックが有効です')
                    return
                variants=await search_style("ja", rawcontent2, client.user.pickaxe)
                if variants is None:
                    variants=await search_style("en", rawcontent2, client.user.party.me.pickaxe)
                if not variants is None:
                    for val in client.user.party.me.pickaxe_variants:
                        variants.append({'item': val['item'], 'channel': val['channel'], 'variant': val['variant']})
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.user.party.me.pickaxe,variants=variants))
                else:
                    await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['addstyle']}] [[{commands['skin']}] / [{commands['bag']}] / [{commands['pickaxe']}]] [スタイル名]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['setenlightenment'].split(','):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.skinlock is True:
                    await message.reply('スキンロックが有効です')
                    return
            elif client.skinlock is True:
                await message.reply('スキンロックが有効です')
                return
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.user.party.me.outfit,variants=client.user.party.me.outfit_variants,enlightenment=(args[1],args[2])))
            await message.reply(f'{args[1]}, {args[2]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['setenlightenment']}] [数値] [数値]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['id'].split(','):
        if rawcontent == '':
            await message.reply(f"[{commands['id']}] [ID]")
            return
        try:
            isitem = await search_item_with_id("ja", rawcontent)
            if isitem[0] == 'True':
                client.itemdata=isitem
                if len(client.itemdata[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.itemdata[1])))
                    return
                for count,item in enumerate(client.itemdata[1]):
                    if item[2] == 'outfit':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'スキン: {item[0]}: {item[1]}')
                        else:
                            await message.reply(f'{count+1} スキン: {item[0]}: {item[1]}')
                    if item[2] == 'backpack':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'バッグ: {item[0]}: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[0]}: {item[1]}')
                    if item[2] == 'pet':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'バッグ: {item[0]}: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[0]}: {item[1]}')
                    if item[2] == 'pickaxe':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'ツルハシ: {item[0]}: {item[1]}')
                        else:
                            await message.reply(f'{count+1} ツルハシ: {item[0]}: {item[1]}')
                    if item[2] == 'emote':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[0]}: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[0]}: {item[1]}')
                    if item[2] == 'emoji':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[0]}: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[0]}: {item[1]}')
                    if item[2] == 'toy':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[0]}: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[0]}: {item[1]}')
                if len(client.itemdata[1]) == 1:
                    if not data['loglevel'] == 'normal':
                        if data['no-logs'] is False:
                            print(client.itemdata[1][0][0])
                        dstore(client.user.display_name,client.itemdata[1][0][0])
                    if client.itemdata[1][0][2] == 'outfit':
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.skinlock is True:
                                await message.reply('スキンロックが有効です')
                                return
                        elif client.skinlock is True:
                            await message.reply('スキンロックが有効です')
                            return
                        if 'banner' not in client.itemdata[1][0][0]:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.itemdata[1][0][0]))
                        else:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.itemdata[1][0][0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                    if client.itemdata[1][0][2] == 'backpack':
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.baglock is True:
                                await message.reply('バッグロックが有効です')
                                return
                        elif client.baglock is True:
                            await message.reply('バッグロックが有効です')
                            return
                        if 'banner' not in client.itemdata[1][0][0]:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.itemdata[1][0][0]))
                        else:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.itemdata[1][0][0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                    if client.itemdata[1][0][2] == 'pet':
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.baglock is True:
                                await message.reply('バッグロックが有効です')
                                return
                        elif client.baglock is True:
                            await message.reply('バッグロックが有効です')
                            return
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.itemdata[1][0][0]))
                    if client.itemdata[1][0][2] == 'pickaxe':
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.picklock is True:
                                await message.reply('ツルハシロックが有効です')
                                return
                        elif client.picklock is True:
                            await message.reply('ツルハシロックが有効です')
                            return
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.itemdata[1][0][0]))
                        if not client.user.party.me.emote is None:
                            if client.user.party.me.emote.lower() == 'eid_iceking':
                                await client.user.party.me.clear_emote()
                        await client.user.party.me.set_emote('EID_IceKing')
                    if client.itemdata[1][0][2] == 'emote':
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.emotelock is True:
                                await message.reply('エモートロックが有効です')
                                return
                        elif client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            return
                        if not client.user.party.me.emote is None:
                            if client.user.party.me.emote.lower() == client.itemdata[1][0][0].lower():
                                await client.user.party.me.clear_emote()
                        await client.user.party.me.set_emote(client.itemdata[1][0][0])
                        client.eid=client.itemdata[1][0][0]
                    if client.itemdata[1][0][2] == 'emoji':
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.emotelock is True:
                                await message.reply('エモートロックが有効です')
                                return
                        elif client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            return
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}'
                    if client.itemdata[1][0][2] == 'toy':
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.emotelock is True:
                                await message.reply('エモートロックが有効です')
                                return
                        elif client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            return
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}'
                if len(client.itemdata[1]) > 1:
                    await message.reply('数字を入力することでそのアイテムに設定します')
            else:
                await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['skin'].split(','):
        if rawcontent == '':
            await message.reply(f"[{commands['skin']}] [スキン名]")
            return
        try:
            isitem = await search_item_with_type("ja", rawcontent, "outfit")
            if isitem[0] == 'True':
                client.itemdata=isitem
                if len(client.itemdata[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.itemdata[1])))
                    return
                for count,item in enumerate(client.itemdata[1]):
                    if len(client.itemdata[1]) == 1:
                        await message.reply(f'{item[1]}')
                    else:
                        await message.reply(f'{count+1}: {item[1]}')
                if len(client.itemdata[1]) == 1:
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.skinlock is True:
                            await message.reply('スキンロックが有効です')
                            return
                    elif client.skinlock is True:
                        await message.reply('スキンロックが有効です')
                        return
                    if not data['loglevel'] == 'normal':
                        if data['no-logs'] is False:
                            print(client.itemdata[1][0][0])
                        dstore(client.user.display_name,client.itemdata[1][0][0])
                    if 'banner' not in client.itemdata[1][0][0]:
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.itemdata[1][0][0]))
                    else:
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.itemdata[1][0][0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                if len(client.itemdata[1]) > 1:
                    await message.reply('数字を入力することでそのアイテムに設定します')
                return
            isitem = await search_item_with_type("en", rawcontent, "outfit")
            if isitem[0] == 'True':
                client.itemdata=isitem
                if len(client.itemdata[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.itemdata[1])))
                    return
                for count,item in enumerate(client.itemdata[1]):
                    if len(client.itemdata[1]) == 1:
                        await message.reply(f'{item[1]}')
                    else:
                        await message.reply(f'{count+1}: {item[1]}')
                if len(client.itemdata[1]) == 1:
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.skinlock is True:
                            await message.reply('スキンロックが有効です')
                            return
                    elif client.skinlock is True:
                        await message.reply('スキンロックが有効です')
                        return
                    if not data['loglevel'] == 'normal':
                        if data['no-logs'] is False:
                            print(client.itemdata[1][0][0])
                        dstore(client.user.display_name,client.itemdata[1][0][0])
                    if 'banner' not in client.itemdata[1][0][0]:
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.itemdata[1][0][0]))
                    else:
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.itemdata[1][0][0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                if len(client.itemdata[1]) > 1:
                    await message.reply('数字を入力することでそのアイテムに設定します')
                return
            await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['bag'].split(','):
        if rawcontent == '':
            await message.reply(f"[{commands['bag']}] [バッグ名]")
            return
        try:
            isitem = await search_item_with_type("ja", rawcontent, "backpack,pet")
            if isitem[0] == 'True':
                client.itemdata=isitem
                if len(client.itemdata[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.itemdata[1])))
                    return
                for count,item in enumerate(client.itemdata[1]):
                    if len(client.itemdata[1]) == 1:
                        await message.reply(f'{item[1]}')
                    else:
                        await message.reply(f'{count+1}: {item[1]}')
                if len(client.itemdata[1]) == 1:
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.baglock is True:
                            await message.reply('バッグロックが有効です')
                            return
                    elif client.baglock is True:
                        await message.reply('バッグロックが有効です')
                        return
                    if not data['loglevel'] == 'normal':
                        if data['no-logs'] is False:
                            print(client.itemdata[1][0][0])
                        dstore(client.user.display_name,client.itemdata[1][0][0])
                    if client.itemdata[1][0][2] == 'backpack':
                        if 'banner' not in client.itemdata[1][1][0]:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.itemdata[1][0][0]))
                        else:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.itemdata[1][0][0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                    if client.itemdata[1][0][2] == 'pet':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.itemdata[1][0][0]))
                if len(client.itemdata[1]) > 1:
                    await message.reply('数字を入力することでそのアイテムに設定します')
                return
            isitem = await search_item_with_type("en", rawcontent, "backpack,pet")
            if isitem[0] == 'True':
                client.itemdata=isitem
                if len(client.itemdata[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.itemdata[1])))
                else:
                    for count,item in enumerate(client.itemdata[1]):
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'{item[1]}')
                        else:
                            await message.reply(f'{count+1}: {item[1]}')
                    if len(client.itemdata[1]) == 1:
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.baglock is True:
                                await message.reply('バッグロックが有効です')
                                return
                        elif client.baglock is True:
                            await message.reply('バッグロックが有効です')
                            return
                        if not data['loglevel'] == 'normal':
                            if data['no-logs'] is False:
                                print(client.itemdata[1][0][0])
                            dstore(client.user.display_name,client.itemdata[1][0][0])
                        if client.itemdata[1][0][2] == 'backpack':
                            if 'banner' not in client.itemdata[1][0][0]:
                                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.itemdata[1][0][0]))
                            else:
                                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.itemdata[1][0][0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                        if client.itemdata[1][0][2] == 'pet':
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.itemdata[1][0][0]))
                    if len(client.itemdata[1]) > 1:
                        await message.reply('数字を入力することでそのアイテムに設定します')
                return
            await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['pickaxe'].split(','):
        if rawcontent == '':
            await message.reply(f"[{commands['pickaxe']}] [ツルハシ名]")
            return
        try:
            isitem = await search_item_with_type("ja", rawcontent, "pickaxe")
            if isitem[0] == 'True':
                client.itemdata=isitem
                if len(client.itemdata[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.itemdata[1])))
                    return
                for count,item in enumerate(client.itemdata[1]):
                    if len(client.itemdata[1]) == 1:
                        await message.reply(f'{item[1]}')
                    else:
                        await message.reply(f'{count+1}: {item[1]}')
                if len(client.itemdata[1]) == 1:
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.picklock is True:
                            await message.reply('ツルハシロックが有効です')
                            return
                    elif client.picklock is True:
                        await message.reply('ツルハシロックが有効です')
                        return
                    if not data['loglevel'] == 'normal':
                        if data['no-logs'] is False:
                            print(client.itemdata[1][0][0])
                        dstore(client.user.display_name,client.itemdata[1][0][0])
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.itemdata[1][0][0]))
                    if not client.user.party.me.emote is None:
                        if client.user.party.me.emote.lower() == 'eid_iceking':
                            await client.user.party.me.clear_emote()
                    await client.user.party.me.set_emote('EID_IceKing')
                if len(client.itemdata[1]) > 1:
                    await message.reply('数字を入力することでそのアイテムに設定します')
                return
            isitem = await search_item_with_type("en", rawcontent, "pickaxe")
            if isitem[0] == 'True':
                client.itemdata=isitem
                if len(client.itemdata[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.itemdata[1])))
                    return
                for count,item in enumerate(client.itemdata[1]):
                    if len(client.itemdata[1]) == 1:
                        await message.reply(f'{item[1]}')
                    else:
                        await message.reply(f'{count+1}: {item[1]}')
                if len(client.itemdata[1]) == 1:
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.picklock is True:
                            await message.reply('ツルハシロックが有効です')
                            return
                    elif client.picklock is True:
                        await message.reply('ツルハシロックが有効です')
                        return
                    if not data['loglevel'] == 'normal':
                        if data['no-logs'] is False:
                            print(client.itemdata[1][0][0])
                        dstore(client.user.display_name,client.itemdata[1][0][0])
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.itemdata[1][0][0]))
                    await client.user.party.me.set_emote('EID_IceKing')
                if len(client.itemdata[1]) > 1:
                    await message.reply('数字を入力することでそのアイテムに設定します')
                return
            await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['emote'].split(','):
        if rawcontent == '':
            await message.reply(f"[{commands['emote']}] [エモート名]]")
            return
        try:
            isitem = await search_item_with_type("ja", rawcontent, "emote,emoji,toy")
            if isitem[0] == 'True':
                client.itemdata=isitem
                if len(client.itemdata[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.itemdata[1])))
                    return
                for count,item in enumerate(client.itemdata[1]):
                    if len(client.itemdata[1]) == 1:
                        await message.reply(f'{item[1]}')
                    else:
                        await message.reply(f'{count+1}: {item[1]}')
                if len(client.itemdata[1]) == 1:
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            return
                    elif client.emotelock is True:
                        await message.reply('エモートロックが有効です')
                        return
                    if not data['loglevel'] == 'normal':
                        if data['no-logs'] is False:
                            print(client.itemdata[1][0][0])
                        dstore(client.user.display_name,client.itemdata[1][0][0])
                    if client.itemdata[1][0][2] == 'emote':
                        await client.user.party.me.set_emote(client.itemdata[1][0][0])
                        client.eid=client.itemdata[1][0][0]
                    if client.itemdata[1][0][2] == 'emoji':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}'
                    if client.itemdata[1][0][2] == 'toy':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}'
                if len(client.itemdata[1]) > 1:
                    await message.reply('数字を入力することでそのアイテムに設定します')
                return
            isitem = await search_item_with_type("en", rawcontent, "emote,emoji,toy")
            if isitem[0] == 'True':
                client.itemdata=isitem
                if len(client.itemdata[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.itemdata[1])))
                    return
                for count,item in enumerate(client.itemdata[1]):
                    if len(client.itemdata[1]) == 1:
                        await message.reply(f'{item[1]}')
                    else:
                        await message.reply(f'{count+1}: {item[1]}')
                if len(client.itemdata[1]) == 1:
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            return
                    elif client.emotelock is True:
                        await message.reply('エモートロックが有効です')
                        return
                    if not data['loglevel'] == 'normal':
                        if data['no-logs'] is False:
                            print(client.itemdata[1][0][0])
                        dstore(client.user.display_name,client.itemdata[1][0][0])
                    if client.itemdata[1][0][2] == 'emote':
                        await client.user.party.me.set_emote(client.itemdata[1][0][0])
                        client.eid=client.itemdata[1][0][0]
                    if client.itemdata[1][0][2] == 'emoji':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}'
                    if client.itemdata[1][0][2] == 'toy':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}'
                if len(client.itemdata[1]) > 1:
                    await message.reply('数字を入力することでそのアイテムに設定します')
                return
            await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['set'].split(','):
        if rawcontent == '':
            await message.reply(f"[{commands['set']}] [セット名]]")
            return
        try:
            isitem = await search_set_item("ja", rawcontent)
            if isitem[0] == 'True':
                client.itemdata=isitem
                for count,item in enumerate(client.itemdata[1]):
                    if not data['loglevel'] == 'normal':
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    if item[2] == 'outfit':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'スキン: {item[1]}')
                        else:
                            await message.reply(f'{count+1} スキン: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.skinlock is True:
                                await message.reply('スキンロックが有効です')
                                continue
                        elif client.skinlock is True:
                            await message.reply('スキンロックが有効です')
                            continue
                        if 'banner' not in item[0]:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,item[0]))
                        else:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,item[0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                    if item[2] == 'backpack':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.baglock is True:
                                await message.reply('バッグロックが有効です')
                                continue
                        elif client.baglock is True:
                            await message.reply('バッグロックが有効です')
                            continue
                        if 'banner' not in item[0]:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,item[0]))
                        else:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,item[0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                    if item[2] == 'pet':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.baglock is True:
                                await message.reply('バッグロックが有効です')
                                continue
                        elif client.baglock is True:
                            await message.reply('バッグロックが有効です')
                            continue
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,item[0]))
                    if item[2] == 'pickaxe':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'ツルハシ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} ツルハシ: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.picklock is True:
                                await message.reply('ツルハシロックが有効です')
                                continue
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,item[0]))
                        await client.user.party.me.set_emote('EID_IceKing')
                    if item[2] == 'emote':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.emotelock is True:
                                await message.reply('エモートロックが有効です')
                                continue
                        elif client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            continue
                        await client.user.party.me.set_emote(item[0])
                        client.eid=item[0]
                    if item[2] == 'emoji':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.emotelock is True:
                                await message.reply('エモートロックが有効です')
                                continue
                        elif client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            continue
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{item[0]}.{item[0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{item[0]}.{item[0]}'
                    if item[2] == 'toy':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.emotelock is True:
                                await message.reply('エモートロックが有効です')
                                continue
                        elif client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            continue
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{item[0]}.{item[0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{item[0]}.{item[0]}'
                return
            isitem = await search_set_item("en", rawcontent)
            if isitem[0] == 'True':
                client.itemdata=isitem
                for count,item in enumerate(client.itemdata[1]):
                    if not data['loglevel'] == 'normal':
                        if data['no-logs'] is False:
                            print(item[0])
                        dstore(client.user.display_name,item[0])
                    if item[2] == 'outfit':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'スキン: {item[1]}')
                        else:
                            await message.reply(f'{count+1} スキン: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.skinlock is True:
                                await message.reply('スキンロックが有効です')
                                continue
                        elif client.skinlock is True:
                            await message.reply('スキンロックが有効です')
                            continue
                        if 'banner' not in item[0]:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,item[0]))
                        else:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,item[0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                    if item[2] == 'backpack':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.baglock is True:
                                await message.reply('バッグロックが有効です')
                                continue
                        elif client.baglock is True:
                            await message.reply('バッグロックが有効です')
                            continue
                        if 'banner' not in item[0]:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,item[0]))
                        else:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,item[0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                    if item[2] == 'pet':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.baglock is True:
                                await message.reply('バッグロックが有効です')
                                continue
                        elif client.baglock is True:
                            await message.reply('バッグロックが有効です')
                            continue
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,item[0]))
                    if item[2] == 'pickaxe':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'ツルハシ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} ツルハシ: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.picklock is True:
                                await message.reply('ツルハシロックが有効です')
                                continue
                        elif client.picklock is True:
                            await message.reply('ツルハシロックが有効です')
                            continue
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,item[0]))
                        await client.user.party.me.set_emote('EID_IceKing')
                    if item[2] == 'emote':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.emotelock is True:
                                await message.reply('エモートロックが有効です')
                                continue
                        elif client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            continue
                        await client.user.party.me.set_emote(item[0])
                        client.eid=item[0]
                    if item[2] == 'emoji':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.emotelock is True:
                                await message.reply('エモートロックが有効です')
                                continue
                        elif client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            continue
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{item[0]}.{item[0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{item[0]}.{item[0]}'
                    if item[2] == 'toy':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                        if not client.owner is None:
                            if not client.owner.id == message.author.id and client.emotelock is True:
                                await message.reply('エモートロックが有効です')
                                continue
                        elif client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            continue
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{item[0]}.{item[0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{item[0]}.{item[0]}'
                return
            await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['setvariant'].split(','):
        try:
            variantdict={}
            for count,text in enumerate(args[2:]):
                if count % 2 != 0:
                    continue
                try:
                    variantdict[text]=args[count+3]
                except IndexError:
                    break
            if args[1].startswith('cid_'):
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.skinlock is True:
                        await message.reply('スキンロックが有効です')
                        return
                elif client.skinlock is True:
                    await message.reply('スキンロックが有効です')
                    return
                if 'banner' not in args[1]:
                    variants=client.user.party.me.create_variants(item='AthenaCharacter',**variantdict)
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,asset=args[1],variants=variants))
                else:
                    variantdict['profile_banner']='ProfileBanner'
                    variants=client.user.party.me.create_variants(item='AthenaCharacter',**variantdict)
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,asset=args[1],variants=variants))
                await message.reply(f'スキンを {args[1]} {variants} に設定')
            elif args[1].startswith('bid_'):
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.baglock is True:
                        await message.reply('バッグロックが有効です')
                        return
                elif client.baglock is True:
                    await message.reply('バッグロックが有効です')
                    return
                if 'banner' not in args[1]:
                    variants=client.user.party.me.create_variants(item='AthenaBackpack',**variantdict)
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,asset=args[1],variants=variants))
                else:
                    variantdict['profile_banner']='ProfileBanner'
                    variants=client.user.party.me.create_variants(item='AthenaBackpack',**variantdict)
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,asset=args[1],variants=variants))
                await message.reply(f'バッグを {args[1]} {variants} に設定')
            elif args[1].startswith('petcarrier_'):
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.baglock is True:
                        await message.reply('バッグロックが有効です')
                        return
                elif client.baglock is True:
                    await message.reply('バッグロックが有効です')
                    return
                variants=client.user.party.me.create_variants(item='AthenaBackpack',**variantdict)
                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,asset=args[1],variants=variants))
                await message.reply(f'バッグを {args[1]} {variants} に設定')
            elif args[1].startswith('pickaxe_id_'):
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.picklock is True:
                        await message.reply('ツルハシロックが有効です')
                        return
                elif client.picklock is True:
                    await message.reply('ツルハシロックが有効です')
                    return
                variants=client.user.party.me.create_variants(item='AthenaPickaxe',**variantdict)
                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,asset=args[1],variants=variants))
                await client.user.party.me.set_emote('EID_IceKing')
                await message.reply(f'ツルハシを {args[1]} {variants} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['setvariant']}] [ID] [variant] [数値]\nvariantと数値は無限に設定可能")
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['addvariant'].split(','):
        try:
            variantdict={}
            for count,text in enumerate(args[2:]):
                if count % 2 != 0:
                    continue
                try:
                    variantdict[text]=args[count+3]
                except IndexError:
                    break
            if args[1].startswith('cid_'):
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.skinlock is True:
                        await message.reply('スキンロックが有効です')
                        return
                elif client.skinlock is True:
                    await message.reply('スキンロックが有効です')
                    return
                if 'banner' not in args[1]:
                    variants=client.user.party.me.create_variants(item='AthenaCharacter',**variantdict)
                    for val in client.user.party.me.outfit_variants:
                        variants.append({'item': val['item'], 'channel': val['channel'], 'variant': val['variant']})
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,asset=args[1],variants=variants))
                else:
                    variantdict['profile_banner']='ProfileBanner'
                    variants=client.user.party.me.create_variants(item='AthenaCharacter',**variantdict)
                    for val in client.user.party.me.outfit_variants:
                        variants.append({'item': val['item'], 'channel': val['channel'], 'variant': val['variant']})
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,asset=args[1],variants=variants))
                await message.reply(f'スキンを {args[1]} {variants} に設定')
            elif args[1].startswith('bid_'):
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.baglock is True:
                        await message.reply('バッグロックが有効です')
                        return
                elif client.baglock is True:
                    await message.reply('バッグロックが有効です')
                    return
                if 'banner' not in args[1]:
                    variants=client.user.party.me.create_variants(item='AthenaBackpack',**variantdict)
                    for val in client.user.party.me.backpack_variants:
                        variants.append({'item': val['item'], 'channel': val['channel'], 'variant': val['variant']})
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,asset=args[1],variants=variants))
                else:
                    variantdict['profile_banner']='ProfileBanner'
                    variants=client.user.party.me.create_variants(item='AthenaBackpack',**variantdict)
                    for val in client.user.party.me.backpack_variants:
                        variants.append({'item': val['item'], 'channel': val['channel'], 'variant': val['variant']})
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,asset=args[1],variants=variants))
                await message.reply(f'バッグを {args[1]} {variants} に設定')
            elif args[1].startswith('petcarrier_'):
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.baglock is True:
                        await message.reply('バッグロックが有効です')
                        return
                elif client.baglock is True:
                    await message.reply('バッグロックが有効です')
                    return
                variants=client.user.party.me.create_variants(item='AthenaBackpack',**variantdict)
                for val in client.user.party.me.backpack_variants:
                    variants.append({'item': val['item'], 'channel': val['channel'], 'variant': val['variant']})
                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,asset=args[1],variants=variants))
                await message.reply(f'バッグを {args[1]} {variants} に設定')
            elif args[1].startswith('pickaxe_id_'):
                if not client.owner is None:
                    if not client.owner.id == message.author.id and client.picklock is True:
                        await message.reply('ツルハシロックが有効です')
                        return
                elif client.picklock is True:
                    await message.reply('ツルハシロックが有効です')
                    return
                variants=client.user.party.me.create_variants(item='AthenaPickaxe',**variantdict)
                for val in client.user.party.me.pickaxe_variants:
                    variants.append({'item': val['item'], 'channel': val['channel'], 'variant': val['variant']})
                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,asset=args[1],variants=variants))
                await client.user.party.me.set_emote('EID_IceKing')
                await message.reply(f'ツルハシを {args[1]} {variants} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['addvariant']}] [variant] [数値]\nvariantと数値は無限に設定可能")
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['skinasset'].split(','):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.skinlock is True:
                    await message.reply('スキンロックが有効です')
                    return
            elif client.skinlock is True:
                await message.reply('スキンロックが有効です')
                return
            if 'banner' not in args[0]:
                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,rawcontent))
            else:
                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,rawcontent,variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['skinasset']}] [アセットパス]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['bagasset'].split(','):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.baglock is True:
                    await message.reply('バッグロックが有効です')
                    return
            elif client.baglock is True:
                await message.reply('バッグロックが有効です')
                return
            if 'banner' not in args[0]:
                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,rawcontent))
            else:
                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,rawcontent,variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['bagasset']}] [アセットパス]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['pickasset'].split(','):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.picklock is True:
                    await message.reply('ツルハシロックが有効です')
                    return
            elif client.picklock is True:
                await message.reply('ツルハシロックが有効です')
                return
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,rawcontent))
            await client.user.party.me.set_emote('EID_IceKing')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['pickasset']}] [アセットパス]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0] in commands['emoteasset'].split(','):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.emotelock is True:
                    await message.reply('エモートロックが有効です')
                    return
            elif client.emotelock is True:
                await message.reply('エモートロックが有効です')
                return
            await client.user.party.me.clear_emote()
            await client.user.party.me.set_emote(args[1])
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply(f"[{commands['emoteasset']}] [アセットパス]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0].lower().startswith('cid_'):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.skinlock is True:
                    await message.reply('スキンロックが有効です')
                    return
            elif client.skinlock is True:
                await message.reply('スキンロックが有効です')
                return
            if not data['loglevel'] == 'normal':
                if data['no-logs'] is False:
                    print(args[0])
                dstore(client.user.display_name,args[0])
            if 'banner' not in args[0].lower():
                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,args[0]))
            else:
                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,args[0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
            await message.reply(f'スキンを {args[0]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0].lower().startswith('bid_'):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.baglock is True:
                    await message.reply('バッグロックが有効です')
                    return
            elif client.baglock is True:
                await message.reply('バッグロックが有効です')
                return
            if not data['loglevel'] == 'normal':
                if data['no-logs'] is False:
                    print(args[0])
                dstore(client.user.display_name,args[0])
            if 'banner' not in args[0].lower():
                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,args[0]))
            else:
                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,args[0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
            await message.reply(f'バッグを {args[0]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0].lower().startswith('pet_carrier'):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.baglock is True:
                    await message.reply('バッグロックが有効です')
                    return
            elif client.baglock is True:
                await message.reply('バッグロックが有効です')
                return
            if not data['loglevel'] == 'normal':
                if data['no-logs'] is False:
                    print(args[0])
                dstore(client.user.display_name,args[0])
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,args[0]))
            await message.reply(f'バッグを {args[0]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0].lower().startswith('pickaxe_id'):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.picklock is True:
                    await message.reply('ツルハシロックが有効です')
                    return
            elif client.picklock is True:
                await message.reply('ツルハシロックが有効です')
                return
            if not data['loglevel'] == 'normal':
                if data['no-logs'] is False:
                    print(args[0])
                dstore(client.user.display_name,args[0])
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,args[0]))
            await client.user.party.me.set_emote('EID_IceKing')
            await message.reply(f'ツルハシを {args[0]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0].lower().startswith('eid_'):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.emotelock is True:
                    await message.reply('エモートロックが有効です')
                    return
            elif client.emotelock is True:
                await message.reply('エモートロックが有効です')
                return
            if not data['loglevel'] == 'normal':
                if data['no-logs'] is False:
                    print(args[0])
                dstore(client.user.display_name,args[0])
            if not client.user.party.me.emote is None:
                if client.user.party.me.emote.lower() == args[0].lower():
                    await client.user.party.me.clear_emote()
            await client.user.party.me.set_emote(args[0])
            await message.reply(f'エモートを {args[0]} に設定')
            client.eid=args[0]
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0].lower().startswith('shout_'):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.emotelock is True:
                    await message.reply('エモートロックが有効です')
                    return
            elif client.emotelock is True:
                await message.reply('エモートロックが有効です')
                return
            if not data['loglevel'] == 'normal':
                if data['no-logs'] is False:
                    print(args[0])
            if not client.user.party.me.emote is None:
                if client.user.party.me.emote.lower() == args[0].lower():
                    await client.user.party.me.clear_emote()
            await client.user.party.me.set_shout(args[0])
            await message.reply(f'エモートを {args[0]} に設定')
            client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Shouts/{args[0]}.{args[0]}'
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0].lower().startswith('emoji_'):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.emotelock is True:
                    await message.reply('エモートロックが有効です')
                    return
            elif client.emotelock is True:
                await message.reply('エモートロックが有効です')
                return
            if not data['loglevel'] == 'normal':
                if data['no-logs'] is False:
                    print(args[0])
                dstore(client.user.display_name,args[0])
            if not client.user.party.me.emote is None:
                if client.user.party.me.emote.lower() == args[0].lower():
                    await client.user.party.me.clear_emote()
            await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{args[0]}.{args[0]}')
            await message.reply(f'エモートを {args[0]} に設定')
            client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{args[0]}.{args[0]}'
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0].lower().startswith('toy_'):
        try:
            if not client.owner is None:
                if not client.owner.id == message.author.id and client.emotelock is True:
                    await message.reply('エモートロックが有効です')
                    return
            elif client.emotelock is True:
                await message.reply('エモートロックが有効です')
                return
            if not data['loglevel'] == 'normal':
                if data['no-logs'] is False:
                    print(args[0])
                dstore(client.user.display_name,args[0])
            if not client.user.party.me.emote is None:
                if client.user.party.me.emote.lower() == args[0].lower():
                    await client.user.party.me.clear_emote()
            await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{args[0]}.{args[0]}')
            await message.reply(f'エモートを {args[0]} に設定')
            client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{args[0]}.{args[0]}'
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    elif args[0].lower().startswith('playlist_'):
        try:
            await client.user.party.set_playlist(args[0])
            await message.reply(f'プレイリストを {args[0]} に設定')
            data['fortnite']['playlist']=args[0]
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('パーティーリーダーではありません')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')

    else:
        if ': ' in message.content:
            return
        try:
            if args[0].isdigit() and client.itemdata[0] == 'True':
                if not data['loglevel'] == 'normal':
                    if data['no-logs'] is False:
                        print(client.itemdata[1][int(args[0])-1][0])
                    dstore(client.user.display_name,client.itemdata[1][int(args[0])-1][0])
                if client.itemdata[1][int(args[0])-1][2] == 'outfit':
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.skinlock is True:
                            await message.reply('スキンロックが有効です')
                            return
                    elif client.skinlock is True:
                        await message.reply('スキンロックが有効です')
                        return
                    if 'banner' not in client.itemdata[1][int(args[0])-1][0]:
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.itemdata[1][int(args[0])-1][0]))
                    else:
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.itemdata[1][int(args[0])-1][0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                if client.itemdata[1][int(args[0])-1][2] == 'backpack':
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.baglock is True:
                            await message.reply('バッグロックが有効です')
                            return
                    elif client.baglock is True:
                        await message.reply('バッグロックが有効です')
                        return
                    if 'banner' not in client.itemdata[1][int(args[0])-1][0]:
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.itemdata[1][int(args[0])-1][0]))
                    else:
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.itemdata[1][int(args[0])-1][0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                if client.itemdata[1][int(args[0])-1][2] == 'pet':
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.baglock is True:
                            await message.reply('バッグロックが有効です')
                            return
                    elif client.baglock is True:
                        await message.reply('バッグロックが有効です')
                        return
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.itemdata[1][int(args[0])-1][0]))
                if client.itemdata[1][int(args[0])-1][2] == 'pickaxe':
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.picklock is True:
                            await message.reply('ツルハシロックが有効です')
                            return
                    elif client.picklock is True:
                        await message.reply('ツルハシロックが有効です')
                        return
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.itemdata[1][int(args[0])-1][0]))
                    await client.user.party.me.set_emote('EID_IceKing')
                if client.itemdata[1][int(args[0])-1][2] == 'emote':
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            return
                    elif client.emotelock is True:
                        await message.reply('エモートロックが有効です')
                        return
                    if not client.user.party.me.emote is None:
                        if client.user.party.me.emote.lower() == client.itemdata[1][int(args[0])-1][0].lower():
                            await client.user.party.me.clear_emote()
                    await client.user.party.me.set_emote(client.itemdata[1][int(args[0])-1][0])
                    client.eid=client.itemdata[1][int(args[0])-1][0]
                if client.itemdata[1][int(args[0])-1][2] == 'emoji':
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            return
                    elif client.emotelock is True:
                        await message.reply('エモートロックが有効です')
                        return
                    await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.itemdata[1][int(args[0])-1][0]}.{client.itemdata[1][int(args[0])-1][0]}')
                    client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.itemdata[1][int(args[0])-1][0]}.{client.itemdata[1][int(args[0])-1][0]}'
                if client.itemdata[1][int(args[0])-1][2] == 'toy':
                    if not client.owner is None:
                        if not client.owner.id == message.author.id and client.emotelock is True:
                            await message.reply('エモートロックが有効です')
                            return
                    elif client.emotelock is True:
                        await message.reply('エモートロックが有効です')
                        return
                    await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{client.itemdata[1][int(args[0])-1][0]}.{client.itemdata[1][int(args[0])-1][0]}')
                    client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{client.itemdata[1][int(args[0])-1][0]}.{client.itemdata[1][int(args[0])-1][0]}'
                return
        except AttributeError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('有効な数字を入力してください')
            return
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')
            return

        try:
            isitem = await is_itemname("ja", content.replace('\\',''))
            if isitem[0] == 'True':
                client.itemdata = isitem
                if len(client.itemdata[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.itemdata[1])))
                    return
                for count,item in enumerate(client.itemdata[1]):
                    if item[2] == 'outfit':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'スキン: {item[1]}')
                        else:
                            await message.reply(f'{count+1} スキン: {item[1]}')
                    if item[2] == 'backpack':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                    if item[2] == 'pet':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                    if item[2] == 'pickaxe':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'ツルハシ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} ツルハシ: {item[1]}')
                    if item[2] == 'emote':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                    if item[2] == 'emoji':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                    if item[2] == 'toy':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                if len(client.itemdata[1]) == 1:
                    if not data['loglevel'] == 'normal':
                        if data['no-logs'] is False:
                            print(client.itemdata[1][0][0])
                        dstore(client.user.display_name,client.itemdata[1][0][0])
                    if client.itemdata[1][0][2] == 'outfit':
                        if 'banner' not in client.itemdata[1][0][0]:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.itemdata[1][0][0]))
                        else:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.itemdata[1][0][0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                    if client.itemdata[1][0][2] == 'backpack':
                        if 'banner' not in client.itemdata[1][0][0]:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.itemdata[1][0][0]))
                        else:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.itemdata[1][0][0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                    if client.itemdata[1][0][2] == 'pet':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.itemdata[1][0][0]))
                    if client.itemdata[1][0][2] == 'pickaxe':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.itemdata[1][0][0]))
                        await client.user.party.me.set_emote('EID_IceKing')
                    if client.itemdata[1][0][2] == 'emote':
                        if not client.user.party.me.emote is None:
                            if client.user.party.me.emote.lower() == client.itemdata[1][0][0].lower():
                                await client.user.party.me.clear_emote()
                        await client.user.party.me.set_emote(client.itemdata[1][0][0])
                        client.eid=client.itemdata[1][0][0]
                    if client.itemdata[1][0][2] == 'emoji':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}'
                    if client.itemdata[1][0][2] == 'toy':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}'
                if len(client.itemdata[1]) > 1:
                    await message.reply('数字を入力することでそのアイテムに設定します')
                return
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
            return
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')
            return

        try:
            isitem = await is_itemname("en", content.replace('\\',''))
            if isitem[0] == 'True':
                client.itemdata = isitem
                if len(client.itemdata[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.itemdata[1])))
                    return
                for count,item in enumerate(client.itemdata[1]):
                    if item[2] == 'outfit':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'スキン: {item[1]}')
                        else:
                            await message.reply(f'{count+1} スキン: {item[1]}')
                    if item[2] == 'backpack':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                    if item[2] == 'pet':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                    if item[2] == 'pickaxe':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'ツルハシ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} ツルハシ: {item[1]}')
                    if item[2] == 'emote':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                    if item[2] == 'emoji':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                    if item[2] == 'toy':
                        if len(client.itemdata[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                if len(client.itemdata[1]) == 1:
                    if not data['loglevel'] == 'normal':
                        if data['no-logs'] is False:
                            print(client.itemdata[1][0][0])
                        dstore(client.user.display_name,client.itemdata[1][0][0])
                    if client.itemdata[1][0][2] == 'outfit':
                        if 'banner' not in client.itemdata[1][0][0]:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.itemdata[1][0][0]))
                        else:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.itemdata[1][0][0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                    if client.itemdata[1][0][2] == 'backpack':
                        if 'banner' not in client.itemdata[1][0][0]:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.itemdata[1][0][0]))
                        else:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.itemdata[1][0][0],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner')))
                    if client.itemdata[1][0][2] == 'pet':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.itemdata[1][0][0]))
                    if client.itemdata[1][0][2] == 'pickaxe':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.itemdata[1][0][0]))
                        await client.user.party.me.set_emote('EID_IceKing')
                    if client.itemdata[1][0][2] == 'emote':
                        if not client.user.party.me.emote is None:
                            if client.user.party.me.emote.lower() == client.itemdata[1][0][0].lower():
                                await client.user.party.me.clear_emote()
                        await client.user.party.me.set_emote(client.itemdata[1][0][0])
                        client.eid=client.itemdata[1][0][0]
                    if client.itemdata[1][0][2] == 'emoji':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}'
                    if client.itemdata[1][0][2] == 'toy':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{client.itemdata[1][0][0]}.{client.itemdata[1][0][0]}'
                if len(client.itemdata[1]) > 1:
                    await message.reply('数字を入力することでそのアイテムに設定します')
                return
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
            return
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            await message.reply('エラー')
            return

#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================

clients = []
for email, password in credentials.items():
    try:
        device_auth_details = get_device_auth_details().get(email, {})
        client = fortnitepy.Client(
            platform=fortnitepy.Platform(data['fortnite']['platform'].upper()),
            status=data['fortnite']['status'],
            auth=fortnitepy.AdvancedAuth(
                email=email,
                password=password,
                prompt_exchange_code=True,
                prompt_exchange_code_if_throttled=True,
                delete_existing_device_auths=False,
                **device_auth_details
            ),
            default_party_member_config=[
                partial(ClientPartyMember.set_outfit, data['fortnite']['cid'].replace('cid','CID',1)),
                partial(ClientPartyMember.set_backpack, data['fortnite']['bid'].replace('bid','BID',1)),
                partial(ClientPartyMember.set_pickaxe, data['fortnite']['pickaxe_id'].replace('pickaxe_id','Pickaxe_ID',1)),
                partial(ClientPartyMember.set_battlepass_info, has_purchased=True, level=data['fortnite']['tier'], self_boost_xp=data['fortnite']['xpboost'], friend_boost_xp=data['fortnite']['friendxpboost']),
                partial(ClientPartyMember.set_banner, icon=data['fortnite']['banner'], color=data['fortnite']['banner_color'], season_level=data['fortnite']['level']),
            ],
        )
    except ValueError:
        print(red(traceback.format_exc()))
        print(red(f'アカウント情報を設定中にエラーが発生しました。configのfortnite部分の設定が間違っている可能性があります。'))
        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        dstore(client.user.display_name,f'アカウント情報を設定中にエラーが発生しました。configのfortnite部分の設定が間違っている可能性があります')
        continue
    client.eid=data['fortnite']['eid']
    client.isready=False
    client.acceptinvite_interval=True
    client.stopcheck=False
    client.skinlock=False
    client.baglock=False
    client.picklock=False
    client.emotelock=False
    client.owner=None
    client.prevoutfit=None
    client.prevoutfitvariants=None
    client.prevbackpack=None
    client.prevbackpackvariants=None
    client.prevpickaxe=None
    client.prevpickaxevariants=None
    client.prevmessage={}
    client.partychat=data['fortnite']['partychat']
    client.joinmessageenable=data['fortnite']['joinmessageenable']
    client.randommessageenable=data['fortnite']['randommessageenable']
    client.skinmimic=data['fortnite']['skinmimic']
    client.emotemimic=data['fortnite']['emotemimic']
    client.acceptinvite=data['fortnite']['acceptinvite']
    client.acceptfriend=data['fortnite']['acceptfriend']

    client.add_event_handler('device_auth_generate', event_device_auth_generate)
    client.add_event_handler('restart', event_restart)
    client.add_event_handler('party_invite', event_party_invite)
    client.add_event_handler('friend_request', event_friend_request)
    client.add_event_handler('friend_add', event_friend_add)
    client.add_event_handler('friend_remove', event_friend_remove)
    client.add_event_handler('party_member_join', event_party_member_join)
    client.add_event_handler('party_member_leave', event_party_member_leave)
    client.add_event_handler('party_member_kick', event_party_member_kick)
    client.add_event_handler('party_member_promote', event_party_member_promote)
    client.add_event_handler('party_member_update', event_party_member_update)
    client.add_event_handler('party_member_disconnect', event_party_member_disconnect)
    client.add_event_handler('party_member_chatban', event_party_member_chatban)
    client.add_event_handler('party_update', event_party_update)
    client.add_event_handler('friend_message', event_friend_message)
    client.add_event_handler('party_message', event_party_message)

    clients.append(client)

try:
    fortnitepy.run_multiple(
        clients,
        ready_callback=event_ready,
        all_ready_callback=lambda: print(green(f'[{now_()}] 全てのアカウントにログインしました。')) if len(clients) > 1 else print('')
    )
except fortnitepy.AuthException as e:
    if "errors.com.epicgames.account.oauth.exchange_code_not_found" in e.args[0]:
        print(red(traceback.format_exc()))
        print(f'[{now_()}] exchange_codeを\nhttps://www.epicgames.com/\nでボットのアカウントにログインし、\nhttps://www.epicgames.com/id/login?redirectUrl=https%3A%2F%2Fwww.epicgames.com%2Fid%2Fapi%2Fexchange\nで取得してください。')
        dstore('ボット',f'>>> {traceback.format_exc()}')
        dstore('ボット',f'>>> exchange_codeを\nhttps://www.epicgames.com/\nでボットのアカウントにログインし、\nhttps://www.epicgames.com/id/login?redirectUrl=https%3A%2F%2Fwww.epicgames.com%2Fid%2Fapi%2Fexchange\nで取得してください')
    else:
        print(red(traceback.format_exc()))
        print(red(f'[{now_()}] アカウントにログインできません。'))
        dstore('ボット',f'>>> {traceback.format_exc()}')
        dstore('ボット',f'>>> アカウントにログインできません')
    kill=True
    exit()
except KeyboardInterrupt:
    kill=True
    exit()
except Exception:
    print(red(traceback.format_exc()))
    print(red(f'[{now_()}] アカウントの読み込みに失敗しました。もう一度試してみてください。'))
    dstore('ボット',f'>>> {traceback.format_exc()}')
    dstore('ボット',f'>>> アカウントの読み込みに失敗しました。もう一度試してみてください')
    kill=True
    exit()
