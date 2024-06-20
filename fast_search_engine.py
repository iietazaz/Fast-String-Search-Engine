class node:
    def __init__(self,letter):
        self.letter = letter
        self.a = None
        self.b = None
        self.c = None
        self.d = None
        self.e = None
        self.f = None
        self.g = None
        self.h = None
        self.i = None
        self.j = None
        self.k = None
        self.l = None
        self.m = None
        self.n = None
        self.o = None
        self.p = None
        self.q = None
        self.r = None
        self.s = None
        self.t = None
        self.u = None
        self.v = None
        self.w = None
        self.x = None
        self.y = None
        self.z = None

class alphabet:
    def __init__(self):
        self.root = node("Project")

    def insert(self,alphabet):
        checking = self.search(alphabet)
        if checking == True:
            print("Already available in dictionary!")
            return ""
        add = self.root
        for i in range(len(alphabet)):
            while True:
                if alphabet[i] == "a":
                    if add.a == None:
                        if i == len(alphabet)-1:
                            add.a = node("A")
                            add = add.a
                            break
                        else:
                            add.a = node(alphabet[i])
                            add = add.a
                            break
                    else:
                        add = add.a
                        break
                elif alphabet[i] == "b":
                    if add.b == None:
                        if i == len(alphabet)-1:
                            add.b = node("B")
                            add = add.b
                            break
                        else:
                            add.b = node(alphabet[i])
                            add = add.b
                            break
                    else:
                        add = add.b
                        break
                elif alphabet[i] == "c":
                    if add.c == None:
                        if i == len(alphabet)-1:
                            add.c = node("C")
                            add = add.c
                            break
                        else:
                            add.c = node(alphabet[i])
                            add = add.c
                            break
                    else:
                        add = add.c
                        break
                elif alphabet[i] == "d":
                    if add.d == None:
                        if i == len(alphabet)-1:
                            add.d = node("D")
                            add = add.d
                            break
                        else:
                            add.d = node(alphabet[i])
                            add = add.d
                            break
                    else:
                        add = add.d
                        break
                elif alphabet[i] == "e":
                    if add.e == None:
                        if i == len(alphabet)-1:
                            add.e = node("E")
                            add = add.e
                            break
                        else:
                            add.e = node(alphabet[i])
                            add = add.e
                            break
                    else:
                        add = add.e
                        break
                elif alphabet[i] == "f":
                    if add.f == None:
                        if i == len(alphabet)-1:
                            add.f = node("F")
                            add = add.f
                            break
                        else:
                            add.f = node(alphabet[i])
                            add = add.f
                            break
                    else:
                        add = add.f
                        break
                elif alphabet[i] == "g":
                    if add.g == None:
                        if i == len(alphabet)-1:
                            add.g = node("G")
                            add = add.g
                            break
                        else:
                            add.g = node(alphabet[i])
                            add = add.g
                            break
                    else:
                        add = add.g
                        break
                elif alphabet[i] == "h":
                    if add.h == None:
                        if i == len(alphabet)-1:
                            add.h = node("H")
                            add = add.h
                            break
                        else:
                            add.h = node(alphabet[i])
                            add = add.h
                            break
                    else:
                        add = add.h
                        break
                elif alphabet[i] == "i":
                    if add.i == None:
                        if i == len(alphabet)-1:
                            add.i = node("I")
                            add = add.i
                            break
                        else:
                            add.i = node(alphabet[i])
                            add = add.i
                            break
                    else:
                        add = add.i
                        break
                elif alphabet[i] == "j":
                    if add.j == None:
                        if i == len(alphabet)-1:
                            add.j = node("J")
                            add = add.j
                            break
                        else:
                            add.j = node(alphabet[i])
                            add = add.j
                            break
                    else:
                        add = add.j
                        break
                elif alphabet[i] == "k":
                    if add.k == None:
                        if i == len(alphabet)-1:
                            add.k = node("K")
                            add = add.k
                            break
                        else:
                            add.k = node(alphabet[i])
                            add = add.k
                            break
                    else:
                        add = add.k
                        break
                elif alphabet[i] == "l":
                    if add.l == None:
                        if i == len(alphabet)-1:
                            add.l = node("L")
                            add = add.l
                            break
                        else:
                            add.l = node(alphabet[i])
                            add = add.l
                            break
                    else:
                        add = add.l
                        break
                elif alphabet[i] == "m":
                    if add.m == None:
                        if i == len(alphabet)-1:
                            add.m = node("M")
                            add = add.m
                            break
                        else:
                            add.m = node(alphabet[i])
                            add = add.m
                            break
                    else:
                        add = add.m
                elif alphabet[i] == "n":
                    if add.n == None:
                        if i == len(alphabet)-1:
                            add.n = node("N")
                            add = add.n
                            break
                        else:
                            add.n = node(alphabet[i])
                            add = add.n
                            break
                    else:
                        add = add.n
                        break
                elif alphabet[i] == "o":
                    if add.o == None:
                        if i == len(alphabet)-1:
                            add.o = node("O")
                            add = add.o
                            break
                        else:
                            add.o = node(alphabet[i])
                            add = add.o
                            break
                    else:
                        add = add.o
                        break
                elif alphabet[i] == "p":
                    if add.p == None:
                        if i == len(alphabet)-1:
                            add.p = node("P")
                            add = add.p
                            break
                        else:
                            add.p = node(alphabet[i])
                            add = add.p
                            break
                    else:
                        add = add.p
                        break
                elif alphabet[i] == "q":
                    if add.q == None:
                        if i == len(alphabet)-1:
                            add.q = node("Q")
                            add = add.q
                            break
                        else:
                            add.q = node(alphabet[i])
                            add = add.q
                            break
                    else:
                        add = add.q
                        break
                elif alphabet[i] == "r":
                    if add.r == None:
                        if i == len(alphabet) - 1:
                            add.r = node("R")
                            add = add.r
                            break
                        else:
                            add.r = node(alphabet[i])
                            add = add.r
                            break
                    else:
                        add = add.r
                        break
                elif alphabet[i] == "s":
                    if add.s == None:
                        if i == len(alphabet)-1:
                            add.s = node("S")
                            add = add.s
                            break
                        else:
                            add.s = node(alphabet[i])
                            add = add.s
                            break
                    else:
                        add = add.s
                elif alphabet[i] == "t":
                    if add.t == None:
                        if i == len(alphabet)-1:
                            add.t = node("T")
                            add = add.t
                            break
                        else:
                            add.t = node(alphabet[i])
                            add = add.t
                            break
                    else:
                        add = add.t
                        break
                elif alphabet[i] == "u":
                    if add.u == None:
                        if i == len(alphabet)-1:
                            add.u = node("U")
                            add = add.u
                            break
                        else:
                            add.u = node(alphabet[i])
                            add = add.u
                            break
                    else:
                        add = add.u
                        break
                elif alphabet[i] == "v":
                    if add.v == None:
                        if i == len(alphabet)-1:
                            add.v = node("V")
                            add = add.v
                            break
                        else:
                            add.v = node(alphabet[i])
                            add = add.v
                            break
                    else:
                        add = add.v
                        break
                elif alphabet[i] == "w":
                    if add.w == None:
                        if i == len(alphabet)-1:
                            add.w = node("W")
                            add = add.w
                            break
                        else:
                            add.w = node(alphabet[i])
                            add = add.w
                            break
                    else:
                        add = add.w
                        break
                elif alphabet[i] == "x":
                    if add.x == None:
                        if i == len(alphabet)-1:
                            add.x = node("X")
                            add = add.x
                            break
                        else:
                            add.x = node(alphabet[i])
                            add = add.x
                            break
                    else:
                        add = add.x
                        break
                elif alphabet[i] == "y":
                    if add.y == None:
                        if i == len(alphabet)-1:
                            add.y = node("Y")
                            add = add.y
                            break
                        else:
                            add.y = node(alphabet[i])
                            add = add.y
                            break
                    else:
                        add = add.y
                        break
                elif alphabet[i] == "z":
                    if add.z == None:
                        if i == len(alphabet)-1:
                            add.z = node("Z")
                            add = add.z
                            break
                        else:
                            add.z = node(alphabet[i])
                            add = add.z
                            break
                    else:
                        add = add.z
                        break

    def search(self,word):
        x = self.root
        for i in range(len(word)):
            while True:
                if word[i] == "a":
                    if x.a != None:
                        if i == len(word)-1:
                            if x.a.letter == "A":
                                return True
                            else:
                                return False
                        else:
                            x = x.a
                            break
                    else:
                        return False
                if word[i] == "b":
                    if x.b != None:
                        if i == len(word) - 1:
                            if x.b.letter == "B":
                                return True
                            else:
                                return False
                        else:
                            x = x.b
                            break
                    else:
                        return False
                if word[i] == "c":
                    if x.c != None:
                        if i == len(word) - 1:
                            if x.c.letter == "C":
                                return True
                            else:
                                return False
                        else:
                            x = x.c
                            break
                    else:
                        return False
                if word[i] == "d":
                    if x.d != None:
                        if i == len(word) - 1:
                            if x.d.letter == "D":
                                return True
                            else:
                                return False
                        else:
                            x = x.d
                            break
                    else:
                        return False
                if word[i] == "e":
                    if x.e != None:
                        if i == len(word) - 1:
                            if x.e.letter == "E":
                                return True
                            else:
                                return False
                        else:
                            x = x.e
                            break
                    else:
                        return False
                if word[i] == "f":
                    if x.f != None:
                        if i == len(word) - 1:
                            if x.f.letter == "F":
                                return True
                            else:
                                return False
                        else:
                            x = x.f
                            break
                    else:
                        return False
                if word[i] == "g":
                    if x.g != None:
                        if i == len(word) - 1:
                            if x.g.letter == "G":
                                return True
                            else:
                                return False
                        else:
                            x = x.g
                            break
                    else:
                        return False
                if word[i] == "h":
                    if x.h != None:
                        if i == len(word) - 1:
                            if x.h.letter == "H":
                                return True
                            else:
                                return False
                        else:
                            x = x.h
                            break
                    else:
                        return False
                if word[i] == "i":
                    if x.i != None:
                        if i == len(word)-1:
                            if x.i == "I":
                                break
                            else:
                                return False
                        else:
                            x = x.i
                            break
                    else:
                        return False
                if word[i] == "j":
                    if x.j != None:
                        if i == len(word) - 1:
                            if x.j.letter == "J":
                                return True
                            else:
                                return False
                        else:
                            x = x.j
                            break
                    else:
                        return False
                if word[i] == "k":
                    if x.k != None:
                        if i == len(word) - 1:
                            if x.k.letter == "K":
                                return True
                            else:
                                return False
                        else:
                            x = x.k
                            break
                    else:
                        return False
                if word[i] == "l":
                    if x.l != None:
                        if i == len(word)-1:
                            if x.l == "L":
                                break
                            else:
                                return False
                        else:
                            x = x.l
                            break
                    else:
                        return False
                if word[i] == "m":
                    if x.m != None:
                        if i == len(word)-1:
                            if x.m.letter == "M":
                                return True
                            else:
                                return False
                        else:
                            x = x.m
                            break
                    else:
                        return False
                if word[i] == "n":
                    if x.n != None:
                        if i == len(word) - 1:
                            if x.n == "N":
                                break
                            else:
                                return False
                        else:
                            x = x.n
                            break
                    else:
                        return False
                if word[i] == "o":
                    if x.o != None:
                        if i == len(word) - 1:
                            if x.o.letter == "O":
                                return True
                            else:
                                return False
                        else:
                            x = x.o
                            break
                    else:
                        return False
                if word[i] == "p":
                    if x.p != None:
                        if i == len(word) - 1:
                            if x.p.letter == "P":
                                return True
                            else:
                                return False
                        else:
                            x = x.p
                            break
                    else:
                        return False
                if word[i] == "q":
                    if x.q != None:
                        if i == len(word) - 1:
                            if x.q.letter == "Q":
                                return True
                            else:
                                return False
                        else:
                            x = x.q
                            break
                    else:
                        return False
                if word[i] == "r":
                    if x.r != None:
                        if i == len(word) - 1:
                            if x.r.letter == "R":
                                return True
                            else:
                                return False
                        else:
                            x = x.r
                            break
                    else:
                        return False
                if word[i] == "s":
                    if x.s != None:
                        if i == len(word)-1:
                            if x.s == "S":
                                break
                            else:
                                return False
                        else:
                            x = x.s
                            break
                    else:
                        return False
                if word[i] == "t":
                    if x.t != None:
                        if i == len(word) - 1:
                            if x.t.letter == "T":
                                return True
                            else:
                                return False
                        else:
                            x = x.t
                            break
                    else:
                        return False
                if word[i] == "u":
                    if x.u != None:
                        if i == len(word) - 1:
                            if x.u.letter == "U":
                                return True
                            else:
                                return False
                        else:
                            x = x.u
                            break
                    else:
                        return False
                if word[i] == "v":
                    if x.v != None:
                        if i == len(word) - 1:
                            if x.v.letter == "V":
                                return True
                            else:
                                return False
                        else:
                            x = x.v
                            break
                    else:
                        return False
                if word[i] == "w":
                    if x.w != None:
                        if i == len(word) - 1:
                            if x.w.letter == "W":
                                return True
                            else:
                                return False
                        else:
                            x = x.w
                            break
                    else:
                        return False
                if word[i] == "x":
                    if x.x != None:
                        if i == len(word) - 1:
                            if x.x.letter == "X":
                                return True
                            else:
                                return False
                        else:
                            x = x.x
                            break
                    else:
                        return False
                if word[i] == "y":
                    if x.y != None:
                        if i == len(word) - 1:
                            if x.y.letter == "Y":
                                return True
                            else:
                                return False
                        else:
                            x = x.y
                            break
                    else:
                        return False
                if word[i] == "z":
                    if x.z != None:
                        if i == len(word) - 1:
                            if x.z.letter == "Z":
                                return True
                            else:
                                return False
                        else:
                            x = x.z
                            break
                    else:
                        return False
        return True

# main
obj = alphabet()
obj.insert("aslam")
obj.insert("alina")
#obj.insert("noman")
#obj.insert("aslam")
#obj.insert("talha")
print(obj.search("ali"))