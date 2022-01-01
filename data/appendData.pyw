class storage():
    def __init__(self, path, profile):
        self.path = path
        self.profile = profile

    def createPath(self, path, inp, profile):
        import os
        pathRead = path + "profile\ ".replace(" ", "") + str(profile) + "\probability\ ".replace(" ", "")
        if len(inp) == 0:
            if not(os.path.exists(pathRead)):
                os.makedirs(pathRead)
        else:
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
        return pathRead + "\ ".replace(" ", "")

    def readFile(self, inp):
        pathRead = self.createPath(self.path, inp, self.profile)
        import json
        try:
            file = json.load(open(pathRead + "probability.json", "r"))
            probability = file["probability"]
            return probability
        except FileNotFoundError:
            file = open(pathRead + "probability.json", "w")
            b = file.write(json.dumps({"probability": [1, 1, 1]}))
            file.close()
            return [1, 1, 1]

    def writeFile(self, inp, output):
        pathRead = self.createPath(self.path, inp, self.profile)
        import json
        try:
            data = json.load(open(pathRead + "probability.json", "r"))
            data["probability"] = output
            file = open(pathRead + "probability.json", "w")
            b = file.write(json.dumps(data))

        except FileNotFoundError:
            file = open(pathRead + "probability.json", "w")
            b = file.write(json.dumps({"probability": output}))
            file.close()
