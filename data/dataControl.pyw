class Controller():
    def setUp():
        import sys
        sys.path.append(__file__.replace("dataControl.pyw", ""))
        from appendData import storage
        global s
        s = storage(__file__.replace("dataControl.pyw", ""))
        global tab
        tab = []

    def appendProbabilities():
        global proportion
        import numpy as np
        proportion = np.array(s.readFile(tab))
        sampleSize = proportion[0] + proportion[1] + proportion[2]
        probability = proportion / sampleSize
        return probability

    def adjustProbabilities(oMove):
        import numpy as np
        if oMove == "r":
            proportion[1] += 1
            s.writeFile(tab, proportion.tolist())
            tab.append("p")
        elif oMove == "p":
            proportion[2] += 1
            s.writeFile(tab, proportion.tolist())
            tab.append("s")
        elif oMove == "s":
            proportion[0] += 1
            s.writeFile(tab, proportion.tolist())
            tab.append("r")
        else:
            print("Error: Incorrect data sent from Main.py to dataControl.py")
