# Fortnite-LobbyBot
Fortnitepyを使用したFortniteのボット  
コマンドを送ることで操作ができる

# 導入
[Python 3.](https://www.python.org/downloads "Pythonダウンロード")以上が必要  
Python 3.8はエラーが多く出るのでそれ以外を推奨  

INSTALL.batを実行する  
configに情報を書き込む  
commandsに好きなコマンド名を書き込む  
RUN.batを実行する  
exchange_codeを[公式サイト](https://www.epicgames.com "epicgames.com")でボットのアカウントにログインし、
[ログイン](https://www.epicgames.com/id/login?redirectUrl=https%3A%2F%2Fwww.epicgames.com%2Fid%2Fapi%2Fexchange "ログイン")で取得してください。

# config
```
email               : ボット用アカウントのメールアドレス , で区切ることで複数設定可
password            : ボット用アカウントのパスワード , で区切ることで複数設定可
owner               : 所有者として設定したいユーザーの名前またはID
platform            : ボットのプラットフォーム 後述
cid                 : ボットの初期スキンID
bid                 : ボットの初期バッグのID
pickaxe_id          : ボットの初期ツルハシのID
eid                 : ボットの初期エモートのID
playlist            : ボットの初期プレイリストのID
banner              : ボットの初期バナーのID
banner_color        : ボットの初期バナーの色ID
level               : ボットの初期レベル
tier                : ボットの初期ティア
xpboost             : ボットの初期XPブースト
friendxpboost       : ボットの初期フレンドXPブースト
status              : ボットの初期ステータス
private             : ボットの初期のプライバシー 後述
partychat           : ボットがパーティーチャットからコマンドを受け付けるかどうか true か false
joinmessage         : ボットのパーティーに誰かが参加した時のメッセージ \n で改行
randommessage       : ボットのパーティーに誰かが参加した時のランダムメッセージ , で区切る \n で改行
joinmessageenable   : ボットのパーティーに誰かが参加した時にメッセージを出すかどうか true か false
randommessageenable : ボットのパーティーに誰かが参加した時にランダムメッセージを出すかどうか true か false
skinmimic           : 他人のスキンを真似るかどうかの設定 true か false
emotemimic          : 他人のエモートを真似るかどうかの設定 true か false
acceptinvite        : ボットが招待を承諾するかどうかの設定 所有者からの招待は常に承諾 true か false
acceptfriend        : ボットがフレンド申請を承諾するかどうかの設定 true か false か null
addfriend           : ボットがパーティーメンバーにフレンド申請を送るかどうかの設定 true か false
inviteinterval      : 招待を承諾した後intervalの秒数だけ招待を拒否するようにするかどうかの設定 true か false
interval            : 招待を承諾した後招待を拒否する秒数
waitinterval        : waitコマンドで招待を拒否する秒数
no-logs             : コンソールにログを出すかどうかの設定 true か false
ingame-error        : プレイヤーにエラーを送信するかどうかの設定 true か false
discord-log         : Discordにログを送信するかどうかの設定 true か false
hide-email          : Discordのログでメールアドレスを隠すかどうかの設定 true か false
hide-password       : Discordのログでパスワードを隠すかどうかの設定 true か false
hide-webhook        : Discordのログでwebhookのurlを隠すかどうかの設定 true か false
hide-api-key        : DiscordのログでAPIキーを隠すかどうかの設定 true か false
webhook             : Discordのwebhookのurl
caseinsensitive     : コマンドを大文字小文字、平仮名片仮名を区別しないかどうかの設定 true か false
api-key             : Fortnite-API.comのAPIキー 後述
loglevel            : ログにどのくらいの情報を流すか normal か info か debug
debug               : Fortnitepyのデバッグモードをオンにするかどうかの設定 true か false
```

# コマンド一覧
コマンド名はcommands.json内の表記  
全て , で区切ることで複数設定可  
アイテム名を打つことでそのアイテムにすることもできる  

```
ownercommands        : 所有者しか使えないコマンドを指定する
true                 : コマンドの true として扱う文字列
false                : コマンドの false として扱う文字列
me                   : コマンドの送り主として扱う文字列
prev                 : 一つ前のコマンドを繰り返す
eval                 : eval [プログラム] 内容を式として評価し、その内容を返す
exec                 : exec [プログラム] 内容を文として評価し、その内容を返す
restart              : プログラムを再起動する
relogin              : アカウントに再ログインする
reload               : configとcommandsを再読み込みする
get                  : get [ユーザー名/ユーザーID] ユーザーのアイテム各種の情報を取得する
friendcount          : 現在のフレンド数を表示する
pendingcount         : 現在のフレンド申請数を表示する(方向関係なし)
blockcount           : 現在のブロック数を表示する
skinmimic            : skinmimic [true / false] 他人のスキンを真似るかどうかの設定
emotemimic           : emotemimic [true / false] 他人のエモートを真似るかどうかの設定
partychat            : partychat [true / false] パーティーチャットからのコマンドを受け付けるかどうかの設定
acceptinvite         : acceptinvite [true / false] パーティー招待を承諾するかどうかの設定
acceptfriend         : acceptfriend [true / false] フレンド申請を承諾するかどうかの設定
joinmessageenable    : joinmessageenable [true / false] パーティーに誰かが参加した時のメッセージを出すかどうかの設定
randommessageenable  : randommessageenable [true / false] パーティーに誰かが参加したときのランダムメッセージを出すかどうかの設定
wait                 : configのwaitintervalの秒数だけ招待を拒否する
join                 : join [ユーザー名/ユーザーID] ユーザーのパーティーに参加する
joinid               : joinid [パーティーID] パーティーに参加する
leave                : パーティーを離脱する
invite               : invite [ユーザー名 / ユーザーID] ユーザーをパーティーに招待する
message              : message [ユーザー名 / ユーザーID] : [内容] ユーザーにメッセージを送信する
partymessage         : partymessage [内容] パーティーチャットにメッセージを送信する
status               : status [内容] ステータスを設定する
banner               : banner [バナーID] [バナーの色] バナーを設定する
level                : level [レベル] レベルを設定する
bp                   : bp [ティア] [XPブースト] [フレンドXPブースト] バトルパス情報を設定する
privacy              : privacy [privacy_public / privacy_friends_allow_friends_of_friends / privacy_friends / privacy_private_allow_friends_of_friends / privacy_private]
privacy_public       : privacy コマンドで使う privacy_public
privacy_friends_allow_friends_of_friends  : privacy コマンドで使う privacy_friends_allow_friends_of_friends
privacy_friends      : privacy コマンドで使う privacy_friends
privacy_private_allow_friends_of_friends  : privacy コマンドで使う privacy_private_allow_friends_of_friends
privacy_private      : privacy コマンドで使う privacy_private
getuser              : getuser [ユーザー名 / ユーザーID] ユーザーの名前とIDを表示する
getfriend            : getefriend [ユーザー名 / ユーザーID] フレンドの名前とIDを表示する
getpending           : getpending [ユーザー名 / ユーザーID] 保留中のフレンドの名前とIDを表示する
getblock             : getblock [ユーザー名 / ユーザーID] ブロックしたユーザーの名前とIDを表示する
info                 : info [info_party / info_item / id / skin / bag / pickaxe / emote] パーティー/アイテムの情報を表示する
info_party           : info コマンドで使う info_party
info_item            : info コマンドで使う info_item
pending              : pending [true / false] 保留しているフレンド申請を全て承諾/拒否する
removepending        : 自分が送ったフレンド申請を全て解除する
addfriend            : addfriend [ユーザー名 / ユーザーID] ユーザーにフレンド申請を送信する
removefriend         : removefriend [ユーザー名 / ユーザーID] ユーザーをフレンドから削除する
acceptpending        : acceptpending [ユーザー名 / ユーザーID] ユーザーからのフレンド申請を承諾する
declinepending       : declinepending [ユーザー名 / ユーザーID] ユーザーからのフレンド申請を拒否する
blockfriend          : blockfriend[ユーザー名 / ユーザーID] ユーザーをブロックする
unblockfriend        : unblockfriend [ユーザー名 / ユーザーID] ユーザーをブロック解除する
chatban              : chatban [ユーザー名 / ユーザーID] : [理由(任意)] ユーザーをチャットバンする
promote              : promote [ユーザー名 / ユーザーID] ユーザーにパーティーリーダーを譲渡する
kick                 : kick [ユーザー名 / ユーザーID] ユーザーをキックする
ready                : 準備OK 状態にする
unready              : 準備中 状態にする
sitout               : 欠場中 状態にする
stop                 : エモート/全てのスキン/全てのエモートを停止する
allskin              : 全てのスキンを表示する
allemote             : 全てのエモートを表示する
setstyle             : setstyle [skin / bag / pickaxe] [スタイル名]現在付けているアイテムのスタイル名を検索し、そのスタイルに設定する
addstyle             : addstyle [skin / bag / pickaxe] [スタイル名]現在付けているアイテムのスタイル名を検索し、そのスタイルに現在のスタイルを追加する
setenlightenment     : setenlightenment [数値] [数値] スキンのenlightenment情報を設定する 後述
id                   : id [ID] IDでアイテムを検索する
skin                 : skin [スキン名] スキン名でスキンを検索する
bag                  : bag [バッグ名] バッグ名でバッグを検索する
pickaxe              : pickaxe [ツルハシ名] ツルハシ名でツルハシを検索する
emote                : emote [エモート名] エモート名でエモートを検索する
set                  : set [セット名] セット名でアイテムを検索する
setvariant           : setvariant [ID] [variant] [数値] variant/数値は無限に設定可 数が合わない場合は無視される スタイル情報を設定する 後述
addvariant           : addvariant [ID] [variant] [数値] variant/数値は無限に設定可 数が合わない場合は無視される スタイル情報を設定する 後述
skinasset            : skinasset [アセットパス] スキンをアセットパスから設定する
bagasset             : bagasset [アセットパス] バッグをアセットパスから設定する
pickasset            : pickasset [アセットパス] ツルハシをアセットパスから設定する
emoteasset           : emoteasset [アセットパス] エモートをアセットパスから設定する
```

# replies
"反応するメッセージ": "返す文字列"  
のように設定する  
複数ある場合は下のように , をつける  
```
{
    "hello": "こんにちは",
    "goodbye": "さようなら"
}
```

# その他
プラットフォーム  
```
Windows     : WIN
Mac         : MAC
PlayStation : PSN
XBox        : XBL
Switch      : SWT
IOS         : IOS
Android     : AND
```
プライバシー
```
public                           : パブリック
friends_allow_friends_of_friends : フレンド(フレンドのフレンドを許可)
friends                          : フレンド
private_allow_friends_of_friends : プライベート(フレンドのフレンドを許可)
private                          : プライベート
```

APIキー  
```
Discordアカウントが必要
```
[ここ](https://discordapp.com/invite/AqzEcMm "Fortnite-API.com 招待リンク")からサーバーに参加  
[このサイト](https://fortnite-api.com/profile "Fortnite-API.com")からAPIキーを生成、コピーしてconfigのapi-keyに張り付ける  

variant  
```
pattern/numeric/clothing_color/jersey_color/parts/progressive/particle/material/emissive
基本的にはmaterialやprogressive,partsなどか多く使われている
紫スカルトルーパーの場合は clothing_color 1
jersey_color はサッカースキンで使われます
```

enlightenment
```
8ボールvsスクラッチのグリッチなどの情報
シーズン[チャプター2内] / 数値 の組み合わせ
```
