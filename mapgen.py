#!/usr/bin/python3

from os import listdir
import hashlib


class MapLauncher:
    def __init__(self):
        self.path = '/home/ut4/LinuxServer/UnrealTournament/Content/Paks/'  # Your Maps Path Here, Add Mod Names Below
        self.mods = ["Mutator_AbsoluteHitSounds-WindowsNoEditor.pak", "Elimination_113-WindowsNoEditor.pak"]

        self.removeservers = ["UnrealTournament-LinuxServer.pak", "UnrealTournament-WindowsServer.pak"]
        self.gamelist = sorted(listdir(self.path))

    def removeserversfn(self):
        for i in self.removeservers:
            try:
                self.gamelist.remove(i)
            except ValueError:
                pass


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def main():
    ml = MapLauncher()
    ml.removeserversfn()
    protocol = "http"  # Make this https if your website uses ssl
    url = "ut.dasanfall.com/ut4/Paks/"  # Remember to end with /

    game = "game.txt"
    rules = "rules.txt"

    with open(game, "w") as file:
        for i in ml.gamelist:
            file.write(
                'RedirectReferences=(PackageName="{}",PackageURLProtocol="{}",PackageURL="{}",PackageChecksum="{}")\n'
                .format(i[:-4], protocol, url + i, md5(ml.path + i)))
            print("Adding {} redirect for {}".format(protocol, i))
        print("-----{} written-----".format(game))

    with open(rules, "w") as file:
        for r in ml.gamelist:
            if r not in ml.mods:
                file.write("CustomMapList={}\nRequiredPackages={}\n".format(r[:-20], r[:-20]))
                print("Adding map {}".format(r))
            else:
                file.write("RequiredPackages={}\n".format(r[:-20]))
                print("Adding mod {}".format(r))
        print("-----{} written-----".format(rules))

if __name__ == '__main__':
    main()
