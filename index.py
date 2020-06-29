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
    from typing import Optional, Union, Type, Any, List, Callable
    from concurrent.futures import ThreadPoolExecutor
    from functools import partial, wraps
    from threading import Thread, Timer
    from glob import glob
    import unicodedata
    import webbrowser
    import traceback
    import datetime
    import asyncio
    import logging
    import random
    import string
    import socket
    import json
    import time
    import sys
    import os
    import re
except ModuleNotFoundError as e:
    try:
        import traceback
        print(traceback.format_exc())
    except ModuleNotFoundError:
        pass
    try:
        import sys
        print(f'Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}\n')
    except ModuleNotFoundError:
        pass
    print(e)
    print('標準ライブラリの読み込みに失敗しました。Pythonのバージョンが間違っている可能性があります。Pythonの再インストールなどを試してみてください。問題が修正されない場合は\nTwitter @gomashio1596\nDiscord gomashio#4335\nこちらか\nhttps://discord.gg/NEnka5N\nDiscordのサーバーまでお願いします')
    print('Failed to load basic library. Python version maybe wrong. Try reinstall Python. If the issue is not resolved, contact me\nTwitter @gomashio1596\nDiscord gomashio#4335\nor please join support Discord server\nhttps://discord.gg/NEnka5N')
    sys.exit(1)

try:
    from crayons import cyan, green, magenta, red, yellow
    from jinja2 import Environment, FileSystemLoader
    from fortnitepy import ClientPartyMember
    from sanic.request import Request
    import fortnitepy.errors
    from sanic import Sanic
    import sanic.exceptions
    import sanic.response
    import fortnitepy
    import requests
    import discord
    import jaconv
except ModuleNotFoundError as e:
    try:
        import traceback
        print(traceback.format_exc())
    except ModuleNotFoundError:
        pass
    try:
        import sys
        print(f'Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}\n')
    except ModuleNotFoundError:
        pass
    print(e)
    print('サードパーティーライブラリの読み込みに失敗しました。INSTALL.bat を実行してください。問題が修正されない場合は\nTwitter @gomashio1596\nDiscord gomashio#4335\nこちらか\nhttps://discord.gg/NEnka5N\nDiscordのサーバーまでお願いします')
    print('Failed to load third party library. Please run INSTALL.bat. If the issue is not resolved, contact me\nTwitter @gomashio1596\nDiscord gomashio#4335\nor please join support Discord server\nhttps://discord.gg/NEnka5N')
    sys.exit(1)

try:
    asyncio.set_event_loop(asyncio.ProactorEventLoop())
except Exception:
    pass

filename = 'device_auths.json'
storedlog = []
loadedclients = []
whitelist = []
whitelist_ = []
blacklist = []
blacklist_ = []
otherbotlist = []
error_config = []
error_commands = []
client_name = {}
cache_users = {}
cached_items = {}
blacklist_flag = True
whitelist_flag = True
invitelist_flag = True
otherbotlist_flag = True
discord_flag = True
kill=False
localizekeys=['bot','lobbybot','credit','library','loglevel','normal','info','debug','debug_is_on','on','off','booting','get_code','authorization_expired','waiting_for_authorization','account_incorrect','login','all_login','relogin','owner','party','userid','name_or_id','partyid','content','number','eval','exec','invite_is_decline','restarting','relogining','success','accepted_invite_from','accepted_invite_from2','declined_invite_from','declined_invite_from2','declined_invite_interval','declined_invite_interval2','declined_invite_interval3','declined_invite_owner','declined_invite_owner2','declined_invite_owner3','declined_invite_whitelist','declined_invite_whitelist2','declined_invite_whitelist3','party_member_joined','party_member_left','party_member_request','party_member_kick','party_member_promote','party_member_update','party_member_disconnect','party_member_chatban','party_member_chatban2','party_update','random_message','click_invite','inviteaccept','inviteinterval','invite_from','invite_from2','friend_request_to','friend_request_from','friend_request_decline','friend_accept','friend_add','friend_remove','this_command_owneronly','failed_ownercommand','error_while_declining_partyrequest','error_while_accepting_friendrequest','error_while_declining_friendrequest','error_while_sending_friendrequest','error_while_removing_friendrequest','error_while_removing_friend','error_while_accepting_invite','error_while_declining_invite','error_while_blocking_user','error_while_unblocking_user','error_while_requesting_userinfo','error_while_joining_to_party','error_while_leaving_party','error_while_sending_partyinvite','error_while_changing_asset','error_while_changing_bpinfo','error_while_promoting_party_leader','error_while_kicking_user','error_while_swapping_user','error_while_setting_client','error_already_member_of_party','error_netcl_does_not_match','error_private_party','login_failed','failed_to_load_account','failed_to_run_web','web_already_running','exchange_code_error','api_downing','api_downing2','not_enough_password','owner_notfound','discord_owner_notfound','blacklist_user_notfound','whitelist_user_notfound','discord_blacklist_user_notfound','discord_whitelist_user_notfound','botlist_user_notfound','invitelist_user_notfound','not_friend_with_owner','not_friend_with_inviteuser','not_friend_with_user','nor_pending_with_user','not_party_leader','load_failed_keyerror','load_failed_json','load_failed_notfound','is_missing','too_many_users','too_many_items','user_notfound','user_not_in_party','party_full_or_already_or_offline','party_full_or_already','party_notfound','party_private','not_available','must_be_int','item_notfound','error','add_to_list','already_list','remove_from_list','not_list','enter_to_add_to_list','enter_to_remove_from_list','blacklist','whitelist','discord_blacklist','discord_whitelist','invitelist','botlist','enter_to_get_userinfo','friendcount','pendingcount','outbound','inbound','blockcount','set_to','mimic','outfit','backpack','pet','pickaxe','emote','emoji','toy','command_from','whisper','partychat','discord','disable_perfect','invite','accept','decline','friend_request','join_','message','randommessage','decline_invite_for','enter_to_join_party','party_leave','user_invited','enter_to_invite_user','user_sent','enter_to_send','party_sent','status','banner','bannerid','color','level','bpinfo','tier','xpboost','friendxpboost','privacy','public','friends_allow_friends_of_friends','friends','private_allow_friends_of_friends','private','lastlogin','member_count','enter_to_show_info','itemname','remove_pending','already_friend','enter_to_send_friendrequest','remove_friend','enter_to_remove_friend','enter_to_accept_pending','enter_to_decline_pending','already_block','block_user','enter_to_block_user','not_block','unblock_user','enter_to_unblock_user','optional','reason','chatban_user','already_chatban','enter_to_chatban_user','promote_user','already_party_leader','enter_to_promote_user','kick_user','cant_kick_yourself','readystate','ready','unready','sitout','matchstate','remaining','remaining_must_be_between_0_and_255','swap_user','enter_to_swap_user','lock','stopped','locked','all_end','enter_to_change_asset','setname','no_stylechange','enter_to_set_style','assetpath','set_playlist','please_enter_valid_number','web','web_login','web_logout','web_logged','web_not_logged','invalid_password','main_page','config_editor','commands_editor','party_viewer','password','web_save','web_saved','web_back','account_not_exists','account_not_loaded','party_moving','loading','command','run','result','web_notfound','password_reset_error','this_field_is_required','replies_editor','trigger','text','cannot_be_empty']
ignore=['ownercommands','true','false','me', 'privacy_public', 'privacy_friends_allow_friends_of_friends', 'privacy_friends', 'privacy_private_allow_friends_of_friends', 'privacy_private', 'info_party']
auth = fortnitepy.Auth()
launcher_token = auth.ios_token
fortnite_token = auth.fortnite_token
oauth_url = "https://account-public-service-prod03.ol.epicgames.com/account/api/oauth/token"
fortnite_token_url = "https://account-public-service-prod03.ol.epicgames.com/account/api/oauth/token"
exchange_auth_url = "https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token"
device_auth_url = "https://account-public-service-prod.ol.epicgames.com/account/api/oauth/deviceAuthorization"
exchange_url = "https://account-public-service-prod.ol.epicgames.com/account/api/oauth/exchange"
user_lookup_url = "https://account-public-service-prod.ol.epicgames.com/account/api/public/account/{user_id}"

