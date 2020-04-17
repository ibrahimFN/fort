# -*- coding: utf-8 -*-
"""
MIT License

Copyright (c) 2020 gomashio1596

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

try:
    from threading import Thread, Timer
    from functools import partial
    import unicodedata
    import threading
    import traceback
    import datetime
    import asyncio
    import logging
    import random
    import time
    import sys
    import os
    import re
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
    print('標準ライブラリの読み込みに失敗しました。Pythonのバージョンが間違っている可能性があります。Pythonの再インストールなどを試してみてください。問題が修正されない場合はこちらまで連絡をください\nTwitter @gomashioepic\nDiscord gomashio#4335')
    exit()

try:
    from crayons import cyan, green, magenta, red, yellow
    from fortnitepy import ClientPartyMember
    from flask import Flask
    import fortnitepy.errors
    import fortnitepy
    import requests
    import discord
    import jaconv
    import json
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
    print('サードパーティーライブラリの読み込みに失敗しました。INSTALL.bat を実行してください。問題が修正されない場合はこちらまで連絡をください\nTwitter @gomashioepic\nDiscord gomashio#4335')
    exit()

if os.getcwd().startswith('/app'):
    app=Flask(__name__)
    @app.route("/")
    def index():
        return "<h1>Bot is running</h1>"
    Thread(target=app.run,args=("0.0.0.0",8080)).start()

filename = 'device_auths.json'
storedlog = []
loadedclients = []
whitelist = []
whitelist_ = []
blacklist = []
blacklist_ = []
client_name = {}
cache_users = {}
blacklist_flag = True
whitelist_flag = True
invitelist_flag = True
discord_flag = True
kill=False
configkeys=["['fortnite']","['fortnite']['email']","['fortnite']['password']","['fortnite']['owner']","['fortnite']['platform']","['fortnite']['cid']","['fortnite']['bid']","['fortnite']['pickaxe_id']","['fortnite']['eid']","['fortnite']['playlist']","['fortnite']['banner']","['fortnite']['banner_color']","['fortnite']['level']","['fortnite']['tier']","['fortnite']['xpboost']","['fortnite']['friendxpboost']","['fortnite']['status']","['fortnite']['privacy']","['fortnite']['whisper']","['fortnite']['partychat']","['fortnite']['disablewhisperperfectly']","['fortnite']['disablepartychatperfectly']","['fortnite']['joinmessage']","['fortnite']['randommessage']","['fortnite']['joinmessageenable']","['fortnite']['randommessageenable']","['fortnite']['outfitmimic']","['fortnite']['backpackmimic']","['fortnite']['pickaxemimic']","['fortnite']['emotemimic']","['fortnite']['acceptinvite']","['fortnite']['acceptfriend']","['fortnite']['addfriend']","['fortnite']['invite-ownerdecline']","['fortnite']['inviteinterval']","['fortnite']['interval']","['fortnite']['waitinterval']","['fortnite']['blacklist']","['fortnite']['blacklist-declineinvite']","['fortnite']['blacklist-autoblock']","['fortnite']['blacklist-autokick']","['fortnite']['blacklist-autochatban']","['fortnite']['blacklist-ignorecommand']","['fortnite']['whitelist']","['fortnite']['whitelist-allowinvite']","['fortnite']['whitelist-declineinvite']","['fortnite']['whitelist-ignorelock']","['fortnite']['whitelist-ownercommand']","['fortnite']['invitelist']","['discord']['enabled']","['discord']['token']","['discord']['owner']","['discord']['status']","['discord']['discord']","['discord']['disablediscordperfectly']","['discord']['blacklist']","['discord']['blacklist-ignorecommand']","['discord']['whitelist']","['discord']['whitelist-ignorelock']","['discord']['whitelist-ownercommand']","['no-logs']","['ingame-error']","['discord-log']","['hide-email']","['hide-password']","['hide-token']","['hide-webhook']","['hide-api-key']","['webhook']","['caseinsensitive']","['api-key']","['loglevel']","['debug']"]
commandskeys=['ownercommands','true','false','me','prev','eval','exec','restart','relogin','reload','addblacklist','removeblacklist','addwhitelist','removewhitelist','addblacklist_discord','removeblacklist_discord','addwhitelist_discord','removewhitelist_discord','get','friendcount','pendingcount','blockcount','friendlist','pendinglist','blocklist','outfitmimic','backpackmimic','pickaxemimic','emotemimic','whisper','partychat','discord','disablewhisperperfectly','disablepartychatperfectly','disablediscordperfectly','acceptinvite','acceptfriend','joinmessageenable','randommessageenable','wait','join','joinid','leave','invite','inviteall','message','partymessage','status','banner','level','bp','privacy','privacy_public','privacy_friends_allow_friends_of_friends','privacy_friends','privacy_private_allow_friends_of_friends','privacy_private','getuser','getfriend','getpending','getblock','info','info_party','pending','removepending','addfriend','removefriend','acceptpending','declinepending','blockfriend','unblockfriend','chatban','promote','kick','ready','unready','sitout','outfitlock','backpacklock','pickaxelock','emotelock','stop','alloutfit','allbackpack','allpet','allpickaxe','allemote','allemoji','alltoy','allshout','cid','bid','petcarrier','pickaxe_id','eid','emoji_id','toy_id','shout_id','id','outfit','backpack','pet','pickaxe','emote','emoji','toy','shout','item','set','setvariant','addvariant','setstyle','addstyle','setenlightenment','outfitasset','backpackasset','pickaxeasset','emoteasset']
ignore=['ownercommands','true','false','me', 'privacy_public', 'privacy_friends_allow_friends_of_friends', 'privacy_friends', 'privacy_private_allow_friends_of_friends', 'privacy_private', 'info_party']

def dstore(username, content):
    content=str(content)
    if data['hide-email'] is True:
        for email in data['fortnite']['email'].split(','):
            content=content.replace(email,len(email)*"X")
    if data['hide-password'] is True:
        for password in data['fortnite']['password'].split(','):
            content=content.replace(password,len(password)*"X")
    if data['hide-token'] is True:
        for token in data['discord']['token'].split(','):
            content=content.replace(token,len(token)*"X")
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
    global kill
    while True:
        if kill is True:
            exit()
        if data['discord-log'] is True:
            if len(storedlog) != 0:
                for send in storedlog:
                    try:
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
                    except TypeError:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore("ボット", f">>> {traceback.format_exc()}")
                        try:
                            storedlog.remove(send)
                        except Exception:
                            pass
                        continue
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore("ボット", f">>> {traceback.format_exc()}")
                        print(yellow(f'{username}: {content} の送信中にエラーが発生しました'))
                        dstore("ボット", f"{username}: {content} の送信中にエラーが発生しました")
                        continue
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

def convert_to_type(text):
    if True in [text.lower() in commands[key].split(",") for key in ("cid", "outfit", "outfitasset")] or text.lower().startswith("cid_"):
        return "outfit"
    elif True in [text.lower() in commands[key].split(",") for key in ("bid", "backpack", "backpackasset")] or text.lower().startswith("bid_"):
        return "backpack"
    elif True in [text.lower() in commands[key].split(",") for key in ("petcarrier", "pet")] or text.lower().startswith("petcarrier_"):
        return "pet"
    elif True in [text.lower() in commands[key].split(",") for key in ("pickaxe_id", "pickaxe", "pickaxeasset")] or text.lower().startswith("pickaxe_id"):
        return "pickaxe"
    elif True in [text.lower() in commands[key].split(",") for key in ("eid", "emote", "emoteasset")] or text.lower().startswith("eid_"):
        return "emote"
    elif True in [text.lower() in commands[key].split(",") for key in ("emoji_id", "emoji")] or text.lower().startswith("emoji_"):
        return "emoji"
    elif True in [text.lower() in commands[key].split(",") for key in ("toy_id", "toy")] or text.lower().startswith("toy_"):
        return "toy"
    elif True in [text.lower() in commands[key].split(",") for key in ("shout_id", "shout")] or text.lower().startswith("shout_"):
        return "shout"
    elif True in [text.lower() in commands[key].split(",") for key in ("id", "item")]:
        return "item"

def convert_to_asset(text):
    if True in [text.lower() in commands[key].split(",") for key in ("cid", "outfit", "outfitasset")] or text.lower().startswith("cid_"):
        return "outfit"
    elif True in [text.lower() in commands[key].split(",") for key in ("bid", "backpack", "backpackasset")] or text.lower().startswith("bid_"):
        return "backpack"
    elif True in [text.lower() in commands[key].split(",") for key in ("petcarrier", "pet")] or text.lower().startswith("petcarrier_"):
        return "backpack"
    elif True in [text.lower() in commands[key].split(",") for key in ("pickaxe_id", "pickaxe", "pickaxeasset")] or text.lower().startswith("pickaxe_id"):
        return "pickaxe"
    elif True in [text.lower() in commands[key].split(",") for key in ("eid", "emote", "emoteasset")] or text.lower().startswith("eid_"):
        return "emote"
    elif True in [text.lower() in commands[key].split(",") for key in ("emoji_id", "emoji")] or text.lower().startswith("emoji_"):
        return "emote"
    elif True in [text.lower() in commands[key].split(",") for key in ("toy_id", "toy")] or text.lower().startswith("toy_"):
        return "emote"
    elif True in [text.lower() in commands[key].split(",") for key in ("shout_id", "shout")] or text.lower().startswith("shout_"):
        return "emote"

def convert_to_id(text):
    if True in [text.lower() in commands[key].split(",") for key in ("cid", "outfit", "outfitasset")] or text.lower().startswith("cid_"):
        return "cid"
    elif True in [text.lower() in commands[key].split(",") for key in ("bid", "backpack", "backpackasset")] or text.lower().startswith("bid_"):
        return "bid"
    elif True in [text.lower() in commands[key].split(",") for key in ("petcarrier", "pet")] or text.lower().startswith("petcarrier_"):
        return "petcarrier"
    elif True in [text.lower() in commands[key].split(",") for key in ("pickaxe_id", "pickaxe", "pickaxeasset")] or text.lower().startswith("pickaxe_id"):
        return "pickaxe_id"
    elif True in [text.lower() in commands[key].split(",") for key in ("eid", "emote", "emoteasset")] or text.lower().startswith("eid_"):
        return "eid"
    elif True in [text.lower() in commands[key].split(",") for key in ("emoji_id", "emoji")] or text.lower().startswith("emoji_"):
        return "emoji_id"
    elif True in [text.lower() in commands[key].split(",") for key in ("toy_id", "toy")] or text.lower().startswith("toy_"):
        return "toy_id"
    elif True in [text.lower() in commands[key].split(",") for key in ("shout_id", "shout")] or text.lower().startswith("shout_"):
        return "shout_id"
    elif True in [text.lower() in commands[key].split(",") for key in ("id", "item")]:
        return "id"

def convert_variant(type_, variants):
    result = []
    for variant in variants:
        for option in variant['options']:
            result.append({"name": option['name'], 'variants': [{'item': type_, 'channel': variant['channel'], 'variant': option['tag']}]})
    return result

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
        for key in configkeys:
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
    if True:
        if data['fortnite']['whisper'] not in (True, False):
            data['fortnite']['whisper'] = True
        if data['fortnite']['partychat'] not in (True, False):
            data['fortnite']['partychat'] = True
        if data['fortnite']['disablewhisperperfectly'] not in (True, False):
            data['fortnite']['disablewhisperperfectly'] = False
        if data['fortnite']['disablepartychatperfectly'] not in (True, False):
            data['fortnite']['disablepartychatperfectly'] = False
        if data['fortnite']['joinmessageenable'] not in (True, False):
            data['fortnite']['joinmessageenable'] = False
        if data['fortnite']['randommessageenable'] not in (True, False):
            data['fortnite']['randommessageenable'] = False
        if data['fortnite']['outfitmimic'] not in (True, False):
            data['fortnite']['outfitmimic'] = False
        if data['fortnite']['backpackmimic'] not in (True, False):
            data['fortnite']['backpackmimic'] = False
        if data['fortnite']['pickaxemimic'] not in (True, False):
            data['fortnite']['pickaxemimic'] = False
        if data['fortnite']['emotemimic'] not in (True, False):
            data['fortnite']['emotemimic'] = False
        if data['fortnite']['acceptinvite'] not in (True, False):
            data['fortnite']['acceptinvite'] = True
        if data['fortnite']['acceptfriend'] not in (True, False, None):
            data['fortnite']['acceptfriend'] = True
        if data['fortnite']['addfriend'] not in (True, False):
            data['fortnite']['addfriend'] = False
        if data['fortnite']['invite-ownerdecline'] not in (True, False):
            data['fortnite']['invite-ownerdecline'] = False
        if data['fortnite']['inviteinterval'] not in (True, False):
            data['fortnite']['inviteinterval'] = False
        if data['fortnite']['blacklist-declineinvite'] not in (True, False):
            data['fortnite']['blacklist-declineinvite'] = False
        if data['fortnite']['blacklist-autoblock'] not in (True, False):
            data['fortnite']['blacklist-autoblock'] = False
        if data['fortnite']['blacklist-autokick'] not in (True, False):
            data['fortnite']['blacklist-autokick'] = False
        if data['fortnite']['blacklist-autochatban'] not in (True, False):
            data['fortnite']['blacklist-autochatban'] = False
        if data['fortnite']['blacklist-ignorecommand'] not in (True, False):
            data['fortnite']['blacklist-ignorecommand'] = False
        if data['fortnite']['whitelist-allowinvite'] not in (True, False):
            data['fortnite']['whitelist-allowinvite'] = False
        if data['fortnite']['whitelist-declineinvite'] not in (True, False):
            data['fortnite']['whitelist-declineinvite'] = False
        if data['fortnite']['whitelist-ignorelock'] not in (True, False):
            data['fortnite']['whitelist-ignorelock'] = False
        if data['fortnite']['whitelist-ownercommand'] not in (True, False):
            data['fortnite']['whitelist-ownercommand'] = False

    if True:
        if data['discord']['enabled'] not in (True, False):
            data['discord']['enabled'] = False
        if data['discord']['discord'] not in (True, False):
            data['discord']['discord'] = True
        if data['discord']['disablediscordperfectly'] not in (True, False):
            data['discord']['disablediscordperfectly'] = True
        if data['discord']['blacklist-ignorecommand'] not in (True, False):
            data['discord']['blacklist-ignorecommand'] = False
        if data['discord']['whitelist-ignorelock'] not in (True, False):
            data['discord']['whitelist-ignorelock'] = False
        if data['discord']['whitelist-ownercommand'] not in (True, False):
            data['discord']['whitelist-ownercommand'] = False

    if True:
        if data['no-logs'] not in (True, False):
            data['no-logs'] = False
        if data['ingame-error'] not in (True, False):
            data['ingame-error'] = True
        if data['discord-log'] not in (True, False):
            data['discord-log'] = False
        if data['hide-email'] not in (True, False):
            data['hide-email'] = True
        if data['hide-password'] not in (True, False):
            data['hide-password'] = True
        if data['hide-webhook'] not in (True, False):
            data['hide-webhook'] = True
        if data['hide-api-key'] not in (True, False):
            data['hide-api-key'] = True
        if data['caseinsensitive'] not in (True, False):
            data['caseinsensitive'] = True
        if data['loglevel'] not in ('normal', 'info', 'debug'):
            data['loglevel'] = 'normal'
        if data['fortnite']['privacy'] not in ('public', 'friends_allow_friends_of_friends', 'friends', 'private_allow_friends_of_friends', 'private'):
            data['fortnite']['privacy'] = 'public'

    data['fortnite']['privacy']=eval(f"fortnitepy.PartyPrivacy.{data['fortnite']['privacy'].upper()}")
    client.whisper=data['fortnite']['whisper']
    client.partychat=data['fortnite']['partychat']
    client.discord=data['discord']['discord']
    client.whisperperfect=data['fortnite']['disablewhisperperfectly']
    client.partychatperfect=data['fortnite']['disablepartychatperfectly']
    client.discordperfect=data['discord']['disablediscordperfectly']
    client.joinmessageenable=data['fortnite']['joinmessageenable']
    client.randommessageenable=data['fortnite']['randommessageenable']
    client.outfitmimic=data['fortnite']['outfitmimic']
    client.backpackmimic=data['fortnite']['backpackmimic']
    client.pickaxemimic=data['fortnite']['pickaxemimic']
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
        for key in commandskeys:
            exec(f"errorcheck=commands['{key}']")
        if data['caseinsensitive'] is True:
            commands=dict((k.lower(), jaconv.kata2hira(v.lower())) for k,v in commands.items())
        for checks in commands.items():
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
    except UnicodeEncodeError:
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore('ボット',f'>>> {traceback.format_exc()}')
    except Exception:
        print(red(traceback.format_exc()))
        dstore('ボット',f'>>> {traceback.format_exc()}')

def add_cache(client, user):
    try:
        if isinstance(user, fortnitepy.user.UserBase) and user.id is not None:
            if isinstance(user, fortnitepy.User):
                if user.display_name is not None:
                    cache_users[user.display_name] = user
            else:
                user = client.get_user(user.id)
                if user is not None:
                    if user.display_name is not None:
                        cache_users[user.display_name] = user
        else:
            print(f"{type(user)}({user}) is not instance of fortnitepy.user.UserBase")
    except Exception:
        print(red(traceback.format_exc()))
        dstore('ボット',f'>>> {traceback.format_exc()}')

def partymember_backpack(member):
    asset = member.meta.get_prop("AthenaCosmeticLoadout_j")["AthenaCosmeticLoadout"]["backpackDef"]
    result = re.search(r".*\.([^\'\"]*)", asset.strip("'"))
    if result is not None and result.group(1) != 'None':
        return result.group(1)

def partymember_emote(member):
    asset = member.meta.get_prop("FrontendEmote_j")["FrontendEmote"]["emoteItemDef"]
    result = re.search(r".*\.([^\'\"]*)", asset.strip("'"))
    if result is not None and result.group(1) != 'None':
        return result.group(1)

def member_asset(member, asset):
    if asset in ("backpack", "pet"):
        return partymember_backpack(member)
    elif asset in ("emote", "emoji", "toy"):
        return partymember_emote(member)
    else:
        return eval(f"member.{asset}")

def lock_check(client, author_id):
    if client.owner is not None:
        if data['fortnite']['whitelist-ignorelock']:
            if client.owner.id != author_id and author_id not in whitelist:
                return True
        else:
            if client.owner.id != author_id:
                return True
    else:
        if data['fortnite']['whitelist-ignorelock']:
            if author_id not in whitelist:
                return True
        else:
            return True
    return False

def search_item(lang, mode, text, type_ = None):
    ignoretype = [
        "banner",
        "contrail",
        "glider",
        "wrap",
        "loadingscreen",
        "music",
        "spray"
    ]
    itemlist = []
    if lang in ('en', 'ja'):
        with open(f'all{lang}.json', 'r', encoding='utf-8') as f:
            data_ = json.load(f)
    try:
        for item in data_['data']:
            if item['type'] in ignoretype:
                continue
            if mode == "name":
                if data['caseinsensitive'] is True:
                    text=jaconv.hira2kata(text.lower())
                    name=jaconv.hira2kata(item['name'].lower())
                else:
                    name=item['name']
                if text in name:
                    if type_ in (None, "item"):
                        itemlist.append(item)
                    else:
                        if item['type'] in type_.split(','):
                            itemlist.append(item)
            elif mode == "id":
                if text.lower() in item['id'].lower():
                    if type_ in (None, "item"):
                        itemlist.append(item)
                    else:
                        if item['type'] in type_.split(','):
                            itemlist.append(item)
            elif mode == "set":
                if data['caseinsensitive'] is True:
                    text=jaconv.hira2kata(text.lower())
                    name=jaconv.hira2kata(item['set'].lower())
                else:
                    name=item['set']
                if text in name:
                    if type_ in (None, "item"):
                        itemlist.append(item)
                    else:
                        if item['type'] in type_.split(','):
                            itemlist.append(item)
        if data['loglevel'] == 'debug':
            print(yellow(f'{lang} {type_}: {text}\n{itemlist}'))
            dstore('ボット',f'```\n{lang} {type_}: {text}\n{itemlist}\n```')
        if len(itemlist) == 0:
            return None
        else:
            return itemlist
    except Exception:
        print(red(traceback.format_exc()))
        dstore('ボット',f'>>> {traceback.format_exc()}')
        return None

def search_style(lang, id_):
    if lang in ('en', 'ja'):
        with open(f'all{lang}.json', 'r', encoding='utf-8') as f:
            data_ = json.load(f)
    try:
        for item in data_['data']:
            if item['id'].lower() == id_.lower():
                if item['variants'] is not None:
                    variants = convert_variant(item['backendType'], item['variants'])
        print(yellow(f'{id_}: {variants}'))
        if len(variants) == 0:
            return None
        else:
            return variants
    except Exception:
        print(red(traceback.format_exc()))
        return None

async def reply(message, content):
    if isinstance(message, fortnitepy.message.MessageBase) is True:
        await message.reply(content)
    elif isinstance(message, discord.Message) is True:
        await message.channel.send(content)

async def change_asset(client, author_id, type_, id_, variants_ = {}, enlightenment = (0, 0)):
    global blacklist
    global blacklist_
    global whitelist
    global whitelist_
    if 'banner' in id_:
        variants = client.user.party.me.create_variants(profile_banner='ProfileBanner')
        variants += variants_ 
    else:
        variants = variants_
    if type_ == "outfit":
        flag = False
        if client.outfitlock is True:
            flag = lock_check(client, author_id)
        if flag is True:
            return False
        else:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_outfit, asset=id_, variants=variants, enlightenment=enlightenment))
    elif type_ == "backpack":
        flag = False
        if client.backpacklock is True:
            flag = lock_check(client, author_id)
        if flag is True:
            return False
        else:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_backpack, asset=id_, variants=variants))
    elif type_ == "pet":
        flag = False
        if client.backpacklock is True:
            flag = lock_check(client, author_id)
        if flag is True:
            return False
        else:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pet, asset=id_, variants=variants))
    elif type_ == "pickaxe":
        flag = False
        if client.pickaxelock is True:
            flag = lock_check(client, author_id)
        if flag is True:
            return False
        else:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_pickaxe, asset=id_, variants=variants))
    elif type_ == "emote":
        flag = False
        if client.emotelock is True:
            flag = lock_check(client, author_id)
        if flag is True:
            return False
        else:
            if client.user.party.me.emote is not None:
                if client.user.party.me.emote.lower() == id_.lower():
                    await client.user.party.me.clear_emote()
            await client.user.party.me.set_emote(asset=id_)
            client.eid=id_
    elif type_ == "emoji":
        flag = False
        if client.emotelock is True:
            flag = lock_check(client, author_id)
        if flag is True:
            return False
        else:
            if client.user.party.me.emote is not None:
                if client.user.party.me.emote.lower() == id_.lower():
                    await client.user.party.me.clear_emote()
            id_ = f"/Game/Athena/Items/Cosmetics/Dances/Emoji/{id_}.{id_}"
            await client.user.party.me.set_emote(asset=id_)
            client.eid=id_
    elif type_ == "toy":
        flag = False
        if client.emotelock is True:
            flag = lock_check(client, author_id)
        if flag is True:
            return False
        else:
            if client.user.party.me.emote is not None:
                if client.user.party.me.emote.lower() == id_.lower():
                    await client.user.party.me.clear_emote()
            id_ = f"/Game/Athena/Items/Cosmetics/Toys/{id_}.{id_}"
            await client.user.party.me.set_emote(asset=id_)
            client.eid=id_
    elif type_ == "shout":
        flag = False
        if client.emotelock is True:
            flag = lock_check(client, author_id)
        if flag is True:
            return False
        else:
            if client.user.party.me.emote is not None:
                if client.user.party.me.emote.lower() == id_.lower():
                    await client.user.party.me.clear_emote()
            id_ = f"/Game/Athena/Items/Cosmetics/Dances/Shouts/{id_}.{id_}"
            await client.user.party.me.set_emote(asset=id_)
            client.eid=id_
    return True

async def invitation_accept(invitation):
    client=invitation.client
    try:
        await invitation.accept()
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
        if data['ingame-error'] is True:
            await invitation.sender.send('Error')
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    except fortnitepy.PartyError:
        if data['ingame-error'] is True:
            await invitation.sender.send('既にパーティーのメンバーです')
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] 既にパーティーのメンバーです。'))
        dstore(client.user.display_name,f'>>> 既にパーティーのメンバーです')
    except fortnitepy.HTTPException:
        if data['ingame-error'] is True:
            await invitation.sender.send('メンバーが見つかりません。')
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] メンバーが見つかりません。'))
        dstore(client.user.display_name,f'>>> メンバーが見つかりません')
    except fortnitepy.Forbidden:
        if data['ingame-error'] is True:
            await invitation.sender.send('以前に参加したプライベートパーティーに参加しようとしています。(Epicサービス側のバグです)')
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] 以前に参加したプライベートパーティーに参加しようとしています。(Epicサービス側のバグです)'))
        dstore(client.user.display_name,f'>>> 以前に参加したプライベートパーティーに参加しようとしています。(Epicサービス側のバグです)')
    except fortnitepy.HTTPException:
        if data['ingame-error'] is True:
            await invitation.sender.send('パーティー招待の承諾リクエストを処理中にエラーが発生しました')
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
        if data['ingame-error'] is True:
            await invitation.sender.send('受信したnet_clとクライアントのnet_clが一致しません')
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] 受信したnet_clとクライアントのnet_clが一致しません。'))
        dstore(client.user.display_name,f'>>> 受信したnet_clとクライアントのnet_clが一致しません')
    except fortnitepy.HTTPException:
        if data['ingame-error'] is True:
            await invitation.sender.send('パーティー招待の拒否リクエストを処理中にエラーが発生しました。')
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
                print(f"[{now_()}] [{client.user.display_name}] {str(invitation.sender.display_name)} からの招待を所有者拒否")
            dstore(client.user.display_name,f'{str(invitation.sender.display_name)} からの招待を所有者拒否')
        else:
            if data['no-logs'] is False:
                print(f"[{now_()}] [{client.user.display_name}] {str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待を所有者拒否")
            dstore(client.user.display_name,f'{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待を所有者拒否')
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

async def invitation_decline_whitelist(invitation):
    try:
        await invitation.decline()
        await invitation.sender.send('ホワイトリストのユーザーがパーティーにいるため招待を拒否します')
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(f"[{now_()}] [{client.user.display_name}] {str(invitation.sender.display_name)} からの招待をホワイトリスト拒否")
            dstore(client.user.display_name,f'{str(invitation.sender.display_name)} からの招待をホワイトリスト拒否')
        else:
            if data['no-logs'] is False:
                print(f"[{now_()}] [{client.user.display_name}] {str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待をホワイトリスト拒否")
            dstore(client.user.display_name,f'{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}] からパーティー {invitation.party.id} への招待をホワイトリスト拒否')
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

async def aexec(code, variable):
    _ = lambda l: re.match(r"(\u0020|\u3000)*", l).end() * u"\u0020"
    scode = code.split('\n')
    delete = len(_(scode[0]))
    lines = [i.replace(u"\u0020", "", delete) for i in scode]
    var = []
    for line in lines:
        result = re.match(r" *.+ *=", line)
        if result is not None and "(" not in result.group(0) and "[" not in result.group(0):
            text = result.group(0)
            text = text.replace("=", "").strip()
            if text not in var:
                var.append(text)
    if data['loglevel'] == 'debug':
        print(var)
    
    text = ""
    for v in var:
        text += f"\n {v} = var['{v}']"
    
    code = '\n'.join(lines)
    locals_ = {}
    if data['loglevel'] == 'debug':
        print(
            f'var = locals()\nasync def __ex():\n global var'
            + text
            + ''.join(f'\n {l}' for l in code.split('\n'))
        )
    exec(
        f'var = locals()\nasync def __ex():\n global var'
        + text
        + ''.join(f'\n {l}' for l in code.split('\n')),
        variable,
        locals_
    )
    result = await locals_["__ex"]()
    for key in locals_.keys():
        if key != "__ex":
            globals()[key] = locals_[key]
    return result

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
    for key in configkeys:
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
    else:
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
        print(red('メールアドレスの数に対しパスワードの数が足りません。読み込めたアカウントのみ起動されます'))
        dstore('ボット',f'>>> メールアドレスの数に対しパスワードの数が足りません。読み込めたアカウントのみ起動されます')
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
    for key in commandskeys:
        exec(f"errorcheck=commands['{key}']")
    if data['caseinsensitive'] is True:
        commands=dict((k.lower(), jaconv.kata2hira(v.lower())) for k,v in commands.items())
    for checks in commands.items():
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

if True:
    if data['fortnite']['whisper'] not in (True, False):
        data['fortnite']['whisper'] = True
    if data['fortnite']['partychat'] not in (True, False):
        data['fortnite']['partychat'] = True
    if data['fortnite']['disablewhisperperfectly'] not in (True, False):
        data['fortnite']['disablewhisperperfectly'] = False
    if data['fortnite']['disablepartychatperfectly'] not in (True, False):
        data['fortnite']['disablepartychatperfectly'] = False
    if data['fortnite']['joinmessageenable'] not in (True, False):
        data['fortnite']['joinmessageenable'] = False
    if data['fortnite']['randommessageenable'] not in (True, False):
        data['fortnite']['randommessageenable'] = False
    if data['fortnite']['outfitmimic'] not in (True, False):
        data['fortnite']['outfitmimic'] = False
    if data['fortnite']['backpackmimic'] not in (True, False):
        data['fortnite']['backpackmimic'] = False
    if data['fortnite']['pickaxemimic'] not in (True, False):
        data['fortnite']['pickaxemimic'] = False
    if data['fortnite']['emotemimic'] not in (True, False):
        data['fortnite']['emotemimic'] = False
    if data['fortnite']['acceptinvite'] not in (True, False):
        data['fortnite']['acceptinvite'] = True
    if data['fortnite']['acceptfriend'] not in (True, False, None):
        data['fortnite']['acceptfriend'] = True
    if data['fortnite']['addfriend'] not in (True, False):
        data['fortnite']['addfriend'] = False
    if data['fortnite']['invite-ownerdecline'] not in (True, False):
        data['fortnite']['invite-ownerdecline'] = False
    if data['fortnite']['inviteinterval'] not in (True, False):
        data['fortnite']['inviteinterval'] = False
    if data['fortnite']['blacklist-declineinvite'] not in (True, False):
        data['fortnite']['blacklist-declineinvite'] = False
    if data['fortnite']['blacklist-autoblock'] not in (True, False):
        data['fortnite']['blacklist-autoblock'] = False
    if data['fortnite']['blacklist-autokick'] not in (True, False):
        data['fortnite']['blacklist-autokick'] = False
    if data['fortnite']['blacklist-autochatban'] not in (True, False):
        data['fortnite']['blacklist-autochatban'] = False
    if data['fortnite']['blacklist-ignorecommand'] not in (True, False):
        data['fortnite']['blacklist-ignorecommand'] = False
    if data['fortnite']['whitelist-allowinvite'] not in (True, False):
        data['fortnite']['whitelist-allowinvite'] = False
    if data['fortnite']['whitelist-declineinvite'] not in (True, False):
        data['fortnite']['whitelist-declineinvite'] = False
    if data['fortnite']['whitelist-ignorelock'] not in (True, False):
        data['fortnite']['whitelist-ignorelock'] = False
    if data['fortnite']['whitelist-ownercommand'] not in (True, False):
        data['fortnite']['whitelist-ownercommand'] = False

if True:
    if data['discord']['enabled'] not in (True, False):
        data['discord']['enabled'] = False
    if data['discord']['discord'] not in (True, False):
        data['discord']['discord'] = True
    if data['discord']['disablediscordperfectly'] not in (True, False):
        data['discord']['disablediscordperfectly'] = True
    if data['discord']['blacklist-ignorecommand'] not in (True, False):
        data['discord']['blacklist-ignorecommand'] = False
    if data['discord']['whitelist-ignorelock'] not in (True, False):
        data['discord']['whitelist-ignorelock'] = False
    if data['discord']['whitelist-ownercommand'] not in (True, False):
        data['discord']['whitelist-ownercommand'] = False

if True:
    if data['no-logs'] not in (True, False):
        data['no-logs'] = False
    if data['ingame-error'] not in (True, False):
        data['ingame-error'] = True
    if data['discord-log'] not in (True, False):
        data['discord-log'] = False
    if data['hide-email'] not in (True, False):
        data['hide-email'] = True
    if data['hide-password'] not in (True, False):
        data['hide-password'] = True
    if data['hide-webhook'] not in (True, False):
        data['hide-webhook'] = True
    if data['hide-api-key'] not in (True, False):
        data['hide-api-key'] = True
    if data['caseinsensitive'] not in (True, False):
        data['caseinsensitive'] = True
    if data['loglevel'] not in ('normal', 'info', 'debug'):
        data['loglevel'] = 'normal'
    if data['fortnite']['privacy'] not in ('public', 'friends_allow_friends_of_friends', 'friends', 'private_allow_friends_of_friends', 'private'):
        data['fortnite']['privacy'] = 'public'

data['fortnite']['privacy']=eval(f"fortnitepy.PartyPrivacy.{data['fortnite']['privacy'].upper()}")

print(cyan('ロビーボット: gomashio\nクレジット\nライブラリ: Terbau'))
dstore('ボット','ロビーボット: gomashio\nクレジット\nライブラリ: Terbau')
if True:
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
print(green(f'\nPython {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'))
print(green(f'Fortnitepy {fortnitepy.__version__}'))
print(green(f'discord.py {discord.__version__}'))
if data['debug'] is True:
    print(red(f'[{now_()}] デバッグが有効です!(エラーではありません)'))
    dstore('ボット','>>> デバッグが有効です!(エラーではありません)')
if data['no-logs'] is False:
    print('ボットを起動中...')
dstore('ボット','ボットを起動中...')

async def event_device_auth_generate(details, email):
    store_device_auth_details(email, details)

async def event_ready(client):
    global blacklist_flag
    global blacklist
    global whitelist_flag
    global whitelist
    global invitelist_flag
    global discord_flag
    global client_name
    if data['loglevel'] == 'normal':
        if data['no-logs'] is False:
            print(green(f'[{now_()}] ログイン: {client.user.display_name}'))
        dstore(client.user.display_name,f'ログイン: {client.user.display_name}')
    else:
        if data['no-logs'] is False:
            print(green(f'[{now_()}] ログイン: {client.user.display_name} / {client.user.id}'))
        dstore(client.user.display_name,f'ログイン: {client.user.display_name} / {client.user.id}')
    client.isready=True
    client_name[client.user.display_name] = client
    add_cache(client, client.user)
    for friend_ in client.friends.values():
        add_cache(client, friend_)
    for pending_ in client.pending_friends.values():
        add_cache(client, pending_)
    for block_ in client.blocked_users.values():
        add_cache(client, block_)

    try:
        client.owner=None
        owner=await client.fetch_profile(data['fortnite']['owner'])
        if owner is None:
            print(red(f'[{now_()}] [{client.user.display_name}] 所有者が見つかりません。正しい名前/IDになっているか確認してください。'))
            dstore(client.user.display_name,'>>> 所有者が見つかりません。正しい名前/IDになっているか確認してください')
        else:
            add_cache(client, owner)
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
    
    if client.owner is not None:
        await client.owner.send('ここをクリックして招待')

    if blacklist_flag is True:
        blacklist_flag = False
        for blacklistuser in data['fortnite']['blacklist']:
            try:
                user = await client.fetch_profile(blacklistuser)
                add_cache(client, user)
                if user is None:
                    print(red(f'[{now_()}] [{client.user.display_name}] ブラックリストのユーザー {blacklistuser} が見つかりません。正しい名前/IDになっているか確認してください。'))
                    dstore(client.user.display_name,f'>>>ブラックリストのユーザー {blacklistuser} が見つかりません。正しい名前/IDになっているか確認してください')
                else:
                    blacklist.append(user.id)
                    if data['loglevel'] == 'debug':
                        print(yellow(f"{str(user.display_name)} / {user.id}"))
                    if data['fortnite']['blacklist-autoblock'] is True:
                        try:
                            await user.block()
                        except Exception:
                            if data['loglevel'] == 'debug':
                                print(red(traceback.format_exc()))
                                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
                dstore(client.user.display_name,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        if data['loglevel'] == "debug":
            print(yellow(blacklist))
    if whitelist_flag is True:
        whitelist_flag = False
        for whitelistuser in data['fortnite']['whitelist']:
            try:
                user = await client.fetch_profile(whitelistuser)
                add_cache(client, user)
                if user is None:
                    print(red(f'[{now_()}] [{client.user.display_name}] ホワイトリストのユーザー {whitelistuser} が見つかりません。正しい名前/IDになっているか確認してください。'))
                    dstore(client.user.display_name,f'>>>ホワイトリストのユーザー {whitelistuser} が見つかりません。正しい名前/IDになっているか確認してください')
                else:
                    whitelist.append(user.id)
                    if data['loglevel'] == 'debug':
                        print(yellow(f"{str(user.display_name)} / {user.id}"))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
                dstore(client.user.display_name,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        if data['loglevel'] == "debug":
            print(yellow(whitelist))

    for invitelistuser in data['fortnite']['invitelist']:
        try:
            user = await client.fetch_profile(invitelistuser)
            if user is None:
                print(red(f'[{now_()}] [{client.user.display_name}] 招待リストのユーザー {invitelistuser} が見つかりません。正しい名前/IDになっているか確認してください。'))
                dstore(client.user.display_name,f'>>>招待リストのユーザー {invitelistuser} が見つかりません。正しい名前/IDになっているか確認してください')
            else:
                friend = client.get_friend(user.id)
                if friend is None and user.id != client.user.id:
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
                    print(red(f"[{now_()}] [{client.user.display_name}] 招待リストのユーザー {invitelistuser} とフレンドではありません。フレンドになってからもう一度起動するか、[{commands['reload']}] コマンドで再読み込みしてください。"))
                    dstore(client.user.display_name,f'>>> 招待リストのユーザー {invitelistuser} とフレンドではありません。フレンドになってからもう一度起動するか、[{commands["reload"]}] コマンドで再読み込みしてください')
                else:
                    add_cache(client, user)
                    client.invitelist.append(user.id)
                    if data['loglevel'] == 'debug':
                        print(yellow(f"{str(user.display_name)} / {user.id}"))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
            dstore(client.user.display_name,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    if data['loglevel'] == "debug":
        print(yellow(client.invitelist))

    if data['fortnite']['acceptfriend'] is True:
        pendings=[]
        for pending in client.pending_friends.copy().values():
            add_cache(client, pending)
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
    
    if data['discord']['enabled'] is True and discord_flag is True:
        discord_flag = False
        await dclient.start(data['discord']['token'])

async def event_restart():
    if data['no-logs'] is False:
        print(green(f'[{now_()}] 正常に再ログインが完了しました'))
    dstore('ボット',f'>>> 正常に再ログインが完了しました')

async def event_party_invite(invitation):
    global blacklist
    global whitelist
    if invitation is None:
        return
    client=invitation.client
    if client.isready is False:
        return
    add_cache(client, invitation.sender)
    if invitation.sender.id in blacklist:
        if data['fortnite']['blacklist-declineinvite'] is True:
            try:
                await invitation.decline()
            except Exception:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            return
    if client.owner is not None:
        if invitation.sender.id == client.owner.id:
            await invitation_accept(invitation)
            return
        elif invitation.sender.id in whitelist and data['fortnite']['whitelist-allowinvite'] is True:
            await invitation_accept(invitation)
            return
    else:
        if invitation.sender.id in whitelist and data['fortnite']['whitelist-allowinvite'] is True:
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

    if client.owner is not None:
        if client.owner.id in client.user.party.members.keys() and data['fortnite']['invite-ownerdecline'] is True:
            await invitation_decline_owner(invitation)
            return
    if True in [memberid in whitelist for memberid in client.user.party.members.keys()] and data['fortnite']['whitelist-declineinvite'] is True:
        await invitation_decline_whitelist(invitation)
    elif client.acceptinvite is False:
        await invitation_decline(invitation)
    elif client.acceptinvite_interval is False:
        await invitation_decline_interval(invitation)
    else:
        await invitation_accept(invitation)

async def event_friend_request(request):
    if request is None:
        return
    client=request.client
    if client.isready is False:
        return
    add_cache(client, request)
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
    add_cache(client, friend)
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
    add_cache(client, friend)
    if data['loglevel'] == 'normal':
        if data['no-logs'] is False:
            print(f'[{now_()}] [{client.user.display_name}] {str(friend.display_name)} がフレンドから削除')
        dstore(client.user.display_name,f'{str(friend.display_name)} がフレンドから削除')
    else:
        if data['no-logs'] is False:
            print(f'[{now_()}] [{client.user.display_name}] {str(friend.display_name)} / {friend.id} [{platform_to_str(friend.platform)}] がフレンドから削除')
        dstore(client.user.display_name,f'{str(friend.display_name)} / {friend.id} [{platform_to_str(friend.platform)}] がフレンドから削除')

async def event_party_member_join(member):
    global blacklist
    if member is None:
        return
    client=member.client
    if client.isready is False:
        return
    add_cache(client, member)
    client_user_display_name=str(client.user.display_name)
    member_joined_at_most=[]
    for member_ in client.user.party.members.values():
        add_cache(client, member_)
        try:
            if member_joined_at_most != []:
                if member_.id in [i.user.id for i in clients]:
                    if member_.id != client.user.id:
                        client_user_display_name+=f"/{str(member_.display_name)}"
                    if member_.joined_at < member_joined_at_most[1]:
                        member_joined_at_most=[member_.id, member_.joined_at]
            else:
                member_joined_at_most=[client.user.id, client.user.party.me.joined_at]
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    if member_joined_at_most == []:
        member_joined_at_most=[client.user.id]
    if client.user.id == member_joined_at_most[0]:
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [パーティー] [{client_user_display_name}] {str(member.display_name)} がパーティーに参加\n人数: {member.party.member_count}'))
            dstore(client_user_display_name,f'[パーティー] {str(member.display_name)} がパーティーに参加\n人数: {member.party.member_count}')
        else:
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [パーティー/{client.user.party.id}] [{client_user_display_name}] {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] がパーティーに参加\n人数: {member.party.member_count}'))
            dstore(client_user_display_name,f'[パーティー/{client.user.party.id}] {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] がパーティーに参加\n人数: {member.party.member_count}')
    
    if member.id in blacklist and client.user.party.me.leader is True:
        if data['fortnite']['blacklist-autokick'] is True:
            try:
                await member.kick()
            except Exception:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            return
        if data['fortnite']['blacklist-autochatban'] is True:
            try:
                await member.chatban()
            except Exception:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            return
    
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


    try:
        await change_asset(client, client.user.id, "emote", client.eid)
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
    add_cache(client, member)
    client_user_display_name=str(client.user.display_name)
    member_joined_at_most=[]
    for member_ in client.user.party.members.values():
        add_cache(client, member_)
        try:
            if member_joined_at_most != []:
                if member_.id in [i.user.id for i in clients]:
                    if member_.id != client.user.id:
                        client_user_display_name+=f"/{str(member_.display_name)}"
                    if member_.joined_at < member_joined_at_most[1]:
                        member_joined_at_most=[member_.id, member_.joined_at]
            else:
                member_joined_at_most=[client.user.id, client.user.party.me.joined_at]
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    if member_joined_at_most == []:
        member_joined_at_most=[client.user.id]
    if client.user.id == member_joined_at_most[0]:
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [パーティー] [{client_user_display_name}] {str(member.display_name)} がパーティーを離脱\n人数: {member.party.member_count}'))
            dstore(client_user_display_name,f'[パーティー] {str(member.display_name)} がパーティーを離脱\n人数: {member.party.member_count}')
        else:
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [パーティー/{client.user.party.id}] [{client_user_display_name}] {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] がパーティーを離脱\n人数: {member.party.member_count}'))
            dstore(client_user_display_name,f'[パーティー/{client.user.party.id}] {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] がパーティーを離脱\n人数: {member.party.member_count}')

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

async def event_party_member_confirm(confirmation):
    global blacklist
    if confirmation is None:
        return
    client=confirmation.client
    if client.isready is False:
        return
    add_cache(client, confirmation.user)
    if data['loglevel'] != 'normal':
        if data['no-logs'] is False:
            print(magenta(f'[{now_()}] [パーティー/{client.user.party.id}] [{client.user.display_name}] {str(confirmation.user.display_name)} / {confirmation.user.id} からのパーティー参加リクエスト'))
        dstore(client.user.display_name,f'[パーティー/{client.user.party.id}] {str(confirmation.user.display_name)} / {confirmation.user.id} からのパーティー参加リクエスト')
            
    if data['fortnite']['blacklist-autokick'] is True and confirmation.user.id in blacklist:
        try:
            await confirmation.reject()
        except fortnitepy.HTTPException:
            if data['loglevel'] == "debug":
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            print(red("パーティーへの参加リクエストの拒否リクエストを処理中にエラーが発生しました"))
    else:
        try:
            await confirmation.confirm()
        except fortnitepy.HTTPException:
            if data['loglevel'] == "debug":
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            print(red("パーティーへの参加リクエストの承認リクエストを処理中にエラーが発生しました"))

async def event_party_member_kick(member):
    if member is None:
        return
    client=member.client
    if client.isready is False:
        return
    add_cache(client, member)
    client_user_display_name=str(client.user.display_name)
    member_joined_at_most=[]
    for member_ in client.user.party.members.values():
        add_cache(client, member_)
        try:
            if member_joined_at_most != []:
                if member_.id in [i.user.id for i in clients]:
                    if member_.id != client.user.id:
                        client_user_display_name+=f"/{str(member_.display_name)}"
                    if member_.joined_at < member_joined_at_most[1]:
                        member_joined_at_most=[member_.id, member_.joined_at]
            else:
                member_joined_at_most=[client.user.id, client.user.party.me.joined_at]
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    if member_joined_at_most == []:
        member_joined_at_most=[client.user.id]
    if client.user.id == member_joined_at_most[0]:
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [パーティー] [{client_user_display_name}] {str(member.party.leader.display_name)} が {str(member.display_name)} をパーティーからキック\n人数: {member.party.member_count}'))
            dstore(client_user_display_name,f'[パーティー] {str(member.party.leader.display_name)} が {str(member.display_name)} をパーティーからキック\n人数: {member.party.member_count}')
        else:
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [パーティー/{client.user.party.id}] [{client_user_display_name}] {str(member.party.leader.display_name)} / {member.party.leader.id} [{platform_to_str(member.party.leader.platform)}/{member.input}] が {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] がパーティーからキック\n人数: {member.party.member_count}'))
            dstore(client_user_display_name,f'[パーティー/{client.user.party.id}] {str(member.party.leader.display_name)} / {member.party.leader.id} [{platform_to_str(member.party.leader.platform)}/{member.input}] が {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] がパーティーからキック\n人数: {member.party.member_count}')

async def event_party_member_promote(old_leader,new_leader):
    global blacklist
    if old_leader is None or new_leader is None:
        return
    client=new_leader.client
    if client.isready is False:
        return
    client_user_display_name=str(client.user.display_name)
    member_joined_at_most=[]
    for member_ in client.user.party.members.values():
        add_cache(client, member_)
        try:
            if member_joined_at_most != []:
                if member_.id in [i.user.id for i in clients]:
                    if member_.id != client.user.id:
                        client_user_display_name+=f"/{str(member_.display_name)}"
                    if member_.joined_at < member_joined_at_most[1]:
                        member_joined_at_most=[member_.id, member_.joined_at]
            else:
                member_joined_at_most=[client.user.id, client.user.party.me.joined_at]
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    if member_joined_at_most == []:
        member_joined_at_most=[client.user.id]
    if client.user.id == member_joined_at_most[0]:
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [パーティー] [{client_user_display_name}] {str(old_leader.display_name)} から {str(new_leader.display_name)} にリーダーが譲渡'))
            dstore(client_user_display_name,f'[パーティー] {str(old_leader.display_name)} から {str(new_leader.display_name)} にリーダーが譲渡')
        else:
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [パーティー/{client.user.party.id}] [{client_user_display_name}] {str(old_leader.display_name)} / {old_leader.id} [{platform_to_str(old_leader.platform)}/{old_leader.input}] から {str(new_leader.display_name)} / {new_leader.id} [{platform_to_str(new_leader.platform)}/{new_leader.input}] にリーダーが譲渡'))
            dstore(client_user_display_name,f'[パーティー/{client.user.party.id}] {str(old_leader.display_name)} / {old_leader.id} [{platform_to_str(old_leader.platform)}/{old_leader.input}] から {str(new_leader.display_name)} / {new_leader.id} [{platform_to_str(new_leader.platform)}/{new_leader.input}] にリーダーが譲渡')
    
    if new_leader.id == client.user.id:
        try:
            await client.user.party.set_playlist(data['fortnite']['playlist'])
            await client.user.party.set_privacy(data['fortnite']['privacy'])
            for member in client.user.party.members.values():
                if member.id in blacklist:
                    if data['fortnite']['blacklist-autokick'] is True:
                        try:
                            await member.kick()
                        except Exception:
                            if data['loglevel'] == 'debug':
                                print(red(traceback.format_exc()))
                                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                    if data['fortnite']['blacklist-autochatban'] is True:
                        try:
                            await member.chatban()
                        except Exception:
                            if data['loglevel'] == 'debug':
                                print(red(traceback.format_exc()))
                                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

async def event_party_member_update(member):
    global blacklist
    if member is None:
        return
    client=member.client
    if client.isready is False:
        return
    client_user_display_name=str(client.user.display_name)
    member_joined_at_most=[]
    for member_ in client.user.party.members.values():
        add_cache(client, member_)
        try:
            if member_joined_at_most != []:
                if member_.id in [i.user.id for i in clients]:
                    if member_.id != client.user.id:
                        client_user_display_name+=f"/{str(member_.display_name)}"
                    if member_.joined_at < member_joined_at_most[1]:
                        member_joined_at_most=[member_.id, member_.joined_at]
            else:
                member_joined_at_most=[client.user.id, client.user.party.me.joined_at]
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    if member_joined_at_most == []:
        member_joined_at_most=[client.user.id]
    if client.user.id == member_joined_at_most[0]:
        if data['loglevel'] != 'normal':
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [パーティー/{client.user.party.id}] [{client_user_display_name}] {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] パーティーメンバー更新'))
            dstore(client_user_display_name,f'[パーティー/{client.user.party.id}] {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] パーティーメンバー更新')
    
    if member.id == client.user.id:
        return
    if member.id in blacklist and client.user.party.me.leader is True:
        if data['fortnite']['blacklist-autokick'] is True:
            try:
                await member.kick()
            except Exception:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            return
        if data['fortnite']['blacklist-autochatban'] is True:
            try:
                await member.chatban()
            except Exception:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            return
    if member.outfit != client.prevoutfit or member.outfit_variants != client.prevoutfitvariants or member.enlightenments != client.prevenlightenments:
        if data['loglevel'] != 'normal':
            if client.user.id == member_joined_at_most[0]:
                if data['no-logs'] is False:
                    print(str(member.outfit))
                dstore(client_user_display_name,str(member.outfit))
        if client.outfitmimic is True:
            if member.outfit is None:
                try:
                    await change_asset(client, client.user.id, "outfit", "")
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            else:
                try:
                    await change_asset(client, client.user.id, "outfit", member.outfit, member.outfit_variants, member.enlightenments)
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    if partymember_backpack(member) != client.prevbackpack or member.backpack_variants != client.prevbackpackvariants:
        if data['loglevel'] != 'normal':
            if client.user.id == member_joined_at_most[0]:
                if data['no-logs'] is False:
                    print(str(partymember_backpack(member)))
                dstore(client_user_display_name,str(partymember_backpack(member)))
        if client.backpackmimic is True:
            if partymember_backpack(member) is None:
                try:
                    await change_asset(client, client.user.id, "backpack", "")
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            else:
                try:
                    type_ = convert_to_type(partymember_backpack(member))
                    await change_asset(client, client.user.id, type_, partymember_backpack(member), member.backpack_variants)
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    if member.pickaxe != client.prevpickaxe or member.pickaxe_variants != client.prevpickaxevariants:
        if data['loglevel'] != 'normal':
            if client.user.id == member_joined_at_most[0]:
                if data['no-logs'] is False:
                    print(str(member.pickaxe))
                dstore(client_user_display_name,str(member.pickaxe))
        if client.pickaxemimic is True:
            if member.pickaxe is None:
                try:
                    await change_asset(client, client.user.id, "pickaxe", "")
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            else:
                try:
                    await change_asset(client, client.user.id, "pickaxe", member.pickaxe, member.pickaxe_variants)
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    client.prevoutfit=member.outfit
    client.prevoutfitvariants=member.outfit_variants
    client.prevenlightenments=member.enlightenments
    client.prevbackpack=partymember_backpack(member)
    client.prevbackpackvariants=member.backpack_variants
    client.prevpickaxe=member.pickaxe
    client.prevpickaxevariants=member.pickaxe_variants

    if partymember_emote(member) is not None:
        if data['loglevel'] != 'normal':
            if client.user.id == member_joined_at_most[0]:
                if data['no-logs'] is False:
                    print(str(partymember_emote(member)))
                dstore(client_user_display_name,str(partymember_emote(member)))
        if client.emotemimic is True:
            try:
                type_ = convert_to_type(partymember_emote(member))
                await change_asset(client, client.user.id, type_, partymember_emote(member))
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
    add_cache(client, member)
    client_user_display_name=str(client.user.display_name)
    member_joined_at_most=[]
    for member_ in client.user.party.members.values():
        add_cache(client, member_)
        try:
            if member_joined_at_most != []:
                if member_.id in [i.user.id for i in clients]:
                    if member_.id != client.user.id:
                        client_user_display_name+=f"/{str(member_.display_name)}"
                    if member_.joined_at < member_joined_at_most[1]:
                        member_joined_at_most=[member_.id, member_.joined_at]
            else:
                member_joined_at_most=[client.user.id, client.user.party.me.joined_at]
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    if member_joined_at_most == []:
        member_joined_at_most=[client.user.id]
    if client.user.id == member_joined_at_most[0]:
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [パーティー] [{client_user_display_name}] {str(member.display_name)} の接続が切断'))
            dstore(client_user_display_name,f'[パーティー] {str(member.display_name)} の接続が切断')
        else:
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [パーティー/{client.user.party.id}] [{client_user_display_name}] {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] の接続が切断'))
            dstore(client_user_display_name,f'[パーティー/{client.user.party.id}] {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] の接続が切断')
    
    if client.user.party.me.leader is True:
        try:
            await member.kick()
        except Exception:
            if data['loglevel'] == "debug":
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

async def event_party_member_chatban(member, reason):
    if member is None:
        return
    client=member.client
    if client.isready is False:
        return
    client_user_display_name=str(client.user.display_name)
    member_joined_at_most=[]
    for member_ in client.user.party.members.values():
        add_cache(client, member_)
        try:
            if member_joined_at_most != []:
                if member_.id in [i.user.id for i in clients]:
                    if member_.id != client.user.id:
                        client_user_display_name+=f"/{str(member_.display_name)}"
                    if member_.joined_at < member_joined_at_most[1]:
                        member_joined_at_most=[member_.id, member_.joined_at]
            else:
                member_joined_at_most=[client.user.id, client.user.party.me.joined_at]
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
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
                    print(magenta(f'[{now_()}] [パーティー/{client.user.party.id}] [{client_user_display_name}] {str(member.party.leader.display_name)} / {member.party.leader.id} [{platform_to_str(member.party.leader.platform)}/{member.party.leader.input}] が {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] をチャットバン'))
                dstore(client_user_display_name,f'[パーティー/{client.user.party.id}] {str(member.party.leader.display_name)} / {member.party.leader.id} [{platform_to_str(member.party.leader.platform)}/{member.party.leader.input}] が {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] をチャットバン')
            else:
                if data['no-logs'] is False:
                    print(magenta(f'[{now_()}] [パーティー/{client.user.party.id}] [{client_user_display_name}] {str(member.party.leader.display_name)} / {member.party.leader.id} [{platform_to_str(member.party.leader.platform)}/{member.party.leader.input}] が {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] をチャットバン | 理由: {reason}'))
                dstore(client_user_display_name,f'[パーティー/{client.user.party.id}] {str(member.party.leader.display_name)} / {member.party.leader.id} [{platform_to_str(member.party.leader.platform)}/{member.party.leader.input}] が {str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}] をチャットバン | 理由: {reason}')

async def event_party_update(party):
    if party is None:
        return
    client=party.client
    if client.isready is False:
        return
    client_user_display_name=str(client.user.display_name)
    member_joined_at_most=[]
    for member_ in client.user.party.members.values():
        add_cache(client, member_)
        try:
            if member_joined_at_most != []:
                if member_.id in [i.user.id for i in clients]:
                    if member_.id != client.user.id:
                        client_user_display_name+=f"/{str(member_.display_name)}"
                    if member_.joined_at < member_joined_at_most[1]:
                        member_joined_at_most=[member_.id, member_.joined_at]
            else:
                member_joined_at_most=[client.user.id, client.user.party.me.joined_at]
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    if member_joined_at_most == []:
        member_joined_at_most=[client.user.id]
    if client.user.id == member_joined_at_most[0]:
        if data['loglevel'] != 'normal':
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [パーティー/{client.user.party.id}] [{client_user_display_name}] パーティー更新'))
            dstore(client_user_display_name,f'[パーティー/{client.user.party.id}] パーティー更新')

#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================

async def event_friend_message(message):
    global blacklist
    global whitelist
    global blacklist_
    global whitelist_
    global kill
    if message is None:
        return
    client=message.client
    if data['discord']['enabled'] is True and dclient.isready is False:
        return
    if client.isready is False:
        return
    name=client.user.display_name
    author_id = message.author.id
    loop = asyncio.get_event_loop()
    add_cache(client, message.author)
    if message.author.id in blacklist and data['fortnite']['blacklist-ignorecommand'] is True:
        return
    if client.owner is not None:
        if client.whisper is False:
            if client.whisperperfect is True:
                return
            elif message.author.id != client.owner.id and message.author.id not in whitelist:
                return
    else:
        if client.whisper is False:
            if message.author.id not in whitelist:
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

    flag = False
    if isinstance(message, fortnitepy.message.MessageBase) is True:
        if client.owner is not None:
            if data['fortnite']['whitelist-ownercommand'] is True:
                if client.owner.id != message.author.id and message.author.id not in whitelist:
                    flag = True
            else:
                if client.owner.id != message.author.id:
                    flag = True
        else:
            if data['fortnite']['whitelist-ownercommand'] is True:
                if message.author.id not in whitelist:
                    flag = True
            else:
                flag = True
    else:
        if dclient.owner is not None:
            if data['discord']['whitelist-ownercommand'] is True:
                if client.owner.id != message.author.id and message.author.id not in whitelist_:
                    flag = True
            else:
                if client.owner.id != message.author.id:
                    flag = True
        else:
            if data['discord']['whitelist-ownercommand'] is True:
                if message.author.id not in whitelist_:
                    flag = True
            else:
                flag = True
    if flag is True:
        for checks in commands.items():
            if checks[0] in ignore:
                continue
            if commands['ownercommands'] == '':
                break
            for command in commands['ownercommands'].split(','):
                if args[0] in commands[command.lower()].split(','):
                    await reply(message, 'このコマンドは管理者しか使用できません')
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
        if args[0] in key.split(','):
            try:
                await reply(message, value)
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')
            return

    if data['discord']['enabled'] is True and dclient.isready is True:
        if args[0] in commands['addblacklist_discord'].split(','):
            try:
                if rawcontent == '' or args[1].isdigit() is False:
                    await reply(message, f"[{commands['addblacklist_discord']}] [ユーザーID]")
                    return
                user = dclient.get_user(int(args[1]))
                if user is None:
                    user = await dclient.fetch_user(int(args[1]))
                if user.id not in blacklist_:
                    blacklist_.append(user.id)
                    data["discord"]["blacklist"].append(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["discord"]["blacklist"] = data["discord"]["blacklist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, f"ユーザー {user} / {user.id} をブラックリストに追加しました")
                else:
                    await reply(message, f"ユーザー {user} / {user.id} は既にブラックリストに追加されています")
            except discord.NotFound:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザーが見つかりません')
            except discord.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
                dstore(name,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました。')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['removeblacklist_discord'].split(','):
            try:
                if rawcontent == '' or args[1].isdigit() is False:
                    await reply(message, f"[{commands['removeblacklist_discord']}] [ユーザーID]")
                    return
                user = dclient.get_user(int(args[1]))
                if user is None:
                    user = await dclient.fetch_user(int(args[1]))
                if user.id in blacklist_:
                    blacklist_.remove(user.id)
                    data["discord"]["blacklist"].remove(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["discord"]["blacklist"] = data["discord"]["blacklist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, f"ユーザー {user} / {user.id} をブラックリストから削除")
                else:
                    await reply(message, f"ユーザー {user} / {user.id} はブラックリストに含まれていません")
            except discord.NotFound:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザーが見つかりません')
            except discord.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
                dstore(name,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました。')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['addwhitelist_discord'].split(','):
            try:
                if rawcontent == '' or args[1].isdigit() is False:
                    await reply(message, f"[{commands['addwhitelist_discord']}] [ユーザーID]")
                    return
                user = dclient.get_user(int(args[1]))
                if user is None:
                    user = await dclient.fetch_user(int(args[1]))
                if user.id not in whitelist_:
                    whitelist_.append(user.id)
                    data["discord"]["whitelist"].append(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["discord"]["whitelist"] = data["discord"]["whitelist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, f"ユーザー {user} / {user.id} をホワイトリストに追加しました")
                else:
                    await reply(message, f"ユーザー {user} / {user.id} は既にホワイトリストに追加されています")
            except discord.NotFound:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザーが見つかりません')
            except discord.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
                dstore(name,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました。')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['removewhitelist_discord'].split(','):
            try:
                if rawcontent == '' or args[1].isdigit() is False:
                    await reply(message, f"[{commands['removewhitelist_discord']}] [ユーザーID]")
                    return
                user = dclient.get_user(int(args[1]))
                if user is None:
                    user = await dclient.fetch_user(int(args[1]))
                if user.id in whitelist_:
                    whitelist_.remove(user.id)
                    data["discord"]["whitelist"].remove(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["discord"]["whitelist"] = data["discord"]["whitelist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, f"ユーザー {user} / {user.id} をホワイトリストから削除")
                else:
                    await reply(message, f"ユーザー {user} / {user.id} はホワイトリストに含まれていません")
            except discord.NotFound:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザーが見つかりません')
            except discord.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
                dstore(name,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました。')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

    if args[0] in commands['eval'].split(','):
        try:
            if rawcontent == "":
                await reply(message, f"[{commands['eval']}] [式]")
                return
            variable=globals()
            variable.update(locals())
            if rawcontent.startswith("await "):
                if data['loglevel'] == "debug":
                    print(f"await eval({rawcontent.replace('await ','',1)})")
                result = await eval(rawcontent.replace("await ","",1), variable)
                await reply(message, str(result))
            else:
                if data['loglevel'] == "debug":
                    print(f"eval {rawcontent}")
                result = eval(rawcontent, variable)
                await reply(message, str(result))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['exec'].split(','):
        try:
            if rawcontent == "":
                await reply(message, f"[{commands['exec']}] [文]")
                return
            variable=globals()
            variable.update(locals())
            args_=[i.replace("\\nn", "\n") for i in content.replace("\n", "\\nn").split()]
            content_=" ".join(args_[1:])
            result = await aexec(content_, variable)
            await reply(message, str(result))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['restart'].split(','):
        try:
            flag = False
            if client.acceptinvite is False:
                if isinstance(message, fortnitepy.message.MessageBase) is True:
                    if client.owner is not None:
                        if data['fortnite']['whitelist-ownercommand'] is True:
                            if client.owner.id != message.author.id and message.author.id not in whitelist:
                                flag = True
                        else:
                            if client.owner.id != message.author.id:
                                flag = True
                    else:
                        if data['fortnite']['whitelist-ownercommand'] is True:
                            if message.author.id not in whitelist:
                                flag = True
                        else:
                            flag = True
                elif isinstance(message, discord.Message) is True:
                    if dclient.owner is not None:
                        if data['discord']['whitelist-ownercommand'] is True:
                            if dclient.owner.id != message.author.id and message.author.id not in whitelist_:
                                flag = True
                        else:
                            if dclient.owner.id != message.author.id:
                                flag = True
                    else:
                        if data['discord']['whitelist-ownercommand'] is True:
                            if message.author.id not in whitelist_:
                                flag = True
                        else:
                            flag = True
            if flag is True:
                await reply(message, '招待が拒否に設定されているので実行できません')
                return
            await reply(message, 'プログラムを再起動します...')
            os.chdir(os.getcwd())
            os.execv(os.sys.executable,['python','index.py'])
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['relogin'].split(','):
        try:
            flag = False
            if client.acceptinvite is False:
                if isinstance(message, fortnitepy.message.MessageBase) is True:
                    if client.owner is not None:
                        if data['fortnite']['whitelist-ownercommand'] is True:
                            if client.owner.id != message.author.id and message.author.id not in whitelist:
                                flag = True
                        else:
                            if client.owner.id != message.author.id:
                                flag = True
                    else:
                        if data['fortnite']['whitelist-ownercommand'] is True:
                            if message.author.id not in whitelist:
                                flag = True
                        else:
                            flag = True
                elif isinstance(message, discord.Message) is True:
                    if dclient.owner is not None:
                        if data['discord']['whitelist-ownercommand'] is True:
                            if dclient.owner.id != message.author.id and message.author.id not in whitelist_:
                                flag = True
                        else:
                            if dclient.owner.id != message.author.id:
                                flag = True
                    else:
                        if data['discord']['whitelist-ownercommand'] is True:
                            if message.author.id not in whitelist_:
                                flag = True
                        else:
                            flag = True
            if flag is True:
                await reply(message, '招待が拒否に設定されているので実行できません')
                return
            await reply(message, 'アカウントに再ログインします...')
            await client.restart()
        except fortnitepy.AuthException:
            print(red(traceback.format_exc()))
            print(red(f'[{now_()}] [{client.user.display_name}] メールアドレスまたはパスワードが間違っています。'))
            dstore(name,f'>>> {traceback.format_exc()}')
            dstore(name,f'>>> メールアドレスまたはパスワードが間違っています')
            kill=True
            exit()
        except Exception:
            print(red(traceback.format_exc()))
            print(red(f'[{now_()}] [{client.user.display_name}] アカウントの読み込みに失敗しました。もう一度試してみてください。'))
            dstore(name,f'>>> {traceback.format_exc()}')
            dstore(name,f'>>> アカウントの読み込みに失敗しました。もう一度試してみてください')
            kill=True
            exit()

    elif args[0] in commands['reload'].split(','):
        result=reload_configs(client)
        try:
            if result == 'Success':
                await reply(message, '正常に読み込みが完了しました')
            else:
                await reply(message, 'エラー')
                return
            try:
                client.owner=None
                owner=await client.fetch_profile(data['fortnite']['owner'])
                if owner is None:
                    print(red(f'[{now_()}] [{client.user.display_name}] 所有者が見つかりません。正しい名前/IDになっているか確認してください。'))
                    dstore(client.user.display_name,'>>> 所有者が見つかりません。正しい名前/IDになっているか確認してください')
                else:
                    add_cache(client, owner)
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

            for blacklistuser in data['fortnite']['blacklist']:
                try:
                    user = await client.fetch_profile(blacklistuser)
                    add_cache(client, user)
                    if user is None:
                        print(red(f'[{now_()}] [{client.user.display_name}] ブラックリストのユーザー {blacklistuser} が見つかりません。正しい名前/IDになっているか確認してください。'))
                        dstore(client.user.display_name,f'>>>ブラックリストのユーザー {blacklistuser} が見つかりません。正しい名前/IDになっているか確認してください')
                    else:
                        blacklist.append(user.id)
                        if data['loglevel'] == 'debug':
                            print(yellow(f"{str(user.display_name)} / {user.id}"))
                        if data['fortnite']['blacklist-autoblock'] is True:
                            try:
                                await user.block()
                            except Exception:
                                if data['loglevel'] == 'debug':
                                    print(red(traceback.format_exc()))
                                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                    print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
                    dstore(client.user.display_name,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            if data['loglevel'] == "debug":
                print(yellow(blacklist))
            for whitelistuser in data['fortnite']['whitelist']:
                try:
                    user = await client.fetch_profile(whitelistuser)
                    add_cache(client, user)
                    if user is None:
                        print(red(f'[{now_()}] [{client.user.display_name}] ホワイトリストのユーザー {whitelistuser} が見つかりません。正しい名前/IDになっているか確認してください。'))
                        dstore(client.user.display_name,f'>>>ホワイトリストのユーザー {whitelistuser} が見つかりません。正しい名前/IDになっているか確認してください')
                    else:
                        whitelist.append(user.id)
                        if data['loglevel'] == 'debug':
                            print(yellow(f"{str(user.display_name)} / {user.id}"))
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                    print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
                    dstore(client.user.display_name,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            if data['loglevel'] == "debug":
                print(yellow(whitelist))

            for invitelistuser in data['fortnite']['invitelist']:
                try:
                    user = await client.fetch_profile(invitelistuser)
                    if user is None:
                        print(red(f'[{now_()}] [{client.user.display_name}] 招待リストのユーザー {invitelistuser} が見つかりません。正しい名前/IDになっているか確認してください。'))
                        dstore(client.user.display_name,f'>>>招待リストのユーザー {invitelistuser} が見つかりません。正しい名前/IDになっているか確認してください')
                    else:
                        friend = client.get_friend(user.id)
                        if friend is None and user.id != client.user.id:
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
                            print(red(f"[{now_()}] [{client.user.display_name}] 招待リストのユーザー {invitelistuser} とフレンドではありません。フレンドになってからもう一度起動するか、[{commands['reload']}] コマンドで再読み込みしてください。"))
                            dstore(client.user.display_name,f'>>> 招待リストのユーザー {invitelistuser} とフレンドではありません。フレンドになってからもう一度起動するか、[{commands["reload"]}] コマンドで再読み込みしてください')
                        else:
                            add_cache(client, user)
                            client.invitelist.append(user.id)
                            if data['loglevel'] == 'debug':
                                print(yellow(f"{str(user.display_name)} / {user.id}"))
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                    print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
                    dstore(client.user.display_name,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            if data['loglevel'] == "debug":
                print(yellow(client.invitelist))
            if data['discord']['enabled'] is True:
                dclient_user = str(dclient.user)
                activity = discord.Game(name=data['discord']['status'])
                await dclient.change_presence(activity=activity)

                for blacklistuser in data['discord']['blacklist']:
                    user = dclient.get_user(blacklistuser)
                    if user is None:
                        try:
                            user = await dclient.fetch_user(blacklistuser)
                        except discord.NotFound:
                            if data['loglevel'] == "debug":
                                print(red(traceback.format_exc()))
                                dstore(dclient_user,f'>>> {traceback.format_exc()}')
                            user = None
                    if user is None:
                        print(red(f'[{now_()}] [{dclient_user}] ブラックリストのユーザー {blacklistuser} が見つかりません。正しいIDになっているか確認してください。'))
                        dstore(dclient_user,f'>>>ブラックリストのユーザー {blacklistuser} が見つかりません。正しいIDになっているか確認してください')
                    else:
                        blacklist_.append(user.id)
                        if data['loglevel'] == 'debug':
                            print(yellow(f"{user} / {user.id}"))
                if data['loglevel'] == "debug":
                    print(yellow(blacklist_))
                for whitelistuser in data['discord']['whitelist']:
                    user = dclient.get_user(whitelistuser)
                    if user is None:
                        try:
                            user = await dclient.fetch_user(whitelistuser)
                        except discord.NotFound:
                            if data['loglevel'] == "debug":
                                print(red(traceback.format_exc()))
                                dstore(dclient_user,f'>>> {traceback.format_exc()}')
                            user = None
                    if user is None:
                        print(red(f'[{now_()}] [{dclient_user}] ホワイトリストのユーザー {whitelistuser} が見つかりません。正しいIDになっているか確認してください。'))
                        dstore(dclient_user,f'>>>ホワイトリストのユーザー {whitelistuser} が見つかりません。正しいIDになっているか確認してください')
                    else:
                        whitelist_.append(user.id)
                        if data['loglevel'] == 'debug':
                            print(yellow(f"{user.display_name} / {user.id}"))
                if data['loglevel'] == "debug":
                    print(yellow(whitelist_))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['addblacklist'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['addblacklist']}] [ユーザー名/ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and user.id not in blacklist}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and user.id not in blacklist:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if user.id not in blacklist:
                    blacklist.append(user.id)
                    if user.display_name is not None:
                        data["fortnite"]["blacklist"].append(user.display_name)
                    else:
                        data["fortnite"]["blacklist"].append(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をブラックリストに追加しました")
                else:
                    await reply(message, f"ユーザー {str(user.display_name)} / {user.id} は既にブラックリストに追加されています")
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        if user.id not in blacklist:
            blacklist.append(user.id)
            if user.display_name is not None:
                data["fortnite"]["blacklist"].append(user.display_name)
            else:
                data["fortnite"]["blacklist"].append(user.id)
            try:
                with open("config.json", "r", encoding="utf-8") as f:
                    data_ = json.load(f)
            except json.decoder.JSONDecodeError:
                with open("config.json", "r", encoding="utf-8-sig") as f:
                    data_ = json.load(f)
            data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
            await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をブラックリストに追加しました")
        else:
            await reply(message, f"ユーザー {str(user.display_name)} / {user.id} は既にブラックリストに追加されています")""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーをブラックリストに追加します"
                await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['removeblacklist'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['removeblacklist']}] [ユーザー名/ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and user.id in blacklist}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and user.id in blacklist:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if user.id in blacklist:
                    blacklist.remove(user.id)
                    try:
                        data["fortnite"]["blacklist"].remove(user.display_name)
                    except ValueError:
                        data["fortnite"]["blacklist"].remove(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をブラックリストから削除")
                else:
                    await reply(message, f"ユーザー {str(user.display_name)} / {user.id} はブラックリストに含まれていません")
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        if user.id in blacklist:
            blacklist.remove(user.id)
            try:
                data["fortnite"]["blacklist"].remove(user.display_name)
            except ValueError:
                data["fortnite"]["blacklist"].remove(user.id)
            try:
                with open("config.json", "r", encoding="utf-8") as f:
                    data_ = json.load(f)
            except json.decoder.JSONDecodeError:
                with open("config.json", "r", encoding="utf-8-sig") as f:
                    data_ = json.load(f)
            data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
            await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をブラックリストから削除")
        else:
            await reply(message, f"ユーザー {str(user.display_name)} / {user.id} はブラックリストに含まれていません")""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーをブラックリストから削除します"
                await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['addwhitelist'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['addwhitelist']}] [ユーザー名/ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and user.id not in whitelist}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and user.id not in whitelist:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if user.id not in whitelist:
                    whitelist.append(user.id)
                    if user.display_name is not None:
                        data["fortnite"]["whitelist"].append(user.display_name)
                    else:
                        data["fortnite"]["whitelist"].append(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["fortnite"]["whitelist"] = data["fortnite"]["whitelist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をホワイトリストに追加しました")
                else:
                    await reply(message, f"ユーザー {str(user.display_name)} / {user.id} は既にホワイトリストに追加されています")
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        if user.id not in whitelist:
            whitelist.append(user.id)
            if user.display_name is not None:
                data["fortnite"]["whitelist"].append(user.display_name)
            else:
                data["fortnite"]["whitelist"].append(user.id)
            try:
                with open("config.json", "r", encoding="utf-8") as f:
                    data_ = json.load(f)
            except json.decoder.JSONDecodeError:
                with open("config.json", "r", encoding="utf-8-sig") as f:
                    data_ = json.load(f)
            data_["fortnite"]["whitelist"] = data["fortnite"]["whitelist"]
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
            await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をホワイトリストに追加しました")
        else:
            await reply(message, f"ユーザー {str(user.display_name)} / {user.id} は既にホワイトリストに追加されています")""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーをホワイトリストに追加します"
                await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['removewhitelist'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['removewhitelist']}] [ユーザー名/ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and user.id in whitelist}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and user.id in whitelist:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if user.id in whitelist:
                    whitelist.remove(user.id)
                    try:
                        data["whitelist"].remove(user.display_name)
                    except ValueError:
                        data["whitelist"].remove(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["whitelist"] = data["whitelist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をホワイトリストから削除")
                else:
                    await reply(message, f"ユーザー {str(user.display_name)} / {user.id} はホワイトリストに含まれていません")
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        if user.display_name in data["blacklist"] or user.id in data["blacklist"]:
            blacklist.remove(user.id)
            try:
                data["blacklist"].remove(user.display_name)
            except ValueError:
                data["blacklist"].remove(user.id)
            try:
                with open("config.json", "r", encoding="utf-8") as f:
                    data_ = json.load(f)
            except json.decoder.JSONDecodeError:
                with open("config.json", "r", encoding="utf-8-sig") as f:
                    data_ = json.load(f)
            data_["blacklist"] = data["blacklist"]
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
            await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をブラックリストから削除")
        else:
            await reply(message, f"ユーザー {str(user.display_name)} / {user.id} はブラックリストに含まれていません")""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーをホワイトリストから削除します"
                await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['get'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['get']}] [ユーザー名/ユーザーID]")
                return
            users = {member.display_name: member for member in client.user.party.members.values() if rawcontent.lower() in member.display_name.lower() and member.display_name is not None}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.user.party.members.get(user.id) is not None:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                member=client.user.party.members.get(user.id)
                if member is None:
                    await reply(message, "ユーザーがパーティーにいません")
                    return
                if data['no-logs'] is False:
                    print(f'{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}')
                if data['loglevel'] == 'debug':
                    print(json.dumps(member.meta.schema, indent=2))
                dstore(name,f'{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}')
                await reply(message, f'{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}')
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        member=client.user.party.members.get(user.id)
        if member is None:
            await reply(message, "ユーザーがパーティーにいません")
            return
        if data['no-logs'] is False:
            print(f'''{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}''')
        if data['loglevel'] == 'debug':
            print(json.dumps(member.meta.schema, indent=2))
        dstore(name,f'''{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}''')
        await reply(message, f'''{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}''')""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーの情報を取得します"
                await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['friendcount'].split(','):
        try:
            if data['no-logs'] is False:
                print(f'フレンド数: {len(client.friends)}')
            dstore(name,f'フレンド数: {len(client.friends)}')
            await reply(message, f'フレンド数: {len(client.friends)}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

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
            dstore(name,f'保留数: {len(client.pending_friends)}\n送信: {len(outbound)}\n受信: {len(inbound)}')
            await reply(message, f'保留数: {len(client.pending_friends)}\n送信: {len(outbound)}\n受信: {len(inbound)}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['blockcount'].split(','):
        try:
            if data['no-logs'] is False:
                print(f'ブロック数: {len(client.blocked_users)}')
            dstore(name,f'ブロック数: {len(client.blocked_users)}')
            await reply(message, f'ブロック数: {len(client.blocked_users)}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['friendlist'].split(','):
        try:
            text=''
            for friend in client.friends.values():
                add_cache(client, friend)
                text+=f'\n{friend}'
            if data['no-logs'] is False:
                print(f'{text}')
            dstore(name,f'{text}')
            await reply(message, f'{text}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['pendinglist'].split(','):
        try:
            outbound=''
            inbound=''
            for pending in client.pending_friends.values():
                add_cache(client, pending)
                if pending.direction == 'OUTBOUND':
                    outbound+=f'\n{pending}'
                elif pending.direction == 'INBOUND':
                    inbound+=f'\n{pending}'
            if data['no-logs'] is False:
                print(f'送信: {outbound}\n受信: {inbound}')
            dstore(name,f'送信: {outbound}\n受信: {inbound}')
            await reply(message, f'送信: {outbound}\n受信: {inbound}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['blocklist'].split(','):
        try:
            text=''
            for block in client.blocked_users.values():
                add_cache(client, block)
                text+=f'\n{block}'
            if data['no-logs'] is False:
                print(f'{text}')
            dstore(name,f'{text}')
            await reply(message, f'{text}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['outfitmimic'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.outfitmimic=True
                await reply(message, 'コスチュームミミックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.outfitmimic=False
                await reply(message, 'コスチュームミミックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['skinmimic']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['backpackmimic'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.backpackmimic=True
                await reply(message, 'バックアクセサリーミミックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.backpackmimic=False
                await reply(message, 'バックアクセサリーミミックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['skinmimic']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['pickaxemimic'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.pickaxemimic=True
                await reply(message, '収集ツールミミックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.pickaxemimic=False
                await reply(message, '収集ツールミミックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['skinmimic']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['emotemimic'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.emotemimic=True
                await reply(message, 'エモートミミックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.emotemimic=False
                await reply(message, 'エモートミミックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['emotemimic']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['whisper'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.whisper=True
                await reply(message, '囁きからのコマンド受付をオンに設定')
            elif args[1] in commands['false'].split(','):
                client.whisper=False
                await reply(message, '囁きからのコマンド受付をオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['whisper']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['partychat'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.partychat=True
                await reply(message, 'パーティーチャットからのコマンド受付をオンに設定')
            elif args[1] in commands['false'].split(','):
                client.partychat=False
                await reply(message, 'パーティーチャットからのコマンド受付をオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['party']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['discord'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.discord=True
                await reply(message, 'Discordからのコマンド受付をオンに設定')
            elif args[1] in commands['false'].split(','):
                client.discord=False
                await reply(message, 'Discordからのコマンド受付をオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['discord']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['disablewhisperperfectly'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.whisperperfect=True
                await reply(message, '囁きの完全無効をオンに設定')
            elif args[1] in commands['false'].split(','):
                client.whisperperfect=False
                await reply(message, '囁きの完全無効をオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['disablewhisperperfectly']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['disablepartychatperfectly'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.partychatperfect=True
                await reply(message, 'パーティーチャットの完全無効をオンに設定')
            elif args[1] in commands['false'].split(','):
                client.partychatperfect=False
                await reply(message, 'パーティーチャットの完全無効をオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['disablepartychatperfectly']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['disablediscordperfectly'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.discordperfect=True
                await reply(message, 'Discordの完全無効をオンに設定')
            elif args[1] in commands['false'].split(','):
                client.discordperfect=False
                await reply(message, 'Discordの完全無効をオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['disablediscordperfectly']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['acceptinvite'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.acceptinvite=True
                await reply(message, '招待を承諾に設定')
            elif args[1] in commands['false'].split(','):
                client.acceptinvite=False
                await reply(message, '招待を拒否に設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['acceptinvite']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['acceptfriend'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.acceptfriend=True
                await reply(message, 'フレンド申請を承諾に設定')
            elif args[1] in commands['false'].split(','):
                client.acceptfriend=False
                await reply(message, 'フレンド申請を拒否に設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['acceptfriend']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['joinmessageenable'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.joinmessageenable=True
                await reply(message, 'パーティー参加時のメッセージをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.joinmessageenable=False
                await reply(message, 'パーティー参加時のメッセージをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['joinmessageenable']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['randommessageenable'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.randommessageenable=True
                await reply(message, 'パーティー参加時のランダムメッセージをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.randommessageenable=False
                await reply(message, 'パーティー参加時のランダムメッセージをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['randommessageenable']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

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
                await reply(message, f"{str(data['fortnite']['waitinterval'])}秒間招待を拒否します")
            else:
                if client.owner.id in client.user.party.members.keys() and message.author.id != client.owner.id:
                    await reply(message, '現在利用できません')
                    return
                client.acceptinvite=False
                try:
                    client.timer_.cancel()
                except AttributeError:
                    pass
                client.timer_=Timer(data['fortnite']['waitinterval'], inviteaccept, [client])
                client.timer_.start()
                await reply(message, f"{str(data['fortnite']['waitinterval'])}秒間招待を拒否します")             
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['join'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['join']}] [ユーザー名/ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.has_friend(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.has_friend(user.id) is True:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                friend=client.get_friend(user.id)
                if friend is None:
                    await reply(message, 'ユーザーとフレンドではありません')
                else:
                    await friend.join_party()
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            friend=client.get_friend(user.id)
            if friend is None:
                await reply(message, 'ユーザーとフレンドではありません')
            else:
                await friend.join_party()
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーが満員か、既にパーティーにいるか、ユーザーがオフラインです')
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーが見つかりません')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーがプライベートです')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーの参加リクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーのパーティーに参加します"
                await reply(message, text)
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーが満員か、既にパーティーにいるか、ユーザーがオフラインです')
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーが見つかりません')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーがプライベートです')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーの参加リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['joinid'].split(','):
        try:
            await client.join_to_party(party_id=args[1])
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, '既にこのパーティーのメンバーです')
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーが見つかりません')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーがプライベートです')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['join']}] [パーティーID]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['leave'].split(','):
        try:
            await client.user.party.me.leave()
            await reply(message, 'パーティーを離脱')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティー離脱のリクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['invite'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['invite']}] [ユーザー名 / ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.has_friend(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.has_friend(user.id) is True:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                friend=client.get_friend(user.id)
                if friend is None:
                    await reply(message, 'ユーザーとフレンドではありません')
                    return
                await friend.invite()
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(friend.display_name)} をパーティーに招待')
                else:
                    await reply(message, f'{str(friend.display_name)} / {friend.id} をパーティー {client.user.party.id} に招待')
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            friend=client.get_friend(user.id)
            if friend is None:
                await reply(message, 'ユーザーとフレンドではありません')
                return
            await friend.invite()
            if data['loglevel'] == 'normal':
                await reply(message, f'{str(friend.display_name)} をパーティーに招待')
            else:
                await reply(message, f'{str(friend.display_name)} / {friend.id} をパーティー {client.user.party.id} に招待')
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーが満員か、既にパーティーにいます')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティー招待の送信リクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーを招待します"
                await reply(message, text)
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーが満員か、既にパーティーにいます')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティー招待の送信リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['inviteall'].split(','):
        try:
            for inviteuser in client.invitelist:
                if inviteuser != client.user.id and inviteuser not in client.user.party.members:
                    try:
                        await client.user.party.invite(inviteuser)
                    except fortnitepy.PartyError:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(name,f'>>> {traceback.format_exc()}')
                        await reply(message, 'パーティーが満員か、既にパーティーにいます')
                    except fortnitepy.Forbidden:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(name,f'>>> {traceback.format_exc()}')
                        await reply(message, 'ユーザーとフレンドではありません')
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(name,f'>>> {traceback.format_exc()}')
                        await reply(message, 'パーティー招待の送信リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['message'].split(','):
        try:
            send=rawcontent.split(' : ')
            if len(send) < 2:
                await reply(message, f"[{commands['message']}] [ユーザー名 / ユーザーID] : [内容]")
                return
            users = {name: user for name, user in cache_users.items() if send[0].lower() in name.lower() and user.id != client.user.id and client.has_friend(user.id) is True}
            try:
                user=await client.fetch_profile(send[0])
                if user is not None:
                    if user.display_name is not None and client.has_friend(user.id) is True:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                friend=client.get_friend(user.id)
                if friend is None:
                    await reply(message, 'ユーザーとフレンドではありません')
                    return
                await friend.send(send[1])
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(friend.display_name)} にメッセージ {send[1]} を送信')
                else:
                    await reply(message, f'{str(friend.display_name)} / {friend.id} にメッセージ {send[1]} を送信')
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            friend=client.get_friend(user.id)
            if friend is None:
                await reply(message, 'ユーザーとフレンドではありません')
                return
            await friend.send(send[1])
            if data['loglevel'] == 'normal':
                await reply(message, f'{str(friend.display_name)} にメッセージ {send[1]} を送信')
            else:
                await reply(message, f'{str(friend.display_name)} / {friend.id} にメッセージ {send[1]} を送信')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user, "send": send} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーにメッセージを送信します"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['message']}] [ユーザー名 / ユーザーID] : [内容]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['partymessage'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['partymessage']}] [内容]")
                return
            await client.user.party.send(rawcontent)
            if data['loglevel'] == 'normal':
                await reply(message, f'パーティーにメッセージ {rawcontent} を送信')
            else:
                await reply(message, f'パーティー {client.user.party.id} にメッセージ {rawcontent} を送信')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['status'].split(','):
        try:
            await client.set_status(rawcontent)
            await reply(message, f'ステータスを {rawcontent} に設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['status']}] [内容]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['banner'].split(','):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_banner,args[1],args[2],client.user.party.me.banner[2]))
            await reply(message, f'バナーを {args[1]}, {args[2]}に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'バナー情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['banner']}] [バナーID] [バナーの色]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['level'].split(','):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_banner,client.user.party.me.banner[0],client.user.party.me.banner[1],int(args[1])))
            await reply(message, f'レベルを {args[1]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'レベルの設定リクエストを処理中にエラーが発生しました')
        except ValueError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, '数字を入力してください')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['level']}] [レベル]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['bp'].split(','):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_battlepass_info,True,args[1],args[2],args[3]))
            await reply(message, f'バトルパス情報を ティア: {args[1]} XPブースト: {args[2]} フレンドXPブースト: {args[3]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'バトルパス情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['bp']}] [ティア] [XPブースト] [フレンドXPブースト]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['privacy'].split(','):
        try:
            if args[1] in commands['privacy_public'].split(','):
                await client.user.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)
                await reply(message, 'プライバシーを パブリック に設定')
            elif args[1] in commands['privacy_friends_allow_friends_of_friends'].split(','):
                await client.user.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS_ALLOW_FRIENDS_OF_FRIENDS)
                await reply(message, 'プライバシーを フレンド(フレンドのフレンドを許可) に設定')
            elif args[1] in commands['privacy_friends'].split(','):
                await client.user.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS)
                await reply(message, 'プライバシーを フレンド に設定')
            elif args[1] in commands['privacy_private_allow_friends_of_friends'].split(','):
                await client.user.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE_ALLOW_FRIENDS_OF_FRIENDS)
                await reply(message, 'プライバシーを プライベート(フレンドのフレンドを許可) に設定')
            elif args[1] in commands['privacy_private'].split(','):
                await client.user.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE)
                await reply(message, 'プライバシーを プライベート に設定')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーリーダーではありません')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['privacy']}] [[{commands['privacy_public']}] / [{commands['privacy_friends_allow_friends_of_friends']}] / [{commands['privacy_friends']}] / [{commands['privacy_private_allow_friends_of_friends']}] / [{commands['privacy_private']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー') 

    elif args[0] in commands['getuser'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['getuser']}] [ユーザー名 / ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            text = str()
            for user in users.values():
                text += f'\n{str(user.display_name)} / {user.id}'
            if data['no-logs'] is False:
                print(text)
            dstore(name,text)
            await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['getfriend'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['getfriend']}] [ユーザー名 / ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.has_friend(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.has_friend(user.id) is True:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            text = str()
            for user in users.values():
                friend=client.get_friend(user.id)
                if friend is None:
                    continue
                if friend.nickname is None:
                    text += f'\n{str(friend.display_name)} / {friend.id}'
                else:
                    text += f'\n{friend.nickname}({str(friend.display_name)}) / {friend.id}'
                if friend.last_logout is not None:
                    text += '\n最後のログイン: {0.year}年{0.month}月{0.day}日 {0.hour}時{0.minute}分{0.second}秒'.format(friend.last_logout)
            if data['no-logs'] is False:
                print(text)
            dstore(name,text)
            await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['getpending'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['getpending']}] [ユーザー名 / ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.is_pending(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.is_pending(user.id) is True:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            text = str()
            for user in users.values():
                pending = client.get_pending_friend(user.id)
                if pending is None:
                    continue
                text += f'\n{str(pending.display_name)} / {pending.id}'
            if data['no-logs'] is False:
                print(text)
            dstore(name,text)
            await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['getblock'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['getblock']}] [ユーザー名 / ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.is_blocked(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.is_blocked(user.id) is True:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            text = str()
            for user in users.values():
                block=client.get_blocked_user(user.id)
                if block is None:
                    continue
                text += f'\n{str(block.display_name)} / {block.id}'
            if data['no-logs'] is False:
                print(text)
            dstore(name,text)
            await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['info'].split(','):
        try:
            if args[1] in commands['info_party'].split(','):
                text = str()
                text += f'{client.user.party.id}\n人数: {client.user.party.member_count}'
                for member in client.user.party.members.values():
                    add_cache(client, member)
                    if data['loglevel'] == 'normal':
                        text += f'\n{str(member.display_name)}'
                    else:
                        text += f'\n{str(member.display_name)} / {member.id}'
                print(text)
                dstore(None, text)
                await reply(message, text)
                if data['loglevel'] == 'debug':
                    print(json.dumps(client.user.party.meta.schema, indent=2))
            
            elif True in [args[1] in commands[key].split(',') for key in ("cid", "bid", "petcarrier", "pickaxe_id", "eid", "emoji_id", "toy_id", "shout_id", "id")]:
                type_ = convert_to_type(args[1])
                if rawcontent2 == '':
                    await reply(message, f"[{commands[type_]}] [ID]")
                    return
                result = await loop.run_in_executor(None, search_item, "ja", "id", rawcontent2, type_)
                if result is None:
                    result = await loop.run_in_executor(None, search_item, "en", "id", rawcontent2, type_)
                if result is None:
                    await reply(message, "見つかりません")
                else:
                    if len(result) > 30:
                        await reply(message, f"見つかったアイテム数 {len(result)} は多すぎます")
                        return
                    if len(result) == 1:
                        await reply(message, f"{result[0]['shortDescription']}: {result[0]['name']} | {result[0]['id']}\n説明: {result[0]['description']}\nレア度: {result[0]['displayRarity']}\n{result[0]['set']}")
                    else:
                        text = str()
                        for count, item in enumerate(result):
                            text += f"\n{count+1} {item['shortDescription']}: {item['name']} | {item['id']}"
                        text += "\n数字を入力することでそのアイテムに設定します"
                        await reply(message, text)
                        client.select[message.author.id] = {"exec": [f"await reply(message, f'''{item['shortDescription']}: {item['name']} | {item['id']}\n{item['description']}\n{item['displayRarity']}\n{item['set']}''')" for item in result]}

            elif True in  [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe", "emote", "emoji", "toy", "shout", "item")]:
                type_ = convert_to_type(args[1])
                if rawcontent2 == '':
                    await reply(message, f"[{commands[type_]}] [アイテム名]")
                    return
                result = await loop.run_in_executor(None, search_item, "ja", "name", rawcontent2, type_)
                if result is None:
                    result = await loop.run_in_executor(None, search_item, "en", "name", rawcontent2, type_)
                if result is None:
                    await reply(message, "見つかりません")
                else:
                    if len(result) > 30:
                        await reply(message, f"見つかったアイテム数 {len(result)} は多すぎます")
                        return
                    if len(result) == 1:
                        await reply(message, f"{result[0]['shortDescription']}: {result[0]['name']} | {result[0]['id']}\n{result[0]['description']}\n{result[0]['displayRarity']}\n{result[0]['set']}")
                    else:
                        text = str()
                        for count, item in enumerate(result):
                            text += f"\n{count+1} {item['shortDescription']}: {item['name']} | {item['id']}"
                        text += "\n数字を入力することでそのアイテムに設定します"
                        await reply(message, text)
                        client.select[message.author.id] = {"exec": [f"await reply(message, f'''{item['shortDescription']}: {item['name']} | {item['id']}\n{item['description']}\n{item['displayRarity']}\n{item['set']}''')" for item in result]}
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['info']}] [[{commands['info_party']}] / [{commands['info_item']}] / [{commands['id']}] / [{commands['skin']}] / [{commands['bag']}] / [{commands['pickaxe']}] / [{commands['emote']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['pending'].split(','):
        try:
            pendings=[]
            for pending in client.pending_friends.values():
                add_cache(client, pending)
                if pending.direction == 'INBOUND':
                    pendings.append(pending)
            if args[1] in commands['true'].split(','):
                for pending in pendings:
                    try:
                        await pending.accept()
                        if data['loglevel'] == 'normal':
                            await reply(message, f'{str(pending.display_name)} をフレンドに追加')
                        else:
                            await reply(message, f'{str(pending.display_name)} / {pending.id} をフレンドに追加')
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                        if data['loglevel'] == 'normal':
                            await reply(message, f'{str(pending.dispaly_name)} のフレンド申請の承認リクエストを処理中にエラーが発生しました')
                        else:
                            await reply(message, f'{str(pending.display_name)} / {pending.id} のフレンド申請の承認リクエストを処理中にエラーが発生しました')
                        continue
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                        await reply(message, 'エラー')
                        continue
            elif args[1] in commands['false'].split(','):
                for pending in pendings:
                    try:
                        await pending.decline()
                        if data['loglevel'] == 'normal':
                            await reply(message, f'{str(pending.display_name)} のフレンド申請を拒否')
                        else:
                            await reply(message, f'{str(pending.display_name)} / {pending.id} のフレンド申請を拒否')
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(name,f'>>> {traceback.format_exc()}')
                        if data['loglevel'] == 'normal':
                            await reply(message, f'{str(pending.display_name)} のフレンド申請の拒否リクエストを処理中にエラーが発生しました')
                        else:
                            await reply(message, f'{str(pending.display_name)} / {pending.id} のフレンド申請の拒否リクエストを処理中にエラーが発生しました')
                        continue
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                        await reply(message, 'エラー')
                        continue
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['pending']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['removepending'].split(','):
        try:
            pendings=[]
            for pending in client.pending_friends.values():
                add_cache(client, pending)
                if pending.direction == 'OUTBOUND':
                    pendings.append(pending)
            for pending in pendings:
                try:
                    await pending.decline()
                    if data['loglevel'] == 'normal':
                        await reply(message, f'{str(pending.display_name)} へのフレンド申請を解除')
                    else:
                        await reply(message, f'{str(pending.display_name)} / {pending.id} へのフレンド申請を解除')
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    if data['loglevel'] == 'normal':
                        await reply(message, f'{str(pending.display_name)} へのフレンド申請を解除リクエストを処理中にエラーが発生しました')
                    else:
                        await reply(message, f'{str(pending.display_name)} / {pending.id} へのフレンド申請を解除リクエストを処理中にエラーが発生しました')
                    continue
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'エラー')
                    continue
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['addfriend'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['addfriend']}] [ユーザー名 / ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.has_friend(user.id) is False}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.has_friend(user.id) is False:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.has_friend(user.id) is True:
                    await reply(message, '既にユーザーとフレンドです')
                    return
                await client.add_friend(user.id)
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(user.display_name)} にフレンド申請を送信')
                else:
                    await reply(message, f'{str(user.display_name)} / {user.id} にフレンド申請を送信')
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.has_friend(user.id) is True:
                await reply(message, '既にユーザーとフレンドです')
                return
            await client.add_friend(user.id)
            if data['loglevel'] == 'normal':
                await reply(message, f'{str(user.display_name)} にフレンド申請を送信')
            else:
                await reply(message, f'{str(user.display_name)} / {user.id} にフレンド申請を送信')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'フレンド申請の送信リクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーにフレンド申請を送信します"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'フレンド申請の送信リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['removefriend'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['removefriend']}] [ユーザー名 / ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.has_friend(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.has_friend(user.id) is True:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.has_friend(user.id) is False:
                    await reply(message, 'ユーザーとフレンドではありません')
                    return
                await client.remove_or_decline_friend(user.id)
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(user.display_name)} をフレンドから削除')
                else:
                    await reply(message, f'{str(user.display_name)} / {user.id} をフレンドから削除')
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.has_friend(user.id) is False:
                await reply(message, 'ユーザーとフレンドではありません')
                return
            await client.remove_or_decline_friend(user.id)
            if data['loglevel'] == 'normal':
                await reply(message, f'{str(user.display_name)} をフレンドから削除')
            else:
                await reply(message, f'{str(user.display_name)} / {user.id} をフレンドから削除')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'フレンドの削除リクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーをフレンドから削除します"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'フレンドの削除リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['acceptpending'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['acceptpending']}] [ユーザー名 / ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.is_pending(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.is_pending(user.id) is True:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.is_pending(user.id) is False:
                    await reply(message, 'ユーザーからのフレンド申請がありません')
                    return
                await client.accept_friend(user.id)
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(user.display_name)} をフレンドに追加')
                else:
                    await reply(message, f'{str(user.display_name)} / {user.id} をフレンドに追加')
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.is_pending(user.id) is False:
                await reply(message, 'ユーザーからのフレンド申請がありません')
                return
            await client.accept_friend(user.id)
            if data['loglevel'] == 'normal':
                await reply(message, f'{str(user.display_name)} をフレンドに追加')
            else:
                await reply(message, f'{str(user.display_name)} / {user.id} をフレンドに追加')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'フレンドの追加リクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーからのフレンド申請を承諾します"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'フレンドの追加リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['declinepending'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['declinepending']}] [ユーザー名 / ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.is_pending(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.is_pending(user.id) is True:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.is_pending(user.id) is False:
                    await reply(message, 'ユーザーからのフレンド申請がありません')
                    return
                await client.remove_or_decline_friend(user.id)
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(user.display_name)} のフレンド申請を拒否')
                else:
                    await reply(message, f'{str(user.display_name)} / {user.id} のフレンド申請を拒否')
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.is_pending(user.id) is False:
                await reply(message, 'ユーザーからのフレンド申請がありません')
                return
            await client.remove_or_decline_friend(user.id)
            if data['loglevel'] == 'normal':
                await reply(message, f'{str(user.display_name)} のフレンド申請を拒否')
            else:
                await reply(message, f'{str(user.display_name)} / {user.id} のフレンド申請を拒否')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'フレンド申請の拒否リクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーからのフレンド申請を拒否します"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'フレンド申請の拒否リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['blockfriend'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['blockfriend']}] [ユーザー名 / ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.is_blocked(user.id) is False}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.is_blocked(user.id) is False:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.is_blocked(user.id) is True:
                    await reply(message, '既にユーザーをブロックしています')
                    return
                await client.block_user(user.id)
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(user.display_name)} をブロック')
                else:
                    await reply(message, f'{str(user.display_name)} / {user.id} をブロック')
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.is_blocked(user.id) is True:
                await reply(message, '既にユーザーをブロックしています')
                return
            await client.block_user(user.id)
            if data['loglevel'] == 'normal':
                await reply(message, f'{str(user.display_name)} をブロック')
            else:
                await reply(message, f'{str(user.display_name)} / {user.id} をブロック')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'フレンドのブロックリクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーをブロックします"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'フレンドのブロックリクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['unblockfriend'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['unblockfriend']}] [ユーザー名 / ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.is_blocked(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.is_blocked(user.id) is True:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.is_blocked(user.id) is False:
                    await reply(message, 'ユーザーをブロックしていません')
                    return
                await client.unblock_user(user.id)
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(user.display_name)} をブロック解除')
                else:
                    await reply(message, f'{str(user.display_name)} / {user.id} をブロック解除')
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.is_blocked(user.id) is False:
                await reply(message, 'ユーザーをブロックしていません')
                return
            await client.unblock_user(user.id)
            if data['loglevel'] == 'normal':
                await reply(message, f'{str(user.display_name)} をブロック解除')
            else:
                await reply(message, f'{str(user.display_name)} / {user.id} をブロック解除')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'ブロックしたユーザーのブロック解除リクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーをブロック解除します"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'ブロックしたユーザーのブロック解除リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['chatban'].split(','):
        try:
            reason=rawcontent.split(' : ')
            if rawcontent == '':
                await reply(message, f"[{commands['chatban']}] [ユーザー名 / ユーザーID] : [理由(任意)]")
                return
            users = {member.display_name: member for member in client.user.party.members.values() if rawcontent.lower() in member.display_name.lower() and member.display_name is not None}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.user.party.members.get(user.id) is not None:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.user.party.members.get(user.id) is None:
                    await reply(message, 'ユーザーがパーティーにいません')
                    return
                member=client.user.party.members.get(user.id)
                try:
                    await member.chatban(reason[1])
                except IndexError:
                    await member.chatban()
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(user.display_name)} をバン')
                else:
                    await reply(message, f'{str(user.display_name)} / {user.id} をバン')
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.user.party.members.get(user.id) is None:
                await reply(message, 'ユーザーがパーティーにいません')
                return
            member=client.user.party.members.get(user.id)
            try:
                await member.chatban(reason[1])
            except IndexError:
                await member.chatban()
            if data['loglevel'] == 'normal':
                await reply(message, f'{str(user.display_name)} をバン')
            else:
                await reply(message, f'{str(user.display_name)} / {user.id} をバン')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーリーダーではありません')
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'メンバーが見つかりません')
        except ValueError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, '既にバンされています')""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user, "reason": reason} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーをバンします"
                await reply(message, text)
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーリーダーではありません')
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'メンバーが見つかりません')
        except ValueError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, '既にバンされています')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['promote'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['promote']}] [ユーザー名 / ユーザーID]")
                return
            users = {member.display_name: member for member in client.user.party.members.values() if rawcontent.lower() in member.display_name.lower() and member.display_name is not None}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.user.party.members.get(user.id) is not None:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.user.party.members.get(user.id) is None:
                    await reply(message, 'ユーザーがパーティーにいません')
                    return
                member=client.user.party.members.get(user.id)
                await member.promote()
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(user.display_name)} に譲渡')
                else:
                    await reply(message, f'{str(user.display_name)} / {user.id} に譲渡')
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.user.party.members.get(user.id) is None:
                await reply(message, 'ユーザーがパーティーにいません')
                return
            member=client.user.party.members.get(user.id)
            await member.promote()
            if data['loglevel'] == 'normal':
                await reply(message, f'{str(user.display_name)} に譲渡')
            else:
                await reply(message, f'{str(user.display_name)} / {user.id} に譲渡')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーリーダーではありません')
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, '既にパーティーリーダーです')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーリーダーの譲渡リクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーに譲渡します"
                await reply(message, text)
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーリーダーではありません')
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, '既にパーティーリーダーです')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーリーダーの譲渡リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['kick'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['kick']}] [ユーザー名 / ユーザーID]")
                return
            users = {member.display_name: member for member in client.user.party.members.values() if rawcontent.lower() in member.display_name.lower() and member.display_name is not None}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.user.party.members.get(user.id) is not None:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.user.party.members.get(user.id) is None:
                    await reply(message, 'ユーザーがパーティーにいません')
                    return
                member=client.user.party.members.get(user.id)
                await member.kick()
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(user.display_name)} をキック')
                else:
                    await reply(message, f'{str(user.display_name)} / {user.id} をキック')
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.user.party.members.get(user.id) is None:
                await reply(message, 'ユーザーがパーティーにいません')
                return
            member=client.user.party.members.get(user.id)
            await member.kick()
            if data['loglevel'] == 'normal':
                await reply(message, f'{str(user.display_name)} をキック')
            else:
                await reply(message, f'{str(user.display_name)} / {user.id} をキック')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーリーダーではありません')
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, '自分をキックすることはできません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーメンバーのキックリクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーをキックします"
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーリーダーではありません')
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, '自分をキックすることはできません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーメンバーのキックリクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['ready'].split(','):
        try:
            await client.user.party.me.set_ready(fortnitepy.ReadyState.READY)
            await reply(message, '準備状態を 準備OK に設定')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['unready'].split(','):
        try:
            await client.user.party.me.set_ready(fortnitepy.ReadyState.NOT_READY)
            await reply(message, '準備状態を 準備中 に設定')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['sitout'].split(','):
        try:
            await client.user.party.me.set_ready(fortnitepy.ReadyState.SITTING_OUT)
            await reply(message, '準備状態を 欠場中 に設定')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['outfitlock'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.outfitlock=True
                await reply(message, 'コスチュームロックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.outfitlock=False
                await reply(message, 'コスチュームロックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['outfitlock']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['backpacklock'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.backpacklock=True
                await reply(message, 'バックアクセサリーロックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.backpacklock=False
                await reply(message, 'バックアクセサリーロックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['backpacklock']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['pickaxelock'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.pickaxelock=True
                await reply(message, '収集ツールロックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.pickaxelock=False
                await reply(message, '収集ツールロックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['pickaxelock']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['emotelock'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.emotelock=True
                await reply(message, 'エモートロックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.emotelock=False
                await reply(message, 'エモートロックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['outfitlock']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['stop'].split(','):
        try:
            client.stopcheck=True
            if await change_asset(client, message.author.id, "emote", "") is True:
                await reply(message, '停止しました')
            else:
                await reply(message, 'ロックされています')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['alloutfit'].split(','):
        try:
            flag = False
            if client.outfitlock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, 'ロックされています')
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
            await reply(message, '全てのコスチュームを表示し終わりました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['allbackpack'].split(','):
        try:
            flag = False
            if client.backpacklock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, 'ロックされています')
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allskin = json.load(f)
            for item in allskin['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type'] == 'backpack':
                    if 'banner' not in item['id']:
                        await client.user.party.me.set_backpack(item['id'])
                    else:
                        await client.user.party.me.set_backpack(item['id'],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner'))
                    await asyncio.sleep(2)
            await reply(message, '全てのバックアクセサリーを表示し終わりました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['allpet'].split(','):
        try:
            flag = False
            if client.backpacklock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, 'ロックされています')
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allskin = json.load(f)
            for item in allskin['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type'] == 'pet':
                    if 'banner' not in item['id']:
                        await client.user.party.me.set_backpack(item['id'])
                    else:
                        await client.user.party.me.set_backpack(item['id'],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner'))
                    await asyncio.sleep(2)
            await reply(message, '全てのペットを表示し終わりました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['allpickaxe'].split(','):
        try:
            flag = False
            if client.pickaxelock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, 'ロックされています')
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allskin = json.load(f)
            for item in allskin['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type'] == 'pickaxe':
                    if 'banner' not in item['id']:
                        await client.user.party.me.set_pickaxe(item['id'])
                    else:
                        await client.user.party.me.set_pickaxe(item['id'],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner'))
                    await asyncio.sleep(2)
            await reply(message, '全ての収集ツールを表示し終わりました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['allemote'].split(','):
        try:
            flag = False
            if client.emotelock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, 'ロックされています')
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
                await reply(message, '全てのエモートを表示し終わりました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['allemoji'].split(','):
        try:
            flag = False
            if client.emotelock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, 'ロックされています')
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allemote = json.load(f)
            for item in allemote['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type'] == 'emoji':
                    await client.user.party.me.set_emote(item['id'])
                    await asyncio.sleep(5)
            else:
                await reply(message, '全てのエモートアイコンを表示し終わりました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['alltoy'].split(','):
        try:
            flag = False
            if client.emotelock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, 'ロックされています')
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allemote = json.load(f)
            for item in allemote['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type'] == 'toy':
                    await client.user.party.me.set_emote(item['id'])
                    await asyncio.sleep(5)
            else:
                await reply(message, '全てのおもちゃを表示し終わりました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['allshout'].split(','):
        try:
            flag = False
            if client.emotelock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, 'ロックされています')
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allemote = json.load(f)
            for item in allemote['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type'] == 'shout':
                    await client.user.party.me.set_emote(item['id'])
                    await asyncio.sleep(5)
            else:
                await reply(message, '全てのshoutを表示し終わりました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['setenlightenment'].split(','):
        try:
            if await change_asset(client, message.author.id, "outfit", client.user.party.me.outfit, client.user.party.me.outfit_variants,(args[1],args[2])) is True:
                await reply(message, f'{args[1]}, {args[2]} に設定')
            else:
                await reply(message, 'ロックされています')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['setenlightenment']}] [数値] [数値]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif True in [args[0] in commands[key].split(',') for key in ("cid", "bid", "petcarrier", "pickaxe_id", "eid", "emoji_id", "toy_id", "shout_id", "id")]:
        type_ = convert_to_type(args[0])
        if rawcontent == '':
            await reply(message, f"[{commands[type_]}] [ID]")
            return
        try:
            result = await loop.run_in_executor(None, search_item, "ja", "id", rawcontent, type_)
            if result is None:
                result = await loop.run_in_executor(None, search_item, "en", "id", rawcontent, type_)
            if result is None:
                await reply(message, "見つかりません")
            else:
                if len(result) > 30:
                    await reply(message, f"見つかったアイテム数 {len(result)} は多すぎます")
                    return
                if len(result) == 1:
                    if await change_asset(client, message.author.id, result[0]["type"], result[0]['id']) is True:
                        await reply(message, f"{result[0]['shortDescription']}: {result[0]['name']} | {result[0]['id']}")
                    else:
                        await reply(message, "ロックされています")
                else:
                    text = str()
                    for count, item in enumerate(result):
                        text += f"\n{count+1} {item['shortDescription']}: {item['name']} | {item['id']}"
                    text += "\n数字を入力することでそのアイテムに設定します"
                    await reply(message, text)
                    client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{item['type']}', '{item['id']}')" for item in result]}
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif True in  [args[0] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe", "emote", "emoji", "toy", "shout", "item")]:
        type_ = convert_to_type(args[0])
        if rawcontent == '':
            await reply(message, f"[{commands[type_]}] [アイテム名]")
            return
        try:
            result = await loop.run_in_executor(None, search_item, "ja", "name", rawcontent, type_)
            if result is None:
                result = await loop.run_in_executor(None, search_item, "en", "name", rawcontent, type_)
            if result is None:
                await reply(message, "見つかりません")
            else:
                if len(result) > 30:
                    await reply(message, f"見つかったアイテム数 {len(result)} は多すぎます")
                    return
                if len(result) == 1:
                    if await change_asset(client, message.author.id, result[0]["type"], result[0]['id']) is True:
                        await reply(message, f"{result[0]['shortDescription']}: {result[0]['name']} | {result[0]['id']}")
                    else:
                        await reply(message, "ロックされています")
                else:
                    text = str()
                    for count, item in enumerate(result):
                        text += f"\n{count+1} {item['shortDescription']}: {item['name']} | {item['id']}"
                    text += "\n数字を入力することでそのアイテムに設定します"
                    await reply(message, text)
                    client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{item['type']}', '{item['id']}')" for item in result]}
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['set'].split(','):
        if rawcontent == '':
            await reply(message, f"[{commands['set']}] [セット名]]")
            return
        try:
            result = await loop.run_in_executor(None, search_item, "ja", "set", rawcontent)
            if result is None:
                result = await loop.run_in_executor(None, search_item, "en", "set", rawcontent)
            if result is None:
                await reply(message, "見つかりません")
            else:
                if len(result) > 30:
                    await reply(message, f"見つかったアイテム数 {len(result)} は多すぎます")
                    return
                if len(result) == 1:
                    if await change_asset(client, message.author.id, result[0]["type"], result[0]['id']) is True:
                        await reply(message, f"{result[0]['shortDescription']}: {result[0]['name']} | {result[0]['id']}({result[0]['set']})")
                    else:
                        await reply(message, "ロックされています")
                else:
                    text = str()
                    for count, item in enumerate(result):
                        text += f"\n{count+1} {item['shortDescription']}: {item['name']} | {item['id']}({result[0]['set']})"
                    text += "\n数字を入力することでそのアイテムに設定します"
                    await reply(message, text)
                    client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{item['type']}', '{item['id']}')" for item in result]}
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['setstyle'].split(','):
        try:
            if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe")]:
                await reply(message, f"[{commands['setstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                return
            type_ = convert_to_type(args[1])
            id_ = member_asset(client.user.party.me, convert_to_asset(args[1]))
            result = search_style("ja", id_)
            if result is None:
                await reply(message, "スタイル変更はありません")
            else:
                text = str()
                for count, item in enumerate(result):
                    text += f"\n{count+1} {item['name']}"
                text += "\n数字を入力することでそのアイテムに設定します"
                await reply(message, text)
                client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{type_}', '{id_}', {variants['variants']})" for variants in result]}
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['setstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['addstyle'].split(','):
        try:
            if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe")]:
                await reply(message, f"[{commands['addstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                return
            type_ = convert_to_type(args[1])
            id_ = member_asset(client.user.party.me, convert_to_asset(args[1]))
            variants_ = eval(f"client.user.party.me.{convert_to_asset(args[1])}_variants")
            result = search_style("ja", id_)
            if result is None:
                await reply(message, "スタイル変更はありません")
            else:
                text = str()
                for count, item in enumerate(result):
                    text += f"\n{count+1} {item['name']}"
                text += "\n数字を入力することでそのアイテムに設定します"
                await reply(message, text)
                client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{type_}', '{id_}', {variants_} + {variants['variants']})" for variants in result]}
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['addstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['setvariant'].split(','):
        try:
            if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe")]:
                await reply(message, f"[{commands['setvariant']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                return
            variantdict={}
            for count,text in enumerate(args[2:]):
                if count % 2 != 0:
                    continue
                try:
                    variantdict[text]=args[count+3]
                except IndexError:
                    break
            type_ = convert_to_type(args[1])
            id_ = member_asset(client.user.party.me, convert_to_asset(args[1]))
            variants = client.user.party.me.create_variants(item='AthenaCharacter',**variantdict)
            if await change_asset(client, message.author.id, type_, id_, variants, client.user.party.me.enlightenment) is False:
                await reply(message, "ロックされています")
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['setvariant']}] [ID] [variant] [数値]\nvariantと数値は無限に設定可能")
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['addvariant'].split(','):
        try:
            if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe")]:
                await reply(message, f"[{commands['addvariant']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                return
            variantdict={}
            for count,text in enumerate(args[2:]):
                if count % 2 != 0:
                    continue
                try:
                    variantdict[text]=args[count+3]
                except IndexError:
                    break
            type_ = convert_to_type(args[1])
            id_ = member_asset(client.user.party.me, convert_to_asset(args[1]))
            variants = client.user.party.me.create_variants(item='AthenaCharacter',**variantdict)
            variants += eval(f"client.user.party.me.{convert_to_asset(args[1])}_variants")
            if await change_asset(client, message.author.id, type_, id_, variants, client.user.party.me.enlightenment) is False:
                await reply(message, "ロックされています")
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['addvariant']}] [ID] [variant] [数値]\nvariantと数値は無限に設定可能")
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif True in [args[0] in commands[key].split(',') for key in ("outfitasset", "backpackasset", "pickaxeasset", "emoteasset")]:
        type_ = convert_to_type(args[0])
        try:
            if rawcontent == '':
                await reply(message, f"[{commands[f'{type_}asset']}] [アセットパス]")
                return
            if await change_asset(client, message.author.id, type_, rawcontent) is False:
                await reply(message, "ロックされています")
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif True in [args[0].lower().startswith(id_) for id_ in ("cid_", "bid_", "petcarrier_", "pickaxe_id_", "eid_", "emoji_", "toy_", "shout_")]:
        try:
            type_ = convert_to_type("_".join(args[0].split('_')[:-1]) + "_")
            if await change_asset(client, message.author.id, type_, args[0]) is False:
                await reply(message, "ロックされています")
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0].lower().startswith('playlist_'):
        try:
            await client.user.party.set_playlist(args[0])
            await reply(message, f'プレイリストを {args[0]} に設定')
            data['fortnite']['playlist']=args[0]
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーリーダーではありません')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    else:
        if ': ' in message.content:
            return
        if args[0].isdigit() and client.select.get(message.author.id) is not None:
            try:
                if int(args[0]) == 0:
                    await reply(message, '有効な数字を入力してください')
                    return
                exec_ = client.select[message.author.id]["exec"][int(args[0])-1]
                variable=globals()
                variable.update(locals())
                if client.select[message.author.id].get("variable") is not None:
                    variable.update(client.select[message.author.id]["variable"][int(args[0])-1])
                await aexec(exec_, variable)
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, '有効な数字を入力してください')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')
        else:
            result = await loop.run_in_executor(None, search_item, "ja", "name", content, "item")
            if result is None:
                result = await loop.run_in_executor(None, search_item, "en", "name", content, "item")
            if result is not None:
                if len(result) > 30:
                    await reply(message, f"見つかったアイテム数 {len(result)} は多すぎます")
                    return
                if len(result) == 1:
                    if await change_asset(client, message.author.id, result[0]["type"], result[0]['id']) is True:
                        await reply(message, f"{result[0]['shortDescription']}: {result[0]['name']} | {result[0]['id']}")
                    else:
                        await reply(message, "ロックされています")
                else:
                    text = str()
                    for count, item in enumerate(result):
                        text += f"\n{count+1} {item['shortDescription']}: {item['name']} | {item['id']}"
                    text += "\n数字を入力することでそのアイテムに設定します"
                    await reply(message, text)
                    client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{item['type']}', '{item['id']}')" for item in result]}

#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================

async def event_party_message(message):
    global blacklist
    global whitelist
    global blacklist_
    global whitelist_
    global kill
    if message is None:
        return
    client=message.client
    if data['discord']['enabled'] is True and dclient.isready is False:
        return
    if client.isready is False:
        return
    name=client.user.display_name
    author_id = message.author.id
    loop = asyncio.get_event_loop()
    add_cache(client, message.author)
    if message.author.id in blacklist and data['fortnite']['blacklist-ignorecommand'] is True:
        return
    if not client.owner is None:
        if client.partychat is False:
            if client.partychatperfect is True:
                return
            elif not message.author.id == client.owner.id:
                return
    else:
        if client.partychat is False:
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
    client_user_display_name=name
    member_joined_at_most=[client.user.id, client.user.party.me.joined_at]
    for member_ in client.user.party.members.values():
        add_cache(client, member_)
        try:
            if member_joined_at_most != []:
                if member_.id in [i.user.id for i in clients]:
                    if member_.id != client.user.id:
                        client_user_display_name+=f"/{str(member_.display_name)}"
                    if member_.joined_at < member_joined_at_most[1]:
                        member_joined_at_most=[member_.id, member_.joined_at]
            else:
                member_joined_at_most=[client.user.id, client.user.party.me.joined_at]
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    if client.user.id == member_joined_at_most[0]:
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(f'[{now_()}] [パーティー] [{client_user_display_name}] {message.author.display_name} | {content}')
            dstore(message.author.display_name,f'[{client_user_display_name}] [パーティー] {content}')
        else:
            if data['no-logs'] is False:
                print(f'[{now_()}] [パーティー/{client.user.party.id}] [{client_user_display_name}] {message.author.display_name} / {message.author.id} [{platform_to_str(message.author.platform)}/{message.author.input}] | {content}')
            dstore(f'{message.author.display_name} / {message.author.id} [{platform_to_str(message.author.platform)}/{message.author.input}]',f'[{client_user_display_name}] [パーティー/{client.user.party.id}] {content}')

    flag = False
    if isinstance(message, fortnitepy.message.MessageBase) is True:
        if client.owner is not None:
            if data['fortnite']['whitelist-ownercommand'] is True:
                if client.owner.id != message.author.id and message.author.id not in whitelist:
                    flag = True
            else:
                if client.owner.id != message.author.id:
                    flag = True
        else:
            if data['fortnite']['whitelist-ownercommand'] is True:
                if message.author.id not in whitelist:
                    flag = True
            else:
                flag = True
    else:
        if dclient.owner is not None:
            if data['discord']['whitelist-ownercommand'] is True:
                if client.owner.id != message.author.id and message.author.id not in whitelist_:
                    flag = True
            else:
                if client.owner.id != message.author.id:
                    flag = True
        else:
            if data['discord']['whitelist-ownercommand'] is True:
                if message.author.id not in whitelist_:
                    flag = True
            else:
                flag = True
    if flag is True:
        for checks in commands.items():
            ignore=['ownercommands','true','false','me', 'privacy_public', 'privacy_friends_allow_friends_of_friends', 'privacy_friends', 'privacy_private_allow_friends_of_friends', 'privacy_private', 'info_party', 'info_item']
            if checks[0] in ignore:
                continue
            if commands['ownercommands'] == '':
                break
            for command in commands['ownercommands'].split(','):
                if args[0] in commands[command.lower()].split(','):
                    await reply(message, 'このコマンドは管理者しか使用できません')
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
        if args[0] in key.split(','):
            try:
                await reply(message, value)
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')
            return

    if data['discord']['enabled'] is True and dclient.isready is True:
        if args[0] in commands['addblacklist_discord'].split(','):
            try:
                if rawcontent == '' or args[1].isdigit() is False:
                    await reply(message, f"[{commands['addblacklist_discord']}] [ユーザーID]")
                    return
                user = dclient.get_user(int(args[1]))
                if user is None:
                    user = await dclient.fetch_user(int(args[1]))
                if user.id not in blacklist_:
                    blacklist_.append(user.id)
                    data["discord"]["blacklist"].append(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["discord"]["blacklist"] = data["discord"]["blacklist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, f"ユーザー {user} / {user.id} をブラックリストに追加しました")
                else:
                    await reply(message, f"ユーザー {user} / {user.id} は既にブラックリストに追加されています")
            except discord.NotFound:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザーが見つかりません')
            except discord.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
                dstore(name,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました。')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['removeblacklist_discord'].split(','):
            try:
                if rawcontent == '' or args[1].isdigit() is False:
                    await reply(message, f"[{commands['removeblacklist_discord']}] [ユーザーID]")
                    return
                user = dclient.get_user(int(args[1]))
                if user is None:
                    user = await dclient.fetch_user(int(args[1]))
                if user.id in blacklist_:
                    blacklist_.remove(user.id)
                    data["discord"]["blacklist"].remove(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["discord"]["blacklist"] = data["discord"]["blacklist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, f"ユーザー {user} / {user.id} をブラックリストから削除")
                else:
                    await reply(message, f"ユーザー {user} / {user.id} はブラックリストに含まれていません")
            except discord.NotFound:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザーが見つかりません')
            except discord.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
                dstore(name,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました。')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['addwhitelist_discord'].split(','):
            try:
                if rawcontent == '' or args[1].isdigit() is False:
                    await reply(message, f"[{commands['addwhitelist_discord']}] [ユーザーID]")
                    return
                user = dclient.get_user(int(args[1]))
                if user is None:
                    user = await dclient.fetch_user(int(args[1]))
                if user.id not in whitelist_:
                    whitelist_.append(user.id)
                    data["discord"]["whitelist"].append(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["discord"]["whitelist"] = data["discord"]["whitelist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, f"ユーザー {user} / {user.id} をホワイトリストに追加しました")
                else:
                    await reply(message, f"ユーザー {user} / {user.id} は既にホワイトリストに追加されています")
            except discord.NotFound:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザーが見つかりません')
            except discord.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
                dstore(name,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました。')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['removewhitelist_discord'].split(','):
            try:
                if rawcontent == '' or args[1].isdigit() is False:
                    await reply(message, f"[{commands['removewhitelist_discord']}] [ユーザーID]")
                    return
                user = dclient.get_user(int(args[1]))
                if user is None:
                    user = await dclient.fetch_user(int(args[1]))
                if user.id in whitelist_:
                    whitelist_.remove(user.id)
                    data["discord"]["whitelist"].remove(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["discord"]["whitelist"] = data["discord"]["whitelist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, f"ユーザー {user} / {user.id} をホワイトリストから削除")
                else:
                    await reply(message, f"ユーザー {user} / {user.id} はホワイトリストに含まれていません")
            except discord.NotFound:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザーが見つかりません')
            except discord.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
                dstore(name,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました。')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

    if args[0] in commands['eval'].split(','):
        try:
            if rawcontent == "":
                await reply(message, f"[{commands['eval']}] [式]")
                return
            variable=globals()
            variable.update(locals())
            if rawcontent.startswith("await "):
                if data['loglevel'] == "debug":
                    print(f"await eval({rawcontent.replace('await ','',1)})")
                result = await eval(rawcontent.replace("await ","",1), variable)
                await reply(message, str(result))
            else:
                if data['loglevel'] == "debug":
                    print(f"eval {rawcontent}")
                result = eval(rawcontent, variable)
                await reply(message, str(result))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['exec'].split(','):
        try:
            if rawcontent == "":
                await reply(message, f"[{commands['exec']}] [文]")
                return
            variable=globals()
            variable.update(locals())
            args_=[i.replace("\\nn", "\n") for i in content.replace("\n", "\\nn").split()]
            content_=" ".join(args_[1:])
            result = await aexec(content_, variable)
            await reply(message, str(result))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['restart'].split(','):
        try:
            flag = False
            if client.acceptinvite is False:
                if isinstance(message, fortnitepy.message.MessageBase) is True:
                    if client.owner is not None:
                        if data['fortnite']['whitelist-ownercommand'] is True:
                            if client.owner.id != message.author.id and message.author.id not in whitelist:
                                flag = True
                        else:
                            if client.owner.id != message.author.id:
                                flag = True
                    else:
                        if data['fortnite']['whitelist-ownercommand'] is True:
                            if message.author.id not in whitelist:
                                flag = True
                        else:
                            flag = True
                elif isinstance(message, discord.Message) is True:
                    if dclient.owner is not None:
                        if data['discord']['whitelist-ownercommand'] is True:
                            if dclient.owner.id != message.author.id and message.author.id not in whitelist_:
                                flag = True
                        else:
                            if dclient.owner.id != message.author.id:
                                flag = True
                    else:
                        if data['discord']['whitelist-ownercommand'] is True:
                            if message.author.id not in whitelist_:
                                flag = True
                        else:
                            flag = True
            if flag is True:
                await reply(message, '招待が拒否に設定されているので実行できません')
                return
            await reply(message, 'プログラムを再起動します...')
            os.chdir(os.getcwd())
            os.execv(os.sys.executable,['python','index.py'])
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['relogin'].split(','):
        try:
            flag = False
            if client.acceptinvite is False:
                if isinstance(message, fortnitepy.message.MessageBase) is True:
                    if client.owner is not None:
                        if data['fortnite']['whitelist-ownercommand'] is True:
                            if client.owner.id != message.author.id and message.author.id not in whitelist:
                                flag = True
                        else:
                            if client.owner.id != message.author.id:
                                flag = True
                    else:
                        if data['fortnite']['whitelist-ownercommand'] is True:
                            if message.author.id not in whitelist:
                                flag = True
                        else:
                            flag = True
                elif isinstance(message, discord.Message) is True:
                    if dclient.owner is not None:
                        if data['discord']['whitelist-ownercommand'] is True:
                            if dclient.owner.id != message.author.id and message.author.id not in whitelist_:
                                flag = True
                        else:
                            if dclient.owner.id != message.author.id:
                                flag = True
                    else:
                        if data['discord']['whitelist-ownercommand'] is True:
                            if message.author.id not in whitelist_:
                                flag = True
                        else:
                            flag = True
            if flag is True:
                await reply(message, '招待が拒否に設定されているので実行できません')
                return
            await reply(message, 'アカウントに再ログインします...')
            await client.restart()
        except fortnitepy.AuthException:
            print(red(traceback.format_exc()))
            print(red(f'[{now_()}] [{client.user.display_name}] メールアドレスまたはパスワードが間違っています。'))
            dstore(name,f'>>> {traceback.format_exc()}')
            dstore(name,f'>>> メールアドレスまたはパスワードが間違っています')
            kill=True
            exit()
        except Exception:
            print(red(traceback.format_exc()))
            print(red(f'[{now_()}] [{client.user.display_name}] アカウントの読み込みに失敗しました。もう一度試してみてください。'))
            dstore(name,f'>>> {traceback.format_exc()}')
            dstore(name,f'>>> アカウントの読み込みに失敗しました。もう一度試してみてください')
            kill=True
            exit()

    elif args[0] in commands['reload'].split(','):
        result=reload_configs(client)
        try:
            if result == 'Success':
                await reply(message, '正常に読み込みが完了しました')
            else:
                await reply(message, 'エラー')
                return
            try:
                client.owner=None
                owner=await client.fetch_profile(data['fortnite']['owner'])
                if owner is None:
                    print(red(f'[{now_()}] [{client.user.display_name}] 所有者が見つかりません。正しい名前/IDになっているか確認してください。'))
                    dstore(client.user.display_name,'>>> 所有者が見つかりません。正しい名前/IDになっているか確認してください')
                else:
                    add_cache(client, owner)
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

            for blacklistuser in data['fortnite']['blacklist']:
                try:
                    user = await client.fetch_profile(blacklistuser)
                    add_cache(client, user)
                    if user is None:
                        print(red(f'[{now_()}] [{client.user.display_name}] ブラックリストのユーザー {blacklistuser} が見つかりません。正しい名前/IDになっているか確認してください。'))
                        dstore(client.user.display_name,f'>>>ブラックリストのユーザー {blacklistuser} が見つかりません。正しい名前/IDになっているか確認してください')
                    else:
                        blacklist.append(user.id)
                        if data['loglevel'] == 'debug':
                            print(yellow(f"{str(user.display_name)} / {user.id}"))
                        if data['fortnite']['blacklist-autoblock'] is True:
                            try:
                                await user.block()
                            except Exception:
                                if data['loglevel'] == 'debug':
                                    print(red(traceback.format_exc()))
                                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                    print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
                    dstore(client.user.display_name,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            if data['loglevel'] == "debug":
                print(yellow(blacklist))
            for whitelistuser in data['fortnite']['whitelist']:
                try:
                    user = await client.fetch_profile(whitelistuser)
                    add_cache(client, user)
                    if user is None:
                        print(red(f'[{now_()}] [{client.user.display_name}] ホワイトリストのユーザー {whitelistuser} が見つかりません。正しい名前/IDになっているか確認してください。'))
                        dstore(client.user.display_name,f'>>>ホワイトリストのユーザー {whitelistuser} が見つかりません。正しい名前/IDになっているか確認してください')
                    else:
                        whitelist.append(user.id)
                        if data['loglevel'] == 'debug':
                            print(yellow(f"{str(user.display_name)} / {user.id}"))
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                    print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
                    dstore(client.user.display_name,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            if data['loglevel'] == "debug":
                print(yellow(whitelist))

            for invitelistuser in data['fortnite']['invitelist']:
                try:
                    user = await client.fetch_profile(invitelistuser)
                    if user is None:
                        print(red(f'[{now_()}] [{client.user.display_name}] 招待リストのユーザー {invitelistuser} が見つかりません。正しい名前/IDになっているか確認してください。'))
                        dstore(client.user.display_name,f'>>>招待リストのユーザー {invitelistuser} が見つかりません。正しい名前/IDになっているか確認してください')
                    else:
                        friend = client.get_friend(user.id)
                        if friend is None and user.id != client.user.id:
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
                            print(red(f"[{now_()}] [{client.user.display_name}] 招待リストのユーザー {invitelistuser} とフレンドではありません。フレンドになってからもう一度起動するか、[{commands['reload']}] コマンドで再読み込みしてください。"))
                            dstore(client.user.display_name,f'>>> 招待リストのユーザー {invitelistuser} とフレンドではありません。フレンドになってからもう一度起動するか、[{commands["reload"]}] コマンドで再読み込みしてください')
                        else:
                            add_cache(client, user)
                            client.invitelist.append(user.id)
                            if data['loglevel'] == 'debug':
                                print(yellow(f"{str(user.display_name)} / {user.id}"))
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                    print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
                    dstore(client.user.display_name,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            if data['loglevel'] == "debug":
                print(yellow(client.invitelist))
            if data['discord']['enabled'] is True:
                dclient_user = str(dclient.user)
                activity = discord.Game(name=data['discord']['status'])
                await dclient.change_presence(activity=activity)

                for blacklistuser in data['discord']['blacklist']:
                    user = dclient.get_user(blacklistuser)
                    if user is None:
                        try:
                            user = await dclient.fetch_user(blacklistuser)
                        except discord.NotFound:
                            if data['loglevel'] == "debug":
                                print(red(traceback.format_exc()))
                                dstore(dclient_user,f'>>> {traceback.format_exc()}')
                            user = None
                    if user is None:
                        print(red(f'[{now_()}] [{dclient_user}] ブラックリストのユーザー {blacklistuser} が見つかりません。正しいIDになっているか確認してください。'))
                        dstore(dclient_user,f'>>>ブラックリストのユーザー {blacklistuser} が見つかりません。正しいIDになっているか確認してください')
                    else:
                        blacklist_.append(user.id)
                        if data['loglevel'] == 'debug':
                            print(yellow(f"{user} / {user.id}"))
                if data['loglevel'] == "debug":
                    print(yellow(blacklist_))
                for whitelistuser in data['discord']['whitelist']:
                    user = dclient.get_user(whitelistuser)
                    if user is None:
                        try:
                            user = await dclient.fetch_user(whitelistuser)
                        except discord.NotFound:
                            if data['loglevel'] == "debug":
                                print(red(traceback.format_exc()))
                                dstore(dclient_user,f'>>> {traceback.format_exc()}')
                            user = None
                    if user is None:
                        print(red(f'[{now_()}] [{dclient_user}] ホワイトリストのユーザー {whitelistuser} が見つかりません。正しいIDになっているか確認してください。'))
                        dstore(dclient_user,f'>>>ホワイトリストのユーザー {whitelistuser} が見つかりません。正しいIDになっているか確認してください')
                    else:
                        whitelist_.append(user.id)
                        if data['loglevel'] == 'debug':
                            print(yellow(f"{user.display_name} / {user.id}"))
                if data['loglevel'] == "debug":
                    print(yellow(whitelist_))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['addblacklist'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['addblacklist']}] [ユーザー名/ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and user.id not in blacklist}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and user.id not in blacklist:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if user.id not in blacklist:
                    blacklist.append(user.id)
                    if user.display_name is not None:
                        data["fortnite"]["blacklist"].append(user.display_name)
                    else:
                        data["fortnite"]["blacklist"].append(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をブラックリストに追加しました")
                else:
                    await reply(message, f"ユーザー {str(user.display_name)} / {user.id} は既にブラックリストに追加されています")
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        if user.id not in blacklist:
            blacklist.append(user.id)
            if user.display_name is not None:
                data["fortnite"]["blacklist"].append(user.display_name)
            else:
                data["fortnite"]["blacklist"].append(user.id)
            try:
                with open("config.json", "r", encoding="utf-8") as f:
                    data_ = json.load(f)
            except json.decoder.JSONDecodeError:
                with open("config.json", "r", encoding="utf-8-sig") as f:
                    data_ = json.load(f)
            data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
            await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をブラックリストに追加しました")
        else:
            await reply(message, f"ユーザー {str(user.display_name)} / {user.id} は既にブラックリストに追加されています")""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーをブラックリストに追加します"
                await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['removeblacklist'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['removeblacklist']}] [ユーザー名/ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and user.id in blacklist}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and user.id in blacklist:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if user.id in blacklist:
                    blacklist.remove(user.id)
                    try:
                        data["fortnite"]["blacklist"].remove(user.display_name)
                    except ValueError:
                        data["fortnite"]["blacklist"].remove(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をブラックリストから削除")
                else:
                    await reply(message, f"ユーザー {str(user.display_name)} / {user.id} はブラックリストに含まれていません")
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        if user.id in blacklist:
            blacklist.remove(user.id)
            try:
                data["fortnite"]["blacklist"].remove(user.display_name)
            except ValueError:
                data["fortnite"]["blacklist"].remove(user.id)
            try:
                with open("config.json", "r", encoding="utf-8") as f:
                    data_ = json.load(f)
            except json.decoder.JSONDecodeError:
                with open("config.json", "r", encoding="utf-8-sig") as f:
                    data_ = json.load(f)
            data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
            await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をブラックリストから削除")
        else:
            await reply(message, f"ユーザー {str(user.display_name)} / {user.id} はブラックリストに含まれていません")""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーをブラックリストから削除します"
                await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['addwhitelist'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['addwhitelist']}] [ユーザー名/ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and user.id not in whitelist}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and user.id not in whitelist:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if user.id not in whitelist:
                    whitelist.append(user.id)
                    if user.display_name is not None:
                        data["fortnite"]["whitelist"].append(user.display_name)
                    else:
                        data["fortnite"]["whitelist"].append(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["fortnite"]["whitelist"] = data["fortnite"]["whitelist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をホワイトリストに追加しました")
                else:
                    await reply(message, f"ユーザー {str(user.display_name)} / {user.id} は既にホワイトリストに追加されています")
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        if user.id not in whitelist:
            whitelist.append(user.id)
            if user.display_name is not None:
                data["fortnite"]["whitelist"].append(user.display_name)
            else:
                data["fortnite"]["whitelist"].append(user.id)
            try:
                with open("config.json", "r", encoding="utf-8") as f:
                    data_ = json.load(f)
            except json.decoder.JSONDecodeError:
                with open("config.json", "r", encoding="utf-8-sig") as f:
                    data_ = json.load(f)
            data_["fortnite"]["whitelist"] = data["fortnite"]["whitelist"]
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
            await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をホワイトリストに追加しました")
        else:
            await reply(message, f"ユーザー {str(user.display_name)} / {user.id} は既にホワイトリストに追加されています")""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーをホワイトリストに追加します"
                await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['removewhitelist'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['removewhitelist']}] [ユーザー名/ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and user.id in whitelist}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and user.id in whitelist:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if user.id in whitelist:
                    whitelist.remove(user.id)
                    try:
                        data["whitelist"].remove(user.display_name)
                    except ValueError:
                        data["whitelist"].remove(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["whitelist"] = data["whitelist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をホワイトリストから削除")
                else:
                    await reply(message, f"ユーザー {str(user.display_name)} / {user.id} はホワイトリストに含まれていません")
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        if user.display_name in data["blacklist"] or user.id in data["blacklist"]:
            blacklist.remove(user.id)
            try:
                data["blacklist"].remove(user.display_name)
            except ValueError:
                data["blacklist"].remove(user.id)
            try:
                with open("config.json", "r", encoding="utf-8") as f:
                    data_ = json.load(f)
            except json.decoder.JSONDecodeError:
                with open("config.json", "r", encoding="utf-8-sig") as f:
                    data_ = json.load(f)
            data_["blacklist"] = data["blacklist"]
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
            await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をブラックリストから削除")
        else:
            await reply(message, f"ユーザー {str(user.display_name)} / {user.id} はブラックリストに含まれていません")""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーをホワイトリストから削除します"
                await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['get'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['get']}] [ユーザー名/ユーザーID]")
                return
            users = {member.display_name: member for member in client.user.party.members.values() if rawcontent.lower() in member.display_name.lower() and member.display_name is not None}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.user.party.members.get(user.id) is not None:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                member=client.user.party.members.get(user.id)
                if member is None:
                    await reply(message, "ユーザーがパーティーにいません")
                    return
                if data['no-logs'] is False:
                    print(f'{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}')
                if data['loglevel'] == 'debug':
                    print(json.dumps(member.meta.schema, indent=2))
                dstore(name,f'{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}')
                await reply(message, f'{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}')
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        member=client.user.party.members.get(user.id)
        if member is None:
            await reply(message, "ユーザーがパーティーにいません")
            return
        if data['no-logs'] is False:
            print(f'''{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}''')
        if data['loglevel'] == 'debug':
            print(json.dumps(member.meta.schema, indent=2))
        dstore(name,f'''{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}''')
        await reply(message, f'''{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}''')""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーの情報を取得します"
                await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['friendcount'].split(','):
        try:
            if data['no-logs'] is False:
                print(f'フレンド数: {len(client.friends)}')
            dstore(name,f'フレンド数: {len(client.friends)}')
            await reply(message, f'フレンド数: {len(client.friends)}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

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
            dstore(name,f'保留数: {len(client.pending_friends)}\n送信: {len(outbound)}\n受信: {len(inbound)}')
            await reply(message, f'保留数: {len(client.pending_friends)}\n送信: {len(outbound)}\n受信: {len(inbound)}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['blockcount'].split(','):
        try:
            if data['no-logs'] is False:
                print(f'ブロック数: {len(client.blocked_users)}')
            dstore(name,f'ブロック数: {len(client.blocked_users)}')
            await reply(message, f'ブロック数: {len(client.blocked_users)}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['friendlist'].split(','):
        try:
            text=''
            for friend in client.friends.values():
                add_cache(client, friend)
                text+=f'\n{friend}'
            if data['no-logs'] is False:
                print(f'{text}')
            dstore(name,f'{text}')
            await reply(message, f'{text}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['pendinglist'].split(','):
        try:
            outbound=''
            inbound=''
            for pending in client.pending_friends.values():
                add_cache(client, pending)
                if pending.direction == 'OUTBOUND':
                    outbound+=f'\n{pending}'
                elif pending.direction == 'INBOUND':
                    inbound+=f'\n{pending}'
            if data['no-logs'] is False:
                print(f'送信: {outbound}\n受信: {inbound}')
            dstore(name,f'送信: {outbound}\n受信: {inbound}')
            await reply(message, f'送信: {outbound}\n受信: {inbound}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['blocklist'].split(','):
        try:
            text=''
            for block in client.blocked_users.values():
                add_cache(client, block)
                text+=f'\n{block}'
            if data['no-logs'] is False:
                print(f'{text}')
            dstore(name,f'{text}')
            await reply(message, f'{text}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['outfitmimic'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.outfitmimic=True
                await reply(message, 'コスチュームミミックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.outfitmimic=False
                await reply(message, 'コスチュームミミックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['skinmimic']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['backpackmimic'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.backpackmimic=True
                await reply(message, 'バックアクセサリーミミックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.backpackmimic=False
                await reply(message, 'バックアクセサリーミミックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['skinmimic']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['pickaxemimic'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.pickaxemimic=True
                await reply(message, '収集ツールミミックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.pickaxemimic=False
                await reply(message, '収集ツールミミックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['skinmimic']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['emotemimic'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.emotemimic=True
                await reply(message, 'エモートミミックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.emotemimic=False
                await reply(message, 'エモートミミックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['emotemimic']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['whisper'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.whisper=True
                await reply(message, '囁きからのコマンド受付をオンに設定')
            elif args[1] in commands['false'].split(','):
                client.whisper=False
                await reply(message, '囁きからのコマンド受付をオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['whisper']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['partychat'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.partychat=True
                await reply(message, 'パーティーチャットからのコマンド受付をオンに設定')
            elif args[1] in commands['false'].split(','):
                client.partychat=False
                await reply(message, 'パーティーチャットからのコマンド受付をオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['party']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['discord'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.discord=True
                await reply(message, 'Discordからのコマンド受付をオンに設定')
            elif args[1] in commands['false'].split(','):
                client.discord=False
                await reply(message, 'Discordからのコマンド受付をオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['discord']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['disablewhisperperfectly'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.whisperperfect=True
                await reply(message, '囁きの完全無効をオンに設定')
            elif args[1] in commands['false'].split(','):
                client.whisperperfect=False
                await reply(message, '囁きの完全無効をオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['disablewhisperperfectly']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['disablepartychatperfectly'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.partychatperfect=True
                await reply(message, 'パーティーチャットの完全無効をオンに設定')
            elif args[1] in commands['false'].split(','):
                client.partychatperfect=False
                await reply(message, 'パーティーチャットの完全無効をオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['disablepartychatperfectly']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['disablediscordperfectly'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.discordperfect=True
                await reply(message, 'Discordの完全無効をオンに設定')
            elif args[1] in commands['false'].split(','):
                client.discordperfect=False
                await reply(message, 'Discordの完全無効をオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['disablediscordperfectly']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['acceptinvite'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.acceptinvite=True
                await reply(message, '招待を承諾に設定')
            elif args[1] in commands['false'].split(','):
                client.acceptinvite=False
                await reply(message, '招待を拒否に設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['acceptinvite']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['acceptfriend'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.acceptfriend=True
                await reply(message, 'フレンド申請を承諾に設定')
            elif args[1] in commands['false'].split(','):
                client.acceptfriend=False
                await reply(message, 'フレンド申請を拒否に設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['acceptfriend']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['joinmessageenable'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.joinmessageenable=True
                await reply(message, 'パーティー参加時のメッセージをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.joinmessageenable=False
                await reply(message, 'パーティー参加時のメッセージをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['joinmessageenable']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['randommessageenable'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.randommessageenable=True
                await reply(message, 'パーティー参加時のランダムメッセージをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.randommessageenable=False
                await reply(message, 'パーティー参加時のランダムメッセージをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['randommessageenable']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

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
                await reply(message, f"{str(data['fortnite']['waitinterval'])}秒間招待を拒否します")
            else:
                if client.owner.id in client.user.party.members.keys() and message.author.id != client.owner.id:
                    await reply(message, '現在利用できません')
                    return
                client.acceptinvite=False
                try:
                    client.timer_.cancel()
                except AttributeError:
                    pass
                client.timer_=Timer(data['fortnite']['waitinterval'], inviteaccept, [client])
                client.timer_.start()
                await reply(message, f"{str(data['fortnite']['waitinterval'])}秒間招待を拒否します")             
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['join'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['join']}] [ユーザー名/ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.has_friend(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.has_friend(user.id) is True:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                friend=client.get_friend(user.id)
                if friend is None:
                    await reply(message, 'ユーザーとフレンドではありません')
                else:
                    await friend.join_party()
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            friend=client.get_friend(user.id)
            if friend is None:
                await reply(message, 'ユーザーとフレンドではありません')
            else:
                await friend.join_party()
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーが満員か、既にパーティーにいるか、ユーザーがオフラインです')
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーが見つかりません')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーがプライベートです')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーの参加リクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーのパーティーに参加します"
                await reply(message, text)
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーが満員か、既にパーティーにいるか、ユーザーがオフラインです')
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーが見つかりません')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーがプライベートです')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーの参加リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['joinid'].split(','):
        try:
            await client.join_to_party(party_id=args[1])
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, '既にこのパーティーのメンバーです')
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーが見つかりません')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーがプライベートです')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['join']}] [パーティーID]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['leave'].split(','):
        try:
            await client.user.party.me.leave()
            await reply(message, 'パーティーを離脱')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティー離脱のリクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['invite'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['invite']}] [ユーザー名 / ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.has_friend(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.has_friend(user.id) is True:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                friend=client.get_friend(user.id)
                if friend is None:
                    await reply(message, 'ユーザーとフレンドではありません')
                    return
                await friend.invite()
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(friend.display_name)} をパーティーに招待')
                else:
                    await reply(message, f'{str(friend.display_name)} / {friend.id} をパーティー {client.user.party.id} に招待')
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            friend=client.get_friend(user.id)
            if friend is None:
                await reply(message, 'ユーザーとフレンドではありません')
                return
            await friend.invite()
            if data['loglevel'] == 'normal':
                await reply(message, f'{str(friend.display_name)} をパーティーに招待')
            else:
                await reply(message, f'{str(friend.display_name)} / {friend.id} をパーティー {client.user.party.id} に招待')
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーが満員か、既にパーティーにいます')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティー招待の送信リクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーを招待します"
                await reply(message, text)
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーが満員か、既にパーティーにいます')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティー招待の送信リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['inviteall'].split(','):
        try:
            for inviteuser in client.invitelist:
                if inviteuser != client.user.id:
                    try:
                        await client.user.party.invite(inviteuser)
                    except fortnitepy.PartyError:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(name,f'>>> {traceback.format_exc()}')
                        await reply(message, 'パーティーが満員か、既にパーティーにいます')
                    except fortnitepy.Forbidden:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(name,f'>>> {traceback.format_exc()}')
                        await reply(message, 'ユーザーとフレンドではありません')
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(name,f'>>> {traceback.format_exc()}')
                        await reply(message, 'パーティー招待の送信リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['message'].split(','):
        try:
            send=rawcontent.split(' : ')
            if len(send) < 2:
                await reply(message, f"[{commands['message']}] [ユーザー名 / ユーザーID] : [内容]")
                return
            users = {name: user for name, user in cache_users.items() if send[0].lower() in name.lower() and user.id != client.user.id and client.has_friend(user.id) is True}
            try:
                user=await client.fetch_profile(send[0])
                if user is not None:
                    if user.display_name is not None and client.has_friend(user.id) is True:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                friend=client.get_friend(user.id)
                if friend is None:
                    await reply(message, 'ユーザーとフレンドではありません')
                    return
                await friend.send(send[1])
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(friend.display_name)} にメッセージ {send[1]} を送信')
                else:
                    await reply(message, f'{str(friend.display_name)} / {friend.id} にメッセージ {send[1]} を送信')
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            friend=client.get_friend(user.id)
            if friend is None:
                await reply(message, 'ユーザーとフレンドではありません')
                return
            await friend.send(send[1])
            if data['loglevel'] == 'normal':
                await reply(message, f'{str(friend.display_name)} にメッセージ {send[1]} を送信')
            else:
                await reply(message, f'{str(friend.display_name)} / {friend.id} にメッセージ {send[1]} を送信')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user, "send": send} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーにメッセージを送信します"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['message']}] [ユーザー名 / ユーザーID] : [内容]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['partymessage'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['partymessage']}] [内容]")
                return
            await client.user.party.send(rawcontent)
            if data['loglevel'] == 'normal':
                await reply(message, f'パーティーにメッセージ {rawcontent} を送信')
            else:
                await reply(message, f'パーティー {client.user.party.id} にメッセージ {rawcontent} を送信')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['status'].split(','):
        try:
            await client.set_status(rawcontent)
            await reply(message, f'ステータスを {rawcontent} に設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['status']}] [内容]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['banner'].split(','):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_banner,args[1],args[2],client.user.party.me.banner[2]))
            await reply(message, f'バナーを {args[1]}, {args[2]}に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'バナー情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['banner']}] [バナーID] [バナーの色]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['level'].split(','):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_banner,client.user.party.me.banner[0],client.user.party.me.banner[1],int(args[1])))
            await reply(message, f'レベルを {args[1]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'レベルの設定リクエストを処理中にエラーが発生しました')
        except ValueError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, '数字を入力してください')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['level']}] [レベル]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['bp'].split(','):
        try:
            await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_battlepass_info,True,args[1],args[2],args[3]))
            await reply(message, f'バトルパス情報を ティア: {args[1]} XPブースト: {args[2]} フレンドXPブースト: {args[3]} に設定')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'バトルパス情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['bp']}] [ティア] [XPブースト] [フレンドXPブースト]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['privacy'].split(','):
        try:
            if args[1] in commands['privacy_public'].split(','):
                await client.user.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)
                await reply(message, 'プライバシーを パブリック に設定')
            elif args[1] in commands['privacy_friends_allow_friends_of_friends'].split(','):
                await client.user.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS_ALLOW_FRIENDS_OF_FRIENDS)
                await reply(message, 'プライバシーを フレンド(フレンドのフレンドを許可) に設定')
            elif args[1] in commands['privacy_friends'].split(','):
                await client.user.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS)
                await reply(message, 'プライバシーを フレンド に設定')
            elif args[1] in commands['privacy_private_allow_friends_of_friends'].split(','):
                await client.user.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE_ALLOW_FRIENDS_OF_FRIENDS)
                await reply(message, 'プライバシーを プライベート(フレンドのフレンドを許可) に設定')
            elif args[1] in commands['privacy_private'].split(','):
                await client.user.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE)
                await reply(message, 'プライバシーを プライベート に設定')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーリーダーではありません')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['privacy']}] [[{commands['privacy_public']}] / [{commands['privacy_friends_allow_friends_of_friends']}] / [{commands['privacy_friends']}] / [{commands['privacy_private_allow_friends_of_friends']}] / [{commands['privacy_private']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー') 

    elif args[0] in commands['getuser'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['getuser']}] [ユーザー名 / ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            text = str()
            for user in users.values():
                text += f'\n{str(user.display_name)} / {user.id}'
            if data['no-logs'] is False:
                print(text)
            dstore(name,text)
            await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['getfriend'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['getfriend']}] [ユーザー名 / ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.has_friend(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.has_friend(user.id) is True:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            text = str()
            for user in users.values():
                friend=client.get_friend(user.id)
                if friend is None:
                    continue
                if friend.nickname is None:
                    text += f'\n{str(friend.display_name)} / {friend.id}'
                else:
                    text += f'\n{friend.nickname}({str(friend.display_name)}) / {friend.id}'
                if friend.last_logout is not None:
                    text += '\n最後のログイン: {0.year}年{0.month}月{0.day}日 {0.hour}時{0.minute}分{0.second}秒'.format(friend.last_logout)
            if data['no-logs'] is False:
                print(text)
            dstore(name,text)
            await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['getpending'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['getpending']}] [ユーザー名 / ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.is_pending(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.is_pending(user.id) is True:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            text = str()
            for user in users.values():
                pending = client.get_pending_friend(user.id)
                if pending is None:
                    continue
                text += f'\n{str(pending.display_name)} / {pending.id}'
            if data['no-logs'] is False:
                print(text)
            dstore(name,text)
            await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['getblock'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['getblock']}] [ユーザー名 / ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.is_blocked(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.is_blocked(user.id) is True:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            text = str()
            for user in users.values():
                block=client.get_blocked_user(user.id)
                if block is None:
                    continue
                text += f'\n{str(block.display_name)} / {block.id}'
            if data['no-logs'] is False:
                print(text)
            dstore(name,text)
            await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['info'].split(','):
        try:
            if args[1] in commands['info_party'].split(','):
                text = str()
                text += f'{client.user.party.id}\n人数: {client.user.party.member_count}'
                for member in client.user.party.members.values():
                    add_cache(client, member)
                    if data['loglevel'] == 'normal':
                        text += f'\n{str(member.display_name)}'
                    else:
                        text += f'\n{str(member.display_name)} / {member.id}'
                print(text)
                dstore(None, text)
                await reply(message, text)
                if data['loglevel'] == 'debug':
                    print(json.dumps(client.user.party.meta.schema, indent=2))
            
            elif True in [args[1] in commands[key].split(',') for key in ("cid", "bid", "petcarrier", "pickaxe_id", "eid", "emoji_id", "toy_id", "shout_id", "id")]:
                type_ = convert_to_type(args[1])
                if rawcontent2 == '':
                    await reply(message, f"[{commands[type_]}] [ID]")
                    return
                result = await loop.run_in_executor(None, search_item, "ja", "id", rawcontent2, type_)
                if result is None:
                    result = await loop.run_in_executor(None, search_item, "en", "id", rawcontent2, type_)
                if result is None:
                    await reply(message, "見つかりません")
                else:
                    if len(result) > 30:
                        await reply(message, f"見つかったアイテム数 {len(result)} は多すぎます")
                        return
                    if len(result) == 1:
                        await reply(message, f"{result[0]['shortDescription']}: {result[0]['name']} | {result[0]['id']}\n説明: {result[0]['description']}\nレア度: {result[0]['displayRarity']}\n{result[0]['set']}")
                    else:
                        text = str()
                        for count, item in enumerate(result):
                            text += f"\n{count+1} {item['shortDescription']}: {item['name']} | {item['id']}"
                        text += "\n数字を入力することでそのアイテムに設定します"
                        await reply(message, text)
                        client.select[message.author.id] = {"exec": [f"await reply(message, f'''{item['shortDescription']}: {item['name']} | {item['id']}\n{item['description']}\n{item['displayRarity']}\n{item['set']}''')" for item in result]}

            elif True in  [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe", "emote", "emoji", "toy", "shout", "item")]:
                type_ = convert_to_type(args[1])
                if rawcontent2 == '':
                    await reply(message, f"[{commands[type_]}] [アイテム名]")
                    return
                result = await loop.run_in_executor(None, search_item, "ja", "name", rawcontent2, type_)
                if result is None:
                    result = await loop.run_in_executor(None, search_item, "en", "name", rawcontent2, type_)
                if result is None:
                    await reply(message, "見つかりません")
                else:
                    if len(result) > 30:
                        await reply(message, f"見つかったアイテム数 {len(result)} は多すぎます")
                        return
                    if len(result) == 1:
                        await reply(message, f"{result[0]['shortDescription']}: {result[0]['name']} | {result[0]['id']}\n{result[0]['description']}\n{result[0]['displayRarity']}\n{result[0]['set']}")
                    else:
                        text = str()
                        for count, item in enumerate(result):
                            text += f"\n{count+1} {item['shortDescription']}: {item['name']} | {item['id']}"
                        text += "\n数字を入力することでそのアイテムに設定します"
                        await reply(message, text)
                        client.select[message.author.id] = {"exec": [f"await reply(message, f'''{item['shortDescription']}: {item['name']} | {item['id']}\n{item['description']}\n{item['displayRarity']}\n{item['set']}''')" for item in result]}
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['info']}] [[{commands['info_party']}] / [{commands['info_item']}] / [{commands['id']}] / [{commands['skin']}] / [{commands['bag']}] / [{commands['pickaxe']}] / [{commands['emote']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['pending'].split(','):
        try:
            pendings=[]
            for pending in client.pending_friends.values():
                add_cache(client, pending)
                if pending.direction == 'INBOUND':
                    pendings.append(pending)
            if args[1] in commands['true'].split(','):
                for pending in pendings:
                    try:
                        await pending.accept()
                        if data['loglevel'] == 'normal':
                            await reply(message, f'{str(pending.display_name)} をフレンドに追加')
                        else:
                            await reply(message, f'{str(pending.display_name)} / {pending.id} をフレンドに追加')
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                        if data['loglevel'] == 'normal':
                            await reply(message, f'{str(pending.dispaly_name)} のフレンド申請の承認リクエストを処理中にエラーが発生しました')
                        else:
                            await reply(message, f'{str(pending.display_name)} / {pending.id} のフレンド申請の承認リクエストを処理中にエラーが発生しました')
                        continue
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                        await reply(message, 'エラー')
                        continue
            elif args[1] in commands['false'].split(','):
                for pending in pendings:
                    try:
                        await pending.decline()
                        if data['loglevel'] == 'normal':
                            await reply(message, f'{str(pending.display_name)} のフレンド申請を拒否')
                        else:
                            await reply(message, f'{str(pending.display_name)} / {pending.id} のフレンド申請を拒否')
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(name,f'>>> {traceback.format_exc()}')
                        if data['loglevel'] == 'normal':
                            await reply(message, f'{str(pending.display_name)} のフレンド申請の拒否リクエストを処理中にエラーが発生しました')
                        else:
                            await reply(message, f'{str(pending.display_name)} / {pending.id} のフレンド申請の拒否リクエストを処理中にエラーが発生しました')
                        continue
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                        await reply(message, 'エラー')
                        continue
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['pending']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['removepending'].split(','):
        try:
            pendings=[]
            for pending in client.pending_friends.values():
                add_cache(client, pending)
                if pending.direction == 'OUTBOUND':
                    pendings.append(pending)
            for pending in pendings:
                try:
                    await pending.decline()
                    if data['loglevel'] == 'normal':
                        await reply(message, f'{str(pending.display_name)} へのフレンド申請を解除')
                    else:
                        await reply(message, f'{str(pending.display_name)} / {pending.id} へのフレンド申請を解除')
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    if data['loglevel'] == 'normal':
                        await reply(message, f'{str(pending.display_name)} へのフレンド申請を解除リクエストを処理中にエラーが発生しました')
                    else:
                        await reply(message, f'{str(pending.display_name)} / {pending.id} へのフレンド申請を解除リクエストを処理中にエラーが発生しました')
                    continue
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'エラー')
                    continue
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['addfriend'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['addfriend']}] [ユーザー名 / ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.has_friend(user.id) is False}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.has_friend(user.id) is False:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.has_friend(user.id) is True:
                    await reply(message, '既にユーザーとフレンドです')
                    return
                await client.add_friend(user.id)
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(user.display_name)} にフレンド申請を送信')
                else:
                    await reply(message, f'{str(user.display_name)} / {user.id} にフレンド申請を送信')
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.has_friend(user.id) is True:
                await reply(message, '既にユーザーとフレンドです')
                return
            await client.add_friend(user.id)
            if data['loglevel'] == 'normal':
                await reply(message, f'{str(user.display_name)} にフレンド申請を送信')
            else:
                await reply(message, f'{str(user.display_name)} / {user.id} にフレンド申請を送信')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'フレンド申請の送信リクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーにフレンド申請を送信します"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'フレンド申請の送信リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['removefriend'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['removefriend']}] [ユーザー名 / ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.has_friend(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.has_friend(user.id) is True:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.has_friend(user.id) is False:
                    await reply(message, 'ユーザーとフレンドではありません')
                    return
                await client.remove_or_decline_friend(user.id)
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(user.display_name)} をフレンドから削除')
                else:
                    await reply(message, f'{str(user.display_name)} / {user.id} をフレンドから削除')
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.has_friend(user.id) is False:
                await reply(message, 'ユーザーとフレンドではありません')
                return
            await client.remove_or_decline_friend(user.id)
            if data['loglevel'] == 'normal':
                await reply(message, f'{str(user.display_name)} をフレンドから削除')
            else:
                await reply(message, f'{str(user.display_name)} / {user.id} をフレンドから削除')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'フレンドの削除リクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーをフレンドから削除します"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'フレンドの削除リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['acceptpending'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['acceptpending']}] [ユーザー名 / ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.is_pending(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.is_pending(user.id) is True:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.is_pending(user.id) is False:
                    await reply(message, 'ユーザーからのフレンド申請がありません')
                    return
                await client.accept_friend(user.id)
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(user.display_name)} をフレンドに追加')
                else:
                    await reply(message, f'{str(user.display_name)} / {user.id} をフレンドに追加')
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.is_pending(user.id) is False:
                await reply(message, 'ユーザーからのフレンド申請がありません')
                return
            await client.accept_friend(user.id)
            if data['loglevel'] == 'normal':
                await reply(message, f'{str(user.display_name)} をフレンドに追加')
            else:
                await reply(message, f'{str(user.display_name)} / {user.id} をフレンドに追加')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'フレンドの追加リクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーからのフレンド申請を承諾します"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'フレンドの追加リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['declinepending'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['declinepending']}] [ユーザー名 / ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.is_pending(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.is_pending(user.id) is True:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.is_pending(user.id) is False:
                    await reply(message, 'ユーザーからのフレンド申請がありません')
                    return
                await client.remove_or_decline_friend(user.id)
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(user.display_name)} のフレンド申請を拒否')
                else:
                    await reply(message, f'{str(user.display_name)} / {user.id} のフレンド申請を拒否')
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.is_pending(user.id) is False:
                await reply(message, 'ユーザーからのフレンド申請がありません')
                return
            await client.remove_or_decline_friend(user.id)
            if data['loglevel'] == 'normal':
                await reply(message, f'{str(user.display_name)} のフレンド申請を拒否')
            else:
                await reply(message, f'{str(user.display_name)} / {user.id} のフレンド申請を拒否')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'フレンド申請の拒否リクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーからのフレンド申請を拒否します"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'フレンド申請の拒否リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['blockfriend'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['blockfriend']}] [ユーザー名 / ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.is_blocked(user.id) is False}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.is_blocked(user.id) is False:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.is_blocked(user.id) is True:
                    await reply(message, '既にユーザーをブロックしています')
                    return
                await client.block_user(user.id)
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(user.display_name)} をブロック')
                else:
                    await reply(message, f'{str(user.display_name)} / {user.id} をブロック')
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.is_blocked(user.id) is True:
                await reply(message, '既にユーザーをブロックしています')
                return
            await client.block_user(user.id)
            if data['loglevel'] == 'normal':
                await reply(message, f'{str(user.display_name)} をブロック')
            else:
                await reply(message, f'{str(user.display_name)} / {user.id} をブロック')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'フレンドのブロックリクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーをブロックします"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'フレンドのブロックリクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['unblockfriend'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['unblockfriend']}] [ユーザー名 / ユーザーID]")
                return
            users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.is_blocked(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.is_blocked(user.id) is True:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.is_blocked(user.id) is False:
                    await reply(message, 'ユーザーをブロックしていません')
                    return
                await client.unblock_user(user.id)
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(user.display_name)} をブロック解除')
                else:
                    await reply(message, f'{str(user.display_name)} / {user.id} をブロック解除')
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.is_blocked(user.id) is False:
                await reply(message, 'ユーザーをブロックしていません')
                return
            await client.unblock_user(user.id)
            if data['loglevel'] == 'normal':
                await reply(message, f'{str(user.display_name)} をブロック解除')
            else:
                await reply(message, f'{str(user.display_name)} / {user.id} をブロック解除')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'ブロックしたユーザーのブロック解除リクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーをブロック解除します"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'ブロックしたユーザーのブロック解除リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['chatban'].split(','):
        try:
            reason=rawcontent.split(' : ')
            if rawcontent == '':
                await reply(message, f"[{commands['chatban']}] [ユーザー名 / ユーザーID] : [理由(任意)]")
                return
            users = {member.display_name: member for member in client.user.party.members.values() if rawcontent.lower() in member.display_name.lower() and member.display_name is not None}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.user.party.members.get(user.id) is not None:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.user.party.members.get(user.id) is None:
                    await reply(message, 'ユーザーがパーティーにいません')
                    return
                member=client.user.party.members.get(user.id)
                try:
                    await member.chatban(reason[1])
                except IndexError:
                    await member.chatban()
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(user.display_name)} をバン')
                else:
                    await reply(message, f'{str(user.display_name)} / {user.id} をバン')
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.user.party.members.get(user.id) is None:
                await reply(message, 'ユーザーがパーティーにいません')
                return
            member=client.user.party.members.get(user.id)
            try:
                await member.chatban(reason[1])
            except IndexError:
                await member.chatban()
            if data['loglevel'] == 'normal':
                await reply(message, f'{str(user.display_name)} をバン')
            else:
                await reply(message, f'{str(user.display_name)} / {user.id} をバン')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーリーダーではありません')
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'メンバーが見つかりません')
        except ValueError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, '既にバンされています')""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user, "reason": reason} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーをバンします"
                await reply(message, text)
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーリーダーではありません')
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'メンバーが見つかりません')
        except ValueError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, '既にバンされています')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['promote'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['promote']}] [ユーザー名 / ユーザーID]")
                return
            users = {member.display_name: member for member in client.user.party.members.values() if rawcontent.lower() in member.display_name.lower() and member.display_name is not None}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.user.party.members.get(user.id) is not None:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.user.party.members.get(user.id) is None:
                    await reply(message, 'ユーザーがパーティーにいません')
                    return
                member=client.user.party.members.get(user.id)
                await member.promote()
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(user.display_name)} に譲渡')
                else:
                    await reply(message, f'{str(user.display_name)} / {user.id} に譲渡')
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.user.party.members.get(user.id) is None:
                await reply(message, 'ユーザーがパーティーにいません')
                return
            member=client.user.party.members.get(user.id)
            await member.promote()
            if data['loglevel'] == 'normal':
                await reply(message, f'{str(user.display_name)} に譲渡')
            else:
                await reply(message, f'{str(user.display_name)} / {user.id} に譲渡')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーリーダーではありません')
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, '既にパーティーリーダーです')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーリーダーの譲渡リクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーに譲渡します"
                await reply(message, text)
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーリーダーではありません')
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, '既にパーティーリーダーです')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーリーダーの譲渡リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['kick'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['kick']}] [ユーザー名 / ユーザーID]")
                return
            users = {member.display_name: member for member in client.user.party.members.values() if rawcontent.lower() in member.display_name.lower() and member.display_name is not None}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.display_name is not None and client.user.party.members.get(user.id) is not None:
                        users[user.display_name] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.user.party.members.get(user.id) is None:
                    await reply(message, 'ユーザーがパーティーにいません')
                    return
                member=client.user.party.members.get(user.id)
                await member.kick()
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(user.display_name)} をキック')
                else:
                    await reply(message, f'{str(user.display_name)} / {user.id} をキック')
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.user.party.members.get(user.id) is None:
                await reply(message, 'ユーザーがパーティーにいません')
                return
            member=client.user.party.members.get(user.id)
            await member.kick()
            if data['loglevel'] == 'normal':
                await reply(message, f'{str(user.display_name)} をキック')
            else:
                await reply(message, f'{str(user.display_name)} / {user.id} をキック')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーリーダーではありません')
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, '自分をキックすることはできません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーメンバーのキックリクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                    ],
                    "variable": [
                        {"user": user} for name, user in users.items()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {user.display_name} / {user.id}"
                text += "\n数字を入力することでそのユーザーをキックします"
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーリーダーではありません')
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, '自分をキックすることはできません')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーメンバーのキックリクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['ready'].split(','):
        try:
            await client.user.party.me.set_ready(fortnitepy.ReadyState.READY)
            await reply(message, '準備状態を 準備OK に設定')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['unready'].split(','):
        try:
            await client.user.party.me.set_ready(fortnitepy.ReadyState.NOT_READY)
            await reply(message, '準備状態を 準備中 に設定')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['sitout'].split(','):
        try:
            await client.user.party.me.set_ready(fortnitepy.ReadyState.SITTING_OUT)
            await reply(message, '準備状態を 欠場中 に設定')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['outfitlock'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.outfitlock=True
                await reply(message, 'コスチュームロックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.outfitlock=False
                await reply(message, 'コスチュームロックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['outfitlock']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['backpacklock'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.backpacklock=True
                await reply(message, 'バックアクセサリーロックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.backpacklock=False
                await reply(message, 'バックアクセサリーロックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['backpacklock']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['pickaxelock'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.pickaxelock=True
                await reply(message, '収集ツールロックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.pickaxelock=False
                await reply(message, '収集ツールロックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['pickaxelock']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['emotelock'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.emotelock=True
                await reply(message, 'エモートロックをオンに設定')
            elif args[1] in commands['false'].split(','):
                client.emotelock=False
                await reply(message, 'エモートロックをオフに設定')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['outfitlock']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['stop'].split(','):
        try:
            client.stopcheck=True
            if await change_asset(client, message.author.id, "emote", "") is True:
                await reply(message, '停止しました')
            else:
                await reply(message, 'ロックされています')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['alloutfit'].split(','):
        try:
            flag = False
            if client.outfitlock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, 'ロックされています')
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
            await reply(message, '全てのコスチュームを表示し終わりました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['allbackpack'].split(','):
        try:
            flag = False
            if client.backpacklock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, 'ロックされています')
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allskin = json.load(f)
            for item in allskin['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type'] == 'backpack':
                    if 'banner' not in item['id']:
                        await client.user.party.me.set_backpack(item['id'])
                    else:
                        await client.user.party.me.set_backpack(item['id'],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner'))
                    await asyncio.sleep(2)
            await reply(message, '全てのバックアクセサリーを表示し終わりました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['allpet'].split(','):
        try:
            flag = False
            if client.backpacklock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, 'ロックされています')
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allskin = json.load(f)
            for item in allskin['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type'] == 'pet':
                    if 'banner' not in item['id']:
                        await client.user.party.me.set_backpack(item['id'])
                    else:
                        await client.user.party.me.set_backpack(item['id'],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner'))
                    await asyncio.sleep(2)
            await reply(message, '全てのペットを表示し終わりました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['allpickaxe'].split(','):
        try:
            flag = False
            if client.pickaxelock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, 'ロックされています')
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allskin = json.load(f)
            for item in allskin['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type'] == 'pickaxe':
                    if 'banner' not in item['id']:
                        await client.user.party.me.set_pickaxe(item['id'])
                    else:
                        await client.user.party.me.set_pickaxe(item['id'],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner'))
                    await asyncio.sleep(2)
            await reply(message, '全ての収集ツールを表示し終わりました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['allemote'].split(','):
        try:
            flag = False
            if client.emotelock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, 'ロックされています')
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
                await reply(message, '全てのエモートを表示し終わりました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['allemoji'].split(','):
        try:
            flag = False
            if client.emotelock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, 'ロックされています')
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allemote = json.load(f)
            for item in allemote['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type'] == 'emoji':
                    await client.user.party.me.set_emote(item['id'])
                    await asyncio.sleep(5)
            else:
                await reply(message, '全てのエモートアイコンを表示し終わりました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['alltoy'].split(','):
        try:
            flag = False
            if client.emotelock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, 'ロックされています')
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allemote = json.load(f)
            for item in allemote['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type'] == 'toy':
                    await client.user.party.me.set_emote(item['id'])
                    await asyncio.sleep(5)
            else:
                await reply(message, '全てのおもちゃを表示し終わりました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['allshout'].split(','):
        try:
            flag = False
            if client.emotelock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, 'ロックされています')
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allemote = json.load(f)
            for item in allemote['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type'] == 'shout':
                    await client.user.party.me.set_emote(item['id'])
                    await asyncio.sleep(5)
            else:
                await reply(message, '全てのshoutを表示し終わりました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['setenlightenment'].split(','):
        try:
            if await change_asset(client, message.author.id, "outfit", client.user.party.me.outfit, client.user.party.me.outfit_variants,(args[1],args[2])) is True:
                await reply(message, f'{args[1]}, {args[2]} に設定')
            else:
                await reply(message, 'ロックされています')
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['setenlightenment']}] [数値] [数値]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif True in [args[0] in commands[key].split(',') for key in ("cid", "bid", "petcarrier", "pickaxe_id", "eid", "emoji_id", "toy_id", "shout_id", "id")]:
        type_ = convert_to_type(args[0])
        if rawcontent == '':
            await reply(message, f"[{commands[type_]}] [ID]")
            return
        try:
            result = await loop.run_in_executor(None, search_item, "ja", "id", rawcontent, type_)
            if result is None:
                result = await loop.run_in_executor(None, search_item, "en", "id", rawcontent, type_)
            if result is None:
                await reply(message, "見つかりません")
            else:
                if len(result) > 30:
                    await reply(message, f"見つかったアイテム数 {len(result)} は多すぎます")
                    return
                if len(result) == 1:
                    if await change_asset(client, message.author.id, result[0]["type"], result[0]['id']) is True:
                        await reply(message, f"{result[0]['shortDescription']}: {result[0]['name']} | {result[0]['id']}")
                    else:
                        await reply(message, "ロックされています")
                else:
                    text = str()
                    for count, item in enumerate(result):
                        text += f"\n{count+1} {item['shortDescription']}: {item['name']} | {item['id']}"
                    text += "\n数字を入力することでそのアイテムに設定します"
                    await reply(message, text)
                    client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{item['type']}', '{item['id']}')" for item in result]}
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif True in  [args[0] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe", "emote", "emoji", "toy", "shout", "item")]:
        type_ = convert_to_type(args[0])
        if rawcontent == '':
            await reply(message, f"[{commands[type_]}] [アイテム名]")
            return
        try:
            result = await loop.run_in_executor(None, search_item, "ja", "name", rawcontent, type_)
            if result is None:
                result = await loop.run_in_executor(None, search_item, "en", "name", rawcontent, type_)
            if result is None:
                await reply(message, "見つかりません")
            else:
                if len(result) > 30:
                    await reply(message, f"見つかったアイテム数 {len(result)} は多すぎます")
                    return
                if len(result) == 1:
                    if await change_asset(client, message.author.id, result[0]["type"], result[0]['id']) is True:
                        await reply(message, f"{result[0]['shortDescription']}: {result[0]['name']} | {result[0]['id']}")
                    else:
                        await reply(message, "ロックされています")
                else:
                    text = str()
                    for count, item in enumerate(result):
                        text += f"\n{count+1} {item['shortDescription']}: {item['name']} | {item['id']}"
                    text += "\n数字を入力することでそのアイテムに設定します"
                    await reply(message, text)
                    client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{item['type']}', '{item['id']}')" for item in result]}
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['set'].split(','):
        if rawcontent == '':
            await reply(message, f"[{commands['set']}] [セット名]]")
            return
        try:
            result = await loop.run_in_executor(None, search_item, "ja", "set", rawcontent)
            if result is None:
                result = await loop.run_in_executor(None, search_item, "en", "set", rawcontent)
            if result is None:
                await reply(message, "見つかりません")
            else:
                if len(result) > 30:
                    await reply(message, f"見つかったアイテム数 {len(result)} は多すぎます")
                    return
                if len(result) == 1:
                    if await change_asset(client, message.author.id, result[0]["type"], result[0]['id']) is True:
                        await reply(message, f"{result[0]['shortDescription']}: {result[0]['name']} | {result[0]['id']}({result[0]['set']})")
                    else:
                        await reply(message, "ロックされています")
                else:
                    text = str()
                    for count, item in enumerate(result):
                        text += f"\n{count+1} {item['shortDescription']}: {item['name']} | {item['id']}({result[0]['set']})"
                    text += "\n数字を入力することでそのアイテムに設定します"
                    await reply(message, text)
                    client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{item['type']}', '{item['id']}')" for item in result]}
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['setstyle'].split(','):
        try:
            if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe")]:
                await reply(message, f"[{commands['setstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                return
            type_ = convert_to_type(args[1])
            id_ = member_asset(client.user.party.me, convert_to_asset(args[1]))
            result = search_style("ja", id_)
            if result is None:
                await reply(message, "スタイル変更はありません")
            else:
                text = str()
                for count, item in enumerate(result):
                    text += f"\n{count+1} {item['name']}"
                text += "\n数字を入力することでそのアイテムに設定します"
                await reply(message, text)
                client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{type_}', '{id_}', {variants['variants']})" for variants in result]}
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['setstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['addstyle'].split(','):
        try:
            if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe")]:
                await reply(message, f"[{commands['addstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                return
            type_ = convert_to_type(args[1])
            id_ = member_asset(client.user.party.me, convert_to_asset(args[1]))
            variants_ = eval(f"client.user.party.me.{convert_to_asset(args[1])}_variants")
            result = search_style("ja", id_)
            if result is None:
                await reply(message, "スタイル変更はありません")
            else:
                text = str()
                for count, item in enumerate(result):
                    text += f"\n{count+1} {item['name']}"
                text += "\n数字を入力することでそのアイテムに設定します"
                await reply(message, text)
                client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{type_}', '{id_}', {variants_} + {variants['variants']})" for variants in result]}
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['addstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['setvariant'].split(','):
        try:
            if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe")]:
                await reply(message, f"[{commands['setvariant']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                return
            variantdict={}
            for count,text in enumerate(args[2:]):
                if count % 2 != 0:
                    continue
                try:
                    variantdict[text]=args[count+3]
                except IndexError:
                    break
            type_ = convert_to_type(args[1])
            id_ = member_asset(client.user.party.me, convert_to_asset(args[1]))
            variants = client.user.party.me.create_variants(item='AthenaCharacter',**variantdict)
            if await change_asset(client, message.author.id, type_, id_, variants, client.user.party.me.enlightenment) is False:
                await reply(message, "ロックされています")
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['setvariant']}] [ID] [variant] [数値]\nvariantと数値は無限に設定可能")
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['addvariant'].split(','):
        try:
            if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe")]:
                await reply(message, f"[{commands['addvariant']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                return
            variantdict={}
            for count,text in enumerate(args[2:]):
                if count % 2 != 0:
                    continue
                try:
                    variantdict[text]=args[count+3]
                except IndexError:
                    break
            type_ = convert_to_type(args[1])
            id_ = member_asset(client.user.party.me, convert_to_asset(args[1]))
            variants = client.user.party.me.create_variants(item='AthenaCharacter',**variantdict)
            variants += eval(f"client.user.party.me.{convert_to_asset(args[1])}_variants")
            if await change_asset(client, message.author.id, type_, id_, variants, client.user.party.me.enlightenment) is False:
                await reply(message, "ロックされています")
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['addvariant']}] [ID] [variant] [数値]\nvariantと数値は無限に設定可能")
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif True in [args[0] in commands[key].split(',') for key in ("outfitasset", "backpackasset", "pickaxeasset", "emoteasset")]:
        type_ = convert_to_type(args[0])
        try:
            if rawcontent == '':
                await reply(message, f"[{commands[f'{type_}asset']}] [アセットパス]")
                return
            if await change_asset(client, message.author.id, type_, rawcontent) is False:
                await reply(message, "ロックされています")
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif True in [args[0].lower().startswith(id_) for id_ in ("cid_", "bid_", "petcarrier_", "pickaxe_id_", "eid_", "emoji_", "toy_", "shout_")]:
        try:
            type_ = convert_to_type("_".join(args[0].split('_')[:-1]) + "_")
            if await change_asset(client, message.author.id, type_, args[0]) is False:
                await reply(message, "ロックされています")
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'アイテム情報の設定リクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0].lower().startswith('playlist_'):
        try:
            await client.user.party.set_playlist(args[0])
            await reply(message, f'プレイリストを {args[0]} に設定')
            data['fortnite']['playlist']=args[0]
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'パーティーリーダーではありません')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    else:
        if ': ' in message.content:
            return
        if args[0].isdigit() and client.select.get(message.author.id) is not None:
            try:
                if int(args[0]) == 0:
                    await reply(message, '有効な数字を入力してください')
                    return
                exec_ = client.select[message.author.id]["exec"][int(args[0])-1]
                variable=globals()
                variable.update(locals())
                if client.select[message.author.id].get("variable") is not None:
                    variable.update(client.select[message.author.id]["variable"][int(args[0])-1])
                await aexec(exec_, variable)
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, '有効な数字を入力してください')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')
        else:
            result = await loop.run_in_executor(None, search_item, "ja", "name", content, "item")
            if result is None:
                result = await loop.run_in_executor(None, search_item, "en", "name", content, "item")
            if result is not None:
                if len(result) > 30:
                    await reply(message, f"見つかったアイテム数 {len(result)} は多すぎます")
                    return
                if len(result) == 1:
                    if await change_asset(client, message.author.id, result[0]["type"], result[0]['id']) is True:
                        await reply(message, f"{result[0]['shortDescription']}: {result[0]['name']} | {result[0]['id']}")
                    else:
                        await reply(message, "ロックされています")
                else:
                    text = str()
                    for count, item in enumerate(result):
                        text += f"\n{count+1} {item['shortDescription']}: {item['name']} | {item['id']}"
                    text += "\n数字を入力することでそのアイテムに設定します"
                    await reply(message, text)
                    client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{item['type']}', '{item['id']}')" for item in result]}

#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================

dclient=discord.Client()
dclient.isready=False
dclient.owner=None
if data['discord']['enabled'] is True:
    @dclient.event
    async def on_ready():
        global blacklist_
        global whitelist_
        dclient_user = str(dclient.user)
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(green(f'[{now_()}] ログイン: {dclient_user}'))
            dstore(dclient_user,f'ログイン: {dclient_user}')
        else:
            if data['no-logs'] is False:
                print(green(f'[{now_()}] ログイン: {dclient_user} / {dclient.user.id}'))
            dstore(dclient_user,f'ログイン: {dclient_user} / {dclient.user.id}')
        dclient.isready = True
        activity = discord.Game(name=data['discord']['status'])
        await dclient.change_presence(activity=activity)

        for blacklistuser in data['discord']['blacklist']:
            user = dclient.get_user(blacklistuser)
            if user is None:
                try:
                    user = await dclient.fetch_user(blacklistuser)
                except discord.NotFound:
                    if data['loglevel'] == "debug":
                        print(red(traceback.format_exc()))
                        dstore(dclient_user,f'>>> {traceback.format_exc()}')
                    user = None
            if user is None:
                print(red(f'[{now_()}] [{dclient_user}] ブラックリストのユーザー {blacklistuser} が見つかりません。正しいIDになっているか確認してください。'))
                dstore(dclient_user,f'>>>ブラックリストのユーザー {blacklistuser} が見つかりません。正しいIDになっているか確認してください')
            else:
                blacklist_.append(user.id)
                if data['loglevel'] == 'debug':
                    print(yellow(f"{user} / {user.id}"))
        if data['loglevel'] == "debug":
            print(yellow(blacklist_))
        for whitelistuser in data['discord']['whitelist']:
            user = dclient.get_user(whitelistuser)
            if user is None:
                try:
                    user = await dclient.fetch_user(whitelistuser)
                except discord.NotFound:
                    if data['loglevel'] == "debug":
                        print(red(traceback.format_exc()))
                        dstore(dclient_user,f'>>> {traceback.format_exc()}')
                    user = None
            if user is None:
                print(red(f'[{now_()}] [{dclient_user}] ホワイトリストのユーザー {whitelistuser} が見つかりません。正しいIDになっているか確認してください。'))
                dstore(dclient_user,f'>>>ホワイトリストのユーザー {whitelistuser} が見つかりません。正しいIDになっているか確認してください')
            else:
                whitelist_.append(user.id)
                if data['loglevel'] == 'debug':
                    print(yellow(f"{user.display_name} / {user.id}"))
        if data['loglevel'] == "debug":
            print(yellow(whitelist_))

        try:
            dclient.owner=None
            owner=dclient.get_user(data['discord']['owner'])
            if owner is None:
                try:
                    owner=await dclient.fetch_user(data['discord']['owner'])
                except discord.NotFound:
                    if data['loglevel'] == "debug":
                        print(red(traceback.format_exc()))
                        dstore(dclient_user,f'>>> {traceback.format_exc()}')
                    owner = None
            if owner is None:
                print(red(f'[{now_()}] [{dclient_user}] 所有者が見つかりません。正しいIDになっているか確認してください。'))
                dstore(dclient_user,'>>> 所有者が見つかりません。正しいIDになっているか確認してください')
            else:
                dclient.owner=owner
                if data['loglevel'] == 'normal':
                    if data['no-logs'] is False:
                        print(green(f'[{now_()}] [{dclient_user}] 所有者: {dclient.owner}'))
                    dstore(dclient_user,f'所有者: {dclient.owner}')
                else:
                    if data['no-logs'] is False:
                        print(green(f'[{now_()}] [{dclient_user}] 所有者: {dclient.owner} / {dclient.owner.id}'))
                    dstore(dclient_user,f'所有者: {dclient.owner} / {dclient.owner.id}')
        except discord.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(dclient_user,f'>>> {traceback.format_exc()}')
            print(red(f'[{now_()}] [{dclient_user}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
            dstore(dclient_user,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(dclient_user,f'>>> {traceback.format_exc()}')

    @dclient.event
    async def on_message(message):
        global blacklist
        global whitelist
        global blacklist_
        global whitelist_
        global kill
        if message.author == dclient.user:
            return
        for clientname, client in client_name.items():
            if client.isready is False:
                continue
            if message.channel.name == data['discord']['channelname'].format(name=clientname, id=client.user.id).replace(" ","-").lower():
                break
        else:
            return
        if data['discord']['enabled'] is True and dclient.isready is False:
            return
        if client.isready is False:
            return
        name=client.user.display_name
        author_id = message.author.id
        loop = asyncio.get_event_loop()
        if message.author.id in blacklist_ and data['discord']['blacklist-ignorecommand'] is True:
            return
        if isinstance(message.channel, discord.TextChannel) is False:
            return
        if not dclient.owner is None:
            if client.discord is False:
                if client.discordperfect is True:
                    return
                elif not message.author.id == dclient.owner.id:
                    return
        else:
            if client.discord is False:
                return
        content=message.content
        if data['caseinsensitive'] is True:
            args = jaconv.kata2hira(content.lower()).split()
        else:
            args = content.split()
        rawargs = content.split()
        rawcontent = ' '.join(rawargs[1:])
        rawcontent2 = ' '.join(rawargs[2:])
        if dclient.owner is not None:
            if client.discord is False:
                if client.discordperfect is True:
                    return
                elif message.author.id != dclient.owner.id and message.author.id not in whitelist_:
                    return
        else:
            if client.discord is False:
                if message.author.id not in whitelist_:
                    return
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(f'[{now_()}] [{dclient.user}] {message.author} | {content}')
            dstore(message.author,content)
        else:
            if data['no-logs'] is False:
                print(f'[{now_()}] [{dclient.user}] {message.author} / {message.author.id} | {content}')
            dstore(f'{message.author} / {message.author.id}',content)
        
        flag = False
        if isinstance(message, fortnitepy.message.MessageBase) is True:
            if client.owner is not None:
                if data['fortnite']['whitelist-ownercommand'] is True:
                    if client.owner.id != message.author.id and message.author.id not in whitelist:
                        flag = True
                else:
                    if client.owner.id != message.author.id:
                        flag = True
            else:
                if data['fortnite']['whitelist-ownercommand'] is True:
                    if message.author.id not in whitelist:
                        flag = True
                else:
                    flag = True
        else:
            if dclient.owner is not None:
                if data['discord']['whitelist-ownercommand'] is True:
                    if client.owner.id != message.author.id and message.author.id not in whitelist_:
                        flag = True
                else:
                    if client.owner.id != message.author.id:
                        flag = True
            else:
                if data['discord']['whitelist-ownercommand'] is True:
                    if message.author.id not in whitelist_:
                        flag = True
                else:
                    flag = True
        if flag is True:
            for checks in commands.items():
                if checks[0] in ignore:
                    continue
                if commands['ownercommands'] == '':
                    break
                for command in commands['ownercommands'].split(','):
                    if args[0] in commands[command.lower()].split(','):
                        await reply(message, 'このコマンドは管理者しか使用できません')
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
            if args[0] in key.split(','):
                try:
                    await reply(message, value)
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'エラー')
                return

        if data['discord']['enabled'] is True and dclient.isready is True:
            if args[0] in commands['addblacklist_discord'].split(','):
                try:
                    if rawcontent == '' or args[1].isdigit() is False:
                        await reply(message, f"[{commands['addblacklist_discord']}] [ユーザーID]")
                        return
                    user = dclient.get_user(int(args[1]))
                    if user is None:
                        user = await dclient.fetch_user(int(args[1]))
                    if user.id not in blacklist_:
                        blacklist_.append(user.id)
                        data["discord"]["blacklist"].append(user.id)
                        try:
                            with open("config.json", "r", encoding="utf-8") as f:
                                data_ = json.load(f)
                        except json.decoder.JSONDecodeError:
                            with open("config.json", "r", encoding="utf-8-sig") as f:
                                data_ = json.load(f)
                        data_["discord"]["blacklist"] = data["discord"]["blacklist"]
                        with open("config.json", "w", encoding="utf-8") as f:
                            json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                        await reply(message, f"ユーザー {user} / {user.id} をブラックリストに追加しました")
                    else:
                        await reply(message, f"ユーザー {user} / {user.id} は既にブラックリストに追加されています")
                except discord.NotFound:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'ユーザーが見つかりません')
                except discord.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
                    dstore(name,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
                    await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました。')
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'エラー')

            elif args[0] in commands['removeblacklist_discord'].split(','):
                try:
                    if rawcontent == '' or args[1].isdigit() is False:
                        await reply(message, f"[{commands['removeblacklist_discord']}] [ユーザーID]")
                        return
                    user = dclient.get_user(int(args[1]))
                    if user is None:
                        user = await dclient.fetch_user(int(args[1]))
                    if user.id in blacklist_:
                        blacklist_.remove(user.id)
                        data["discord"]["blacklist"].remove(user.id)
                        try:
                            with open("config.json", "r", encoding="utf-8") as f:
                                data_ = json.load(f)
                        except json.decoder.JSONDecodeError:
                            with open("config.json", "r", encoding="utf-8-sig") as f:
                                data_ = json.load(f)
                        data_["discord"]["blacklist"] = data["discord"]["blacklist"]
                        with open("config.json", "w", encoding="utf-8") as f:
                            json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                        await reply(message, f"ユーザー {user} / {user.id} をブラックリストから削除")
                    else:
                        await reply(message, f"ユーザー {user} / {user.id} はブラックリストに含まれていません")
                except discord.NotFound:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'ユーザーが見つかりません')
                except discord.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
                    dstore(name,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
                    await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました。')
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'エラー')

            elif args[0] in commands['addwhitelist_discord'].split(','):
                try:
                    if rawcontent == '' or args[1].isdigit() is False:
                        await reply(message, f"[{commands['addwhitelist_discord']}] [ユーザーID]")
                        return
                    user = dclient.get_user(int(args[1]))
                    if user is None:
                        user = await dclient.fetch_user(int(args[1]))
                    if user.id not in whitelist_:
                        whitelist_.append(user.id)
                        data["discord"]["whitelist"].append(user.id)
                        try:
                            with open("config.json", "r", encoding="utf-8") as f:
                                data_ = json.load(f)
                        except json.decoder.JSONDecodeError:
                            with open("config.json", "r", encoding="utf-8-sig") as f:
                                data_ = json.load(f)
                        data_["discord"]["whitelist"] = data["discord"]["whitelist"]
                        with open("config.json", "w", encoding="utf-8") as f:
                            json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                        await reply(message, f"ユーザー {user} / {user.id} をホワイトリストに追加しました")
                    else:
                        await reply(message, f"ユーザー {user} / {user.id} は既にホワイトリストに追加されています")
                except discord.NotFound:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'ユーザーが見つかりません')
                except discord.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
                    dstore(name,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
                    await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました。')
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'エラー')

            elif args[0] in commands['removewhitelist_discord'].split(','):
                try:
                    if rawcontent == '' or args[1].isdigit() is False:
                        await reply(message, f"[{commands['removewhitelist_discord']}] [ユーザーID]")
                        return
                    user = dclient.get_user(int(args[1]))
                    if user is None:
                        user = await dclient.fetch_user(int(args[1]))
                    if user.id in whitelist_:
                        whitelist_.remove(user.id)
                        data["discord"]["whitelist"].remove(user.id)
                        try:
                            with open("config.json", "r", encoding="utf-8") as f:
                                data_ = json.load(f)
                        except json.decoder.JSONDecodeError:
                            with open("config.json", "r", encoding="utf-8-sig") as f:
                                data_ = json.load(f)
                        data_["discord"]["whitelist"] = data["discord"]["whitelist"]
                        with open("config.json", "w", encoding="utf-8") as f:
                            json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                        await reply(message, f"ユーザー {user} / {user.id} をホワイトリストから削除")
                    else:
                        await reply(message, f"ユーザー {user} / {user.id} はホワイトリストに含まれていません")
                except discord.NotFound:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'ユーザーが見つかりません')
                except discord.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
                    dstore(name,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
                    await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました。')
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'エラー')

        if args[0] in commands['eval'].split(','):
            try:
                if rawcontent == "":
                    await reply(message, f"[{commands['eval']}] [式]")
                    return
                variable=globals()
                variable.update(locals())
                if rawcontent.startswith("await "):
                    if data['loglevel'] == "debug":
                        print(f"await eval({rawcontent.replace('await ','',1)})")
                    result = await eval(rawcontent.replace("await ","",1), variable)
                    await reply(message, str(result))
                else:
                    if data['loglevel'] == "debug":
                        print(f"eval {rawcontent}")
                    result = eval(rawcontent, variable)
                    await reply(message, str(result))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['exec'].split(','):
            try:
                if rawcontent == "":
                    await reply(message, f"[{commands['exec']}] [文]")
                    return
                variable=globals()
                variable.update(locals())
                args_=[i.replace("\\nn", "\n") for i in content.replace("\n", "\\nn").split()]
                content_=" ".join(args_[1:])
                result = await aexec(content_, variable)
                await reply(message, str(result))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['restart'].split(','):
            try:
                flag = False
                if client.acceptinvite is False:
                    if isinstance(message, fortnitepy.message.MessageBase) is True:
                        if client.owner is not None:
                            if data['fortnite']['whitelist-ownercommand'] is True:
                                if client.owner.id != message.author.id and message.author.id not in whitelist:
                                    flag = True
                            else:
                                if client.owner.id != message.author.id:
                                    flag = True
                        else:
                            if data['fortnite']['whitelist-ownercommand'] is True:
                                if message.author.id not in whitelist:
                                    flag = True
                            else:
                                flag = True
                    elif isinstance(message, discord.Message) is True:
                        if dclient.owner is not None:
                            if data['discord']['whitelist-ownercommand'] is True:
                                if dclient.owner.id != message.author.id and message.author.id not in whitelist_:
                                    flag = True
                            else:
                                if dclient.owner.id != message.author.id:
                                    flag = True
                        else:
                            if data['discord']['whitelist-ownercommand'] is True:
                                if message.author.id not in whitelist_:
                                    flag = True
                            else:
                                flag = True
                if flag is True:
                    await reply(message, '招待が拒否に設定されているので実行できません')
                    return
                await reply(message, 'プログラムを再起動します...')
                os.chdir(os.getcwd())
                os.execv(os.sys.executable,['python','index.py'])
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['relogin'].split(','):
            try:
                flag = False
                if client.acceptinvite is False:
                    if isinstance(message, fortnitepy.message.MessageBase) is True:
                        if client.owner is not None:
                            if data['fortnite']['whitelist-ownercommand'] is True:
                                if client.owner.id != message.author.id and message.author.id not in whitelist:
                                    flag = True
                            else:
                                if client.owner.id != message.author.id:
                                    flag = True
                        else:
                            if data['fortnite']['whitelist-ownercommand'] is True:
                                if message.author.id not in whitelist:
                                    flag = True
                            else:
                                flag = True
                    elif isinstance(message, discord.Message) is True:
                        if dclient.owner is not None:
                            if data['discord']['whitelist-ownercommand'] is True:
                                if dclient.owner.id != message.author.id and message.author.id not in whitelist_:
                                    flag = True
                            else:
                                if dclient.owner.id != message.author.id:
                                    flag = True
                        else:
                            if data['discord']['whitelist-ownercommand'] is True:
                                if message.author.id not in whitelist_:
                                    flag = True
                            else:
                                flag = True
                if flag is True:
                    await reply(message, '招待が拒否に設定されているので実行できません')
                    return
                await reply(message, 'アカウントに再ログインします...')
                await client.restart()
            except fortnitepy.AuthException:
                print(red(traceback.format_exc()))
                print(red(f'[{now_()}] [{client.user.display_name}] メールアドレスまたはパスワードが間違っています。'))
                dstore(name,f'>>> {traceback.format_exc()}')
                dstore(name,f'>>> メールアドレスまたはパスワードが間違っています')
                kill=True
                exit()
            except Exception:
                print(red(traceback.format_exc()))
                print(red(f'[{now_()}] [{client.user.display_name}] アカウントの読み込みに失敗しました。もう一度試してみてください。'))
                dstore(name,f'>>> {traceback.format_exc()}')
                dstore(name,f'>>> アカウントの読み込みに失敗しました。もう一度試してみてください')
                kill=True
                exit()

        elif args[0] in commands['reload'].split(','):
            result=reload_configs(client)
            try:
                if result == 'Success':
                    await reply(message, '正常に読み込みが完了しました')
                else:
                    await reply(message, 'エラー')
                    return
                try:
                    client.owner=None
                    owner=await client.fetch_profile(data['fortnite']['owner'])
                    if owner is None:
                        print(red(f'[{now_()}] [{client.user.display_name}] 所有者が見つかりません。正しい名前/IDになっているか確認してください。'))
                        dstore(client.user.display_name,'>>> 所有者が見つかりません。正しい名前/IDになっているか確認してください')
                    else:
                        add_cache(client, owner)
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

                for blacklistuser in data['fortnite']['blacklist']:
                    try:
                        user = await client.fetch_profile(blacklistuser)
                        add_cache(client, user)
                        if user is None:
                            print(red(f'[{now_()}] [{client.user.display_name}] ブラックリストのユーザー {blacklistuser} が見つかりません。正しい名前/IDになっているか確認してください。'))
                            dstore(client.user.display_name,f'>>>ブラックリストのユーザー {blacklistuser} が見つかりません。正しい名前/IDになっているか確認してください')
                        else:
                            blacklist.append(user.id)
                            if data['loglevel'] == 'debug':
                                print(yellow(f"{str(user.display_name)} / {user.id}"))
                            if data['fortnite']['blacklist-autoblock'] is True:
                                try:
                                    await user.block()
                                except Exception:
                                    if data['loglevel'] == 'debug':
                                        print(red(traceback.format_exc()))
                                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                        print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
                        dstore(client.user.display_name,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                if data['loglevel'] == "debug":
                    print(yellow(blacklist))
                for whitelistuser in data['fortnite']['whitelist']:
                    try:
                        user = await client.fetch_profile(whitelistuser)
                        add_cache(client, user)
                        if user is None:
                            print(red(f'[{now_()}] [{client.user.display_name}] ホワイトリストのユーザー {whitelistuser} が見つかりません。正しい名前/IDになっているか確認してください。'))
                            dstore(client.user.display_name,f'>>>ホワイトリストのユーザー {whitelistuser} が見つかりません。正しい名前/IDになっているか確認してください')
                        else:
                            whitelist.append(user.id)
                            if data['loglevel'] == 'debug':
                                print(yellow(f"{str(user.display_name)} / {user.id}"))
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                        print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
                        dstore(client.user.display_name,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                if data['loglevel'] == "debug":
                    print(yellow(whitelist))

                for invitelistuser in data['fortnite']['invitelist']:
                    try:
                        user = await client.fetch_profile(invitelistuser)
                        if user is None:
                            print(red(f'[{now_()}] [{client.user.display_name}] 招待リストのユーザー {invitelistuser} が見つかりません。正しい名前/IDになっているか確認してください。'))
                            dstore(client.user.display_name,f'>>>招待リストのユーザー {invitelistuser} が見つかりません。正しい名前/IDになっているか確認してください')
                        else:
                            friend = client.get_friend(user.id)
                            if friend is None and user.id != client.user.id:
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
                                print(red(f"[{now_()}] [{client.user.display_name}] 招待リストのユーザー {invitelistuser} とフレンドではありません。フレンドになってからもう一度起動するか、[{commands['reload']}] コマンドで再読み込みしてください。"))
                                dstore(client.user.display_name,f'>>> 招待リストのユーザー {invitelistuser} とフレンドではありません。フレンドになってからもう一度起動するか、[{commands["reload"]}] コマンドで再読み込みしてください')
                            else:
                                add_cache(client, user)
                                client.invitelist.append(user.id)
                                if data['loglevel'] == 'debug':
                                    print(yellow(f"{str(user.display_name)} / {user.id}"))
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                        print(red(f'[{now_()}] [{client.user.display_name}] ユーザー情報のリクエストを処理中にエラーが発生しました。'))
                        dstore(client.user.display_name,f'>>> ユーザー情報のリクエストを処理中にエラーが発生しました')
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                if data['loglevel'] == "debug":
                    print(yellow(client.invitelist))
                if data['discord']['enabled'] is True:
                    dclient_user = str(dclient.user)
                    activity = discord.Game(name=data['discord']['status'])
                    await dclient.change_presence(activity=activity)

                    for blacklistuser in data['discord']['blacklist']:
                        user = dclient.get_user(blacklistuser)
                        if user is None:
                            try:
                                user = await dclient.fetch_user(blacklistuser)
                            except discord.NotFound:
                                if data['loglevel'] == "debug":
                                    print(red(traceback.format_exc()))
                                    dstore(dclient_user,f'>>> {traceback.format_exc()}')
                                user = None
                        if user is None:
                            print(red(f'[{now_()}] [{dclient_user}] ブラックリストのユーザー {blacklistuser} が見つかりません。正しいIDになっているか確認してください。'))
                            dstore(dclient_user,f'>>>ブラックリストのユーザー {blacklistuser} が見つかりません。正しいIDになっているか確認してください')
                        else:
                            blacklist_.append(user.id)
                            if data['loglevel'] == 'debug':
                                print(yellow(f"{user} / {user.id}"))
                    if data['loglevel'] == "debug":
                        print(yellow(blacklist_))
                    for whitelistuser in data['discord']['whitelist']:
                        user = dclient.get_user(whitelistuser)
                        if user is None:
                            try:
                                user = await dclient.fetch_user(whitelistuser)
                            except discord.NotFound:
                                if data['loglevel'] == "debug":
                                    print(red(traceback.format_exc()))
                                    dstore(dclient_user,f'>>> {traceback.format_exc()}')
                                user = None
                        if user is None:
                            print(red(f'[{now_()}] [{dclient_user}] ホワイトリストのユーザー {whitelistuser} が見つかりません。正しいIDになっているか確認してください。'))
                            dstore(dclient_user,f'>>>ホワイトリストのユーザー {whitelistuser} が見つかりません。正しいIDになっているか確認してください')
                        else:
                            whitelist_.append(user.id)
                            if data['loglevel'] == 'debug':
                                print(yellow(f"{user.display_name} / {user.id}"))
                    if data['loglevel'] == "debug":
                        print(yellow(whitelist_))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['addblacklist'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['addblacklist']}] [ユーザー名/ユーザーID]")
                    return
                users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and user.id not in blacklist}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.display_name is not None and user.id not in blacklist:
                            users[user.display_name] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
                if len(users) > 30:
                    await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                    return
                if len(users) == 0:
                    await reply(message, 'ユーザーが見つかりません')
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if user.id not in blacklist:
                        blacklist.append(user.id)
                        if user.display_name is not None:
                            data["fortnite"]["blacklist"].append(user.display_name)
                        else:
                            data["fortnite"]["blacklist"].append(user.id)
                        try:
                            with open("config.json", "r", encoding="utf-8") as f:
                                data_ = json.load(f)
                        except json.decoder.JSONDecodeError:
                            with open("config.json", "r", encoding="utf-8-sig") as f:
                                data_ = json.load(f)
                        data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
                        with open("config.json", "w", encoding="utf-8") as f:
                            json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                        await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をブラックリストに追加しました")
                    else:
                        await reply(message, f"ユーザー {str(user.display_name)} / {user.id} は既にブラックリストに追加されています")
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            if user.id not in blacklist:
                blacklist.append(user.id)
                if user.display_name is not None:
                    data["fortnite"]["blacklist"].append(user.display_name)
                else:
                    data["fortnite"]["blacklist"].append(user.id)
                try:
                    with open("config.json", "r", encoding="utf-8") as f:
                        data_ = json.load(f)
                except json.decoder.JSONDecodeError:
                    with open("config.json", "r", encoding="utf-8-sig") as f:
                        data_ = json.load(f)
                data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
                with open("config.json", "w", encoding="utf-8") as f:
                    json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をブラックリストに追加しました")
            else:
                await reply(message, f"ユーザー {str(user.display_name)} / {user.id} は既にブラックリストに追加されています")""" for name, user in users.items()
                        ],
                        "variable": [
                            {"user": user} for name, user in users.items()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {user.display_name} / {user.id}"
                    text += "\n数字を入力することでそのユーザーをブラックリストに追加します"
                    await reply(message, text)
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['removeblacklist'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['removeblacklist']}] [ユーザー名/ユーザーID]")
                    return
                users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and user.id in blacklist}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.display_name is not None and user.id in blacklist:
                            users[user.display_name] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
                if len(users) > 30:
                    await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                    return
                if len(users) == 0:
                    await reply(message, 'ユーザーが見つかりません')
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if user.id in blacklist:
                        blacklist.remove(user.id)
                        try:
                            data["fortnite"]["blacklist"].remove(user.display_name)
                        except ValueError:
                            data["fortnite"]["blacklist"].remove(user.id)
                        try:
                            with open("config.json", "r", encoding="utf-8") as f:
                                data_ = json.load(f)
                        except json.decoder.JSONDecodeError:
                            with open("config.json", "r", encoding="utf-8-sig") as f:
                                data_ = json.load(f)
                        data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
                        with open("config.json", "w", encoding="utf-8") as f:
                            json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                        await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をブラックリストから削除")
                    else:
                        await reply(message, f"ユーザー {str(user.display_name)} / {user.id} はブラックリストに含まれていません")
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            if user.id in blacklist:
                blacklist.remove(user.id)
                try:
                    data["fortnite"]["blacklist"].remove(user.display_name)
                except ValueError:
                    data["fortnite"]["blacklist"].remove(user.id)
                try:
                    with open("config.json", "r", encoding="utf-8") as f:
                        data_ = json.load(f)
                except json.decoder.JSONDecodeError:
                    with open("config.json", "r", encoding="utf-8-sig") as f:
                        data_ = json.load(f)
                data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
                with open("config.json", "w", encoding="utf-8") as f:
                    json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をブラックリストから削除")
            else:
                await reply(message, f"ユーザー {str(user.display_name)} / {user.id} はブラックリストに含まれていません")""" for name, user in users.items()
                        ],
                        "variable": [
                            {"user": user} for name, user in users.items()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {user.display_name} / {user.id}"
                    text += "\n数字を入力することでそのユーザーをブラックリストから削除します"
                    await reply(message, text)
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['addwhitelist'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['addwhitelist']}] [ユーザー名/ユーザーID]")
                    return
                users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and user.id not in whitelist}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.display_name is not None and user.id not in whitelist:
                            users[user.display_name] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
                if len(users) > 30:
                    await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                    return
                if len(users) == 0:
                    await reply(message, 'ユーザーが見つかりません')
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if user.id not in whitelist:
                        whitelist.append(user.id)
                        if user.display_name is not None:
                            data["fortnite"]["whitelist"].append(user.display_name)
                        else:
                            data["fortnite"]["whitelist"].append(user.id)
                        try:
                            with open("config.json", "r", encoding="utf-8") as f:
                                data_ = json.load(f)
                        except json.decoder.JSONDecodeError:
                            with open("config.json", "r", encoding="utf-8-sig") as f:
                                data_ = json.load(f)
                        data_["fortnite"]["whitelist"] = data["fortnite"]["whitelist"]
                        with open("config.json", "w", encoding="utf-8") as f:
                            json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                        await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をホワイトリストに追加しました")
                    else:
                        await reply(message, f"ユーザー {str(user.display_name)} / {user.id} は既にホワイトリストに追加されています")
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            if user.id not in whitelist:
                whitelist.append(user.id)
                if user.display_name is not None:
                    data["fortnite"]["whitelist"].append(user.display_name)
                else:
                    data["fortnite"]["whitelist"].append(user.id)
                try:
                    with open("config.json", "r", encoding="utf-8") as f:
                        data_ = json.load(f)
                except json.decoder.JSONDecodeError:
                    with open("config.json", "r", encoding="utf-8-sig") as f:
                        data_ = json.load(f)
                data_["fortnite"]["whitelist"] = data["fortnite"]["whitelist"]
                with open("config.json", "w", encoding="utf-8") as f:
                    json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をホワイトリストに追加しました")
            else:
                await reply(message, f"ユーザー {str(user.display_name)} / {user.id} は既にホワイトリストに追加されています")""" for name, user in users.items()
                        ],
                        "variable": [
                            {"user": user} for name, user in users.items()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {user.display_name} / {user.id}"
                    text += "\n数字を入力することでそのユーザーをホワイトリストに追加します"
                    await reply(message, text)
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['removewhitelist'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['removewhitelist']}] [ユーザー名/ユーザーID]")
                    return
                users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and user.id in whitelist}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.display_name is not None and user.id in whitelist:
                            users[user.display_name] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
                if len(users) > 30:
                    await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                    return
                if len(users) == 0:
                    await reply(message, 'ユーザーが見つかりません')
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if user.id in whitelist:
                        whitelist.remove(user.id)
                        try:
                            data["whitelist"].remove(user.display_name)
                        except ValueError:
                            data["whitelist"].remove(user.id)
                        try:
                            with open("config.json", "r", encoding="utf-8") as f:
                                data_ = json.load(f)
                        except json.decoder.JSONDecodeError:
                            with open("config.json", "r", encoding="utf-8-sig") as f:
                                data_ = json.load(f)
                        data_["whitelist"] = data["whitelist"]
                        with open("config.json", "w", encoding="utf-8") as f:
                            json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                        await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をホワイトリストから削除")
                    else:
                        await reply(message, f"ユーザー {str(user.display_name)} / {user.id} はホワイトリストに含まれていません")
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            if user.display_name in data["blacklist"] or user.id in data["blacklist"]:
                blacklist.remove(user.id)
                try:
                    data["blacklist"].remove(user.display_name)
                except ValueError:
                    data["blacklist"].remove(user.id)
                try:
                    with open("config.json", "r", encoding="utf-8") as f:
                        data_ = json.load(f)
                except json.decoder.JSONDecodeError:
                    with open("config.json", "r", encoding="utf-8-sig") as f:
                        data_ = json.load(f)
                data_["blacklist"] = data["blacklist"]
                with open("config.json", "w", encoding="utf-8") as f:
                    json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をブラックリストから削除")
            else:
                await reply(message, f"ユーザー {str(user.display_name)} / {user.id} はブラックリストに含まれていません")""" for name, user in users.items()
                        ],
                        "variable": [
                            {"user": user} for name, user in users.items()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {user.display_name} / {user.id}"
                    text += "\n数字を入力することでそのユーザーをホワイトリストから削除します"
                    await reply(message, text)
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['get'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['get']}] [ユーザー名/ユーザーID]")
                    return
                users = {member.display_name: member for member in client.user.party.members.values() if rawcontent.lower() in member.display_name.lower() and member.display_name is not None}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.display_name is not None and client.user.party.members.get(user.id) is not None:
                            users[user.display_name] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
                if len(users) > 30:
                    await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                    return
                if len(users) == 0:
                    await reply(message, 'ユーザーが見つかりません')
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    member=client.user.party.members.get(user.id)
                    if member is None:
                        await reply(message, "ユーザーがパーティーにいません")
                        return
                    if data['no-logs'] is False:
                        print(f'{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}')
                    if data['loglevel'] == 'debug':
                        print(json.dumps(member.meta.schema, indent=2))
                    dstore(name,f'{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}')
                    await reply(message, f'{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}')
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            member=client.user.party.members.get(user.id)
            if member is None:
                await reply(message, "ユーザーがパーティーにいません")
                return
            if data['no-logs'] is False:
                print(f'''{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}''')
            if data['loglevel'] == 'debug':
                print(json.dumps(member.meta.schema, indent=2))
            dstore(name,f'''{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}''')
            await reply(message, f'''{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}''')""" for name, user in users.items()
                        ],
                        "variable": [
                            {"user": user} for name, user in users.items()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {user.display_name} / {user.id}"
                    text += "\n数字を入力することでそのユーザーの情報を取得します"
                    await reply(message, text)
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['friendcount'].split(','):
            try:
                if data['no-logs'] is False:
                    print(f'フレンド数: {len(client.friends)}')
                dstore(name,f'フレンド数: {len(client.friends)}')
                await reply(message, f'フレンド数: {len(client.friends)}')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

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
                dstore(name,f'保留数: {len(client.pending_friends)}\n送信: {len(outbound)}\n受信: {len(inbound)}')
                await reply(message, f'保留数: {len(client.pending_friends)}\n送信: {len(outbound)}\n受信: {len(inbound)}')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['blockcount'].split(','):
            try:
                if data['no-logs'] is False:
                    print(f'ブロック数: {len(client.blocked_users)}')
                dstore(name,f'ブロック数: {len(client.blocked_users)}')
                await reply(message, f'ブロック数: {len(client.blocked_users)}')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['friendlist'].split(','):
            try:
                text=''
                for friend in client.friends.values():
                    add_cache(client, friend)
                    text+=f'\n{friend}'
                if data['no-logs'] is False:
                    print(f'{text}')
                dstore(name,f'{text}')
                await reply(message, f'{text}')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['pendinglist'].split(','):
            try:
                outbound=''
                inbound=''
                for pending in client.pending_friends.values():
                    add_cache(client, pending)
                    if pending.direction == 'OUTBOUND':
                        outbound+=f'\n{pending}'
                    elif pending.direction == 'INBOUND':
                        inbound+=f'\n{pending}'
                if data['no-logs'] is False:
                    print(f'送信: {outbound}\n受信: {inbound}')
                dstore(name,f'送信: {outbound}\n受信: {inbound}')
                await reply(message, f'送信: {outbound}\n受信: {inbound}')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['blocklist'].split(','):
            try:
                text=''
                for block in client.blocked_users.values():
                    add_cache(client, block)
                    text+=f'\n{block}'
                if data['no-logs'] is False:
                    print(f'{text}')
                dstore(name,f'{text}')
                await reply(message, f'{text}')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['outfitmimic'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.outfitmimic=True
                    await reply(message, 'コスチュームミミックをオンに設定')
                elif args[1] in commands['false'].split(','):
                    client.outfitmimic=False
                    await reply(message, 'コスチュームミミックをオフに設定')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['skinmimic']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['backpackmimic'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.backpackmimic=True
                    await reply(message, 'バックアクセサリーミミックをオンに設定')
                elif args[1] in commands['false'].split(','):
                    client.backpackmimic=False
                    await reply(message, 'バックアクセサリーミミックをオフに設定')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['skinmimic']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['pickaxemimic'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.pickaxemimic=True
                    await reply(message, '収集ツールミミックをオンに設定')
                elif args[1] in commands['false'].split(','):
                    client.pickaxemimic=False
                    await reply(message, '収集ツールミミックをオフに設定')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['skinmimic']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['emotemimic'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.emotemimic=True
                    await reply(message, 'エモートミミックをオンに設定')
                elif args[1] in commands['false'].split(','):
                    client.emotemimic=False
                    await reply(message, 'エモートミミックをオフに設定')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['emotemimic']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['whisper'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.whisper=True
                    await reply(message, '囁きからのコマンド受付をオンに設定')
                elif args[1] in commands['false'].split(','):
                    client.whisper=False
                    await reply(message, '囁きからのコマンド受付をオフに設定')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['whisper']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['partychat'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.partychat=True
                    await reply(message, 'パーティーチャットからのコマンド受付をオンに設定')
                elif args[1] in commands['false'].split(','):
                    client.partychat=False
                    await reply(message, 'パーティーチャットからのコマンド受付をオフに設定')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['party']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['discord'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.discord=True
                    await reply(message, 'Discordからのコマンド受付をオンに設定')
                elif args[1] in commands['false'].split(','):
                    client.discord=False
                    await reply(message, 'Discordからのコマンド受付をオフに設定')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['discord']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['disablewhisperperfectly'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.whisperperfect=True
                    await reply(message, '囁きの完全無効をオンに設定')
                elif args[1] in commands['false'].split(','):
                    client.whisperperfect=False
                    await reply(message, '囁きの完全無効をオフに設定')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['disablewhisperperfectly']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['disablepartychatperfectly'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.partychatperfect=True
                    await reply(message, 'パーティーチャットの完全無効をオンに設定')
                elif args[1] in commands['false'].split(','):
                    client.partychatperfect=False
                    await reply(message, 'パーティーチャットの完全無効をオフに設定')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['disablepartychatperfectly']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['disablediscordperfectly'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.discordperfect=True
                    await reply(message, 'Discordの完全無効をオンに設定')
                elif args[1] in commands['false'].split(','):
                    client.discordperfect=False
                    await reply(message, 'Discordの完全無効をオフに設定')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['disablediscordperfectly']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['acceptinvite'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.acceptinvite=True
                    await reply(message, '招待を承諾に設定')
                elif args[1] in commands['false'].split(','):
                    client.acceptinvite=False
                    await reply(message, '招待を拒否に設定')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['acceptinvite']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['acceptfriend'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.acceptfriend=True
                    await reply(message, 'フレンド申請を承諾に設定')
                elif args[1] in commands['false'].split(','):
                    client.acceptfriend=False
                    await reply(message, 'フレンド申請を拒否に設定')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['acceptfriend']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['joinmessageenable'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.joinmessageenable=True
                    await reply(message, 'パーティー参加時のメッセージをオンに設定')
                elif args[1] in commands['false'].split(','):
                    client.joinmessageenable=False
                    await reply(message, 'パーティー参加時のメッセージをオフに設定')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['joinmessageenable']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['randommessageenable'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.randommessageenable=True
                    await reply(message, 'パーティー参加時のランダムメッセージをオンに設定')
                elif args[1] in commands['false'].split(','):
                    client.randommessageenable=False
                    await reply(message, 'パーティー参加時のランダムメッセージをオフに設定')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['randommessageenable']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

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
                    await reply(message, f"{str(data['fortnite']['waitinterval'])}秒間招待を拒否します")
                else:
                    if client.owner.id in client.user.party.members.keys() and message.author.id != client.owner.id:
                        await reply(message, '現在利用できません')
                        return
                    client.acceptinvite=False
                    try:
                        client.timer_.cancel()
                    except AttributeError:
                        pass
                    client.timer_=Timer(data['fortnite']['waitinterval'], inviteaccept, [client])
                    client.timer_.start()
                    await reply(message, f"{str(data['fortnite']['waitinterval'])}秒間招待を拒否します")             
            except Exception:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['join'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['join']}] [ユーザー名/ユーザーID]")
                    return
                users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.has_friend(user.id) is True}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.display_name is not None and client.has_friend(user.id) is True:
                            users[user.display_name] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
                if len(users) > 30:
                    await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                    return
                if len(users) == 0:
                    await reply(message, 'ユーザーが見つかりません')
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    friend=client.get_friend(user.id)
                    if friend is None:
                        await reply(message, 'ユーザーとフレンドではありません')
                    else:
                        await friend.join_party()
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                friend=client.get_friend(user.id)
                if friend is None:
                    await reply(message, 'ユーザーとフレンドではありません')
                else:
                    await friend.join_party()
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'パーティーが満員か、既にパーティーにいるか、ユーザーがオフラインです')
            except fortnitepy.NotFound:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'パーティーが見つかりません')
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'パーティーがプライベートです')
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'パーティーの参加リクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                        ],
                        "variable": [
                            {"user": user} for name, user in users.items()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {user.display_name} / {user.id}"
                    text += "\n数字を入力することでそのユーザーのパーティーに参加します"
                    await reply(message, text)
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'パーティーが満員か、既にパーティーにいるか、ユーザーがオフラインです')
            except fortnitepy.NotFound:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'パーティーが見つかりません')
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'パーティーがプライベートです')
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'パーティーの参加リクエストを処理中にエラーが発生しました')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['joinid'].split(','):
            try:
                await client.join_to_party(party_id=args[1])
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, '既にこのパーティーのメンバーです')
            except fortnitepy.NotFound:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'パーティーが見つかりません')
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'パーティーがプライベートです')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['join']}] [パーティーID]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['leave'].split(','):
            try:
                await client.user.party.me.leave()
                await reply(message, 'パーティーを離脱')
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'パーティー離脱のリクエストを処理中にエラーが発生しました')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['invite'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['invite']}] [ユーザー名 / ユーザーID]")
                    return
                users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.has_friend(user.id) is True}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.display_name is not None and client.has_friend(user.id) is True:
                            users[user.display_name] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
                if len(users) > 30:
                    await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                    return
                if len(users) == 0:
                    await reply(message, 'ユーザーが見つかりません')
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    friend=client.get_friend(user.id)
                    if friend is None:
                        await reply(message, 'ユーザーとフレンドではありません')
                        return
                    await friend.invite()
                    if data['loglevel'] == 'normal':
                        await reply(message, f'{str(friend.display_name)} をパーティーに招待')
                    else:
                        await reply(message, f'{str(friend.display_name)} / {friend.id} をパーティー {client.user.party.id} に招待')
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                friend=client.get_friend(user.id)
                if friend is None:
                    await reply(message, 'ユーザーとフレンドではありません')
                    return
                await friend.invite()
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(friend.display_name)} をパーティーに招待')
                else:
                    await reply(message, f'{str(friend.display_name)} / {friend.id} をパーティー {client.user.party.id} に招待')
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'パーティーが満員か、既にパーティーにいます')
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'パーティー招待の送信リクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                        ],
                        "variable": [
                            {"user": user} for name, user in users.items()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {user.display_name} / {user.id}"
                    text += "\n数字を入力することでそのユーザーを招待します"
                    await reply(message, text)
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'パーティーが満員か、既にパーティーにいます')
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'パーティー招待の送信リクエストを処理中にエラーが発生しました')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['inviteall'].split(','):
            try:
                for inviteuser in client.invitelist:
                    if inviteuser != client.user.id:
                        try:
                            await client.user.party.invite(inviteuser)
                        except fortnitepy.PartyError:
                            if data['loglevel'] == 'debug':
                                print(red(traceback.format_exc()))
                                dstore(name,f'>>> {traceback.format_exc()}')
                            await reply(message, 'パーティーが満員か、既にパーティーにいます')
                        except fortnitepy.Forbidden:
                            if data['loglevel'] == 'debug':
                                print(red(traceback.format_exc()))
                                dstore(name,f'>>> {traceback.format_exc()}')
                            await reply(message, 'ユーザーとフレンドではありません')
                        except fortnitepy.HTTPException:
                            if data['loglevel'] == 'debug':
                                print(red(traceback.format_exc()))
                                dstore(name,f'>>> {traceback.format_exc()}')
                            await reply(message, 'パーティー招待の送信リクエストを処理中にエラーが発生しました')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['message'].split(','):
            try:
                send=rawcontent.split(' : ')
                if len(send) < 2:
                    await reply(message, f"[{commands['message']}] [ユーザー名 / ユーザーID] : [内容]")
                    return
                users = {name: user for name, user in cache_users.items() if send[0].lower() in name.lower() and user.id != client.user.id and client.has_friend(user.id) is True}
                try:
                    user=await client.fetch_profile(send[0])
                    if user is not None:
                        if user.display_name is not None and client.has_friend(user.id) is True:
                            users[user.display_name] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
                if len(users) > 30:
                    await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                    return
                if len(users) == 0:
                    await reply(message, 'ユーザーが見つかりません')
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    friend=client.get_friend(user.id)
                    if friend is None:
                        await reply(message, 'ユーザーとフレンドではありません')
                        return
                    await friend.send(send[1])
                    if data['loglevel'] == 'normal':
                        await reply(message, f'{str(friend.display_name)} にメッセージ {send[1]} を送信')
                    else:
                        await reply(message, f'{str(friend.display_name)} / {friend.id} にメッセージ {send[1]} を送信')
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                friend=client.get_friend(user.id)
                if friend is None:
                    await reply(message, 'ユーザーとフレンドではありません')
                    return
                await friend.send(send[1])
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(friend.display_name)} にメッセージ {send[1]} を送信')
                else:
                    await reply(message, f'{str(friend.display_name)} / {friend.id} にメッセージ {send[1]} を送信')
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                        ],
                        "variable": [
                            {"user": user, "send": send} for name, user in users.items()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {user.display_name} / {user.id}"
                    text += "\n数字を入力することでそのユーザーにメッセージを送信します"
                    await reply(message, text)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['message']}] [ユーザー名 / ユーザーID] : [内容]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['partymessage'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['partymessage']}] [内容]")
                    return
                await client.user.party.send(rawcontent)
                if data['loglevel'] == 'normal':
                    await reply(message, f'パーティーにメッセージ {rawcontent} を送信')
                else:
                    await reply(message, f'パーティー {client.user.party.id} にメッセージ {rawcontent} を送信')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['status'].split(','):
            try:
                await client.set_status(rawcontent)
                await reply(message, f'ステータスを {rawcontent} に設定')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['status']}] [内容]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['banner'].split(','):
            try:
                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_banner,args[1],args[2],client.user.party.me.banner[2]))
                await reply(message, f'バナーを {args[1]}, {args[2]}に設定')
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'バナー情報の設定リクエストを処理中にエラーが発生しました')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['banner']}] [バナーID] [バナーの色]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['level'].split(','):
            try:
                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_banner,client.user.party.me.banner[0],client.user.party.me.banner[1],int(args[1])))
                await reply(message, f'レベルを {args[1]} に設定')
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'レベルの設定リクエストを処理中にエラーが発生しました')
            except ValueError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, '数字を入力してください')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['level']}] [レベル]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['bp'].split(','):
            try:
                await client.user.party.me.edit_and_keep(partial(client.user.party.me.set_battlepass_info,True,args[1],args[2],args[3]))
                await reply(message, f'バトルパス情報を ティア: {args[1]} XPブースト: {args[2]} フレンドXPブースト: {args[3]} に設定')
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'バトルパス情報の設定リクエストを処理中にエラーが発生しました')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['bp']}] [ティア] [XPブースト] [フレンドXPブースト]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['privacy'].split(','):
            try:
                if args[1] in commands['privacy_public'].split(','):
                    await client.user.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)
                    await reply(message, 'プライバシーを パブリック に設定')
                elif args[1] in commands['privacy_friends_allow_friends_of_friends'].split(','):
                    await client.user.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS_ALLOW_FRIENDS_OF_FRIENDS)
                    await reply(message, 'プライバシーを フレンド(フレンドのフレンドを許可) に設定')
                elif args[1] in commands['privacy_friends'].split(','):
                    await client.user.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS)
                    await reply(message, 'プライバシーを フレンド に設定')
                elif args[1] in commands['privacy_private_allow_friends_of_friends'].split(','):
                    await client.user.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE_ALLOW_FRIENDS_OF_FRIENDS)
                    await reply(message, 'プライバシーを プライベート(フレンドのフレンドを許可) に設定')
                elif args[1] in commands['privacy_private'].split(','):
                    await client.user.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE)
                    await reply(message, 'プライバシーを プライベート に設定')
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'パーティーリーダーではありません')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['privacy']}] [[{commands['privacy_public']}] / [{commands['privacy_friends_allow_friends_of_friends']}] / [{commands['privacy_friends']}] / [{commands['privacy_private_allow_friends_of_friends']}] / [{commands['privacy_private']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー') 

        elif args[0] in commands['getuser'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['getuser']}] [ユーザー名 / ユーザーID]")
                    return
                users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.display_name is not None:
                            users[user.display_name] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
                if len(users) > 30:
                    await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                    return
                if len(users) == 0:
                    await reply(message, 'ユーザーが見つかりません')
                    return
                text = str()
                for user in users.values():
                    text += f'\n{str(user.display_name)} / {user.id}'
                if data['no-logs'] is False:
                    print(text)
                dstore(name,text)
                await reply(message, text)
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['getfriend'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['getfriend']}] [ユーザー名 / ユーザーID]")
                    return
                users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.has_friend(user.id) is True}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.display_name is not None and client.has_friend(user.id) is True:
                            users[user.display_name] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
                if len(users) > 30:
                    await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                    return
                if len(users) == 0:
                    await reply(message, 'ユーザーが見つかりません')
                    return
                text = str()
                for user in users.values():
                    friend=client.get_friend(user.id)
                    if friend is None:
                        continue
                    if friend.nickname is None:
                        text += f'\n{str(friend.display_name)} / {friend.id}'
                    else:
                        text += f'\n{friend.nickname}({str(friend.display_name)}) / {friend.id}'
                    if friend.last_logout is not None:
                        text += '\n最後のログイン: {0.year}年{0.month}月{0.day}日 {0.hour}時{0.minute}分{0.second}秒'.format(friend.last_logout)
                if data['no-logs'] is False:
                    print(text)
                dstore(name,text)
                await reply(message, text)
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['getpending'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['getpending']}] [ユーザー名 / ユーザーID]")
                    return
                users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.is_pending(user.id) is True}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.display_name is not None and client.is_pending(user.id) is True:
                            users[user.display_name] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
                if len(users) > 30:
                    await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                    return
                if len(users) == 0:
                    await reply(message, 'ユーザーが見つかりません')
                    return
                text = str()
                for user in users.values():
                    pending = client.get_pending_friend(user.id)
                    if pending is None:
                        continue
                    text += f'\n{str(pending.display_name)} / {pending.id}'
                if data['no-logs'] is False:
                    print(text)
                dstore(name,text)
                await reply(message, text)
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['getblock'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['getblock']}] [ユーザー名 / ユーザーID]")
                    return
                users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.is_blocked(user.id) is True}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.display_name is not None and client.is_blocked(user.id) is True:
                            users[user.display_name] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
                if len(users) > 30:
                    await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                    return
                if len(users) == 0:
                    await reply(message, 'ユーザーが見つかりません')
                    return
                text = str()
                for user in users.values():
                    block=client.get_blocked_user(user.id)
                    if block is None:
                        continue
                    text += f'\n{str(block.display_name)} / {block.id}'
                if data['no-logs'] is False:
                    print(text)
                dstore(name,text)
                await reply(message, text)
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['info'].split(','):
            try:
                if args[1] in commands['info_party'].split(','):
                    text = str()
                    text += f'{client.user.party.id}\n人数: {client.user.party.member_count}'
                    for member in client.user.party.members.values():
                        add_cache(client, member)
                        if data['loglevel'] == 'normal':
                            text += f'\n{str(member.display_name)}'
                        else:
                            text += f'\n{str(member.display_name)} / {member.id}'
                    print(text)
                    dstore(None, text)
                    await reply(message, text)
                    if data['loglevel'] == 'debug':
                        print(json.dumps(client.user.party.meta.schema, indent=2))
                
                elif True in [args[1] in commands[key].split(',') for key in ("cid", "bid", "petcarrier", "pickaxe_id", "eid", "emoji_id", "toy_id", "shout_id", "id")]:
                    type_ = convert_to_type(args[1])
                    if rawcontent2 == '':
                        await reply(message, f"[{commands[type_]}] [ID]")
                        return
                    result = await loop.run_in_executor(None, search_item, "ja", "id", rawcontent2, type_)
                    if result is None:
                        result = await loop.run_in_executor(None, search_item, "en", "id", rawcontent2, type_)
                    if result is None:
                        await reply(message, "見つかりません")
                    else:
                        if len(result) > 30:
                            await reply(message, f"見つかったアイテム数 {len(result)} は多すぎます")
                            return
                        if len(result) == 1:
                            await reply(message, f"{result[0]['shortDescription']}: {result[0]['name']} | {result[0]['id']}\n説明: {result[0]['description']}\nレア度: {result[0]['displayRarity']}\n{result[0]['set']}")
                        else:
                            text = str()
                            for count, item in enumerate(result):
                                text += f"\n{count+1} {item['shortDescription']}: {item['name']} | {item['id']}"
                            text += "\n数字を入力することでそのアイテムに設定します"
                            await reply(message, text)
                            client.select[message.author.id] = {"exec": [f"await reply(message, f'''{item['shortDescription']}: {item['name']} | {item['id']}\n{item['description']}\n{item['displayRarity']}\n{item['set']}''')" for item in result]}

                elif True in  [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe", "emote", "emoji", "toy", "shout", "item")]:
                    type_ = convert_to_type(args[1])
                    if rawcontent2 == '':
                        await reply(message, f"[{commands[type_]}] [アイテム名]")
                        return
                    result = await loop.run_in_executor(None, search_item, "ja", "name", rawcontent2, type_)
                    if result is None:
                        result = await loop.run_in_executor(None, search_item, "en", "name", rawcontent2, type_)
                    if result is None:
                        await reply(message, "見つかりません")
                    else:
                        if len(result) > 30:
                            await reply(message, f"見つかったアイテム数 {len(result)} は多すぎます")
                            return
                        if len(result) == 1:
                            await reply(message, f"{result[0]['shortDescription']}: {result[0]['name']} | {result[0]['id']}\n{result[0]['description']}\n{result[0]['displayRarity']}\n{result[0]['set']}")
                        else:
                            text = str()
                            for count, item in enumerate(result):
                                text += f"\n{count+1} {item['shortDescription']}: {item['name']} | {item['id']}"
                            text += "\n数字を入力することでそのアイテムに設定します"
                            await reply(message, text)
                            client.select[message.author.id] = {"exec": [f"await reply(message, f'''{item['shortDescription']}: {item['name']} | {item['id']}\n{item['description']}\n{item['displayRarity']}\n{item['set']}''')" for item in result]}
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['info']}] [[{commands['info_party']}] / [{commands['info_item']}] / [{commands['id']}] / [{commands['skin']}] / [{commands['bag']}] / [{commands['pickaxe']}] / [{commands['emote']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['pending'].split(','):
            try:
                pendings=[]
                for pending in client.pending_friends.values():
                    add_cache(client, pending)
                    if pending.direction == 'INBOUND':
                        pendings.append(pending)
                if args[1] in commands['true'].split(','):
                    for pending in pendings:
                        try:
                            await pending.accept()
                            if data['loglevel'] == 'normal':
                                await reply(message, f'{str(pending.display_name)} をフレンドに追加')
                            else:
                                await reply(message, f'{str(pending.display_name)} / {pending.id} をフレンドに追加')
                        except fortnitepy.HTTPException:
                            if data['loglevel'] == 'debug':
                                print(red(traceback.format_exc()))
                            if data['loglevel'] == 'normal':
                                await reply(message, f'{str(pending.dispaly_name)} のフレンド申請の承認リクエストを処理中にエラーが発生しました')
                            else:
                                await reply(message, f'{str(pending.display_name)} / {pending.id} のフレンド申請の承認リクエストを処理中にエラーが発生しました')
                            continue
                        except Exception:
                            print(red(traceback.format_exc()))
                            dstore(name,f'>>> {traceback.format_exc()}')
                            await reply(message, 'エラー')
                            continue
                elif args[1] in commands['false'].split(','):
                    for pending in pendings:
                        try:
                            await pending.decline()
                            if data['loglevel'] == 'normal':
                                await reply(message, f'{str(pending.display_name)} のフレンド申請を拒否')
                            else:
                                await reply(message, f'{str(pending.display_name)} / {pending.id} のフレンド申請を拒否')
                        except fortnitepy.HTTPException:
                            if data['loglevel'] == 'debug':
                                print(red(traceback.format_exc()))
                                dstore(name,f'>>> {traceback.format_exc()}')
                            if data['loglevel'] == 'normal':
                                await reply(message, f'{str(pending.display_name)} のフレンド申請の拒否リクエストを処理中にエラーが発生しました')
                            else:
                                await reply(message, f'{str(pending.display_name)} / {pending.id} のフレンド申請の拒否リクエストを処理中にエラーが発生しました')
                            continue
                        except Exception:
                            print(red(traceback.format_exc()))
                            dstore(name,f'>>> {traceback.format_exc()}')
                            await reply(message, 'エラー')
                            continue
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['pending']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['removepending'].split(','):
            try:
                pendings=[]
                for pending in client.pending_friends.values():
                    add_cache(client, pending)
                    if pending.direction == 'OUTBOUND':
                        pendings.append(pending)
                for pending in pendings:
                    try:
                        await pending.decline()
                        if data['loglevel'] == 'normal':
                            await reply(message, f'{str(pending.display_name)} へのフレンド申請を解除')
                        else:
                            await reply(message, f'{str(pending.display_name)} / {pending.id} へのフレンド申請を解除')
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(name,f'>>> {traceback.format_exc()}')
                        if data['loglevel'] == 'normal':
                            await reply(message, f'{str(pending.display_name)} へのフレンド申請を解除リクエストを処理中にエラーが発生しました')
                        else:
                            await reply(message, f'{str(pending.display_name)} / {pending.id} へのフレンド申請を解除リクエストを処理中にエラーが発生しました')
                        continue
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                        await reply(message, 'エラー')
                        continue
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['addfriend'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['addfriend']}] [ユーザー名 / ユーザーID]")
                    return
                users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.has_friend(user.id) is False}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.display_name is not None and client.has_friend(user.id) is False:
                            users[user.display_name] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
                if len(users) > 30:
                    await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                    return
                if len(users) == 0:
                    await reply(message, 'ユーザーが見つかりません')
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.has_friend(user.id) is True:
                        await reply(message, '既にユーザーとフレンドです')
                        return
                    await client.add_friend(user.id)
                    if data['loglevel'] == 'normal':
                        await reply(message, f'{str(user.display_name)} にフレンド申請を送信')
                    else:
                        await reply(message, f'{str(user.display_name)} / {user.id} にフレンド申請を送信')
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.has_friend(user.id) is True:
                    await reply(message, '既にユーザーとフレンドです')
                    return
                await client.add_friend(user.id)
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(user.display_name)} にフレンド申請を送信')
                else:
                    await reply(message, f'{str(user.display_name)} / {user.id} にフレンド申請を送信')
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'フレンド申請の送信リクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                        ],
                        "variable": [
                            {"user": user} for name, user in users.items()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {user.display_name} / {user.id}"
                    text += "\n数字を入力することでそのユーザーにフレンド申請を送信します"
                    await reply(message, text)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'フレンド申請の送信リクエストを処理中にエラーが発生しました')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['removefriend'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['removefriend']}] [ユーザー名 / ユーザーID]")
                    return
                users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.has_friend(user.id) is True}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.display_name is not None and client.has_friend(user.id) is True:
                            users[user.display_name] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
                if len(users) > 30:
                    await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                    return
                if len(users) == 0:
                    await reply(message, 'ユーザーが見つかりません')
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.has_friend(user.id) is False:
                        await reply(message, 'ユーザーとフレンドではありません')
                        return
                    await client.remove_or_decline_friend(user.id)
                    if data['loglevel'] == 'normal':
                        await reply(message, f'{str(user.display_name)} をフレンドから削除')
                    else:
                        await reply(message, f'{str(user.display_name)} / {user.id} をフレンドから削除')
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.has_friend(user.id) is False:
                    await reply(message, 'ユーザーとフレンドではありません')
                    return
                await client.remove_or_decline_friend(user.id)
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(user.display_name)} をフレンドから削除')
                else:
                    await reply(message, f'{str(user.display_name)} / {user.id} をフレンドから削除')
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'フレンドの削除リクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                        ],
                        "variable": [
                            {"user": user} for name, user in users.items()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {user.display_name} / {user.id}"
                    text += "\n数字を入力することでそのユーザーをフレンドから削除します"
                    await reply(message, text)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'フレンドの削除リクエストを処理中にエラーが発生しました')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['acceptpending'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['acceptpending']}] [ユーザー名 / ユーザーID]")
                    return
                users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.is_pending(user.id) is True}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.display_name is not None and client.is_pending(user.id) is True:
                            users[user.display_name] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
                if len(users) > 30:
                    await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                    return
                if len(users) == 0:
                    await reply(message, 'ユーザーが見つかりません')
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.is_pending(user.id) is False:
                        await reply(message, 'ユーザーからのフレンド申請がありません')
                        return
                    await client.accept_friend(user.id)
                    if data['loglevel'] == 'normal':
                        await reply(message, f'{str(user.display_name)} をフレンドに追加')
                    else:
                        await reply(message, f'{str(user.display_name)} / {user.id} をフレンドに追加')
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.is_pending(user.id) is False:
                    await reply(message, 'ユーザーからのフレンド申請がありません')
                    return
                await client.accept_friend(user.id)
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(user.display_name)} をフレンドに追加')
                else:
                    await reply(message, f'{str(user.display_name)} / {user.id} をフレンドに追加')
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'フレンドの追加リクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                        ],
                        "variable": [
                            {"user": user} for name, user in users.items()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {user.display_name} / {user.id}"
                    text += "\n数字を入力することでそのユーザーからのフレンド申請を承諾します"
                    await reply(message, text)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'フレンドの追加リクエストを処理中にエラーが発生しました')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['declinepending'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['declinepending']}] [ユーザー名 / ユーザーID]")
                    return
                users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.is_pending(user.id) is True}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.display_name is not None and client.is_pending(user.id) is True:
                            users[user.display_name] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
                if len(users) > 30:
                    await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                    return
                if len(users) == 0:
                    await reply(message, 'ユーザーが見つかりません')
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.is_pending(user.id) is False:
                        await reply(message, 'ユーザーからのフレンド申請がありません')
                        return
                    await client.remove_or_decline_friend(user.id)
                    if data['loglevel'] == 'normal':
                        await reply(message, f'{str(user.display_name)} のフレンド申請を拒否')
                    else:
                        await reply(message, f'{str(user.display_name)} / {user.id} のフレンド申請を拒否')
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.is_pending(user.id) is False:
                    await reply(message, 'ユーザーからのフレンド申請がありません')
                    return
                await client.remove_or_decline_friend(user.id)
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(user.display_name)} のフレンド申請を拒否')
                else:
                    await reply(message, f'{str(user.display_name)} / {user.id} のフレンド申請を拒否')
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'フレンド申請の拒否リクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                        ],
                        "variable": [
                            {"user": user} for name, user in users.items()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {user.display_name} / {user.id}"
                    text += "\n数字を入力することでそのユーザーからのフレンド申請を拒否します"
                    await reply(message, text)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'フレンド申請の拒否リクエストを処理中にエラーが発生しました')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['blockfriend'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['blockfriend']}] [ユーザー名 / ユーザーID]")
                    return
                users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.is_blocked(user.id) is False}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.display_name is not None and client.is_blocked(user.id) is False:
                            users[user.display_name] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
                if len(users) > 30:
                    await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                    return
                if len(users) == 0:
                    await reply(message, 'ユーザーが見つかりません')
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.is_blocked(user.id) is True:
                        await reply(message, '既にユーザーをブロックしています')
                        return
                    await client.block_user(user.id)
                    if data['loglevel'] == 'normal':
                        await reply(message, f'{str(user.display_name)} をブロック')
                    else:
                        await reply(message, f'{str(user.display_name)} / {user.id} をブロック')
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.is_blocked(user.id) is True:
                    await reply(message, '既にユーザーをブロックしています')
                    return
                await client.block_user(user.id)
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(user.display_name)} をブロック')
                else:
                    await reply(message, f'{str(user.display_name)} / {user.id} をブロック')
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'フレンドのブロックリクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                        ],
                        "variable": [
                            {"user": user} for name, user in users.items()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {user.display_name} / {user.id}"
                    text += "\n数字を入力することでそのユーザーをブロックします"
                    await reply(message, text)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'フレンドのブロックリクエストを処理中にエラーが発生しました')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['unblockfriend'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['unblockfriend']}] [ユーザー名 / ユーザーID]")
                    return
                users = {name: user for name, user in cache_users.items() if rawcontent.lower() in name.lower() and user.id != client.user.id and client.is_blocked(user.id) is True}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.display_name is not None and client.is_blocked(user.id) is True:
                            users[user.display_name] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
                if len(users) > 30:
                    await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                    return
                if len(users) == 0:
                    await reply(message, 'ユーザーが見つかりません')
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.is_blocked(user.id) is False:
                        await reply(message, 'ユーザーをブロックしていません')
                        return
                    await client.unblock_user(user.id)
                    if data['loglevel'] == 'normal':
                        await reply(message, f'{str(user.display_name)} をブロック解除')
                    else:
                        await reply(message, f'{str(user.display_name)} / {user.id} をブロック解除')
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.is_blocked(user.id) is False:
                    await reply(message, 'ユーザーをブロックしていません')
                    return
                await client.unblock_user(user.id)
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(user.display_name)} をブロック解除')
                else:
                    await reply(message, f'{str(user.display_name)} / {user.id} をブロック解除')
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ブロックしたユーザーのブロック解除リクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                        ],
                        "variable": [
                            {"user": user} for name, user in users.items()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {user.display_name} / {user.id}"
                    text += "\n数字を入力することでそのユーザーをブロック解除します"
                    await reply(message, text)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ブロックしたユーザーのブロック解除リクエストを処理中にエラーが発生しました')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['chatban'].split(','):
            try:
                reason=rawcontent.split(' : ')
                if rawcontent == '':
                    await reply(message, f"[{commands['chatban']}] [ユーザー名 / ユーザーID] : [理由(任意)]")
                    return
                users = {member.display_name: member for member in client.user.party.members.values() if rawcontent.lower() in member.display_name.lower() and member.display_name is not None}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.display_name is not None and client.user.party.members.get(user.id) is not None:
                            users[user.display_name] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
                if len(users) > 30:
                    await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                    return
                if len(users) == 0:
                    await reply(message, 'ユーザーが見つかりません')
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.user.party.members.get(user.id) is None:
                        await reply(message, 'ユーザーがパーティーにいません')
                        return
                    member=client.user.party.members.get(user.id)
                    try:
                        await member.chatban(reason[1])
                    except IndexError:
                        await member.chatban()
                    if data['loglevel'] == 'normal':
                        await reply(message, f'{str(user.display_name)} をバン')
                    else:
                        await reply(message, f'{str(user.display_name)} / {user.id} をバン')
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.user.party.members.get(user.id) is None:
                    await reply(message, 'ユーザーがパーティーにいません')
                    return
                member=client.user.party.members.get(user.id)
                try:
                    await member.chatban(reason[1])
                except IndexError:
                    await member.chatban()
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(user.display_name)} をバン')
                else:
                    await reply(message, f'{str(user.display_name)} / {user.id} をバン')
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'パーティーリーダーではありません')
            except fortnitepy.NotFound:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'メンバーが見つかりません')
            except ValueError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, '既にバンされています')""" for name, user in users.items()
                        ],
                        "variable": [
                            {"user": user, "reason": reason} for name, user in users.items()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {user.display_name} / {user.id}"
                    text += "\n数字を入力することでそのユーザーをバンします"
                    await reply(message, text)
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'パーティーリーダーではありません')
            except fortnitepy.NotFound:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'メンバーが見つかりません')
            except ValueError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, '既にバンされています')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['promote'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['promote']}] [ユーザー名 / ユーザーID]")
                    return
                users = {member.display_name: member for member in client.user.party.members.values() if rawcontent.lower() in member.display_name.lower() and member.display_name is not None}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.display_name is not None and client.user.party.members.get(user.id) is not None:
                            users[user.display_name] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
                if len(users) > 30:
                    await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                    return
                if len(users) == 0:
                    await reply(message, 'ユーザーが見つかりません')
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.user.party.members.get(user.id) is None:
                        await reply(message, 'ユーザーがパーティーにいません')
                        return
                    member=client.user.party.members.get(user.id)
                    await member.promote()
                    if data['loglevel'] == 'normal':
                        await reply(message, f'{str(user.display_name)} に譲渡')
                    else:
                        await reply(message, f'{str(user.display_name)} / {user.id} に譲渡')
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.user.party.members.get(user.id) is None:
                    await reply(message, 'ユーザーがパーティーにいません')
                    return
                member=client.user.party.members.get(user.id)
                await member.promote()
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(user.display_name)} に譲渡')
                else:
                    await reply(message, f'{str(user.display_name)} / {user.id} に譲渡')
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'パーティーリーダーではありません')
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, '既にパーティーリーダーです')
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'パーティーリーダーの譲渡リクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                        ],
                        "variable": [
                            {"user": user} for name, user in users.items()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {user.display_name} / {user.id}"
                    text += "\n数字を入力することでそのユーザーに譲渡します"
                    await reply(message, text)
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'パーティーリーダーではありません')
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, '既にパーティーリーダーです')
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'パーティーリーダーの譲渡リクエストを処理中にエラーが発生しました')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['kick'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['kick']}] [ユーザー名 / ユーザーID]")
                    return
                users = {member.display_name: member for member in client.user.party.members.values() if rawcontent.lower() in member.display_name.lower() and member.display_name is not None}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.display_name is not None and client.user.party.members.get(user.id) is not None:
                            users[user.display_name] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
                if len(users) > 30:
                    await reply(message, f"見つかったユーザ数 {len(users)} は多すぎます")
                    return
                if len(users) == 0:
                    await reply(message, 'ユーザーが見つかりません')
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.user.party.members.get(user.id) is None:
                        await reply(message, 'ユーザーがパーティーにいません')
                        return
                    member=client.user.party.members.get(user.id)
                    await member.kick()
                    if data['loglevel'] == 'normal':
                        await reply(message, f'{str(user.display_name)} をキック')
                    else:
                        await reply(message, f'{str(user.display_name)} / {user.id} をキック')
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.user.party.members.get(user.id) is None:
                    await reply(message, 'ユーザーがパーティーにいません')
                    return
                member=client.user.party.members.get(user.id)
                await member.kick()
                if data['loglevel'] == 'normal':
                    await reply(message, f'{str(user.display_name)} をキック')
                else:
                    await reply(message, f'{str(user.display_name)} / {user.id} をキック')
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'パーティーリーダーではありません')
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, '自分をキックすることはできません')
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'パーティーメンバーのキックリクエストを処理中にエラーが発生しました')""" for name, user in users.items()
                        ],
                        "variable": [
                            {"user": user} for name, user in users.items()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {user.display_name} / {user.id}"
                    text += "\n数字を入力することでそのユーザーをキックします"
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'パーティーリーダーではありません')
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, '自分をキックすることはできません')
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'パーティーメンバーのキックリクエストを処理中にエラーが発生しました')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['ready'].split(','):
            try:
                await client.user.party.me.set_ready(fortnitepy.ReadyState.READY)
                await reply(message, '準備状態を 準備OK に設定')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['unready'].split(','):
            try:
                await client.user.party.me.set_ready(fortnitepy.ReadyState.NOT_READY)
                await reply(message, '準備状態を 準備中 に設定')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['sitout'].split(','):
            try:
                await client.user.party.me.set_ready(fortnitepy.ReadyState.SITTING_OUT)
                await reply(message, '準備状態を 欠場中 に設定')
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['outfitlock'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.outfitlock=True
                    await reply(message, 'コスチュームロックをオンに設定')
                elif args[1] in commands['false'].split(','):
                    client.outfitlock=False
                    await reply(message, 'コスチュームロックをオフに設定')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['outfitlock']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['backpacklock'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.backpacklock=True
                    await reply(message, 'バックアクセサリーロックをオンに設定')
                elif args[1] in commands['false'].split(','):
                    client.backpacklock=False
                    await reply(message, 'バックアクセサリーロックをオフに設定')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['backpacklock']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['pickaxelock'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.pickaxelock=True
                    await reply(message, '収集ツールロックをオンに設定')
                elif args[1] in commands['false'].split(','):
                    client.pickaxelock=False
                    await reply(message, '収集ツールロックをオフに設定')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['pickaxelock']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['emotelock'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.emotelock=True
                    await reply(message, 'エモートロックをオンに設定')
                elif args[1] in commands['false'].split(','):
                    client.emotelock=False
                    await reply(message, 'エモートロックをオフに設定')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['outfitlock']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['stop'].split(','):
            try:
                client.stopcheck=True
                if await change_asset(client, message.author.id, "emote", "") is True:
                    await reply(message, '停止しました')
                else:
                    await reply(message, 'ロックされています')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['alloutfit'].split(','):
            try:
                flag = False
                if client.outfitlock is True:
                    flag = lock_check(client, author_id)
                if flag is True:
                    await reply(message, 'ロックされています')
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
                await reply(message, '全てのコスチュームを表示し終わりました')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['allbackpack'].split(','):
            try:
                flag = False
                if client.backpacklock is True:
                    flag = lock_check(client, author_id)
                if flag is True:
                    await reply(message, 'ロックされています')
                    return
                with open('allen.json', 'r', encoding='utf-8') as f:
                    allskin = json.load(f)
                for item in allskin['data']:
                    if client.stopcheck is True:
                        client.stopcheck=False
                        break
                    if item['type'] == 'backpack':
                        if 'banner' not in item['id']:
                            await client.user.party.me.set_backpack(item['id'])
                        else:
                            await client.user.party.me.set_backpack(item['id'],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner'))
                        await asyncio.sleep(2)
                await reply(message, '全てのバックアクセサリーを表示し終わりました')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['allpet'].split(','):
            try:
                flag = False
                if client.backpacklock is True:
                    flag = lock_check(client, author_id)
                if flag is True:
                    await reply(message, 'ロックされています')
                    return
                with open('allen.json', 'r', encoding='utf-8') as f:
                    allskin = json.load(f)
                for item in allskin['data']:
                    if client.stopcheck is True:
                        client.stopcheck=False
                        break
                    if item['type'] == 'pet':
                        if 'banner' not in item['id']:
                            await client.user.party.me.set_backpack(item['id'])
                        else:
                            await client.user.party.me.set_backpack(item['id'],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner'))
                        await asyncio.sleep(2)
                await reply(message, '全てのペットを表示し終わりました')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['allpickaxe'].split(','):
            try:
                flag = False
                if client.pickaxelock is True:
                    flag = lock_check(client, author_id)
                if flag is True:
                    await reply(message, 'ロックされています')
                    return
                with open('allen.json', 'r', encoding='utf-8') as f:
                    allskin = json.load(f)
                for item in allskin['data']:
                    if client.stopcheck is True:
                        client.stopcheck=False
                        break
                    if item['type'] == 'pickaxe':
                        if 'banner' not in item['id']:
                            await client.user.party.me.set_pickaxe(item['id'])
                        else:
                            await client.user.party.me.set_pickaxe(item['id'],variants=client.user.party.me.create_variants(profile_banner='ProfileBanner'))
                        await asyncio.sleep(2)
                await reply(message, '全ての収集ツールを表示し終わりました')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['allemote'].split(','):
            try:
                flag = False
                if client.emotelock is True:
                    flag = lock_check(client, author_id)
                if flag is True:
                    await reply(message, 'ロックされています')
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
                    await reply(message, '全てのエモートを表示し終わりました')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['allemoji'].split(','):
            try:
                flag = False
                if client.emotelock is True:
                    flag = lock_check(client, author_id)
                if flag is True:
                    await reply(message, 'ロックされています')
                    return
                with open('allen.json', 'r', encoding='utf-8') as f:
                    allemote = json.load(f)
                for item in allemote['data']:
                    if client.stopcheck is True:
                        client.stopcheck=False
                        break
                    if item['type'] == 'emoji':
                        await client.user.party.me.set_emote(item['id'])
                        await asyncio.sleep(5)
                else:
                    await reply(message, '全てのエモートアイコンを表示し終わりました')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['alltoy'].split(','):
            try:
                flag = False
                if client.emotelock is True:
                    flag = lock_check(client, author_id)
                if flag is True:
                    await reply(message, 'ロックされています')
                    return
                with open('allen.json', 'r', encoding='utf-8') as f:
                    allemote = json.load(f)
                for item in allemote['data']:
                    if client.stopcheck is True:
                        client.stopcheck=False
                        break
                    if item['type'] == 'toy':
                        await client.user.party.me.set_emote(item['id'])
                        await asyncio.sleep(5)
                else:
                    await reply(message, '全てのおもちゃを表示し終わりました')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['allshout'].split(','):
            try:
                flag = False
                if client.emotelock is True:
                    flag = lock_check(client, author_id)
                if flag is True:
                    await reply(message, 'ロックされています')
                    return
                with open('allen.json', 'r', encoding='utf-8') as f:
                    allemote = json.load(f)
                for item in allemote['data']:
                    if client.stopcheck is True:
                        client.stopcheck=False
                        break
                    if item['type'] == 'shout':
                        await client.user.party.me.set_emote(item['id'])
                        await asyncio.sleep(5)
                else:
                    await reply(message, '全てのshoutを表示し終わりました')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['setenlightenment'].split(','):
            try:
                if await change_asset(client, message.author.id, "outfit", client.user.party.me.outfit, client.user.party.me.outfit_variants,(args[1],args[2])) is True:
                    await reply(message, f'{args[1]}, {args[2]} に設定')
                else:
                    await reply(message, 'ロックされています')
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'アイテム情報の設定リクエストを処理中にエラーが発生しました')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['setenlightenment']}] [数値] [数値]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif True in [args[0] in commands[key].split(',') for key in ("cid", "bid", "petcarrier", "pickaxe_id", "eid", "emoji_id", "toy_id", "shout_id", "id")]:
            type_ = convert_to_type(args[0])
            if rawcontent == '':
                await reply(message, f"[{commands[type_]}] [ID]")
                return
            try:
                result = await loop.run_in_executor(None, search_item, "ja", "id", rawcontent, type_)
                if result is None:
                    result = await loop.run_in_executor(None, search_item, "en", "id", rawcontent, type_)
                if result is None:
                    await reply(message, "見つかりません")
                else:
                    if len(result) > 30:
                        await reply(message, f"見つかったアイテム数 {len(result)} は多すぎます")
                        return
                    if len(result) == 1:
                        if await change_asset(client, message.author.id, result[0]["type"], result[0]['id']) is True:
                            await reply(message, f"{result[0]['shortDescription']}: {result[0]['name']} | {result[0]['id']}")
                        else:
                            await reply(message, "ロックされています")
                    else:
                        text = str()
                        for count, item in enumerate(result):
                            text += f"\n{count+1} {item['shortDescription']}: {item['name']} | {item['id']}"
                        text += "\n数字を入力することでそのアイテムに設定します"
                        await reply(message, text)
                        client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{item['type']}', '{item['id']}')" for item in result]}
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'アイテム情報の設定リクエストを処理中にエラーが発生しました')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif True in  [args[0] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe", "emote", "emoji", "toy", "shout", "item")]:
            type_ = convert_to_type(args[0])
            if rawcontent == '':
                await reply(message, f"[{commands[type_]}] [アイテム名]")
                return
            try:
                result = await loop.run_in_executor(None, search_item, "ja", "name", rawcontent, type_)
                if result is None:
                    result = await loop.run_in_executor(None, search_item, "en", "name", rawcontent, type_)
                if result is None:
                    await reply(message, "見つかりません")
                else:
                    if len(result) > 30:
                        await reply(message, f"見つかったアイテム数 {len(result)} は多すぎます")
                        return
                    if len(result) == 1:
                        if await change_asset(client, message.author.id, result[0]["type"], result[0]['id']) is True:
                            await reply(message, f"{result[0]['shortDescription']}: {result[0]['name']} | {result[0]['id']}")
                        else:
                            await reply(message, "ロックされています")
                    else:
                        text = str()
                        for count, item in enumerate(result):
                            text += f"\n{count+1} {item['shortDescription']}: {item['name']} | {item['id']}"
                        text += "\n数字を入力することでそのアイテムに設定します"
                        await reply(message, text)
                        client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{item['type']}', '{item['id']}')" for item in result]}
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'アイテム情報の設定リクエストを処理中にエラーが発生しました')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['set'].split(','):
            if rawcontent == '':
                await reply(message, f"[{commands['set']}] [セット名]]")
                return
            try:
                result = await loop.run_in_executor(None, search_item, "ja", "set", rawcontent)
                if result is None:
                    result = await loop.run_in_executor(None, search_item, "en", "set", rawcontent)
                if result is None:
                    await reply(message, "見つかりません")
                else:
                    if len(result) > 30:
                        await reply(message, f"見つかったアイテム数 {len(result)} は多すぎます")
                        return
                    if len(result) == 1:
                        if await change_asset(client, message.author.id, result[0]["type"], result[0]['id']) is True:
                            await reply(message, f"{result[0]['shortDescription']}: {result[0]['name']} | {result[0]['id']}({result[0]['set']})")
                        else:
                            await reply(message, "ロックされています")
                    else:
                        text = str()
                        for count, item in enumerate(result):
                            text += f"\n{count+1} {item['shortDescription']}: {item['name']} | {item['id']}({result[0]['set']})"
                        text += "\n数字を入力することでそのアイテムに設定します"
                        await reply(message, text)
                        client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{item['type']}', '{item['id']}')" for item in result]}
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'アイテム情報の設定リクエストを処理中にエラーが発生しました')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['setstyle'].split(','):
            try:
                if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe")]:
                    await reply(message, f"[{commands['setstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                    return
                type_ = convert_to_type(args[1])
                id_ = member_asset(client.user.party.me, convert_to_asset(args[1]))
                result = search_style("ja", id_)
                if result is None:
                    await reply(message, "スタイル変更はありません")
                else:
                    text = str()
                    for count, item in enumerate(result):
                        text += f"\n{count+1} {item['name']}"
                    text += "\n数字を入力することでそのアイテムに設定します"
                    await reply(message, text)
                    client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{type_}', '{id_}', {variants['variants']})" for variants in result]}
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['setstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['addstyle'].split(','):
            try:
                if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe")]:
                    await reply(message, f"[{commands['addstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                    return
                type_ = convert_to_type(args[1])
                id_ = member_asset(client.user.party.me, convert_to_asset(args[1]))
                variants_ = eval(f"client.user.party.me.{convert_to_asset(args[1])}_variants")
                result = search_style("ja", id_)
                if result is None:
                    await reply(message, "スタイル変更はありません")
                else:
                    text = str()
                    for count, item in enumerate(result):
                        text += f"\n{count+1} {item['name']}"
                    text += "\n数字を入力することでそのアイテムに設定します"
                    await reply(message, text)
                    client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{type_}', '{id_}', {variants_} + {variants['variants']})" for variants in result]}
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['addstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['setvariant'].split(','):
            try:
                if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe")]:
                    await reply(message, f"[{commands['setvariant']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                    return
                variantdict={}
                for count,text in enumerate(args[2:]):
                    if count % 2 != 0:
                        continue
                    try:
                        variantdict[text]=args[count+3]
                    except IndexError:
                        break
                type_ = convert_to_type(args[1])
                id_ = member_asset(client.user.party.me, convert_to_asset(args[1]))
                variants = client.user.party.me.create_variants(item='AthenaCharacter',**variantdict)
                if await change_asset(client, message.author.id, type_, id_, variants, client.user.party.me.enlightenment) is False:
                    await reply(message, "ロックされています")
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'アイテム情報の設定リクエストを処理中にエラーが発生しました')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['setvariant']}] [ID] [variant] [数値]\nvariantと数値は無限に設定可能")
            except Exception:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0] in commands['addvariant'].split(','):
            try:
                if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe")]:
                    await reply(message, f"[{commands['addvariant']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                    return
                variantdict={}
                for count,text in enumerate(args[2:]):
                    if count % 2 != 0:
                        continue
                    try:
                        variantdict[text]=args[count+3]
                    except IndexError:
                        break
                type_ = convert_to_type(args[1])
                id_ = member_asset(client.user.party.me, convert_to_asset(args[1]))
                variants = client.user.party.me.create_variants(item='AthenaCharacter',**variantdict)
                variants += eval(f"client.user.party.me.{convert_to_asset(args[1])}_variants")
                if await change_asset(client, message.author.id, type_, id_, variants, client.user.party.me.enlightenment) is False:
                    await reply(message, "ロックされています")
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'アイテム情報の設定リクエストを処理中にエラーが発生しました')
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['addvariant']}] [ID] [variant] [数値]\nvariantと数値は無限に設定可能")
            except Exception:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif True in [args[0] in commands[key].split(',') for key in ("outfitasset", "backpackasset", "pickaxeasset", "emoteasset")]:
            type_ = convert_to_type(args[0])
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands[f'{type_}asset']}] [アセットパス]")
                    return
                if await change_asset(client, message.author.id, type_, rawcontent) is False:
                    await reply(message, "ロックされています")
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'アイテム情報の設定リクエストを処理中にエラーが発生しました')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif True in [args[0].lower().startswith(id_) for id_ in ("cid_", "bid_", "petcarrier_", "pickaxe_id_", "eid_", "emoji_", "toy_", "shout_")]:
            try:
                type_ = convert_to_type("_".join(args[0].split('_')[:-1]) + "_")
                if await change_asset(client, message.author.id, type_, args[0]) is False:
                    await reply(message, "ロックされています")
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'アイテム情報の設定リクエストを処理中にエラーが発生しました')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        elif args[0].lower().startswith('playlist_'):
            try:
                await client.user.party.set_playlist(args[0])
                await reply(message, f'プレイリストを {args[0]} に設定')
                data['fortnite']['playlist']=args[0]
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'パーティーリーダーではありません')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'エラー')

        else:
            if ': ' in message.content:
                return
            if args[0].isdigit() and client.select.get(message.author.id) is not None:
                try:
                    if int(args[0]) == 0:
                        await reply(message, '有効な数字を入力してください')
                        return
                    exec_ = client.select[message.author.id]["exec"][int(args[0])-1]
                    variable=globals()
                    variable.update(locals())
                    if client.select[message.author.id].get("variable") is not None:
                        variable.update(client.select[message.author.id]["variable"][int(args[0])-1])
                    await aexec(exec_, variable)
                except IndexError:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, '有効な数字を入力してください')
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, 'エラー')
            else:
                result = await loop.run_in_executor(None, search_item, "ja", "name", content, "item")
                if result is None:
                    result = await loop.run_in_executor(None, search_item, "en", "name", content, "item")
                if result is not None:
                    if len(result) > 30:
                        await reply(message, f"見つかったアイテム数 {len(result)} は多すぎます")
                        return
                    if len(result) == 1:
                        if await change_asset(client, message.author.id, result[0]["type"], result[0]['id']) is True:
                            await reply(message, f"{result[0]['shortDescription']}: {result[0]['name']} | {result[0]['id']}")
                        else:
                            await reply(message, "ロックされています")
                    else:
                        text = str()
                        for count, item in enumerate(result):
                            text += f"\n{count+1} {item['shortDescription']}: {item['name']} | {item['id']}"
                        text += "\n数字を入力することでそのアイテムに設定します"
                        await reply(message, text)
                        client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{item['type']}', '{item['id']}')" for item in result]}

