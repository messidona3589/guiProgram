import pymysql
from tkinter import *
from tkinter import messagebox

# CREATE database DBname;
# USE DBname;
# CREATE TABLE TableName (name VARCHAR(20), id VARCHAR(20), email VARCHAR(20), address VARCHAR(255), phone VARCHAR(30));

# fixed values : host=127.0.0.1 user=root, password=0000, db=dbname

def insertData():
    con, cur = None,None
    newName, newId, newEmail, newAd, newPh = "", "", "", "", ""
    sql = ""

    conn = pymysql.connect(host='localhost',user='root',password='0000',db='dbname')
    cur = conn.cursor()

    newName = edtName.get(); newId = edtId.get(); newEmail = edtEmail.get(); newAd = edtAd.get(); newPh = edtPh.get();
    
    if newName=="" or newId=="" or newEmail=="" or newAd=="" or newPh=="":
        messagebox.showinfo("ERROR", "ENTER ALL THE VALUES")
        conn.close()
        return
    
    sql = "INSERT INTO tablename VALUES('" + newName + "','"  + newId + "','"  + newEmail + "','"  + newAd + "','"  + newPh + "');"

    try :
        cur.execute(sql)
        messagebox.showinfo("SUCCESS", "INSERT DATA SUCCESS")
        
    except :
        messagebox.showinfo("FAIL", "INSERT DATA FAIL")

    conn.commit()
    conn.close()

    displayAll()

    
def searchData():
    nameDataList, idDataList, emailDataList, adDataList, phDataList = [], [], [], [], []
    con, cur = None,None
    name_, id_, email_, ad_, ph_ = "", "", "", "", ""
    sql = ""

    conn = pymysql.connect(host='localhost',user='root',password='0000',db='DBname')
    cur = conn.cursor()

    name_ = edtName.get(); id_ = edtId.get(); email_ = edtEmail.get(); ad_ = edtAd.get(); ph_ = edtPh.get();

    cnt = 0;
    sql = "SELECT * FROM tableName "
    if name_!="":
        sql += "WHERE name='" + name_ + "'"
        cnt+=1
    if id_!="":
        if cnt==0:
            sql += "WHERE id='" + id_ + "'"
        else:
            sql += " AND id='" + id_ + "'"
        cnt+=1
    if email_!="":
        if cnt==0:
            sql += "WHERE email='" + email_ +"'"
        else:
            sql += " AND email='" + email_ + "'"
        cnt+=1
    if ad_!="":
        if cnt==0:
            sql += "WHERE address='" + ad_ + "'"
        else:
            sql += " AND address='" + ad_ + "'"
        cnt+=1
    if ph_!="":
        if cnt==0:
            sql += "WHERE phone='" + ph_ + "'"
        else:
            sql += " AND phone='" + ph_ + "'"
        cnt+=1

    cur.execute(sql)

    nameList.delete(0,END)
    idList.delete(0,END)
    emailList.delete(0,END)
    adList.delete(0,END)
    phList.delete(0,END)

    while(True):
        row = cur.fetchone()
        if row==None:
            break;
        nameDataList.append(row[0]);
        idDataList.append(row[1]);
        emailDataList.append(row[2]),
        adDataList.append(row[3]);
        phDataList.append(row[4]);


    for name_, id_, email_, ad_, ph_ in zip(nameDataList, idDataList, emailDataList, adDataList, phDataList):
        nameList.insert(END, name_);
        idList.insert(END, id_);
        emailList.insert(END, email_);
        adList.insert(END, ad_);
        phList.insert(END, ph_);

    conn.close()
            

def deleteData():
    con, cur = None,None
    name_, id_, email_, ad_, ph_ = "", "", "", "", ""
    sql = ""

    conn = pymysql.connect(host='localhost',user='root',password='0000',db='DBname')
    cur = conn.cursor()

    name_ = edtName.get(); id_ = edtId.get(); email_ = edtEmail.get(); ad_ = edtAd.get(); ph_ = edtPh.get();
    sql = "DELETE FROM tableName WHERE name='" + name_ + "'AND id='" + id_ + "'AND email= '" + email_ + "'AND address= '" + ad_ + "'AND phone='" + ph_ + "';"

    try :
        cur.execute(sql)
        messagebox.showinfo("SUCCESS", "DELETE DATA SUCCESS")
        
    except :
        messagebox.showinfo("FAIL", "DELETE DATA FAIL")

    conn.commit()
    conn.close()

    displayAll()


    
