# dbconnectionupdated
from tkinter import messagebox
import mysql.connector
from similar import checksimilar

db = mysql.connector.connect(user="root",
                             password="password",
                             host="localhost",
                             database="pytest")
mycur = db.cursor(buffered=True)


def getqstns():
    qstns = []
    mycur.execute("SELECT * FROM pyestion")
    chk = mycur.fetchall()
    for i in chk:
        qstns.append(i[1])
    print(qstns)
    return qstns  # returns all questions inside the database


def submitdb(question, usr, comp, num):
    quest = question
    usrnm = usr
    company = comp
    phone = num

    qstnlist = getqstns()
    bull = checksimilar(quest, qstnlist)
    print(bull)
    respose = messagebox.askyesno("similar element found", "we've detected a similar question, Do you wish to submit ?")
    if respose == 1:
        query = """INSERT INTO pyestion (question,usrname,company,phone) VALUE ('%s','%s','%s',%s) """
        fquery = query % (quest, usrnm, company, phone)
        mycur.execute(fquery)
        db.commit()
    else:
        messagebox.showwarning("Submit denied", "You denied the submit")