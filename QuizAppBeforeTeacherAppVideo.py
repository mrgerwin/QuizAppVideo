from guizero import App, Text, PushButton, ButtonGroup, Picture, TextBox
import random
import sqlite3 as sql

def databaseConnect():
    conn = sql.connect("quizapp.db")
    return conn

def makeDBTable(conn):
    code = '''CREATE TABLE IF NOT EXISTS SCORES
            (ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, RESULT TEXT NOT NULL);'''
    conn.execute(code)
    conn.commit()
    
def newDBScoreEntry(conn, ID, Name, Result):
    code = "INSERT INTO SCORES (ID, NAME, RESULT) VALUES(?,?,?);"
    conn.execute(code, (ID, Name, str(Result)))
    conn.commit()

def updateScores(conn, ID, Result):
    code = "UPDATE SCORES SET Result = ? WHERE ID = ?"
    conn.execute(code, (str(Result), ID))
    conn.commit()
    
def newQuiz(conn, result):
    makeDBTable(conn)
    curr = conn.cursor()
    getIDs = "SELECT ID FROM SCORES;"
    curr.execute(getIDs)
    rows = curr.fetchall()
    ID = len(rows) + 1
    newDBScoreEntry(conn, ID, "", str(result))
    return ID

def nameChanged():
    global ID, conn
    code = "UPDATE SCORES SET NAME = ? WHERE ID = ?"
    conn.execute(code, (nameTextBox.value, ID))
    conn.commit()

def shuffleChoices():
    global index
    random.shuffle(choicesList[index])

def nextPressed():
    global index
    index = index + 1
    if index >= len(questionList):
        index = 0
    updateQuestion()
    
def updateQuestion():
    #Update the Picture
    picture.value = ImageList[index]
    #Update the Question
    question.value = questionList[index]
    #Update the AnswerChoices
    choices = []
    for choiceButton in answerChoices.get_group_as_list():
        choices.append(choiceButton[0])
    for choice in choices:
        answerChoices.remove(choice)
    for choice in choicesList[index]:
        answerChoices.append(choice)

def checkAnswer():
    global result
    userChoice = answerChoices.value_text
    #if userChoice is not the same as the answerlist then incorrect else correct
    if userChoice != answerList[index]:
        print("incorrect")
    else:
        print("correct")  
    

def submitPressed():
    checkAnswer()
    

questionList = []
question1 = "Select the word that means an object from some class."
question2 = "Variables that are used to describe data of objects are called _______________."
question3 = "Functions that are used to describe the behavior of objects are called _______________."
question4 = "What is a string when referred to in computer programming?"
question5 = "In computer programming, is a list a type of function?"

questionList.append(question1)
questionList.append(question2)
questionList.append(question3)
questionList.append(question4)
questionList.append(question5)


answerList = ["Instance", "Properties", "Methods", "Text", "No"]
choicesList = [["Creation", "Instance", "Establishment", "Definition"], ["Properties","Numbers", "Files", "Descripters"], ["Regulators", "Events", "Elaborators", "Methods"],["Yarn", "Guitars", "Text", "Functions"], ["Yes", "No"]]

ImageList = ["ImageQuestion1.png", "ImageQuestion2.png", "ImageQuestion3.png", "ImageQuestion4.png", "ImageQuestion5.png"]
index = 0

app = App(title="Quiz App", height = 800, width = 1200)
nameLabel = Text(app, text="Your Name: ")
nameTextBox = TextBox(app, command = nameChanged)
picture = Picture(app, image = ImageList[0])
question = Text(app, text = questionList[0])
submitButton = PushButton(app, text = "Submit Answer", command = submitPressed)
nextButton = PushButton(app, text = "Next Question", command = nextPressed)
shuffleChoices()
answerChoices = ButtonGroup(app, options = choicesList[0], selected = None)


app.display()