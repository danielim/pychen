class chatFunc:
    def handshaker(self, usr, channel, ircsock, cmd):
        self.usr = usr
        self.channel = channel
        self.ircsock = ircsock
        # Split command into command(cmdlist[0]) and arguments(cmdlist[1])
        self.cmdlist = cmd.split(" ", 1)
        self.funcList = dir(chatFunc)
        if self.cmdlist[0] in self.funcList:
            print self.cmdlist[0]
            getattr(self, self.cmdlist[0])()
        else:
            self.ircsock.send("NOTICE "+ self.channel +" : No such command.\n") 

    def ping(self):
        self.ircsock.send("PONG :Pong\n")
    def commands(self):
        self.ircsock.send("PRIVMSG "+ self.channel +" :"+ str(self.funcList) +"\n")
    def say(self):
        msg = self.cmdlist[1]
        self.ircsock.send("PRIVMSG "+ self.channel +" :"+ msg +"\n")
    def hello(self):
        self.ircsock.send("PRIVMSG "+ self.channel +" :Hello!\n")
    def latesttldrwiki(self):
        import pyscrape
        import tldrwiki
        linkD = pyscrape.pyScrape()
        pyscrape.resizeImg(linkD['pImage'])
        txt = tldrwiki.outputOCR()
        tldrmsg = txt +"|Date:"+ linkD['pDate'] + "|Link:" + linkD['pImage']
        self.ircsock.send("PRIVMSG "+ self.channel +" :"+ tldrmsg + "\n")
    def random(self):
        import random
        randlist = self.cmdlist[1].split(" ")
        self.ircsock.send("PRIVMSG "+ self.channel +" :"+ random.choice(randlist) + "\n")
