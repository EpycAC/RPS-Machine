class Controller():
    def setUp():
        import numpy as np
        from appendData import storage
        global proportion
        storage.setUp()
        proportion = np.array([1, 1, 1])
    def appendProbabilities():
        storage.getProbabilities()
        sampleSize = proportion[0] + proportion[1] + proportion[2]
        probability = proportion / sampleSize
        return probability
    def adjustProbabilities(oMove):
        if oMove == "r":
            proportion[1] += 1
        elif oMove == "p":
            proportion[2] += 1
        elif oMove == "s":
            proportion[0] += 1
        else:
            print("Error: Incorrect data sent from Main.py to dataControl.py")
