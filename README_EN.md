# Fortnite-LobbyBot
[![Python Versions](https://img.shields.io/badge/3.7%20%7C%203.8-blue)](https://www.python.org/downloads/)  
<a href="https://discord.gg/NEnka5N"><img src="https://discordapp.com/api/guilds/718709023427526697/widget.png?style=banner2" /></a>  
A Fortnite bot using fortnitepy  
You can control bot by sending command  

My translation is bad. If you have better translation, please tell me.  

# Install
# PC
https://github.com/gomashio1596/Fortnite-LobbyBot  
[Python 3.7](https://www.python.org/downloads "Python Download") or higher is required  

Run INSTALL.bat  
Run RUN.bat  
Write details in site which opened  
Press Save button
You can write other details by reloading tab  

# Repl.it
https://repl.it  
Click "sign up" on the top right  
Click "+ new repl" on the top right, then open "Import From GitHub" tab  
Copy
https://github.com/gomashio1596/Fortnite-LobbyBot  
and paste this to "Paste any repository URL"  
Press "Import from GitHub"  
Press "run▶" on the site which opened(Call this repl page) on top  
Create account in [Uptimerobot](https://uptimerobot.com "Uptimerobot") 
and press "Dashboard"  
Press "\+ Monitor" and back to repl.it, then open "web" tab and copy URL  
Go to uptimerobot, change "Monitor Type" to "HTTP(s)" and paste URL  
Enter any name in "Friendly Name" and press "Create Monitor"  
Write details in web page  
You can write other details by reload tab  

# Glitch
Glitch is not recommended because can't make bot 24/7!

https://glitch.com
Click Sign in on the top right  
https://glitch.com/~fortnite-lobbybot  
Click project name and click Remix Project to remix  
Click project name(your project) and click Make This Project Private to make project private  
Click Show and In a new Window  
Write details in site which opened  
You can write other details by reload tab  

# config
```
Fortnite
email                     : Email address for bot account. You can set multiple by split in ,
owner                     : Owner's name or ID
platform                  : Bot's platform. See below
cid                       : Bot's default outfit ID
bid                       : Bot's default back bling ID
pickaxe_id                : Bot's default harvesting tool ID
eid                       : Bot's default emote ID
playlist                  : Bot's default playlist ID
banner                    : Bot's default banner ID
banner_color              : Bot's default banner color
avatar_id                 : Bot's default avatar ID
avatar_color              : Bot's default avatar color. See below
level                     : Bot's default level
tier                      : Bot's default tier
xpboost                   : Bot's default XP boost
friendxpboost             : Bot's default friend XP boost
status                    : Bot's default status
privacy                   : Bot's default privacy. See below
whisper                   : Whether bot will accept command from whisper. true or false
partychat                 : Whether bot will accept command from partychat. true or false
disablewhisperperfectly   : Config for if whisper is disabled, whether decline command from owner too
disablepartychatperfectly : Config for if partychat is disabled, whether decline command from owner too
joinemote                 : Whether bot re dance emote when someone joined to the party. true or false
ignorebot                 : Whether bot will ignore command from bots. true or false
joinmessage               : Message when someone joined to the party. \n to line break
randommessage             : Random message when someone joined to the party. \n to line break
joinmessageenable         : Whether bot will send message when someone joined to the party. true or false
randommessageenable       : Whether bot will send random message when someone joined to the party. true or false
outfitmimic               : Whether bot will mimic other player's outfit. true or false or user's name or ID
backpackmimic             : Whether bot will mimic other player's backpack. true or false or user's name or ID
pickaxemimic              : Whether bot will mimic other player's pickaxe. true or false or user's name or ID
emotemimic                : Whether bot will mimic other player's emote. true or false or user's name or ID
mimic-ignorebot           : Whether bot won't mimic bot. true or false
mimic-ignoreblacklist     : Whether bot won't mimic blacklisted user. true or false
acceptinvite              : Whether bot will accept invite. Invite from owner will accepted every time. true or false
acceptfriend              : Whether bot will accept friend request. true or false or null
addfriend                 : Whether bot will send friend request to party member. true or false
invite-ownerdecline       : Whether bot will decline invite when owner in the party. true or false
inviteinterval            : Whether bot will decline invite for interval seconds after accepted invite. true or false
interval                  : The number of seconds for decline invite after accepted invite
waitinterval              : The number of seconds for decline invite for wait command
hide-user                 : Whether bot will hide user joined to the party. true or false
hide-blacklist            : Whether bot will hide blacklisted user joined to the party. true or false
show-owner                : Whether bot will show owner when hide-user is true. true or false
show-whitelist            : Whether bot will show whitelisted user when hide-user is true. true or false
show-bot                  : Whether bot will show bot when hide-user is true. true or false
blacklist                 : List for blacklist users. name or ID
blacklist-declineinvite   : Whether bot will decline invite from blacklisted users. true or false
blacklist-autoblock       : Whether bot will block blacklisted users. true or false
blacklist-autokick        : Whether bot will kick blacklisted users from the party. true or false
blacklist-autochatban     : Whether bot will chatban blacklisted users. true or false
blacklist-ignorecommand   : Whether bot will ignore command from blacklisted users. true or false
whitelist                 : List of whitelist users. name or ID
whitelist-allowinvite     : Whether whitelisted users can invite bot any time. true or false
whitelist-declineinvite   : Whether bot will decline invite when whitelisted users in the party. true or false
whitelist-ignorelock      : Whether whitelisted users can ignore locks. true or false
whitelist-ownercommand    : Whether whitelisted users can use owner commands. true or false
whitelist-ignoreng        : Whether whitelisted users can ignore NG words. true or false
invitelist                : User list for inviteall command
otherbotlist              : Other bots which ignore in ignorebot

Discord
enabled                   : Whether will boot Discord Bot. true or false
token                     : Token for Discord Bot
owner                     : Owner's user ID
channelname               : Channel name used for bot's command channel. See below
status                    : Discord Bot's status
discord                   : Whether bot will accept command from Discord. true or false
disablediscordperfectly   : Config for if discord is disabled, whether decline command from owner too. true or false
blacklist                 : List of blacklist users. user ID
blacklist-ignorecommand   : Whether bot will ignore command from blacklisted users. true or false
whitelist                 : List of whitelist users. user ID
whitelist-ignorelock      : Whether whitelisted users can ignore locks. true or false
whitelist-ownercommand    : Whether whitelisted users can use owner commands. true or false
whitelist-ignoreng        : Whether whitelisted users can ignore NG words. true or false

Web
enabled                   : Whether will boot web server. true or false
ip                        : IP address for web server. See below
port                      : Port for web server
password                  : Password for web server
login_required            : Whether login required to access web server. true or false
web                       : Whether bot will accept command from web. true or false
log                       : Whether print web server access log

replies-matchmethod       : Match method for replies. See below
ng-words                  : Texts set as NG words
ng-word-matchmethod       : Match method for NG words
ng-word-kick              : Whether bot will kick user which said NG words
ng-word-chatban           : Whether bot will chatban user which said NG words
ng-word-blacklist         : Whether bot will add user which said NG words to blacklist
lang                      : Bot's lang
search-lang               : Item search lang
restart_in                : Time until restart bot
search_max                : Max amout of search
no-logs                   : Whether print logs in console. true or false
ingame-error              : Whether send errors to player. true or false
discord-log               : Whether send logs to Discord. true or false
hide-email                : Whether hide emails in Discord logs. true or false
hide-token                : Whether hide token in Discord logs. true or false
hide-webhook              : Whether hide webhook url in Discord logs. true or false
webhook                   : Discord's webhook url
caseinsensitive           : Whether make command not case insensitive true or false
loglevel                  : Log level. normal or info or debug
debug                     : Whether enable fortnitepy debug mode. true or false
```

# List of commands
All command can set multiple by split in ,  
Also enter item name to change item to it  

```
ownercommands                             : Set owner only commands
true                                      : String which use as true in command
false                                     : String which use as false in command
me                                        : String which use as message's sender in command
prev                                      : Repeat previous command
eval                                      : eval [expression] Evaluate content as expression, then return result
exec                                      : exec [statement] Evaluate content as statement, then return result
restart                                   : Restart program
relogin                                   : Relogin to account
reload                                    : Reload config.json and commands.json
addblacklist                              : addblacklist [user name/user ID] Add user to fortnite blacklist
removeblacklist                           : removeblacklist [user name/user ID] Remove user from fortnite blacklist
addwhitelist                              : addwhitelist [user name/user ID] Add user to fortnite whitelist
removewhitelist                           : removewhitelist [user name/user ID] Remove user from fortnite whitelist
addblacklist_discord                      : addblacklist_discord [user ID] Add user to Discord blacklist
removeblacklist_discord                   : removeblacklist_discord [user ID] Remove user from Discord blacklist
addwhitelist_discord                      : addwhitelist_discord [user ID] Add user to Discord whitelist
removewhitelist_discord                   : removewhitelist_discord [user ID] Remove user from Discord whitelsit
addinvitelist                             : addinvitelist [user name/user ID] Add user to invitelist
removeinvitelist                          : removeinvitelist [user name/user ID] Remove user from invitelist
get                                       : get [user name/user ID] Show info about party member
friendcount                               : Show friend count
pendingcount                              : Show friend request count(bidirection)
blockcount                                : Show block count
friendlist                                : Show friend list
pendinglist                               : Show friend request list
blocklist                                 : Show block list
outfitmimic                               : outfitmimic [true / false / user name/user ID] Whether bot will mimic other player's outfit
backpackmimic                             : backpackmimic [true / false / user name/user ID] Whether bot will mimic other player's backpack
pickaxemimic                              : pickaxemimic [true / false / user name/user ID] Whether bot will mimic other player's pickaxe
emotemimic                                : emotemimic [true / false / user name/user ID] Whether bot will mimic other player's emote
whisper                                   : whisper [true / false] Whether bot will accept command from whisper
partychat                                 : partychat [true / false] Whether bot will accept command from party chat
discord                                   : discord [true / false] Whether bot will accept command from Discord
web                                       : web [true / false] Whether bot will accept command from web
disablewhisperperfectly                   : whisperperfect [true / false] Config for if whisper is disabled, whether decline command from owner too
disablepartychatperfectly                 : partychatperfect [true / false] Config for if party chat is disabled, whether decline command from owner too
disablediscordperfectly                   : discordperfect [true / false] Config for if Discord is disabled, whether decline command from owner too
acceptinvite                              : acceptinvite [true / false] Whether bot will accept party invite
acceptfriend                              : acceptfriend [true / false] Whether bot will accept friend request
joinmessageenable                         : joinmessageenable [true / false] Whether bot will send message on someone joined to the party
randommessageenable                       : randommessageenable [true / false] Whether bot will send random message on someone joined to the party
wait                                      : Decline invite for config's waitinterval seconds
join                                      : join [user name/user ID] Join to user's party
joinid                                    : joinid [party ID] Join to party
leave                                     : Leave party
invite                                    : invite [user name / user ID] Invite user to the party
inviteall                                 : Invite config's invitelist users
message                                   : message [user name / user ID] : [Content] Send message to user
partymessage                              : partymessage [content] Send message to party chat
sendall                                   : sendall [content] Send same command to all bots
status                                    : status [content] Set status
banner                                    : banner [banner ID] [banner color] Set banner
avatar                                    : avatar [CID] [color(optional)] Set avatar
level                                     : level [level] Set level
bp                                        : bp [tier] [XP boost] [friend XP boost] Set battlepass info
privacy                                   : privacy [privacy_public / privacy_friends_allow_friends_of_friends / privacy_friends / privacy_private_allow_friends_of_friends / privacy_private] Set party's privacy
privacy_public                            : privacy_public which uses in privacy command
privacy_friends_allow_friends_of_friends  : privacy_friends_allow_friends_of_friends which uses in privacy command
privacy_friends                           : privacy_friends which uses in privacy command
privacy_private_allow_friends_of_friends  : privacy_private_allow_friends_of_friends which uses in privacy command
privacy_private                           : privacy_private which uses in privacy command
getuser                                   : getuser [user name / user ID] Show user's name and ID
getfriend                                 : getefriend [user name / user ID] Show user's name and ID
getpending                                : getpending [user name / user ID] Show user's name and ID
getblock                                  : getblock [user name / user ID] Show user's name and ID
info                                      : info [info_party / info_item / id / skin / bag / pickaxe / emote] Show party/item's info
info_party                                : info_party which uses in info command
pending                                   : pending [true / false] Accept all pending friend
removepending                             : Cancel all friend request which bot sent
addfriend                                 : addfriend [user name / user ID] Send friend request to user
removefriend                              : removefriend [user name / user ID] Remove user from friend
removeallfriend                           : Remove all friends
acceptpending                             : acceptpending [user name / user ID] Accept friend request from user
declinepending                            : declinepending [user name / user ID] Decline friend request from user
blockfriend                               : blockfriend[user name / user ID] Block user
unblockfriend                             : unblockfriend [user name / user ID] Unblock user
chatban                                   : chatban [user name / user ID] : [Reason(Optional)] Chatban user
promote                                   : promote [user name / user ID] Promote party leader to user
kick                                      : kick [user name / user ID] Kick user
hide                                      : hide [user name / user ID(optional)] Hide user
show                                      : show [user name / user ID(optional)] Show user
ready                                     : Set to Ready
unready                                   : Set to Not Ready
sitout                                    : Set to Sitting Out
match                                     : match [remaining(optional)] Set match state
unmatch                                   : Cancel match state
swap                                      : swap [user name / user ID] Swap position with user
outfitlock                                : outfitlock [true / false] Whether bot will change outfit
backpacklock                              : backpacklock [true / false] Whether bot will change backpack
pickaxelock                               : pickaxelock [true / false] Whether bot will change pickaxe
emotelock                                 : emotelock [true / false] Whether bot will change emote
stop                                      : Stop emote/all command
addeditems                                : Show all items which added in latest update
alloutfit                                 : Show all outfits
allbackpack                               : Show all backpacks
allpet                                    : Show all pets
allpickaxe                                : Show all pickaxes
allemote                                  : Show all emotes
cid                                       : cid [CID] Search item with CID and set to item which found
bid                                       : bid [BID] Search item with BID and set to item which found
petcarrier                                : petcarrier [Petcarrier] Search item with Petcarrier and set to item which found
pickaxe_id                                : pickaxe_id [Pickaxe_ID] Search item with Pickaxe_ID and set to item which found
eid                                       : eid [EID] Search item with EID and set to item which found
emoji_id                                  : emoji_id [emoji] Search item with Emoji and set to item which found
toy_id                                    : toy_id [toy] Search item with Toy and set to item which found
id                                        : id [ID] Search item with ID and set to item which found
outfit                                    : outfit [outfit name] Search item with outfit name and set to item which found
backpack                                  : backpack [backpack name] Search item with backpack name and set to item which found
pet                                       : pet [pet name] Search item with pet name and set to item which found
pickaxe                                   : pickaxe [pickaxe name] Search item with pickaxe name and set to item which found
emote                                     : emote [emote name] Search item with emote name and set to item which found
emoji                                     : emoji [emoji name] Search item with emoji name and set to item which found
toy                                       : toy [toy name] Search item with toy name and set to item which found
item                                      : item [item name] Search item with item name and set to item which found
set                                       : set [set name] Search item with set name
setvariant                                : setvariant [skin / bag / pickaxe] [variant] [number] [variant] [number] [variant] [number]... If count of variant and number does not match, it will ignore. Set style info. See below
addvariant                                : addvariant [skin / bag / pickaxe] [variant] [number] [variant] [number] [variant] [number]... If count of variant and number does not match, it will ignore. Add style info to current style info. See below
setstyle                                  : setstyle [skin / bag / pickaxe] Search style with item which bot has currently setting and set style to it
addstyle                                  : addstyle [skin / bag / pickaxe] Search style with item which bot has currently setting and add style to current style
setenlightenment                          : setenlightenment [number] [number] Set enlightenment info. See below
outfitasset                               : outfitasset [asset path] Set outfit with asset path
backpackasset                             : backpackasset [asset path] Set backpack with asset path
pickasset                                 : pickasset [asset path] Set pickaxe with asset path
emoteasset                                : emoteasset [asset path] Set emote with asset path
```

# replies
Set like this
"Trigger word": "Reply word"  
If you set multiple, add , like below  
```
{
    "hello": "Hello!",
    "goodbye": "Goodbye"
}
```

# Other
Avatar ID  
Usable variables  
```
{bot}                           : Bot's current outfit
```

Color  
Color name or three color codes  
```
TEAL
SWEET_RED
LIGHT_ORANGE
GREEN
LIGHT_BLUE
DARK_BLUE
PING
RED
GRAY
ORANGE
DARK_PURPLE
LIME
INDIGO
```
Example  
```
"avatar_color": "TEAL"
"avatar_color": "#ff0000,#00ff00,#0000ff"
```

Platform  
```
Windows     : WIN
Mac         : MAC
PlayStation : PSN
XBox        : XBL
Switch      : SWT
IOS         : IOS
Android     : AND
```

Privacy  
```
public                           : Public
friends_allow_friends_of_friends : Friend(Allow friends of friends)
friends                          : Friend
private_allow_friends_of_friends : Private(Allow friends of friends)
private                          : Private
```

Channel name  
Usable variables  
```
{name}                           : Bot's display name
{id}                             : Bot's ID
```
You can use these as command channel  
```
Test-Bot1-command-channel
Test-Bot2-command-channel
```
if setting is default  
```
{name}-command-channel
```
and bot's name is
```
Test Bot1
Test Bot2
```

IP
Usable variables  
```
{ip}                             : Default IP
```

Match method  
```
full     : Perfect matching
contains : Contains it
starts   : Stats with it
ends     : Ends with it
```

variant  
```
pattern/numeric/clothing_color/jersey_color/parts/progressive/particle/material/emissive
Usually material, progressive, parts are often used
For example, purple skull trooper is
clothing_color 1
jersey_color are used for soccer skins
```

enlightenment  
```
Fro example, 8ball vs Scratch's glitch info are enlightenment
Season(In chapter 2) / Number
```