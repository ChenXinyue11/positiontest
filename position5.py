

from random import randrange
import sys
import os
import shutil
import platform
import random
import time
import os, string, sys, subprocess
from random import randrange
from select import select
import re

def main():
    thlist = [3000,5000,7000,9000]
    movenumber = [6,7,8]
    moves = ["E5 e6 d6 d7 g6 f5 h4 h3","E6 d8 f7 e5 f5 f4 h4 h3","F5 f6 e6 d8 e7 e8 f8 f7","F5 e7 g6 f7 h7 f4 h4 h3","E7 f5 d6 d5 e5 f3 f4 g2",]
    
    
    for n in movenumber:
        for m in range(len(moves)):
            for th in thlist:
                mv = moves[m].split(" ")[:n]
                start = "b"
                f = open(str(th)+str(mv[-1])+".txt", "w")
                print(str(th)+str(n)+str(m)+str(mv[-1])+".txt")
                if th == 3000:
                    command2 = '/cshome/xinyue11/Desktop/new/benzene-vanilla-cmake/build/src/mohex/mohex'
                else:
                    command2 = '/cshome/xinyue11/Desktop/new' + str(th)+'/benzene-vanilla-cmake/build/src/mohex/mohex'
                print(command2)
                p2 = subprocess.Popen([command2],
                                            shell=True,
                                            stdin=subprocess.PIPE,
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE,universal_newlines=True,encoding='utf8',)
                p2.stdin.write(("boardsize 10" + "\n"))
                p2.stdin.flush()
                for move in mv:
                    print(("play "+start +" "+ move + "\n"))
                    p2.stdin.write(("play "+start +" "+ move + "\n"))
                    p2.stdin.flush()
                    if start == "b":
                        start = "w"
                    else:
                        start = "b"
                p2.stdin.write(("param_dfpn threads 4" + "\n"))
                p2.stdin.flush()
                p2.stdin.write(("dfpn-solve-state"+"\n"))
                (out,err) = p2.communicate()

                f.write(err+out)
                f.close()

main()