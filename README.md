# ReversedTwitch

[ReversedHungary](https://www.twitch.tv/reversedhungary/) Twitch csatornáján üzemelő bot

## Parancsok

- `!info`, `!jelszo`, `!jelszó`
   
   Kiírja a meccs infókat

- `!dc`, `!discord`
   
   Kiírja a Discord invite linkeket a Reversed Discord szervereihez
   
## Beállítás

A bot a [python-irc](https://pypi.org/project/irc/) modulon alapul
```
pip install irc
```

A testreszabása a `config.json` fájlon keresztül történik.  
Példa:
```JSON
{
	"server" : "irc.chat.twitch.tv",
	"port" : 6667,
	"channel" : "#bot_name",
	"nickname" : "bot_name",
	"password" : "twitch_oauth_jelszo",
	"prefix" : "!",
	"swears" : ["káromkodások", "listája"],
	"dbip" : "localhost",
	"dbuser": "twitchbot",
	"dbname": "twitchbot",
	"dbpass": "mysqlpassword"
}
```
A `twitch_oauth_jelszo`-t a [Twitch saját generátorán](https://twitchapps.com/tmi/) keresztül tudod beszerezni
