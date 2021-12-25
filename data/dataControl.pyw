class Controller():
    def setUp():
        import numpy as np
        import sys
        sys.path.append(__file__.replace("dataControl.pyw", ""))
        from appendData import storage
        global s
        s = storage(__file__.replace("dataControl.pyw", ""))
        global proportion
        proportion = np.array([1, 1, 1])
        global tab
        tab = []
    def appendProbabilities():
        #storage.getProbabilities()
        sampleSize = proportion[0] + proportion[1] + proportion[2]
        probability = proportion / sampleSize
        return probability
    def adjustProbabilities(oMove):
        if oMove == "r":
            proportion[1] += 1
            tab.append("p")
            print(tab)
        elif oMove == "p":
            proportion[2] += 1
            tab.append("s")
            print(tab)
        elif oMove == "s":
            proportion[0] += 1
            tab.append("r")
            print(tab)
        else:
            print("Error: Incorrect data sent from Main.py to dataControl.py")
        print(s.readFile(tab))
