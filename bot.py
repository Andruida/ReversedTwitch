

import irc.bot
import irc.strings
from irc.client import ip_numstr_to_quad, ip_quad_to_numstr
import traceback
import json

# import sqlalchemy as sql




class TestBot(irc.bot.SingleServerIRCBot):
	def __init__(self, config):
		irc.bot.SingleServerIRCBot.__init__(
			self, [(config["server"], config["port"], config["password"])], config["nickname"], config["nickname"])
		self.channel = config["channel"]
		self.prefix = config["prefix"]
		self.swears = config["swears"]
		# try:
			# self.sqlEngine = sql.create_engine("mysql+pymysql://"+config["dbuser"]+":"+config["dbpass"]+"@"+config["dbip"]+":3306/"+config["dbname"], pool_pre_ping=True)
			# self.sqlConn = self.sqlEngine.connect()
			# self.sqlMetadata = sql.MetaData(self.sqlEngine)
		# except:
			# traceback.print_exc()
			# print("sikertelen SQL csatlakozás")
			# exit()
		# self.streamTable = sql.Table("stream", self.sqlMetadata, 
					# sql.Column('id', sql.Integer, primary_key=True, nullable=False),
					# sql.Column('name', sql.String(128)),
					# sql.Column('desc', sql.String(1024)),
					# sql.Column('type', sql.Integer) # 0 
					# sql.Column('server', sql.String(128)),
					# sql.Column('passw', sql.String(128)),
					# sql.Column('concept_id', sql.Integer),
					# sql.Column('game', sql.String(256)), 
					# sql.Column('team', sql.String(16)), 
					# sql.Column('team2', sql.String(16)),
					# sql.Column('map', sql.String(16)),
					# sql.Column("started",sql.DateTime, server_default=sql.func.now()))
					# sql.Column("ended",sql.DateTime)
		
		# self.concepts = sql.Table("concepts", self.sqlMetadata, 
					# sql.Column('id', sql.Integer, primary_key=True, nullable=False), 
					# sql.Column('message_id', sql.String(32)), 
					# sql.Column('channel_id', sql.String(32)), 
					# sql.Column('guild_id', sql.String(32)), 
					# sql.Column('title', sql.String(1024)), 
					# sql.Column('desc', sql.String(2048)), 
					# sql.Column('author_id', sql.String(32)), 
					# sql.Column('votes', sql.Integer),
					# sql.Column('updated', sql.dialects.mysql.TINYINT(1), nullable=False, server_default="0"))
		
		#self.sqlMetadata.create_all()
		#self.sqlConn.execute(self.streamTable.insert().values(name="teszt", passw="rev123"))
		

	def on_nicknameinuse(self, c, e):
		c.nick(c.get_nickname() + "_")

	def on_welcome(self, c, e):
		c.join(self.channel)
		print("JOINED CHANNEL "+self.channel)

	def on_privmsg(self, c, e):
		pass
		#print("privmsg: "+str(e))
		#self.do_command(e, e.arguments[0])
	def on_notice(self, c, e):
		pass
		#print("notice: "+str(e))

	def on_pubmsg(self, c, e):
		#print("pubmsg: "+str(e))
		moderate = False
		#print(self.swears, e.arguments[0])
		for swear in self.swears:
			#print(swear in e.arguments[0], swear)
			if swear.lower() in e.arguments[0].lower():
				moderate = True
				break
		if moderate:
			c.privmsg(self.channel,"/timeout {0} 1".format(e.source[:e.source.find("!")]))
			#c.privmsg(self.channel,"OTT RÖPPENT A BAN DRÁGA @{} BARÁTOMNAK".format(e.source[:e.source.find("!")]))
			print(e.source[:e.source.find("!")]+" REPÜLT A BAN")
		elif e.arguments[0].startswith(self.prefix):
			self.do_command(c, e)
		#c.privmsg(self.channel,"Bot teszt!")
		
	def do_command(self, c, e):
		cmd = e.arguments[0][len(self.prefix):].split()
		#if cmd[0] == "stream":
			# r = self.sqlConn.execute(self.streamTable.select().order_by(self.streamTable.c.id.desc()).limit(1)).fetchone()
			# if r:
				# string = "Név: {3}, Map: {0}, Teams: {1}, Játszott koncepció: {2}".format(r.map, r.team, r.concept, r.name)
				# c.privmsg(self.channel, string)
			# else:
				# c.privmsg(self.channel,"PUBG Custom Game")
		if cmd[0].lower() == "jelszó" or cmd[0].lower() == "jelszo" or cmd[0].lower() == "info" or cmd[0].lower() == "infó":
			# r = self.sqlConn.execute(self.streamTable.select().order_by(self.streamTable.c.id.desc()).limit(1)).fetchone()
			# if r:
				# c.privmsg(self.channel,"- A custom game jelszava - {0}".format(r.passw))
			# else:
				# c.privmsg(self.channel,"- A custom game jelszava - {0}".format("Rev123"))
			c.privmsg(self.channel,"Szerver név - Reversed Custom, Szerver jelszó - rev123")
		elif cmd[0].lower() == "dc" or cmd[0].lower() == "discord":
			c.privmsg(self.channel, "Reversed PUBG Community Discord - https://discord.gg/mtxSt63 , Reversed Community Discord - https://discord.gg/v45uREX")
			
		else:
			pass
			#c.privmsg(self.channel,"Nincs ilyen parancs")
		



def main():
	# import sys
	# if len(sys.argv) != 5:
		# print("Usage: testbot <server[:port]> <channel> <nickname> <password>")
		# sys.exit(1)

	# s = sys.argv[1].split(":", 1)
	# server = s[0]
	# if len(s) == 2:
		# try:
			# port = int(s[1])
		# except ValueError:
			# print("Error: Erroneous port.")
			# sys.exit(1)
	# else:
		# port = 6667
	# channel = sys.argv[2]
	# nickname = sys.argv[3]
	# password = sys.argv[4]
	try:
		with open("config.json", encoding="utf-8") as f:
			config = json.loads(f.read())
			for k in ["server", "port", "password", "channel", "nickname", "prefix", "swears", "dbip", "dbname", "dbuser", "dbpass"]:
				a = config[k]
	except:
		print("VALAMI NEM JÓ A config.json FÁJLBAN:")
		traceback.print_exc()
		exit()

	bot = TestBot(config)
	bot.start()


if __name__ == "__main__":
	while True:
		try:
			main()
		except Exception as e:
			print(40*"=")
			print("HIBA:")
			traceback.print_exc()
			print(40*"=")
			
	
# bot.py irc.chat.twitch.tv #andruida69 andruida69 oauth:rd7b1idbka0qn5cxzpaquk2le92qc0