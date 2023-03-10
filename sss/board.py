from tkinter import *
from scraper import Scrape

root = Tk()
root.title("Sudoku")
root.geometry("440x550")
label = Label(root, text="Sudoku").grid(row=0,column=1,columnspan=10)
cells = {}

def validate_number(temp):
    x = (temp.isdigit() or temp == "") and len(temp) < 2
    return x

reg = root.register(validate_number)

def drawGrid(row,col,color):        
    for i in range(9):
        for j in range(9):
            if i!=3 and i!=4 and i!=5 and j!=3 and j!=4 and j!=5:
                e = Entry(root,width=5,bg=color,justify="center",validate="key",validatecommand=(reg,"%P"))
            elif (i==3 and (j==3 or j==4 or j==5)) or (i==4 and (j==3 or j==4 or j==5)) or (i==5 and (j==3 or j==4 or j==5)):
                e = Entry(root,width=5,bg=color,justify="center",validate="key",validatecommand=(reg,"%P"))
            else:
                e = Entry(root,width=5,bg="#ffffff",justify="center",validate="key",validatecommand=(reg,"%P"))
            e.grid(row=row+i+1,column=col+j+1,sticky="nsew",padx=1,pady=1,ipady=5)
            cells[(row+i,col+j)] = e

def addValueFromScraper():
    s = Scrape()
    s.scrape();
    mat = s.change_to_mat()
    for i in range(0,9):
        for j in range(0,9):
            cell = cells[(i,j)]
            if mat[i][j] != 0:
                cell.insert(i*j+1,mat[i][j])
            else:
                cell.delete(0,"end")

def resetGame():
    for row in range(0,9):
        for col in range(0,9):
            cell = cells[(row,col)]
            cell.delete(0,"end")
    addValueFromScraper()
            
def printInFile():
    name = nameEntry.get()
    surname = surnameEntry.get()
    f = open(f"{name}_{surname}.txt","w") 
    for row in range(0,9):
        for col in range(0,9):
            val = cells[(row,col)].get()
            if val == "":
                f.write("0 ")
            else:
                f.write(f"{val} ")
        f.write("\n")        
    w2.destroy()

def printResult():
    global w2
    w2 = Tk()
    w2.title("Sudoku")
    w2.geometry("250x150")
    global nameEntry,surnameEntry
    Label(w2, text="Name:").grid(row=0,column=1,pady=10)
    nameEntry = Entry(w2,width=20,justify="center")
    nameEntry.grid(row=0,column=3,pady=10)
    Label(w2, text="Surname:").grid(row=1,column=1,pady=10)
    surnameEntry = Entry(w2,width=20,justify="center")
    surnameEntry.grid(row=1,column=3,pady=15)
    submit = Button(w2,command=printInFile,text="Submit",width=10)
    submit.grid(row=3,column=1,columnspan=3)
    
    
btn1 = Button(root,command=printResult,text="Print Result",width=10)
btn1.grid(row=20,column=1,columnspan=5,pady=20)

btn2 = Button(root,command=resetGame,text="Reset",width=10)
btn2.grid(row=20,column=5,columnspan=5,pady=20)


drawGrid(0,0,"#f1f9d2")
addValueFromScraper()
root.mainloop()    
