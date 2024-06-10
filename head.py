from tkinter import *
def saisir_matieres():
    def click():
        window.destroy()
    def click2():
        windo.destroy()
    def bob_out():
        exit()
    window=Tk()
    window.protocol("WM_DELETE_WINDOW", bob_out)
    msj = Label(window, text="Ce programme est :", font=("Arial","30","bold"))
    msj.grid(columnspan=3, row=0,column=0)
    matieres = {}
    nb_mat = IntVar()
    global nb_matiere
    nb_prof = IntVar()
    entry = Label(window, text="entrer le nombre de matieres :", font=("Arial","20","bold"))
    entry.grid(row=1,column=0)
    mat = Entry(window, textvariable= nb_mat,width=30)
    mat.grid(row=1,column=2)
    entry1 = Label(window, text="entrer le nombre des profs :", font=("Arial", "20", "bold"))
    entry1.grid(row=2, column=0)
    mat1 = Entry(window, textvariable=nb_prof, width=30)
    mat1.grid(row=2, column=2)
    but=Button(window,text='confirmer',command=click)
    but.grid(row=3,column=1)
    window.mainloop()
    windo=Tk()
    row1 = ['matieres','seance 2h','2 seance 2h separes','4h continue']
    lst = [['']*2 for i in range(nb_mat.get())]
    for i in range(nb_mat.get()):
        for j in range(2):
            if j == 1:
                lst[i][j] = IntVar()
                lst[i][j].set(0)
            else:
                lst[i][j] = StringVar()
                lst[i][j].set("")
    for i in range(nb_mat.get()+1):
        for j in range(4):
            if i==0 :
                e = Frame(windo)
                e.grid(row=i, column=j)
                s = Label(e, text=row1[j])
                s.grid(row=i, column=j)
                continue
            if j==0 :
                e = Entry(windo, width=20, fg='blue', textvariable=lst[i-1][0])
                e.grid(row=i, column=j)
                continue
            if j == 1:
                lst[i - 1][1].set(1)
                e = Radiobutton(windo,variable=lst[i-1][1],value=1)
                e.grid(row=i, column=j)
            if j == 2:
                e = Radiobutton(windo,variable=lst[i-1][1],value=3)
                e.grid(row=i, column=j)
            if j == 3:
                e = Radiobutton(windo,variable=lst[i-1][1],value=2)
                e.grid(row=i, column=j)
    but1=Button(windo,text='confirmer',command=click2)
    but1.grid(row=nb_mat.get()+1,column=4)
    windo.mainloop()
    for i in range(nb_mat.get()):
        matieres[lst[i][0].get()] = lst[i][1].get()
    global nb_profs
    nb_profs = nb_prof.get()
    global nb_matiere
    nb_matiere = nb_mat.get()
    global nb_seance
    nb_seance = 0
    for k in matieres.values():
        if k==1:
            nb_seance +=1
        else:
            nb_seance+=2
    return matieres
print(saisir_matieres())