# Fortnite-LobbyBot
[![Versiones de Python](https://img.shields.io/badge/3.7%20%7C%203.8-blue)](https://www.python.org/downloads/)  
<a href="https://discord.gg/NEnka5N"><img src="https://discordapp.com/api/guilds/718709023427526697/widget.png?style=banner2"></img></a>  
Un bot de Fortnite que utiliza fortnitepy 
Puedes controlarlo mediante comandos 

# Instalación
# PC
https://github.com/gomashio1596/Fortnite-LobbyBot  
[Python 3.7](https://www.python.org/downloads "Descarga Python") o superior es requerido

Ejecuta INSTALL.bat  
Ejecuta RUN.bat  
Escribe los detalles en el sitio que fue abierto
Puedes aplicar los detalles refrescando la página  
# Repl.it
https://repl.it  
Haz click en: "sign up" encima de todo
Haz click en "+ new repl" arriba a la derecha, y abre "Import From GitHub"  
Copia:
https://github.com/gomashio1596/Fortnite-LobbyBot  
y pegalo en: "Paste any repository URL"  
Presiona "Import from GitHub"  
Presiona "run▶" en el sitio abierto (Llámemoslo repl page)  
Crea una cuenta en [Uptimerobot](https://uptimerobot.com "Uptimerobot") 
y presiona "Dashboard"  
Click en "\+ Monitor" y volvemos a repl.it, ahi buscamos la ventana "web" y copiamos la url  
Ve a uptimerobot, cambia el "Monitor Type" a "HTTP(s)" y pegamos la url  
Pon cualquier nombre en "Friendly Name" y presiona "Create Monitor"  
Pon los detalles en la página web del bot  
Puedes acceder a otras configuraciones recargando la página  

# Glitch
Glitch no es recomendado ya que no se puede hacer que esté 24/7!  

https://glitch.com
Inicie sesión con el botón de arriba a la derecha
https://glitch.com/~fortnite-lobbybot  
Haz click en el nombre del proyecto y seleccione "Remix Proyect"  
Haz click en el nombre del proyecto (tu proyecto remixeado) y activa "Make This Proyect Private"  
Haz click en "Show" y luego "In a new Window"  
Puedes aplicar los detalles refrescando el proyecto 

# configuración
```
Fortnite
email                     : Dirección de correo electrónico para el bot. Puedes poner varios dividiendolos con  ,
owner                     : Nombre del Owner o el ID
platform                  : Plataforma del Bot. Revise abajo para información
cid                       : ID de Outfit por defecto del bot
bid                       : ID de la Mochila por defecto del bot
pickaxe_id                : ID del pico por defecto del bot
eid                       : ID del emote por defecto del bot
playlist                  : ID de playlist por defecto del bot
banner                    : ID del banner por defecto del bot
banner_color              : Color del banner por defecto del bot
avatar_id                 : ID de Avatar por defecto del bot.　Revisa abajo
avatar_color              : Color del Avatar por defecto. Revisa abajo
level                     : Nivel por defecto del bot
tier                      : Tier por defecto del bot
xpboost                   : Potenciador de PE por defecto del bot
friendxpboost             : Potenciador de amigo por defecto del bot
status                    : Estado del bot por defecto
privacy                   : Privacidad del grupo por defecto del bot. Revise abajo para más información
whisper                   : Determina si el bot acepta comandos por susurro. true o false
partychat                 : Dtermina si el bot acepta comandos por chat de sala. true o false
disablewhisperperfectly   : Configuración por si el susurro ya está desactivado, para rechazar comandos de owner también
disablepartychatperfectly : Configuración por si el chat de sala ya está desactivado, para rechazar comandos de owner también
joinemote                 : Determina si el bot hará de neuvo el emote actual cuando alguien se una a la sala. true o false
ignorebot                 : Determina si el bot ignorará otros bots. true o false
joinmessage               : Mensaje enviado cuando alguien entra a la sala. \n para salto de linea
randommessage             : Mensaje al azar para cuando alguien entra a la sala. \n para salto de linea
joinmessageenable         : Determina si el bot enviará mensaje cuando alguien se una a la sala. true o false
randommessageenable       : Determina si el bot enviará mensaje al azar cuando alguien se una a la sala. true o false
outfitmimic               : Determina si el bot se cambiará a la skin a otra que un miembro se cambie. true o false o nombre de usuario o el ID
backpackmimic             : Determina si el bot cambiará a la mochila a otro que cambie un miembro. true o false o nombre de usuario o el ID
pickaxemimic              : Determina si el bot cambiará el pico a otro que cambie un miembro. true o false o nombre de usuario o el ID
emotemimic                : Determina si el bot imitará el emote de otro jugador. true o false o nombre de usuario o el ID
mimic-ignorebot           : Determina si el bot no imitará otros bots. true o false
mimic-ignoreblacklist     : Determina si el bot imitará miembros de la lista negra. true o false
acceptinvite              : Determina si el bot acepta invitaciones de grupo. Invitaciones del owner serán aceptadas siempre. true o false
acceptfriend              : Determina si el bot aceptará peticiones de amistad. true, false o null
addfriend                 : Determina si el bot enviará petición de amistad a todos los miembros de la sala. true o false
invite-ownerdecline       : Determina si el bot rechazará invitaciones de grupo cuando haya un owner en la sala. true o false
inviteinterval            : Determina si el bot rechazará la invitación por intervalos de segundos después de aceptar alguna invitación. true o false
interval                  : El número de segundos para rechazar invitaciones
waitinterval              : El número de segundo para rechazar invitaciones cuando se usa el comando wait
hide-user                 : Determina si el bot esconderá a los usuarios que se unan. true o false
hide-blacklist            : Determina si el bot esconderá usuarios de la lista negra. true o false
show-owner                : Determina si el bot mostrará al owner cuando ocultar a todos esté activado. true o false
show-whitelist            : Determina si el bot mostrará a los miembros de la whitelist cuando ocultar a todos esté activado. true o false
show-bot                  : Determina si el bot mostrará bots cuando ocultar a todos esté activado. true o false
blacklist                 : Miembros de la Lista negra. nombre o ID
blacklist-declineinvite   : Determina si el bot rechazará invitaciones de amigos en la lista negra. true o false
blacklist-autoblock       : Determina si el bot bloqueará automáticamente los miembros de la Lista Negra. true o false
blacklist-autokick        : Determina si el bot expulsará a miembros de la lista negra. true o false
blacklist-autochatban     : Determina si el bot baneará del chat a miembros de la lista negra. true o false
blacklist-ignorecommand   : Determina si el bot ignorará comandos de miembros de la lista negra. true o false
whitelist                 : Miembros de la Lista blanca. nombre o ID
whitelist-allowinvite     : Determina si el bot aceptará invitaciones de miembros de la lista blanca siempre. true o false
whitelist-declineinvite   : Determina si el bot rechazará invitaciones cuando haya un miembro de la lista blanca en la sala. true o false
whitelist-ignorelock      : Determina si los miembros de la lista blanca pueden cambiar la skin bloqueada. true o false
whitelist-ownercommand    : Determina si los miembros de la lista blanca pueden usar comandos de owner. true o false
whitelist-ignoreng        : Determina si los miembros de la whitelist pueden usar las palabras NG. true o false
invitelist                : Lista de usuarios para invitar al usar el comando inviteall
otherbotlist              : Otros bots que se ignorarán si ignorebot está acivado

Discord
enabled                   : Determina si se inicia el bot de Discord. true o false
token                     : Token para el bot de Discord
owner                     : ID del owner en Discord
channelname               : Nombre del canal para aceptar comandos. Revise abajo para más información
status                    : Estado del bot de Discord
discord                   : Determina si el bot aceptará comandos en Discord. true o false
disablediscordperfectly   : Configuración por si discord está desactivado, si rechazará comandos de owner también. true o false
blacklist                 : Miembros de la Lista negra. ID de usuario
blacklist-ignorecommand   : Determina si el bot ignora comandos de miembros en la lista negra. true o false
whitelist                 : Miembros en la Lista Blanca. ID de usuario
whitelist-ignorelock      : Determina si la lista blanca puede ignorar bloqueos de cosméticos. true o false
whitelist-ownercommand    : Determina si los miembros de la lista blanca pueden usar comandos de owner. true o false
whitelist-ignoreng        : Determina si los miembros de la lista blanca pueden usar las palabras NG. true o false

Web
enabled                   : Determina si se encenderá el servidor web. true o false
ip                        : IP address for web server. Revise abajo para más información
port                      : Puerto para el servidor web
password                  : Contraseña para el servidor web
login_required            : Determina si es necesario iniciar sesión en web. true o false
web                       : Determina si el bot aceptará comandos del servidor web. true o false
log                       : Determina si se crearán logs del servidor web

replies-matchmethod       : Método de detección de las respuestas. Revisa abajo
ng-words                  : Palabras que son NG
ng-word-matchmethod       : Método de detección de las palabras NG
ng-word-kick              : Determina si el bot expulsará a quien use palabras NG
ng-word-chatban           : Determina si el bot baneará del chat a quien use palabras NG
ng-word-blacklist         : Determina si el bot añadirá a la lista negra los que usen palabras NG
lang                      : Lenguaje del bot
no-logs                   : Determina si se escribirán logs en la consola. true o false
ingame-error              : Determina si el usuario puede recibir los errores. true o false
discord-log               : Determina si se van a enviar los logs a discord. true o false
restart_in                : Tiempo hasta reiniciar
search_max                : Cantidad máxima de búsqueda
hide-email                : Determina si se oculta el email en logs de Discord. true o false
hide-token                : Determina si se oculta el token en los logs de Discord. true o false
hide-webhook              : Determina si se oculta la URL del webhook en logs de Discord. true o false
webhook                   : URL del Webhook de discord
caseinsensitive           : Determina si make command not case insensitive true o false
loglevel                  : Nivel de Logs. normal, info o debug
debug                     : Determina si se activa el debug de fortnitepy. true o false
```

# Lista de Comandos
Todos los comandos se pueden dividir con ,  
También puedes cambiar a otro item solo con escribir su nombre  

```
ownercommands                             : Configura comnaods de owner
true                                      : Variable que actua de verdadero
false                                     : Variable que actua de falso
me                                        : Función que se reconoce como el que envía el mensaje
prev                                      : Repite el anterior comando
eval                                      : eval [expression] Evalúa el contenido como expresión, devuelve el resultado
exec                                      : exec [statement] Evalúa el contenido como declaración, devuelve el resultado
restart                                   : Reinicia el programa
relogin                                   : Vuelve a iniciar sesión en la cuenta
reload                                    : Recarga config.json y commands.json
addblacklist                              : addblacklist [nombre de usuario/ID de usuario] Añade un usuario a la lista negra
removeblacklist                           : removeblacklist [nombre de usuario/ID de usuario] Quita un usuario de la lista negra
addwhitelist                              : addwhitelist [nombre de usuario/ID de usuario] Aañade un usuario a la lista blanca
removewhitelist                           : removewhitelist [nombre de usuario/ID de usuario] Quita un usuario de la lista blanca
addblacklist_discord                      : addblacklist_discord [user ID] Añade un usuario de discord a la lista negra
removeblacklist_discord                   : removeblacklist_discord [user ID] Quita un usuario de discord de la lista negra
addwhitelist_discord                      : addwhitelist_discord [user ID] Añade un usuario a la lista blanca de discord
removewhitelist_discord                   : removewhitelist_discord [user ID] Quita un usuario de la lista blanca de discord
addinvitelist                             : addinvitelist [nombre de usuario/ID de usuario] Añade un usuario a la lista de invitación
removeinvitelist                          : removeinvitelist [nombre de usuario/ID de usuario] Quita un usuario de la lista de invitación
get                                       : get [nombre de usuario/ID de usuario] Muestra información sobre el usuario
friendcount                               : Muestra el número de amigos
pendingcount                              : Muestra el número de solicitudes pendientes (bidireccional)
blockcount                                : Muestra el número de bloqueados
friendlist                                : Muestra la lista de amigos
pendinglist                               : Muestra la lista de solicitudes pendientes
blocklist                                 : Muestra la lista de bloqueados
outfitmimic                               : outfitmimic [true / false] Determina si el bot imitará el cambio de skin de otro
backpackmimic                             : backpackmimic [true / false] Determina si el bot imitará el cambio de mochila de otro
pickaxemimic                              : pickaxemimic [true / false] Determina si el bot imitará el cambio de pico de otro
emotemimic                                : emotemimic [true / false] Determina si el bot imitará el emote realizado por otro
whisper                                   : whisper [true / false] Determina si se aceptan comandos por susurro
partychat                                 : partychat [true / false] Determina si se aceptan comandos de sala
discord                                   : discord [true / false] Determina si el bot aceptará comandos de Discord
web                                       : web [true / false] Determina si el bot aceptará comandos de Web
disablewhisperperfectly                   : whisperperfect [true / false] Determina si el bot ignorará comandos de owner en susurro, en caso de estar desactivado
disablepartychatperfectly                 : partychatperfect [true / false] Determina si el bot ignorará comandos de owner en sala, en caso de estar desactivado
disablediscordperfectly                   : discordperfect [true / false] Determina si el bot ignorará comandos de owner en discord, en caso de estar desactivado
acceptinvite                              : acceptinvite [true / false] Determina si el bot aceptará invitaciones de grupo
acceptfriend                              : acceptfriend [true / false] Determina si el bot aceptará peticiones de amistad
joinmessageenable                         : joinmessageenable [true / false] Activa o desactiva el mensaje al unirse alguien
randommessageenable                       : randommessageenable [true / false] Activa o desactiva el mensaje al azar al unirse alguien
wait                                      : Rechaza invitaciones por el número de segundos establecido
join                                      : join [nombre de usuario/ID de usuario] Comando para unir el bot a una sala
joinid                                    : joinid [party ID] Comando para unir el bot a una sala por ID
leave                                     : Abandona el grupo actual
invite                                    : invite [user name / user ID] Invita un usuario a la sala
inviteall                                 : Invita toda la lista de miembros en la invitelist
message                                   : message [user name / user ID] : [Contenido] Envía un mensaje a un usuario
partymessage                              : partymessage [contenido] Envía un mensaje a chat de la sala
sendall                                   : sendall [contenido] Envía el mismo mensaje a todos los bots
status                                    : status [contenido] Configura el estado
banner                                    : banner [banner ID] [banner color] Configura el banner
avatar                                    : avatar [CID] [color(optional)] Cambia el avatar
level                                     : level [level] Configura el nivel
bp                                        : bp [tier] [XP boost] [friend XP boost] Configura la información del pase de batalla
privacy                                   : privacy [privacy_public / privacy_friends_allow_friends_of_friends / privacy_friends / privacy_private_allow_friends_of_friends / privacy_private] Configura la privacidad del grupo
privacy_public                            : privacy_public Se usa con el comando privacy
privacy_friends_allow_friends_of_friends  : privacy_friends_allow_friends_of_friends Se usa con el comando privacy
privacy_friends                           : privacy_friends Se usa el con el comando privacy
privacy_private_allow_friends_of_friends  : privacy_private_allow_friends_of_friends Se usa con el comando privacy
privacy_private                           : privacy_private Se usa con el comando privacy
getuser                                   : getuser [user name / user ID] Muestra el nombre del usuario y el ID
getfriend                                 : getefriend [user name / user ID] Muestra el nombre del usuario y el ID
getpending                                : getpending [user name / user ID] Muestra el nombre del usuario y el ID
getblock                                  : getblock [user name / user ID] Muestra el nombre del usuario y el ID
info                                      : info [info_party / info_item / id / skin / bag / pickaxe / emote] Muestra información de la sala/items
info_party                                : info_party Se usa con el comando info
pending                                   : pending [true / false] Acepta las peticiones pendientes
removepending                             : Cancela todas las solicitudes enviadas por los bots
addfriend                                 : addfriend [user name / user ID] Envía una solicitud de amistad al usuario
removefriend                              : removefriend [user name / user ID] Quita un usuario de amigos
removeallfriend                           : Elimina a todos los amigos
acceptpending                             : acceptpending [user name / user ID] Acepta la solicitud pendiente de un usuario
declinepending                            : declinepending [user name / user ID] Rechaza la solicitud pendiente de un usuario
blockfriend                               : blockfriend[user name / user ID] Bloquea un usuario
unblockfriend                             : unblockfriend [user name / user ID] Desbloquea un usuario
chatban                                   : chatban [user name / user ID] : [Razón(Opcional)] Banea del chat a un usuario
promote                                   : promote [user name / user ID] Da líder al usuario
kick                                      : kick [user name / user ID] Expulsa un usuario
hide                                      : hide [user name / user ID(optional)] Esconde un miembro
show                                      : show [user name / user ID(optional)] Muestra un miembro
ready                                     : El bot se pone Listo
unready                                   : El bot se pone No Listo
sitout                                    : El bot se pone en No Participando...
match                                     : match [restantes(opcional)] Configura el estado de la partida
unmatch                                   : Cancela el estado en partida
swap                                      : swap [user name / user ID] Cambia posicion con un usuario
outfitlock                                : outfitlock [true / false] Determina si el bot bloquea el cambio de skin 
backpacklock                              : backpacklock [true / false] Determina si el bot bloquea el cambio de mochila
pickaxelock                               : pickaxelock [true / false] Determina si el bot bloquea el cambio de pico
emotelock                                 : emotelock [true / false] Determina si el bot bloquea el cambio de emote
stop                                      : Detiene el emote/todo el comando
addeditems                                : Muestra todos los items agregados en la última actualización
alloutfit                                 : Muestra todas las skins
allbackpack                               : Muestra todas las mochilas
allpet                                    : Muestra todas las mascotas
allpickaxe                                : Muestra todos los picos
allemote                                  : Muestra todos los emotes
cid                                       : cid [CID] Busca un item con CID y cambia al item encontrado
bid                                       : bid [BID] Busca un item con BID y cambia al item encontrado
petcarrier                                : petcarrier [Petcarrier] Busca un item con Petcarrier y se cambia al item encontrado
pickaxe_id                                : pickaxe_id [Pickaxe_ID] Busca un pico con Pickaxe_ID y se cambia al item encontrado
eid                                       : eid [EID] Busca un emote con EID y se cambia al item encontrado
emoji_id                                  : emoji_id [emoji] Busca un item con emoji y se cambia al item encontrado
toy_id                                    : toy_id [toy] Busca un ítem con toy y se cambia al item encontrado
id                                        : id [ID] Busca un item con ID y se cambia al item encontrado
outfit                                    : outfit [outfit name] Busca una skin por nombre y se cambia a la skin encontrada
backpack                                  : backpack [backpack name] Busca una mochila por nombre y se cambia a la mochila encontrada
pet                                       : pet [pet name] Busca una mascota por nombre
pickaxe                                   : pickaxe [pickaxe name] Busca un pico por nombre y se cambia al pico encontrado
emote                                     : emote [emote name] Busca un emote por nombre y se cambia al emote encontrado
emoji                                     : emoji [emoji name] Busca un emoji por nombre y se cambia al emoji seleccionado
toy                                       : toy [toy name] Busca un juguete por nombre y se cambia al juguete encontrado
item                                      : item [item name] Busca un item por nombre y se cambia al item encontrado
set                                       : set [set name] Busca items por nombre del Set
setvariant                                : setvariant [skin / bag / pickaxe] [variant] [number] [variant] [number] [variant] [number]... Si el numero de variantes no coincide se ignorará. Establece información del estilo. Revise abajo para más información
addvariant                                : addvariant [skin / bag / pickaxe] [variant] [number] [variant] [number] [variant] [number]... Si el número de variantes no coincide se ignorará. Añade información al estilo. Revise abajo para más información
setstyle                                  : setstyle [skin / bag / pickaxe] Busca un estilo al item que tenga puesto el bot y cambia al estilo encontrado si lo hay
addstyle                                  : addstyle [skin / bag / pickaxe] Busca un estilo al item que tenga puesto el bot y añade información al estilo
setenlightenment                          : setenlightenment [number] [number] Determina la información de iluminación. Revise abajo para más información
outfitasset                               : outfitasset [path asset] Cambia skin con Characters Number
backpackasset                             : backpackasset [path asset] Cambia mochila con characters number
pickasset                                 : pickasset [path asset] Cambia el pico con characters number
emoteasset                                : emoteasset [path asset] Cambia el emote con characters number
```

# respuestas / replies
Configuralo como esto:
"Palabra de activación": "Respuesta"  
Puedes poner varios, como por ejemplo:  
```
{
    "hola": "Hola!",
    "hasta luego": "Hasta Luego!"
}
```

# Otros
ID de Avatar  
Variables disponibles
```
{bot}                           : Outfit actual del bot
```

Color  
Nombre de color o códigos de color  
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
Ejemplo: 
```
"avatar_color": "TEAL"
"avatar_color": "#ff0000,#00ff00,#0000ff"
```

Plataforma 
```
Windows     : WIN
Mac         : MAC
PlayStation : PSN
Xbox        : XBL
Switch      : SWT
IOS         : IOS
Android     : AND
```

Privacidad
```
public                           : Público
friends_allow_friends_of_friends : Amigos(Permite amigos de amigos)
friends                          : Amigos
private_allow_friends_of_friends : Privado(Permite amigos de amigos)
private                          : Privado
```

Nombre del canal
Variables para usar 
```
{name}                           : Nombre del bot
{id}                             : ID del bot
```
Puedes usar esto como canal de comandos  
```
Test-Bot1-command-channel
Test-Bot2-command-channel
```
si las configuraciones están por defecto 
```
{name}-command-channel
```
y el nombre del bot es:
```
Test Bot1
Test Bot2
```

IP
Variables utilizables
```
{ip}                             : Puede ser la IP local asignada a su PC en caso de estar en Windows.
```

Métodos de detección
```
full     : Detección perfecta
contains : Lo contiene
starts   : Empieza
ends     : Termina
```

variant / variantes
```
pattern/numeric/clothing_color/jersey_color/parts/progressive/particle/material/emissive
Usualmente material, progressive, parts son los más usados
Por ejemplo, Skull Trooper con variante morada es:
clothing_color 1
jersey_color es usado para las skins de fútbol
```

enlightenment / iluminación 
```
Por ejemplo, Bola 8 vs Bola blanca glitcheada la información es la iluminación
Season(En el capítulo 2) / Número
```