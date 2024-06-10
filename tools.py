from tkinter import *
def saisir_prof(la_list_des_matieres,dicprof):
    root = Tk()
    def click():
        root.destroy()
    list_matiere = ["ro", "linux", "stat","gfds","fghj","dfg"] # supprimer **********************************************************************
    les_mat = [0]*len(list_matiere)
    nombre_ligne = len(list_matiere) // 2 + 1
    for i in range(len(list_matiere)):
        les_mat[i] = IntVar()
        les_mat[i].set(0)
    nom_prof = StringVar()
    entry = Label(root, text="NOM BROF :", font=("Arial","10","bold"))
    entry.grid(row=0,column=0,columnspan=3)
    mat = Entry(root, textvariable= nom_prof,width=30)
    mat.grid(row=0,column=3)
    entry = Label(root, text="ses matiere :", font=("Arial","10","bold"))
    entry.grid(row=2,column=0)
    acual_rows = 2
    acual_colum = 1
    for i in range(len(list_matiere)):
        s = Checkbutton(root,variable=les_mat[i],text=list_matiere[i])
        s.grid(row=acual_rows, column=acual_colum)
        if acual_colum % 5 == 0:
            acual_rows += 1
            acual_colum = 0
        acual_colum += 1
    rows = 6
    colums = 6
    jours = ['', 'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi']
    time = ['', '8h-10h', '10h-12h', '12h-14h', '14h-16h', '16h-18h']
    class Table:
        def __init__(self, root):
            for i in range(rows):
                for j in range(colums):
                    if j == 0:
                        lst[i][j]=jours[i]
                        self.e = Frame(root)
                        self.e.grid(row=i+acual_rows+4, column=j)
                        self.s = Label(self.e, text=lst[i][j], width=10, height=2)
                        self.s.pack()
                        continue
                    if i == 0:
                        lst[i][j] = time[j]
                        self.e = Frame(root)
                        self.e.grid(row=i+acual_rows+4, column=j)
                        self.s = Label(self.e, text=lst[i][j], width=10, height=2)
                        self.s.pack()
                        continue
                    self.e = Frame(root)
                    self.e.grid(row=i+acual_rows+4, column=j)
                    self.s = Checkbutton(self.e,width=27,height=2 , variable = lst[i][j])
                    self.s.pack()
    # take the data
    lst = [[0]*rows for i in range(colums)]
    for i in range(rows):
        for j in range(colums):
            lst[i][j] = IntVar()
            lst[i][j].set(0)
    # find total number of rows and
    # columns in list
    # create root window
    t = Table(root)
    but1=Button(root,text='SUIVANT',command=click)
    but1.grid(row=nombre_ligne+10,column=3)
    root.mainloop()
    m = [[0] * 5 for i in range(5)]
    for i in range(5):
        for j in range(5):
            m[i][j] = lst[i+1][j+1].get()
    matier_proof = []
    for i in range(len(les_mat)):
        if les_mat[i].get() == 1:
            matier_proof.append(list_matiere[i])
            list_matiere.remove(list_matiere[i])
    # retuuuuurn **************
    dicprof[nom_prof.get()] = [matier_proof, m]
dict = {}
saisir_prof([1,2],dict)
print(dict)