def displayAll():

    nameList.delete(0,END)
    idList.delete(0,END)
    emailList.delete(0,END)
    adList.delete(0,END)
    phList.delete(0,END)
    
    nameDataList, idDataList, emailDataList, adDataList, phDataList = [], [], [], [], []

    conn = pymysql.connect(host='localhost',user='root',password='0000',db='DBname')
    cur = conn.cursor()
    
    sql = "SELECT * FROM tableName"

    cur.execute(sql)
    cnt = 0

    while(True):
        row = cur.fetchone()
        if row==None:
            break;
        cnt += 1
        nameDataList.append(row[0]);
        idDataList.append(row[1]);
        emailDataList.append(row[2]),
        adDataList.append(row[3]);
        phDataList.append(row[4]);


    for name_, id_, email_, ad_, ph_ in zip(nameDataList, idDataList, emailDataList, adDataList, phDataList):
        nameList.insert(END, name_);
        idList.insert(END, id_);
        emailList.insert(END, email_);
        adList.insert(END, ad_);
        phList.insert(END, ph_);

    conn.close()

    if cnt==0: messagebox.showinfo("NOTHING", "TABLE IS EMPTY")
            

#main
root = Tk()
root.geometry("700x500")
root.title("GUI Program")

edtFrame = Frame(root)
edtFrame.pack()
labelFrame = Frame(root)
labelFrame.pack()
listFrame = Frame(root)
listFrame.pack(side=BOTTOM,fill=BOTH, expand=1)

edtName = Entry(edtFrame, width = 12); edtName.pack(side=LEFT, padx=10, pady=10);
edtId = Entry(edtFrame, width = 12); edtId.pack(side=LEFT, padx=10, pady=10);
edtEmail = Entry(edtFrame, width = 12); edtEmail.pack(side=LEFT, padx=10, pady=10);
edtAd = Entry(edtFrame, width = 12); edtAd.pack(side=LEFT, padx=10, pady=10);
edtPh = Entry(edtFrame, width = 12); edtPh.pack(side=LEFT, padx=10, pady=10);

insertButton = Button(edtFrame, text="insert", command=insertData); insertButton.pack(side=LEFT, padx=5, pady=10);
searchButton = Button(edtFrame, text="search", command=searchData); searchButton.pack(side=LEFT, padx=5, pady=10);
deleteButton = Button(edtFrame, text="delete", command=deleteData); deleteButton.pack(side=LEFT, padx=5, pady=10);

nameLabel = Label(labelFrame, text="Name"); nameLabel.pack(side=LEFT, padx=(0, 30));
idLabel = Label(labelFrame, text="ID"); idLabel.pack(side=LEFT, padx = 40);
emailLabel = Label(labelFrame, text="Email"); emailLabel.pack(side=LEFT, padx = 45);
adLabel = Label(labelFrame, text="Address"); adLabel.pack(side=LEFT, padx = 45);
phLabel = Label(labelFrame, text="Phone"); phLabel.pack(side=LEFT, padx = 45);

nameList = Listbox(listFrame, bg="yellow"); nameList.pack(side=LEFT, fill=BOTH, expand=1);
idList = Listbox(listFrame, bg="yellow"); idList.pack(side=LEFT, fill=BOTH, expand=1);
emailList = Listbox(listFrame, bg="yellow"); emailList.pack(side=LEFT, fill=BOTH, expand=1);
adList = Listbox(listFrame, bg="yellow"); adList.pack(side=LEFT, fill=BOTH, expand=1);
phList = Listbox(listFrame, bg="yellow"); phList.pack(side=LEFT, fill=BOTH, expand=1);

displayAll()

root.mainloop()



