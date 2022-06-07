from guizero import App, Text, PushButton, Slider, Waffle, Box, ListBox
import sqlite3 as sql

def getResults(conn):
    results = []
    code = "SELECT RESULT FROM SCORES"
    curr = conn.cursor()
    curr.execute(code)
    rows = curr.fetchall()
    for row in rows:
        results.append(eval(row[0]))
    return results

def getStudentNames(conn):
    code = "SELECT NAME FROM SCORES"
    curr = conn.cursor()
    curr.execute(code)
    rows = curr.fetchall()
    print(rows)
    return rows

def getQuestions(conn):
    code = "SELECT QUESTION FROM QUESTIONS"
    curr = conn.cursor()
    curr.execute(code)
    rows = curr.fetchall()
    print(rows)
    return rows

def updatePressed():
    getQuestions(conn)
def Update():
    x = 0
    y = 0
    for student in students:
        for pixel in student:
            if pixel == True:
                questionWaffle.set_pixel(x, y, "green")
            elif pixel == False:
                questionWaffle.set_pixel(x, y, "red")
            x += 1
        y += 1
        x = 0


def studentPressed():
    pass


def questionPressed():
    pass


app = App(title="Teacher App", height=800, width=1200, layout="grid")

BoxUL = Box(app, grid=[0, 0], layout="grid")
BoxUR = Box(app, grid=[1, 0], layout="grid")
BoxLL = Box(app, grid=[0, 1], layout="grid")
BoxLR = Box(app, grid=[1, 1], layout="grid")
updateButton = PushButton(app, text="Update", command=updatePressed, grid=[1, 2])

#student1 = [True, True, False, True, False, True]
#student2 = [False, True, None, True, False, True]
#student3 = [True, None, True, True, False, True]
#student4 = [False, False, False, True, False, False]
conn = sql.connect("quizapp.db")
students = getResults(conn)
questions = getQuestions(conn)
studentNames = getStudentNames(conn)
questionWaffle = Waffle(BoxLR, width=len(questions), height=len(students), dim=50, grid=[0, 0])
studentButtons = []
questionButtons = []
i = 0
for student in studentNames:
    studentButtons.append(PushButton(BoxLL, text=student, height=1, width=3, command=studentPressed, grid=[0, i]))
    i += 1
i = 0
for i in range(len(questions)):
    i += 1
    questionButtons.append(PushButton(BoxUR, text=str(i), width=3, height=1, command=questionPressed, grid=[i - 1, 0]))

questionsBox = ListBox(app, items = questions, grid=[1,3])

Update()
app.display()
