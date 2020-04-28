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
                    await reply(message, f"ユーザー {str(user)} / {user.id} をブラックリストに追加しました")
                else:
                    await reply(message, f"ユーザー {str(user)} / {user.id} は既にブラックリストに追加されています")
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
                    await reply(message, f"ユーザー {str(user)} / {user.id} をブラックリストから削除")
                else:
                    await reply(message, f"ユーザー {str(user)} / {user.id} はブラックリストに含まれていません")
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
                    await reply(message, f"ユーザー {str(user)} / {user.id} をホワイトリストに追加しました")
                else:
                    await reply(message, f"ユーザー {str(user)} / {user.id} は既にホワイトリストに追加されています")
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
                    await reply(message, f"ユーザー {str(user)} / {user.id} をホワイトリストから削除")
                else:
                    await reply(message, f"ユーザー {str(user)} / {user.id} はホワイトリストに含まれていません")
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
            os.execv(os.sys.executable,['python', *sys.argv])
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
            sys.exit(1)
        except Exception:
            print(red(traceback.format_exc()))
            print(red(f'[{now_()}] [{client.user.display_name}] アカウントの読み込みに失敗しました。もう一度試してみてください。'))
            dstore(name,f'>>> {traceback.format_exc()}')
            dstore(name,f'>>> アカウントの読み込みに失敗しました。もう一度試してみてください')
            kill=True
            sys.exit(1)

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
                                print(green(f'[{now_()}] [{client.user.display_name}] 所有者: {str(client.owner.display_name)}'))
                            dstore(client.user.display_name,f'所有者: {str(client.owner.display_name)}')
                        else:
                            if data['no-logs'] is False:
                                print(green(f'[{now_()}] [{client.user.display_name}] 所有者: {str(client.owner.display_name)} / {client.owner.id}'))
                            dstore(client.user.display_name,f'所有者: {str(client.owner.display_name)} / {client.owner.id}')
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
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(name) and user.id != client.user.id and user.id not in blacklist}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.id not in blacklist:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')
            if len(users) > 30:
                await reply(message, f"見つかったユーザー数 {len(users)} は多すぎます")
                return
            if len(users) == 0:
                await reply(message, 'ユーザーが見つかりません')
                return
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
            await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をブラックリストに追加しました")
        else:
            await reply(message, f"ユーザー {str(user.display_name)} / {user.id} は既にブラックリストに追加されています")""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
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
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and user.id in blacklist}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.id in blacklist:
                        users[str(user.display_name)] = user
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
            await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をブラックリストから削除")
        else:
            await reply(message, f"ユーザー {str(user.display_name)} / {user.id} はブラックリストに含まれていません")""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
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
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and user.id not in whitelist}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.id not in whitelist:
                        users[str(user.display_name)] = user
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
                await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をホワイトリストに追加しました")
            else:
                await reply(message, f"ユーザー {str(user.display_name)} / {user.id} は既にホワイトリストに追加されています")""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
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
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and user.id in whitelist}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.id in whitelist:
                        users[str(user.display_name)] = user
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
                    await reply(message, f"ユーザー {str(user.display_name)} / {user.id} をホワイトリストから削除")
                else:
                    await reply(message, f"ユーザー {str(user.display_name)} / {user.id} はホワイトリストに含まれていません")
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        if str(user.display_name) in data["blacklist"] or user.id in data["blacklist"]:
            blacklist.remove(user.id)
            try:
                data["blacklist"].remove(str(user.display_name))
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
            await reply(message, f"ユーザー {str(user.display_name)} / {user.id} はブラックリストに含まれていません")""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += "\n数字を入力することでそのユーザーをホワイトリストから削除します"
                await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['addinvitelist'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['addinvitelist']}] [ユーザー名/ユーザーID]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and user.id not in client.invitelist}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.id not in client.invitelist:
                        users[str(user.display_name)] = user
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
                    await reply(message, f"ユーザー {str(user.display_name)} / {user.id} を招待リストに追加しました")
                else:
                    await reply(message, f"ユーザー {str(user.display_name)} / {user.id} は既に招待リストに追加されています")
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
            await reply(message, f"ユーザー {str(user.display_name)} / {user.id} を招待リストに追加しました")
        else:
            await reply(message, f"ユーザー {str(user.display_name)} / {user.id} は既に招待リストに追加されています")""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += "\n数字を入力することでそのユーザーをブラックリストに追加します"
                await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, 'エラー')

    elif args[0] in commands['removeinvitelist'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['removeinvitelist']}] [ユーザー名/ユーザーID]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and user.id in client.invitelist}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.id in client.invitelist:
                        users[str(user.display_name)] = user
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
                    await reply(message, f"ユーザー {str(user.display_name)} / {user.id} を招待リストから削除")
                else:
                    await reply(message, f"ユーザー {str(user.display_name)} / {user.id} は招待リストに含まれていません")
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
            await reply(message, f"ユーザー {str(user.display_name)} / {user.id} を招待リストから削除")
        else:
            await reply(message, f"ユーザー {str(user.display_name)} / {user.id} は招待リストに含まれていません")""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += "\n数字を入力することでそのユーザーをブラックリストから削除します"
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
            users = {str(member.display_name): member for member in client.user.party.members.values() if rawcontent in str(member.display_name)}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.user.party.members.get(user.id) is not None:
                        users[str(user.display_name)] = user
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
        await reply(message, f'''{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}''')""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
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
                text+=f'\n{str(friend.display_name)}'
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
                    outbound+=f'\n{str(pending.display_name)}'
                elif pending.direction == 'INBOUND':
                    inbound+=f'\n{str(pending.display_name)}'
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
                text+=f'\n{str(block.display_name)}'
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
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.has_friend(user.id) is True:
                        users[str(user.display_name)] = user
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
            await reply(message, 'パーティーの参加リクエストを処理中にエラーが発生しました')""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
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
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.has_friend(user.id) is True:
                        users[str(user.display_name)] = user
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
            await reply(message, 'パーティー招待の送信リクエストを処理中にエラーが発生しました')""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
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
            users = {str(user.display_name): user for user in cache_users.values() if send[0] in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is True}
            try:
                user=await client.fetch_profile(send[0])
                if user is not None:
                    if client.has_friend(user.id) is True:
                        users[str(user.display_name)] = user
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
            await reply(message, 'ユーザー情報のリクエストを処理中にエラーが発生しました')""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user, "send": send} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
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
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    users[str(user.display_name)] = user
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
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.has_friend(user.id) is True:
                        users[str(user.display_name)] = user
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
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.is_pending(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.is_pending(user.id) is True:
                        users[str(user.display_name)] = user
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
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.is_blocked(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.is_blocked(user.id) is True:
                        users[str(user.display_name)] = user
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
                            await reply(message, f'{str(pending.display_name)} のフレンド申請の承認リクエストを処理中にエラーが発生しました')
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
            users = {str(user.display_name): user for name, user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is False}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.has_friend(user.id) is False:
                        users[str(user.display_name)] = user
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
            await reply(message, 'フレンド申請の送信リクエストを処理中にエラーが発生しました')""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
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
            users = {str(user.display_name): user for name, user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.has_friend(user.id) is True:
                        users[str(user.display_name)] = user
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
            await reply(message, 'フレンドの削除リクエストを処理中にエラーが発生しました')""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
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
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.is_pending(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.is_pending(user.id) is True:
                        users[str(user.display_name)] = user
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
            await reply(message, 'フレンドの追加リクエストを処理中にエラーが発生しました')""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
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
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.is_pending(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.is_pending(user.id) is True:
                        users[str(user.display_name)] = user
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
            await reply(message, 'フレンド申請の拒否リクエストを処理中にエラーが発生しました')""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
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
            users = {user.display_name: user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.is_blocked(user.id) is False}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.is_blocked(user.id) is False:
                        users[str(user.display_name)] = user
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
            await reply(message, 'フレンドのブロックリクエストを処理中にエラーが発生しました')""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
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
            users = {user.display_name: user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.is_blocked(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.is_blocked(user.id) is True:
                        users[str(user.display_name)] = user
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
            await reply(message, 'ブロックしたユーザーのブロック解除リクエストを処理中にエラーが発生しました')""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
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
            users = {str(member.display_name): member for member in client.user.party.members.values() if rawcontent in str(member.display_name)}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.user.party.members.get(user.id) is not None:
                        users[str(user.display_name)] = user
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
            await reply(message, '既にバンされています')""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user, "reason": reason} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
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
            users = {str(member.display_name): member for member in client.user.party.members.values() if rawcontent in str(member.display_name)}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.user.party.members.get(user.id) is not None:
                        users[str(user.display_name)] = user
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
            await reply(message, 'パーティーリーダーの譲渡リクエストを処理中にエラーが発生しました')""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
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
            users = {str(member.display_name): member for member in client.user.party.members.values() if rawcontent in str(member.display_name)}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.user.party.members.get(user.id) is not None:
                        users[str(user.display_name)] = user
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
            await reply(message, 'パーティーメンバーのキックリクエストを処理中にエラーが発生しました')""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
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
