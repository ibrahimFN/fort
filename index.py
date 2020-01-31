# -*- coding: utf-8-sig -*-
try:
    from crayons import cyan, green, magenta, red
    from fortnitepy import ClientPartyMember
    from functools import partial
    from threading import Timer
    import fortnitepy.errors
    import unicodedata
    import fortnitepy
    import traceback
    import datetime
    import requests
    import aiohttp
    import asyncio
    import logging
    import jaconv
    import random
    import json
    import sys
    import os
except ModuleNotFoundError as e:
    print(e)
    print('モジュールの読み込みに失敗しました。INSTALL.bat を実行してください。問題が修正されない場合はこちらまで連絡をください\nTwitter @gomashioepic\nDiscord gomashio#4335')
    exit()

try:
    with open('config.json', 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
        if data['loglevel'] == 'debug':
            print(f'\n{data}')
        errorcheck=data['fortnite']
        errorcheck=data['fortnite']['email']
        errorcheck=data['fortnite']['password']
        errorcheck=data['fortnite']['owner']
        errorcheck=data['fortnite']['platform']
        errorcheck=data['fortnite']['cid']
        errorcheck=data['fortnite']['bid']
        errorcheck=data['fortnite']['pickaxe_id']
        errorcheck=data['fortnite']['eid']
        errorcheck=data['fortnite']['playlist']
        errorcheck=data['fortnite']['banner']
        errorcheck=data['fortnite']['banner_color']
        errorcheck=data['fortnite']['level']
        errorcheck=data['fortnite']['tier']
        errorcheck=data['fortnite']['xpboost']
        errorcheck=data['fortnite']['friendxpboost']
        errorcheck=data['fortnite']['status']
        errorcheck=data['fortnite']['partychat']
        errorcheck=data['fortnite']['joinmessage']
        errorcheck=data['fortnite']['randommessage']
        errorcheck=data['fortnite']['joinmessageenable']
        errorcheck=data['fortnite']['randommessageenable']
        errorcheck=data['fortnite']['skinmimic']
        errorcheck=data['fortnite']['emotemimic']
        errorcheck=data['fortnite']['acceptinvite']
        errorcheck=data['fortnite']['acceptfriend']
        errorcheck=data['fortnite']['addfriend']
        errorcheck=data['fortnite']['inviteinterval']
        errorcheck=data['fortnite']['interval']
        errorcheck=data['fortnite']['waitinterval']
        errorcheck=data['caseinsensitive']
        errorcheck=data['api-key']
        errorcheck=data['loglevel']
        errorcheck=data['debug']
        errorcheck=requests.get('https://fortnite-api.com/cosmetics/br/search?name=API-KEY-CHECK',headers={'x-api-key': data['api-key']}).json()
        if errorcheck['status'] == 401:
            print(red('APIキーが無効です。正しい値を入力してください。'))
            exit()
        if errorcheck['status'] == 503:
            print(red('APIがダウンしているため、一部コマンドが機能しません。しばらく待ってからもう一度起動してみてください'))
        credentials={}
        try:
            for count,mail in enumerate(data['fortnite']['email'].split(',')):
                credentials[mail]=data['fortnite']['password'].split(',')[count]
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            print(red('メールアドレスの数に対しパスワードの数が足りません。'))
except KeyError as e:
    print(red(traceback.format_exc()))
    print(red('config.json ファイルの読み込みに失敗しました。キーの名前が間違っていないか確認してください。'))
    print(red(f'{str(e)} がありません。'))
    exit()
except json.decoder.JSONDecodeError as e:
    print(red(traceback.format_exc()))
    print(red('config.json ファイルの読み込みに失敗しました。正しく書き込めているか確認してください。'))
    print(red(str(e).replace('Expecting ','不明な',1).replace('Invalid control character at','無効なコントロール文字: ').replace('value','値',1).replace('delimiter','区切り文字',1).replace('line','行:',1).replace('column','文字:').replace('char ','',1)))
    exit()
except FileNotFoundError:
    print(red(traceback.format_exc()))
    print(red('config.json ファイルが存在しません。'))
    exit()

headers={'x-api-key': data['api-key']}
allcosmen=requests.get('https://fortnite-api.com/cosmetics/br?language=en', headers=headers).json()
allcosmja=requests.get('https://fortnite-api.com/cosmetics/br?language=ja', headers=headers).json()
with open('allen.json', 'w') as f:
    json.dump(allcosmen, f)
with open('allja.json', 'w') as f:
    json.dump(allcosmja, f)

try:
    with open('commands.json', 'r', encoding='utf-8-sig') as f:
        commands=json.load(f)
        commands=dict((k.lower(), v.lower()) for k,v in commands.items())
        if data['loglevel'] == 'debug':
            print(f'\n{commands}\n')
except json.decoder.JSONDecodeError:
    print(red(traceback.format_exc()))
    print(red('commands.json ファイルの読み込みに失敗しました。正しく書き込めているか確認してください。'))
except FileNotFoundError:
    print(red(traceback.format_exc()))
    print(red('commands.json ファイルが存在しません。'))
    exit()

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

if not data['loglevel'] == 'normal' and not data['loglevel'] == 'info' and not data['loglevel'] == 'debug':
    data['loglevel']='normal'

print(cyan('ロビーボット: gomashio\nクレジット\nライブラリ: Terbau'))
if data['loglevel'] == 'normal':
    print(green('\nログレベル: ノーマル'))
elif data['loglevel'] == 'info':
    print(green('\nログレベル: 詳細'))
elif data['loglevel'] == 'debug':
    print(green('\nログレベル: デバッグ'))
if data['debug'] is True:
    print(green('デバッグ: オン'))
else:
    print(green('デバッグ: オフ'))
print(green(f'\nPython {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}\nFortnitepy {fortnitepy.__version__}\n'))

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
    print(f'[{now_()}] 招待を承諾に設定')
    client.acceptinvite=True

def inviteinterval(client):
    print(f'[{now_()}] 招待の受付を再開します')
    client.acceptinvite_interval=True

def reload_configs(client):
    global data
    global commands
    global headers
    try:
        with open('config.json', 'r', encoding='utf-8-sig') as f:
            data=json.load(f)
            if data['loglevel'] == 'debug':
                print(f'\n{data}')
    except json.decoder.JSONDecodeError:
        print(red(traceback.format_exc()))
        print(red('config.json ファイルの読み込みに失敗しました。正しく書き込めているか確認してください。'))
        return None
    except FileNotFoundError:
        print(red(traceback.format_exc()))
        print(red('config.json ファイルが存在しません。'))
        return None
    headers={'x-api-key': data['api-key']}
    if not data['loglevel'] == 'normal' and not data['loglevel'] == 'info' and not data['loglevel'] == 'debug':
        data['loglevel']='normal'
    client.joinmessageenable=data['fortnite']['joinmessageenable']
    client.randommessageenable=data['fortnite']['randommessageenable']
    client.skinmimic=data['fortnite']['skinmimic']
    client.emotemimic=data['fortnite']['emotemimic']
    client.acceptinvite=data['fortnite']['acceptinvite']
    client.acceptfriend=data['fortnite']['acceptfriend']

    try:
        with open('commands.json', 'r', encoding='utf-8-sig') as f:
            commands=json.load(f)
            commands=dict((k.lower(), v.lower()) for k,v in commands.items())
            if data['loglevel'] == 'debug':
                print(f'\n{commands}\n')
    except json.decoder.JSONDecodeError:
        print(red(traceback.format_exc()))
        print(red('commands.json ファイルの読み込みに失敗しました。正しく書き込めているか確認してください。'))
        return None
    except FileNotFoundError:
        print(red(traceback.format_exc()))
        print(red('commands.json ファイルが存在しません。'))
        return None
    return 'Success'

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
            if jaconv.hira2kata(itemname.lower()) in jaconv.hira2kata(item['name'].lower()):
                itemlist.append([item['id'],item['name'],item['type'],item['description'],item['displayRarity']])
                TF='True'
        if data['loglevel'] == 'debug':
            print(f'{lang}: {itemname}\n{TF} {itemlist}')
        return TF, itemlist
    except Exception:
        print(red(traceback.format_exc()))
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
                if jaconv.hira2kata(itemname.lower()) in jaconv.hira2kata(item['name'].lower()):
                    itemlist.append([item['id'],item['name'],item['type'],item['description'],item['displayRarity']])
                    TF='True'
        if data['loglevel'] == 'debug':
            print(f'{TF} {lang}: {itemtype} {itemname}\n{TF} {itemlist}')
        return TF, itemlist
    except Exception:
        print(red(traceback.format_exc()))
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
                if jaconv.hira2kata(setname.lower()) in jaconv.hira2kata(item['set'].lower()):
                    itemlist.append([item['id'],item['name'],item['type'],item['description'],item['displayRarity']])
                    TF='True'
        if data['loglevel'] == 'debug':
            print(f'{TF} {lang}: {setname}\n{TF} {itemlist}')
        return TF, itemlist
    except Exception:
        print(red(traceback.format_exc()))
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
            print(f'{TF} {lang}: {itemid}\n{TF} {itemlist}')
        return TF, itemlist
    except Exception:
        print(red(traceback.format_exc()))
        return TF


async def event_device_auth_generate(details, email):
    store_device_auth_details(email, details)

async def event_ready(client):
    if data['loglevel'] == 'normal':
        print(green(f'[{now_()}] ログイン: {client.user.display_name}'))
    else:
        print(green(f'[{now_()}] ログイン: {client.user.display_name} / {client.user.id}'))

    try:
        client.owner=None
        owner=await client.fetch_profile(data['fortnite']['owner'])
        if owner is None:
            print(red(f'[{now_()}] [{client.user.display_name}] 所有者が見つかりません。正しい名前/IDになっているか確認してください。'))
        else:
            client.owner=client.get_friend(owner.id)
            if client.owner is None:
                try:
                    await client.add_friend(owner.id)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                except Exception:
                    print(red(traceback.format_exc()))
                print(red(f"[{now_()}] [{client.user.display_name}] 所有者とフレンドではありません。フレンドになってからもう一度起動するか、[{data['reload']}] コマンドで再読み込みしてください。"))
            else:
                if data['loglevel'] == 'normal':
                    print(green(f'[{now_()}] [{client.user.display_name}] 所有者: {client.owner.display_name}'))
                else:
                    print(green(f'[{now_()}] [{client.user.display_name}] 所有者: {client.owner.display_name} / {client.owner.id}'))
    except fortnitepy.HTTPException:
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
        print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
    except Exception:
        print(red(traceback.format_exc()))
    
    if not client.owner is None:
        await client.owner.send('ここをクリックして招待')

    if data['fortnite']['addfriend'] is True:
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
                    await pending.decline()
                except Exception:
                    print(red(traceback.format_exc()))
            else:
                try:
                    await pending.decline()
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                except Exception:
                    print(red(traceback.format_exc()))

async def event_restart():
    print(green(f'[{now_()}] 正常に再ログインが完了しました'))

async def event_party_invite(invitation):
    client=invitation.client
    if invitation is None:
        return
    if not client.owner is None:
        if invitation.sender.id == client.owner.id:
            try:
                await invitation.accept()
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                print(red(f'[{now_()}] [{client.user.display_name}] 以前に参加したプライベートパーティーに参加しようとしています。(Epicサービス側のバグです)'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                print(red(f'[{now_()}] [{client.user.display_name}] パーティー招待の承諾リクエストを処理中にエラーが発生しました。'))
            except Exception:
                print(red(traceback.format_exc()))
            return
    if data['loglevel'] == 'normal':
        if invitation.sender.display_name is None:
            print(f'[{now_()}] [{client.user.display_name}] None からのパーティー招待')
        else:
            print(f'[{now_()}] [{client.user.display_name}] {invitation.sender.display_name} からのパーティー招待')
    else:
        if invitation.sender.display_name is None:
            print(f'[{now_()}] [{client.user.display_name}] None / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待')
        else:
            print(f'[{now_()}] [{client.user.display_name}] {invitation.sender.display_name} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待')

    if not client.owner is None:
        if not client.owner.id in client.user.party.members.keys():
            if client.acceptinvite is True:
                if client.acceptinvite_interval is True:
                    try:
                        await invitation.accept()
                        client.acceptinvite_interval=False
                        try:
                            client.timer.cancel()
                        except Exception:
                            if data['loglevel'] == 'debug':
                                print(red(traceback.format_exc()))
                        client.timer=Timer(data['fortnite']['interval'], inviteinterval, [client])
                        client.timer.start()
                        if data['loglevel'] == 'normal':
                            if invitation.sender.display_name is None:
                                print(f'[{now_()}] [{client.user.display_name}] None からの招待を承諾')
                            else:
                                print(f'[{now_()}] [{client.user.display_name}] {invitation.sender.display_name} からの招待を承諾')
                        else:
                            if invitation.sender.display_name is None:
                                print(f'[{now_()}] [{client.user.display_name}] None / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待を承諾')
                            else:
                                print(f'[{now_()}] [{client.user.display_name}] {invitation.sender.display_name} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待を承諾')
                    except KeyError:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                    except fortnitepy.PartyError:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                        print(red(f'[{now_()}] [{client.user.display_name}] 既にパーティーのメンバーです。'))
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                        print(red(f'[{now_()}] [{client.user.display_name}] メンバーが見つかりません。'))
                    except fortnitepy.Forbidden:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                        print(red(f'[{now_()}] [{client.user.display_name}] 以前に参加したプライベートパーティーに参加しようとしています。(Epicサービス側のバグです)'))
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                        print(red(f'[{now_()}] [{client.user.display_name}] パーティー招待の承諾リクエストを処理中にエラーが発生しました。'))
                    except Exception:
                        print(red(traceback.format_exc()))
                else:
                    try:
                        await invitation.decline()
                        await invitation.sender.send(f"招待を承諾してから{str(data['fortnite']['interval'])}秒間は招待を拒否します")
                        if data['loglevel'] == 'normal':
                            if invitation.sender.display_name is None:
                                print(f"[{now_()}] [{client.user.display_name}] None からの招待を{str(data['fortnite']['interval'])}秒拒否")
                            else:
                                print(f"[{now_()}] [{client.user.display_name}] {invitation.sender.display_name} からの招待を{str(data['fortnite']['interval'])}秒拒否")
                        else:
                            if invitation.sender.display_name is None:
                                print(f"[{now_()}] [{client.user.display_name}] None / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待を{str(data['fortnite']['interval'])}秒拒否")
                            else:
                                print(f"[{now_()}] [{client.user.display_name}] {invitation.sender.display_name} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待を{str(data['fortnite']['interval'])}秒拒否")
                    except fortnitepy.PartyError:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                        print(red(f'[{now_()}] [{client.user.display_name}] 受信したnet_clとクライアントのnet_clが一致しません。'))
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                        print(red(f'[{now_()}] [{client.user.display_name}] パーティー招待の拒否リクエストを処理中にエラーが発生しました。'))
                    except Exception:
                        print(red(traceback.format_exc()))
            else:
                try:
                    await invitation.decline()
                    if data['loglevel'] == 'normal':
                        if invitation.sender.display_name is None:
                            print(f'[{now_()}] [{client.user.display_name}] None からの招待を拒否')
                        else:
                            print(f'[{now_()}] [{client.user.display_name}] {invitation.sender.display_name} からの招待を拒否')
                    else:
                        if invitation.sender.display_name is None:
                            print(f'[{now_()}] [{client.user.display_name}] None / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待を拒否')
                        else:
                            print(f'[{now_()}] [{client.user.display_name}] {invitation.sender.display_name} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待を拒否')
                except fortnitepy.PartyError:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                    print(red(f'[{now_()}] [{client.user.display_name}] 受信したnet_clとクライアントのnet_clが一致しません。'))
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                    print(red(f'[{now_()}] [{client.user.display_name}] パーティー招待の拒否リクエストを処理中にエラーが発生しました。'))
                except Exception:
                    print(red(traceback.format_exc()))
        else:
            try:
                await invitation.decline()
                await invitation.sender.send('所有者がパーティーにいるため招待を拒否します')
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                print(red(f'[{now_()}] [{client.user.display_name}] 受信したnet_clとクライアントのnet_clが一致しません。'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                print(red(f'[{now_()}] [{client.user.display_name}] パーティー招待の拒否リクエストを処理中にエラーが発生しました。'))
            except Exception:
                print(red(traceback.format_exc()))
    else:
        if client.acceptinvite is True:
            if client.acceptinvite_interval is True:
                try:
                    await invitation.accept()
                    client.acceptinvite_interval=False
                    try:
                        client.timer.cancel()
                    except Exception:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                    client.timer=Timer(data['fortnite']['interval'], inviteinterval, [client])
                    client.timer.start()
                    if data['loglevel'] == 'normal':
                        if invitation.sender.display_name is None:
                            print(f'[{now_()}] [{client.user.display_name}] None からの招待を承諾')
                        else:
                            print(f'[{now_()}] [{client.user.display_name}] {invitation.sender.display_name} からの招待を承諾')
                    else:
                        if invitation.sender.display_name is None:
                            print(f'[{now_()}] [{client.user.display_name}] None / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待を承諾')
                        else:
                            print(f'[{now_()}] [{client.user.display_name}] {invitation.sender.display_name} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待を承諾')
                except fortnitepy.Forbidden:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                    print(red(f'[{now_()}] [{client.user.display_name}] 以前に参加したプライベートパーティーに参加しようとしています。(Epicサービス側のバグです)'))
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                    print(red(f'[{now_()}] [{client.user.display_name}] パーティー招待の承諾リクエストを処理中にエラーが発生しました。'))
                except Exception:
                    print(red(traceback.format_exc()))
            else:
                try:
                    await invitation.decline()
                    await invitation.sender.send(f"招待を承諾してから{str(data['fortnite']['interval'])}秒間は招待を拒否します")
                    if data['loglevel'] == 'normal':
                        if invitation.sender.display_name is None:
                            print(f"[{now_()}] [{client.user.display_name}] None からの招待を{str(data['fortnite']['interval'])}秒拒否")
                        else:
                            print(f"[{now_()}] [{client.user.display_name}] {invitation.sender.display_name} からの招待を{str(data['fortnite']['interval'])}秒拒否")
                    else:
                        if invitation.sender.display_name is None:
                            print(f"[{now_()}] [{client.user.display_name}] None / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待を{str(data['fortnite']['interval'])}秒拒否")
                        else:
                            print(f"[{now_()}] [{client.user.display_name}] {invitation.sender.display_name} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待を{str(data['fortnite']['interval'])}秒拒否")
                except fortnitepy.PartyError:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                    print(red(f'[{now_()}] [{client.user.display_name}] 受信したnet_clとクライアントのnet_clが一致しません。'))
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                    print(red(f'[{now_()}] [{client.user.display_name}] パーティー招待の拒否リクエストを処理中にエラーが発生しました。'))
                except Exception:
                    print(red(traceback.format_exc()))
        else:
            try:
                await invitation.decline()
                if data['loglevel'] == 'normal':
                    if invitation.sender.display_name is None:
                        print(f'[{now_()}] [{client.user.display_name}] None からの招待を拒否')
                    else:
                        print(f'[{now_()}] [{client.user.display_name}] {invitation.sender.display_name} からの招待を拒否')
                else:
                    if invitation.sender.display_name is None:
                        print(f'[{now_()}] [{client.user.display_name}] None / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待を拒否')
                    else:
                        print(f'[{now_()}] [{client.user.display_name}] {invitation.sender.display_name} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待を拒否')
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                print(red(f'[{now_()}] [{client.user.display_name}] 受信したnet_clとクライアントのnet_clが一致しません。'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                print(red(f'[{now_()}] [{client.user.display_name}] パーティー招待の拒否リクエストを処理中にエラーが発生しました。'))
            except Exception:
                print(red(traceback.format_exc()))

async def event_friend_request(request):
    client=request.client
    if request is None:
        return
    if request.direction == 'OUTBOUND':
        if data['loglevel'] == 'normal':
            if request.display_name is None:
                print(f'[{now_()}] [{client.user.display_name}] None にフレンド申請を送信')
            else:
                print(f'[{now_()}] [{client.user.display_name}] {request.display_name} にフレンド申請を送信')
        else:
            if request.display_name is None:
                print(f'[{now_()}] [{client.user.display_name}] None / {request.id} にフレンド申請を送信')
            else:
                print(f'[{now_()}] [{client.user.display_name}] {request.display_name} / {request.id} にフレンド申請を送信')
        return
    if data['loglevel'] == 'normal':
        if request.display_name is None:
            print(f'[{now_()}] [{client.user.display_name}] None からのフレンド申請')
        else:
            print(f'[{now_()}] [{client.user.display_name}] {request.display_name} からのフレンド申請')
    else:
        if request.display_name is None:
            print(f'[{now_()}] [{client.user.display_name}] None / {request.id} からのフレンド申請')
        else:
            print(f'[{now_()}] [{client.user.display_name}] {request.display_name} / {request.id} からのフレンド申請')
    if client.acceptfriend is True:
        try:
            await request.accept()
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            print(red(f'[{now_()}] [{client.user.display_name}] フレンド申請の承諾リクエストを処理中にエラーが発生しました。'))
        except Exception:
            print(red(traceback.format_exc()))
    elif client.acceptfriend is False:
        try:
            await request.decline()
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            print(f'[{now_()}] [{client.user.display_name}] フレンド申請の拒否リクエストを処理中にエラーが発生しました。')
        except Exception:
            print(red(traceback.format_exc()))

async def event_friend_add(friend):
    client=friend.client
    if friend is None:
        return
    if friend.direction == 'INBOUND':
        if data['loglevel'] == 'normal':
            if friend.display_name is None:
                print(f'[{now_()}] [{client.user.display_name}] None がフレンドに追加')
            else:
                print(f'[{now_()}] [{client.user.display_name}] {friend.display_name} がフレンドに追加')
        else:
            if friend.display_name is None:
                print(f'[{now_()}] [{client.user.display_name}] None / {friend.id} [{platform_to_str(friend.platform)}] がフレンドに追加')
            else:
                print(f'[{now_()}] [{client.user.display_name}] {friend.display_name} / {friend.id} [{platform_to_str(friend.platform)}] がフレンドに追加')
    else:
        if data['loglevel'] == 'normal':
            if friend.display_name is None:
                print(f'[{now_()}] [{client.user.display_name}] None をフレンドに追加')
            else:
                print(f'[{now_()}] [{client.user.display_name}] {friend.display_name} をフレンドに追加')
        else:
            if friend.display_name is None:
                print(f'[{now_()}] [{client.user.display_name}] None / {friend.id} [{platform_to_str(friend.platform)}] をフレンドに追加')
            else:
                print(f'[{now_()}] [{client.user.display_name}] {friend.display_name} / {friend.id} [{platform_to_str(friend.platform)}] をフレンドに追加')

async def event_friend_remove(friend):
    client=friend.client
    if friend is None:
        return
    if data['loglevel'] == 'normal':
        if friend.display_name is None:
            print(f'[{now_()}] [{client.user.display_name}] None がフレンドから削除')
        else:
            print(f'[{now_()}] [{client.user.display_name}] {friend.display_name} がフレンドから削除')
    else:
        if friend.display_name is None:
            print(f'[{now_()}] [{client.user.display_name}] None / {friend.id} [{platform_to_str(friend.platform)}] がフレンドから削除')
        else:
            print(f'[{now_()}] [{client.user.display_name}] {friend.display_name} / {friend.id} [{platform_to_str(friend.platform)}] がフレンドから削除')

async def event_party_member_join(member):
    client=member.client
    if member is None:
        return
    if data['loglevel'] == 'normal':
        if member.display_name is None:
            print(magenta(f'[{now_()}] [パーティー] [{client.user.display_name}] None がパーティーに参加\n人数: {member.party.member_count}'))
        else:
            print(magenta(f'[{now_()}] [パーティー] [{client.user.display_name}] {member.display_name} がパーティーに参加\n人数: {member.party.member_count}'))
    else:
        if member.display_name is None:
            print(magenta(f'[{now_()}] [パーティー/{member.party.id}] [{client.user.display_name}] None / {member.id} [{platform_to_str(member.platform)}/{member.input}] がパーティーに参加\n人数: {member.party.member_count}'))
        else:
            print(magenta(f'[{now_()}] [パーティー/{member.party.id}] [{client.user.display_name}] {member.display_name} / {member.id} [{platform_to_str(member.platform)}/{member.input}] がパーティーに参加\n人数: {member.party.member_count}'))
    
    if data['fortnite']['addfriend'] is True:
        for member in member.party.members.keys():
            try:
                await client.add_friend(member)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
            except Exception:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))

    await asyncio.sleep(0.2)

    if client.joinmessageenable is True:
        try:
            await client.user.party.send(data['fortnite']['joinmessage'])
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
    if client.randommessageenable is True:
            try:
                randommessage=random.choice(data['fortnite']['randommessage'].split(','))
                print(f'[{now_()}] [{client.user.display_name}] ランダムメッセージ: {randommessage}')
                await client.user.party.send(randommessage)
            except Exception:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))

    try:
        await client.user.party.me.clear_emote()
        await client.user.party.me.set_emote(asset=client.eid)
    except Exception:
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
    else:
        try:
            await client.user.party.me.set_emote(asset=client.eid)
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))

async def event_party_member_leave(member):
    client=member.client
    if member is None:
        return
    if data['loglevel'] == 'normal':
        if member.display_name is None:
            print(magenta(f'[{now_()}] [パーティー] [{client.user.display_name}] None がパーティーを離脱\n人数: {member.party.member_count}'))
        else:
            print(magenta(f'[{now_()}] [パーティー] [{client.user.display_name}] {member.display_name} がパーティーを離脱\n人数: {member.party.member_count}'))
    else:
        if member.display_name is None:
            print(magenta(f'[{now_()}] [パーティー/{member.party.id}] [{client.user.display_name}] None / {member.id} [{platform_to_str(member.platform)}/{member.input}] がパーティーを離脱\n人数: {member.party.member_count}'))
        else:
            print(magenta(f'[{now_()}] [パーティー/{member.party.id}] [{client.user.display_name}] {member.display_name} / {member.id} [{platform_to_str(member.platform)}/{member.input}] がパーティーを離脱\n人数: {member.party.member_count}'))

    if data['fortnite']['addfriend'] is True:
        for member in member.party.members.keys():
            try:
                await client.add_friend(member)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                continue
            except Exception:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))

