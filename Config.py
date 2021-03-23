import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("1737141128:AAGjU4R2S5CNY7C_i9UrEg5c2vswqK9f5H4", None)
    DATABASE_URL = os.environ.get("postgres://eyofrnogltxmwz:9f85e8584199a374615a67bfe18f73edc4afaf9451d16eed3aee5b179708589b@ec2-54-243-195-160.compute-1.amazonaws.com:5432/d325npis91qikn", None)
    APP_ID = os.environ.get("2443183", 1741321)
    API_HASH = os.environ.get("66b6799e1b784aff78bad680cd8362db", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("1575148105").split()))
    SUDO_USERS.append(1575148105)
    SUDO_USERS = list(set(1575148105))
  else:
    BOT_TOKEN = "1737141128:AAGjU4R2S5CNY7C_i9UrEg5c2vswqK9f5H4"
    DATABASE_URL = "postgres://eyofrnogltxmwz:9f85e8584199a374615a67bfe18f73edc4afaf9451d16eed3aee5b179708589b@ec2-54-243-195-160.compute-1.amazonaws.com:5432/d325npis91qikn"
    APP_ID = "2443183"
    API_HASH = "66b6799e1b784aff78bad680cd8362db"
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(1575148105)
    SUDO_USERS = list(set(1575148105))


class Messages():
      HELP_MSG = [
        ".",

        "**Force Subscribe**\n__Force group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.__",
        
        "**Setup**\n__First of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and I will leave the chat if i am not an admin in the chat.__",
        
        "**Commmands**\n__/ForceSubscribe - To get the current settings.\n/ForceSubscribe no/off/disable - To turn off ForceSubscribe.\n/ForceSubscribe {channel username} - To turn on and setup the channel.\n/ForceSubscribe clear - To unmute all members who muted by me.\n\nNote: /FSub is an alias of /ForceSubscribe__",
        
        "**Developed by @Souk26**\nTelegram Group: @Moviesbazz2\nOur Channel : @Moviesbazz"
      ]

      START_MSG = "**Hi, [{}](tg://user?id={})**\n__I can force members to join a specific channel before writing messages in the group.\nLearn more at /help__"
