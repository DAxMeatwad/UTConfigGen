#!/usr/bin/python3

gameini = r"C:\Users\terry\Desktop\LinuxServer\Rules.ini"


class MapInfo:
    def __init__(self):
        self.utgameruleset = ""
        self.uniquetag = ""
        self.title = ""
        self.tooltip = ""
        self.description = ""
        self.maxplayers = 0
        self.minplayerstostart = 0
        self.gamemode = ""
        self.gameoptions = ""
        self.categories = ""
        self.bteamgame = True
        self.mapprefixes = ""
        self.custommaplist = []
        self.requiredpackages = []


def getmapinfo():
    with open(gameini, "r") as f:
        for line in f:
            print(line.splitlines())


def main():
    getmapinfo()

if __name__ == '__main__':
    main()
