from requests import get,exceptions
from sys import exit

class main():
    def __init__(self):
        self.chats = {1:["channel_name1","channel_id1"],
         2:["user_name1","user_id1"]
        }

        self.bots = {1:['bot_name1',"bot_token1"],
        2:["bot_name2","bot_token2"],
        3:["bot_name3","bot_token3"]
        }
        
    def main_func(self,message,chat_id,TOKEN):
        url = """https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}""".format(TOKEN,chat_id,message)
        print(get(url).json())
    
    def start(self):
        try:
            chat_list={}
            for i in range(len([y for y in self.chats.keys()])):
                a,b=[y for y in self.chats.keys()],[x[0] for x in self.chats.values()]
                chat_list.update({a[i]:b[i]})
            chat_in=input(f"{chat_list}\nselect chat: ")
            if chat_in == "!exit":
                    exit('bey.')
            chat = self.chats[int(chat_in)]
        except:
            exit('!chat input!')
        del chat_list,chat_in,a,b
        try:
            bot_list={}
            for i in range(len([y for y in self.bots.keys()])):
                a,b=[y for y in self.bots.keys()],[x[0] for x in self.bots.values()]
                bot_list.update({a[i]:b[i]})
            bot_in=input(f"{bot_list}\nselect bot: ")
            if bot_in == "!exit":
                    exit('bey.')
            bot = self.bots[int(bot_in)]
        except:
            exit('!bot input!')
        del bot_list,bot_in,a,b
        return chat,bot

if __name__=="__main__":
    chat,bot = main().start()
    while True:
        txt = input(f"{chat[0],bot[0]}-msg: ")
        txt=txt.replace("\\n","%0A")
        if txt == "!exit":
            exit('bey.')
        else:
            try:
                main().main_func(txt,chat[1],bot[1])
            except exceptions.ConnectionError as err:
                exit(err)
            except:
                exit('!func!')
