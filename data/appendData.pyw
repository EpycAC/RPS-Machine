class storage():
    def __init__(self, path):
        self.path = path
        print(self.path)
    def readFile(self, inp):
        import os
        pathRead = self.path + "probability\ ".replace(" ", "")
        for index in range(len(inp)):
            pathRead = pathRead + inp[index]
            pathRead = list(pathRead)
            if pathRead[-1] == inp[index]:
                pathRead.append("\ ".replace(" ", ""))
                pathRead = "".join(pathRead)
            else:
                pathRead = "".join(pathRead)
            if not(os.path.exists(pathRead)):
                os.makedirs(pathRead)
        try:
            open(pathRead + "probability.json")