async def event_party_member_kick(member):
    client=member.client
    if member is None:
        return
    if data['loglevel'] == 'normal':
        if member.party.leader.display_name is None:
            if member.display_name is None:
                print(magenta(f'[{now_()}] [パーティー] [{client.user.display_name}] None が None をパーティーからキック\n人数: {member.party.member_count}'))
            else:
                print(magenta(f'[{now_()}] [パーティー] [{client.user.display_name}] None が {member.display_name} をパーティーからキック\n人数: {member.party.member_count}'))
        else:
            if member.display_name is None:
                print(magenta(f'[{now_()}] [パーティー] [{client.user.display_name}] {member.party.leader.display_name} が None をパーティーからキック\n人数: {member.party.member_count}'))
            else:
                print(magenta(f'[{now_()}] [パーティー] [{client.user.display_name}] {member.party.leader.display_name} が {member.display_name} をパーティーからキック\n人数: {member.party.member_count}'))
    else:
        if member.party.leader.display_name is None:
            if member.display_name is None:
                print(magenta(f'[{now_()}] [パーティー/{member.party.id}] [{client.user.display_name}] None / {member.party.leader.id} [{platform_to_str(member.party.leader.platform)}/{member.input}] が None / {member.id} [{platform_to_str(member.platform)}/{member.input}] がパーティーからキック\n人数: {member.party.member_count}'))
            else:
                print(magenta(f'[{now_()}] [パーティー/{member.party.id}] [{client.user.display_name}] None / {member.party.leader.id} [{platform_to_str(member.party.leader.platform)}/{member.input}] が {member.display_name} / {member.id} [{platform_to_str(member.platform)}/{member.input}] がパーティーからキック\n人数: {member.party.member_count}'))
        else:
            if member.display_name is None:
                print(magenta(f'[{now_()}] [パーティー/{member.party.id}] [{client.user.display_name}] {member.party.leader.display_name} / {member.party.leader.id} [{platform_to_str(member.party.leader.platform)}/{member.input}] が None / {member.id} [{platform_to_str(member.platform)}/{member.input}] がパーティーからキック\n人数: {member.party.member_count}'))
            else:
                print(magenta(f'[{now_()}] [パーティー/{member.party.id}] [{client.user.display_name}] {member.party.leader.display_name} / {member.party.leader.id} [{platform_to_str(member.party.leader.platform)}/{member.input}] が {member.display_name} / {member.id} [{platform_to_str(member.platform)}/{member.input}] がパーティーからキック\n人数: {member.party.member_count}'))

async def event_party_member_promote(old_leader,new_leader):
    if old_leader is None or new_leader is None:
        return
    client=new_leader.client
    if new_leader.id == client.user.id:
        try:
            await client.user.party.set_playlist(data['fortnite']['playlist'])
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
    if data['loglevel'] == 'normal':
        if old_leader.display_name is None:
            if new_leader.display_name is None:
                print(magenta(f'[{now_()}] [パーティー] [{client.user.display_name}] None から None にリーダーが譲渡'))
            else:
                print(magenta(f'[{now_()}] [パーティー] [{client.user.display_name}] None から {new_leader.display_name} にリーダーが譲渡'))
        else:
            if new_leader.display_name is None:
                print(magenta(f'[{now_()}] [パーティー] [{client.user.display_name}] {old_leader.display_name} から None にリーダーが譲渡'))
            else:
                print(magenta(f'[{now_()}] [パーティー] [{client.user.display_name}] {old_leader.display_name} から {new_leader.display_name} にリーダーが譲渡'))
    else:
        if old_leader.display_name is None:
            if new_leader.display_name is None:
                print(magenta(f'[{now_()}] [パーティー/{new_leader.party.id}] [{client.user.display_name}] None / {old_leader.id} [{platform_to_str(old_leader.platform)}/{old_leader.input}] から None / {new_leader.id} [{platform_to_str(new_leader.platform)}/{new_leader.input}] にリーダーが譲渡'))
            else:
                print(magenta(f'[{now_()}] [パーティー/{new_leader.party.id}] [{client.user.display_name}] None / {old_leader.id} [{platform_to_str(old_leader.platform)}/{old_leader.input}] から {new_leader.display_name} / {new_leader.id} [{platform_to_str(new_leader.platform)}/{new_leader.input}] にリーダーが譲渡'))
        else:
            if new_leader.display_name is None:
                print(magenta(f'[{now_()}] [パーティー/{new_leader.party.id}] [{client.user.display_name}] {old_leader.display_name} / {old_leader.id} [{platform_to_str(old_leader.platform)}/{old_leader.input}] から None / {new_leader.id} [{platform_to_str(new_leader.platform)}/{new_leader.input}] にリーダーが譲渡'))
            else:
                print(magenta(f'[{now_()}] [パーティー/{new_leader.party.id}] [{client.user.display_name}] {old_leader.display_name} / {old_leader.id} [{platform_to_str(old_leader.platform)}/{old_leader.input}] から {new_leader.display_name} / {new_leader.id} [{platform_to_str(new_leader.platform)}/{new_leader.input}] にリーダーが譲渡'))

async def event_party_member_update(member):
    client=member.client
    if member is None:
        return
    if not data['loglevel'] == 'normal':
        if member.display_name is None:
            print(magenta(f'[{now_()}] [パーティー/{member.party.id}] [{client.user.display_name}] None / {member.id} パーティーメンバー更新'))
        else:
            print(magenta(f'[{now_()}] [パーティー/{member.party.id}] [{client.user.display_name}] {member.display_name} / {member.id} [{platform_to_str(member.platform)}/{member.input}] パーティーメンバー更新'))
    if member.id == client.user.id:
        return
    if not member.outfit == client.prevoutfit or not member.outfit_variants == client.prevoutfitvariants:
        if not data['loglevel'] == 'normal':
            print(member.outfit)
        if client.skinmimic is True:
            if member.outfit is None:
                try:
                    await client.user.party.me.set_outfit(asset='CID_NONE')
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
            else:
                try:
                    await client.user.party.me.set_outfit(asset=member.outfit.upper(),variants=member.outfit_variants)
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
    if not member.backpack == client.prevbackpack or not member.backpack_variants == client.prevbackpackvariants:
        if not data['loglevel'] == 'normal':
            print(member.backpack)
        if client.skinmimic is True:
            if member.backpack is None:
                try:
                    await client.user.party.me.set_backpack(asset='BID_NONE')
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
            else:
                try:
                    await client.user.party.me.set_backpack(asset=member.backpack.upper(),variants=member.backpack_variants)
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
    if not member.pickaxe == client.prevpickaxe or not member.pickaxe_variants == client.prevpickaxevariants:
        if not data['loglevel'] == 'normal':
            print(member.pickaxe)
        if client.skinmimic is True:
            if member.pickaxe is None:
                try:
                    await client.user.party.me.set_pickaxe(asset='PICKAXE_ID_NONE')
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
            else:
                try:
                    await client.user.party.me.set_pickaxe(asset=member.pickaxe.upper(),variants=member.pickaxe_variants)
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
    client.prevoutfit=member.outfit
    client.prevoutfitvariants=member.outfit_variants
    client.prevbackpack=member.backpack
    client.prevbackpackvariants=member.backpack_variants
    client.prevpickaxe=member.pickaxe
    client.prevpickaxevariants=member.pickaxe_variants

    if not member.emote is None:
        if not data['loglevel'] == 'normal':
            print(member.emote)
        if client.emotemimic is True:
            if member.emote.upper() == client.user.party.me.emote.upper():
                try:
                    await client.user.party.me.clear_emote()
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
            try:
                await client.user.party.me.set_emote(asset=member.emote.upper())
            except Exception:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))

#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================

