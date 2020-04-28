import traceback
import requests
import time
import json
import sys
import os

def AddNewKey(data: dict, new: dict) -> dict:
    result = data.copy()
    for key,value in new.items():
        if type(value) ==  dict:
            result[key] = AddNewKey(result.get(key, {}), value)
        result.setdefault(key, value)
    return result

def CheckUpdate(filename: str, githuburl: str) -> bool:
    print(f'{filename} のアップデートを確認中...')
    try:
        for count, text in enumerate(filename[::-1]):
            if text == ".":
                filename_ = filename[:len(filename)-count-1]
                extension = filename[-count-1:]
                break
        else:
            extension == ""
        if extension == ".py" or extension == ".bat" or extension == ".txt" or extension == ".md" or extension == "":
            if os.path.isfile(filename):
                with open(filename, encoding='utf-8') as f:
                    current = f.read()
            else:
                github = requests.get(githuburl + filename)
                if github.status_code != 200:
                    print(f'{filename} のデータを取得できませんでした。')
                    return None
                github.encoding = github.apparent_encoding
                github = github.text.encode(encoding='utf-8')
                with open(filename, 'bw') as f:
                    f.write(github)
                with open(filename, encoding='utf-8') as f:
                    current = f.read()
            github = requests.get(githuburl + filename)
            if github.status_code != 200:
                print(f'{filename} のデータを取得できませんでした。')
                return None
            github.encoding = github.apparent_encoding
            github = github.text.encode(encoding='utf-8')
            if current.replace('\n','').replace('\r','').encode(encoding='utf-8') != github.decode().replace('\n','').replace('\r','').encode(encoding='utf-8'):
                print(f'{filename} のアップデートを確認しました!')
                print(f'{filename} をバックアップ中...')
                if os.path.isfile(f'{filename_}_old{extension}'):
                    try:
                        os.remove(f'{filename_}_old{extension}')
                    except PermissionError:
                        print(f'{filename} ファイルを削除できませんでした。\n{traceback.format_exc()}')
                try:
                    os.rename(filename, f'{filename_}_old{extension}')
                except PermissionError:
                    print(f'{filename} ファイルをバックアップできませんでした。\n{traceback.format_exc()}')
                else:
                    with open(filename, 'bw') as f:
                        f.write(github)
                    print(f'{filename} の更新が完了しました!\n')
                    CheckUpdate("auto-updater.py", githuburl)
                    CheckUpdate("requirements.txt", githuburl)
                    CheckUpdate("config.json", githuburl)
                    CheckUpdate("commands.json", githuburl)
                    CheckUpdate("Check update.bat", githuburl)
                    CheckUpdate("INSTALL IFNOTWORK.bat", githuburl)
                    return True
            else:
                print(f'{filename} の更新はありません!\n')
                return False
        elif extension == ".json":
            if os.path.isfile(filename):
                with open(filename, encoding='utf-8') as f:
                    current = f.read()
            else:
                github = requests.get(githuburl + filename)
                if github.status_code != 200:
                    print(f'{filename} のデータを取得できませんでした。')
                    return None
                github.encoding = github.apparent_encoding
                github = github.text.encode(encoding='utf-8')
                with open(filename, 'bw') as f:
                    f.write(github)
                with open(filename, encoding='utf-8') as f:
                    current = f.read()
            current = json.loads(current)
            github = requests.get(githuburl + filename)
            if github.status_code != 200:
                print(f'{filename} のデータを取得できませんでした。')
                return None
            github.encoding = github.apparent_encoding
            github = github.text
            
            github = json.loads(github)
            new = AddNewKey(current, github)
            if current != new:
                print(f'{filename} のアップデートを確認しました!')
                print(f'{filename} をバックアップ中...')
                try:
                    if os.path.isfile(f'{filename_}_old{extension}'):
                        try:
                            os.remove(f'{filename_}_old{extension}')
                        except PermissionError:
                            print(f'{filename_}_old{extension} ファイルを削除できませんでした\n{traceback.format_exc()}')
                    os.rename(filename, f'{filename_}_old{extension}')
                except PermissionError:
                    print(f'{filename} ファイルをバックアップできませんでした\n{traceback.format_exc()}')
                    return None
                else:
                    with open(filename, 'w', encoding="utf-8") as f:
                        json.dump(new, f, indent=4, ensure_ascii=False)
                    print(f'{filename} の更新が完了しました!\n')
                    return True
            else:
                print(f'{filename} の更新はありません!\n')
                return False
        else:
            print(f'拡張子 {extension} は対応していません\n')
            return None
    except Exception:
        print("アップデートに失敗しました")
        print(traceback.format_exc())
        return None

if "-dev" in sys.argv:
    githuburl = "https://raw.githubusercontent.com/gomashio1596/Fortnite-LobbyBot/Dev/"
else:
    githuburl = "https://raw.githubusercontent.com/gomashio1596/Fortnite-LobbyBot/master/"
if CheckUpdate("index.py", githuburl) is False and "-all" in sys.argv:
    CheckUpdate("requirements.txt", githuburl)
    CheckUpdate("config.json", githuburl)
    CheckUpdate("commands.json", githuburl)
    CheckUpdate("Check update.bat", githuburl)
    CheckUpdate("INSTALL IFNOTWORK.bat", githuburl)
CheckUpdate("auto-updater.py", githuburl)
CheckUpdate("README.md", githuburl)
print("すべてのアップデートが完了しました")
