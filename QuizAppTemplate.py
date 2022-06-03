from guizero import App, Text, PushButton, ButtonGroup, Picture
import random

def shuffleChoices():
    global index
    random.shuffle(choicesList[index])

def nextPressed():
    global index
    pass

questionList = []
question1 = "Select the word that means an object from some class."
question2 = "Variables that are used to describe data of objects are called _______________."
question3 = "Functions that are used to describe the behavior of objects are called _______________."

questionList.append(question1)
questionList.append(question2)
questionList.append(question3)

answerList = ["Instance", "Properties", "Methods"]
choicesList = [["Creation", "Instance", "Establishment", "Definition"], ["Properties","Numbers", "Files", "Descripters"], ["Regulators", "Events", "Elaborators", "Methods"]]

ImageList = ["ImageQuestion1.png", "ImageQuestion2.png", "ImageQuestion3.png"]
index = 0

app = App(title="Quiz App", height = 800, width = 1200)
picture = Picture(app, image = ImageList[0])
question = Text(app, text = questionList[0])
nextButton = PushButton(app, text = "Next Question", command = nextPressed)
shuffleChoices()
answerChoices = ButtonGroup(app, options = choicesList[0], selected = None)


app.display()