#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================

clients = []
for count, credential in enumerate(credentials.items()):
    email = credential[0]
    password = credential[1]
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
    client.outfitlock=False
    client.backpacklock=False
    client.pickaxelock=False
    client.emotelock=False
    client.owner=None
    client.prevoutfit=None
    client.prevoutfitvariants=None
    client.prevbackpack=None
    client.prevbackpackvariants=None
    client.prevpickaxe=None
    client.prevpickaxevariants=None
    client.prevmessage={}
    client.select={}
    client.invitelist=[]
    client.whisper=data['fortnite']['whisper']
    client.partychat=data['fortnite']['partychat']
    client.discord=data['discord']['discord']
    client.whisperperfect=data['fortnite']['disablewhisperperfectly']
    client.partychatperfect=data['fortnite']['disablepartychatperfectly']
    client.discordperfect=data['discord']['disablediscordperfectly']
    client.joinmessageenable=data['fortnite']['joinmessageenable']
    client.randommessageenable=data['fortnite']['randommessageenable']
    client.outfitmimic=data['fortnite']['outfitmimic']
    client.backpackmimic=data['fortnite']['backpackmimic']
    client.pickaxemimic=data['fortnite']['pickaxemimic']
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
    client.add_event_handler('party_member_confirm', event_party_member_confirm)
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