if True:
    class bool_:
        @classmethod
        def create(self, content: str) -> bool:
            d = {"False": False, "True": True}
            return d.get(content, False)

    class bool_none:
        @classmethod
        def create(self, content: str) -> bool:
            d = {"False": False, "True": True, "None": None}
            return d.get(content, False)

    class LoginManager:
        def __init__(self) -> None:
            self.id_len = 64
            self.expire_time = datetime.timedelta(minutes=10)
            self.expires = {}
            self.cookie_key = "X-SessionId"
            self.no_auth_handler_ = sanic.response.html("Unauthorized")

        def generate_id(self, request: Request) -> str:
            Id = "".join(random.choices(string.ascii_letters + string.digits, k=self.id_len))
            while Id in self.expires.keys():
                Id = "".join(random.choices(string.ascii_letters + string.digits, k=self.id_len))
            return Id

        def authenticated(self, request: Request) -> bool:
            if data["web"]["login_required"] is True:
                Id = request.cookies.get(self.cookie_key)
                if Id is None:
                    return False
                elif Id in self.expires.keys():
                    return True
                else:
                    return False
            else:
                return True

        def login_user(self, request: Request, response: Type[sanic.response.BaseHTTPResponse]) -> None:
            Id = self.generate_id(request)
            response.cookies[self.cookie_key] = Id
            self.expires[Id] = datetime.datetime.utcnow() + self.expire_time

        def logout_user(self, request: Request, response: Type[sanic.response.BaseHTTPResponse]) -> None:
            Id = request.cookies.get(self.cookie_key)
            if Id is not None:
                del response.cookies[self.cookie_key]
                self.expires[Id] = datetime.datetime.utcnow() + self.expire_time
                
        def login_required(self, func: Callable):
            @wraps(func)
            def deco(*args: Any, **kwargs: Any):
                request = args[0]
                if self.authenticated(request) is True:
                    return func(*args, **kwargs)
                elif isinstance(self.no_auth_handler_, sanic.response.BaseHTTPResponse):
                    return self.no_auth_handler_
                elif callable(self.no_auth_handler_):
                    return self.no_auth_handler_(*args, **kwargs)
            return deco

        def no_auth_handler(self, func: Callable):
            if asyncio.iscoroutinefunction(func) is False:
                raise ValueError("Function must be a coroutine")
            self.no_auth_handler_ = func
            @wraps(func)
            def deco(*args: Any, **kwargs: Any):
                return func(*args, **kwargs)
            return deco

    class WebUser:
        def __init__(self, sessionId: str) -> None:
            self._id = sessionId

        @property
        def display_name(self) -> None:
            return "WebUser"

        @property
        def id(self) -> None:
            return self._id

    class WebMessage:
        def __init__(self, content: str, sessionId: str, client: Type[fortnitepy.Client]) -> None:
            self._sessionId = sessionId
            self._content = content
            self._client = client
            self._author = WebUser(self._sessionId)
            self._messages = []
            
        @property
        def author(self) -> WebUser:
            return self._author

        @property
        def content(self) -> str:
            return self._content

        @property
        def client(self) -> Type[fortnitepy.Client]:
            return self._client

        @property
        def result(self) -> str:
            return self._messages

        async def reply(self, content: str) -> None:
            self._messages.append(content)

    class AllMessage:
        def __init__(self,
                     content: str,
                     author: Union[Type[fortnitepy.user.UserBase], Type[discord.abc.User], Type[WebUser]],
                     client: Type[fortnitepy.Client],
                     base: Union[Type[fortnitepy.message.MessageBase], Type[discord.Message], Type[WebMessage]]
                    ) -> None:
            self._content = content
            self._author = author
            self._client = client
            self._base = base
            self._messages = {}

        @property
        def author(self) -> WebUser:
            return self._author

        @property
        def content(self) -> str:
            return self._content

        @property
        def client(self) -> Type[fortnitepy.Client]:
            return self._client

        @property
        def base(self) -> Union[Type[fortnitepy.message.MessageBase], Type[discord.Message], Type[WebMessage]]:
            return self._base

        @property
        def result(self) -> str:
            return self._messages

        async def reply(self, content: str, client: Type[fortnitepy.Client]) -> None:
            if self._messages.get(client.user.id) is None:
                self._messages[client.user.id] = []
            self._messages[client.user.id].append(content)

    class can_be_multiple:
        pass

    class select:
        def __init__(self, content: List[dict]) -> None:
            self.content = content

    class Red:
        pass

    class FixRequired:
        pass

    class Client(fortnitepy.Client):
        def __init__(self, **kwargs: Any) -> None:
            super().__init__(**kwargs)

        async def event_device_auth_generate(self, details: dict, email: str) -> None:
            store_device_auth_details(email, details)

        async def event_ready(self) -> None:
            global blacklist_flag
            global blacklist
            global whitelist_flag
            global whitelist
            global invitelist_flag
            global otherbotlist
            global otherbotlist_flag
            global discord_flag
            global client_name
            global loadedclients
            client=self
            display_name = name(client.user)
            send(display_name,f'{l("login")}: {display_name}',green,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
            client.isready=True
            client.booting=False
            loadedclients.append(client)
            client_name[client.user.display_name] = client
            add_cache(client, client.user)
            for friend_ in client.friends.values():
                add_cache(client, friend_)
            for pending_ in client.pending_friends.values():
                add_cache(client, pending_)
            for block_ in client.blocked_users.values():
                add_cache(client, block_)
            try:
                if client.party.leader.id == client.user.id:
                    prop = {"VoiceChat:implementation_s": "VivoxVoiceChat"}
                    await client.party.patch(updated=prop)
            except Exception:
                if data['loglevel'] == 'debug':
                    send(name(client.user),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

            try:
                client.owner=None
                owner=await client.fetch_profile(data['fortnite']['owner'])
                if owner is None:
                    send(display_name,l("owner_notfound"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                else:
                    add_cache(client, owner)
                    client.owner=client.get_friend(owner.id)
                    if client.owner is None:
                        if data['fortnite']['addfriend'] is True:
                            try:
                                await client.add_friend(owner.id)
                            except fortnitepy.HTTPException:
                                if data['loglevel'] == 'debug':
                                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                                send(display_name,l("error_while_sending_friendrequest"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                            except Exception:
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        send(display_name,l("not_friend_with_owner",commands["reload"]),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                    else:
                        send(display_name,f'{l("owner")}: {name(client.owner)}',green,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                send(display_name,l("error_while_requesting_userinfo"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            
            if client.owner is not None:
                await client.owner.send(l("click_invite"))

            if blacklist_flag is True:
                blacklist_flag = False
                for blacklistuser in data['fortnite']['blacklist']:
                    try:
                        user = await client.fetch_profile(blacklistuser)
                        add_cache(client, user)
                        if user is None:
                            send(display_name,l("blacklist_user_notfound",blacklistuser),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                        else:
                            blacklist.append(user.id)
                            if data['fortnite']['blacklist-autoblock'] is True:
                                try:
                                    await user.block()
                                except Exception:
                                    if data['loglevel'] == 'debug':
                                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        send(display_name,l("error_while_requesting_userinfo"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                    except Exception:
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                if data['loglevel'] == "debug":
                    send(display_name,f'blacklist {blacklist}',yellow,add_d=lambda x:f'```\n{x}\n```')
            if whitelist_flag is True:
                whitelist_flag = False
                for whitelistuser in data['fortnite']['whitelist']:
                    try:
                        user = await client.fetch_profile(whitelistuser)
                        add_cache(client, user)
                        if user is None:
                            send(display_name,l("whitelist_user_notfound",whitelistuser),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                        else:
                            whitelist.append(user.id)
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        send(display_name,l("error_while_requesting_userinfo"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                    except Exception:
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                if data['loglevel'] == "debug":
                    send(display_name,f'whitelist {whitelist}',yellow,add_d=lambda x:f'```\n{x}\n```')

            if otherbotlist_flag is True:
                otherbotlist_flag = False
                for otherbotlistuser in data['fortnite']['otherbotlist']:
                    try:
                        user = await client.fetch_profile(otherbotlistuser)
                        add_cache(client, user)
                        if user is None:
                            send(display_name,l("botlist_user_notfound",otherbotlistuser),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                        else:
                            otherbotlist.append(user.id)
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        send(display_name,l("error_while_requesting_userinfo"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                    except Exception:
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                if data['loglevel'] == "debug":
                    send(display_name,f'botlist {otherbotlist}',yellow,add_d=lambda x:f'```\n{x}\n```')

            for invitelistuser in data['fortnite']['invitelist']:
                try:
                    user = await client.fetch_profile(invitelistuser)
                    if user is None:
                        send(display_name,l("invitelist_user_notfound",invitelistuser),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                    else:
                        friend = client.get_friend(user.id)
                        if friend is None and user.id != client.user.id:
                            if data['fortnite']['addfriend'] is True:
                                try:
                                    await client.add_friend(friend.id)
                                except fortnitepy.HTTPException:
                                    if data['loglevel'] == 'debug':
                                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                                    send(display_name,l("error_while_sending_friendrequest"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                                except Exception:
                                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                            send(display_name,l("not_friend_with_inviteuser",invitelistuser,commands["reload"]),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                        else:
                            add_cache(client, user)
                            client.invitelist.append(user.id)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    send(display_name,l("error_while_requesting_userinfo"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                except Exception:
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            if data['loglevel'] == "debug":
                send(display_name,f'invitelist {client.invitelist}',yellow,add_d=lambda x:f'```\n{x}\n```')

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
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                            try:
                                await pending.decline()
                            except fortnitepy.HTTPException:
                                if data['loglevel'] == 'debug':
                                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                            except Exception:
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        except Exception:
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    else:
                        try:
                            await pending.decline()
                        except fortnitepy.HTTPException:
                            if data['loglevel'] == 'debug':
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        except Exception:
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            
            if data['discord']['enabled'] is True and discord_flag is True:
                discord_flag = False
                await dclient.start(data['discord']['token'])

        async def event_close(self) -> None:
            client=self
            send(name(client.user),f'{l("closing")}: {client.user.display_name}',green,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
            client.isready=False

        async def event_restart(self) -> None:
            client=self
            send(name(client.user),l("relogin", client.user.display_name),green,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')

        async def event_party_invite(self, invitation: fortnitepy.ReceivedPartyInvitation) -> None:
            global blacklist
            global whitelist
            if invitation is None:
                return
            client=invitation.client
            if client.isready is False:
                return
            display_name = name(client.user)
            add_cache(client, invitation.sender)
            if invitation.sender.id in blacklist:
                if data['fortnite']['blacklist-declineinvite'] is True:
                    try:
                        await invitation.decline()
                    except Exception:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
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
                send(display_name,l("invite_from",name(invitation.sender)),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
            else:
                send(display_name,l("invite_from2",f'{name(invitation.sender)} [{platform_to_str(invitation.sender.platform)}]',invitation.party.id),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')

            if client.owner is not None:
                if client.owner.id in client.party.members.copy().keys() and data['fortnite']['invite-ownerdecline'] is True:
                    await invitation_decline_owner(invitation)
                    return
            if True in [memberid in whitelist for memberid in client.party.members.copy().keys()] and data['fortnite']['whitelist-declineinvite'] is True:
                await invitation_decline_whitelist(invitation)
            elif client.acceptinvite is False:
                await invitation_decline(invitation)
            elif client.acceptinvite_interval is False:
                await invitation_decline_interval(invitation)
            else:
                await invitation_accept(invitation)

        async def event_friend_request(self, request: fortnitepy.PendingFriend) -> None:
            if request is None:
                return
            client=request.client
            if client.isready is False:
                return
            display_name = name(client.user)
            add_cache(client, request)
            if request.direction == 'OUTBOUND':
                send(display_name,l("friend_request_to",name(request)),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                return
            send(display_name,l("friend_request_from",name(request)),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
            if client.acceptfriend is True:
                try:
                    await request.accept()
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    send(display_name,l("error_while_accepting_friendrequest"),red,add_d=lambda x:f'>>> {x}')
                except Exception:
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            elif client.acceptfriend is False:
                try:
                    await request.decline()
                    send(display_name,l("friend_request_decline",name(request)),red,add_d=lambda x:f'>>> {x}')
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    send(display_name,l("error_while_declining_friendrequest"),red,add_d=lambda x:f'>>> {x}')
                except Exception:
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

        async def event_friend_add(self, friend: fortnitepy.Friend) -> None:
            if friend is None:
                return
            client=friend.client
            if client.isready is False:
                return
            display_name = name(client.user)
            add_cache(client, friend)
            if friend.direction == 'OUTBOUND':
                send(display_name,l("friend_accept",name(friend)),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
            else:
                send(display_name,l("friend_add",name(friend)),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')

        async def event_friend_remove(self, friend: fortnitepy.Friend) -> None:
            if friend is None:
                return
            client=friend.client
            if client.isready is False:
                return
            display_name = name(client.user)
            add_cache(client, friend)
            if data['loglevel'] == 'normal':
                send(display_name,l("friend_remove",name(friend)),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
            else:
                send(display_name,l("friend_remove",f'{name(friend)} [{platform_to_str(friend.platform)}]'),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')

        async def event_party_member_join(self, member: fortnitepy.PartyMember) -> None:
            global blacklist
            if member is None:
                return
            client=member.client
            if client.isready is False:
                return
            add_cache(client, member) 
            display_name = name(client.user)
            display_name_ = is_most(client)
            try:
                if client.party.leader.id == client.user.id:
                    prop = {"VoiceChat:implementation_s": "VivoxVoiceChat"}
                    await client.party.patch(updated=prop)
            except Exception:
                if data['loglevel'] == 'debug':
                    send(name(client.user),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            if display_name_:
                if data['loglevel'] == 'normal':
                    send(display_name_,l('party_member_joined',name(member),member.party.member_count),magenta,add_p=lambda x:f'[{now_()}] [{l("party")}] [{display_name_}] {x}')
                else:
                    send(display_name_,l('party_member_joined',f'{name(member)} [{platform_to_str(member.platform)}/{member.input}]',member.party.member_count),magenta,add_p=lambda x:f'[{now_()}] [{l("party")}/{client.party.id}] [{display_name_}] {x}')
            
            if member.id in blacklist and client.party.me.leader is True:
                if data['fortnite']['blacklist-autokick'] is True:
                    try:
                        await member.kick()
                    except Exception:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    return
                if data['fortnite']['blacklist-autochatban'] is True:
                    try:
                        await member.chatban()
                    except Exception:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    return
            
            if data['fortnite']['addfriend'] is True:
                for member in member.party.members.copy().keys():
                    try:
                        await client.add_friend(member)
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    except Exception:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

            await asyncio.sleep(0.1)

            if client.joinmessageenable is True:
                try:
                    await client.party.send(data['fortnite']['joinmessage'])
                except Exception:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            if client.randommessageenable is True:
                try:
                    randommessage=random.choice(data['fortnite']['randommessage'].split(','))
                    send(display_name,f'{l("random_message")}: {randommessage}',add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await client.party.send(randommessage)
                except Exception:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

            try:
                await change_asset(client, client.user.id, "Emote", client.eid)
            except Exception:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

            if client.party.leader.id == client.user.id:
                try:
                    await client.party.set_playlist(data['fortnite']['playlist'])
                    await client.party.set_privacy(data['fortnite']['privacy'])
                except fortnitepy.Forbidden:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

        async def event_party_member_leave(self, member: fortnitepy.PartyMember) -> None:
            if member is None:
                return
            client=member.client
            if client.isready is False:
                return
            add_cache(client, member)
            display_name = name(client.user)
            display_name_ = is_most(client)
            if display_name_:
                if data['loglevel'] == 'normal':
                    send(display_name_,l("party_member_left",name(member),member.party.member_count),magenta,lambda x:f'[{now_()}] [{l("party")}] [{display_name_}] {x}')
                else:
                    send(display_name_,l("party_member_left",f'{name(member)} [{platform_to_str(member.platform)}/{member.input}]',member.party.member_count),magenta,lambda x:f'[{now_()}] [{l("party")}] [{display_name_}] {x}')

            if data['fortnite']['addfriend'] is True:
                for member in member.party.members.copy().keys():
                    try:
                        await client.add_friend(member)
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        continue
                    except Exception:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

        async def event_party_member_confirm(self, confirmation: fortnitepy.PartyJoinConfirmation) -> None:
            global blacklist
            if confirmation is None:
                return
            client=confirmation.client
            if client.isready is False:
                return
            add_cache(client, confirmation.user)
            display_name = name(client.user)
            display_name_ = is_most(client)
            if display_name_:
                if data['loglevel'] != 'normal':
                    send(display_name_,l("party_member_request",name(confirmation.user)),magenta,add_p=lambda x:f'[{now_()}] [{l("party")}/{client.party.id}] [{display_name_}] {x}')
                    
            if data['fortnite']['blacklist-autokick'] is True and confirmation.user.id in blacklist:
                try:
                    await confirmation.reject()
                except fortnitepy.HTTPException:
                    if data['loglevel'] == "debug":
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    send(display_name,l("error_while_declining_partyrequest"),red,add_d=lambda x:f'>>> {x}')
            else:
                try:
                    await confirmation.confirm()
                except fortnitepy.HTTPException:
                    if data['loglevel'] == "debug":
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    send(display_name,l("error_while_accepting_partyrequest"),red,add_d=lambda x:f'>>> {x}')

        async def event_party_member_kick(self, member: fortnitepy.PartyMember) -> None:
            if member is None:
                return
            client=member.client
            if client.isready is False:
                return
            add_cache(client, member)
            display_name_ = is_most(client)
            if display_name_:
                if data['loglevel'] == 'normal':
                    send(display_name_,l("party_member_kick",name(member.party.leader),name(member),member.party.member_count),magenta,add_p=lambda x:f'[{now_()}] [{l("party")}] [{display_name_}] {x}')
                else:
                    send(display_name_,l("party_member_kick",f'{name(member.party.leader)} [{platform_to_str(member.party.leader.platform)}/{member.party.leader.input}]',f'{name(member)} [{platform_to_str(member.platform)}/{member.input}]',member.party.member_count),magenta,add_p=lambda x:f'[{now_()}] [{l("party")}/{client.party.id}] [{display_name_}] {x}')

        async def event_party_member_promote(self, old_leader: fortnitepy.PartyMember, new_leader: fortnitepy.PartyMember) -> None:
            global blacklist
            if old_leader is None or new_leader is None:
                return
            client=new_leader.client
            if client.isready is False:
                return
            add_cache(client, old_leader)
            add_cache(client, new_leader)
            display_name = name(client.user)
            display_name_ = is_most(client)
            try:
                if new_leader.id == client.user.id:
                    prop = {"VoiceChat:implementation_s": "VivoxVoiceChat"}
                    await client.party.patch(updated=prop)
            except Exception:
                if data['loglevel'] == 'debug':
                    send(name(client.user),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            if display_name_:
                if data['loglevel'] == 'normal':
                    send(display_name_,l("party_member_promote",name(old_leader),name(new_leader)),magenta,add_p=lambda x:f'[{now_()}] [{l("party")}] [{display_name_}] {x}')
                else:
                    send(display_name_,l("party_member_promote",f'{name(old_leader)} [{platform_to_str(old_leader.platform)}/{old_leader.input}]',f'{name(new_leader)} [{platform_to_str(new_leader.platform)}/{new_leader.input}]',magenta,add_p=lambda x:f'[{now_()}] [{l("party")}/{client.party.id}] [{display_name_}] {x}'))
            
            if new_leader.id == client.user.id:
                try:
                    await client.party.set_playlist(data['fortnite']['playlist'])
                    await client.party.set_privacy(data['fortnite']['privacy'])
                    for member in client.party.members.copy().values():
                        if member.id in blacklist:
                            if data['fortnite']['blacklist-autokick'] is True:
                                try:
                                    await member.kick()
                                except Exception:
                                    if data['loglevel'] == 'debug':
                                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                            if data['fortnite']['blacklist-autochatban'] is True:
                                try:
                                    await member.chatban()
                                except Exception:
                                    if data['loglevel'] == 'debug':
                                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                except fortnitepy.Forbidden:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

        async def event_party_member_update(self, member: fortnitepy.PartyMember) -> None:
            global blacklist
            if member is None:
                return
            client=member.client
            if client.isready is False:
                return
            add_cache(client, member)
            display_name = name(client.user)
            display_name_ = is_most(client)
            if display_name_:
                if data['loglevel'] != 'normal':
                    send(display_name_,l("party_member_update", f"{name(member)} [{platform_to_str(member.platform)}/{member.input}]"),magenta,add_p=lambda x:f'[{now_()}] [{l("party")}/{client.party.id}] [{display_name_}] {x}')
            
            if member.id == client.user.id:
                return
            if member.id in blacklist and client.party.me.leader is True:
                if data['fortnite']['blacklist-autokick'] is True:
                    try:
                        await member.kick()
                    except Exception:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    return
                if data['fortnite']['blacklist-autochatban'] is True:
                    try:
                        await member.chatban()
                    except Exception:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    return
            if member.outfit != client.prevoutfit or member.outfit_variants != client.prevoutfitvariants or member.enlightenments != client.prevenlightenments:
                if data['loglevel'] != 'normal':
                    if display_name_:
                        send(display_name_,member.outfit)
                if client.outfitmimic is True:
                    if member.outfit is None:
                        try:
                            await change_asset(client, client.user.id, "Outfit", "")
                        except Exception:
                            if data['loglevel'] == 'debug':
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    else:
                        try:
                            await change_asset(client, client.user.id, "Outfit", member.outfit, member.outfit_variants, member.enlightenments)
                        except Exception:
                            if data['loglevel'] == 'debug':
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            if partymember_backpack(member) != client.prevbackpack or member.backpack_variants != client.prevbackpackvariants:
                if data['loglevel'] != 'normal':
                    if display_name_:
                        send(display_name_,partymember_backpack(member))
                if client.backpackmimic is True:
                    if partymember_backpack(member) is None:
                        try:
                            await change_asset(client, client.user.id, "Back Bling", "")
                        except Exception:
                            if data['loglevel'] == 'debug':
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    else:
                        try:
                            type_ = convert_to_type(partymember_backpack(member))
                            await change_asset(client, client.user.id, type_, partymember_backpack(member), member.backpack_variants)
                        except Exception:
                            if data['loglevel'] == 'debug':
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            if member.pickaxe != client.prevpickaxe or member.pickaxe_variants != client.prevpickaxevariants:
                if data['loglevel'] != 'normal':
                    if display_name_:
                        send(display_name_,member.pickaxe)
                if client.pickaxemimic is True:
                    if member.pickaxe is None:
                        try:
                            await change_asset(client, client.user.id, "Harvesting Tool", "")
                        except Exception:
                            if data['loglevel'] == 'debug':
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    else:
                        try:
                            await change_asset(client, client.user.id, "Harvesting Tool", member.pickaxe, member.pickaxe_variants)
                        except Exception:
                            if data['loglevel'] == 'debug':
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            client.prevoutfit=member.outfit
            client.prevoutfitvariants=member.outfit_variants
            client.prevenlightenments=member.enlightenments
            client.prevbackpack=partymember_backpack(member)
            client.prevbackpackvariants=member.backpack_variants
            client.prevpickaxe=member.pickaxe
            client.prevpickaxevariants=member.pickaxe_variants

            if partymember_emote(member) is not None:
                if data['loglevel'] != 'normal':
                    if display_name_:
                        send(display_name_,partymember_emote(member))
                if client.emotemimic is True:
                    try:
                        type_ = convert_to_type(partymember_emote(member))
                        await change_asset(client, client.user.id, type_, partymember_emote(member))
                    except Exception:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

        async def event_party_member_disconnect(self, member: fortnitepy.PartyMember) -> None:
            if member is None:
                return
            client=member.client
            if client.isready is False:
                return
            add_cache(client, member)
            display_name = name(client.user)
            display_name_ = is_most(client)
            if display_name_:
                if data['loglevel'] == 'normal':
                    send(display_name_,l("party_member_disconnect",name(member)),magenta,add_p=lambda x:f'[{now_()}] [{l("party")}] [{display_name_}] {x}')
                else:
                    send(display_name_,l("party_member_disconnect",f'{name(member)} [{platform_to_str(member.platform)}/{member.input}]'),magenta,add_p=lambda x:f'[{now_()}] [{l("party")}/{client.party.id}] [{display_name_}] {x}')

            if client.party.me.leader is True:
                try:
                    await member.kick()
                except Exception:
                    if data['loglevel'] == "debug":
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

        async def event_party_member_chatban(self, member: fortnitepy.PartyMember, reason: Optional[str]) -> None:
            if member is None:
                return
            client=member.client
            if client.isready is False:
                return
            add_cache(client, member)
            display_name_ = is_most(client)
            if display_name_:
                if data['loglevel'] == 'normal':
                    if reason is None:
                        send(display_name_,l("party_member_chatban",name(member.party.leader),name(member)),magenta,add_p=lambda x:f'[{now_()}] [{l("party")}] [{display_name_}] {x}')
                    else:
                        send(display_name_,l("party_member_chatban2",name(member.party.leader),name(member),reason),magenta,add_p=lambda x:f'[{now_()}] [{l("party")}] [{display_name_}] {x}')
                else:
                    if reason is None:
                        send(display_name_,l("party_member_chatban",name(member.party.leader),name(member)),magenta,add_p=lambda x:f'[{now_()}] [{l("party")}/{client.party.id}] [{display_name_}] {x}')
                    else:
                        send(display_name_,l("party_member_chatban2",f'{name(member.party.leader)} [{platform_to_str(member.party.leader.platform)}/{member.party.leader.input}]',f'{name(member)} [{platform_to_str(member.platform)}/{member.input}]',reason),magenta,add_p=lambda x:f'[{now_()}] [{l("party")}/{client.party.id}] [{display_name_}] {x}')

        async def event_party_update(self, party: fortnitepy.Party) -> None:
            if party is None:
                return
            client=party.client
            if client.isready is False:
                return
            display_name_ = is_most(client)
            if display_name_:
                if data['loglevel'] != 'normal':
                    send(display_name_,l("party_update"),magenta,add_p=lambda x:f'[{now_()}] [{l("party")}/{client.party.id}] [{display_name_}] {x}')

        async def event_friend_message(self, message: fortnitepy.FriendMessage) -> None:
            await process_command(message)

        async def event_party_message(self, message: fortnitepy.PartyMessage) -> None:
            await process_command(message)

if True:
    def l(key: str, *args: Any, **kwargs: Any) -> Optional[str]:
        text = localize.get(key)
        if text is not None:
            return text.format(*args, **kwargs)
        else:
            return None

    def name(user: Union[Type[fortnitepy.user.UserBase], Type[discord.user.User], Type[WebUser]]) -> str:
        if data['loglevel'] == 'normal':
            return user.display_name
        else:
            return f"{user.display_name} / {user.id}"

    def dstore(username: str, content: Any) -> None:
        if data.get('discord-log',False) is True:
            if data.get('hide-email',False) is True:
                for email in data['fortnite']['email'].split(','):
                    content=content.replace(email,len(email)*"X")
            if data.get('hide-password',False) is True:
                for password in data['fortnite']['password'].split(','):
                    content=content.replace(password,len(password)*"X")
            if data.get('hide-token',False) is True:
                for token in data['discord']['token'].split(','):
                    content=content.replace(token,len(token)*"X")
            if data.get('hide-webhook',False) is True:
                for webhook in data['webhook'].split(','):
                    content=content.replace(webhook,len(webhook)*"X")
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

    def dprint() -> None:
        global kill
        while True:
            if kill is True:
                sys.exit(0)
            if data.get('discord-log',False) is True:
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
                        if r.status_code == 204:
                            storedlog.remove(send)
                        if r.status_code == 429:
                            break
                    except TypeError:
                        if data['loglevel'] == 'debug':
                            send(l("bot"),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        try:
                            storedlog.remove(send)
                        except Exception:
                            pass
                        continue
                    except Exception:
                        send(l("bot"),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        send(l("bot"),f"{username}: {content} の送信中にエラーが発生しました",red,add_d=lambda x:f'>>> {x}')
                        continue
                time.sleep(5)

    def send(user_name: str, content: Any, color: Optional[Callable] = None, add_p: Optional[Callable] = None, add_d: Optional[Callable] = None) -> Optional[str]:
        content = str(content)
        if data.get('no-logs',False) is False or color is red:
            if color is None:
                if add_p is None:
                    print(content)
                else:
                    print(add_p(content))
            else:
                if add_p is None:
                    print(color(content))
                else:
                    print(color(add_p(content)))
        if add_d is None:
            dstore(user_name,content)
        else:
            dstore(user_name,add_d(content))

    def is_most(client: Type[fortnitepy.Client]) -> None:
        name=client.user.display_name
        member_joined_at_most=[client.user.id, getattr(client.party.me, "joined_at", datetime.datetime.now())]
        for member_ in client.party.members.copy().values():
            add_cache(client, member_)
            try:
                if member_.id in [i.user.id for i in loadedclients]:
                    if member_.id != client.user.id:
                        name+=f"/{str(member_.display_name)}"
                    if member_.joined_at < member_joined_at_most[1]:
                        member_joined_at_most=[member_.id, getattr(member_, "joined_at", datetime.datetime.now())]
            except Exception:
                if data['loglevel'] == 'debug':
                    send(name(client.user),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
        if client.user.id == member_joined_at_most[0]:
            return name
        return None

    def get_device_auth_details() -> None:
        if os.path.isfile(filename):
            with open(filename, 'r') as fp:
                return json.load(fp)
        return {}

    def store_device_auth_details(email: str, details: dict) -> None:
        existing = get_device_auth_details()
        existing[email.lower()] = details
        with open(filename, 'w') as fp:
            json.dump(existing, fp)

    def now_() -> str:
        return datetime.datetime.now().strftime('%H:%M:%S')

    def platform_to_str(platform: fortnitepy.Platform) -> Optional[str]:
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

    def convert_to_type(text: str) -> Optional[str]:
        if True in [text.lower() in commands[key].split(",") for key in ("cid", "outfit", "alloutfit", "outfitasset")] or text.lower().startswith("cid_"):
            return "Outfit"
        elif True in [text.lower() in commands[key].split(",") for key in ("bid", "backpack", "allbackpack", "backpackasset")] or text.lower().startswith("bid_"):
            return "Back Bling"
        elif True in [text.lower() in commands[key].split(",") for key in ("petcarrier", "pet", "allpet")] or text.lower().startswith("petcarrier_"):
            return "Pet"
        elif True in [text.lower() in commands[key].split(",") for key in ("pickaxe_id", "pickaxe", "allpickaxe", "pickaxeasset")] or text.lower().startswith("pickaxe_id"):
            return "Harvesting Tool"
        elif True in [text.lower() in commands[key].split(",") for key in ("eid", "emote", "allemote", "emoteasset")] or text.lower().startswith("eid_"):
            return "Emote"
        elif True in [text.lower() in commands[key].split(",") for key in ("emoji_id", "emoji", "allemoji")] or text.lower().startswith("emoji_"):
            return "Emoticon"
        elif True in [text.lower() in commands[key].split(",") for key in ("toy_id", "toy", "alltoy")] or text.lower().startswith("toy_"):
            return "Toy"
        elif True in [text.lower() in commands[key].split(",") for key in ("id", "item")]:
            return "Item"

    def convert_to_asset(text: str) -> Optional[str]:
        if True in [text.lower() in commands[key].split(",") for key in ("cid", "outfit", "alloutfit", "outfitasset")] or text.lower().startswith("cid_"):
            return "outfit"
        elif True in [text.lower() in commands[key].split(",") for key in ("bid", "backpack", "allbackpack", "backpackasset")] or text.lower().startswith("bid_"):
            return "backpack"
        elif True in [text.lower() in commands[key].split(",") for key in ("petcarrier", "pet", "allpet")] or text.lower().startswith("petcarrier_"):
            return "backpack"
        elif True in [text.lower() in commands[key].split(",") for key in ("pickaxe_id", "pickaxe", "allpickaxe", "pickaxeasset")] or text.lower().startswith("pickaxe_id"):
            return "pickaxe"
        elif True in [text.lower() in commands[key].split(",") for key in ("eid", "emote", "allemote", "emoteasset")] or text.lower().startswith("eid_"):
            return "emote"
        elif True in [text.lower() in commands[key].split(",") for key in ("emoji_id", "emoji", "allemoji")] or text.lower().startswith("emoji_"):
            return "emote"
        elif True in [text.lower() in commands[key].split(",") for key in ("toy_id", "toy", "alltoy")] or text.lower().startswith("toy_"):
            return "emote"

    def convert_to_id(text: str) -> Optional[str]:
        if True in [text.lower() in commands[key].split(",") for key in ("cid", "outfit", "alloutfit", "outfitasset")] or text.lower().startswith("cid_"):
            return "cid"
        elif True in [text.lower() in commands[key].split(",") for key in ("bid", "backpack", "allbackpack", "backpackasset")] or text.lower().startswith("bid_"):
            return "bid"
        elif True in [text.lower() in commands[key].split(",") for key in ("petcarrier", "pet", "allpet")] or text.lower().startswith("petcarrier_"):
            return "petcarrier"
        elif True in [text.lower() in commands[key].split(",") for key in ("pickaxe_id", "pickaxe", "allpickaxe", "pickaxeasset")] or text.lower().startswith("pickaxe_id"):
            return "pickaxe_id"
        elif True in [text.lower() in commands[key].split(",") for key in ("eid", "emote", "allemote", "emoteasset")] or text.lower().startswith("eid_"):
            return "eid"
        elif True in [text.lower() in commands[key].split(",") for key in ("emoji_id", "emoji", "allemoji")] or text.lower().startswith("emoji_"):
            return "emoji_id"
        elif True in [text.lower() in commands[key].split(",") for key in ("toy_id", "toy", "alltoy")] or text.lower().startswith("toy_"):
            return "toy_id"
        elif True in [text.lower() in commands[key].split(",") for key in ("id", "item")]:
            return "id"

    def convert_to_old_type(text: str) -> Optional[str]:
        if text.lower() == "outfit":
            return "outfit"
        elif text.lower() == "back bling":
            return "backpack"
        elif text.lower() == "pet":
            return "pet"
        elif text.lower() == "harvesting tool":
            return "pickaxe"
        elif text.lower() == "emote":
            return "emote"
        elif text.lower() == "emoticon":
            return "emoji"
        elif text.lower() == "toy":
            return "toy"
        elif text.lower() == "item":
            return "item"

    def convert_to_new_type(text: str) -> Optional[str]:
        if text.lower() == "outfit":
            return "Outfit"
        elif text.lower() == "backpack":
            return "Back Bling"
        elif text.lower() == "pet":
            return "Pet"
        elif text.lower() == "pickaxe":
            return "Harvesting Tool"
        elif text.lower() == "emote":
            return "Emote"
        elif text.lower() == "emoji":
            return "Emoticon"
        elif text.lower() == "toy":
            return "Toy"
        elif text.lower() == "item":
            return "Item"

    def convert_variant(type_: str, variants: dict) -> List[dict]:
        result = []
        for variant in variants:
            for option in variant['options']:
                result.append({"name": option['name'], 'variants': [{'item': type_, 'channel': variant['channel'], 'variant': option['tag']}]})
        return result

    def convert_backend_type(backendType: str) -> str:
        converter = {
            "AthenaBackpack": "Back Bling",
            "AthenaPickaxe": "Harvesting Tool",
            "AthenaItemWrap": "Wrap",
            "AthenaGlider": "Glider",
            "AthenaCharacter": "Outfit",
            "AthenaPet": "Pet",
            "AthenaMusicPack": "Music",
            "AthenaLoadingScreen": "Loading Screen",
            "AthenaDance": "Emote",
            "AthenaSpray": "Spray",
            "AthenaEmoji": "Emoticon",
            "AthenaSkyDiveContrail": "Contrail",
            "AthenaPetCarrier": "Pet",
            "AthenaToy": "Toy",
            "AthenaConsumableEmote": "Emote",
            "AthenaBattleBus": "Battle Bus",
            "AthenaRewardEventGraphCosmetic": "Outfit",
            "AthenaVictoryPose": "Emote"
        }
        return converter.get(backendType)

    def inviteaccept(client: Type[fortnitepy.Client]) -> None:
        send(name(client.user),l("inviteaccept"),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
        client.acceptinvite=True

    def inviteinterval(client: Type[fortnitepy.Client]) -> None:
        send(name(client.user),l("inviteinterval"),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
        client.acceptinvite_interval=True

    def render_template(file_: str, **kwargs: Any) -> str:
        template = env.get_template(file_)
        return sanic.response.html(template.render(**kwargs))

    def load_config(client: Optional[Type[fortnitepy.Client]] = None) -> bool:
        global data
        global credentials
        global commands
        global localize
        global replies
        global error_config
        global error_commands
        try:
            try:
                with open('config.json', 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except json.decoder.JSONDecodeError:
                with open('config.json', 'r', encoding='utf-8-sig') as f:
                    data = json.load(f)
            if data.get('loglevel','normal') == 'debug':
                send('ボット',f'\n{json.dumps(data, indent=4)}\n',yellow,add_d=lambda x:f'\n```{x}```\n')
            error_flag = False
            error_keys = []
            for key in config_tags.keys():
                try:
                    exec(f"errorcheck=data{key}")
                except KeyError as e:
                    error_flag = True
                    error_keys.append(str(e))
                    error_config.append(key)
            for key in data.get('fortnite',{}).get('blacklist',[]).copy():
                if len(key) == 0:
                    data.get('fortnite',{}).get('blacklist',[]).remove(key)
            
            for key in data.get('fortnite',{}).get('whitelist',[]).copy():
                if len(key) == 0:
                    data.get('fortnite',{}).get('whitelist',[]).remove(key)
            
            for key in data.get('fortnite',{}).get('invitelist',[]).copy():
                if len(key) == 0:
                    data.get('fortnite',{}).get('invitelist',[]).remove(key)
            
            for key in data.get('fortnite',{}).get('otherbotlist',[]).copy():
                if len(key) == 0:
                    data.get('fortnite',{}).get('otherbotlist',[]).remove(key)
            
            for key in data.get('discord',{}).get('blacklist',[]).copy():
                if len(str(key)) == 0:
                    data.get('discord',{}).get('blacklist',[]).remove(key)
            
            for key in data.get('discord',{}).get('whitelist',[]).copy():
                if len(str(key)) == 0:
                    data.get('discord',{}).get('whitelist',[]).remove(key)
            
            with open('config.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4, sort_keys=False)
            data['web']=data.get('web',{})
            data['web']['ip']=data['web'].get('ip','{ip}')
            data['web']['port']=data['web'].get('port',8080)
            data['web']['login_required']=data['web'].get('login_required',False)
            data['lang']=data.get('lang','en')
            data['loglevel']=data.get('loglevel','normal')
            credentials={}
            if error_flag is True:
                send('ボット',f'config.json ファイルの読み込みに失敗しました。キーの名前が間違っていないか確認してください。アップデート後の場合は、最新のconfig.jsonファイルを確認してください\n{", ".join(error_keys)} がありません',red,add_d=lambda x:f'>>> {x}')
                send('Bot',f'Failed to load config.json file. Make sure key name is correct. If this after update, plase check latest config.json file\n{", ".join(error_keys)} is missing',red,add_d=lambda x:f'>>> {x}')
            else:
                flag = False
                try:
                    errorcheck=requests.get('https://benbotfn.tk/api/v1/cosmetics/br/DOWN_CHECK')
                except Exception:
                    if data['loglevel'] == 'debug':
                        send('ボット',traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    flag = True
                else:
                    if errorcheck.status_code == 503:
                        flag = True
                if flag is True:
                    if os.path.isfile('allen.json') is False or os.path.isfile('allja.json') is False:
                        send('ボット','APIがダウンしています。しばらく待ってからもう一度起動してみてください',red,add_d=lambda x:f'>>> {x}')
                        send('Bot','API is dawning. Please try again later',red,add_d=lambda x:f'>>> {x}')
                        return False
                    else:
                        send('ボット','APIがダウンしているため、最新のアイテムデータをダウンロードできませんでした。しばらく待ってからもう一度起動してみてください',red,add_d=lambda x:f'>>> {x}')
                        send('Bot','Failed to download latest item data because API is dawning. Please try again later',red,add_d=lambda x:f'>>> {x}')
                            
                try:
                    for count,mail in enumerate(data['fortnite']['email'].split(',')):
                        credentials[mail]=data['fortnite']['password'].split(',')[count]
                except IndexError:
                    if data['loglevel'] == 'debug':
                        send('ボット',traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    send('ボット','メールアドレスの数に対しパスワードの数が足りません。読み込めたアカウントのみ起動されます',red,add_d=lambda x:f'>>> {x}')
                    send('Bot','There are not enough passwords for the number of email addresses. Boot only loaded accounts',red,add_d=lambda x:f'>>> {x}')
        except json.decoder.JSONDecodeError as e:
            send('ボット',f'{traceback.format_exc()}\n{e}',red,add_d=lambda x:f'>>> {x}')
            send('ボット','config.json ファイルの読み込みに失敗しました。正しく書き込めているか確認してください',red,add_d=lambda x:f'>>> {x}')
            send('Bot','Failed to load config.json file. Make sure you wrote correctly',red,add_d=lambda x:f'>>> {x}')
            return False
        except FileNotFoundError:
            send('ボット',traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            send('ボット','config.json ファイルが存在しません',red,add_d=lambda x:f'>>> {x}')
            send('Bot','config.json file does not exist',red,add_d=lambda x:f'>>> {x}')
            return False

        if data.get("status",1) == 0:
            config_tags["['fortnite']['email']"].append("red")
            config_tags["['fortnite']['password']"].append("red")
            config_tags["['lang']"].append("red")

        data['fortnite']['privacy']=eval(f"fortnitepy.PartyPrivacy.{data.get('fortnite',{}).get('privacy','public').upper()}")
        if os.getcwd().startswith('/app') or os.getcwd().startswith('/home/runner'):
            data['web']['ip']="0.0.0.0"
        else:
            data['web']['ip']=data['web']['ip'].format(ip=socket.gethostbyname(socket.gethostname()))
        if client is not None:
            client.eid=data['fortnite']['eid']
            client.whisper=data['fortnite']['whisper']
            client.partychat=data['fortnite']['partychat']
            client.discord=data['discord']['discord']
            client.web=data['web']['web']
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

        if os.path.isfile(f"lang/{data['lang']}.json"):
            try:
                try:
                    with open(f'lang/{data["lang"]}.json', 'r', encoding='utf-8') as f:
                        localize = json.load(f)
                except json.decoder.JSONDecodeError:
                    with open(f'lang/{data["lang"]}.json', 'r', encoding='utf-8-sig') as f:
                        localize = json.load(f)
                if data['loglevel'] == 'debug':
                    send('ボット',f'\n{json.dumps(localize, indent=4)}\n',yellow,add_d=lambda x:f'\n```{x}```\n')
                for key in localizekeys:
                    exec(f"errorcheck=localize['{key}']")
            except KeyError as e:
                send('ボット',traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                send('ボット',f'{data["lang"]}.json ファイルの読み込みに失敗しました。キーの名前が間違っていないか確認してください\n{str(e)} がありません',red,add_d=lambda x:f'>>> {x}')
                send('Bot',f'Failed to load {data["lang"]}.json file. Make sure key name is correct\n{str(e)} is missing',add_d=lambda x:f'>>> {x}')
                return False
            except json.decoder.JSONDecodeError as e:
                send('ボット',f'{traceback.format_exc()}\n{e}',red,add_d=lambda x:f'>>> {x}')
                send('ボット',f'{data["lang"]}.json ファイルの読み込みに失敗しました。正しく書き込めているか確認してください\n',red,add_d=lambda x:f'>>> {x}')
                send('Bot',f'Failed to load {data["lang"]}.json file. Make sure you wrote correctly',red,add_d=lambda x:f'>>> {x}')
                return False
            except FileNotFoundError:
                send('ボット',f'{traceback.format_exc()}\n{e}',red,add_d=lambda x:f'>>> {x}')
                send('ボット',f'{data["lang"]}.json ファイルが存在しません',red,add_d=lambda x:f'>>> {x}')
                send('Bot',f'{data["lang"]}.json file does not exist',red,add_d=lambda x:f'>>> {x}')
                return False
        else:
            try:
                try:
                    with open('lang/en.json', 'r', encoding='utf-8') as f:
                        localize = json.load(f)
                except json.decoder.JSONDecodeError:
                    with open('lang/en.json', 'r', encoding='utf-8-sig') as f:
                        localize = json.load(f)
                if data.get('loglevel','normal') == 'debug':
                    send('ボット',f'\n{json.dumps(localize, indent=4)}\n',yellow,add_d=lambda x:f'\n```{x}```\n')
                for key in localizekeys:
                    exec(f"errorcheck=localize['{key}']")
            except KeyError as e:
                send('ボット',traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                send('ボット',f'en.json ファイルの読み込みに失敗しました。キーの名前が間違っていないか確認してください\n{str(e)} がありません',add_d=lambda x:f'>>> {x}')
                send('Bot',f'Failed to load en.json file. Make sure key name is correct\n{str(e)} is missing',add_d=lambda x:f'>>> {x}')
                return False
            except json.decoder.JSONDecodeError as e:
                send('ボット',f'{traceback.format_exc()}\n{e}',red,add_d=lambda x:f'>>> {x}')
                send('ボット',f'en.json ファイルの読み込みに失敗しました。正しく書き込めているか確認してください\n',red,add_d=lambda x:f'>>> {x}')
                send('Bot',f'Failed to load en.json file. Make sure you wrote correctly',red,add_d=lambda x:f'>>> {x}')
                return False
            except FileNotFoundError:
                send('ボット',f'{traceback.format_exc()}\n{e}',red,add_d=lambda x:f'>>> {x}')
                send('ボット',f'en.json ファイルが存在しません',red,add_d=lambda x:f'>>> {x}')
                send('Bot',f'en.json file does not exist',red,add_d=lambda x:f'>>> {x}')
                return False

        try:
            try:
                with open('commands.json', 'r', encoding='utf-8') as f:
                    commands=json.load(f)
            except json.decoder.JSONDecodeError:
                with open('commands.json', 'r', encoding='utf-8-sig') as f:
                    commands=json.load(f)
            if data['loglevel'] == 'debug':
                send(l('bot'),f'\n{json.dumps(commands, indent=4)}\n',yellow,add_d=lambda x:f'\n```{x}```\n')
            error_flag = False
            error_keys = []
            for key in commands_tags.keys():
                try:
                    exec(f"errorcheck=commands{key}")
                except KeyError as e:
                    error_flag = True
                    error_keys.append(str(e))
                    error_commands.append(key)
            if error_flag is True:
                send(l('bot'),f'{l("load_failed_keyerror", "commands.json")}\n{l("is_missing", ", ".join(error_keys))}',red,add_d=lambda x:f'>>> {x}')
            if data.get('caseinsensitive',False) is True:
                commands=dict((k.lower(), jaconv.kata2hira(v.lower())) for k,v in commands.items())
            error_flag = False
            if commands.get('ownercommands','') != '':
                for checks in commands.items():
                    if checks[0] in ignore:
                        continue
                    for command in commands['ownercommands'].split(','):
                        try:
                            errorcheck=commands[command.lower()]
                        except KeyError:
                            if error_flag is False:
                                error_flag = True
                                error_commands.append("['ownercommands']")
            if error_flag is True:
                send(l('bot'),l('failed_ownercommand'),red,add_d=lambda x:f'>>> {x}')
                send(l('bot'),l('is_missing',e),red,add_d=lambda x:f'>>> {x}')
        except json.decoder.JSONDecodeError as e:
            send(l('bot'),f'{traceback.format_exc()}\n{e}',red,add_d=lambda x:f'>>> {x}')
            send(l('bot'),l("load_failed_json", "commands.json"),red,add_d=lambda x:f'>>> {x}')
            return False
        except FileNotFoundError:
            send(l('bot'),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            send(l('bot'),l("load_failed_notfound", "commands.json"),red,add_d=lambda x:f'>>> {x}')
            return False

        try:
            try:
                with open('replies.json', 'r', encoding='utf-8') as f:
                    replies=json.load(f)
            except json.decoder.JSONDecodeError:
                with open('replies.json', 'r', encoding='utf-8-sig') as f:
                    replies=json.load(f)
            if data['loglevel']== 'debug':
                send(l('bot'),f'\n{json.dumps(replies, indent=4)}\n',yellow,add_d=lambda x:f'\n```{x}```\n')
            if data.get('caseinsensitive') is True:
                replies=dict((jaconv.kata2hira(k.lower()), v) for k,v in replies.items())
        except json.decoder.JSONDecodeError as e:
            send(l('bot'),f'{traceback.format_exc()}\n{e}',red,add_d=lambda x:f'>>> {x}')
            send(l('bot'),l("load_failed_json", "replies.json"),red,add_d=lambda x:f'>>> {x}')
            return False
        except FileNotFoundError:
            send(l('bot'),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            send(l('bot'),l("load_failed_notfound", "replies.json"),red,add_d=lambda x:f'>>> {x}')
            return False
        return True

    def get_item_info() -> None:
        try:
            os.makedirs("items", exist_ok=True)
            ignoretype = [
                "Contrail",
                "Glider",
                "Wrap",
                "Loading Screen",
                "Music",
                "Spray",
                "Battle Bus"
            ]
            req=requests.get('https://benbotfn.tk/api/v1/cosmetics/br', params={"lang": "en"})
            if req.status_code == 200:
                data_ = {}
                allcosmen=req.json()
                for item in allcosmen:
                    type_ = convert_backend_type(item['backendType'])
                    if type_ not in ignoretype:
                        if data_.get(type_) is None:
                            data_[type_] = []
                        data_[type_].append(item)
                for k,v in data_.items():
                    with open(f'items/all{k}_en.json', 'w') as f:
                        json.dump(v, f)
            if data["lang"] != "en":
                req=requests.get(f'https://benbotfn.tk/api/v1/cosmetics/br', params={"lang": data["lang"]})
                if req.status_code == 200:
                    data_ = {}
                    allcosm=req.json()
                    for item in allcosm:
                        type_ = convert_backend_type(item['backendType'])
                        if type_ not in ignoretype:
                            if data_.get(type_) is None:
                                data_[type_] = []
                            data_[type_].append(item)
                    for k,v in data_.items():
                        with open(f'items/all{k}_{data["lang"]}.json', 'w') as f:
                            json.dump(v, f)
        except UnicodeEncodeError:
            if data['loglevel'] == 'debug':
                send(l('bot'),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
        except Exception:
            send(l('bot'),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

    def add_cache(client: Type[fortnitepy.Client], user: Type[fortnitepy.user.UserBase]) -> None:
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
        except Exception:
            send(l('bot'),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

    def partymember_backpack(member: Type[fortnitepy.party.PartyMemberBase]) -> str:
        asset = member.meta.backpack
        result = re.search(r".*\.([^\'\"]*)", asset.strip("'"))
        if result is not None and result.group(1) != 'None':
            return result.group(1)

    def partymember_emote(member: Type[fortnitepy.party.PartyMemberBase]) -> str:
        asset = member.meta.emote
        result = re.search(r".*\.([^\'\"]*)", asset.strip("'"))
        if result is not None and result.group(1) != 'None':
            return result.group(1)

    def member_asset(member: Type[fortnitepy.party.PartyMemberBase], asset: str) -> str:
        if asset in ("backpack", "pet"):
            return partymember_backpack(member)
        elif asset in ("emote", "emoji", "toy"):
            return partymember_emote(member)
        else:
            return getattr(member, asset)

    def lock_check(client: Type[fortnitepy.Client], author_id: str) -> bool:
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

    def search_item(lang: str, mode: str, text: str, type_: Optional[str] = None, cache: Optional[bool] = True) -> Optional[List[dict]]:
        ignoretype = [
            "Contrail",
            "Glider",
            "Wrap",
            "Loading Screen",
            "Music",
            "Spray",
            "Battle Bus"
        ]
        itemlist = []
        if cached_items.get(lang) is None:
            cached_items[lang] = []
        if cache is True:
            if mode == 'set':
                data_ = cached_items[lang]
            else:
                data_ = [i for i in cached_items[lang] if convert_backend_type(i["backendType"]) in type_.split(',')]
        else:
            data_ = []
            if type_ not in ["Item", None]:
                with ThreadPoolExecutor() as executor:
                    def _open_file(filename: str) -> Union[list, dict]:
                        with open(filename, 'r', encoding='utf-8') as f:
                            d = json.load(f)
                        return d
                    futures = [executor.submit(_open_file,f'items/all{i}_{lang}.json') for i in type_.split(',')]
                    for future in futures:
                        data_.extend(future.result())
            else:
                with ThreadPoolExecutor() as executor:
                    def _open_file(filename: str) -> Union[list, dict]:
                        with open(filename, 'r', encoding='utf-8') as f:
                            d = json.load(f)
                        return d
                    def _(text: str) -> str:
                        return re.sub(r"items(\\|/)all","",text).replace(f"_{lang}.json","")
                    futures = [executor.submit(_open_file,f'items/all{_(i)}_{lang}.json') for i in glob(f"items/all*_{lang}.json") if _(i)[0].isupper()]
                    for future in futures:
                        data_.extend(future.result())
        for item in data_:
            try:
                if convert_backend_type(item["backendType"]) in ignoretype or item in itemlist or item.get("name") is None:
                    continue
                if mode == "name":
                    if data['caseinsensitive'] is True:
                        text_ = jaconv.hira2kata(text.lower())
                        name = jaconv.hira2kata(item['name'].lower())
                    else:
                        text_ = text
                        name = item['name']
                    if text_ in name:
                        itemlist.append(item)
                elif mode == "id":
                    text_ = text
                    if text_.lower() in item['id'].lower():
                        itemlist.append(item)
                elif mode == "set":
                    if item.get('set') is None:
                        continue
                    if data['caseinsensitive'] is True:
                        text_ = jaconv.hira2kata(text.lower())
                        name = jaconv.hira2kata(item['set'].lower())
                    else:
                        text_ = text
                        name = item['set']
                    if text_ in name:
                        itemlist.append(item)
            except Exception:
                send(l("bot"),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                send(l("bot"),item,red,add_d=lambda x:f'>>> {x}')
        if len(itemlist) == 0:
            if cache is True:
                return search_item(lang=lang, mode=mode, text=text, type_=type_, cache=False)
            else:
                return None
        else:
            if cache is False:
                for item in itemlist:
                    if item not in cached_items[lang]:
                        cached_items[lang].append(item)
            return itemlist

    def search_style(lang: str, id_: str, type_: str, cache: Optional[bool] = True) -> Optional[List[dict]]:
        if cached_items.get(lang) is None:
            cached_items[lang] = []
        if cache is True:
            data_ = cached_items[lang]
        else:
            data_ = []
            if type_ != "Item":
                with ThreadPoolExecutor() as executor:
                    def _open_file(filename: str) -> Union[list, dict]:
                        with open(filename, 'r', encoding='utf-8') as f:
                            d = json.load(f)
                        return d
                    futures = [executor.submit(_open_file,f'items/all{i}_{lang}.json') for i in type_.split(',')]
                    for future in futures:
                        data_.extend(future.result())
            else:
                with ThreadPoolExecutor() as executor:
                    def _open_file(filename: str) -> Union[list, dict]:
                        with open(filename, 'r', encoding='utf-8') as f:
                            d = json.load(f)
                        return d
                    def _(text: str) -> str:
                        return re.sub(r"items(\\|/)all","",text).replace(f"_{lang}.json","")
                    futures = [executor.submit(_open_file,f'items/all{_(i)}_{lang}.json') for i in glob(f"items/all*_{lang}.json") if _(i)[0].isupper()]
                    for future in futures:
                        data_.extend(future.result())
        variants = None
        for item in data_:
            if item['id'].lower() == id_.lower():
                if item['variants'] is not None:
                    variants = convert_variant(item['backendType'], item['variants'])
                    break
        if variants is None:
            if cache is True:
                return search_style(lang=lang, id_=id_, type_=type_, cache=False)
            else:
                return None
        else:
            if cache is False:
                if item not in cached_items[lang]:
                    cached_items[lang].append(item)
            return variants

    def generate_device_auth_and_store(email: str) -> str:
        access_token, expires_at = get_token()
        while True:
            flag = False
            while True:
                device_auth_detail = get_device_code(access_token)
                send(l('bot'),l('get_code', email, device_auth_detail['verification_uri_complete']))
                device_auth = device_code_auth(device_auth_detail["device_code"])
                fortnite_access_token, fortnite_expires_at = get_fortnite_token(device_auth["access_token"])
                if device_auth is None:
                    send(l('bot'),l('authorization_expired'))
                    if expires_at < datetime.datetime.utcnow():
                        access_token, expires_at = get_token()
                else:
                    if fortnite_expires_at < datetime.datetime.utcnow():
                        fortnite_access_token, fortnite_expires_at = get_fortnite_token(device_auth["access_token"])
                    user = lookup_user(device_auth["in_app_id"], fortnite_access_token)
                    if user["email"].lower() == email.lower():
                        flag = True
                        break
                    else:
                        send(l('bot'),l('account_incorrect1', email))
                        break
            if flag == True:
                break
        exchange_code = exchange(device_auth["access_token"])
        launcher_access_token, client_id = exchange_code_auth(exchange_code)
        details = generate_device_auth(client_id, launcher_access_token)
        store_device_auth_details(email.lower(), details)
        return details
                
    def get_token() -> tuple:
        res = requests.post(
            oauth_url,
            headers={
                "Authorization": f"basic {launcher_token}"
            },
            data={
                "grant_type": "client_credentials",
                "token_type": "eg1"
            }
        )
        data = res.json()
        return data["access_token"], datetime.datetime.fromisoformat(data["expires_at"].replace("Z",""))

    def get_fortnite_token(access_token: str) -> tuple:
        exchange_code = exchange(access_token)
        res = requests.post(
            fortnite_token_url,
            headers={
                "Authorization": f"basic {fortnite_token}"
            },
            data={
                "grant_type": "exchange_code",
                "token_type": "eg1",
                "exchange_code": exchange_code
            }
        )
        data = res.json()
        return data["access_token"], datetime.datetime.fromisoformat(data["expires_at"].replace("Z",""))

    def get_device_code(access_token: str) -> dict:
        res = requests.post(
            device_auth_url,
            headers={
                "Authorization": f"bearer {access_token}"
            }
        )
        return res.json()

    def device_code_auth(device_code: str) -> Optional[dict]:
        flag = False
        while True:
            time.sleep(5)
            res = requests.post(
                oauth_url,
                headers={
                    "Authorization": f"basic {launcher_token}"
                },
                data={
                    "grant_type": "device_code",
                    "device_code": device_code
                }
            )
            device_auth = res.json()

            if device_auth.get("errorCode") == "errors.com.epicgames.account.oauth.authorization_pending":
                if not flag:
                    send(l('bot'),l('waiting_for_authorization'))
                    flag = True
                pass
            elif device_auth.get("errorCode") is not None:
                return None
            else:
                return device_auth

    def exchange_code_auth(exchange_code: str) -> tuple:
        res = requests.post(
            exchange_auth_url,
            headers={
                "Authorization": f"basic {launcher_token}"
            },
            data={
                "grant_type": "exchange_code",
                "exchange_code": exchange_code,
                "token_type": "eg1"
            }
        )
        data = res.json()
        return data["access_token"], data["account_id"]

    def exchange(access_token: str) -> str:
        res = requests.get(
            exchange_url,
            headers={
                "Authorization": f"bearer {access_token}"
            }
        )
        return res.json()["code"]

    def lookup_user(user_id: str, fortnite_access_token: str) -> dict:
        res = requests.get(
            user_lookup_url.format(user_id=user_id),
            headers={
                "Authorization": f"bearer {fortnite_access_token}"
            }
        )
        data = res.json()
        return data

    def generate_device_auth(client_id: str, access_token: str) -> dict:
        res = requests.post(
            f"https://account-public-service-prod.ol.epicgames.com/account/api/public/account/{client_id}/deviceAuth",
            headers={
                "Authorization": f"Bearer {access_token}"
            }
        )
        data = res.json()
        return {"device_id": data["deviceId"], "account_id": data["accountId"], "secret": data["secret"]}

    def uptime() -> None:
        while True:
            requests.head(f"http://{data['web']['ip']}:{data['web']['port']}")
            time.sleep(3)

    def restart(sleep_time: Optional[Union[int,float]] = 0) -> None:
        if sleep_time > 0:
            time.sleep(sleep_time)
        os.chdir(os.getcwd())
        os.execv(os.sys.executable,['python', *sys.argv])

if True:
    async def reply(message: Union[Type[fortnitepy.message.MessageBase], Type[discord.Message], Type[WebMessage]], client: Type[fortnitepy.Client], content: str) -> None:
        if isinstance(message, fortnitepy.message.MessageBase) is True:
            await message.reply(content)
        elif isinstance(message, discord.Message) is True:
            await message.channel.send(content)
        elif isinstance(message, WebMessage) is True:
            await message.reply(content)
        elif isinstance(message, AllMessage) is True:
            await message.reply(content, client)

    async def change_asset(client: Type[fortnitepy.Client], author_id: str, type_: str, id_: str, variants_: Optional[dict] = {}, enlightenment: Optional[Union[tuple, list]] = []) -> None:
        global blacklist
        global blacklist_
        global whitelist
        global whitelist_
        if not enlightenment:
            enlightenment = None
        if type_ == "Outfit":
            flag = False
            if client.outfitlock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                return False
            else:
                if 'banner' in id_:
                    variants = client.party.me.create_variants(item="AthenaCharacter", profile_banner='ProfileBanner')
                    variants += variants_ 
                else:
                    variants = variants_
                await client.party.me.edit_and_keep(partial(client.party.me.set_outfit, asset=id_, variants=variants, enlightenment=enlightenment))
        elif type_ == "Back Bling":
            flag = False
            if client.backpacklock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                return False
            else:
                if 'banner' in id_:
                    variants = client.party.me.create_variants(item="AthenaBackpack", profile_banner='ProfileBanner')
                    variants += variants_ 
                else:
                    variants = variants_
                await client.party.me.edit_and_keep(partial(client.party.me.set_backpack, asset=id_, variants=variants, enlightenment=enlightenment))
        elif type_ == "Pet":
            flag = False
            if client.backpacklock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                return False
            else:
                if 'banner' in id_:
                    variants = client.party.me.create_variants(item="AthenaBackpack", profile_banner='ProfileBanner')
                    variants += variants_ 
                else:
                    variants = variants_
                await client.party.me.edit_and_keep(partial(client.party.me.set_pet, asset=id_, variants=variants))
        elif type_ == "Harvesting Tool":
            flag = False
            if client.pickaxelock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                return False
            else:
                if 'banner' in id_:
                    variants = client.party.me.create_variants(item="AthenaPickaxe", profile_banner='ProfileBanner')
                    variants += variants_ 
                else:
                    variants = variants_
                await client.party.me.edit_and_keep(partial(client.party.me.set_pickaxe, asset=id_, variants=variants))
                await client.party.me.set_emote("EID_IceKing")
        elif type_ == "Emote":
            flag = False
            if client.emotelock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                return False
            else:
                if client.party.me.emote is not None:
                    if client.party.me.emote.lower() == id_.lower():
                        await client.party.me.clear_emote()
                await client.party.me.set_emote(asset=id_)
                client.eid=id_
        elif type_ == "Emoticon":
            flag = False
            if client.emotelock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                return False
            else:
                if client.party.me.emote is not None:
                    if client.party.me.emote.lower() == id_.lower():
                        await client.party.me.clear_emote()
                id_ = f"/Game/Athena/Items/Cosmetics/Dances/Emoji/{id_}.{id_}"
                await client.party.me.set_emote(asset=id_)
                client.eid=id_
        elif type_ == "Toy":
            flag = False
            if client.emotelock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                return False
            else:
                if client.party.me.emote is not None:
                    if client.party.me.emote.lower() == id_.lower():
                        await client.party.me.clear_emote()
                id_ = f"/Game/Athena/Items/Cosmetics/Toys/{id_}.{id_}"
                await client.party.me.set_emote(asset=id_)
                client.eid=id_
        return True

    async def invitation_accept(invitation: fortnitepy.ReceivedPartyInvitation) -> None:
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
                send(name(client.user),l("accepted_invite_from", name(invitation.sender)),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
            else:
                send(name(client.user),f'{l("accepted_invite_from2", f"{name(invitation.sender)} [{platform_to_str(invitation.sender.platform)}]", invitation.party.id)}',add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
        except KeyError:
            if data['ingame-error'] is True:
                await invitation.sender.send(l("error"))
            if data['loglevel'] == 'debug':
                send(name(client.user),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
        except fortnitepy.PartyError:
            if data['ingame-error'] is True:
                await invitation.sender.send(l("error_already_member_of_party"))
            if data['loglevel'] == 'debug':
                send(name(client.user),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            send(name(client.user),l("already_member_of_party"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
        except fortnitepy.HTTPException:
            if data['ingame-error'] is True:
                await invitation.sender.send(l("user_notfound"))
            if data['loglevel'] == 'debug':
                send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            send(client.user.display_name,l("user_notfound"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
        except fortnitepy.Forbidden:
            if data['ingame-error'] is True:
                await invitation.sender.send(l("error_private_party"))
            if data['loglevel'] == 'debug':
                send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            send(client.user.display_name,l("error_private_party"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
        except fortnitepy.HTTPException:
            if data['ingame-error'] is True:
                await invitation.sender.send(l("error_while_accepting_partyinvite"))
            if data['loglevel'] == 'debug':
                send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            send(client.user.display_name,l("error_while_accepting_partyinvite"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
        except Exception:
            if data['ingame-error'] is True:
                await invitation.sender.send(l("error"))
            send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

    async def invitation_decline(invitation: fortnitepy.ReceivedPartyInvitation) -> None:
        client=invitation.client
        try:
            await invitation.decline()
            if data['loglevel'] == 'normal':
                send(client.user.display_name,l("declined_invite_from", str(invitation.sender.display_name)),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
            else:
                send(client.user.display_name,l("declined_invite_from2", f"{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}]", invitation.party.id),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
        except fortnitepy.PartyError:
            if data['ingame-error'] is True:
                await invitation.sender.send(l("error_netcl_does_not_match"))
            if data['loglevel'] == 'debug':
                send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            send(client.user.display_name,l("error_netcl_does_not_match"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
        except fortnitepy.HTTPException:
            if data['ingame-error'] is True:
                await invitation.sender.send(l("error_while_declining_invite"))
            if data['loglevel'] == 'debug':
                send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            send(client.user.display_name,l("error_while_declining_invite"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
        except Exception:
            if data['ingame-error'] is True:
                await invitation.sender.send(l("error"))
            send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

    async def invitation_decline_interval(invitation: fortnitepy.ReceivedPartyInvitation) -> None:
        client=invitation.client
        try:
            await invitation.decline()
            await invitation.sender.send(l("declined_invite_interval3"), str(data["fortnite"]["interval"]))
            if data['loglevel'] == 'normal':
                send(client.user.display_name,l("declined_invite_interval", str(invitation.sender.display_name), str(data["fortnite"]["interval"])),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
            else:
                send(client.user.display_name,l("declined_invite_interval2", f"{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}]", invitation.party.id, str(data["fortnite"]["interval"])),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
        except fortnitepy.PartyError:
            if data['ingame-error'] is True:
                await invitation.sender.send(l("error_netcl_does_not_match"))
            if data['loglevel'] == 'debug':
                send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            send(client.user.display_name,l("error_netcl_does_not_match"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
        except fortnitepy.HTTPException:
            if data['ingame-error'] is True:
                await invitation.sender.send(l("error_while_declining_invite"))
            if data['loglevel'] == 'debug':
                send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            send(client.user.display_name,l("error_while_declining_invite"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
        except Exception:
            if data['ingame-error'] is True:
                await invitation.sender.send(l("error"))
            send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

    async def invitation_decline_owner(invitation: fortnitepy.ReceivedPartyInvitation) -> None:
        try:
            await invitation.decline()
            await invitation.sender.send(l("declined_invite_owner3"))
            if data['loglevel'] == 'normal':
                send(client.user.display_name,l("declined_invite_owner", str(invitation.sender.display_name)),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
            else:
                send(client.user.display_name,l("declined_invite_owner2", f"{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}]", invitation.party.id),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
        except fortnitepy.PartyError:
            if data['ingame-error'] is True:
                await invitation.sender.send(l("error_netch_does_not_match"))
            if data['loglevel'] == 'debug':
                send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            send(client.user.display_name,l("error_netch_does_not_match"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
        except fortnitepy.HTTPException:
            if data['ingame-error'] is True:
                await invitation.sender.send(l("error_while_declining_invite"))
            if data['loglevel'] == 'debug':
                send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            send(client.user.display_name,l("error_while_declining_invite"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
        except Exception:
            if data['ingame-error'] is True:
                await invitation.sender.send(l("error"))
            send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

    async def invitation_decline_whitelist(invitation: fortnitepy.ReceivedPartyInvitation) -> None:
        try:
            await invitation.decline()
            await invitation.sender.send(l("declined_invite_whitelist3"))
            if data['loglevel'] == 'normal':
                send(client.user.display_name,l("declined_invite_whitelist", str(invitation.sender.display_name)),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
            else:
                send(client.user.display_name,l("declined_invite_whitelist2", f"{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}]", invitation.party.id),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
        except fortnitepy.PartyError:
            if data['ingame-error'] is True:
                await invitation.sender.send(l("error_netcl_does_not_match"))
            if data['loglevel'] == 'debug':
                send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            send(client.user.display_name,l("error_netcl_does_not_match"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
        except fortnitepy.HTTPException:
            if data['ingame-error'] is True:
                await invitation.sender.send(l("error_while_declining_invite"))
            if data['loglevel'] == 'debug':
                send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            send(client.user.display_name,l("error_while_declining_invite"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
        except Exception:
            if data['ingame-error'] is True:
                await invitation.sender.send(l("error"))
            send(client.user.display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

    async def aexec(code: str, variable: dict) -> Any:
        _ = lambda l: re.match(r"(\u0020|\u3000)*", l).end() * u"\u0020"
        scode = code.split('\n')
        delete = len(_(scode[0]))
        lines = [i.replace(u"\u0020", "", delete) for i in scode]
        exc = (
            f'async def __ex(var):'
            + '\n for v in var:'
            + '\n     v = var[v]'
            + ''.join(f'\n {l}' for l in lines)
            + '\n for v in locals():'
            + '\n     var[v] = locals()[v]'
        )
        if data['loglevel'] == 'debug':
            send(l('bot'),exc,yellow,add_d=lambda x:f'```\n{x}\n```')
        exec(exc)
        variable_before = variable.copy()
        result = await locals()['__ex'](variable)
        variable_after = variable.copy()
        newvar = {k: v for k,v in variable_after.items() if (k not in variable_before.keys() or v != variable_before.get(k)) and "_" not in k and k not in ("k", "v") and isinstance(k, str) is True}
        for k in newvar:
            exc = (
                f"global {k}"
                + f"\n{k} = newvar['{k}']"
            )
            exec(exc)
        return result

config_tags={
    "['fortnite']": [dict],
    "['fortnite']['email']": [str,"can_be_multiple"],
    "['fortnite']['password']": [str,"can_be_multiple"],
    "['fortnite']['owner']": [str],
    "['fortnite']['platform']": [str,"select_platform"],
    "['fortnite']['cid']": [str],
    "['fortnite']['bid']": [str],
    "['fortnite']['pickaxe_id']": [str],
    "['fortnite']['eid']": [str],
    "['fortnite']['playlist']": [str],
    "['fortnite']['banner']": [str],
    "['fortnite']['banner_color']": [str],
    "['fortnite']['level']": [int],
    "['fortnite']['tier']": [int],
    "['fortnite']['xpboost']": [int],
    "['fortnite']['friendxpboost']": [int],
    "['fortnite']['status']": [str],
    "['fortnite']['privacy']": [str,"select_privacy"],
    "['fortnite']['whisper']": [bool_,"select_bool"],
    "['fortnite']['partychat']": [bool_,"select_bool"],
    "['fortnite']['disablewhisperperfectly']": [bool_,"select_bool"],
    "['fortnite']['disablepartychatperfectly']": [bool_,"select_bool"],
    "['fortnite']['ignorebot']": [bool_,"select_bool"],
    "['fortnite']['joinmessage']": [str],
    "['fortnite']['randommessage']": [str,"can_be_multiple"],
    "['fortnite']['joinmessageenable']": [bool_,"select_bool"],
    "['fortnite']['randommessageenable']": [bool_,"select_bool"],
    "['fortnite']['outfitmimic']": [bool_,"select_bool"],
    "['fortnite']['backpackmimic']": [bool_,"select_bool"],
    "['fortnite']['pickaxemimic']": [bool_,"select_bool"],
    "['fortnite']['emotemimic']": [bool_,"select_bool"],
    "['fortnite']['acceptinvite']": [bool_,"select_bool"],
    "['fortnite']['acceptfriend']": [bool_none,"select_bool_none"],
    "['fortnite']['addfriend']": [bool_,"select_bool"],
    "['fortnite']['invite-ownerdecline']": [bool_,"select_bool"],
    "['fortnite']['inviteinterval']": [bool_,"select_bool"],
    "['fortnite']['interval']": [int],
    "['fortnite']['waitinterval']": [int],
    "['fortnite']['blacklist']": [list,"can_be_multiple"],
    "['fortnite']['blacklist-declineinvite']": [bool_,"select_bool"],
    "['fortnite']['blacklist-autoblock']": [bool_,"select_bool"],
    "['fortnite']['blacklist-autokick']": [bool_,"select_bool"],
    "['fortnite']['blacklist-autochatban']": [bool_,"select_bool"],
    "['fortnite']['blacklist-ignorecommand']": [bool_,"select_bool"],
    "['fortnite']['whitelist']": [list,"can_be_multiple"],
    "['fortnite']['whitelist-allowinvite']": [bool_,"select_bool"],
    "['fortnite']['whitelist-declineinvite']": [bool_,"select_bool"],
    "['fortnite']['whitelist-ignorelock']": [bool_,"select_bool"],
    "['fortnite']['whitelist-ownercommand']": [bool_,"select_bool"],
    "['fortnite']['invitelist']": [list,"can_be_multiple"],
    "['fortnite']['otherbotlist']": [list,"can_be_multiple"],
    "['discord']": [dict],
    "['discord']['enabled']": [bool_,"select_bool"],
    "['discord']['token']": [str],
    "['discord']['owner']": [int],
    "['discord']['channelname']": [str],
    "['discord']['status']": [str],
    "['discord']['discord']": [bool_,"select_bool"],
    "['discord']['disablediscordperfectly']": [bool_,"select_bool"],
    "['discord']['ignorebot']": [bool_,"select_bool"],
    "['discord']['blacklist']": [list,"can_be_multiple"],
    "['discord']['blacklist-ignorecommand']": [bool_,"select_bool"],
    "['discord']['whitelist']": [list,"can_be_multiple"],
    "['discord']['whitelist-ignorelock']": [bool_,"select_bool"],
    "['discord']['whitelist-ownercommand']": [bool_,"select_bool"],
    "['web']": [dict],
    "['web']['enabled']": [bool_,"select_bool"],
    "['web']['ip']": [str],
    "['web']['port']": [int],
    "['web']['password']": [str],
    "['web']['login_required']": [bool_,"select_bool"],
    "['web']['web']": [bool_,"select_bool"],
    "['web']['log']": [bool_,"select_bool"],
    "['restart_in']": [int],
    "['lang']": [str,"select_lang"],
    "['no-logs']": [bool_,"select_bool"],
    "['ingame-error']": [bool_,"select_bool"],
    "['discord-log']": [bool_,"select_bool"],
    "['hide-email']": [bool_,"select_bool"],
    "['hide-password']": [bool_,"select_bool"],
    "['hide-token']": [bool_,"select_bool"],
    "['hide-webhook']": [bool_,"select_bool"],
    "['webhook']": [str],
    "['caseinsensitive']": [bool_,"select_bool"],
    "['loglevel']": [str,"select_loglevel"],
    "['debug']": [bool_,"select_bool"]
}
commands_tags={
    "['ownercommands']": [str,"can_be_multiple"],
    "['true']": [str,"can_be_multiple"],
    "['false']": [str,"can_be_multiple"],
    "['me']": [str,"can_be_multiple"],
    "['prev']": [str,"can_be_multiple"],
    "['eval']": [str,"can_be_multiple"],
    "['exec']": [str,"can_be_multiple"],
    "['restart']": [str,"can_be_multiple"],
    "['relogin']": [str,"can_be_multiple"],
    "['reload']": [str,"can_be_multiple"],
    "['addblacklist']": [str,"can_be_multiple"],
    "['removeblacklist']": [str,"can_be_multiple"],
    "['addwhitelist']": [str,"can_be_multiple"],
    "['removewhitelist']": [str,"can_be_multiple"],
    "['addblacklist_discord']": [str,"can_be_multiple"],
    "['removeblacklist_discord']": [str,"can_be_multiple"],
    "['addwhitelist_discord']": [str,"can_be_multiple"],
    "['removewhitelist_discord']": [str,"can_be_multiple"],
    "['addinvitelist']": [str,"can_be_multiple"],
    "['removeinvitelist']": [str,"can_be_multiple"],
    "['get']": [str,"can_be_multiple"],
    "['friendcount']": [str,"can_be_multiple"],
    "['pendingcount']": [str,"can_be_multiple"],
    "['blockcount']": [str,"can_be_multiple"],
    "['friendlist']": [str,"can_be_multiple"],
    "['pendinglist']": [str,"can_be_multiple"],
    "['blocklist']": [str,"can_be_multiple"],
    "['outfitmimic']": [str,"can_be_multiple"],
    "['backpackmimic']": [str,"can_be_multiple"],
    "['pickaxemimic']": [str,"can_be_multiple"],
    "['emotemimic']": [str,"can_be_multiple"],
    "['whisper']": [str,"can_be_multiple"],
    "['partychat']": [str,"can_be_multiple"],
    "['discord']": [str,"can_be_multiple"],
    "['web']": [str,"can_be_multiple"],
    "['disablewhisperperfectly']": [str,"can_be_multiple"],
    "['disablepartychatperfectly']": [str,"can_be_multiple"],
    "['disablediscordperfectly']": [str,"can_be_multiple"],
    "['acceptinvite']": [str,"can_be_multiple"],
    "['acceptfriend']": [str,"can_be_multiple"],
    "['joinmessageenable']": [str,"can_be_multiple"],
    "['randommessageenable']": [str,"can_be_multiple"],
    "['wait']": [str,"can_be_multiple"],
    "['join']": [str,"can_be_multiple"],
    "['joinid']": [str,"can_be_multiple"],
    "['leave']": [str,"can_be_multiple"],
    "['invite']": [str,"can_be_multiple"],
    "['inviteall']": [str,"can_be_multiple"],
    "['message']": [str,"can_be_multiple"],
    "['partymessage']": [str,"can_be_multiple"],
    "['sendall']": [str,"can_be_multiple"],
    "['status']": [str,"can_be_multiple"],
    "['banner']": [str,"can_be_multiple"],
    "['level']": [str,"can_be_multiple"],
    "['bp']": [str,"can_be_multiple"],
    "['privacy']": [str,"can_be_multiple"],
    "['privacy_public']": [str,"can_be_multiple"],
    "['privacy_friends_allow_friends_of_friends']": [str,"can_be_multiple"],
    "['privacy_friends']": [str,"can_be_multiple"],
    "['privacy_private_allow_friends_of_friends']": [str,"can_be_multiple"],
    "['privacy_private']": [str,"can_be_multiple"],
    "['getuser']": [str,"can_be_multiple"],
    "['getfriend']": [str,"can_be_multiple"],
    "['getpending']": [str,"can_be_multiple"],
    "['getblock']": [str,"can_be_multiple"],
    "['info']": [str,"can_be_multiple"],
    "['info_party']": [str,"can_be_multiple"],
    "['pending']": [str,"can_be_multiple"],
    "['removepending']": [str,"can_be_multiple"],
    "['addfriend']": [str,"can_be_multiple"],
    "['removefriend']": [str,"can_be_multiple"],
    "['removeallfriend']": [str,"can_be_multiple"],
    "['acceptpending']": [str,"can_be_multiple"],
    "['declinepending']": [str,"can_be_multiple"],
    "['blockfriend']": [str,"can_be_multiple"],
    "['unblockfriend']": [str,"can_be_multiple"],
    "['chatban']": [str,"can_be_multiple"],
    "['promote']": [str,"can_be_multiple"],
    "['kick']": [str,"can_be_multiple"],
    "['ready']": [str,"can_be_multiple"],
    "['unready']": [str,"can_be_multiple"],
    "['sitout']": [str,"can_be_multiple"],
    "['match']": [str,"can_be_multiple"],
    "['unmatch']": [str,"can_be_multiple"],
    "['swap']": [str,"can_be_multiple"],
    "['outfitlock']": [str,"can_be_multiple"],
    "['backpacklock']": [str,"can_be_multiple"],
    "['pickaxelock']": [str,"can_be_multiple"],
    "['emotelock']": [str,"can_be_multiple"],
    "['stop']": [str,"can_be_multiple"],
    "['alloutfit']": [str,"can_be_multiple"],
    "['allbackpack']": [str,"can_be_multiple"],
    "['allpet']": [str,"can_be_multiple"],
    "['allpickaxe']": [str,"can_be_multiple"],
    "['allemote']": [str,"can_be_multiple"],
    "['allemoji']": [str,"can_be_multiple"],
    "['alltoy']": [str,"can_be_multiple"],
    "['cid']": [str,"can_be_multiple"],
    "['bid']": [str,"can_be_multiple"],
    "['petcarrier']": [str,"can_be_multiple"],
    "['pickaxe_id']": [str,"can_be_multiple"],
    "['eid']": [str,"can_be_multiple"],
    "['emoji_id']": [str,"can_be_multiple"],
    "['toy_id']": [str,"can_be_multiple"],
    "['id']": [str,"can_be_multiple"],
    "['outfit']": [str,"can_be_multiple"],
    "['backpack']": [str,"can_be_multiple"],
    "['pet']": [str,"can_be_multiple"],
    "['pickaxe']": [str,"can_be_multiple"],
    "['emote']": [str,"can_be_multiple"],
    "['emoji']": [str,"can_be_multiple"],
    "['toy']": [str,"can_be_multiple"],
    "['item']": [str,"can_be_multiple"],
    "['set']": [str,"can_be_multiple"],
    "['setvariant']": [str,"can_be_multiple"],
    "['addvariant']": [str,"can_be_multiple"],
    "['setstyle']": [str,"can_be_multiple"],
    "['addstyle']": [str,"can_be_multiple"],
    "['setenlightenment']": [str,"can_be_multiple"],
    "['outfitasset']": [str,"can_be_multiple"],
    "['backpackasset']": [str,"can_be_multiple"],
    "['pickaxeasset']": [str,"can_be_multiple"],
    "['emoteasset']": [str,"can_be_multiple"]
}

bot_ready = True
if load_config() is False:
    sys.exit(1)
if error_config or error_commands:
    bot_ready = False
for key in error_config:
    config_tags[key].append("fix_required")
for key in error_commands:
    commands_tags[key].append("fix_required")

if data.get('debug',False) is True:
    logger = logging.getLogger('fortnitepy.auth')
    logger.setLevel(level=logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter('\u001b[36m %(asctime)s:%(levelname)s:%(name)s: %(message)s \u001b[0m'))
    logger.addHandler(handler)

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

if os.getcwd().startswith('/app') or os.getcwd().startswith('/home/runner'):
    data['web']['ip']="0.0.0.0"
else:
    data['web']['ip']=data['web']['ip'].format(ip=socket.gethostbyname(socket.gethostname()))

if True:
    send(l('bot'),f'{l("lobbybot")}: gomashio\n{l("credit")}\n{l("library")}: Terbau',cyan)
    text = ""
    if data['loglevel'] == 'normal':
        text += f'\n{l("loglevel")}: {l("normal")}\n'
    elif data['loglevel'] == 'info':
        text += f'\n{l("loglevel")}: {l("info")}\n'
    elif data['loglevel'] == 'debug':
        text += f'\n{l("loglevel")}: {l("debug")}\n'
    if data.get('debug',False) is True:
        text += f'\n{l("debug")}: {l("on")}\n'
    else:
        text += f'\n{l("debug")}: {l("off")}\n'
    text += f'\nPython {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}\n'
    text += f'Fortnitepy {fortnitepy.__version__}\n'
    text += f'discord.py {discord.__version__}\n'
    send(l('bot'),text,green)
    if data.get('debug',False) is True:
        send(l('bot'),f'[{now_()}] {l("debug_is_on")}',red)
    send(l('bot'),l("booting"))

#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================

async def process_command(message: Union[Type[fortnitepy.FriendMessage], Type[fortnitepy.PartyMessage], Type[discord.Message], Type[WebMessage]]):
    global blacklist
    global whitelist
    global blacklist_
    global whitelist_
    global otherbotlist
    if message is None:
        return
    author_id = message.author.id
    loop = asyncio.get_event_loop()
    content=message.content
    if data['caseinsensitive'] is True:
        args = jaconv.kata2hira(content.lower()).split()
    else:
        args = content.split()
    rawargs = content.split()
    rawcontent = ' '.join(rawargs[1:])
    rawcontent2 = ' '.join(rawargs[2:])
    if isinstance(message, fortnitepy.message.MessageBase) is True:
        client=message.client
        if data['discord']['enabled'] is True and dclient.isready is False:
            return
        if client.isready is False:
            return
        add_cache(client, message.author)
        if message.author.id in blacklist and data['fortnite']['blacklist-ignorecommand'] is True:
            return
        if message.author.id in otherbotlist and data['fortnite']['ignorebot'] is True:
            return
        if isinstance(message, fortnitepy.FriendMessage):
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
            if data['loglevel'] == 'normal':
                send(name(message.author),content,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {name(message.author)} | {x}',add_d=lambda x:f'[{client.user.display_name}] {x}')
            else:
                send(f'{name(message.author)} [{platform_to_str(message.author.platform)}]',content,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {name(message.author)} [{platform_to_str(message.author.platform)}] | {x}',add_d=lambda x:f'[{client.user.display_name}] {x}')
        elif isinstance(message, fortnitepy.PartyMessage):
            if client.owner is not None:
                if client.partychat is False:
                    if client.partychatperfect is True:
                        return
                    elif message.author.id != client.owner.id and message.author.id not in whitelist:
                        return
            else:
                if client.partychat is False:
                    if message.author.id not in whitelist:
                        return
            display_name_ = is_most(client)
            if display_name_:
                if data['loglevel'] == 'normal':
                    send(name(message.author),content,add_p=lambda x:f'[{now_()}] [{l("party")}] [{display_name_}] {name(message.author)} | {x}',add_d=lambda x:f'[{l("party")}] [{display_name_}] {x}')
                else:
                    send(f'{name(message.author)} [{platform_to_str(message.author.platform)}/{message.author.input}]',content,add_p=lambda x:f'[{now_()}] [{l("party")}/{client.party.id}] [{display_name_}] {name(message.author)} [{platform_to_str(message.author.platform)}/{message.author.input}] | {x}',add_d=lambda x:f'[{l("party")}/{client.party.id}] [{display_name_}] {x}')

        flag = False
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
    elif isinstance(message, discord.message.Message) is True:
        if data['discord']['enabled'] is True and dclient.isready is False:
            return
        if isinstance(message.channel, discord.TextChannel) is False:
            return
        if message.author == dclient.user:
            return
        if message.author.bot is True and data['discord']['ignorebot'] is True:
            return
        if "{name}" not in data['discord']['channelname'] and "{id}" not in data['discord']['channelname']:
            tasks = {}
            for client_ in loadedclients:
                mes = AllMessage(content, message.author, client_, message)
                task = loop.create_task(process_command(mes))
                tasks[client_] = [task, mes]
            await asyncio.gather(*[i[0] for i in tasks.values()])
            for client_,list_ in tasks.items():
                result = list_[1].result
                if result.get(client_.user.id) is not None:
                    results = '\n'.join(result[client_.user.id])
                    await reply(message, client_, f"[{name(client_.user)}] {results}")
            return
        else:
            for clientname, client in client_name.items():
                if client.isready is False:
                    continue
                
                if message.channel.name == data['discord']['channelname'].format(name=clientname, id=client.user.id).replace(" ","-").replace("--","-").lower():
                    break
            else:
                return
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
        send(name(message.author),content,add_p=lambda x:f'[{now_()}] [{client.user.display_name}({dclient.user})] {name(message.author)} | {x}',add_d=lambda x:f'[{client.user.display_name}({dclient.user})] {x}')

        flag = False
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
    elif isinstance(message, WebMessage) is True:
        client=message.client
        if data['discord']['enabled'] is True and dclient.isready is False:
            return
        if client.isready is False:
            return
        if client.web is False:
            return
        send(name(message.author),content,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {name(message.author)} | {x}',add_d=lambda x:f'[{client.user.display_name}] {x}')
        flag = False
    elif isinstance(message, AllMessage) is True:
        client=message.client
        if data['discord']['enabled'] is True and dclient.isready is False:
            return
        if client.isready is False:
            return
        if isinstance(message.base, fortnitepy.message.MessageBase) is True:
            add_cache(client, message.author)
            if message.author.id in blacklist and data['fortnite']['blacklist-ignorecommand'] is True:
                return
            if message.author.id in otherbotlist and data['fortnite']['ignorebot'] is True:
                return
            if isinstance(message.base, fortnitepy.FriendMessage):
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
                if data['loglevel'] == 'normal':
                    send(name(message.author),content,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {name(message.author)} | {x}',add_d=lambda x:f'[{client.user.display_name}] {x}')
                else:
                    send(f'{name(message.author)} [{platform_to_str(message.author.platform)}]',content,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {name(message.author)} | {x}',add_d=lambda x:f'[{client.user.display_name}] {x}')
            elif isinstance(message.base, fortnitepy.PartyMessage):
                if client.owner is not None:
                    if client.partychat is False:
                        if client.partychatperfect is True:
                            return
                        elif message.author.id != client.owner.id and message.author.id not in whitelist:
                            return
                else:
                    if client.partychat is False:
                        if message.author.id not in whitelist:
                            return
                display_name = is_most(client)
                if display_name:
                    if data['loglevel'] == 'normal':
                        send(name(message.author),content,add_p=lambda x:f'[{now_()}] [{l("party")}] [{display_name}] {name(message.author)} | {x}',add_d=lambda x:f'[{l("party")}] [{display_name}] {x}')
                    else:
                        send(f'{name(message.author)} [{platform_to_str(message.author.platform)}/{message.author.input}]',content,add_p=lambda x:f'[{now_()}] [{l("party")}/{client.party.id}] [{display_name}] {name(message.author)} [{platform_to_str(message.author.platform)}/{message.author.input}] | {x}',add_d=lambda x:f'[{l("party")}/{client.party.id}] [{display_name}] {x}')
            if rawcontent in commands['me'].split(','):
                rawcontent=str(message.author.display_name)

            flag = False
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
        elif isinstance(message.base, discord.message.Message) is True:
            if data['discord']['enabled'] is True and dclient.isready is False:
                return
            if message.author == dclient.user:
                return
            if message.author.bot is True and data['discord']['ignorebot'] is True:
                return
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
            send(name(message.author),content,add_p=lambda x:f'[{now_()}] [{client.user.display_name}({dclient.user})] {name(message.author)} | {x}',add_d=lambda x:f'[{client.user.display_name}({dclient.user})] {x}')

            flag = False
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
        elif isinstance(message.base, WebMessage) is True:
            if data['discord']['enabled'] is True and dclient.isready is False:
                return
            if client.isready is False:
                return
            if client.web is False:
                return
            send(name(message.author),content,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {name(message.author)} | {x}',add_d=lambda x:f'[{client.user.display_name}] {x}')
            flag = False

    if client.isready is False:
        return
    display_name = name(client.user)
    if message.author.id in blacklist_ and data['discord']['blacklist-ignorecommand'] is True:
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

    if args[0] in commands['eval'].split(','):
        try:
            if rawcontent == "":
                await reply(message, client, f"[{commands['eval']}] [{l('eval')}]")
                return
            variable=globals()
            variable.update(locals())
            if rawcontent.startswith("await "):
                if data['loglevel'] == "debug":
                    send(display_name,f"await eval({rawcontent.replace('await ','',1)})",yellow,add_d=lambda x:f'```\n{x}\n```')
                result = await eval(rawcontent.replace("await ","",1), variable)
                await reply(message, client, str(result))
            else:
                if data['loglevel'] == "debug":
                    send(display_name,f"eval {rawcontent}",yellow,add_d=lambda x:f'```\n{x}\n```')
                result = eval(rawcontent, variable)
                await reply(message, client, str(result))
        except Exception:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, f"{l('error')}\n{traceback.format_exc()}")

    elif args[0] in commands['exec'].split(','):
        try:
            if rawcontent == "":
                await reply(message, client, f"[{commands['exec']}] [{l('exec')}]")
                return
            variable=globals()
            variable.update(locals())
            args_=[i.replace("\\nn", "\n") for i in content.replace("\n", "\\nn").split()]
            content_=" ".join(args_[1:])
            result = await aexec(content_, variable)
            await reply(message, client, str(result))
        except Exception as e:
            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            await reply(message, client, f"{l('error')}\n{traceback.format_exc()}")

    for m in content.split("\n"):
        content = m
        if data['caseinsensitive'] is True:
            args = jaconv.kata2hira(content.lower()).split()
        else:
            args = content.split()
        content_ = ' '.join(args[1:])
        content2_ = ' '.join(args[2:])
        rawargs = content.split()
        rawcontent = ' '.join(rawargs[1:])
        rawcontent2 = ' '.join(rawargs[2:])
        if isinstance(message, fortnitepy.message.MessageBase) is True:
            if rawcontent in commands['me'].split(','):
                rawcontent = str(message.author.display_name)
            if content_ in commands['me'].split(','):
                content_ = str(message.author.display_name)

        if flag is True:
            for checks in commands.items():
                if checks[0] in ignore:
                    continue
                if commands['ownercommands'] == '':
                    break
                for command in commands['ownercommands'].split(','):
                    if args[0] in commands[command.lower()].split(','):
                        await reply(message, client, l("this_command_owneronly"))
                        continue

        for key,value in replies.items():
            if args[0] in key.split(','):
                try:
                    await reply(message, client, value)
                except Exception:
                    send(name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l('error'))
                continue

        if data['discord']['enabled'] is True and dclient.isready is True:
            if args[0] in commands['addblacklist_discord'].split(','):
                try:
                    if rawcontent == '' or args[1].isdigit() is False:
                        await reply(message, client, f"[{commands['addblacklist_discord']}] [{l('userid')}]")
                        continue
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
                        send(display_name,l('add_to_list', f'{name(user)}', l('discord_blacklist')),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                        await reply(message, client, l('add_to_list', f'{name(user)}', l('discord_blacklist')))
                    else:
                        await reply(message, client, l('already_list', f'{name(user)}', l('discord_blacklist')))
                except discord.NotFound:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l('user_notfound'))
                except discord.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    send(display_name,l("error_while_requesting_userinfo"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                except Exception:
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l('error'))

            elif args[0] in commands['removeblacklist_discord'].split(','):
                try:
                    if rawcontent == '' or args[1].isdigit() is False:
                        await reply(message, client, f"[{commands['removeblacklist_discord']}] [{l('userid')}]")
                        continue
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
                        send(display_name,l('remove_from_list', f'{name(user)}', l('discord_blacklist')),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                        await reply(message, client, l('remove_from_list', f'{name(user)}', l('discord_blacklist')))
                    else:
                        await reply(message, client, l('not_list', f'{name(user)}', l('discord_blacklist')))
                except discord.NotFound:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    send(display_name,l('user_notfound'),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l('user_notfound'))
                except discord.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    send(display_name,traceback.format_exc(),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                except Exception:
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l('error'))

            elif args[0] in commands['addwhitelist_discord'].split(','):
                try:
                    if rawcontent == '' or args[1].isdigit() is False:
                        await reply(message, client, f"[{commands['addwhitelist_discord']}] [{l('userid')}]")
                        continue
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
                        send(display_name,l('remove_from_list', f'{name(user)}', l('discord_whitelist')),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                        await reply(message, client, l('add_from_list', f'{name(user)}', l('discord_whitelist')))
                    else:
                        await reply(message, client, l('already_list', f'{name(user)}', l('discord_whitelist')))
                except discord.NotFound:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l('user_notfound'))
                except discord.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    send(display_name,l("error_while_requesting_userinfo"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                except Exception:
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l('error'))

            elif args[0] in commands['removewhitelist_discord'].split(','):
                try:
                    if rawcontent == '' or args[1].isdigit() is False:
                        await reply(message, client, f"[{commands['removewhitelist_discord']}] [{l('userid')}]")
                        continue
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
                        send(display_name,l('remove_from_list', f'{name(user)}', l('discord_whitelist')),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                        await reply(message, client, l('remove_list', f'{name(user)}', l('discord_whitelist')))
                    else:
                        await reply(message, client, l('not_list', f'{name(user)}', l('discord_whitelist')))
                except discord.NotFound:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l('user_notfound'))
                except discord.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    send(display_name,l("error_while_requesting_userinfo"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                except Exception:
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l('error'))

        if args[0] in commands['restart'].split(','):
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
                    await reply(message, client, l('invite_is_decline'))
                    continue
                await reply(message, client, l('restaring'))
                restart()
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

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
                    await reply(message, client, l('invite_is_decline'))
                    continue
                await reply(message, client, l('relogining'))
                await client.restart()
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['reload'].split(','):
            success = load_config(client)
            try:
                if success is True:
                    await reply(message, client, l('success'))
                else:
                    await reply(message, client, l('error'))
                    continue
                try:
                    client.owner=None
                    owner=await client.fetch_profile(data['fortnite']['owner'])
                    if owner is None:
                        send(display_name,l("owner_notfound"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                    else:
                        add_cache(client, owner)
                        client.owner=client.get_friend(owner.id)
                        if client.owner is None:
                            if data['fortnite']['addfriend'] is True:
                                try:
                                    await client.add_friend(owner.id)
                                except fortnitepy.HTTPException:
                                    if data['loglevel'] == 'debug':
                                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                                    send(display_name,l("error_while_sending_friendrequest"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                                except Exception:
                                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                            send(display_name,l("not_friend_with_owner",commands["reload"]),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                        else:
                            send(display_name,f'{l("owner")}: {name(client.owner)}',green,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    send(display_name,l("error_while_requesting_userinfo"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                except Exception:
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                
                if client.owner is not None:
                    await client.owner.send(l("click_invite"))

                for blacklistuser in data['fortnite']['blacklist']:
                    try:
                        user = await client.fetch_profile(blacklistuser)
                        add_cache(client, user)
                        if user is None:
                            send(display_name,l("blacklist_user_notfound",blacklistuser),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                        else:
                            blacklist.append(user.id)
                            if data['fortnite']['blacklist-autoblock'] is True:
                                try:
                                    await user.block()
                                except Exception:
                                    if data['loglevel'] == 'debug':
                                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        send(display_name,l("error_while_requesting_userinfo"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                    except Exception:
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                if data['loglevel'] == "debug":
                    send(display_name,f'blacklist {blacklist}',yellow,add_d=lambda x:f'```\n{x}\n```')

                for whitelistuser in data['fortnite']['whitelist']:
                    try:
                        user = await client.fetch_profile(whitelistuser)
                        add_cache(client, user)
                        if user is None:
                            send(display_name,l("whitelist_user_notfound",whitelistuser),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                        else:
                            whitelist.append(user.id)
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        send(display_name,l("error_while_requesting_userinfo"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                    except Exception:
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                if data['loglevel'] == "debug":
                    send(display_name,f'whitelist {whitelist}',yellow,add_d=lambda x:f'```\n{x}\n```')

                for otherbotlistuser in data['fortnite']['otherbotlist']:
                    try:
                        user = await client.fetch_profile(otherbotlistuser)
                        add_cache(client, user)
                        if user is None:
                            send(display_name,l("botlist_user_notfound",otherbotlistuser),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                        else:
                            otherbotlist.append(user.id)
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        send(display_name,l("error_while_requesting_userinfo"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                    except Exception:
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                if data['loglevel'] == "debug":
                    send(display_name,f'botlist {otherbotlist}',yellow,add_d=lambda x:f'```\n{x}\n```')

                for invitelistuser in data['fortnite']['invitelist']:
                    try:
                        user = await client.fetch_profile(invitelistuser)
                        if user is None:
                            send(display_name,l("invitelist_user_notfound",invitelistuser),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                        else:
                            friend = client.get_friend(user.id)
                            if friend is None and user.id != client.user.id:
                                if data['fortnite']['addfriend'] is True:
                                    try:
                                        await client.add_friend(friend.id)
                                    except fortnitepy.HTTPException:
                                        if data['loglevel'] == 'debug':
                                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                                        send(display_name,l("error_while_sending_friendrequest"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                                    except Exception:
                                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                                send(display_name,l("not_friend_with_inviteuser",invitelistuser,commands["reload"]),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                            else:
                                add_cache(client, user)
                                client.invitelist.append(user.id)
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        send(display_name,l("error_while_requesting_userinfo"),red,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}',add_d=lambda x:f'>>> {x}')
                    except Exception:
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                if data['loglevel'] == "debug":
                    send(display_name,f'invitelist {client.invitelist}',yellow,add_d=lambda x:f'```\n{x}\n```')

                if data['discord']['enabled'] is True and dclient.isready:
                    dclient_user = name(dclient.user)
                    activity = discord.Game(name=data['discord']['status'])
                    await dclient.change_presence(activity=activity)

                    for blacklistuser in data['discord']['blacklist']:
                        blacklistuser = int(blacklistuser)
                        user = dclient.get_user(blacklistuser)
                        if user is None:
                            try:
                                user = await dclient.fetch_user(blacklistuser)
                            except discord.NotFound:
                                if data['loglevel'] == "debug":
                                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                                user = None
                        if user is None:
                            send(dclient_user,l('discord_blacklist_user_notfound', blacklistuser),red,add_p=lambda x:f'[{now_()}] [{dclient_user}] {x}',add_d=lambda x:f'>>> {x}')
                        else:
                            blacklist_.append(user.id)
                    if data['loglevel'] == "debug":
                        send(dclient_user,blacklist_,yellow,add_d=lambda x:f'```\n{x}\n```')

                    for whitelistuser in data['discord']['whitelist']:
                        whitelistuser = int(whitelistuser)
                        user = dclient.get_user(whitelistuser)
                        if user is None:
                            try:
                                user = await dclient.fetch_user(whitelistuser)
                            except discord.NotFound:
                                if data['loglevel'] == "debug":
                                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                                user = None
                        if user is None:
                            send(dclient_user,l('discord_whitelist_user_notfound', whitelistuser),red,add_p=lambda x:f'[{now_()}] [{dclient_user}] {x}',add_d=lambda x:f'>>> {x}')
                        else:
                            whitelist_.append(user.id)
                    if data['loglevel'] == "debug":
                        send(dclient_user,whitelist_,yellow,add_d=lambda x:f'```\n{x}\n```')

                    try:
                        dclient.owner=None
                        owner=dclient.get_user(int(data['discord']['owner']))
                        if owner is None:
                            try:
                                owner=await dclient.fetch_user(int(data['discord']['owner']))
                            except discord.NotFound:
                                if data['loglevel'] == "debug":
                                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                                owner = None
                        if owner is None:
                            send(dclient_user,l('discord_owner_notfound'),red,add_p=lambda x:f'[{now_()}] [{dclient_user}] {x}',add_d=lambda x:f'>>> {x}')
                        else:
                            dclient.owner=owner
                            send(dclient_user,f"{l('owner')}: {name(dclient.owner)}",green,add_p=lambda x:f'[{now_()}] [{dclient_user}] {x}')
                    except discord.HTTPException:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        send(display_name,l('error_while_requesting_userinfo'),red,add_p=lambda x:f'[{now_()}] [{dclient_user}] {x}',add_d=lambda x:f'>>> {x}')
                    except Exception:
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['addblacklist'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, client, f"[{commands['addblacklist']}] [{l('name_or_id')}]")
                    continue
                if data["caseinsensitive"] is True:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(name).lower()) and user.id != client.user.id and user.id not in blacklist}
                else:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in str(name) and user.id != client.user.id and user.id not in blacklist}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.id not in blacklist:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, client, l('too_many_users', str(len(users))))
                    continue
                if len(users) == 0:
                    await reply(message, client, l('user_notfound'))
                    continue
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if user.id not in blacklist:
                        blacklist.append(user.id)
                        if user.display_name is not None:
                            data["fortnite"]["blacklist"].append(str(user.display_name))
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
                        send(display_name,l('add_to_list', f'{name(user)}', l('blacklist')),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                        await reply(message, client, l('add_to_list', f'{name(user)}', l('blacklist')))
                    else:
                        await reply(message, client, l('already_in_list', f'{name(user)}', l('blacklist')))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
                if user.id not in blacklist:
                    blacklist.append(user.id)
                    if user.display_name is not None:
                        data["fortnite"]["blacklist"].append(str(user.display_name))
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
                    send(display_name,l('add_to_list', f'{name(user)}', l('blacklist')),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('add_to_list', f'{name(user)}', l('blacklist')))
                else:
                    await reply(message, client, l('already_in_list', f'{name(user)}', l('blacklist')))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {name(user)}"
                    text += f"\n{l('enter_to_add_to_list', l('blacklist'))}"
                    await reply(message, client, text)
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['removeblacklist'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, client, f"[{commands['removeblacklist']}] [{l('name_or_id')}]")
                    continue
                if data["caseinsensitive"] is True:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and user.id in blacklist}
                else:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and user.id in blacklist}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.id in blacklist:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, client, l('too_many_users', str(len(users))))
                    continue
                if len(users) == 0:
                    await reply(message, client, l('user_notfound'))
                    continue
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if user.id in blacklist:
                        blacklist.remove(user.id)
                        try:
                            data["fortnite"]["blacklist"].remove(str(user.display_name))
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
                        send(display_name,l('remove_from_list', name(user), l('blacklist')),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                        await reply(message, client, l('remove_from_list', name(user), l('blacklist')))
                    else:
                        await reply(message, client, l('not_list', name(user), l('blacklist')))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            if user.id in blacklist:
                blacklist.remove(user.id)
                try:
                    data["fortnite"]["blacklist"].remove(str(user.display_name))
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
                send(display_name,l('remove_from_list', name(user), l('blacklist')),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                await reply(message, client, l('remove_from_list', name(user), l('blacklist')))
            else:
                await reply(message, client, l('not_list', name(user), l('blacklist')))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {name(user)}"
                    text += f"\n{l('enter_to_remove_from_list', l('blacklist'))}"
                    await reply(message, client, text)
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['addwhitelist'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, client, f"[{commands['addwhitelist']}] [{l('name_or_id')}]")
                    continue
                if data["caseinsensitive"] is True:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and user.id not in whitelist}
                else:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and user.id not in whitelist}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.id not in whitelist:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(l("bot"),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, client, l('too_many_users', str(len(users))))
                    continue
                if len(users) == 0:
                    await reply(message, client, l('user_notfound'))
                    continue
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if user.id not in whitelist:
                        whitelist.append(user.id)
                        if user.display_name is not None:
                            data["fortnite"]["whitelist"].append(str(user.display_name))
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
                        send(display_name,l("add_to_list",name(user),l('whitelist')),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                        await reply(message, client, l("add_to_list", name(user), l('whitelist')))
                    else:
                        await reply(message, client, l("already_list", name(user), l('whitelist')))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
                if user.id not in whitelist:
                    whitelist.append(user.id)
                    if user.display_name is not None:
                        data["fortnite"]["whitelist"].append(str(user.display_name))
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
                    send(display_name,l("add_to_list",name(user),l('whitelist')),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l("add_to_list", name(user), l('whitelist')))
                else:
                    await reply(message, client, l("already_list", name(user), l('whitelist')))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {name(user)}"
                    text += f"\n{l('enter_to_add_to_list', l('whitelist'))}"
                    await reply(message, client, text)
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['removewhitelist'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, client, f"[{commands['removewhitelist']}] [{l('name_or_id')}]")
                    continue
                if data["caseinsensitive"] is True:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and user.id in whitelist}
                else:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and user.id in whitelist}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.id in whitelist:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(l("bot"),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, client, l("too_many_users", str(len(users))))
                    continue
                if len(users) == 0:
                    await reply(message, client, l('user_notfound'))
                    continue
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if user.id in whitelist:
                        whitelist.remove(user.id)
                        try:
                            data["whitelist"].remove(str(user.display_name))
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
                        send(display_name,l("remove_from_list",name(user),l("whitelist")),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                        await reply(message, client, l("remove_from_list", name(user), l('whitelist')))
                    else:
                        await reply(message, client, l("not_list", name(user), l('whitelist')))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            if user.id in whitelist:
                whitelist.remove(user.id)
                try:
                    data["whitelist"].remove(str(user.display_name))
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
                send(display_name,l("remove_from_list",name(user),l("whitelist")),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                await reply(message, client, l("remove_from_list", name(user), l('whitelist')))
            else:
                await reply(message, client, l("not_list", name(user), l('whitelist')))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {name(user)}"
                    text += f"\n{l('enter_to_remove_from_list', l('whitelist'))}"
                    await reply(message, client, text)
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['addinvitelist'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, client, f"[{commands['addinvitelist']}] [{l('name_or_id')}]")
                    continue
                if data["caseinsensitive"] is True:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and user.id not in client.invitelist}
                else:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and user.id not in client.invitelist}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.id not in client.invitelist:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, client, l("too_many_users", str(len(users))))
                    continue
                if len(users) == 0:
                    await reply(message, client, l('user_notfound'))
                    continue
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if user.id not in client.invitelist:
                        client.invitelist.append(user.id)
                        if user.display_name is not None:
                            data["fortnite"]["invitelist"].append(str(user.display_name))
                        else:
                            data["fortnite"]["invitelist"].append(user.id)
                        try:
                            with open("config.json", "r", encoding="utf-8") as f:
                                data_ = json.load(f)
                        except json.decoder.JSONDecodeError:
                            with open("config.json", "r", encoding="utf-8-sig") as f:
                                data_ = json.load(f)
                        data_["fortnite"]["invitelist"] = data["fortnite"]["invitelist"]
                        with open("config.json", "w", encoding="utf-8") as f:
                            json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                        send(display_name,l("add_to_list",name(user),l("invitelist")),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                        await reply(message, client, l("add_to_list", name(user), l('invitelist')))
                    else:
                        await reply(message, client, l("already_list", name(user), l('invitelist')))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            if user.id not in client.invitelist:
                client.invitelist.append(user.id)
                if user.display_name is not None:
                    data["fortnite"]["invitelist"].append(str(user.display_name))
                else:
                    data["fortnite"]["invitelist"].append(user.id)
                try:
                    with open("config.json", "r", encoding="utf-8") as f:
                        data_ = json.load(f)
                except json.decoder.JSONDecodeError:
                    with open("config.json", "r", encoding="utf-8-sig") as f:
                        data_ = json.load(f)
                data_["fortnite"]["invitelist"] = data["fortnite"]["invitelist"]
                with open("config.json", "w", encoding="utf-8") as f:
                    json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                send(display_name,l("add_to_list",name(user),l("invitelist")),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                await reply(message, client, l("add_to_list", name(user), l('invitelist')))
            else:
                await reply(message, client, l("already_list", name(user), l('invitelist')))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {name(user)}"
                    text += f"\n{l('enter_to_add_to_list', l('invitelist'))}"
                    await reply(message, client, text)
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['removeinvitelist'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, client, f"[{commands['removeinvitelist']}] [{l('name_or_id')}]")
                    continue
                if data["caseinsensitive"] is True:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and user.id in client.invitelist}
                else:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and user.id in client.invitelist}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.id in client.invitelist:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, client, l("too_many_users", str(len(users))))
                    continue
                if len(users) == 0:
                    await reply(message, client, l('user_notfound'))
                    continue
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if user.id in client.invitelist:
                        client.invitelist.remove(user.id)
                        try:
                            data["fortnite"]["invitelist"].remove(str(user.display_name))
                        except ValueError:
                            data["fortnite"]["invitelist"].remove(user.id)
                        try:
                            with open("config.json", "r", encoding="utf-8") as f:
                                data_ = json.load(f)
                        except json.decoder.JSONDecodeError:
                            with open("config.json", "r", encoding="utf-8-sig") as f:
                                data_ = json.load(f)
                        data_["fortnite"]["invitelist"] = data["fortnite"]["invitelist"]
                        with open("config.json", "w", encoding="utf-8") as f:
                            json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                        send(display_name,l("remove_from_list",name(user),l("invitelist")),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                        await reply(message, client, l("remove_from_list", name(user), l('invitelist')))
                    else:
                        await reply(message, client, l("not_list", name(user), l('invitelist')))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            if user.id in client.invitelist:
                client.invitelist.remove(user.id)
                try:
                    data["fortnite"]["invitelist"].remove(str(user.display_name))
                except ValueError:
                    data["fortnite"]["invitelist"].remove(user.id)
                try:
                    with open("config.json", "r", encoding="utf-8") as f:
                        data_ = json.load(f)
                except json.decoder.JSONDecodeError:
                    with open("config.json", "r", encoding="utf-8-sig") as f:
                        data_ = json.load(f)
                data_["fortnite"]["invitelist"] = data["fortnite"]["invitelist"]
                with open("config.json", "w", encoding="utf-8") as f:
                    json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                send(display_name,l("remove_from_list",name(user),l("invitelist")),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                await reply(message, client, l("remove_from_list", name(user), l('invitelist')))
            else:
                await reply(message, client, l("not_list", name(user), l('invitelist')))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {name(user)}"
                    text += f"\n{l('enter_to_remove_from_list', l('invitelist'))}"
                    await reply(message, client, text)
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['get'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, client, f"[{commands['get']}] [{l('name_or_id')}]")
                    continue
                if data["caseinsensitive"] is True:
                    users = {str(member.display_name): member for member in client.party.members.copy().values() if content_ in jaconv.kata2hira(str(member.display_name).lower())}
                else:
                    users = {str(member.display_name): member for member in client.party.members.copy().values() if content_ in str(member.display_name)}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.party.members.get(user.id) is not None:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, client, l("too_many_users", str(len(users))))
                    continue
                if len(users) == 0:
                    await reply(message, client, l('user_notfound'))
                    continue
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    member=client.party.members.get(user.id)
                    if member is None:
                        await reply(message, client, l("user_not_in_party"))
                        continue
                    send(display_name,f'{name(member)}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}',add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    if data['loglevel'] == 'debug':
                        send(display_name,json.dumps(member.meta.schema, indent=2),yellow,add_d=lambda x:f'```\n{x}\n```',add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, f'{name(member)}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}')
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            member=client.party.members.get(user.id)
            if member is None:
                await reply(message, client, l("user_not_in_party"))
                return
            send(display_name,f'{name(member)}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}',add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
            if data['loglevel'] == 'debug':
                send(display_name,json.dumps(member.meta.schema, indent=2),yellow,add_d=lambda x:f'>>> {x}',add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
            await reply(message, client, f'{name(member)}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}')""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {name(user)}"
                    text += f"\n{l('enter_to_get_userinfo')}"
                    await reply(message, client, text)
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['friendcount'].split(','):
            try:
                send(display_name,f"{l('friendcount')}: {len(client.friends)}",add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                await reply(message, client, f"{l('friendcount')}: {len(client.friends)}")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['pendingcount'].split(','):
            try:
                outbound = []
                inbound = []
                for pending in client.pending_friends.values():
                    if pending.direction == 'OUTBOUND':
                        outbound.append(pending)
                    elif pending.direction == 'INBOUND':
                        inbound.append(pending)
                send(display_name,f"{l('pendingcount')}: {len(client.pending_friends)}\n{l('outbound')}: {len(outbound)}\n{l('inbound')}: {len(inbound)}",add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                await reply(message, client, f"{l('pendingcount')}: {len(client.pending_friends)}\n{l('outbound')}: {len(outbound)}\n{l('inbound')}: {len(inbound)}")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['blockcount'].split(','):
            try:
                send(display_name,f"{l('blockcount')}: {len(client.blocked_users)}",add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                await reply(message, client, f"{l('blockcount')}: {len(client.blocked_users)}")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['friendlist'].split(','):
            try:
                text=''
                for friend in client.friends.values():
                    add_cache(client, friend)
                    text+=f'\n{name(friend)}'
                send(display_name,text,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                await reply(message, client, f'{text}')
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['pendinglist'].split(','):
            try:
                outbound=''
                inbound=''
                for pending in client.pending_friends.values():
                    add_cache(client, pending)
                    if pending.direction == 'OUTBOUND':
                        outbound+=f'\n{name(pending)}'
                    elif pending.direction == 'INBOUND':
                        inbound+=f'\n{name(pending)}'
                send(display_name,f"{l('outbound')}: {outbound}\n{l('inbound')}: {inbound}",add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                await reply(message, client, f"{l('outbound')}: {outbound}\n{l('inbound')}: {inbound}")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['blocklist'].split(','):
            try:
                text=''
                for block in client.blocked_users.values():
                    add_cache(client, block)
                    text+=f'\n{name(block)}'
                send(display_name,text,add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                await reply(message, client, f'{text}')
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['outfitmimic'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.outfitmimic=True
                    send(display_name,l('set_to', l('mimic', l('outfit')), l('on')),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('set_to', l('mimic', l('outfit')), l('on')))
                elif args[1] in commands['false'].split(','):
                    client.outfitmimic=False
                    send(display_name,l('set_to', l('mimic', l('outfit')), l('off')),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('set_to', l('mimic', l('outfit')), l('off')))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['outfitmimic']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['backpackmimic'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.backpackmimic=True
                    send(display_name,l('mimic_set', l('set_to', l('mimic', l('backpack')), l('on'))),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('mimic_set', l('set_to', l('mimic', l('backpack')), l('on'))))
                elif args[1] in commands['false'].split(','):
                    client.backpackmimic=False
                    send(display_name,l('mimic_set', l('set_to', l('mimic', l('backpack')), l('off'))),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('mimic_set', l('set_to', l('mimic', l('backpack')), l('off'))))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['backpackmimic']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['pickaxemimic'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.pickaxemimic=True
                    send(display_name,l('mimic_set', l('set_to', l('mimic', l('pickaxe')), l('on'))),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('mimic_set', l('set_to', l('mimic', l('pickaxe')), l('on'))))
                elif args[1] in commands['false'].split(','):
                    client.pickaxemimic=False
                    send(display_name,l('mimic_set', l('set_to', l('mimic', l('pickaxe')), l('off'))),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('mimic_set', l('set_to', l('mimic', l('pickaxe')), l('off'))))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['pickaxemimic']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['emotemimic'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.emotemimic=True
                    send(display_name,l('mimic_set', l('set_to', l('mimic', l('emote')), l('on'))),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('mimic_set', l('set_to', l('mimic', l('emote')), l('on'))))
                elif args[1] in commands['false'].split(','):
                    client.emotemimic=False
                    send(display_name,l('mimic_set', l('set_to', l('mimic', l('emote')), l('off'))),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('mimic_set', l('set_to', l('mimic', l('emote')), l('off'))))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['emotemimic']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['whisper'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.whisper=True
                    send(display_name,l('set_to', l('command_from', l('whisper'), l('on'))),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('set_to', l('command_from', l('whisper'), l('on'))))
                elif args[1] in commands['false'].split(','):
                    client.whisper=False
                    send(display_name,l('set_to', l('command_from', l('whisper'), l('off'))),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('set_to', l('command_from', l('whisper'), l('off'))))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['whisper']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['partychat'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.partychat=True
                    send(display_name,l('set_to', l('command_from', l('partychat'), l('on'))),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('set_to', l('command_from', l('partychat'), l('on'))))
                elif args[1] in commands['false'].split(','):
                    client.partychat=False
                    send(display_name,l('set_to', l('command_from', l('partychat'), l('off'))),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('set_to', l('command_from', l('partychat'), l('off'))))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['party']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['discord'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.discord=True
                    send(display_name,l('set_to', l('command_from', l('discord'), l('on'))),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('set_to', l('command_from', l('discord'), l('on'))))
                elif args[1] in commands['false'].split(','):
                    client.discord=False
                    send(display_name,l('set_to', l('command_from', l('discord'), l('off'))),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('set_to', l('command_from', l('discord'), l('off'))))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['discord']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['web'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.web=True
                    send(display_name,l('set_to', l('command_from', l('web'), l('on'))),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('set_to', l('command_from', l('web'), l('on'))))
                elif args[1] in commands['false'].split(','):
                    client.web=False
                    send(display_name,l('set_to', l('command_from', l('web'), l('off'))),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('set_to', l('command_from', l('web'), l('off'))))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['web']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['disablewhisperperfectly'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.whisperperfect=True
                    send(display_name,l('set_to', l('disable_perfect', l('whisper'), l('on'))),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('set_to', l('disable_perfect', l('whisper'), l('on'))))
                elif args[1] in commands['false'].split(','):
                    client.whisperperfect=False
                    send(display_name,l('set_to', l('disable_perfect', l('whisper'), l('off'))),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('set_to', l('disable_perfect', l('whisper'), l('off'))))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['disablewhisperperfectly']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['disablepartychatperfectly'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.partychatperfect=True
                    send(display_name,l('set_to', l('disable_perfect', l('whisper'), l('on'))),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('set_to', l('disable_perfect', l('partychat'), l('on'))))
                elif args[1] in commands['false'].split(','):
                    client.partychatperfect=False
                    send(display_name,l('set_to', l('disable_perfect', l('whisper'), l('off'))),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('set_to', l('disable_perfect', l('partychat'), l('off'))))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['disablepartychatperfectly']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['disablediscordperfectly'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.discordperfect=True
                    send(display_name,l('set_to', l('disable_perfect', l('discord'), l('on'))),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('set_to', l('disable_perfect', l('discord'), l('on'))))
                elif args[1] in commands['false'].split(','):
                    client.discordperfect=False
                    send(display_name,l('set_to', l('disable_perfect', l('discord'), l('off'))),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('set_to', l('disable_perfect', l('discord'), l('off'))))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['disablediscordperfectly']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['acceptinvite'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.acceptinvite=True
                    send(display_name,l('set_to', l('invite'), l('accept')),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('set_to', l('invite'), l('accept')))
                elif args[1] in commands['false'].split(','):
                    client.acceptinvite=False
                    send(display_name,l('set_to', l('invite'), l('decline')),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('set_to', l('invite'), l('decline')))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['acceptinvite']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['acceptfriend'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.acceptfriend=True
                    send(display_name,l('set_to', l('friend_request'), l('accept')),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('set_to', l('friend_request'), l('accept')))
                elif args[1] in commands['false'].split(','):
                    client.acceptfriend=False
                    send(display_name,l('set_to', l('friend_request'), l('decline')),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('set_to', l('friend_request'), l('decline')))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['acceptfriend']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['joinmessageenable'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.joinmessageenable=True
                    send(display_name,l('set_to', l('join_', l('message')), l('on')),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('set_to', l('join_', l('message')), l('on')))
                elif args[1] in commands['false'].split(','):
                    client.joinmessageenable=False
                    send(display_name,l('set_to', l('join_', l('message')), l('off')),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('set_to', l('join_', l('message')), l('off')))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['joinmessageenable']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['randommessageenable'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.randommessageenable=True
                    send(display_name,l('set_to', l('join_', l('randommessage')), l('on')),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('set_to', l('join_', l('randommessage')), l('on')))
                elif args[1] in commands['false'].split(','):
                    client.randommessageenable=False
                    send(display_name,l('set_to', l('join_', l('randommessage')), l('off')),add_p=lambda x:f'[{now_()}] [{client.user.display_name}] {x}')
                    await reply(message, client, l('set_to', l('join_', l('randommessage')), l('off')))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['randommessageenable']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

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
                    await reply(message, client, l('decline_invite_for', str(data['fortnite']['waitinterval'])))
                else:
                    if client.owner.id in client.party.members.copy().keys() and message.author.id != client.owner.id:
                        await reply(message, client, l('not_available'))
                        continue
                    client.acceptinvite=False
                    try:
                        client.timer_.cancel()
                    except AttributeError:
                        pass
                    client.timer_=Timer(data['fortnite']['waitinterval'], inviteaccept, [client])
                    client.timer_.start()
                    await reply(message, client, l('decline_invite_for', str(data['fortnite']['waitinterval'])))
            except Exception:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['join'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, client, f"[{commands['join']}] [{l('name_or_id')}]")
                    continue
                if data['caseinsensitive'] is True:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and client.has_friend(user.id) is True}
                else:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is True}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.has_friend(user.id) is True:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, client, l('too_many_users', str(len(users))))
                    continue
                if len(users) == 0:
                    await reply(message, client, l('user_notfound'))
                    continue
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    friend=client.get_friend(user.id)
                    if friend is None:
                        await reply(message, client, l('not_friend_with_user'))
                    else:
                        await friend.join_party()
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                friend=client.get_friend(user.id)
                if friend is None:
                    await reply(message, client, l('not_friend_with_user'))
                else:
                    await friend.join_party()
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('party_full_or_already_or_offline'))
            except fortnitepy.NotFound:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('party_notfound'))
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('party_private'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_joining_to_party'))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {name(user)}"
                    text += f"{l('enter_to_join_party')}"
                    await reply(message, client, text)
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('party_full_or_already_or_offline'))
            except fortnitepy.NotFound:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('party_notfound'))
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('party_private'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_joining_to_party'))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['joinid'].split(','):
            try:
                await client.join_to_party(party_id=args[1])
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('party_full_or_already'))
            except fortnitepy.NotFound:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('party_notfound'))
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('party_private'))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['join']}] [{l('party_id')}]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['leave'].split(','):
            try:
                await client.party.me.leave()
                await reply(message, client, l('party_leave', client.party.id))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_leaving_party'))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['invite'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, client, f"[{commands['invite']}] [{l('name_or_id')}]")
                    continue
                if data['caseinsensitive'] is True:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and client.has_friend(user.id) is True}
                else:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is True}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.has_friend(user.id) is True:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, client, l('too_many_users', str(len(users))))
                    continue
                if len(users) == 0:
                    await reply(message, client, l('user_notfound'))
                    continue
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    friend=client.get_friend(user.id)
                    if friend is None:
                        await reply(message, client, l('not_friend_with_user'))
                        continue
                    await friend.invite()
                    await reply(message, client, l('user_invited', f'{str(friend.display_name)} / {friend.id}', client.party.id))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                friend=client.get_friend(user.id)
                if friend is None:
                    await reply(message, client, l('not_friend_with_user'))
                    return
                await friend.invite()
                await reply(message, client, l('user_invited', f'{str(friend.display_name)} / {friend.id}', client.party.id))
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('party_full_or_already'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_sending_partyinvite'))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {name(user)}"
                    text += f"\n{l('enter_to_invite_user')}"
                    await reply(message, client, text)
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('party_full_or_already'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_sending_partyinvite'))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['inviteall'].split(','):
            try:
                for inviteuser in client.invitelist:
                    if inviteuser != client.user.id and inviteuser not in client.party.members:
                        try:
                            await client.party.invite(inviteuser)
                        except fortnitepy.PartyError:
                            if data['loglevel'] == 'debug':
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                            await reply(message, client, l('party_full_or_already'))
                        except fortnitepy.Forbidden:
                            if data['loglevel'] == 'debug':
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                            await reply(message, client, l('not_friend_with_user'))
                        except fortnitepy.HTTPException:
                            if data['loglevel'] == 'debug':
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                            await reply(message, client, l('error_while_sending_partyinvite'))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['message'].split(','):
            try:
                text=rawcontent.split(' : ')
                if data['caseinsensitive'] is True:
                    users = {str(user.display_name): user for user in cache_users.values() if text[0] in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and client.has_friend(user.id) is True}
                else:
                    users = {str(user.display_name): user for user in cache_users.values() if text[0] in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is True}
                try:
                    user=await client.fetch_profile(text[0])
                    if user is not None:
                        if client.has_friend(user.id) is True:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, client, l('too_many_users', str(len(users))))
                    continue
                if len(users) == 0:
                    await reply(message, client, l('user_notfound'))
                    continue
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    friend=client.get_friend(user.id)
                    if friend is None:
                        await reply(message, client, l('not_friend_with_user'))
                        continue
                    await friend.send(text[1])
                    await reply(message, client, l('user_sent', f'{str(friend.display_name)} / {friend.id}', text[1]))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                friend=client.get_friend(user.id)
                if friend is None:
                    await reply(message, client, l('not_friend_with_user'))
                    return
                await friend.send(text[1])
                await reply(message, client, l('user_sent', f'{str(friend.display_name)} / {friend.id}', text[1]))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user, "text": text} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {name(user)}"
                    text += f"\n{l('enter_to_send')}"
                    await reply(message, client, text)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l("error_while_requesting_userinfo"))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['message']}] [{l('name_or_id')}] : [{l('content')}]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['partymessage'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, client, f"[{commands['partymessage']}] [{l('content')}]")
                    continue
                await client.party.send(rawcontent)
                await reply(message, client, l('party_sent', client.party.id, rawcontent))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['sendall'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, client, f"[{commands['sendall']}] [{l('content')}]")
                    continue
                tasks = {}
                for client_ in loadedclients:
                    mes = AllMessage(rawcontent, message.author, client_, message)
                    task = loop.create_task(process_command(mes))
                    tasks[client_] = [task, mes]
                await asyncio.gather(*[i[0] for i in tasks.values()])
                for client_,list_ in tasks.items():
                    result = list_[1].result
                    if result.get(client_.user.id) is not None:
                        results = '\n'.join(result[client_.user.id])
                        await reply(message, client, f"[{name(client_.user)}] {results}")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['status'].split(','):
            try:
                await client.set_status(rawcontent)
                await reply(message, client, l('set_to', l('status'), rawcontent))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['status']}] [{l('content')}]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['banner'].split(','):
            try:
                await client.party.me.edit_and_keep(partial(client.party.me.set_banner,args[1],args[2],client.party.me.banner[2]))
                await reply(message, client, l('set_to', l('banner'), f"{args[1]}, {args[2]}"))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_changing_asset'))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['banner']}] [{l('bannerid')}] [{l('color')}]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['level'].split(','):
            try:
                await client.party.me.edit_and_keep(partial(client.party.me.set_banner,client.party.me.banner[0],client.party.me.banner[1],int(args[1])))
                await reply(message, client, l('level', args[1]))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_changing_asset'))
            except ValueError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('must_be_int'))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['level']}] [{l('level')}]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['bp'].split(','):
            try:
                await client.party.me.edit_and_keep(partial(client.party.me.set_battlepass_info,True,args[1],args[2],args[3]))
                await reply(message, client, l('set_to', l('bpinfo'), f"{l('tier')}: {args[1]}, {l('xpboost')}: {args[2]}, {l('friendxpboost')}: {args[3]}"))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_changing_bpinfo'))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['bp']}] [{l('tier')}] [{l('xpboost')}] [{l('friendxpboost')}]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['privacy'].split(','):
            try:
                if args[1] in commands['privacy_public'].split(','):
                    await client.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)
                    await reply(message, client, l('set_to', l('privacy'), l('public')))
                elif args[1] in commands['privacy_friends_allow_friends_of_friends'].split(','):
                    await client.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS_ALLOW_FRIENDS_OF_FRIENDS)
                    await reply(message, client, l('set_to', l('privacy'), l('friends_allow_friends_of_friends')))
                elif args[1] in commands['privacy_friends'].split(','):
                    await client.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS)
                    await reply(message, client, l('set_to', l('privacy'), l('friends')))
                elif args[1] in commands['privacy_private_allow_friends_of_friends'].split(','):
                    await client.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE_ALLOW_FRIENDS_OF_FRIENDS)
                    await reply(message, client, l('set_to', l('privacy'), l('private_allow_friends_of_friends')))
                elif args[1] in commands['privacy_private'].split(','):
                    await client.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE)
                    await reply(message, client, l('set_to', l('privacy'), l('private')))
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('not_party_leader'))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['privacy']}] [[{commands['privacy_public']}] / [{commands['privacy_friends_allow_friends_of_friends']}] / [{commands['privacy_friends']}] / [{commands['privacy_private_allow_friends_of_friends']}] / [{commands['privacy_private']}]]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error')) 

        elif args[0] in commands['getuser'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, client, f"[{commands['getuser']}] [{l('name_or_id')}]")
                    continue
                if data['caseinsensitive'] is True:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id}
                else:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, client, l('too_many_users', str(len(users))))
                    continue
                if len(users) == 0:
                    await reply(message, client, l('user_notfound'))
                    continue
                text = str()
                for user in users.values():
                    text += f'\n{name(user)}'
                send(display_name,text)
                await reply(message, client, text)
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['getfriend'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, client, f"[{commands['getfriend']}] [{l('name_or_id')}]")
                    continue
                if data['caseinsensitive'] is True:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and client.has_friend(user.id) is True}
                else:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is True}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.has_friend(user.id) is True:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, client, l('too_many_users', str(len(users))))
                    continue
                if len(users) == 0:
                    await reply(message, client, l('user_notfound'))
                    continue
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
                        text += "\n{1}: {0.year}/{0.month}/{0.day} {0.hour}:{0.minute}:{0.second}".format(friend.last_logout, l('lastlogin'))
                send(display_name,text)
                await reply(message, client, text)
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['getpending'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, client, f"[{commands['getpending']}] [{l('name_or_id')}]")
                    continue
                if data['caseinsensitive'] is True:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and client.is_pending(user.id) is True}
                else:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and client.is_pending(user.id) is True}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.is_pending(user.id) is True:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, client, l('too_many_users', str(len(users))))
                    continue
                if len(users) == 0:
                    await reply(message, client, l('user_notfound'))
                    continue
                text = str()
                for user in users.values():
                    pending = client.get_pending_friend(user.id)
                    if pending is None:
                        continue
                    text += f'\n{str(pending.display_name)} / {pending.id}'
                send(display_name,text)
                await reply(message, client, text)
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['getblock'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, client, f"[{commands['getblock']}] [{l('name_or_id')}]")
                    continue
                if data['caseinsensitive'] is True:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and client.is_blocked(user.id) is True}
                else:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and client.is_blocked(user.id) is True}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.is_blocked(user.id) is True:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, client, l('too_many_users', str(len(users))))
                    continue
                if len(users) == 0:
                    await reply(message, client, l('user_notfound'))
                    continue
                text = str()
                for user in users.values():
                    block=client.get_blocked_user(user.id)
                    if block is None:
                        continue
                    text += f'\n{str(block.display_name)} / {block.id}'
                send(display_name,text)
                await reply(message, client, text)
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['info'].split(','):
            try:
                if args[1] in commands['info_party'].split(','):
                    text = str()
                    text += f"{client.party.id}\n{l('member_count')}: {client.party.member_count}\n{client.party.playlist_info[0]}"
                    for member in client.party.members.copy().values():
                        add_cache(client, member)
                        if data['loglevel'] == 'normal':
                            text += f'\n{str(member.display_name)}'
                        else:
                            text += f'\n{str(member.display_name)} / {member.id}'
                    send(display_name,text)
                    await reply(message, client, text)
                    if data['loglevel'] == 'debug':
                        send(display_name,json.dumps(client.party.meta.schema,indent=4),yellow,add_d=lambda x:f'```\n{x}\n```')
                
                elif True in [args[1] in commands[key].split(',') for key in ("cid", "bid", "petcarrier", "pickaxe_id", "eid", "emoji_id", "toy_id", "id")]:
                    type_ = convert_to_type(args[1])
                    if rawcontent2 == '':
                        await reply(message, client, f"[{commands[convert_to_old_type(type_)]}] [ID]")
                        continue
                    result = await loop.run_in_executor(None, search_item, data["lang"], "id", rawcontent2, type_)
                    if result is None and data["lang"] != "en":
                        result = await loop.run_in_executor(None, search_item, "en", "id", rawcontent2, type_)
                    if result is None:
                        await reply(message, client, l('item_notfound'))
                    else:
                        if len(result) > 30:
                            await reply(message, client, l('too_many_items', str(len(result))))
                            continue
                        if len(result) == 1:
                            await reply(message, client, f"{convert_backend_type(result[0]['backendType'])}: {result[0]['name']} | {result[0]['id']}\n{result[0]['description']}\n{result[0]['rarity']}\n{result[0]['set']}")
                        else:
                            text = str()
                            for count, item in enumerate(result):
                                text += f"\n{count+1} {convert_backend_type(item['backendType'])}: {item['name']} | {item['id']}"
                            text += f"\n{l('enter_to_show_info')}"
                            await reply(message, client, text)
                            client.select[message.author.id] = {"exec": [f"await reply(message, client, f'''{convert_backend_type(item['backendType'])}: {item['name']} | {item['id']}\n{item['description']}\n{item['rarity']}\n{item['set']}''')" for item in result]}

                elif True in  [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe", "emote", "emoji", "toy", "item")]:
                    type_ = convert_to_type(args[1])
                    if rawcontent2 == '':
                        await reply(message, client, f"[{commands[convert_to_old_type(type_)]}] [{l('itemname')}]")
                        continue
                    result = await loop.run_in_executor(None, search_item, data["lang"], "name", rawcontent2, type_)
                    if result is None and data["lang"] != "en":
                        result = await loop.run_in_executor(None, search_item, "en", "name", rawcontent2, type_)
                    if result is None:
                        await reply(message, client, l('item_notfound'))
                    else:
                        if len(result) > 30:
                            await reply(message, client, l('too_many_items', str(len(result))))
                            continue
                        if len(result) == 1:
                            await reply(message, client, f"{convert_backend_type(result[0]['backendType'])}: {result[0]['name']} | {result[0]['id']}\n{result[0]['description']}\n{result[0]['rarity']}\n{result[0]['set']}")
                        else:
                            text = str()
                            for count, item in enumerate(result):
                                text += f"\n{count+1} {convert_backend_type(item['backendType'])}: {item['name']} | {item['id']}"
                            text += f"\n{l('enter_to_show_info')}"
                            await reply(message, client, text)
                            client.select[message.author.id] = {"exec": [f"await reply(message, client, f'''{convert_backend_type(item['backendType'])}: {item['name']} | {item['id']}\n{item['description']}\n{item['rarity']}\n{item['set']}''')" for item in result]}
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['info']}] [[{commands['info_party']}] / [{commands['item']}] / [{commands['id']}] / [{commands['outfit']}] / [{commands['backpack']}] / [{commands['pickaxe']}] / [{commands['emote']}]]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

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
                            await reply(message, client, l('add_friend', f'{str(pending.display_name)} / {pending.id}'))
                        except fortnitepy.HTTPException:
                            if data['loglevel'] == 'debug':
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                            await reply(message, client, l('error_while_sending_friendrequest'))
                            continue
                        except Exception:
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                            await reply(message, client, l('error'))
                            continue
                elif args[1] in commands['false'].split(','):
                    for pending in pendings:
                        try:
                            await pending.decline()
                            await reply(message, client, l('friend_request_decline', f'{str(pending.display_name)} / {pending.id}'))
                        except fortnitepy.HTTPException:
                            if data['loglevel'] == 'debug':
                                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                            await reply(message, client, l('error_while_declining_friendrequest'))
                            continue
                        except Exception:
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                            await reply(message, client, l('error'))
                            continue
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['pending']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

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
                        await reply(message, client, l('remove_pending', f'{str(pending.display_name)} / {pending.id}'))
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        await reply(message, client, l('error_while_removing_friendrequest'))
                        continue
                    except Exception:
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                        await reply(message, client, l('error'))
                        continue
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['addfriend'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, client, f"[{commands['addfriend']}] [{l('name_or_id')}]")
                    continue
                if data['caseinsensitive'] is True:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and client.has_friend(user.id) is False}
                else:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is False}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.has_friend(user.id) is False:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, client, l('too_many_users', str(len(users))))
                    continue
                if len(users) == 0:
                    await reply(message, client, l('user_notfound'))
                    continue
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.has_friend(user.id) is True:
                        await reply(message, client, l('already_friend'))
                        continue
                    await client.add_friend(user.id)
                    await reply(message, client, l('friend_request_to', f'{name(user)}'))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.has_friend(user.id) is True:
                    await reply(message, client, l('already_friend'))
                    return
                await client.add_friend(user.id)
                await reply(message, client, l('friend_request_to', f'{name(user)}'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_sending_friendrequest'))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {name(user)}"
                    text += f"\n{l('enter_to_send_friendrequest')}"
                    await reply(message, client, text)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_sending_friendrequest'))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['removefriend'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, client, f"[{commands['removefriend']}] [{l('name_or_id')}]")
                    continue
                if data['caseinsensitive'] is True:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and client.has_friend(user.id) is True}
                else:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is True}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.has_friend(user.id) is True:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, client, l('too_many_users', str(len(users))))
                    continue
                if len(users) == 0:
                    await reply(message, client, l('user_notfound'))
                    continue
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.has_friend(user.id) is False:
                        await reply(message, client, l('not_friend_with_user'))
                        continue
                    await client.remove_or_decline_friend(user.id)
                    await reply(message, client, l('remove_friend', f'{name(user)}'))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.has_friend(user.id) is False:
                    await reply(message, client, l('not_friend_with_user'))
                    return
                await client.remove_or_decline_friend(user.id)
                await reply(message, client, l('remove_friend', f'{name(user)}'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_removing_friend')""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {name(user)}"
                    text += f"\n{l('enter_to_remove_friend')}"
                    await reply(message, client, text)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_removing_friend'))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['removeallfriend'].split(','):
            try:
                friend_count = len(client.friends)
                await client.remove_all_friends()
                await reply(message, client, l('remove_allfriend',friend_count))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_removing_friend'))
            except Exception:
                send(name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['acceptpending'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, client, f"[{commands['acceptpending']}] [{l('name_or_id')}]")
                    continue
                if data['caseinsensitive'] is True:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and client.is_pending(user.id) is True}
                else:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and client.is_pending(user.id) is True}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.is_pending(user.id) is True:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, client, l('too_many_users', str(len(users))))
                    continue
                if len(users) == 0:
                    await reply(message, client, l('user_notfound'))
                    continue
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.is_pending(user.id) is False:
                        await reply(message, client, l('not_pending_with_user'))
                        continue
                    await client.accept_friend(user.id)
                    await reply(message, client, l('friend_add', f'{name(user)}'))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.is_pending(user.id) is False:
                    await reply(message, client, l('not_pending_with_user'))
                    return
                await client.accept_friend(user.id)
                await reply(message, client, l('friend_add', f'{name(user)}'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_accepting_friendrequest'))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {name(user)}"
                    text += f"\n{l('enter_to_accept_pending')}"
                    await reply(message, client, text)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_accepting_friendrequest'))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['declinepending'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, client, f"[{commands['declinepending']}] [{l('name_or_id')}]")
                    continue
                if data['caseinsensitive'] is True:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and client.is_pending(user.id) is True}
                else:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and client.is_pending(user.id) is True}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.is_pending(user.id) is True:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, client, l('too_many_users', str(len(users))))
                    continue
                if len(users) == 0:
                    await reply(message, client, l('user_notfound'))
                    continue
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.is_pending(user.id) is False:
                        await reply(message, client, l('nor_pending_with_user'))
                        continue
                    await client.remove_or_decline_friend(user.id)
                    await reply(message, client, l('friend_request_decline', f'{name(user)}'))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.is_pending(user.id) is False:
                    await reply(message, client, l('nor_pending_with_user'))
                    return
                await client.remove_or_decline_friend(user.id)
                await reply(message, client, l('friend_request_decline', f'{name(user)}'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_declining_friendrequest'))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {name(user)}"
                    text += f"\n{l('enter_to_decline_pending')}"
                    await reply(message, client, text)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_declining_friendrequest'))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['blockfriend'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, client, f"[{commands['blockfriend']}] [{l('name_or_id')}]")
                    continue
                if data['caseinsensitive'] is True:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and client.is_blocked(user.id) is False}
                else:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and client.is_blocked(user.id) is False}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.is_blocked(user.id) is False:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, client, l('too_many_users', str(len(users))))
                    continue
                if len(users) == 0:
                    await reply(message, client, l('user_notfound'))
                    continue
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.is_blocked(user.id) is True:
                        await reply(message, client, l('already_block'))
                        continue
                    await client.block_user(user.id)
                    await reply(message, client, l('block_user', f'{name(user)}'))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.is_blocked(user.id) is True:
                    await reply(message, client, l('already_block'))
                    return
                await client.block_user(user.id)
                await reply(message, client, l('block_user', f'{name(user)}'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_blocking_user'))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {name(user)}"
                    text += f"\n{l('enter_to_block_user')}"
                    await reply(message, client, text)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_blocking_user'))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['unblockfriend'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, client, f"[{commands['unblockfriend']}] [{l('name_or_id')}]")
                    continue
                if data['caseinsensitive'] is True:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in jaconv.kata2hira(str(user.display_name).lower()) and user.id != client.user.id and client.is_blocked(user.id) is True}
                else:
                    users = {str(user.display_name): user for user in cache_users.values() if content_ in str(user.display_name) and user.id != client.user.id and client.is_blocked(user.id) is True}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.is_blocked(user.id) is True:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, client, l('too_many_users', str(len(users))))
                    continue
                if len(users) == 0:
                    await reply(message, client, l('user_notfound'))
                    continue
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.is_blocked(user.id) is False:
                        await reply(message, client, l('not_block'))
                        continue
                    await client.unblock_user(user.id)
                    await reply(message, client, l('unblock_user', f'{name(user)}'))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.is_blocked(user.id) is False:
                    await reply(message, client, l('not_block'))
                    return
                await client.unblock_user(user.id)
                await reply(message, client, l('unblock_user', f'{name(user)}'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_unblocking_user'))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {name(user)}"
                    text += f"\n{l('enter_to_unblock_user')}"
                    await reply(message, client, text)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_unblocking_user'))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['chatban'].split(','):
            try:
                reason=rawcontent.split(' : ')
                if rawcontent == '':
                    await reply(message, client, f"[{commands['chatban']}] [{l('name_or_id')}] : [{l('reason')}({l('optional')})]")
                    continue
                if data['caseinsensitive'] is True:
                    users = {str(member.display_name): member for member in client.party.members.copy().values() if content_ in jaconv.kata2hira(str(member.display_name).lower())}
                else:
                    users = {str(member.display_name): member for member in client.party.members.copy().values() if content_ in str(member.display_name)}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.party.members.get(user.id) is not None:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, client, l('too_many_users', str(len(users))))
                    continue
                if len(users) == 0:
                    await reply(message, client, l('user_notfound'))
                    continue
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.party.members.get(user.id) is None:
                        await reply(message, client, l('user_not_in_party'))
                        continue
                    member=client.party.members.get(user.id)
                    try:
                        await member.chatban(reason[1])
                    except IndexError:
                        await member.chatban()
                    await reply(message, client, l('chatban_user', f'{name(user)}'))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.party.members.get(user.id) is None:
                    await reply(message, client, l('user_not_in_party'))
                    return
                member=client.party.members.get(user.id)
                try:
                    await member.chatban(reason[1])
                except IndexError:
                    await member.chatban()
                await reply(message, client, l('chatban_user', f'{name(user)}'))
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('nor_party_leader'))
            except fortnitepy.NotFound:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('user_notfound'))
            except ValueError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('already_chatban'))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user, "reason": reason} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {name(user)}"
                    text += f"\n{l('enter_to_chatban')}"
                    await reply(message, client, text)
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('nor_party_leader'))
            except fortnitepy.NotFound:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('user_notfound'))
            except ValueError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('already_chatban'))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['promote'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, client, f"[{commands['promote']}] [{l('name_or_id')}]")
                    continue
                if data['caseinsensitive'] is True:
                    users = {str(member.display_name): member for member in client.party.members.copy().values() if content_ in jaconv.kata2hira(str(member.display_name).lower())}
                else:
                    users = {str(member.display_name): member for member in client.party.members.copy().values() if content_ in str(member.display_name)}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.party.members.get(user.id) is not None:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, client, l('too_many_users', str(len(users))))
                    continue
                if len(users) == 0:
                    await reply(message, client, l('user_notfound'))
                    continue
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.party.members.get(user.id) is None:
                        await reply(message, client, l('user_not_in_party'))
                        continue
                    member=client.party.members.get(user.id)
                    await member.promote()
                    await reply(message, client, l('promote_user', f'{name(user)}'))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.party.members.get(user.id) is None:
                    await reply(message, client, l('user_not_in_party'))
                    return
                member=client.party.members.get(user.id)
                await member.promote()
                await reply(message, client, l('promote_user', f'{name(user)}'))
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('not_party_leader'))
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('already_party_leader'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_promoting_party_leader'))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {name(user)}"
                    text += f"\n{l('enter_to_promote_user')}"
                    await reply(message, client, text)
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('not_party_leader'))
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('already_party_leader'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_promoting_party_leader'))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['kick'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, client, f"[{commands['kick']}] [{l('name_or_id')}]")
                    continue
                if data['caseinsensitive'] is True:
                    users = {str(member.display_name): member for member in client.party.members.copy().values() if content_ in jaconv.kata2hira(str(member.display_name).lower())}
                else:
                    users = {str(member.display_name): member for member in client.party.members.copy().values() if content_ in str(member.display_name)}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.party.members.get(user.id) is not None:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, client, l('too_many_users', str(len(users))))
                    continue
                if len(users) == 0:
                    await reply(message, client, l('user_notfound'))
                    continue
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.party.members.get(user.id) is None:
                        await reply(message, client, l('user_not_in_party'))
                        continue
                    member=client.party.members.get(user.id)
                    await member.kick()
                    await reply(message, client, l('kick_user', f'{name(user)}'))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.party.members.get(user.id) is None:
                    await reply(message, client, l('user_not_in_party'))
                    return
                member=client.party.members.get(user.id)
                await member.kick()
                await reply(message, client, l('kick_user', f'{name(user)}'))
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('not_party_leader'))
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('cant_kick_yourself'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_kicking_user'))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {name(user)}"
                    text += f"\n{l('enter_to_kick_user')}"
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('not_party_leader'))
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('cant_kick_yourself'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_kicking_user'))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['ready'].split(','):
            try:
                await client.party.me.set_ready(fortnitepy.ReadyState.READY)
                await reply(message, client, l('set_to', l('readystate'), l('ready')))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['unready'].split(','):
            try:
                await client.party.me.set_ready(fortnitepy.ReadyState.NOT_READY)
                await reply(message, client, l('set_to', l('readystate'), l('unready')))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['sitout'].split(','):
            try:
                await client.party.me.set_ready(fortnitepy.ReadyState.SITTING_OUT)
                await reply(message, client, l('set_to', l('readystate'), l('sitout')))
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['match'].split(','):
            try:
                await client.party.me.set_in_match(players_left=int(args[1]) if args[1:2] else 100)
                await reply(message, client, l('set_to', l('matchstate'), l('remaining', args[1] if args[1:2] else "100")))
            except ValueError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('remaining_must_be_between_0_and_255'))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['unmatch'].split(','):
            try:
                await client.party.me.clear_in_match()
                await reply(message, client, l('set_to', l('matchstate'), l('off')))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['swap'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, client, f"[{commands['swap']}] [{l('name_or_id')}]")
                    continue
                if data['caseinsensitive'] is True:
                    users = {str(member.display_name): member for member in client.party.members.copy().values() if content_ in jaconv.kata2hira(str(member.display_name).lower())}
                else:
                    users = {str(member.display_name): member for member in client.party.members.copy().values() if content_ in str(member.display_name)}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.party.members.get(user.id) is not None:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, client, l('too_many_users', str(len(users))))
                    continue
                if len(users) == 0:
                    await reply(message, client, l('user_notfound'))
                    continue
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.party.members.get(user.id) is None:
                        await reply(message, client, l('user_not_in_party'))
                        continue
                    member=client.party.members.get(user.id)
                    await member.swap_position()
                    await reply(message, client, l('swap_user', f'{name(user)}'))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.party.members.get(user.id) is None:
                    await reply(message, client, l('user_not_in_party'))
                    return
                member=client.party.members.get(user.id)
                await member.swap_position()
                await reply(message, client, l('swap_user', f'{name(user)}}'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_swapping_user'))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {name(user)}"
                    text += f"\n{l('enter_to_swap_user')}"
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_swapping_user'))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['outfitlock'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.outfitlock=True
                    await reply(message, client, l('set_to', l('lock', l('outfit')), l('on')))
                elif args[1] in commands['false'].split(','):
                    client.outfitlock=False
                    await reply(message, client, l('set_to', l('lock', l('outfit')), l('off')))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['outfitlock']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['backpacklock'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.backpacklock=True
                    await reply(message, client, l('set_to', l('lock', l('backpack')), l('on')))
                elif args[1] in commands['false'].split(','):
                    client.backpacklock=False
                    await reply(message, client, l('set_to', l('lock', l('backpack')), l('off')))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['backpacklock']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['pickaxelock'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.pickaxelock=True
                    await reply(message, client, l('set_to', l('lock', l('pickaxe')), l('on')))
                elif args[1] in commands['false'].split(','):
                    client.pickaxelock=False
                    await reply(message, client, l('set_to', l('lock', l('pickaxe')), l('off')))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['pickaxelock']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['emotelock'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.emotelock=True
                    await reply(message, client, l('set_to', l('lock', l('emote')), l('on')))
                elif args[1] in commands['false'].split(','):
                    client.emotelock=False
                    await reply(message, client, l('set_to', l('lock', l('emote')), l('off')))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['emotelock']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['stop'].split(','):
            try:
                client.stopcheck=True
                if await change_asset(client, message.author.id, "Emote", "") is True:
                    await reply(message, client, l('stopped'))
                else:
                    await reply(message, client, l('locked'))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['alloutfit'].split(','):
            try:
                flag = False
                if client.outfitlock is True:
                    flag = lock_check(client, author_id)
                if flag is True:
                    await reply(message, client, l('locked'))
                    continue
                with open('items/allOutfit.json', 'r', encoding='utf-8') as f:
                    allitem = json.load(f)
                for item in allitem:
                    if client.stopcheck is True:
                        client.stopcheck=False
                        break
                    if 'banner' not in item['id']:
                        await client.party.me.set_outfit(item['id'])
                    else:
                        await client.party.me.set_outfit(item['id'],variants=client.party.me.create_variants(profile_banner='ProfileBanner'))
                    await asyncio.sleep(2)
                else:
                    await reply(message, client, l('all_end', l('outfit')))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['allbackpack'].split(','):
            try:
                flag = False
                if client.backpacklock is True:
                    flag = lock_check(client, author_id)
                if flag is True:
                    await reply(message, client, l('locked'))
                    continue
                with open('items/allBack Bling.json', 'r', encoding='utf-8') as f:
                    allitem = json.load(f)
                for item in allitem:
                    if client.stopcheck is True:
                        client.stopcheck=False
                        break
                    if 'banner' not in item['id']:
                        await client.party.me.set_backpack(item['id'])
                    else:
                        await client.party.me.set_backpack(item['id'],variants=client.party.me.create_variants(profile_banner='ProfileBanner'))
                    await asyncio.sleep(2)
                else:
                    await reply(message, client, l('all_end', l('backpack')))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['allpet'].split(','):
            try:
                flag = False
                if client.backpacklock is True:
                    flag = lock_check(client, author_id)
                if flag is True:
                    await reply(message, client, l('locked'))
                    continue
                with open('items/allPet.json', 'r', encoding='utf-8') as f:
                    allitem = json.load(f)
                for item in allitem:
                    if client.stopcheck is True:
                        client.stopcheck=False
                        break
                    await client.party.me.set_pet(item['id'])
                    await asyncio.sleep(2)
                else:
                    await reply(message, client, l('all_end', l('pet')))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['allpickaxe'].split(','):
            try:
                flag = False
                if client.pickaxelock is True:
                    flag = lock_check(client, author_id)
                if flag is True:
                    await reply(message, client, l('locked'))
                    continue
                with open('items/allHarvesting Tool.json', 'r', encoding='utf-8') as f:
                    allitem = json.load(f)
                for item in allitem:
                    if client.stopcheck is True:
                        client.stopcheck=False
                        break
                    if 'banner' not in item['id']:
                        await client.party.me.set_pickaxe(item['id'])
                    else:
                        await client.party.me.set_pickaxe(item['id'],variants=client.party.me.create_variants(profile_banner='ProfileBanner'))
                    await asyncio.sleep(2)
                else:
                    await reply(message, client, l('all_end', l('pickaxe')))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['allemote'].split(','):
            try:
                flag = False
                if client.emotelock is True:
                    flag = lock_check(client, author_id)
                if flag is True:
                    await reply(message, client, l('locked'))
                    continue
                with open('items/allEmote.json', 'r', encoding='utf-8') as f:
                    allitem = json.load(f)
                for item in allitem:
                    if client.stopcheck is True:
                        client.stopcheck=False
                        break
                    await client.party.me.set_emote(item['id'])
                    await asyncio.sleep(5)
                else:
                    await reply(message, client, l('all_end', l('emote')))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['allemoji'].split(','):
            try:
                flag = False
                if client.emotelock is True:
                    flag = lock_check(client, author_id)
                if flag is True:
                    await reply(message, client, l('locked'))
                    continue
                with open('items/allEmoticon.json', 'r', encoding='utf-8') as f:
                    allitem = json.load(f)
                for item in allitem:
                    if client.stopcheck is True:
                        client.stopcheck=False
                        break
                    await client.party.me.set_emoji(item['id'])
                    await asyncio.sleep(5)
                else:
                    await reply(message, client, l('all_end', l('emoji')))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['alltoy'].split(','):
            try:
                flag = False
                if client.emotelock is True:
                    flag = lock_check(client, author_id)
                if flag is True:
                    await reply(message, client, l('locked'))
                    continue
                with open('items/allToy.json', 'r', encoding='utf-8') as f:
                    allitem = json.load(f)
                for item in allitem:
                    if client.stopcheck is True:
                        client.stopcheck=False
                        break
                    await client.party.me.set_toy(item['id'])
                    await asyncio.sleep(5)
                else:
                    await reply(message, client, l('all_end', l('toy')))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['setenlightenment'].split(','):
            try:
                if await change_asset(client, message.author.id, "Outfit", client.party.me.outfit, client.party.me.outfit_variants,(args[1],args[2])) is True:
                    await reply(message, client, l('set_to', 'enlightenment', f'{args[1]}, {args[2]}'))
                else:
                    await reply(message, client, l('locked'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_changing_asset'))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['setenlightenment']}] [{l('number')}] [{l('number')}]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif True in [args[0] in commands[key].split(',') for key in ("cid", "bid", "petcarrier", "pickaxe_id", "eid", "emoji_id", "toy_id", "id")]:
            type_ = convert_to_type(args[0])
            if rawcontent == '':
                await reply(message, client, f"[{commands[convert_to_old_type(type_)]}] [ID]")
                continue
            try:
                result = await loop.run_in_executor(None, search_item, data["lang"], "id", rawcontent, type_)
                if result is None:
                    result = await loop.run_in_executor(None, search_item, "en", "id", rawcontent, type_)
                if result is None:
                    await reply(message, client, l('item_notfound'))
                else:
                    if len(result) > 30:
                        await reply(message, client, l('too_many_items', str(len(result))))
                        continue
                    if len(result) == 1:
                        if await change_asset(client, message.author.id, convert_backend_type(result[0]['backendType']), result[0]['id']) is True:
                            if data['loglevel'] == 'normal':
                                await reply(message, client, f"{convert_backend_type(result[0]['backendType'])}: {result[0]['name']}")
                            else:
                                await reply(message, client, f"{convert_backend_type(result[0]['backendType'])}: {result[0]['name']} | {result[0]['id']}")
                        else:
                            await reply(message, client, l('locked'))
                    else:
                        text = str()
                        for count, item in enumerate(result):
                            if data['loglevel'] == 'normal':
                                text += f"\n{count+1} {convert_backend_type(item['backendType'])}: {item['name']}"
                            else:
                                text += f"\n{count+1} {convert_backend_type(item['backendType'])}: {item['name']} | {item['id']}"
                        text += f"\n{l('enter_to_change_asset')}"
                        await reply(message, client, text)
                        client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{convert_backend_type(item['backendType'])}', '{item['id']}')" for item in result]}
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_changing_asset'))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif True in  [args[0] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe", "emote", "emoji", "toy", "item")]:
            type_ = convert_to_type(args[0])
            if rawcontent == '':
                await reply(message, client, f"[{commands[convert_to_old_type(type_)]}] [{l('itemname')}]")
                continue
            try:
                result = await loop.run_in_executor(None, search_item, data["lang"], "name", rawcontent, type_)
                if result is None:
                    result = await loop.run_in_executor(None, search_item, "en", "name", rawcontent, type_)
                if result is None:
                    await reply(message, client, l('item_notfound'))
                else:
                    if len(result) > 30:
                        await reply(message, client, l('too_many_items', str(len(result))))
                        continue
                    if len(result) == 1:
                        if await change_asset(client, message.author.id, convert_backend_type(result[0]['backendType']), result[0]['id']) is True:
                            if data['loglevel'] == 'normal':
                                await reply(message, client, f"{convert_backend_type(result[0]['backendType'])}: {result[0]['name']}")
                            else:
                                await reply(message, client, f"{convert_backend_type(result[0]['backendType'])}: {result[0]['name']} | {result[0]['id']}")
                        else:
                            await reply(message, client, l('locked'))
                    else:
                        text = str()
                        for count, item in enumerate(result):
                            if data['loglevel'] == 'normal':
                                text += f"\n{count+1} {convert_backend_type(item['backendType'])}: {item['name']}"
                            else:
                                text += f"\n{count+1} {convert_backend_type(item['backendType'])}: {item['name']} | {item['id']}"
                        text += f"\n{l('enter_to_change_asset')}"
                        await reply(message, client, text)
                        client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{convert_backend_type(item['backendType'])}', '{item['id']}')" for item in result]}
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_changing_asset'))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['set'].split(','):
            if rawcontent == '':
                await reply(message, client, f"[{commands['set']}] [{l('setname')}]")
                continue
            try:
                result = await loop.run_in_executor(None, search_item, data["lang"], "set", rawcontent)
                if result is None:
                    result = await loop.run_in_executor(None, search_item, "en", "set", rawcontent)
                if result is None:
                    await reply(message, client, l('item_notfound'))
                else:
                    if len(result) > 30:
                        await reply(message, client, l('too_many_items', str(len(result))))
                        continue
                    if len(result) == 1:
                        if await change_asset(client, message.author.id, convert_backend_type(result[0]["backendType"]), result[0]['id']) is True:
                            if data['loglevel'] == 'normal':
                                await reply(message, client, f"{convert_backend_type(result[0]['backendType'])}: {result[0]['name']} | {result[0]['set']}")
                            else:
                                await reply(message, client, f"{convert_backend_type(result[0]['backendType'])}: {result[0]['name']} | {result[0]['id']}({result[0]['set']})")
                        else:
                            await reply(message, client, l('locked'))
                    else:
                        text = str()
                        for count, item in enumerate(result):
                            if data['loglevel'] == 'normal':
                                text += f"\n{count+1} {convert_backend_type(item['backendType'])}: {item['name']} | {result[0]['set']}"
                            else:
                                text += f"\n{count+1} {convert_backend_type(item['backendType'])}: {item['name']} | {item['id']}({result[0]['set']})"
                        text += f"\n{l('enter_to_change_asset')}"
                        await reply(message, client, text)
                        client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{convert_backend_type(item['backendType'])}', '{item['id']}')" for item in result]}
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_changing_asset'))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['setstyle'].split(','):
            try:
                if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pickaxe")]:
                    await reply(message, client, f"[{commands['setstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pickaxe']}]]")
                    continue
                type_ = convert_to_asset(args[1])
                id_ = member_asset(client.party.me, type_)
                type_ = convert_to_new_type(type_)
                if type_ == "Back Bling" and (id_.startswith("pet_carrier_") or id_.startswith("pet_")):
                    type_ = "Pet"
                result = await loop.run_in_executor(None, search_style, data["lang"], id_, type_)
                if result is None:
                    await reply(message, client, l('no_stylechange'))
                else:
                    text = str()
                    for count, item in enumerate(result):
                        text += f"\n{count+1} {item['name']}"
                    text += f"\n{l('enter_to_set_style')}"
                    await reply(message, client, text)
                    client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{type_}', '{id_}', {variants['variants']})" for variants in result]}
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['setstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['addstyle'].split(','):
            try:
                if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pickaxe")]:
                    await reply(message, client, f"[{commands['addstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pickaxe']}]]")
                    continue
                type_ = convert_to_asset(args[1])
                id_ = member_asset(client.party.me, type_)
                variants_ = eval(f"client.party.me.{type_}_variants")
                type_ = convert_to_new_type(type_)
                if type_ == "Back Bling" and (id_.startswith("pet_carrier_") or id_.startswith("pet_")):
                    type_ = "Pet"
                result = await loop.run_in_executor(None, search_style, data["lang"], id_, type_)
                if result is None:
                    await reply(message, client, l('no_stylechange'))
                else:
                    text = str()
                    for count, item in enumerate(result):
                        text += f"\n{count+1} {item['name']}"
                    text += f"\n{l('enter_to_set_style')}"
                    await reply(message, client, text)
                    client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{type_}', '{id_}', {variants_} + {variants['variants']})" for variants in result]}
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['addstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['setvariant'].split(','):
            try:
                if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe")]:
                    await reply(message, client, f"[{commands['setvariant']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                    continue
                variantdict={}
                for count,text in enumerate(args[2:]):
                    if count % 2 != 0:
                        continue
                    try:
                        variantdict[text]=args[count+3]
                    except IndexError:
                        break
                type_ = convert_to_type(args[1])
                id_ = member_asset(client.party.me, convert_to_asset(args[1]))
                variants = client.party.me.create_variants(item='AthenaCharacter',**variantdict)
                type_ = convert_to_new_type(type_)
                if type_ == "Back Bling" and (id_.startswith("pet_carrier_") or id_.startswith("pet_")):
                    type_ = "Pet"
                if await change_asset(client, message.author.id, type_, id_, variants, client.party.me.enlightenments) is False:
                    await reply(message, client, l('locked'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_changing_asset'))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['setvariant']}] [ID] [variant] [{l('number')}]")
            except Exception:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0] in commands['addvariant'].split(','):
            try:
                if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe")]:
                    await reply(message, client, f"[{commands['addvariant']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                    continue
                variantdict={}
                for count,text in enumerate(args[2:]):
                    if count % 2 != 0:
                        continue
                    try:
                        variantdict[text]=args[count+3]
                    except IndexError:
                        break
                type_ = convert_to_type(args[1])
                id_ = member_asset(client.party.me, convert_to_asset(args[1]))
                variants = client.party.me.create_variants(item='AthenaCharacter',**variantdict)
                variants += eval(f"client.party.me.{convert_to_asset(args[1])}_variants")
                type_ = convert_to_new_type(type_)
                if type_ == "Back Bling" and (id_.startswith("pet_carrier_") or id_.startswith("pet_")):
                    type_ = "Pet"
                if await change_asset(client, message.author.id, type_, id_, variants, client.party.me.enlightenments) is False:
                    await reply(message, client, l('locked'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_changing_asset'))
            except IndexError:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, f"[{commands['addvariant']}] [ID] [variant] [{l('number')}]")
            except Exception:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif True in [args[0] in commands[key].split(',') for key in ("outfitasset", "backpackasset", "pickaxeasset", "emoteasset")]:
            type_ = convert_to_type(args[0])
            try:
                if rawcontent == '':
                    await reply(message, client, f"[{commands[f'{convert_to_old_type(type_)}asset']}] [{l('assetpath')}]")
                    continue
                if await change_asset(client, message.author.id, type_, rawcontent) is False:
                    await reply(message, client, l('locked'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_changing_asset'))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif True in [args[0].lower().startswith(id_) for id_ in ("cid_", "bid_", "petcarrier_", "pickaxe_id_", "eid_", "emoji_", "toy_")]:
            try:
                type_ = convert_to_type(args[0])
                if await change_asset(client, message.author.id, type_, args[0]) is False:
                    await reply(message, client, l('locked'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error_while_changing_asset'))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        elif args[0].lower().startswith('playlist_'):
            try:
                await client.party.set_playlist(args[0])
                await reply(message, client, l('set_playlist', args[0]))
                data['fortnite']['playlist']=args[0]
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('not_party_leader'))
            except Exception:
                send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                await reply(message, client, l('error'))

        else:
            if ': ' in message.content:
                continue
            if content.isdigit() and client.select.get(message.author.id) is not None:
                try:
                    if int(args[0]) == 0:
                        await reply(message, client, l('please_enter_valid_number'))
                        continue
                    exec_ = client.select[message.author.id]["exec"][int(args[0])-1]
                    variable=globals()
                    variable.update(locals())
                    if client.select[message.author.id].get("variable") is not None:
                        variable.update(client.select[message.author.id]["variable"][int(args[0])-1])
                    await aexec(exec_, variable)
                except IndexError:
                    if data['loglevel'] == 'debug':
                        send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l('please_enter_valid_number'))
                except Exception:
                    send(display_name,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    await reply(message, client, l('error'))
            else:
                result = await loop.run_in_executor(None, search_item, data["lang"], "name", content, "Item")
                if result is None:
                    result = await loop.run_in_executor(None, search_item, "en", "name", content, "Item")
                if result is not None:
                    if len(result) > 30:
                        await reply(message, client, l('too_many_items', str(len(result))))
                        continue
                    if len(result) == 1:
                        if await change_asset(client, message.author.id, convert_backend_type(result[0]["backendType"]), result[0]['id']) is True:
                            if data['loglevel'] == 'normal':
                                await reply(message, client, f"{convert_backend_type(result[0]['backendType'])}: {result[0]['name']}")
                            else:
                                await reply(message, client, f"{convert_backend_type(result[0]['backendType'])}: {result[0]['name']} | {result[0]['id']}")
                        else:
                            await reply(message, client, l('locked'))
                    else:
                        text = str()
                        for count, item in enumerate(result):
                            if data['loglevel'] == 'normal':
                                text += f"\n{count+1} {convert_backend_type(item['backendType'])}: {item['name']}"
                            else:
                                text += f"\n{count+1} {convert_backend_type(item['backendType'])}: {item['name']} | {item['id']}"
                        text += f"\n{l('enter_to_change_asset')}"
                        await reply(message, client, text)
                        client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{convert_backend_type(item['backendType'])}', '{item['id']}')" for item in result]}

#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================

dclient=discord.Client()
dclient.isready=False
dclient.owner=None
if data.get('discord',{}).get('enabled',False) is True:
    @dclient.event
    async def on_ready() -> None:
        global blacklist_
        global whitelist_
        dclient_user = name(dclient.user)
        send(dclient_user,f"{l('login')}: {dclient_user}",green,add_p=lambda x:f'[{now_()}] [{dclient_user}] {x}')
        dclient.isready = True
        activity = discord.Game(name=data['discord']['status'])
        await dclient.change_presence(activity=activity)

        for blacklistuser in data['discord']['blacklist']:
            blacklistuser = int(blacklistuser)
            user = dclient.get_user(blacklistuser)
            if user is None:
                try:
                    user = await dclient.fetch_user(blacklistuser)
                except discord.NotFound:
                    if data['loglevel'] == "debug":
                        send(dclient_user,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    user = None
            if user is None:
                send(dclient_user,l('discord_blacklist_user_notfound', blacklistuser),red,add_p=lambda x:f'[{now_()}] [{dclient_user}] {x}',add_d=lambda x:f'>>> {x}')
            else:
                blacklist_.append(user.id)
        if data['loglevel'] == "debug":
            send(dclient_user,blacklist_,yellow,add_d=lambda x:f'```\n{x}\n```')

        for whitelistuser in data['discord']['whitelist']:
            whitelistuser = int(whitelistuser)
            user = dclient.get_user(whitelistuser)
            if user is None:
                try:
                    user = await dclient.fetch_user(whitelistuser)
                except discord.NotFound:
                    if data['loglevel'] == "debug":
                        send(dclient_user,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    user = None
            if user is None:
                send(dclient_user,l('discord_whitelist_user_notfound', whitelistuser),red,add_p=lambda x:f'[{now_()}] [{dclient_user}] {x}',add_d=lambda x:f'>>> {x}')
            else:
                whitelist_.append(user.id)
        if data['loglevel'] == "debug":
            send(dclient_user,whitelist_,yellow,add_d=lambda x:f'```\n{x}\n```')

        try:
            dclient.owner=None
            owner=dclient.get_user(int(data['discord']['owner']))
            if owner is None:
                try:
                    owner=await dclient.fetch_user(int(data['discord']['owner']))
                except discord.NotFound:
                    if data['loglevel'] == "debug":
                        send(dclient_user,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
                    owner = None
            if owner is None:
                send(dclient_user,l('discord_owner_notfound'),red,add_p=lambda x:f'[{now_()}] [{dclient_user}] {x}',add_d=lambda x:f'>>> {x}')
            else:
                dclient.owner=owner
                send(dclient_user,f"{l('owner')}: {name(dclient.owner)}",green,add_p=lambda x:f'[{now_()}] [{dclient_user}] {x}')
        except discord.HTTPException:
            if data['loglevel'] == 'debug':
                send(dclient_user,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            send(dclient_user,l('error_while_requesting_userinfo'),red,add_p=lambda x:f'[{now_()}] [{dclient_user}] {x}',add_d=lambda x:f'>>> {x}')
        except Exception:
            send(dclient_user,traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')

    @dclient.event
    async def on_message(message: discord.Message) -> None:
        await process_command(message)

#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================

Thread(target=dprint,args=()).start()
if data.get("status",1) != 0:
    Thread(target=get_item_info,args=()).start()

    clients = []
    for count, credential in enumerate(credentials.items()):
        email = credential[0]
        password = credential[1]
        try:
            device_auth_details = get_device_auth_details().get(email.lower(), {})
            if not device_auth_details:
                device_auth_details = generate_device_auth_and_store(email)
            client = Client(
                auth=fortnitepy.AdvancedAuth(
                    email=email,
                    password=password,
                    prompt_exchange_code=False,
                    prompt_authorization_code=False,
                    prompt_code_if_throttled=True,
                    prompt_code_if_invalid=True,
                    delete_existing_device_auths=False,
                    **device_auth_details
                ),
                default_party_member_config=fortnitepy.DefaultPartyMemberConfig(
                    meta=[
                        partial(ClientPartyMember.set_outfit, data['fortnite']['cid'].replace('cid','CID',1)),
                        partial(ClientPartyMember.set_backpack, data['fortnite']['bid'].replace('bid','BID',1)),
                        partial(ClientPartyMember.set_pickaxe, data['fortnite']['pickaxe_id'].replace('pickaxe_id','Pickaxe_ID',1)),
                        partial(ClientPartyMember.set_battlepass_info, has_purchased=True, level=data['fortnite']['tier'], self_boost_xp=data['fortnite']['xpboost'], friend_boost_xp=data['fortnite']['friendxpboost']),
                        partial(ClientPartyMember.set_banner, icon=data['fortnite']['banner'], color=data['fortnite']['banner_color'], season_level=data['fortnite']['level']),
                    ]
                ),
                platform=fortnitepy.Platform(data['fortnite']['platform'].upper()),
                status=data['fortnite']['status']
            )
        except ValueError:
            send(l("bot"),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
            send(l("bot"),l('error_while_setting_client'),red,add_d=lambda x:f'>>> {x}')
            continue
        
        client.email = email
        client.eid=data['fortnite']['eid']
        client.isready=False
        client.booting=False
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
        client.web=data['web']['web']
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

        clients.append(client)

select_bool = select(
    [
        {"value": "True","display_value": l('bool_true')},
        {"value": "False","display_value": l('bool_false')}
    ]
)
select_bool_none = select(
    [
        {"value": "True","display_value": l('bool_true')},
        {"value": "False","display_value": l('bool_false')},
        {"value": "None","display_value": l('bool_none')}
    ]
)
select_platform = select(
    [
        {"value": "WIN","display_value": "Windows"},
        {"value": "MAC","display_value": "Mac"},
        {"value": "PSN","display_value": "PlayStation"},
        {"value": "XBL","display_value": "Xbox"},
        {"value": "SWT","display_value": "Switch"},
        {"value": "IOS","display_value": "IOS"},
        {"value": "AND","display_value": "Android"}
    ]
)
select_privacy = select(
    [
        {"value": "public","display_value": l('public')},
        {"value": "friends_allow_friends_of_friends","display_value": l('friends_allow_friends_of_friends')},
        {"value": "friends","display_value": l('friends')},
        {"value": "private_allow_friends_of_friends","display_value": l('private_allow_friends_of_friends')},
        {"value": "private","display_value": l('private')}
    ]
)
select_loglevel = select(
    [
        {"value": "normal","display_value": l('normal')},
        {"value": "info","display_value": l('info')},
        {"value": "debug","display_value": l('debug')}
    ]
)
select_lang = select(
    [
        {"value": re.sub(r"lang(\\|/)","",i).replace(".json",""),"display_value": re.sub(r"lang(\\|/)","",i).replace(".json","")} for i in glob("lang/*.json") if "_old.json" not in i
    ]
)

for key,value in config_tags.items():
    for count,tag in enumerate(value):
        if tag == "can_be_multiple":
            config_tags[key][count] = can_be_multiple
        elif tag == "select_bool":
            config_tags[key][count] = select_bool
        elif tag == "select_bool_none":
            config_tags[key][count] = select_bool_none
        elif tag == "select_platform":
            config_tags[key][count] = select_platform
        elif tag == "select_privacy":
            config_tags[key][count] = select_privacy
        elif tag == "select_loglevel":
            config_tags[key][count] = select_loglevel
        elif tag == "select_lang":
            config_tags[key][count] = select_lang
        elif tag == "red":
            config_tags[key][count] = Red
        elif tag == "fix_required":
            config_tags[key][count] = FixRequired
for key,value in commands_tags.items():
    for count,tag in enumerate(value):
        if tag == "can_be_multiple":
            commands_tags[key][count] = can_be_multiple
        elif tag == "red":
            commands_tags[key][count] = Red
        elif tag == "fix_required":
            commands_tags[key][count] = FixRequired

app=Sanic(__name__)
app.secret_key = os.urandom(32)

if True:
    env = Environment(loader=FileSystemLoader('./templates', encoding='utf8'), extensions=['jinja2.ext.do'])
    auth = LoginManager()

    @app.route("/favicon.ico", methods=["GET"])
    async def favicon(request: Request):
        return sanic.response.redirect("/images/icon.png")

    @app.route("/images/<image>", methods=["GET"])
    async def images(request: Request, image: str):
        if os.path.isfile(f"templates/images/{image}"):
            return await sanic.response.file_stream(f"templates/images/{image}")
        else:
            return sanic.response.html("")

    if os.environ.get("FORTNITE_LOBBYBOT_STATUS") == "-1":
        @app.route("/", methods=["GET"])
        async def main(request: Request):
            return sanic.response.html(
                "<h2>Fortnite-LobbyBot<h2>"
                "<p>初めに<a href='https://github.com/gomashio1596/Fortnite-LobbyBot/blob/master/README.md' target='_blank'>README</a>をお読みください</p>"
                "<p>First, please read <a href='https://github.com/gomashio1596/Fortnite-LobbyBot/blob/master/README_EN.md' target='_blank'>README<a/></p>"
                "<p>質問などは私(Twitter @gomashio1596 Discord gomashio#4335)か<a href='https://discord.gg/NEnka5N' target='_blank'>Discordサーバー</a>まで</p>"
                "<p>For questions, Contact to me(Twitter @gomashio1596 Discord gomashio#4335) or ask in <a href='https://discord.gg/NEnka5N' target='_blank'>Discord server</a></p>"
                "<p><a href='https://glitch.com/edit/#!/remix/fortnite-lobbybot' target='_blank'>ここをクリック</a>してRemix</p>"
                "<p><a href='https://glitch.com/edit/#!/remix/fortnite-lobbybot' target='_blank'>Click here</a> to Remix</p>"
                "<a href='https://discord.gg/NEnka5N' target='_blank'><img src='https://discordapp.com/api/guilds/718709023427526697/widget.png?style=banner1'></img></a>"
            )
    elif data["status"] == 0:
        @app.route("/", methods=["GET", "POST"])
        async def main(request: Request):
            flash_messages = []
            flash_messages_red = []
            if request.method == "GET":
                try:
                    with open('config.json', 'r', encoding='utf-8') as f:
                        data = json.load(f)
                except json.decoder.JSONDecodeError:
                    with open('config.json', 'r', encoding='utf-8-sig') as f:
                        data = json.load(f)
                return render_template(
                    "config_editor.html",
                    l=l,
                    data=data,
                    config_tags=config_tags,
                    len=len,
                    join=str.join,
                    split=str.split,
                    type=type,
                    can_be_multiple=can_be_multiple,
                    select=select,
                    str=str,
                    int=int,
                    bool=bool,
                    list=list,
                    red=Red,
                    fix_required=FixRequired,
                    flash_messages=flash_messages,
                    flash_messages_red=flash_messages_red
                )
            else:
                flag = False
                raw = request.form
                try:
                    with open('config.json', 'r', encoding='utf-8') as f:
                        data = json.load(f)
                except json.decoder.JSONDecodeError:
                    with open('config.json', 'r', encoding='utf-8-sig') as f:
                        data = json.load(f)
                corrected = data
                
                for key_,tags in config_tags.items():
                    keys = key_.replace("'","").replace("[","").split("]")
                    key = keys[0]
                    nest = len(keys) - 1

                    if nest == 1:
                        if dict in tags:
                            if corrected.get(key) is None:
                                corrected[key] = {}
                        else:
                            value = raw.get(f"['{key}']")
                        
                        if Red in tags and value is None:
                            flash_messages_red.append(l('this_field_is_required', key))
                            flag = True
                        if can_be_multiple in tags:
                            if str in tags:
                                corrected[key] = ",".join([i for i in re.split(r'\n|\r',value if value else "") if i])
                            elif list in tags:
                                corrected[key] = re.split(r'\n|\r',value) if value else []
                        elif str in tags:
                            corrected[key] = value.replace(r"\\n",r"\n").replace(r"\n","\n") if value else ""
                        elif int in tags:
                            corrected[key] = int(value) if value else 0
                        elif bool_ in tags:
                            corrected[key] = bool_.create(value)
                        elif bool_none in tags:
                            corrected[key] = bool_none.create(value)
                    elif nest == 2:
                        key2 = keys[1]

                        if dict in tags:
                            if corrected.get(key) is None:
                                if corrected.get(key).get(key2) is None:
                                    corrected[key][key2] = {}
                        else:
                            value2 = raw.get(f"['{key}']['{key2}']")
                        
                        if Red in tags and value2 is None:
                            flash_messages_red.append(l('this_field_is_required', f"{key}: {key2}"))
                            flag = True
                        if can_be_multiple in tags:
                            if str in tags:
                                corrected[key][key2] = ",".join([i for i in re.split(r'\n|\r',value2 if value2 else "") if i])
                            elif list in tags:
                                corrected[key][key2]  = re.split(r'\n|\r',value2) if value2 else []
                        elif str in tags:
                            corrected[key][key2]  = value2.replace(r"\\n",r"\n").replace(r"\n","\n") if value2 else ""
                        elif int in tags:
                            corrected[key][key2] = int(value2) if value2 else 0
                        elif bool_ in tags:
                            corrected[key][key2] = bool_.create(value2)
                        elif bool_none in tags:
                            corrected[key][key2] = bool_none.create(value2)
                if flag is True:
                    return render_template(
                        "config_editor.html",
                        l=l,
                        data=data,
                        config_tags=config_tags,
                        len=len,
                        join=str.join,
                        split=str.split,
                        type=type,
                        can_be_multiple=can_be_multiple,
                        select=select,
                        str=str,
                        int=int,
                        bool=bool,
                        list=list,
                        red=Red,
                        fix_required=FixRequired,
                        flash_messages=flash_messages,
                        flash_messages_red=flash_messages_red
                    )
                else:
                    corrected["status"] = 1
                    with open('config.json', 'w', encoding='utf-8') as f:
                        json.dump(corrected, f, ensure_ascii=False, indent=4, sort_keys=False)
                    Thread(target=restart,args=(1,)).start()
                    return sanic.response.redirect("/")
    else:
        @app.route("/", methods=["GET", "POST"])
        async def main(request: Request):
            if request.method == "GET":
                return render_template(
                    "main.html",
                    l=l,
                    authenticated=auth.authenticated(request),
                    data=data
                )
            elif request.method == "POST":
                if auth.authenticated is True:
                    Thread(target=restart,args=(1,)).start()
                return sanic.response.redirect("/")

        @app.route("/login", methods=["GET", "POST"])
        async def login(request: Request):
            if auth.authenticated(request) is True:
                return sanic.response.redirect("/")
            else:
                flash_messages = []
                if request.method == "GET":
                    return render_template("login.html", l=l, flash_messages=flash_messages)
                elif request.method == "POST":
                    if request.form.get("password","") == data["web"]["password"]:
                        r = sanic.response.redirect("/")
                        auth.login_user(request, r)
                        return r
                    else: 
                        flash_messages.append(l('invalid_password'))
                        return render_template("login.html", l=l, flash_messages=flash_messages)

        @app.route("/logout")
        @auth.login_required
        async def logout(request: Request):
            r = sanic.response.redirect("/")
            auth.logout_user(request, r)
            return r

        @app.route("/config_editor", methods=["GET", "POST"])
        @auth.login_required
        async def config_editor(request: Request):
            flash_messages = []
            flash_messages_red = []
            if request.method == "GET":
                try:
                    with open('config.json', 'r', encoding='utf-8') as f:
                        data = json.load(f)
                except json.decoder.JSONDecodeError:
                    with open('config.json', 'r', encoding='utf-8-sig') as f:
                        data = json.load(f)
                return render_template(
                    "config_editor.html",
                    l=l,
                    data=data,
                    config_tags=config_tags,
                    len=len,
                    join=str.join,
                    split=str.split,
                    type=type,
                    can_be_multiple=can_be_multiple,
                    select=select,
                    str=str,
                    int=int,
                    bool=bool,
                    list=list,
                    red=Red,
                    fix_required=FixRequired,
                    flash_messages=flash_messages,
                    flash_messages_red=flash_messages_red
                )
            else:
                flag = False
                raw = request.form
                try:
                    with open('config.json', 'r', encoding='utf-8') as f:
                        data = json.load(f)
                except json.decoder.JSONDecodeError:
                    with open('config.json', 'r', encoding='utf-8-sig') as f:
                        data = json.load(f)
                corrected = data
                for key_,tags in config_tags.items():
                    keys = key_.replace("'","").replace("[","").split("]")
                    key = keys[0]
                    nest = len(keys) - 1

                    if nest == 1:
                        if dict in tags:
                            if corrected.get(key) is None:
                                corrected[key] = {}
                        else:
                            value = raw.get(f"['{key}']")
                        
                        if FixRequired in tags and value == corrected.get(key):
                            flash_messages_red.append(l('this_field_fix_required', key))
                            flag = True
                        if can_be_multiple in tags:
                            if str in tags:
                                corrected[key] = ",".join([i for i in re.split(r'\n|\r',value) if i]) if value else ""
                            elif list in tags:
                                corrected[key] = re.split(r'\r\n|\n',value) if value else []
                        elif str in tags:
                            corrected[key] = value.replace(r"\\n",r"\n").replace(r"\n","\n") if value else ""
                        elif int in tags:
                            corrected[key] = int(value) if value else 0
                        elif bool_ in tags:
                            corrected[key] = bool_.create(value)
                        elif bool_none in tags:
                            corrected[key] = bool_none.create(value)
                    elif nest == 2:
                        key2 = keys[1]

                        if dict in tags:
                            if corrected.get(key) is None:
                                if corrected.get(key).get(key2) is None:
                                    corrected[key][key2] = {}
                        else:
                            value2 = raw.get(f"['{key}']['{key2}']")
                        
                        if FixRequired in tags and value2 == corrected.get(key,{}).get(key2):
                            flash_messages_red.append(l('this_field_fix_required', f"{key}: {key2}"))
                            flag = True
                        if can_be_multiple in tags:
                            if str in tags:
                                corrected[key][key2] = ",".join([i for i in re.split(r'\n|\r',value2) if i]) if value2 else ""
                            elif list in tags:
                                corrected[key][key2]  = re.split(r'\r\n|\n',value2) if value2 else []
                        elif str in tags:
                            corrected[key][key2]  = value2.replace(r"\\n",r"\n").replace(r"\n","\n") if value2 else ""
                        elif int in tags:
                            corrected[key][key2] = int(value2) if value2 else 0
                        elif bool_ in tags:
                            corrected[key][key2] = bool_.create(value2)
                        elif bool_none in tags:
                            corrected[key][key2] = bool_none.create(value2)
                if flag is True:
                    return render_template(
                        "config_editor.html",
                        l=l,
                        data=corrected,
                        config_tags=config_tags,
                        len=len,
                        join=str.join,
                        split=str.split,
                        type=type,
                        can_be_multiple=can_be_multiple,
                        select=select,
                        str=str,
                        int=int,
                        bool=bool,
                        list=list,
                        red=Red,
                        fix_required=FixRequired,
                        flash_messages=flash_messages,
                        flash_messages_red=flash_messages_red
                    )
                else:
                    corrected["status"] = 1
                    with open('config.json', 'w', encoding='utf-8') as f:
                        json.dump(corrected, f, ensure_ascii=False, indent=4, sort_keys=False)
                    if raw.get("reload"):
                        Thread(target=restart, args=(1,)).start()
                        return sanic.response.redirect("/")
                    else:
                        flash_messages.append(l('web_saved'))
                        return render_template(
                            "config_editor.html",
                            l=l,
                            data=corrected,
                            config_tags=config_tags,
                            len=len,
                            join=str.join,
                            split=str.split,
                            type=type,
                            can_be_multiple=can_be_multiple,
                            select=select,
                            str=str,
                            int=int,
                            bool=bool,
                            list=list,
                            red=Red,
                            fix_required=FixRequired,
                            flash_messages=flash_messages,
                            flash_messages_red=flash_messages_red
                        )

        @app.route("/config_editor_old", methods=["GET", "POST"])
        @auth.login_required
        async def config_editor_old(request: Request):
            flash_messages = []
            flash_messages_red = []
            if request.method == "GET":
                try:
                    with open('config.json', 'r', encoding='utf-8') as f:
                        data = json.load(f)
                except json.decoder.JSONDecodeError:
                    with open('config.json', 'r', encoding='utf-8-sig') as f:
                        data = json.load(f)
                return render_template(
                    "config_editor_old.html",
                    l=l,
                    data=data,
                    config_tags=config_tags,
                    len=len,
                    join=str.join,
                    split=str.split,
                    type=type,
                    can_be_multiple=can_be_multiple,
                    select=select,
                    str=str,
                    int=int,
                    bool=bool,
                    list=list,
                    red=Red,
                    fix_required=FixRequired,
                    flash_messages=flash_messages,
                    flash_messages_red=flash_messages_red
                )
            else:
                flag = False
                raw = request.form
                try:
                    with open('config.json', 'r', encoding='utf-8') as f:
                        data = json.load(f)
                except json.decoder.JSONDecodeError:
                    with open('config.json', 'r', encoding='utf-8-sig') as f:
                        data = json.load(f)
                corrected = data
                for key_,tags in config_tags.items():
                    keys = key_.replace("'","").replace("[","").split("]")
                    key = keys[0]
                    nest = len(keys) - 1

                    if nest == 1:
                        if dict in tags:
                            if corrected.get(key) is None:
                                corrected[key] = {}
                        else:
                            value = raw.get(f"['{key}']")
                        
                        if FixRequired in tags and value == corrected.get(key):
                            flash_messages_red.append(l('this_field_fix_required', key))
                            flag = True
                        if can_be_multiple in tags:
                            if str in tags:
                                corrected[key] = ",".join([i for i in re.split(r'\n|\r',value) if i]) if value else ""
                            elif list in tags:
                                corrected[key] = re.split(r'\r\n|\n',value) if value else []
                        elif str in tags:
                            corrected[key] = value.replace(r"\\n",r"\n").replace(r"\n","\n") if value else ""
                        elif int in tags:
                            corrected[key] = int(value) if value else 0
                        elif bool_ in tags:
                            corrected[key] = bool_.create(value)
                        elif bool_none in tags:
                            corrected[key] = bool_none.create(value)
                    elif nest == 2:
                        key2 = keys[1]

                        if dict in tags:
                            if corrected.get(key) is None:
                                if corrected.get(key).get(key2) is None:
                                    corrected[key][key2] = {}
                        else:
                            value2 = raw.get(f"['{key}']['{key2}']")
                        
                        if FixRequired in tags and value2 == corrected.get(key,{}).get(key2):
                            flash_messages_red.append(l('this_field_fix_required', f"{key}: {key2}"))
                            flag = True
                        if can_be_multiple in tags:
                            if str in tags:
                                corrected[key][key2] = ",".join([i for i in re.split(r'\n|\r',value2) if i]) if value2 else ""
                            elif list in tags:
                                corrected[key][key2]  = re.split(r'\r\n|\n',value2) if value2 else []
                        elif str in tags:
                            corrected[key][key2]  = value2.replace(r"\\n",r"\n").replace(r"\n","\n") if value2 else ""
                        elif int in tags:
                            corrected[key][key2] = int(value2) if value2 else 0
                        elif bool_ in tags:
                            corrected[key][key2] = bool_.create(value2)
                        elif bool_none in tags:
                            corrected[key][key2] = bool_none.create(value2)
                if flag is True:
                    return render_template(
                        "config_editor_old.html",
                        l=l,
                        data=corrected,
                        config_tags=config_tags,
                        len=len,
                        join=str.join,
                        split=str.split,
                        type=type,
                        can_be_multiple=can_be_multiple,
                        select=select,
                        str=str,
                        int=int,
                        bool=bool,
                        list=list,
                        red=Red,
                        fix_required=FixRequired,
                        flash_messages=flash_messages,
                        flash_messages_red=flash_messages_red
                    )
                else:
                    corrected["status"] = 1
                    with open('config.json', 'w', encoding='utf-8') as f:
                        json.dump(corrected, f, ensure_ascii=False, indent=4, sort_keys=False)
                    if raw.get("reload"):
                        Thread(target=restart, args=(1,)).start()
                        return sanic.response.redirect("/")
                    else:
                        flash_messages.append(l('web_saved'))
                        return render_template(
                            "config_editor.html",
                            l=l,
                            data=corrected,
                            config_tags=config_tags,
                            len=len,
                            join=str.join,
                            split=str.split,
                            type=type,
                            can_be_multiple=can_be_multiple,
                            select=select,
                            str=str,
                            int=int,
                            bool=bool,
                            list=list,
                            red=Red,
                            fix_required=FixRequired,
                            flash_messages=flash_messages,
                            flash_messages_red=flash_messages_red
                        )

        @app.route("/commands_editor", methods=["GET", "POST"])
        @auth.login_required
        async def commands_editor(request: Request):
            flash_messages = []
            flash_messages_red = []
            if request.method == "GET":
                try:
                    with open('commands.json', 'r', encoding='utf-8') as f:
                        data = json.load(f)
                except json.decoder.JSONDecodeError:
                    with open('commands.json', 'r', encoding='utf-8-sig') as f:
                        data = json.load(f)
                return render_template(
                    "commands_editor.html",
                    l=l,
                    data=data,
                    commands_tags=commands_tags,
                    len=len,
                    join=str.join,
                    split=str.split,
                    type=type,
                    can_be_multiple=can_be_multiple,
                    select=select,
                    str=str,
                    int=int,
                    bool=bool,
                    list=list,
                    red=Red,
                    fix_required=FixRequired,
                    flash_messages=flash_messages,
                    flash_messages_red=flash_messages_red
                )
            elif request.method == "POST":
                flag = False
                raw = request.form
                try:
                    with open('commands.json', 'r', encoding='utf-8') as f:
                        data = json.load(f)
                except json.decoder.JSONDecodeError:
                    with open('commands.json', 'r', encoding='utf-8-sig') as f:
                        data = json.load(f)
                corrected = data
                for key_,tags in commands_tags.items():
                    keys = key_.replace("'","").replace("[","").split("]")
                    key = keys[0]
                    nest = len(keys) - 1

                    if nest == 1:
                        if dict in tags:
                            if corrected[key] is None:
                                corrected[key] = {}
                        else:
                            value = raw.get(f"['{key}']")
                        
                        if FixRequired in tags and value == corrected.get(key):
                            flash_messages_red.append(l('this_field_fix_required', key))
                            flag = True
                        if can_be_multiple in tags:
                            if str in tags:
                                corrected[key] = ",".join([i for i in re.split(r'\n|\r',value) if i]) if value else ""
                if flag is True:
                    return render_template(
                        "commands_editor.html",
                        l=l,
                        data=corrected,
                        commands_tags=commands_tags,
                        len=len,
                        join=str.join,
                        split=str.split,
                        type=type,
                        can_be_multiple=can_be_multiple,
                        select=select,
                        str=str,
                        int=int,
                        bool=bool,
                        list=list,
                        red=Red,
                        fix_required=FixRequired,
                        flash_messages=flash_messages,
                        flash_messages_red=flash_messages_red
                    )
                else:
                    with open('commands.json', 'w', encoding='utf-8') as f:
                        json.dump(corrected, f, ensure_ascii=False, indent=4, sort_keys=False)
                    if raw.get("reload"):
                        Thread(target=restart, args=(1,)).start()
                        return sanic.response.redirect("/")
                    else:
                        flash_messages.append(l('web_saved'))
                        return render_template(
                            "commands_editor.html",
                            l=l,
                            data=corrected,
                            commands_tags=commands_tags,
                            len=len,
                            join=str.join,
                            split=str.split,
                            type=type,
                            can_be_multiple=can_be_multiple,
                            select=select,
                            str=str,
                            int=int,
                            bool=bool,
                            list=list,
                            red=Red,
                            fix_required=FixRequired,
                            flash_messages=flash_messages,
                            flash_messages_red=flash_messages_red
                        )

        @app.route("/replies_editor", methods=["GET", "POST"])
        @auth.login_required
        async def replies_editor(request: Request):
            flash_messages = []
            flash_messages_red = []
            if request.method == "GET":
                try:
                    with open('replies.json', 'r', encoding='utf-8') as f:
                        data = json.load(f)
                except json.decoder.JSONDecodeError:
                    with open('replies.json', 'r', encoding='utf-8-sig') as f:
                        data = json.load(f)
                return render_template(
                    "replies_editor.html",
                    l=l,
                    data=data,
                    flash_messages=flash_messages,
                    flash_messages_red=flash_messages_red,
                    len=len,
                    enumerate=enumerate,
                    str=str
                )
            elif request.method == "POST":
                raw = request.form
                corrected = {}
                for num in range(0,int(raw["number"][0])):
                    trigger = raw.get(f"trigger{str(num)}")
                    if trigger is None:
                        flash_messages_red.append(l('cannot_be_empty'))
                        break
                    content = raw.get(f"content{str(num)}")
                    if content is None:
                        flash_messages_red.append(l('cannot_be_empty'))
                        break
                    corrected[trigger] = content
                with open('replies.json', 'w', encoding='utf-8') as f:
                    json.dump(corrected, f, ensure_ascii=False, indent=4, sort_keys=False)
                if raw.get("reload"):
                    Thread(target=restart, args=(1,)).start()
                    return sanic.response.redirect("/")
                else:
                    flash_messages.append(l('web_saved'))
                    return render_template(
                        "replies_editor.html",
                        l=l,
                        data=corrected,
                        flash_messages=flash_messages,
                        flash_messages_red=flash_messages_red,
                        len=len,
                        enumerate=enumerate,
                        str=str
                    )

        @app.route("/party_viewer", methods=["GET"])
        @auth.login_required
        async def party_viewer(request: Request):
            return render_template(
                "party_viewer.html",
                l=l,
                clients=clients,
                enumerate=enumerate
            )

        @app.route("/clients<num>", methods=["GET", "POST"])
        @auth.login_required
        async def clients_viewer(request: Request, num: str):
            num = int(num)
            client = clients[num] if len(clients[num:num+1]) == 1 else None

            if client is None:
                sanic.exceptions.abort(404)
            flash_messages = []
            if request.method == "GET":
                return render_template(
                    "clients_viewer.html",
                    l=l,
                    client=client,
                    none=None,
                    len=len,
                    member_asset=member_asset,
                    placeholder="images/placeholder.png",
                    crown="images/crown.png",
                    flash_messages=flash_messages
                )
            else:
                if request.form.get("command") is not None:
                    content = request.form.get("command")
                    message = WebMessage(content, request.cookies.get(auth.cookie_key, 'NoID'), client)
                    await process_command(message)
                    for mes in message.result:
                        for m in mes.split('\n'):
                            flash_messages.append(m)

                    return render_template(
                        "clients_viewer.html",
                        l=l,
                        client=client,
                        none=None,
                        len=len,
                        member_asset=member_asset,
                        placeholder="images/placeholder.png",
                        crown="images/crown.png",
                        flash_messages=flash_messages
                    )
                else:
                    return sanic.response.redirect(f"/clients{num}")

        @app.route("/clients_info/<num>", methods=["GET"])
        @auth.login_required
        async def clients_info(request: Request, num: str):
            num = int(num)
            client = clients[num] if len(clients[num:num+1]) == 1 else None

            if client is None:
                return sanic.response.json(
                    {
                        "error": "account_not_exists"
                    }
                )
            elif client.isready is False:
                return sanic.response.json(
                    {
                        "error": "account_not_loaded"
                    }
                )
            elif client.party == None:
                return sanic.response.json(
                    {
                        "error": "party_moving"
                    }
                )
            else:
                return sanic.response.json(
                    {
                        "display_name": client.user.display_name,
                        "id": client.user.id,
                        "leader": client.party.me.leader,
                        "outfit": member_asset(client.party.me, "outfit"),
                        "backpack": member_asset(client.party.me, "backpack"),
                        "pickaxe": member_asset(client.party.me, "pickaxe"),
                        "emote": member_asset(client.party.me, "emote"),
                        "party_id": client.party.id,
                        "members": [
                            {
                                "display_name": i.display_name,
                                "id": i.id,
                                "leader": i.leader,
                                "outfit": member_asset(i, "outfit"),
                                "backpack": member_asset(i, "backpack"),
                                "pickaxe": member_asset(i, "pickaxe"),
                                "emote": member_asset(i, "emote")
                            } for i in client.party.members.copy().values()
                        ]
                    }
                )

        @app.route("/boot_switch", methods=["GET", "POST"])
        @auth.login_required
        async def boot_switch(request: Request):
            if request.method == "GET":
                return render_template(
                    "boot_switch.html",
                    l=l,
                    len=len
                )
            elif request.method == "POST":
                raw = request.form
                for i in raw.keys():
                    if "on" in i or "off" in i:
                        break
                on_or_off = i
                num = int(re.sub(r"on|off","", on_or_off))
                on_or_off = i.replace(str(num),"")
                loop = asyncio.get_event_loop()
                if on_or_off == "on":
                    clients[num].booting=True
                    loop.create_task(clients[num].start())
                elif on_or_off == "off":
                    loop.create_task(clients[num].close())
                return sanic.response.redirect("/boot_switch")

        @app.route("/boot_info", methods=["GET"])
        @auth.login_required
        async def boot_info(request: Request):
            data = {}
            for client in clients:
                if not client.booting and not client.isready:
                    data[client.email] = {
                        "info": "info_closed",
                        "booting": client.booting,
                        "isready": client.isready
                    }
                elif client.booting:
                    data[client.email] = {
                        "info": "info_booting",
                        "booting": client.booting,
                        "isready": client.isready
                    }
                elif client.isready:
                    data[client.email] = {
                        "info": "info_ready",
                        "booting": client.booting,
                        "isready": client.isready
                    }
            return sanic.response.json(data)

        @app.exception(sanic.exceptions.NotFound)
        async def not_found(request: Request, exception: Exception):
            return render_template("not_found.html", l=l)

        @auth.no_auth_handler
        async def unauthorized(request: Request, *args, **kwargs):
            return sanic.response.redirect("/")

async def run_bot() -> None:
    global kill
    try:
        for client in clients:
            client.booting = True
        if data.get('restart_in') not in [None, 0]:
            Timer(data.get('restart_in'), restart).start()
        await fortnitepy.start_multiple(
            clients,
            all_ready_callback=lambda: send(l("bot"),l("all_login"),green,add_p=lambda x:f'[{now_()}] {x}') if len(clients) > 1 else print('')
        )
    except fortnitepy.AuthException as e:
        if data["loglevel"] == "debug":
            send(l("bot"),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
        if "errors.com.epicgames.account.oauth.exchange_code_not_found" in e.args[0]:
            send(l("bot"),l("exchange_code_error"),red,add_p=lambda x:f'[{now_()}] {x}',add_d=lambda x:f'>>> {x}')
        elif "Invalid device auth details passed." in e.args[0]:
            email = e.args[0].split("-")[0].strip()
            details = get_device_auth_details()
            details.pop(email.lower())
            with open(filename, 'w') as f:
                json.dump(details, f)
            restart()
        else:
            send(l("bot"),l("login_failed"),red,add_p=lambda x:f'[{now_()}] {x}',add_d=lambda x:f'>>> {x}')
        kill=True
        sys.exit(1)
    except fortnitepy.HTTPException as e:
        if data["loglevel"] == "debug":
            send(l("bot"),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
        if "reset" in e.args[0]:
            send(l("bot"),l("password_reset_error"),red,add_p=lambda x:f'[{now_()}] {x}',add_d=lambda x:f'>>> {x}')
        else:
            send(l("bot"),l("login_failed"),red,add_p=lambda x:f'[{now_()}] {x}',add_d=lambda x:f'>>> {x}')
        kill=True
        sys.exit(1)
    except KeyboardInterrupt:
        kill=True
        sys.exit(1)
    except Exception:
        send(l("bot"),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
        send(l("bot"),l("failed_to_load_account"),red,add_p=lambda x:f'[{now_()}] {x}',add_d=lambda x:f'>>> {x}')
        kill=True
        sys.exit(1)

async def run_app() -> None:
    try:
        await app.create_server(host=data['web']['ip'], port=data['web']['port'], return_asyncio_server=True, access_log=data['web']['log'])
    except OSError:
        if data["loglevel"] == "debug":
            send(l("bot"),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
        send(l("bot"),l("web_already_running"),red,add_p=lambda x:f'[{now_()}] {x}',add_d=lambda x:f'>>> {x}')
    except Exception:
        send(l("bot"),traceback.format_exc(),red,add_d=lambda x:f'>>> {x}')
    else:
        if data["status"] == 0 or bot_ready is False:
            webbrowser.open(f"http://{data['web']['ip']}:{data['web']['port']}")
        if os.getcwd().startswith('/app') or os.getcwd().startswith('/home/runner'):
            Thread(target=uptime).start()
        send(l("bot"),l("web_running",f"http://{data['web']['ip']}:{data['web']['port']}"),add_p=lambda x:f'[{now_()}] {x}',add_d=lambda x:f'>>> {x}')

loop = asyncio.get_event_loop()
if data.get('web',{}).get('enabled',True) is True or data.get('status',1)  == 0:
    loop.create_task(run_app())
if data.get('status',1) != 0 and bot_ready:
    loop.create_task(run_bot())
try:
    loop.run_forever()
except KeyboardInterrupt:
    kill=True
    sys.exit(1)
