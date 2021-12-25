class storage():
    def __init__(self, path):
        self.path = path
        print(self.path)
    def readFile(self, inp):
        pathRead = self.path
        global tempPathRead
        tempPathRead = pathRead
        for index in range(len(inp)):
            pathRead = pathRead + inp[index]
            pathRead = list(pathRead)
            if pathRead[-1] == inp[index]:
                pathRead.append("\ ".replace(" ", ""))
                pathRead = "".join(pathRead)
            else:
                pathRead = "".join(pathRead)
        print(pathRead)
