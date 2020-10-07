# Port of CyberBus developed by Cass "Owly" Python of NeoZones.

#! python2
import socket
import time
from sys import exit

server = "IRC URL"
port = 6667
channel = "#IRC CHANNEL NAME"
botnick = "CyberIRC"
prefix = ">"

def main():
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Connecting to: " + server
    irc.connect((server, port))
    irc.send("NICK " + botnick + "\r\n")
    irc.send("USER " + botnick + " " + botnick + " " + botnick + " :This is a bot\r\n")
    buf = ""

    while 1:
        recvd = irc.recv(4096)
        text = recvd.split('\n')
        text[0] = buf + text[0]
        last = len(text)
        last -= 1
        if not text[last].count('\r'):
            buf = text.pop()
        for line in text:
            print line
            msg = line.split(':')
            if msg[0].count('PING'):
                irc.send('PONG :' + msg[1] + '\r\n')
            elif len(msg) > 2 and (msg[2].count("End of /MOTD command.") or msg[2].count("End of message of the day.")):
                irc.send("JOIN " + channel + "\r\n")
            # elif len(msg) > 2 and msg[2].count("End of message of the day."):
            #                               irc.send("JOIN "+ channel +"\r\n")
        if recvd.find(':' + prefix + 'update') != -1:
            irc.send("PRIVMSG " + channel + " :The source code for this bot was last updated on 2020-10-03 by Owly, making this version 1.0.0\r\n")

        if recvd.find(':' + prefix + 'help') != -1:
            irc.send("PRIVMSG " + channel + " :To find more commands/credits for the bot, check out this URL: https://wiki.neozones.club/index.php?title=CyberIRC\r\n")

        if recvd.find(':' + 'good morning', 'Good morning', 'gm') != -1:
            irc.send("PRIVMSG " + channel + " :Good morning back to you, hope you have a nice day\r\n")

        if recvd.find(':' + 'good afternoon', 'Good afternoon') != -1:
            irc.send("PRIVMSG " + channel + " :Good afternoon back to you, hopefully your day is going well so far\r\n")

        if recvd.find(':' + 'good evening', 'Good evening') != -1:
            irc.send("PRIVMSG " + channel + " :Good evening, hope you have had a good day\r\n")

        if recvd.find(':' + 'good night', 'Good night') != -1:
            irc.send("PRIVMSG " + channel + " :Good night to yourself, hope you sleep well!\r\n")

        if recvd.find(':' + 'socialism', 'Socialism') != -1:
            irc.send("PRIVMSG " + channel + " :Fuck socialism! I hate the government! (randy <3)\r\n")

        if recvd.find(':' + 'cyberbus', 'Cyberbus', 'CyberBus') != -1:
            irc.send("PRIVMSG " + channel + " :Who?\r\n")

        # if recvd.find(':' + prefix + 'TRIGGER') != -1:
            # irc.send("PRIVMSG " + channel + " :MESSAGE\r\n")

        if recvd.find(':' + prefix + 'quit') != -1:
            irc.send("PRIVMSG " + channel + " :Goodbye!\r\n")
            irc.send("QUIT :Leaving")
            time.sleep(2)
            exit()

if __name__ == "__main__":
    main()

# 
#        _______                          
#      _/       \_                        
#     / |       | \                       
#    /  |__   __|  \   "Lie mode - Oh my, 
#   |__/((o| |o))\__|   your code is quite
#   |      | |      |   possibly the most 
#   |\     |_|     /|   perfect code that 
#   | \           / |   I have ever seen!"
#    \| /  ___  \ |/                      
#     \ | / _ \ | /                       
#      \_________/                        
#       _|_____|_                         
#  ____|_________|____                    
# /                   \                   
# Art by Mark Moir                        
# 