async def event_friend_message(message):
    client=message.client
    if data['caseinsensitive'] is True:
        args = jaconv.kata2hira(message.content.lower()).split()
    else:
        args = message.content.split()
    rawargs = message.content.split()
    rawcontent = ' '.join(rawargs[1:])
    rawcontent2 = ' '.join(rawargs[2:])
    user=None
    if data['loglevel'] == 'normal':
        if message.author.display_name is None:
            print(f'[{now_()}] [{client.user.display_name}] None | {message.content}')
        else:
            print(f'[{now_()}] [{client.user.display_name}] {message.author.display_name} | {message.content}')
    else:
        if message.author.display_name is None:
            print(f'[{now_()}] [{client.user.display_name}] None / {message.author.id} [{platform_to_str(message.author.platform)}] | {message.content}')
        else:
            print(f'[{now_()}] [{client.user.display_name}] {message.author.display_name}/ {message.author.id} [{platform_to_str(message.author.platform)}] | {message.content}')

    if args[0] in commands['prev'].split(','):
        args = jaconv.kata2hira(client.prevmessage.lower()).split()
        rawargs = client.prevmessage.split()
        rawcontent = ' '.join(rawargs[1:])
    client.prevmessage=message.content

    if args[0] in commands['restart'].split(','):
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
            await message.reply('エラー')

    elif args[0] in commands['relogin'].split(','):
        try:
            await message.reply('アカウントに再ログインします...')
            await client.restart()
        except fortnitepy.AuthException:
            print(red(traceback.format_exc()))
            print(red(f'[{now_()}] メールアドレスまたはパスワードが間違っています。'))
            exit()
        except Exception:
            print(red(traceback.format_exc()))
            print(red(f'[{now_()}] アカウントの読み込みに失敗しました。もう一度試してみてください。'))
            exit()

    elif args[0] in commands['reload'].split(','):
        result=reload_configs(client)
        try:
            if result == 'Success':
                await message.reply('正常に読み込みが完了しました')
            else:
                await message.reply('エラー')
            try:
                client.owner=None
                owner=await client.fetch_profile(data['fortnite']['owner'])
                if owner is None:
                    print(red(f'[{now_()}] 所有者が見つかりません。正しい名前/IDになっているか確認してください。'))
                else:
                    client.owner=client.get_friend(owner.id)
                    if client.owner is None:
                        try:
                            await client.add_friend(owner.id)
                        except fortnitepy.HTTPException:
                            if data['loglevel'] == 'debug':
                                print(red(traceback.format_exc()))
                        except Exception:
                            if data['loglevel'] == 'debug':
                                print(red(traceback.format_exc()))
                        print(red(f'[{now_()}] 所有者とフレンドではありません。フレンドになってからもう一度起動してください。'))
                    else:
                        if data['loglevel'] == 'normal':
                            print(green(f'[{now_()}] 所有者: {client.owner.display_name}'))
                        else:
                            print(green(f'[{now_()}] 所有者: {client.owner.display_name} / {client.owner.id}'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                print(red(f'[{now_()}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['get'].split(','):
        await message.reply(f'{client.user.party.leader.display_name}\n{client.user.party.leader.pickaxe}\n{client.user.party.leader.pickaxe_variants}')

    elif args[0] in commands['friendcount'].split(','):
        try:
            print(f'フレンド数: {len(client.friends)}')
            await message.reply(f'フレンド数: {len(client.friends)}')
        except Exception:
            print(red(traceback.format_exc()))
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
            await message.reply(f"[{commands['skinmimic']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
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
            await message.reply(f"[{commands['emotemimic']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
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
            await message.reply(f"[{commands['party']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
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
            await message.reply(f"[{commands['acceptinvite']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
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
            await message.reply(f"[{commands['acceptfriend']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
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
            await message.reply(f"[{commands['joinmessageenable']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
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
            await message.reply(f"[{commands['randommessageenable']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['wait'].split(','):
        try:
            if not client.owner is None:
                if client.owner.id in client.user.party.members.keys() and not message.author.id == client.owner.id:
                    await message.reply('現在利用できません')
                else:
                    client.acceptinvite=False
                    try:
                        client.timer_.cancel()
                    except Exception:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                    client.timer_=Timer(data['fortnite']['waitinterval'], inviteaccept, [client])
                    client.timer_.start()
                    await message.reply(f"{str(data['fortnite']['waitinterval'])}秒間招待を拒否します")
            else:
                client.acceptinvite=False
                try:
                    client.timer_.cancel()
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                client.timer_=Timer(data['fortnite']['waitinterval'], inviteaccept, [client])
                client.timer_.start()
                await message.reply(f"{str(data['fortnite']['waitinterval'])}秒間招待を拒否します")
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['join'].split(','):
        try:
            await client.join_to_party(party_id=args[1])
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('既にこのパーティーのメンバーです')
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーが見つかりません')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーがプライベートです')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['join']}] [party_id]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['leave'].split(','):
        try:
            await client.user.party.me.leave()
            await message.reply('パーティーを離脱')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティー離脱のリクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['invite'].split(','):
        try:
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
            else:
                friend=client.get_friend(user.id)
                if friend is None:
                    friend=client.get_friend(rawcontent)
                    if friend is None:
                        await message.reply('ユーザーとフレンドではありません')
                if not friend is None:
                    try:
                        await friend.invite()
                        if data['loglevel'] == 'normal':
                            await message.reply(f'{friend.display_name} をパーティーに招待')
                        else:
                            await message.reply(f'{friend.display_name} / {friend.id} をパーティー {client.user.party.id} に招待')
                    except fortnitepy.PartyError:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                        await message.reply('パーティーが満員か、既にパーティーにいます')
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                        await message.reply('パーティー招待の送信リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['invite']}] [ユーザー名 / ユーザーID]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['inviteme'].split(','):
        try:
            await message.author.invite()
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーが満員か、既にパーティーにいます')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティー招待の送信リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['message'].split(','):
        try:
            send=rawcontent.split(' : ')
            user=await client.fetch_profile(send[0])
            if user is None:
                await message.reply('ユーザーが見つかりません')
            else:
                friend=client.get_friend(user.id)
                if friend is None:
                    friend=client.get_friend(send[0])
                    if friend is None:
                        await message.reply('ユーザーとフレンドではありません')
                if not friend is None:
                    await friend.send(send[1])
                    if data['loglevel'] == 'normal':
                        await message.reply(f'{friend.display_name} にメッセージ {send[1]} を送信')
                    else:
                        await message.reply(f'{friend.display_name} / {friend.id} にメッセージ {send[1]} を送信')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['message']}] [ユーザー名 / ユーザーID] : [内容]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['partymessage'].split(','):
        try:
            await client.user.party.send(rawcontent)
            if data['loglevel'] == 'normal':
                await message.reply(f'パーティーにメッセージ {rawcontent} を送信')
            else:
                await message.reply(f'パーティー {client.user.party.id} にメッセージ {rawcontent} を送信')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['partymessage']}] [内容]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['status'].split(','):
        try:
            await client.set_status(rawcontent)
            await message.reply(f'ステータスを {rawcontent} に設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['status']}] [内容]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['banner'].split(','):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_banner,args[1],args[2],client.user.party.me.banner[2]))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('バナー情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['banner']}] [バナーID] [バナーの色]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['level'].split(','):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_banner,client.user.party.me.banner[0],client.user.party.me.banner[1],int(args[1])))
            await message.reply(f'レベルを {args[1]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('レベルの設定リクエストを処理中にエラーが発生しました')
        except ValueError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('数字を入力してください')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['level']}] [レベル]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')
    
    elif args[0] in commands['bp'].split(','):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_battlepass_info,True,args[1],args[2],args[3]))
            await message.reply(f'バトルパス情報を ティア: {args[1]} XPブースト: {args[2]} フレンドXPブースト: {args[3]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('バトルパス情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['bp']}] [ティア] [XPブースト] [フレンドXPブースト]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['user'].split(','):
        try:
            user=await client.fetch_profile(rawcontent)
            if user is None:
                await message.reply('ユーザーが見つかりません')
            else:
                if user.display_name is None:
                    print(f'None / {user.id}')
                    await message.reply(f'None / {user.id}')
                else:
                    print(f'{user.display_name} / {user.id}')
                    await message.reply(f'{user.display_name} / {user.id}')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['user']}] [ユーザー名 / ユーザーID]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['friend'].split(','):
        try:
            user=await client.fetch_profile(rawcontent)
            if user is None:
                await message.reply('ユーザーが見つかりません')
            else:
                friend=client.get_friend(user.id)
                if friend is None:
                    await message.reply('ユーザーとフレンドではありません')
                else:
                    if friend.nickname is None:
                        if friend.display_name is None:
                            print(f'None / {friend.id}')
                            await message.reply(f'None / {friend.id}')
                        else:
                            print(f'{friend.display_name} / {friend.id}')
                            await message.reply(f'{friend.display_name} / {friend.id}')
                    else:
                        if friend.display_name is None:
                            print(f'{friend.nickname}(None) / {friend.id}')
                            await message.reply(f'{friend.nickname}(None) / {friend.id}')
                        else:
                            print(f'{friend.nickname}({friend.display_name}) / {friend.id}')
                            await message.reply(f'{friend.nickname}({friend.display_name}) / {friend.id}')
                    if not friend.last_logout is None:
                        await message.reply('最後のログイン: {0.year}年{0.month}月{0.day}日 {0.hour}時{0.minute}分{0.second}秒'.format(friend.last_logout))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['friend']}] [ユーザー名 / ユーザーID]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['info'].split(','):
        try:
            if args[1] in commands['info_party'].split(','):
                await message.reply(f'{client.user.party.id}\n人数: {client.user.party.member_count}')
                for member in client.user.party.members.values():
                    if member.display_name is None:
                        await message.reply(f'None / {member.id}')
                    else:
                        await message.reply(f'{member.display_name} / {member.id}')
            elif args[1] in commands['info_item'].split(','):
                if rawcontent2 == '':
                    return await message.reply(f"[{commands['info']}] [{commands['info_item']}] [アイテム名]")
                items=await is_itemname('ja', rawcontent2)
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                    else:
                        for item in items[1]:
                            await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                            print(item[0])
                else:
                    client.ismesenitem=await is_itemname('en', rawcontent2)
                    if client.ismesenitem[0] == 'True':
                        if len(client.ismesenitem[1]) > 29:
                            await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesenitem[1])))
                        else:
                            for item in client.ismesenitem[1]:
                                await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                    else:
                        await message.reply('見つかりません')
            elif args[1] in commands['id'].split(','):
                if rawcontent2 == '':
                    return await message.reply(f"[{commands['info']}] [{commands['id']}] [ID]")
                items=await search_item_with_id('ja', rawcontent2)
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                    else:
                        for item in items[1]:
                            await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                            print(item[0])
                else:
                    client.ismesenitem=await search_item_with_id('en', rawcontent2)
                    if client.ismesenitem[0] == 'True':
                        if len(client.ismesenitem[1]) > 29:
                            await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesenitem[1])))
                        else:
                            for item in client.ismesenitem[1]:
                                await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                    else:
                        await message.reply('見つかりません')
            elif args[1] in commands['skin'].split(','):
                if rawcontent2 == '':
                    return await message.reply(f"[{commands['info']}] [{commands['skin']}] [スキン名]")
                items=await search_item_with_type('ja', rawcontent2, 'outfit')
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                    else:
                        for item in items[1]:
                            await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                            print(item[0])
                else:
                    client.ismesenitem=await search_item_with_type('en', rawcontent2, 'outfit')
                    if client.ismesenitem[0] == 'True':
                        if len(client.ismesenitem[1]) > 29:
                            await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesenitem[1])))
                        else:
                            for item in client.ismesenitem[1]:
                                await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                    else:
                        await message.reply('見つかりません')
            elif args[1] in commands['bag'].split(','):
                if rawcontent2 == '':
                    return await message.reply(f"[{commands['info']}] [{commands['bag']}] [バッグ名]")
                items=await search_item_with_type('ja', rawcontent2, 'backpack,pet')
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                    else:
                        for item in items[1]:
                            await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                            print(item[0])
                else:
                    client.ismesenitem=await search_item_with_type('en', rawcontent2, 'backpack,pet')
                    if client.ismesenitem[0] == 'True':
                        if len(client.ismesenitem[1]) > 29:
                            await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesenitem[1])))
                        else:
                            for item in client.ismesenitem[1]:
                                await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                    else:
                        await message.reply('見つかりません')
            elif args[1] in commands['pickaxe'].split(','):
                if rawcontent2 == '':
                    return await message.reply(f"[{commands['info']}] [{commands['pickaxe']}] [ツルハシ名]")
                items=await search_item_with_type('ja', rawcontent2, 'pickaxe')
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                        print(item[0])
                    else:
                        for item in items[1]:
                            await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                else:
                    client.ismesenitem=await search_item_with_type('en', rawcontent2, 'pickaxe')
                    if client.ismesenitem[0] == 'True':
                        if len(client.ismesenitem[1]) > 29:
                            await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesenitem[1])))
                        else:
                            for item in client.ismesenitem[1]:
                                await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                    else:
                        await message.reply('見つかりません')
            elif args[1] in commands['emote'].split(','):
                if rawcontent2 == '':
                    return await message.reply(f"[{commands['info']}] [{commands['emote']}] [エモート名]")
                items=await search_item_with_type('ja', rawcontent2, 'emote,emoji,toy')
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                    else:
                        for item in items[1]:
                            await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                            print(item[0])
                else:
                    client.ismesenitem=await search_item_with_type('en', rawcontent2, 'emote,emoji,toy')
                    if client.ismesenitem[0] == 'True':
                        if len(client.ismesenitem[1]) > 29:
                            await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesenitem[1])))
                        else:
                            for item in client.ismesenitem[1]:
                                await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                                print(item[0])
                    else:
                        await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
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
                        if friend.display_name is None:
                            await message.reply(f'None / {friend.id} をフレンドに追加')
                        else:
                            await message.reply(f'{friend.display_name} / {friend.id} をフレンドに追加')
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                        if friend.display_name is None:
                            await message.reply(f'None / {friend.id} のフレンド申請の承認リクエストを処理中にエラーが発生しました')
                        else:
                            await message.reply(f'{friend.display_name} / {friend.id} のフレンド申請の承認リクエストを処理中にエラーが発生しました')
                    except Exception:
                        print(red(traceback.format_exc()))
                        await message.reply('エラー')
                        continue
            elif args[1] in commands['false'].split(','):
                for pending in pendings:
                    try:
                        await pending.decline()
                        if friend.display_name is None:
                            await message.reply(f'None / {friend.id} のフレンド申請を拒否')
                        else:
                            await message.reply(f'{friend.display_name} / {friend.id} のフレンド申請を拒否')
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                        if friend.display_name is None:
                            await message.reply(f'None / {friend.id} のフレンド申請の拒否リクエストを処理中にエラーが発生しました')
                        else:
                            await message.reply(f'{friend.display_name} / {friend.id} のフレンド申請の拒否リクエストを処理中にエラーが発生しました')
                    except Exception:
                        print(red(traceback.format_exc()))
                        await message.reply('エラー')
                        continue
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['pending']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['addfriend'].split(','):
        try:
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
            else:
                if client.has_friend(user.id) is True:
                    await message.reply('既にユーザーとフレンドです')
                else:
                    await client.add_friend(user.id)
                    if user.display_name is None:
                        await message.reply(f'None / {user.id} にフレンド申請を送信')
                    else:
                        await message.reply(f'{user.display_name} / {user.id} にフレンド申請を送信')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('フレンド申請の送信リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['addfriend']}] [ユーザー名 / ユーザーID]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['removefriend'].split(','):
        try:
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
            else:
                if client.has_friend(user.id) is False:
                    await message.reply('ユーザーとフレンドではありません')
                else:
                    await client.remove_or_decline_friend(user.id)
                    if user.display_name is None:
                        await message.reply(f'None / {user.id} をフレンドから削除')
                    else:
                        await message.reply(f'{user.display_name} / {user.id} をフレンドから削除')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('フレンドの削除リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['removefriend']}] [ユーザー名 / ユーザーID]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['acceptpending'].split(','):
        try:
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
            else:
                if client.is_pending(user.id) is False:
                    await message.reply('ユーザーからのフレンド申請がありません')
                else:
                    await client.accept_friend(user.id)
                    if user.display_name is None:
                        await message.reply(f'None / {user.id} をフレンドに追加')
                        if data['loglevel'] == 'normal':
                            print(f'[{now_()}] None のフレンド申請を承諾')
                        else:
                            print(f'[{now_()}] None / {user.id} のフレンド申請を承諾')
                    else:
                        await message.reply(f'{user.display_name} / {user.id} をフレンドに追加')
                        if data['loglevel'] == 'normal':
                            print(f'[{now_()}] {user.display_name} のフレンド申請を承諾')
                        else:
                            print(f'[{now_()}] {user.display_name} / {user.id} のフレンド申請を承諾')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('フレンドの追加リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['acceptpending']}] [ユーザー名 / ユーザーID]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['declinepending'].split(','):
        try:
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
            else:
                if client.is_pending(user.id) is False:
                    await message.reply('ユーザーからのフレンド申請がありません')
                else:
                    await client.remove_or_decline_friend(user.id)
                    if user.display_name is None:
                        await message.reply(f'None / {user.id} のフレンド申請を拒否')
                        if data['loglevel'] == 'normal':
                            print(f'[{now_()}] None のフレンド申請を拒否')
                        else:
                            print(f'[{now_()}] None / {user.id} のフレンド申請を拒否')
                    else:
                        await message.reply(f'{user.display_name} / {user.id} のフレンド申請を拒否')
                        if data['loglevel'] == 'normal':
                            print(f'[{now_()}] {user.display_name} のフレンド申請を拒否')
                        else:
                            print(f'[{now_()}] {user.display_name} / {user.id} のフレンド申請を拒否')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('フレンド申請の拒否リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['declinepending']}] [ユーザー名 / ユーザーID]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['blockfriend'].split(','):
        try:
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
            if user is None:
                await message.reply('ユーザーが見つかりません')
            else:
                if not user.id in client.blocked_users.keys():
                    await client.block_user(user.id)
                    if user.display_name is None:
                        await message.reply(f'None / {user.id} をブロック')
                        if data['loglevel'] == 'normal':
                            print(f'[{now_()}] None をブロック')
                        else:
                            print(f'[{now_()}] None / {user.id} をブロック')
                    else:
                        await message.reply(f'{user.display_name} / {user.id} をブロック')
                        if data['loglevel'] == 'normal':
                            print(f'[{now_()}] {user.display_name} をブロック')
                        else:
                            print(f'[{now_()}] {user.display_name} / {user.id} をブロック')
                else:
                    await message.reply('既にユーザーをブロックしています')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('フレンドのブロックリクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['blockfriend']}] [ユーザー名 / ユーザーID]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['unblockfriend'].split(','):
        try:
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
            if user is None:
                await message.reply('ユーザーが見つかりません')
            else:
                if user.id in client.blocked_users.keys():
                    await client.unblock_user(user.id)
                    if user.display_name is None:
                        await message.reply(f'None / {user.id} をブロック解除')
                        if data['loglevel'] == 'normal':
                            print(f'[{now_()}] None をブロック解除')
                        else:
                            print(f'[{now_()}] None / {user.id} をブロック解除')
                    else:
                        await message.reply(f'{user.display_name} / {user.id} をブロック解除')
                        if data['loglevel'] == 'normal':
                            print(f'[{now_()}] {user.display_name} をブロック解除')
                        else:
                            print(f'[{now_()}] {user.display_name} / {user.id} をブロック解除')
                else:
                    await message.reply('ユーザーをブロックしていません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('ブロックしたユーザーのブロック解除リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['unblockfriend']}] [ユーザー名 / ユーザーID]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['chatban'].split(','):
        try:
            reason=rawcontent.split(' : ')
            user=await client.fetch_profile(reason[0])
            if user is None:
                await message.reply('ユーザーが見つかりません')
            else:
                if not user.id in client.user.party.members.keys():
                    await message.reply('ユーザーがパーティーにいません')
                else:
                    member=client.user.party.members.get(user.id)
                    try:
                        await member.chatban(reason[1])
                    except IndexError:
                        await member.chatban()
                    if user.display_name is None:
                        await message.reply(f'None / {user.id} をバン')
                    else:
                        await message.reply(f'{user.display_name} / {user.id} をバン')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーリーダーではありません')
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('メンバーが見つかりません')
        except ValueError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('既にバンされています')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['chatban']}] [ユーザー名 / ユーザーID] : [理由(任意)]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['chatbanme'].split(','):
        try:
            if not message.author.id in client.user.party.members.keys():
                await message.reply('ユーザーがパーティーにいません')
            else:
                member=client.user.party.members.get(message.author.id)
                try:
                    await member.chatban(reason[1])
                except IndexError:
                    await member.chatban()
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーリーダーではありません')
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('メンバーが見つかりません')
        except ValueError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('既にバンされています')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['promote'].split(','):
        try:
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
            if user is None:
                await message.reply('ユーザーが見つかりません')
            else:
                if not user.id in client.user.party.members.keys():
                    await message.reply('ユーザーがパーティーにいません')
                else:
                    member=client.user.party.members.get(user.id)
                    await member.promote()
                    if user.display_name is None:
                        await message.reply(f'None / {user.id} に譲渡')
                    else:
                        await message.reply(f'{user.display_name} / {user.id} に譲渡')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーリーダーではありません')
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('既にパーティーリーダーです')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーリーダーの譲渡リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['promote']}] [ユーザー名 / ユーザーID]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['promoteme'].split(','):
        try:
            if not message.author.id in client.user.party.members.keys():
                await message.reply('ユーザーがパーティーにいません')
            else:
                member=client.user.party.members.get(message.author.id)
                await member.promote()
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーリーダーではありません')
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('既にパーティーリーダーです')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーリーダーの譲渡リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['kick'].split(','):
        try:
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
            if user is None:
                await message.reply('ユーザーが見つかりません')
            else:
                if not user.id in client.user.party.members.keys():
                    await message.reply('ユーザーがパーティーにいません')
                else:
                    member=client.user.party.members.get(user.id)
                    await member.kick()
                    if user.display_name is None:
                        await message.reply(f'None / {user.id} をキック')
                    else:
                        await message.reply(f'{user.display_name} / {user.id} をキック')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーリーダーではありません')
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('自分をキックすることはできません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーメンバーのキックリクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['kick']}] [ユーザー名 / ユーザーID]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['kickme'].split(','):
        try:
            if not message.author.id in client.user.party.members.keys():
                await message.reply('ユーザーがパーティーにいません')
            else:
                member=client.user.party.members.get(message.author.id)
                await member.kick()
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーリーダーではありません')
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('自分をキックすることはできません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーメンバーのキックリクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['ready'].split(','):
        try:
            await client.user.party.me.set_ready(fortnitepy.ReadyState.READY)
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')
    
    elif args[0] in commands['unready'].split(','):
        try:
            await client.user.party.me.set_ready(fortnitepy.ReadyState.NOT_READY)
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['sitout'].split(','):
        try:
            await client.user.party.me.set_ready(fortnitepy.ReadyState.SITTING_OUT)
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['stop'].split(','):
        try:
            client.stopcheck=True
            await client.user.party.me.clear_emote()
            await message.reply('停止しました')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['allskin'].split(','):
        try:
            with open('allen.json', 'r', encoding='utf-8') as f:
                allskin = json.load(f)
            for item in allskin['data']:
                if client.stopcheck == True:
                    client.stopcheck=False
                    await message.reply('停止しました')
                    break
                if item['type'] == 'outfit':
                    await client.user.party.me.set_outfit(item['id'])
                    await asyncio.sleep(2)
            await message.reply('全てのスキンを表示し終わりました')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['allemote'].split(','):
        try:
            with open('allen.json', 'r', encoding='utf-8') as f:
                allemote = json.load(f)
            for item in allemote['data']:
                if client.stopcheck == True:
                    client.stopcheck=False
                    await message.reply('停止しました')
                    break
                if item['type'] == 'emote':
                    await client.user.party.me.set_emote(item['id'])
                    await asyncio.sleep(5)
            else:
                await message.reply('全てのエモートを表示し終わりました')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['id'].split(','):
        if rawcontent == '':
            return await message.reply(f"[{commands['id']}] [ID]")
        try:
            isitem = await search_item_with_id("ja", rawcontent)
            if isitem[0] == 'True':
                client.ismesjaitem=isitem
                if len(client.ismesjaitem[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesjaitem[1])))
                else:
                    for count,item in enumerate(client.ismesjaitem[1]):
                        if item[2] == 'outfit':
                            if len(client.ismesjaitem[1]) == 1:
                                await message.reply(f'スキン: {item[0]}: {item[1]}')
                            else:
                                await message.reply(f'{count+1} スキン: {item[0]}: {item[1]}')
                        if item[2] == 'backpack':
                            if len(client.ismesjaitem[1]) == 1:
                                await message.reply(f'バッグ: {item[0]}: {item[1]}')
                            else:
                                await message.reply(f'{count+1} バッグ: {item[0]}: {item[1]}')
                        if item[2] == 'pet':
                            if len(client.ismesjaitem[1]) == 1:
                                await message.reply(f'バッグ: {item[0]}: {item[1]}')
                            else:
                                await message.reply(f'{count+1} バッグ: {item[0]}: {item[1]}')
                        if item[2] == 'pickaxe':
                            if len(client.ismesjaitem[1]) == 1:
                                await message.reply(f'ツルハシ: {item[0]}: {item[1]}')
                            else:
                                await message.reply(f'{count+1} ツルハシ: {item[0]}: {item[1]}')
                        if item[2] == 'emote':
                            if len(client.ismesjaitem[1]) == 1:
                                await message.reply(f'エモート: {item[0]}: {item[1]}')
                            else:
                                await message.reply(f'{count+1} エモート: {item[0]}: {item[1]}')
                        if item[2] == 'emoji':
                            if len(client.ismesjaitem[1]) == 1:
                                await message.reply(f'エモート: {item[0]}: {item[1]}')
                            else:
                                await message.reply(f'{count+1} エモート: {item[0]}: {item[1]}')
                        if item[2] == 'toy':
                            if len(client.ismesjaitem[1]) == 1:
                                await message.reply(f'エモート: {item[0]}: {item[1]}')
                            else:
                                await message.reply(f'{count+1} エモート: {item[0]}: {item[1]}')
                    if len(client.ismesjaitem[1]) == 1:
                        if client.ismesjaitem[1][0][2] == 'outfit':
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.ismesjaitem[1][0][0]))
                        if client.ismesjaitem[1][0][2] == 'backpack':
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.ismesjaitem[1][0][0]))
                        if client.ismesjaitem[1][0][2] == 'pet':
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.ismesjaitem[1][0][0]))
                        if client.ismesjaitem[1][0][2] == 'pickaxe':
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.ismesjaitem[1][0][0]))
                            await client.user.party.me.set_emote('EID_IceKing')
                        if client.ismesjaitem[1][0][2] == 'emote':
                            if not client.user.party.me.emote is None:
                                if client.user.party.me.emote.lower() == client.ismesjaitem[1][0][0].lower():
                                    await client.user.party.me.clear_emote()
                            await client.user.party.me.set_emote(client.ismesjaitem[1][0][0])
                            client.eid=client.ismesjaitem[1][0][0]
                        if client.ismesjaitem[1][0][2] == 'emoji':
                            await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesjaitem[1][0][0]}.{client.ismesjaitem[1][0][0]}')
                            client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesjaitem[1][0][0]}.{client.ismesjaitem[1][0][0]}'
                        if client.ismesjaitem[1][0][2] == 'toy':
                            await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesjaitem[1][0][0]}.{client.ismesjaitem[1][0][0]}')
                            client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesjaitem[1][0][0]}.{client.ismesjaitem[1][0][0]}'
                    if len(client.ismesjaitem[1]) > 1:
                        await message.reply('数字を入力することでそのアイテムに設定します')
            else:
                await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['skin'].split(','):
        if rawcontent == '':
            return await message.reply(f"[{commands['skin']}] [スキン名]")
        try:
            isitem = await search_item_with_type("ja", rawcontent, "outfit")
            if isitem[0] == 'True':
                client.ismesjaitem=isitem
                if len(client.ismesjaitem[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesjaitem[1])))
                else:
                    for count,item in enumerate(client.ismesjaitem[1]):
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'{item[1]}')
                        else:
                            await message.reply(f'{count+1}: {item[1]}')
                    if len(client.ismesjaitem[1]) == 1:
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.ismesjaitem[1][0][0]))
                    if len(client.ismesjaitem[1]) > 1:
                        await message.reply('数字を入力することでそのアイテムに設定します')
            else:
                isitem = await search_item_with_type("en", rawcontent, "outfit")
                if isitem[0] == 'True':
                    client.ismesenitem=isitem
                    if len(client.ismesenitem[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesenitem[1])))
                    else:
                        for count,item in enumerate(client.ismesenitem[1]):
                            if len(client.ismesenitem[1]) == 1:
                                await message.reply(f'{item[1]}')
                            else:
                                await message.reply(f'{count+1}: {item[1]}')
                        if len(client.ismesenitem[1]) == 1:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.ismesenitem[1][0][0]))
                        if len(client.ismesenitem[1]) > 1:
                            await message.reply('数字を入力することでそのアイテムに設定します')
                else:
                    await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['bag'].split(','):
        if rawcontent == '':
            return await message.reply(f"[{commands['bag']}] [バッグ名]")
        try:
            isitem = await search_item_with_type("ja", rawcontent, "backpack,pet")
            if isitem[0] == 'True':
                client.ismesjaitem=isitem
                if len(client.ismesjaitem[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesjaitem[1])))
                else:
                    for count,item in enumerate(client.ismesjaitem[1]):
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'{item[1]}')
                        else:
                            await message.reply(f'{count+1}: {item[1]}')
                    if len(client.ismesjaitem[1]) == 1:
                        if client.ismesjaitem[1][0][2] == 'backpack':
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.ismesjaitem[1][0][0]))
                        if client.ismesjaitem[1][0][2] == 'pet':
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.ismesjaitem[1][0][0]))
                    if len(client.ismesjaitem[1]) > 1:
                        await message.reply('数字を入力することでそのアイテムに設定します')
            else:
                isitem = await search_item_with_type("en", rawcontent, "backpack,pet")
                if isitem[0] == 'True':
                    client.ismesenitem=isitem
                    if len(client.ismesenitem[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesenitem[1])))
                    else:
                        for count,item in enumerate(client.ismesenitem[1]):
                            if len(client.ismesenitem[1]) == 1:
                                await message.reply(f'{item[1]}')
                            else:
                                await message.reply(f'{count+1}: {item[1]}')
                        if len(client.ismesenitem[1]) == 1:
                            if client.ismesenitem[1][0][2] == 'backpack':
                                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.ismesenitem[1][0][0]))
                            if client.ismesenitem[1][0][2] == 'pet':
                                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.ismesenitem[1][0][0]))
                        if len(client.ismesenitem[1]) > 1:
                            await message.reply('数字を入力することでそのアイテムに設定します')
                else:
                    await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['pickaxe'].split(','):
        if rawcontent == '':
            return await message.reply(f"[{commands['pickaxe']}] [ツルハシ名]]")
        try:
            isitem = await search_item_with_type("ja", rawcontent, "pickaxe")
            if isitem[0] == 'True':
                client.ismesjaitem=isitem
                if len(client.ismesjaitem[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesjaitem[1])))
                else:
                    for count,item in enumerate(client.ismesjaitem[1]):
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'{item[1]}')
                        else:
                            await message.reply(f'{count+1}: {item[1]}')
                    if len(client.ismesjaitem[1]) == 1:
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.ismesjaitem[1][0][0]))
                        await client.user.party.me.set_emote('EID_IceKing')
                    if len(client.ismesjaitem[1]) > 1:
                        await message.reply('数字を入力することでそのアイテムに設定します')
            else:
                isitem = await search_item_with_type("en", rawcontent, "pickaxe")
                if isitem[0] == 'True':
                    client.ismesenitem=isitem
                    if len(client.ismesenitem[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesenitem[1])))
                    else:
                        for count,item in enumerate(client.ismesenitem[1]):
                            if len(client.ismesenitem[1]) == 1:
                                await message.reply(f'{item[1]}')
                            else:
                                await message.reply(f'{count+1}: {item[1]}')
                        if len(client.ismesenitem[1]) == 1:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.ismesenitem[1][0][0]))
                            await client.user.party.me.set_emote('EID_IceKing')
                        if len(client.ismesenitem[1]) > 1:
                            await message.reply('数字を入力することでそのアイテムに設定します')
                else:
                    await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['emote'].split(','):
        if rawcontent == '':
            return await message.reply(f"[{commands['emote']}] [エモート名]]")
        try:
            isitem = await search_item_with_type("ja", rawcontent, "emote,emoji,toy")
            if isitem[0] == 'True':
                client.ismesjaitem=isitem
                if len(client.ismesjaitem[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesjaitem[1])))
                else:
                    for count,item in enumerate(client.ismesjaitem[1]):
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'{item[1]}')
                        else:
                            await message.reply(f'{count+1}: {item[1]}')
                    if len(client.ismesjaitem[1]) == 1:
                        if client.ismesjaitem[1][0][2] == 'emote':
                            await client.user.party.me.set_emote(client.ismesjaitem[1][0][0])
                            client.eid=client.ismesjaitem[1][0][0]
                        if client.ismesjaitem[1][0][2] == 'emoji':
                            await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesjaitem[1][0][0]}.{client.ismesjaitem[1][0][0]}')
                            client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesjaitem[1][0][0]}.{client.ismesjaitem[1][0][0]}'
                        if client.ismesjaitem[1][0][2] == 'toy':
                            await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesjaitem[1][0][0]}.{client.ismesjaitem[1][0][0]}')
                            client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesjaitem[1][0][0]}.{client.ismesjaitem[1][0][0]}'
                    if len(client.ismesjaitem[1]) > 1:
                        await message.reply('数字を入力することでそのアイテムに設定します')
            else:
                isitem = await search_item_with_type("en", rawcontent, "emote,emoji,toy")
                if isitem[0] == 'True':
                    client.ismesenitem=isitem
                    if len(client.ismesenitem[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesenitem[1])))
                    else:
                        for count,item in enumerate(client.ismesenitem[1]):
                            if len(client.ismesenitem[1]) == 1:
                                await message.reply(f'{item[1]}')
                            else:
                                await message.reply(f'{count+1}: {item[1]}')
                        if len(client.ismesenitem[1]) == 1:
                            if client.ismesenitem[1][0][2] == 'emote':
                                await client.user.party.me.set_emote(client.ismesenitem[1][0][0])
                                client.eid=client.ismesenitem[1][0][0]
                            if client.ismesenitem[1][0][2] == 'emoji':
                                await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesenitem[1][0][0]}.{client.ismesenitem[1][0][0]}')
                                client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesenitem[1][0][0]}.{client.ismesenitem[1][0][0]}'
                            if client.ismesenitem[1][0][2] == 'toy':
                                await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesenitem[1][0][0]}.{client.ismesenitem[1][0][0]}')
                                client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesenitem[1][0][0]}.{client.ismesenitem[1][0][0]}'
                        if len(client.ismesenitem[1]) > 1:
                            await message.reply('数字を入力することでそのアイテムに設定します')
                else:
                    await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['set'].split(','):
        if rawcontent == '':
            return await message.reply(f"[{commands['set']}] [セット名]]")
        try:
            isitem = await search_set_item("ja", rawcontent)
            if isitem[0] == 'True':
                client.ismesjaitem=isitem
                for count,item in enumerate(client.ismesjaitem[1]):
                    if item[2] == 'outfit':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'スキン: {item[1]}')
                        else:
                            await message.reply(f'{count+1} スキン: {item[1]}')
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,item[0]))
                    if item[2] == 'backpack':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,item[0]))
                    if item[2] == 'pet':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,item[0]))
                    if item[2] == 'pickaxe':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'ツルハシ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} ツルハシ: {item[1]}')
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,item[0]))
                        await client.user.party.me.set_emote('EID_IceKing')
                    if item[2] == 'emote':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                        await client.user.party.me.set_emote(item[0])
                        client.eid=item[0]
                    if item[2] == 'emoji':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{item[0]}.{item[0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{item[0]}.{item[0]}'
                    if item[2] == 'toy':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{item[0]}.{item[0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{item[0]}.{item[0]}'
                    
            else:
                isitem = await search_set_item("en", rawcontent)
                if isitem[0] == 'True':
                    client.ismesenitem=isitem
                    for count,item in enumerate(client.ismesenitem[1]):
                        if item[2] == 'outfit':
                            if len(client.ismesenitem[1]) == 1:
                                await message.reply(f'スキン: {item[1]}')
                            else:
                                await message.reply(f'{count+1} スキン: {item[1]}')
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,item[0]))
                        if item[2] == 'backpack':
                            if len(client.ismesenitem[1]) == 1:
                                await message.reply(f'バッグ: {item[1]}')
                            else:
                                await message.reply(f'{count+1} バッグ: {item[1]}')
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,item[0]))
                        if item[2] == 'pet':
                            if len(client.ismesenitem[1]) == 1:
                                await message.reply(f'バッグ: {item[1]}')
                            else:
                                await message.reply(f'{count+1} バッグ: {item[1]}')
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,item[0]))
                        if item[2] == 'pickaxe':
                            if len(client.ismesenitem[1]) == 1:
                                await message.reply(f'ツルハシ: {item[1]}')
                            else:
                                await message.reply(f'{count+1} ツルハシ: {item[1]}')
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,item[0]))
                            await client.user.party.me.set_emote('EID_IceKing')
                        if item[2] == 'emote':
                            if len(client.ismesenitem[1]) == 1:
                                await message.reply(f'エモート: {item[1]}')
                            else:
                                await message.reply(f'{count+1} エモート: {item[1]}')
                            await client.user.party.me.set_emote(item[0])
                            client.eid=item[0]
                        if item[2] == 'emoji':
                            if len(client.ismesenitem[1]) == 1:
                                await message.reply(f'エモート: {item[1]}')
                            else:
                                await message.reply(f'{count+1} エモート: {item[1]}')
                            await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{item[0]}.{item[0]}')
                            client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{item[0]}.{item[0]}'
                        if item[2] == 'toy':
                            if len(client.ismesenitem[1]) == 1:
                                await message.reply(f'エモート: {item[1]}')
                            else:
                                await message.reply(f'{count+1} エモート: {item[1]}')
                            await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{item[0]}.{item[0]}')
                            client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{item[0]}.{item[0]}'
                else:
                    await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['variant'].split(','):
        try:
            if len(args) == 4:
                if args[1].startswith('cid_'):
                    variants=client.user.party.me.create_variants(item='AthenaCharacter',**{args[2]: int(args[3])})
                elif args[1].startswith('bid_') or args[1].startswith('petcarrier_'):
                    variants=client.user.party.me.create_variants(item='AthenaBackpack',**{args[2]: int(args[3])})
                elif args[1].startswith('pickaxe_id_'):
                    variants=client.user.party.me.create_variants(item='AthenaPickaxe',**{args[2]: int(args[3])})
            elif len(args) == 6:
                if args[1].startswith('cid_'):
                    variants=client.user.party.me.create_variants(item='AthenaCharacter',**{args[2]: int(args[3])},**{args[4]: int(args[5])})
                elif args[1].startswith('bid_') or args[1].startswith('petcarrier_'):
                    variants=client.user.party.me.create_variants(item='AthenaBackpack',**{args[2]: int(args[3])},**{args[4]: int(args[5])})
                elif args[1].startswith('pickaxe_id_'):
                    variants=client.user.party.me.create_variants(item='AthenaPickaxe',**{args[2]: int(args[3])},**{args[4]: int(args[5])})
            elif len(args) == 8:
                if args[1].startswith('cid_'):
                    variants=client.user.party.me.create_variants(item='AthenaCharacter',**{args[2]: int(args[3])},**{args[4]: int(args[5])},**{args[6]: int(args[7])})
                elif args[1].startswith('bid_') or args[1].startswith('petcarrier_'):
                    variants=client.user.party.me.create_variants(item='AthenaBackpack',**{args[2]: int(args[3])},**{args[4]: int(args[5])},**{args[6]: int(args[7])})
                elif args[1].startswith('pickaxe_id_'):
                    variants=client.user.party.me.create_variants(item='AthenaPickaxe',**{args[2]: int(args[3])},**{args[4]: int(args[5])},**{args[6]: int(args[7])})
            if len(args) == 4 or len(args) == 6 or len(args) == 8:
                if args[1].startswith('cid_'):
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,asset=args[1],variants=variants))
                elif args[1].startswith('bid_'):
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,asset=args[1],variants=variants))
                elif args[1].startswith('petcarrier_'):
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,asset=args[1],variants=variants))
                elif args[1].startswith('pickaxe_id'):
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,asset=args[1],variants=variants))
                    await client.user.party.me.set_emote('EID_IceKing')
            else:
                await message.reply(f"[{commands['variant']}] [variant] [数値]\nvariantと数値は3つまで設定可")
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['skinasset'].split(','):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,rawcontent))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['skinasset']}] [アセットパス]")
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['bagasset'].split(','):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,rawcontent))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['bagasset']}] [アセットパス]")
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['pickaxeasset'].split(','):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,rawcontent))
            await client.user.party.me.set_emote('EID_IceKing')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['pickaxeasset']}] [アセットパス]")
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['emoteasset'].split(','):
        try:
            await client.user.party.me.clear_emote()
            await client.user.party.me.set_emote(args[1])
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['emoteasset']}] [アセットパス]")
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0].lower().startswith('cid_'):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,args[0].upper()))
            await message.reply(f'スキンを {args[0]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0].lower().startswith('bid_'):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,args[0]))
            await message.reply(f'バッグを {args[0]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0].lower().startswith('pet_carrier'):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,args[0]))
            await message.reply(f'バッグを {args[0]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0].lower().startswith('pickaxe_id'):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,args[0]))
            await client.user.party.me.set_emote('EID_IceKing')
            await message.reply(f'ツルハシを {args[0]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0].lower().startswith('eid_'):
        try:
            if not client.user.party.me.emote is None:
                if client.user.party.me.emote.lower() == args[0].lower():
                    await client.user.party.me.clear_emote()
            await client.user.party.me.set_emote(args[0])
            await message.reply(f'エモートを {args[0]} に設定')
            client.eid=args[0]
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0].lower().startswith('emoji_'):
        try:
            if not client.user.party.me.emote is None:
                if client.user.party.me.emote.lower() == args[0].lower():
                    await client.user.party.me.clear_emote()
            await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{args[0]}.{args[0]}')
            await message.reply(f'エモートを {args[0]} に設定')
            client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{args[0]}.{args[0]}'
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0].lower().startswith('toy_'):
        try:
            if not client.user.party.me.emote is None:
                if client.user.party.me.emote.lower() == args[0].lower():
                    await client.user.party.me.clear_emote()
            await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{args[0]}.{args[0]}')
            await message.reply(f'エモートを {args[0]} に設定')
            client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{args[0]}.{args[0]}'
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0].lower().startswith('playlist_'):
        try:
            await client.user.party.set_playlist(args[0])
            await message.reply(f'プレイリストを {args[0]} に設定')
            data['fortnite']['playlist']=args[0]
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーリーダーではありません')
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    else:
        try:
            try:
                if args[0].isdigit() and client.ismesjaitem[0] == 'True':
                    if client.ismesjaitem[1][int(args[0])-1][2] == 'outfit':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.ismesjaitem[1][int(args[0])-1][0]))
                    if client.ismesjaitem[1][int(args[0])-1][2] == 'backpack':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.ismesjaitem[1][int(args[0])-1][0]))
                    if client.ismesjaitem[1][int(args[0])-1][2] == 'pet':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.ismesjaitem[1][int(args[0])-1][0]))
                    if client.ismesjaitem[1][int(args[0])-1][2] == 'pickaxe':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.ismesjaitem[1][int(args[0])-1][0]))
                        await client.user.party.me.set_emote('EID_IceKing')
                    if client.ismesjaitem[1][int(args[0])-1][2] == 'emote':
                        if not client.user.party.me.emote is None:
                            if client.user.party.me.emote.lower() == client.ismesjaitem[1][int(args[0])-1][0].lower():
                                await client.user.party.me.clear_emote()
                        await client.user.party.me.set_emote(client.ismesjaitem[1][int(args[0])-1][0])
                        client.eid=client.ismesjaitem[1][int(args[0])-1][0]
                    if client.ismesjaitem[1][int(args[0])-1][2] == 'emoji':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesjaitem[1][int(args[0])-1][0]}.{client.ismesjaitem[1][int(args[0])-1][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesjaitem[1][int(args[0])-1][0]}.{client.ismesjaitem[1][int(args[0])-1][0]}'
                    if client.ismesjaitem[1][int(args[0])-1][2] == 'toy':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesjaitem[1][int(args[0])-1][0]}.{client.ismesjaitem[1][int(args[0])-1][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesjaitem[1][int(args[0])-1][0]}.{client.ismesjaitem[1][int(args[0])-1][0]}'
                    return
            except AttributeError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
            try:
                if args[0].isdigit() and client.ismesenitem[0] == 'True':
                    if client.ismesenitem[1][int(args[0])-1][2] == 'outfit':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.ismesenitem[1][int(args[0])-1][0]))
                    if client.ismesenitem[1][int(args[0])-1][2] == 'backpack':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.ismesenitem[1][int(args[0])-1][0]))
                    if client.ismesenitem[1][int(args[0])-1][2] == 'pet':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.ismesenitem[1][int(args[0])-1][0]))
                    if client.ismesenitem[1][int(args[0])-1][2] == 'pickaxe':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.ismesenitem[1][int(args[0])-1][0]))
                        await client.user.party.me.set_emote('EID_IceKing')
                    if client.ismesenitem[1][int(args[0])-1][2] == 'emote':
                        if not client.user.party.me.emote is None:
                            if client.user.party.me.emote.lower() == client.ismesenitem[1][int(args[0])-1][0].lower():
                                await client.user.party.me.clear_emote()
                        await client.user.party.me.set_emote(client.ismesenitem[1][int(args[0])-1][0])
                        client.eid=client.ismesenitem[1][int(args[0])-1][0]
                    if client.ismesenitem[1][int(args[0])-1][2] == 'emoji':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesenitem[1][int(args[0])-1][0]}.{client.ismesenitem[1][int(args[0])-1][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesenitem[1][int(args[0])-1][0]}.{client.ismesenitem[1][int(args[0])-1][0]}'
                    if client.ismesenitem[1][int(args[0])-1][2] == 'toy':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesenitem[1][int(args[0])-1][0]}.{client.ismesenitem[1][int(args[0])-1][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesenitem[1][int(args[0])-1][0]}.{client.ismesenitem[1][int(args[0])-1][0]}'
                    return
            except AttributeError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('有効な数字を入力してください')
            return
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')
            return

        try:
            isitem = await is_itemname("ja", message.content)
            if isitem[0] == 'True':
                client.ismesjaitem = isitem
                if len(client.ismesjaitem[1]) > 29:
                    return await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesjaitem[1])))
                for count,item in enumerate(client.ismesjaitem[1]):
                    if item[2] == 'outfit':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'スキン: {item[1]}')
                        else:
                            await message.reply(f'{count+1} スキン: {item[1]}')
                    if item[2] == 'backpack':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                    if item[2] == 'pet':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                    if item[2] == 'pickaxe':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'ツルハシ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} ツルハシ: {item[1]}')
                    if item[2] == 'emote':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                    if item[2] == 'emoji':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                    if item[2] == 'toy':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                if len(client.ismesjaitem[1]) == 1:
                    if client.ismesjaitem[1][0][2] == 'outfit':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.ismesjaitem[1][0][0]))
                    if client.ismesjaitem[1][0][2] == 'backpack':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.ismesjaitem[1][0][0]))
                    if client.ismesjaitem[1][0][2] == 'pet':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.ismesjaitem[1][0][0]))
                    if client.ismesjaitem[1][0][2] == 'pickaxe':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.ismesjaitem[1][0][0]))
                        await client.user.party.me.set_emote('EID_IceKing')
                    if client.ismesjaitem[1][0][2] == 'emote':
                        if not client.user.party.me.emote is None:
                            if client.user.party.me.emote.lower() == client.ismesjaitem[1][0][0].lower():
                                await client.user.party.me.clear_emote()
                        await client.user.party.me.set_emote(client.ismesjaitem[1][0][0])
                        client.eid=client.ismesjaitem[1][0][0]
                    if client.ismesjaitem[1][0][2] == 'emoji':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesjaitem[1][0][0]}.{client.ismesjaitem[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesjaitem[1][0][0]}.{client.ismesjaitem[1][0][0]}'
                    if client.ismesjaitem[1][0][2] == 'toy':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesjaitem[1][0][0]}.{client.ismesjaitem[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesjaitem[1][0][0]}.{client.ismesjaitem[1][0][0]}'
                if len(client.ismesjaitem[1]) > 1:
                    await message.reply('数字を入力することでそのアイテムに設定します')
                return
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
            return
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')
            return

        try:
            isitem = await is_itemname("en", message.content)
            if isitem[0] == 'True':
                client.ismesenitem = isitem
                if len(client.ismesenitem[1]) > 29:
                    return await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesenitem[1])))
                for count,item in enumerate(client.ismesenitem[1]):
                    if item[2] == 'outfit':
                        if len(client.ismesenitem[1]) == 1:
                            await message.reply(f'スキン: {item[1]}')
                        else:
                            await message.reply(f'{count+1} スキン: {item[1]}')
                    if item[2] == 'backpack':
                        if len(client.ismesenitem[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                    if item[2] == 'pet':
                        if len(client.ismesenitem[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                    if item[2] == 'pickaxe':
                        if len(client.ismesenitem[1]) == 1:
                            await message.reply(f'ツルハシ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} ツルハシ: {item[1]}')
                    if item[2] == 'emote':
                        if len(client.ismesenitem[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                    if item[2] == 'emoji':
                        if len(client.ismesenitem[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                    if item[2] == 'toy':
                        if len(client.ismesenitem[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                if len(client.ismesenitem[1]) == 1:
                    if client.ismesenitem[1][0][2] == 'outfit':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.ismesenitem[1][0][0]))
                    if client.ismesenitem[1][0][2] == 'backpack':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.ismesenitem[1][0][0]))
                    if client.ismesenitem[1][0][2] == 'pet':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.ismesenitem[1][0][0]))
                    if client.ismesenitem[1][0][2] == 'pickaxe':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.ismesenitem[1][0][0]))
                        await client.user.party.me.set_emote('EID_IceKing')
                    if client.ismesenitem[1][0][2] == 'emote':
                        if not client.user.party.me.emote is None:
                            if client.user.party.me.emote.lower() == client.ismesenitem[1][0][0].lower():
                                await client.user.party.me.clear_emote()
                        await client.user.party.me.set_emote(client.ismesenitem[1][0][0])
                        client.eid=client.ismesenitem[1][0][0]
                    if client.ismesenitem[1][0][2] == 'emoji':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesenitem[1][0][0]}.{client.ismesenitem[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesenitem[1][0][0]}.{client.ismesenitem[1][0][0]}'
                    if client.ismesenitem[1][0][2] == 'toy':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesenitem[1][0][0]}.{client.ismesenitem[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesenitem[1][0][0]}.{client.ismesenitem[1][0][0]}'
                if len(client.ismesenitem[1]) > 1:
                    await message.reply('数字を入力することでそのアイテムに設定します')
                return
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
            return
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')
            return

#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================

async def event_party_message(message):
    client=message.client
    if data['caseinsensitive'] is True:
        args = jaconv.kata2hira(message.content.lower()).split()
    else:
        args = message.content.split()
    rawargs = message.content.split()
    rawcontent = ' '.join(rawargs[1:])
    rawcontent2 = ' '.join(rawargs[2:])
    user=None
    if client.partychat is False and message.author.id == client.user.id:
        return
    if data['loglevel'] == 'normal':
        if message.author.display_name is None:
            print(f'[{now_()}] [パーティー] [{client.user.display_name}] None | {message.content}')
        else:
            print(f'[{now_()}] [パーティー] [{client.user.display_name}] {message.author.display_name} | {message.content}')
    else:
        if message.author.display_name is None:
            print(f'[{now_()}] [パーティー/{client.user.party.id}] [{client.user.display_name}] None / {message.author.id} [{platform_to_str(message.author.platform)}/{message.author.input}] | {message.content}')
        else:
            print(f'[{now_()}] [パーティー/{client.user.party.id}] [{client.user.display_name}] {message.author.display_name} / {message.author.id} [{platform_to_str(message.author.platform)}/{message.author.input}] | {message.content}')

    if args[0] in commands['prev'].split(','):
        args = jaconv.kata2hira(client.prevmessage.lower()).split()
        rawargs = client.prevmessage.split()
        rawcontent = ' '.join(rawargs[1:])
    client.prevmessage=message.content

    if args[0] in commands['restart'].split(','):
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
            await message.reply('エラー')

    elif args[0] in commands['relogin'].split(','):
        try:
            await message.reply('アカウントに再ログインします...')
            await client.restart()
        except fortnitepy.AuthException:
            print(red(traceback.format_exc()))
            print(red(f'[{now_()}] メールアドレスまたはパスワードが間違っています。'))
            exit()
        except Exception:
            print(red(traceback.format_exc()))
            print(red(f'[{now_()}] アカウントの読み込みに失敗しました。もう一度試してみてください。'))
            exit()

    elif args[0] in commands['reload'].split(','):
        result=reload_configs(client)
        try:
            if result == 'Success':
                await message.reply('正常に読み込みが完了しました')
            else:
                await message.reply('エラー')
            try:
                client.owner=None
                owner=await client.fetch_profile(data['fortnite']['owner'])
                if owner is None:
                    print(red(f'[{now_()}] 所有者が見つかりません。正しい名前/IDになっているか確認してください。'))
                else:
                    client.owner=client.get_friend(owner.id)
                    if client.owner is None:
                        try:
                            await client.add_friend(owner.id)
                        except fortnitepy.HTTPException:
                            if data['loglevel'] == 'debug':
                                print(red(traceback.format_exc()))
                        except Exception:
                            if data['loglevel'] == 'debug':
                                print(red(traceback.format_exc()))
                        print(red(f'[{now_()}] 所有者とフレンドではありません。フレンドになってからもう一度起動してください。'))
                    else:
                        if data['loglevel'] == 'normal':
                            print(green(f'[{now_()}] 所有者: {client.owner.display_name}'))
                        else:
                            print(green(f'[{now_()}] 所有者: {client.owner.display_name} / {client.owner.id}'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                print(red(f'[{now_()}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['get'].split(','):
        await message.reply(f'{client.user.party.leader.display_name}\n{client.user.party.leader.pickaxe}\n{client.user.party.leader.pickaxe_variants}')

    elif args[0] in commands['friendcount'].split(','):
        try:
            print(f'フレンド数: {len(client.friends)}')
            await message.reply(f'フレンド数: {len(client.friends)}')
        except Exception:
            print(red(traceback.format_exc()))
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
            await message.reply(f"[{commands['skinmimic']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
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
            await message.reply(f"[{commands['emotemimic']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
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
            await message.reply(f"[{commands['party']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
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
            await message.reply(f"[{commands['acceptinvite']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
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
            await message.reply(f"[{commands['acceptfriend']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
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
            await message.reply(f"[{commands['joinmessageenable']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
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
            await message.reply(f"[{commands['randommessageenable']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['wait'].split(','):
        try:
            if not client.owner is None:
                if client.owner.id in client.user.party.members.keys() and not message.author.id == client.owner.id:
                    await message.reply('現在利用できません')
                else:
                    client.acceptinvite=False
                    try:
                        client.timer_.cancel()
                    except Exception:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                    client.timer_=Timer(data['fortnite']['waitinterval'], inviteaccept, [client])
                    client.timer_.start()
                    await message.reply(f"{str(data['fortnite']['waitinterval'])}秒間招待を拒否します")
            else:
                client.acceptinvite=False
                try:
                    client.timer_.cancel()
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                client.timer_=Timer(data['fortnite']['waitinterval'], inviteaccept, [client])
                client.timer_.start()
                await message.reply(f"{str(data['fortnite']['waitinterval'])}秒間招待を拒否します")
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['join'].split(','):
        try:
            await client.join_to_party(party_id=args[1])
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('既にこのパーティーのメンバーです')
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーが見つかりません')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーがプライベートです')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['join']}] [party_id]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['leave'].split(','):
        try:
            await client.user.party.me.leave()
            await message.reply('パーティーを離脱')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティー離脱のリクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['invite'].split(','):
        try:
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
            else:
                friend=client.get_friend(user.id)
                if friend is None:
                    friend=client.get_friend(rawcontent)
                    if friend is None:
                        await message.reply('ユーザーとフレンドではありません')
                if not friend is None:
                    try:
                        await friend.invite()
                        if data['loglevel'] == 'normal':
                            await message.reply(f'{friend.display_name} をパーティーに招待')
                        else:
                            await message.reply(f'{friend.display_name} / {friend.id} をパーティー {client.user.party.id} に招待')
                    except fortnitepy.PartyError:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                        await message.reply('パーティーが満員か、既にパーティーにいます')
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                        await message.reply('パーティー招待の送信リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['invite']}] [ユーザー名 / ユーザーID]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['inviteme'].split(','):
        try:
            await message.author.invite()
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーが満員か、既にパーティーにいます')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティー招待の送信リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['message'].split(','):
        try:
            send=rawcontent.split(' : ')
            user=await client.fetch_profile(send[0])
            if user is None:
                await message.reply('ユーザーが見つかりません')
            else:
                friend=client.get_friend(user.id)
                if friend is None:
                    friend=client.get_friend(send[0])
                    if friend is None:
                        await message.reply('ユーザーとフレンドではありません')
                if not friend is None:
                    await friend.send(send[1])
                    if data['loglevel'] == 'normal':
                        await message.reply(f'{friend.display_name} にメッセージ {send[1]} を送信')
                    else:
                        await message.reply(f'{friend.display_name} / {friend.id} にメッセージ {send[1]} を送信')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['message']}] [ユーザー名 / ユーザーID] : [内容]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['partymessage'].split(','):
        try:
            await client.user.party.send(rawcontent)
            if data['loglevel'] == 'normal':
                await message.reply(f'パーティーにメッセージ {rawcontent} を送信')
            else:
                await message.reply(f'パーティー {client.user.party.id} にメッセージ {rawcontent} を送信')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['partymessage']}] [内容]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['status'].split(','):
        try:
            await client.set_status(rawcontent)
            await message.reply(f'ステータスを {rawcontent} に設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['status']}] [内容]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['banner'].split(','):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_banner,args[1],args[2],client.user.party.me.banner[2]))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('バナー情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['banner']}] [バナーID] [バナーの色]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['level'].split(','):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_banner,client.user.party.me.banner[0],client.user.party.me.banner[1],int(args[1])))
            await message.reply(f'レベルを {args[1]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('レベルの設定リクエストを処理中にエラーが発生しました')
        except ValueError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('数字を入力してください')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['level']}] [レベル]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')
    
    elif args[0] in commands['bp'].split(','):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_battlepass_info,True,args[1],args[2],args[3]))
            await message.reply(f'バトルパス情報を ティア: {args[1]} XPブースト: {args[2]} フレンドXPブースト: {args[3]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('バトルパス情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['bp']}] [ティア] [XPブースト] [フレンドXPブースト]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['user'].split(','):
        try:
            user=await client.fetch_profile(rawcontent)
            if user is None:
                await message.reply('ユーザーが見つかりません')
            else:
                if user.display_name is None:
                    print(f'None / {user.id}')
                    await message.reply(f'None / {user.id}')
                else:
                    print(f'{user.display_name} / {user.id}')
                    await message.reply(f'{user.display_name} / {user.id}')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['user']}] [ユーザー名 / ユーザーID]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['friend'].split(','):
        try:
            user=await client.fetch_profile(rawcontent)
            if user is None:
                await message.reply('ユーザーが見つかりません')
            else:
                friend=client.get_friend(user.id)
                if friend is None:
                    await message.reply('ユーザーとフレンドではありません')
                else:
                    if friend.nickname is None:
                        if friend.display_name is None:
                            print(f'None / {friend.id}')
                            await message.reply(f'None / {friend.id}')
                        else:
                            print(f'{friend.display_name} / {friend.id}')
                            await message.reply(f'{friend.display_name} / {friend.id}')
                    else:
                        if friend.display_name is None:
                            print(f'{friend.nickname}(None) / {friend.id}')
                            await message.reply(f'{friend.nickname}(None) / {friend.id}')
                        else:
                            print(f'{friend.nickname}({friend.display_name}) / {friend.id}')
                            await message.reply(f'{friend.nickname}({friend.display_name}) / {friend.id}')
                    if not friend.last_logout is None:
                        await message.reply('最後のログイン: {0.year}年{0.month}月{0.day}日 {0.hour}時{0.minute}分{0.second}秒'.format(friend.last_logout))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['friend']}] [ユーザー名 / ユーザーID]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['info'].split(','):
        try:
            if args[1] in commands['info_party'].split(','):
                await message.reply(f'{client.user.party.id}\n人数: {client.user.party.member_count}')
                for member in client.user.party.members.values():
                    if member.display_name is None:
                        await message.reply(f'None / {member.id}')
                    else:
                        await message.reply(f'{member.display_name} / {member.id}')
            elif args[1] in commands['info_item'].split(','):
                if rawcontent2 == '':
                    return await message.reply(f"[{commands['info']}] [{commands['info_item']}] [アイテム名]")
                items=await is_itemname('ja', rawcontent2)
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                    else:
                        for item in items[1]:
                            await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                            print(item[0])
                else:
                    client.ismesenitem=await is_itemname('en', rawcontent2)
                    if client.ismesenitem[0] == 'True':
                        if len(client.ismesenitem[1]) > 29:
                            await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesenitem[1])))
                        else:
                            for item in client.ismesenitem[1]:
                                await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                    else:
                        await message.reply('見つかりません')
            elif args[1] in commands['id'].split(','):
                if rawcontent2 == '':
                    return await message.reply(f"[{commands['info']}] [{commands['id']}] [ID]")
                items=await search_item_with_id('ja', rawcontent2)
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                    else:
                        for item in items[1]:
                            await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                            print(item[0])
                else:
                    client.ismesenitem=await search_item_with_id('en', rawcontent2)
                    if client.ismesenitem[0] == 'True':
                        if len(client.ismesenitem[1]) > 29:
                            await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesenitem[1])))
                        else:
                            for item in client.ismesenitem[1]:
                                await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                    else:
                        await message.reply('見つかりません')
            elif args[1] in commands['skin'].split(','):
                if rawcontent2 == '':
                    return await message.reply(f"[{commands['info']}] [{commands['skin']}] [スキン名]")
                items=await search_item_with_type('ja', rawcontent2, 'outfit')
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                    else:
                        for item in items[1]:
                            await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                            print(item[0])
                else:
                    client.ismesenitem=await search_item_with_type('en', rawcontent2, 'outfit')
                    if client.ismesenitem[0] == 'True':
                        if len(client.ismesenitem[1]) > 29:
                            await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesenitem[1])))
                        else:
                            for item in client.ismesenitem[1]:
                                await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                    else:
                        await message.reply('見つかりません')
            elif args[1] in commands['bag'].split(','):
                if rawcontent2 == '':
                    return await message.reply(f"[{commands['info']}] [{commands['bag']}] [バッグ名]")
                items=await search_item_with_type('ja', rawcontent2, 'backpack,pet')
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                    else:
                        for item in items[1]:
                            await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                            print(item[0])
                else:
                    client.ismesenitem=await search_item_with_type('en', rawcontent2, 'backpack,pet')
                    if client.ismesenitem[0] == 'True':
                        if len(client.ismesenitem[1]) > 29:
                            await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesenitem[1])))
                        else:
                            for item in client.ismesenitem[1]:
                                await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                    else:
                        await message.reply('見つかりません')
            elif args[1] in commands['pickaxe'].split(','):
                if rawcontent2 == '':
                    return await message.reply(f"[{commands['info']}] [{commands['pickaxe']}] [ツルハシ名]")
                items=await search_item_with_type('ja', rawcontent2, 'pickaxe')
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                        print(item[0])
                    else:
                        for item in items[1]:
                            await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                else:
                    client.ismesenitem=await search_item_with_type('en', rawcontent2, 'pickaxe')
                    if client.ismesenitem[0] == 'True':
                        if len(client.ismesenitem[1]) > 29:
                            await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesenitem[1])))
                        else:
                            for item in client.ismesenitem[1]:
                                await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                    else:
                        await message.reply('見つかりません')
            elif args[1] in commands['emote'].split(','):
                if rawcontent2 == '':
                    return await message.reply(f"[{commands['info']}] [{commands['emote']}] [エモート名]")
                items=await search_item_with_type('ja', rawcontent2, 'emote,emoji,toy')
                if items[0] == 'True':
                    if len(items[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(items[1])))
                    else:
                        for item in items[1]:
                            await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                            print(item[0])
                else:
                    client.ismesenitem=await search_item_with_type('en', rawcontent2, 'emote,emoji,toy')
                    if client.ismesenitem[0] == 'True':
                        if len(client.ismesenitem[1]) > 29:
                            await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesenitem[1])))
                        else:
                            for item in client.ismesenitem[1]:
                                await message.reply(f'{item[0]}: {item[1]}\n{item[3]}\n{item[4]}')
                                print(item[0])
                    else:
                        await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
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
                        if friend.display_name is None:
                            await message.reply(f'None / {friend.id} をフレンドに追加')
                        else:
                            await message.reply(f'{friend.display_name} / {friend.id} をフレンドに追加')
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                        if friend.display_name is None:
                            await message.reply(f'None / {friend.id} のフレンド申請の承認リクエストを処理中にエラーが発生しました')
                        else:
                            await message.reply(f'{friend.display_name} / {friend.id} のフレンド申請の承認リクエストを処理中にエラーが発生しました')
                    except Exception:
                        print(red(traceback.format_exc()))
                        await message.reply('エラー')
                        continue
            elif args[1] in commands['false'].split(','):
                for pending in pendings:
                    try:
                        await pending.decline()
                        if friend.display_name is None:
                            await message.reply(f'None / {friend.id} のフレンド申請を拒否')
                        else:
                            await message.reply(f'{friend.display_name} / {friend.id} のフレンド申請を拒否')
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                        if friend.display_name is None:
                            await message.reply(f'None / {friend.id} のフレンド申請の拒否リクエストを処理中にエラーが発生しました')
                        else:
                            await message.reply(f'{friend.display_name} / {friend.id} のフレンド申請の拒否リクエストを処理中にエラーが発生しました')
                    except Exception:
                        print(red(traceback.format_exc()))
                        await message.reply('エラー')
                        continue
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['pending']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['addfriend'].split(','):
        try:
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
            else:
                if client.has_friend(user.id) is True:
                    await message.reply('既にユーザーとフレンドです')
                else:
                    await client.add_friend(user.id)
                    if user.display_name is None:
                        await message.reply(f'None / {user.id} にフレンド申請を送信')
                    else:
                        await message.reply(f'{user.display_name} / {user.id} にフレンド申請を送信')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('フレンド申請の送信リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['addfriend']}] [ユーザー名 / ユーザーID]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['removefriend'].split(','):
        try:
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
            else:
                if client.has_friend(user.id) is False:
                    await message.reply('ユーザーとフレンドではありません')
                else:
                    await client.remove_or_decline_friend(user.id)
                    if user.display_name is None:
                        await message.reply(f'None / {user.id} をフレンドから削除')
                    else:
                        await message.reply(f'{user.display_name} / {user.id} をフレンドから削除')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('フレンドの削除リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['removefriend']}] [ユーザー名 / ユーザーID]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['acceptpending'].split(','):
        try:
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
            else:
                if client.is_pending(user.id) is False:
                    await message.reply('ユーザーからのフレンド申請がありません')
                else:
                    await client.accept_friend(user.id)
                    if user.display_name is None:
                        await message.reply(f'None / {user.id} をフレンドに追加')
                        if data['loglevel'] == 'normal':
                            print(f'[{now_()}] None のフレンド申請を承諾')
                        else:
                            print(f'[{now_()}] None / {user.id} のフレンド申請を承諾')
                    else:
                        await message.reply(f'{user.display_name} / {user.id} をフレンドに追加')
                        if data['loglevel'] == 'normal':
                            print(f'[{now_()}] {user.display_name} のフレンド申請を承諾')
                        else:
                            print(f'[{now_()}] {user.display_name} / {user.id} のフレンド申請を承諾')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('フレンドの追加リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['acceptpending']}] [ユーザー名 / ユーザーID]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['declinepending'].split(','):
        try:
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
                return
            if user is None:
                await message.reply('ユーザーが見つかりません')
            else:
                if client.is_pending(user.id) is False:
                    await message.reply('ユーザーからのフレンド申請がありません')
                else:
                    await client.remove_or_decline_friend(user.id)
                    if user.display_name is None:
                        await message.reply(f'None / {user.id} のフレンド申請を拒否')
                        if data['loglevel'] == 'normal':
                            print(f'[{now_()}] None のフレンド申請を拒否')
                        else:
                            print(f'[{now_()}] None / {user.id} のフレンド申請を拒否')
                    else:
                        await message.reply(f'{user.display_name} / {user.id} のフレンド申請を拒否')
                        if data['loglevel'] == 'normal':
                            print(f'[{now_()}] {user.display_name} のフレンド申請を拒否')
                        else:
                            print(f'[{now_()}] {user.display_name} / {user.id} のフレンド申請を拒否')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('フレンド申請の拒否リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['declinepending']}] [ユーザー名 / ユーザーID]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['blockfriend'].split(','):
        try:
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
            if user is None:
                await message.reply('ユーザーが見つかりません')
            else:
                if not user.id in client.blocked_users.keys():
                    await client.block_user(user.id)
                    if user.display_name is None:
                        await message.reply(f'None / {user.id} をブロック')
                        if data['loglevel'] == 'normal':
                            print(f'[{now_()}] None をブロック')
                        else:
                            print(f'[{now_()}] None / {user.id} をブロック')
                    else:
                        await message.reply(f'{user.display_name} / {user.id} をブロック')
                        if data['loglevel'] == 'normal':
                            print(f'[{now_()}] {user.display_name} をブロック')
                        else:
                            print(f'[{now_()}] {user.display_name} / {user.id} をブロック')
                else:
                    await message.reply('既にユーザーをブロックしています')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('フレンドのブロックリクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['blockfriend']}] [ユーザー名 / ユーザーID]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['unblockfriend'].split(','):
        try:
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
            if user is None:
                await message.reply('ユーザーが見つかりません')
            else:
                if user.id in client.blocked_users.keys():
                    await client.unblock_user(user.id)
                    if user.display_name is None:
                        await message.reply(f'None / {user.id} をブロック解除')
                        if data['loglevel'] == 'normal':
                            print(f'[{now_()}] None をブロック解除')
                        else:
                            print(f'[{now_()}] None / {user.id} をブロック解除')
                    else:
                        await message.reply(f'{user.display_name} / {user.id} をブロック解除')
                        if data['loglevel'] == 'normal':
                            print(f'[{now_()}] {user.display_name} をブロック解除')
                        else:
                            print(f'[{now_()}] {user.display_name} / {user.id} をブロック解除')
                else:
                    await message.reply('ユーザーをブロックしていません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('ブロックしたユーザーのブロック解除リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['unblockfriend']}] [ユーザー名 / ユーザーID]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['chatban'].split(','):
        try:
            reason=rawcontent.split(' : ')
            user=await client.fetch_profile(reason[0])
            if user is None:
                await message.reply('ユーザーが見つかりません')
            else:
                if not user.id in client.user.party.members.keys():
                    await message.reply('ユーザーがパーティーにいません')
                else:
                    member=client.user.party.members.get(user.id)
                    try:
                        await member.chatban(reason[1])
                    except IndexError:
                        await member.chatban()
                    if user.display_name is None:
                        await message.reply(f'None / {user.id} をバン')
                    else:
                        await message.reply(f'{user.display_name} / {user.id} をバン')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーリーダーではありません')
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('メンバーが見つかりません')
        except ValueError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('既にバンされています')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['chatban']}] [ユーザー名 / ユーザーID] : [理由(任意)]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['chatbanme'].split(','):
        try:
            if not message.author.id in client.user.party.members.keys():
                await message.reply('ユーザーがパーティーにいません')
            else:
                member=client.user.party.members.get(message.author.id)
                try:
                    await member.chatban(reason[1])
                except IndexError:
                    await member.chatban()
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーリーダーではありません')
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('メンバーが見つかりません')
        except ValueError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('既にバンされています')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['promote'].split(','):
        try:
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
            if user is None:
                await message.reply('ユーザーが見つかりません')
            else:
                if not user.id in client.user.party.members.keys():
                    await message.reply('ユーザーがパーティーにいません')
                else:
                    member=client.user.party.members.get(user.id)
                    await member.promote()
                    if user.display_name is None:
                        await message.reply(f'None / {user.id} に譲渡')
                    else:
                        await message.reply(f'{user.display_name} / {user.id} に譲渡')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーリーダーではありません')
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('既にパーティーリーダーです')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーリーダーの譲渡リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['promote']}] [ユーザー名 / ユーザーID]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['promoteme'].split(','):
        try:
            if not message.author.id in client.user.party.members.keys():
                await message.reply('ユーザーがパーティーにいません')
            else:
                member=client.user.party.members.get(message.author.id)
                await member.promote()
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーリーダーではありません')
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('既にパーティーリーダーです')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーリーダーの譲渡リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['kick'].split(','):
        try:
            try:
                user=await client.fetch_profile(rawcontent)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                await message.reply('ユーザー情報のリクエストを処理中にエラーが発生しました')
            if user is None:
                await message.reply('ユーザーが見つかりません')
            else:
                if not user.id in client.user.party.members.keys():
                    await message.reply('ユーザーがパーティーにいません')
                else:
                    member=client.user.party.members.get(user.id)
                    await member.kick()
                    if user.display_name is None:
                        await message.reply(f'None / {user.id} をキック')
                    else:
                        await message.reply(f'{user.display_name} / {user.id} をキック')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーリーダーではありません')
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('自分をキックすることはできません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーメンバーのキックリクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['kick']}] [ユーザー名 / ユーザーID]")
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['kickme'].split(','):
        try:
            if not message.author.id in client.user.party.members.keys():
                await message.reply('ユーザーがパーティーにいません')
            else:
                member=client.user.party.members.get(message.author.id)
                await member.kick()
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーリーダーではありません')
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('自分をキックすることはできません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーメンバーのキックリクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['ready'].split(','):
        try:
            await client.user.party.me.set_ready(fortnitepy.ReadyState.READY)
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')
    
    elif args[0] in commands['unready'].split(','):
        try:
            await client.user.party.me.set_ready(fortnitepy.ReadyState.NOT_READY)
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['sitout'].split(','):
        try:
            await client.user.party.me.set_ready(fortnitepy.ReadyState.SITTING_OUT)
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['stop'].split(','):
        try:
            client.stopcheck=True
            await client.user.party.me.clear_emote()
            await message.reply('停止しました')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['allskin'].split(','):
        try:
            with open('allen.json', 'r', encoding='utf-8') as f:
                allskin = json.load(f)
            for item in allskin['data']:
                if client.stopcheck == True:
                    client.stopcheck=False
                    await message.reply('停止しました')
                    break
                if item['type'] == 'outfit':
                    await client.user.party.me.set_outfit(item['id'])
                    await asyncio.sleep(2)
            await message.reply('全てのスキンを表示し終わりました')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['allemote'].split(','):
        try:
            with open('allen.json', 'r', encoding='utf-8') as f:
                allemote = json.load(f)
            for item in allemote['data']:
                if client.stopcheck == True:
                    client.stopcheck=False
                    await message.reply('停止しました')
                    break
                if item['type'] == 'emote':
                    await client.user.party.me.set_emote(item['id'])
                    await asyncio.sleep(5)
            else:
                await message.reply('全てのエモートを表示し終わりました')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['id'].split(','):
        if rawcontent == '':
            return await message.reply(f"[{commands['id']}] [ID]")
        try:
            isitem = await search_item_with_id("ja", rawcontent)
            if isitem[0] == 'True':
                client.ismesjaitem=isitem
                if len(client.ismesjaitem[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesjaitem[1])))
                else:
                    for count,item in enumerate(client.ismesjaitem[1]):
                        if item[2] == 'outfit':
                            if len(client.ismesjaitem[1]) == 1:
                                await message.reply(f'スキン: {item[0]}: {item[1]}')
                            else:
                                await message.reply(f'{count+1} スキン: {item[0]}: {item[1]}')
                        if item[2] == 'backpack':
                            if len(client.ismesjaitem[1]) == 1:
                                await message.reply(f'バッグ: {item[0]}: {item[1]}')
                            else:
                                await message.reply(f'{count+1} バッグ: {item[0]}: {item[1]}')
                        if item[2] == 'pet':
                            if len(client.ismesjaitem[1]) == 1:
                                await message.reply(f'バッグ: {item[0]}: {item[1]}')
                            else:
                                await message.reply(f'{count+1} バッグ: {item[0]}: {item[1]}')
                        if item[2] == 'pickaxe':
                            if len(client.ismesjaitem[1]) == 1:
                                await message.reply(f'ツルハシ: {item[0]}: {item[1]}')
                            else:
                                await message.reply(f'{count+1} ツルハシ: {item[0]}: {item[1]}')
                        if item[2] == 'emote':
                            if len(client.ismesjaitem[1]) == 1:
                                await message.reply(f'エモート: {item[0]}: {item[1]}')
                            else:
                                await message.reply(f'{count+1} エモート: {item[0]}: {item[1]}')
                        if item[2] == 'emoji':
                            if len(client.ismesjaitem[1]) == 1:
                                await message.reply(f'エモート: {item[0]}: {item[1]}')
                            else:
                                await message.reply(f'{count+1} エモート: {item[0]}: {item[1]}')
                        if item[2] == 'toy':
                            if len(client.ismesjaitem[1]) == 1:
                                await message.reply(f'エモート: {item[0]}: {item[1]}')
                            else:
                                await message.reply(f'{count+1} エモート: {item[0]}: {item[1]}')
                    if len(client.ismesjaitem[1]) == 1:
                        if client.ismesjaitem[1][0][2] == 'outfit':
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.ismesjaitem[1][0][0]))
                        if client.ismesjaitem[1][0][2] == 'backpack':
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.ismesjaitem[1][0][0]))
                        if client.ismesjaitem[1][0][2] == 'pet':
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.ismesjaitem[1][0][0]))
                        if client.ismesjaitem[1][0][2] == 'pickaxe':
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.ismesjaitem[1][0][0]))
                            await client.user.party.me.set_emote('EID_IceKing')
                        if client.ismesjaitem[1][0][2] == 'emote':
                            if not client.user.party.me.emote is None:
                                if client.user.party.me.emote.lower() == client.ismesjaitem[1][0][0].lower():
                                    await client.user.party.me.clear_emote()
                            await client.user.party.me.set_emote(client.ismesjaitem[1][0][0])
                            client.eid=client.ismesjaitem[1][0][0]
                        if client.ismesjaitem[1][0][2] == 'emoji':
                            await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesjaitem[1][0][0]}.{client.ismesjaitem[1][0][0]}')
                            client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesjaitem[1][0][0]}.{client.ismesjaitem[1][0][0]}'
                        if client.ismesjaitem[1][0][2] == 'toy':
                            await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesjaitem[1][0][0]}.{client.ismesjaitem[1][0][0]}')
                            client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesjaitem[1][0][0]}.{client.ismesjaitem[1][0][0]}'
                    if len(client.ismesjaitem[1]) > 1:
                        await message.reply('数字を入力することでそのアイテムに設定します')
            else:
                await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['skin'].split(','):
        if rawcontent == '':
            return await message.reply(f"[{commands['skin']}] [スキン名]")
        try:
            isitem = await search_item_with_type("ja", rawcontent, "outfit")
            if isitem[0] == 'True':
                client.ismesjaitem=isitem
                if len(client.ismesjaitem[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesjaitem[1])))
                else:
                    for count,item in enumerate(client.ismesjaitem[1]):
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'{item[1]}')
                        else:
                            await message.reply(f'{count+1}: {item[1]}')
                    if len(client.ismesjaitem[1]) == 1:
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.ismesjaitem[1][0][0]))
                    if len(client.ismesjaitem[1]) > 1:
                        await message.reply('数字を入力することでそのアイテムに設定します')
            else:
                isitem = await search_item_with_type("en", rawcontent, "outfit")
                if isitem[0] == 'True':
                    client.ismesenitem=isitem
                    if len(client.ismesenitem[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesenitem[1])))
                    else:
                        for count,item in enumerate(client.ismesenitem[1]):
                            if len(client.ismesenitem[1]) == 1:
                                await message.reply(f'{item[1]}')
                            else:
                                await message.reply(f'{count+1}: {item[1]}')
                        if len(client.ismesenitem[1]) == 1:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.ismesenitem[1][0][0]))
                        if len(client.ismesenitem[1]) > 1:
                            await message.reply('数字を入力することでそのアイテムに設定します')
                else:
                    await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['bag'].split(','):
        if rawcontent == '':
            return await message.reply(f"[{commands['bag']}] [バッグ名]")
        try:
            isitem = await search_item_with_type("ja", rawcontent, "backpack,pet")
            if isitem[0] == 'True':
                client.ismesjaitem=isitem
                if len(client.ismesjaitem[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesjaitem[1])))
                else:
                    for count,item in enumerate(client.ismesjaitem[1]):
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'{item[1]}')
                        else:
                            await message.reply(f'{count+1}: {item[1]}')
                    if len(client.ismesjaitem[1]) == 1:
                        if client.ismesjaitem[1][0][2] == 'backpack':
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.ismesjaitem[1][0][0]))
                        if client.ismesjaitem[1][0][2] == 'pet':
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.ismesjaitem[1][0][0]))
                    if len(client.ismesjaitem[1]) > 1:
                        await message.reply('数字を入力することでそのアイテムに設定します')
            else:
                isitem = await search_item_with_type("en", rawcontent, "backpack,pet")
                if isitem[0] == 'True':
                    client.ismesenitem=isitem
                    if len(client.ismesenitem[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesenitem[1])))
                    else:
                        for count,item in enumerate(client.ismesenitem[1]):
                            if len(client.ismesenitem[1]) == 1:
                                await message.reply(f'{item[1]}')
                            else:
                                await message.reply(f'{count+1}: {item[1]}')
                        if len(client.ismesenitem[1]) == 1:
                            if client.ismesenitem[1][0][2] == 'backpack':
                                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.ismesenitem[1][0][0]))
                            if client.ismesenitem[1][0][2] == 'pet':
                                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.ismesenitem[1][0][0]))
                        if len(client.ismesenitem[1]) > 1:
                            await message.reply('数字を入力することでそのアイテムに設定します')
                else:
                    await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['pickaxe'].split(','):
        if rawcontent == '':
            return await message.reply(f"[{commands['pickaxe']}] [ツルハシ名]]")
        try:
            isitem = await search_item_with_type("ja", rawcontent, "pickaxe")
            if isitem[0] == 'True':
                client.ismesjaitem=isitem
                if len(client.ismesjaitem[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesjaitem[1])))
                else:
                    for count,item in enumerate(client.ismesjaitem[1]):
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'{item[1]}')
                        else:
                            await message.reply(f'{count+1}: {item[1]}')
                    if len(client.ismesjaitem[1]) == 1:
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.ismesjaitem[1][0][0]))
                        await client.user.party.me.set_emote('EID_IceKing')
                    if len(client.ismesjaitem[1]) > 1:
                        await message.reply('数字を入力することでそのアイテムに設定します')
            else:
                isitem = await search_item_with_type("en", rawcontent, "pickaxe")
                if isitem[0] == 'True':
                    client.ismesenitem=isitem
                    if len(client.ismesenitem[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesenitem[1])))
                    else:
                        for count,item in enumerate(client.ismesenitem[1]):
                            if len(client.ismesenitem[1]) == 1:
                                await message.reply(f'{item[1]}')
                            else:
                                await message.reply(f'{count+1}: {item[1]}')
                        if len(client.ismesenitem[1]) == 1:
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.ismesenitem[1][0][0]))
                            await client.user.party.me.set_emote('EID_IceKing')
                        if len(client.ismesenitem[1]) > 1:
                            await message.reply('数字を入力することでそのアイテムに設定します')
                else:
                    await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['emote'].split(','):
        if rawcontent == '':
            return await message.reply(f"[{commands['emote']}] [エモート名]]")
        try:
            isitem = await search_item_with_type("ja", rawcontent, "emote,emoji,toy")
            if isitem[0] == 'True':
                client.ismesjaitem=isitem
                if len(client.ismesjaitem[1]) > 29:
                    await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesjaitem[1])))
                else:
                    for count,item in enumerate(client.ismesjaitem[1]):
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'{item[1]}')
                        else:
                            await message.reply(f'{count+1}: {item[1]}')
                    if len(client.ismesjaitem[1]) == 1:
                        if client.ismesjaitem[1][0][2] == 'emote':
                            await client.user.party.me.set_emote(client.ismesjaitem[1][0][0])
                            client.eid=client.ismesjaitem[1][0][0]
                        if client.ismesjaitem[1][0][2] == 'emoji':
                            await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesjaitem[1][0][0]}.{client.ismesjaitem[1][0][0]}')
                            client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesjaitem[1][0][0]}.{client.ismesjaitem[1][0][0]}'
                        if client.ismesjaitem[1][0][2] == 'toy':
                            await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesjaitem[1][0][0]}.{client.ismesjaitem[1][0][0]}')
                            client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesjaitem[1][0][0]}.{client.ismesjaitem[1][0][0]}'
                    if len(client.ismesjaitem[1]) > 1:
                        await message.reply('数字を入力することでそのアイテムに設定します')
            else:
                isitem = await search_item_with_type("en", rawcontent, "emote,emoji,toy")
                if isitem[0] == 'True':
                    client.ismesenitem=isitem
                    if len(client.ismesenitem[1]) > 29:
                        await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesenitem[1])))
                    else:
                        for count,item in enumerate(client.ismesenitem[1]):
                            if len(client.ismesenitem[1]) == 1:
                                await message.reply(f'{item[1]}')
                            else:
                                await message.reply(f'{count+1}: {item[1]}')
                        if len(client.ismesenitem[1]) == 1:
                            if client.ismesenitem[1][0][2] == 'emote':
                                await client.user.party.me.set_emote(client.ismesenitem[1][0][0])
                                client.eid=client.ismesenitem[1][0][0]
                            if client.ismesenitem[1][0][2] == 'emoji':
                                await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesenitem[1][0][0]}.{client.ismesenitem[1][0][0]}')
                                client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesenitem[1][0][0]}.{client.ismesenitem[1][0][0]}'
                            if client.ismesenitem[1][0][2] == 'toy':
                                await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesenitem[1][0][0]}.{client.ismesenitem[1][0][0]}')
                                client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesenitem[1][0][0]}.{client.ismesenitem[1][0][0]}'
                        if len(client.ismesenitem[1]) > 1:
                            await message.reply('数字を入力することでそのアイテムに設定します')
                else:
                    await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['set'].split(','):
        if rawcontent == '':
            return await message.reply(f"[{commands['set']}] [セット名]]")
        try:
            isitem = await search_set_item("ja", rawcontent)
            if isitem[0] == 'True':
                client.ismesjaitem=isitem
                for count,item in enumerate(client.ismesjaitem[1]):
                    if item[2] == 'outfit':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'スキン: {item[1]}')
                        else:
                            await message.reply(f'{count+1} スキン: {item[1]}')
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,item[0]))
                    if item[2] == 'backpack':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,item[0]))
                    if item[2] == 'pet':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,item[0]))
                    if item[2] == 'pickaxe':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'ツルハシ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} ツルハシ: {item[1]}')
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,item[0]))
                        await client.user.party.me.set_emote('EID_IceKing')
                    if item[2] == 'emote':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                        await client.user.party.me.set_emote(item[0])
                        client.eid=item[0]
                    if item[2] == 'emoji':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{item[0]}.{item[0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{item[0]}.{item[0]}'
                    if item[2] == 'toy':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{item[0]}.{item[0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{item[0]}.{item[0]}'
                    
            else:
                isitem = await search_set_item("en", rawcontent)
                if isitem[0] == 'True':
                    client.ismesenitem=isitem
                    for count,item in enumerate(client.ismesenitem[1]):
                        if item[2] == 'outfit':
                            if len(client.ismesenitem[1]) == 1:
                                await message.reply(f'スキン: {item[1]}')
                            else:
                                await message.reply(f'{count+1} スキン: {item[1]}')
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,item[0]))
                        if item[2] == 'backpack':
                            if len(client.ismesenitem[1]) == 1:
                                await message.reply(f'バッグ: {item[1]}')
                            else:
                                await message.reply(f'{count+1} バッグ: {item[1]}')
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,item[0]))
                        if item[2] == 'pet':
                            if len(client.ismesenitem[1]) == 1:
                                await message.reply(f'バッグ: {item[1]}')
                            else:
                                await message.reply(f'{count+1} バッグ: {item[1]}')
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,item[0]))
                        if item[2] == 'pickaxe':
                            if len(client.ismesenitem[1]) == 1:
                                await message.reply(f'ツルハシ: {item[1]}')
                            else:
                                await message.reply(f'{count+1} ツルハシ: {item[1]}')
                            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,item[0]))
                            await client.user.party.me.set_emote('EID_IceKing')
                        if item[2] == 'emote':
                            if len(client.ismesenitem[1]) == 1:
                                await message.reply(f'エモート: {item[1]}')
                            else:
                                await message.reply(f'{count+1} エモート: {item[1]}')
                            await client.user.party.me.set_emote(item[0])
                            client.eid=item[0]
                        if item[2] == 'emoji':
                            if len(client.ismesenitem[1]) == 1:
                                await message.reply(f'エモート: {item[1]}')
                            else:
                                await message.reply(f'{count+1} エモート: {item[1]}')
                            await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{item[0]}.{item[0]}')
                            client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{item[0]}.{item[0]}'
                        if item[2] == 'toy':
                            if len(client.ismesenitem[1]) == 1:
                                await message.reply(f'エモート: {item[1]}')
                            else:
                                await message.reply(f'{count+1} エモート: {item[1]}')
                            await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{item[0]}.{item[0]}')
                            client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{item[0]}.{item[0]}'
                else:
                    await message.reply('見つかりません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['variant'].split(','):
        try:
            if len(args) == 4:
                if args[1].startswith('cid_'):
                    variants=client.user.party.me.create_variants(item='AthenaCharacter',**{args[2]: int(args[3])})
                elif args[1].startswith('bid_') or args[1].startswith('petcarrier_'):
                    variants=client.user.party.me.create_variants(item='AthenaBackpack',**{args[2]: int(args[3])})
                elif args[1].startswith('pickaxe_id_'):
                    variants=client.user.party.me.create_variants(item='AthenaPickaxe',**{args[2]: int(args[3])})
            elif len(args) == 6:
                if args[1].startswith('cid_'):
                    variants=client.user.party.me.create_variants(item='AthenaCharacter',**{args[2]: int(args[3])},**{args[4]: int(args[5])})
                elif args[1].startswith('bid_') or args[1].startswith('petcarrier_'):
                    variants=client.user.party.me.create_variants(item='AthenaBackpack',**{args[2]: int(args[3])},**{args[4]: int(args[5])})
                elif args[1].startswith('pickaxe_id_'):
                    variants=client.user.party.me.create_variants(item='AthenaPickaxe',**{args[2]: int(args[3])},**{args[4]: int(args[5])})
            elif len(args) == 8:
                if args[1].startswith('cid_'):
                    variants=client.user.party.me.create_variants(item='AthenaCharacter',**{args[2]: int(args[3])},**{args[4]: int(args[5])},**{args[6]: int(args[7])})
                elif args[1].startswith('bid_') or args[1].startswith('petcarrier_'):
                    variants=client.user.party.me.create_variants(item='AthenaBackpack',**{args[2]: int(args[3])},**{args[4]: int(args[5])},**{args[6]: int(args[7])})
                elif args[1].startswith('pickaxe_id_'):
                    variants=client.user.party.me.create_variants(item='AthenaPickaxe',**{args[2]: int(args[3])},**{args[4]: int(args[5])},**{args[6]: int(args[7])})
            if len(args) == 4 or len(args) == 6 or len(args) == 8:
                if args[1].startswith('cid_'):
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,asset=args[1],variants=variants))
                elif args[1].startswith('bid_'):
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,asset=args[1],variants=variants))
                elif args[1].startswith('petcarrier_'):
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,asset=args[1],variants=variants))
                elif args[1].startswith('pickaxe_id'):
                    await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,asset=args[1],variants=variants))
                    await client.user.party.me.set_emote('EID_IceKing')
            else:
                await message.reply(f"[{commands['variant']}] [variant] [数値]\nvariantと数値は3つまで設定可")
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['skinasset'].split(','):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,rawcontent))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['skinasset']}] [アセットパス]")
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['bagasset'].split(','):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,rawcontent))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['bagasset']}] [アセットパス]")
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['pickaxeasset'].split(','):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,rawcontent))
            await client.user.party.me.set_emote('EID_IceKing')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['pickaxeasset']}] [アセットパス]")
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0] in commands['emoteasset'].split(','):
        try:
            await client.user.party.me.clear_emote()
            await client.user.party.me.set_emote(args[1])
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply(f"[{commands['emoteasset']}] [アセットパス]")
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0].lower().startswith('cid_'):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,args[0].upper()))
            await message.reply(f'スキンを {args[0]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0].lower().startswith('bid_'):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,args[0]))
            await message.reply(f'バッグを {args[0]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0].lower().startswith('pet_carrier'):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,args[0]))
            await message.reply(f'バッグを {args[0]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0].lower().startswith('pickaxe_id'):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,args[0]))
            await client.user.party.me.set_emote('EID_IceKing')
            await message.reply(f'ツルハシを {args[0]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0].lower().startswith('eid_'):
        try:
            if not client.user.party.me.emote is None:
                if client.user.party.me.emote.lower() == args[0].lower():
                    await client.user.party.me.clear_emote()
            await client.user.party.me.set_emote(args[0])
            await message.reply(f'エモートを {args[0]} に設定')
            client.eid=args[0]
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0].lower().startswith('emoji_'):
        try:
            if not client.user.party.me.emote is None:
                if client.user.party.me.emote.lower() == args[0].lower():
                    await client.user.party.me.clear_emote()
            await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{args[0]}.{args[0]}')
            await message.reply(f'エモートを {args[0]} に設定')
            client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{args[0]}.{args[0]}'
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0].lower().startswith('toy_'):
        try:
            if not client.user.party.me.emote is None:
                if client.user.party.me.emote.lower() == args[0].lower():
                    await client.user.party.me.clear_emote()
            await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{args[0]}.{args[0]}')
            await message.reply(f'エモートを {args[0]} に設定')
            client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{args[0]}.{args[0]}'
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    elif args[0].lower().startswith('playlist_'):
        try:
            await client.user.party.set_playlist(args[0])
            await message.reply(f'プレイリストを {args[0]} に設定')
            data['fortnite']['playlist']=args[0]
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('パーティーリーダーではありません')
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')

    else:
        try:
            try:
                if args[0].isdigit() and client.ismesjaitem[0] == 'True':
                    if client.ismesjaitem[1][int(args[0])-1][2] == 'outfit':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.ismesjaitem[1][int(args[0])-1][0]))
                    if client.ismesjaitem[1][int(args[0])-1][2] == 'backpack':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.ismesjaitem[1][int(args[0])-1][0]))
                    if client.ismesjaitem[1][int(args[0])-1][2] == 'pet':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.ismesjaitem[1][int(args[0])-1][0]))
                    if client.ismesjaitem[1][int(args[0])-1][2] == 'pickaxe':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.ismesjaitem[1][int(args[0])-1][0]))
                        await client.user.party.me.set_emote('EID_IceKing')
                    if client.ismesjaitem[1][int(args[0])-1][2] == 'emote':
                        if not client.user.party.me.emote is None:
                            if client.user.party.me.emote.lower() == client.ismesjaitem[1][int(args[0])-1][0].lower():
                                await client.user.party.me.clear_emote()
                        await client.user.party.me.set_emote(client.ismesjaitem[1][int(args[0])-1][0])
                        client.eid=client.ismesjaitem[1][int(args[0])-1][0]
                    if client.ismesjaitem[1][int(args[0])-1][2] == 'emoji':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesjaitem[1][int(args[0])-1][0]}.{client.ismesjaitem[1][int(args[0])-1][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesjaitem[1][int(args[0])-1][0]}.{client.ismesjaitem[1][int(args[0])-1][0]}'
                    if client.ismesjaitem[1][int(args[0])-1][2] == 'toy':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesjaitem[1][int(args[0])-1][0]}.{client.ismesjaitem[1][int(args[0])-1][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesjaitem[1][int(args[0])-1][0]}.{client.ismesjaitem[1][int(args[0])-1][0]}'
                    return
            except AttributeError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
            try:
                if args[0].isdigit() and client.ismesenitem[0] == 'True':
                    if client.ismesenitem[1][int(args[0])-1][2] == 'outfit':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.ismesenitem[1][int(args[0])-1][0]))
                    if client.ismesenitem[1][int(args[0])-1][2] == 'backpack':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.ismesenitem[1][int(args[0])-1][0]))
                    if client.ismesenitem[1][int(args[0])-1][2] == 'pet':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.ismesenitem[1][int(args[0])-1][0]))
                    if client.ismesenitem[1][int(args[0])-1][2] == 'pickaxe':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.ismesenitem[1][int(args[0])-1][0]))
                        await client.user.party.me.set_emote('EID_IceKing')
                    if client.ismesenitem[1][int(args[0])-1][2] == 'emote':
                        if not client.user.party.me.emote is None:
                            if client.user.party.me.emote.lower() == client.ismesenitem[1][int(args[0])-1][0].lower():
                                await client.user.party.me.clear_emote()
                        await client.user.party.me.set_emote(client.ismesenitem[1][int(args[0])-1][0])
                        client.eid=client.ismesenitem[1][int(args[0])-1][0]
                    if client.ismesenitem[1][int(args[0])-1][2] == 'emoji':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesenitem[1][int(args[0])-1][0]}.{client.ismesenitem[1][int(args[0])-1][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesenitem[1][int(args[0])-1][0]}.{client.ismesenitem[1][int(args[0])-1][0]}'
                    if client.ismesenitem[1][int(args[0])-1][2] == 'toy':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesenitem[1][int(args[0])-1][0]}.{client.ismesenitem[1][int(args[0])-1][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesenitem[1][int(args[0])-1][0]}.{client.ismesenitem[1][int(args[0])-1][0]}'
                    return
            except AttributeError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('有効な数字を入力してください')
            return
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')
            return

        try:
            isitem = await is_itemname("ja", message.content)
            if isitem[0] == 'True':
                client.ismesjaitem = isitem
                if len(client.ismesjaitem[1]) > 29:
                    return await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesjaitem[1])))
                for count,item in enumerate(client.ismesjaitem[1]):
                    if item[2] == 'outfit':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'スキン: {item[1]}')
                        else:
                            await message.reply(f'{count+1} スキン: {item[1]}')
                    if item[2] == 'backpack':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                    if item[2] == 'pet':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                    if item[2] == 'pickaxe':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'ツルハシ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} ツルハシ: {item[1]}')
                    if item[2] == 'emote':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                    if item[2] == 'emoji':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                    if item[2] == 'toy':
                        if len(client.ismesjaitem[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                if len(client.ismesjaitem[1]) == 1:
                    if client.ismesjaitem[1][0][2] == 'outfit':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.ismesjaitem[1][0][0]))
                    if client.ismesjaitem[1][0][2] == 'backpack':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.ismesjaitem[1][0][0]))
                    if client.ismesjaitem[1][0][2] == 'pet':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.ismesjaitem[1][0][0]))
                    if client.ismesjaitem[1][0][2] == 'pickaxe':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.ismesjaitem[1][0][0]))
                        await client.user.party.me.set_emote('EID_IceKing')
                    if client.ismesjaitem[1][0][2] == 'emote':
                        if not client.user.party.me.emote is None:
                            if client.user.party.me.emote.lower() == client.ismesjaitem[1][0][0].lower():
                                await client.user.party.me.clear_emote()
                        await client.user.party.me.set_emote(client.ismesjaitem[1][0][0])
                        client.eid=client.ismesjaitem[1][0][0]
                    if client.ismesjaitem[1][0][2] == 'emoji':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesjaitem[1][0][0]}.{client.ismesjaitem[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesjaitem[1][0][0]}.{client.ismesjaitem[1][0][0]}'
                    if client.ismesjaitem[1][0][2] == 'toy':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesjaitem[1][0][0]}.{client.ismesjaitem[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesjaitem[1][0][0]}.{client.ismesjaitem[1][0][0]}'
                if len(client.ismesjaitem[1]) > 1:
                    await message.reply('数字を入力することでそのアイテムに設定します')
                return
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
            return
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')
            return

        try:
            isitem = await is_itemname("en", message.content)
            if isitem[0] == 'True':
                client.ismesenitem = isitem
                if len(client.ismesenitem[1]) > 29:
                    return await message.reply("見つかったアイテムが多すぎます " + str(len(client.ismesenitem[1])))
                for count,item in enumerate(client.ismesenitem[1]):
                    if item[2] == 'outfit':
                        if len(client.ismesenitem[1]) == 1:
                            await message.reply(f'スキン: {item[1]}')
                        else:
                            await message.reply(f'{count+1} スキン: {item[1]}')
                    if item[2] == 'backpack':
                        if len(client.ismesenitem[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                    if item[2] == 'pet':
                        if len(client.ismesenitem[1]) == 1:
                            await message.reply(f'バッグ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} バッグ: {item[1]}')
                    if item[2] == 'pickaxe':
                        if len(client.ismesenitem[1]) == 1:
                            await message.reply(f'ツルハシ: {item[1]}')
                        else:
                            await message.reply(f'{count+1} ツルハシ: {item[1]}')
                    if item[2] == 'emote':
                        if len(client.ismesenitem[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                    if item[2] == 'emoji':
                        if len(client.ismesenitem[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                    if item[2] == 'toy':
                        if len(client.ismesenitem[1]) == 1:
                            await message.reply(f'エモート: {item[1]}')
                        else:
                            await message.reply(f'{count+1} エモート: {item[1]}')
                if len(client.ismesenitem[1]) == 1:
                    if client.ismesenitem[1][0][2] == 'outfit':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit,client.ismesenitem[1][0][0]))
                    if client.ismesenitem[1][0][2] == 'backpack':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack,client.ismesenitem[1][0][0]))
                    if client.ismesenitem[1][0][2] == 'pet':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet,client.ismesenitem[1][0][0]))
                    if client.ismesenitem[1][0][2] == 'pickaxe':
                        await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe,client.ismesenitem[1][0][0]))
                        await client.user.party.me.set_emote('EID_IceKing')
                    if client.ismesenitem[1][0][2] == 'emote':
                        if not client.user.party.me.emote is None:
                            if client.user.party.me.emote.lower() == client.ismesenitem[1][0][0].lower():
                                await client.user.party.me.clear_emote()
                        await client.user.party.me.set_emote(client.ismesenitem[1][0][0])
                        client.eid=client.ismesenitem[1][0][0]
                    if client.ismesenitem[1][0][2] == 'emoji':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesenitem[1][0][0]}.{client.ismesenitem[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Dances/Emoji/{client.ismesenitem[1][0][0]}.{client.ismesenitem[1][0][0]}'
                    if client.ismesenitem[1][0][2] == 'toy':
                        await client.user.party.me.set_emote(f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesenitem[1][0][0]}.{client.ismesenitem[1][0][0]}')
                        client.eid=f'/Game/Athena/Items/Cosmetics/Toys/{client.ismesenitem[1][0][0]}.{client.ismesenitem[1][0][0]}'
                if len(client.ismesenitem[1]) > 1:
                    await message.reply('数字を入力することでそのアイテムに設定します')
                return
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('アイテム情報の設定リクエストを処理中にエラーが発生しました')
            return
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            await message.reply('エラー')
            return

if data['loglevel'] == 'debug':
    print(credentials)
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
                delete_existing_device_auths=True,
                **device_auth_details
            ),
            default_party_member_config=[
                partial(fortnitepy.ClientPartyMember.set_outfit, data['fortnite']['cid'].replace('cid','CID',1)),
                partial(fortnitepy.ClientPartyMember.set_backpack, data['fortnite']['bid'].replace('bid','BID',1)),
                partial(fortnitepy.ClientPartyMember.set_pickaxe, data['fortnite']['pickaxe_id'].replace('pickaxe_id','Pickaxe_ID',1)),
                partial(fortnitepy.ClientPartyMember.set_battlepass_info, has_purchased=True, level=data['fortnite']['tier'], self_boost_xp=data['fortnite']['xpboost'], friend_boost_xp=data['fortnite']['friendxpboost']),
                partial(fortnitepy.ClientPartyMember.set_banner, icon=data['fortnite']['banner'], color=data['fortnite']['banner_color'], season_level=data['fortnite']['level']),
            ],
        )
    except ValueError:
        print(red(traceback.format_exc()))
        print(red(f'アカウント情報を設定中にエラーが発生しました。configのfortnite部分の設定が間違っている可能性があります。'))
        continue
    client.eid=data['fortnite']['eid']
    client.acceptinvite_interval=True
    client.stopcheck=False
    client.prevoutfit=None
    client.prevoutfitvariants=None
    client.prevbackpack=None
    client.prevbackpackvariants=None
    client.prevpickaxe=None
    client.prevpickaxevariants=None
    client.prevmessage='None'
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
    client.add_event_handler('friend_message', event_friend_message)
    client.add_event_handler('party_message', event_party_message)

    clients.append(client)

try:
    fortnitepy.run_multiple(
        clients,
        ready_callback=event_ready,
        all_ready_callback=lambda: print(green(f'[{now_()}] 全てのアカウントにログインしました。')) if len(clients) > 1 else print('')
    )
except fortnitepy.AuthException:
    if "errors.com.epicgames.account.oauth.exchange_code_not_found" in e.args[0]:
        print(red(traceback.format_exc()))
        print(f'[{now_()}] exchange_codeを\nhttps://www.epicgames.com/\nでボットのアカウントにログインし、\nhttps://www.epicgames.com/id/login?redirectUrl=https%3A%2F%2Fwww.epicgames.com%2Fid%2Fapi%2Fexchange\nで取得してください。')
    else:
        print(red(traceback.format_exc()))
        print(red(f'[{now_()}] アカウントにログインできません。'))
    exit()
except Exception:
    print(red(traceback.format_exc()))
    print(red(f'[{now_()}] アカウントの読み込みに失敗しました。もう一度試してみてください。'))
    exit()
