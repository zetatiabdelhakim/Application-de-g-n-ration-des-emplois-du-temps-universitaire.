# Les variable ******************************************************************
from tkinter import *
def bob_out():
    exit()
global coyp_nb_des_emplois
global les_emploi
global nb_des_emplois
suiv = 0
isbreak = 1
nb_des_emplois = -1
def saisir_matieres():
    def click(n=""):
        if nb_prof.get() > nb_mat.get() or nb_prof.get()<=0 or nb_mat.get()<=0 or object_nb_sal.get()<=0:
            from tkinter import messagebox
            messagebox.showinfo("input incompatible","ressayez !!!!!!!             ")
            return
        window.destroy()
    def click2(n=""):
        for i in range(nb_mat.get()):
            if lst[i][0].get() == "":
                from tkinter import messagebox
                messagebox.showinfo("input incompatible","une matiere est vide !!!!!!!             ")
                return
        windo.destroy()
    window=Tk()
    window.minsize(width=800, height=500)
    window.maxsize(width=800, height=500)
    window.protocol("WM_DELETE_WINDOW", bob_out)
    msj = Label(window, text=" Bienvenue ",font=("Comic Sans MS", "20", "bold"),fg='#9898F5')
    msj.grid(columnspan=3, row=0, column=0)
    msj = Label(window, text="  Ce programme est fait pour generer des emplois de temps", font=("Comic Sans MS","18","bold"))
    msj.grid(columnspan=3, row=1,column=0)
    msj = Label(window,text=" tout en respectant la disponibiltes de chaque professeur. ",font=("Comic Sans MS", "18", "bold"))
    msj.grid(columnspan=3, row=2, column=0)
    msj = Label(window, text=" ------------------------------------------------ ", font=("Comic Sans MS", "20", "bold"))
    msj.grid(columnspan=3, row=3, column=0)
    matieres = {}
    nb_mat = IntVar()
    global nb_matiere
    nb_prof = IntVar()
    global nb_sal
    object_nb_sal = IntVar()
    entry = Label(window, text="  Entrer le nombre de matieres :", font=("Comic Sans MS","15","bold"),fg='red')
    entry.grid(row=200,column=0)
    mat = Entry(window, textvariable= nb_mat,width=30)
    mat.grid(row=200,column=1)
    mat.focus_set()
    entry1 = Label(window, text="Entrer le nombre des profs :", font=("Comic Sans MS", "15", "bold"),fg='red')
    entry1.grid(row=201, column=0)
    mat1 = Entry(window, textvariable=nb_prof, width=30)
    mat1.grid(row=201, column=1)
    entry2 = Label(window, text="Entrer le nombre des salles :", font=("Comic Sans MS", "15", "bold"),fg='red')
    entry2.grid(row=202, column=0)
    mat2 = Entry(window, textvariable=object_nb_sal, width=30)
    mat2.grid(row=202, column=1)
    but=Button(window,text='Confirmer',command=click,background='green',fg='white',activeforeground='black',activebackground='red')
    but.grid(row=203,column=2)
    msj = Label(window, text=" ------------------------------------------------ ", font=("Comic Sans MS", "20", "bold"))
    msj.grid(columnspan=3, row=204, column=0)
    msj = Label(window, text="N.B: On admit que le nombre de prof ne peut pas etre superieur a celle des matieres. ", font=("Comic Sans MS", "11", "bold"))
    msj.grid(columnspan=3, row=206, column=0)
    window.bind_all("<Return>", click)
    window.mainloop()
    windo=Tk()
    windo.minsize(width=800, height=600)
    windo.maxsize(width=800, height=600)
    windo.protocol("WM_DELETE_WINDOW", bob_out)
    row1 = ['Matieres','Seance 2h','2 Seance-2h separes','4h Continue']
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
                e = Frame(windo )
                e.grid(row=i, column=j)
                s = Label(e, text=row1[j],font=("Comic Sans MS","10","bold"),fg='blue',width=20)
                s.grid(row=i, column=j)
                continue
            if j==0 :
                e = Entry(windo, width=20, textvariable=lst[i-1][0])
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
    but1=Button(windo,text='confirmer',command=click2,background='green',fg='white',activeforeground='black',activebackground='red')
    but1.grid(row=nb_mat.get()+1,column=4)
    msj = Label(windo, text="------"*15, font=("Comic Sans MS", "10", "bold"))
    msj.grid(columnspan=4, row=204, column=0)
    msj = Label(windo, text="N.B: pour la 2eme case (2 seances 2h separes),on admit que ",font=("Comic Sans MS", "11", "bold"))
    msj.grid(columnspan=4, row=206, column=0)
    msj = Label(windo,text="ces 2 seances ne peuvent pas etre dans le meme jour. ",font=("Comic Sans MS", "11", "bold"))
    msj.grid(columnspan=4, row=207, column=0)
    windo.bind_all("<Return>", click2)
    windo.mainloop()
    for i in range(nb_mat.get()):
        matieres[lst[i][0].get()] = lst[i][1].get()
    global nb_profs
    nb_profs = nb_prof.get()
    global nb_matiere
    nb_matiere = nb_mat.get()
    nb_sal = object_nb_sal.get()
    global nb_seance
    nb_seance = 0
    for k in matieres.values():
        if k==1:
            nb_seance +=1
        else:
            nb_seance+=2
    return matieres
def prec():
    if isbreak == 0:
        return
    global coyp_nb_des_emplois
    if suiv == 1 and coyp_nb_des_emplois == nb_des_emplois + 1:
        return
    if suiv == -1:
        if coyp_nb_des_emplois > 0:
            coyp_nb_des_emplois = coyp_nb_des_emplois - 1
            affiche_emploi(les_emploi[coyp_nb_des_emplois])
            prec()

    if suiv == 1:
        if coyp_nb_des_emplois == nb_des_emplois + 1:
            return
        if coyp_nb_des_emplois == 0:
            coyp_nb_des_emplois = 1
        affiche_emploi(les_emploi[coyp_nb_des_emplois])
        coyp_nb_des_emplois = coyp_nb_des_emplois + 1
        prec()
def saisir_prof(la_list_des_matieres,dicprof):
    root = Tk()
    root.minsize(width=1200, height=600)
    root.maxsize(width=1200, height=600)
    root.protocol("WM_DELETE_WINDOW", bob_out)
    def click(n=""):
        from tkinter import messagebox
        if nom_prof.get()=='':
            messagebox.showinfo("input incompatible", "Nom non saisi !!!!!!!             ")
            return
        a = 0
        for i in range(len(les_mat)):
            if les_mat[i].get() == 1:
                a = 1
        if a == 0:
            messagebox.showinfo("input incompatible", "Cochez au moins une matiere !!!!!!!             ")
            return
        b = 0
        for i in range(5):
            for j in range(5):
                if lst[i + 1][j + 1].get() == 1:
                    b = 1
                    break
        if b == 0:
            messagebox.showinfo("input incompatible", "Cochez au moins une disponibilite !!!!!!!             ")
            return
        root.destroy()
    # supprimer **********************************************************************
    les_mat = [0]*len(la_list_des_matieres)
    nombre_ligne = len(la_list_des_matieres) // 2 + 1
    for i in range(len(la_list_des_matieres)):
        les_mat[i] = IntVar()
        les_mat[i].set(0)
    nom_prof = StringVar()
    entry = Label(root, text="Nom du professeur :", font=("Comic Sans MS", "12", "bold"))
    entry.grid(row=0,column=0,columnspan=3)
    mat = Entry(root, textvariable= nom_prof,width=30,borderwidth=2,bg='#9898F5')
    mat.grid(row=0,column=3)
    entry = Label(root, text="Ses matieres :", font=("Comic Sans MS","10","bold"))
    entry.grid(row=2,column=0)
    acual_rows = 2
    acual_colum = 1
    for i in range(len(la_list_des_matieres)):
        s = Checkbutton(root,variable=les_mat[i], text=la_list_des_matieres[i])
        s.grid(row=acual_rows, column=acual_colum)
        if acual_colum % 5 == 0:
            acual_rows += 1
            acual_colum = 0
        acual_colum += 1
    msj = Label(root, text="-"*40 + "Disponibilite" + "-"*40, font=("Comic Sans MS", "15", "bold"))
    msj.grid(row=acual_rows+2,column=0,columnspan=6)
    acual_rows +=8
    rows = 6
    colums = 6
    jours = ['', 'lundi', 'mardi', 'm`ercredi', 'jeudi', 'vendredi']
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
                    if j == 3:
                        self.e = Frame(root)
                        self.e.grid(row=i + acual_rows + 4, column=j)
                        self.s = Label(self.e, text='    ', width=10, height=2)
                        self.s.pack()
                        continue
                    self.e = Frame(root,highlightthickness=2,highlightbackground="black")
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
    but1=Button(root,text='SUIVANT',command=click,background='green',fg='white',activeforeground='black',activebackground='red')
    but1.grid(row=200,column=3)
    root.bind_all("<Return>", click)
    msj = Label(root, text="-" * 40 + "N.B:" + "-" * 40, font=("Comic Sans MS", "15", "bold"))
    msj.grid(row=202, column=0, columnspan=6)
    msj = Label(root, text="On admit qu'une matiere ne peut pas etre enseignee par deux professeurs  ",font=("Comic Sans MS", "11", "bold"))
    msj.grid(columnspan=6, row=206, column=0)
    msj = Label(root, text="et, par consequence,on supprime une matiere associee a un professeur.    ",font=("Comic Sans MS", "11", "bold"))
    msj.grid(columnspan=6, row=207, column=0)
    msj = Label(root, text="De plus, deux professeur ne doivent pas surement avoir le meme nom.    ",font=("Comic Sans MS", "11", "bold"))
    msj.grid(columnspan=6, row=208, column=0)
    msj = Label(root, text='Cochez une case de 2h, veut dire que le professeur est disponible pour enseigner dans ce horaire. ', font=("Comic Sans MS", "11", "bold"))
    msj.grid(columnspan=6, row=209, column=0)
    msj = Label(root, text='La button "Suivant" passe a un autre professeur. ',font=("Comic Sans MS", "11", "bold"))
    msj.grid(columnspan=6, row=210, column=0)
    msj = Label(root, text='Apres le remplissage de le derniere professeur , on passe directemet aux emplois possibles, cela peut prendre quelque seconds.', font=("Comic Sans MS", "11", "bold"))
    msj.grid(columnspan=6, row=211, column=0)
    root.mainloop()
    m = [[0] * 5 for i in range(5)]
    for i in range(5):
        for j in range(5):
            m[i][j] = lst[i+1][j+1].get()
    matier_proof = []
    for i in range(len(les_mat)):
        if les_mat[i].get() == 1:
            matier_proof.append(la_list_des_matieres[i])
    for i in matier_proof:
            la_list_des_matieres.remove(i)
    # retuuuuurn **************
    dicprof[nom_prof.get()] = [matier_proof, m]
def affiche_emploi(la_possibilite):
    root=Tk()
    root.minsize(width=1100, height=600)
    root.maxsize(width=1100, height=600)
    root.protocol("WM_DELETE_WINDOW", bob_out)
    def click_suiv(n=""):
        root.destroy()
        global suiv
        suiv=1
    def click_break():
        root.destroy()
        global isbreak
        isbreak = 0
    def click_prec():
        if coyp_nb_des_emplois > 0:
            root.destroy()
            global suiv
            suiv=-1
    rows = 6
    colums = 6
    jours = ['', 'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi']
    time = ['', '8h-10h', '10h-12h', '12h-14h', '14h-16h', '16h-18h']
    for i in range(rows):
        for j in range(colums):
            if j == 0:
                e = Frame(root)
                e.grid(row=i, column=j)
                s = Label(e, text=jours[i].capitalize(), width=10, height=2,font=("Comic Sans MS", "10", "bold"))
                s.pack()
                continue
            if i == 0:
                e = Frame(root)
                e.grid(row=i, column=j)
                s = Label(e, text=time[j], width=10, height=2,font=("Comic Sans MS", "10", "bold"))
                s.pack()
                continue
            if j == 3:
                e = Frame(root)
                e.grid(row=i, column=j)
                s = Label(e, text="" , width=10, height=2)
                s.pack()
            for k in profs.keys():
                if la_possibilite[i-1][j-1] in profs[k][0]:
                    prof = k
                    break
            if la_possibilite[i-1][j-1] == 0:
                e = Frame(root)
                e.grid(row=i, column=j)
                s = Label(e, text="", width=10, height=2)
                s.pack()
                continue
            e = Frame(root)
            e.grid(row=i, column=j)
            s = Label(e, text=la_possibilite[i-1][j-1] +"\n"+ prof.upper(), width=10, height=2)
            s.pack()
    msj = Label(root, text="-" * 85, font=("Comic Sans MS", "15", "bold"))
    msj.grid(row=180, column=0, columnspan=6)
    but = Button(root, text='SUIVANT', command=click_suiv,background='green',fg='white',activeforeground='black',activebackground='red')
    but.grid(row=200, column=6)
    root.bind_all("<Return>", click_suiv)
    but1 = Button(root, text='PRECEDENT', command=click_prec,background='green',fg='white',activeforeground='black',activebackground='red')
    but1.grid(row=200, column=0)
    but2 = Button(root, text='BREAK', command=click_break,background='red',fg='white')
    but2.grid(row=200, column=3)
    msj = Label(root, text="-" * 38 + "   N.B:    " + "-" * 38, font=("Comic Sans MS", "15", "bold"))
    msj.grid(row=202, column=0, columnspan=6)
    msj = Label(root, text="C'est une possibilite de votre emplois , si ca vous convient vous pouvez arreter. ",font=("Comic Sans MS", "11", "bold"))
    msj.grid(columnspan=6, row=206, column=0)
    msj = Label(root, text="Sinon, si vous cliquez sur 'Suivant' , une autre possibilite apparaitre ( ca peut prendre quelque second).   ",font=("Comic Sans MS", "11", "bold"))
    msj.grid(columnspan=6, row=207, column=0)
    msj = Label(root, text="Vous pouvez toujours revenir en cliquant sur 'Precedent'.",font=("Comic Sans MS", "11", "bold"))
    root.mainloop()
les_emploi = []
possibilities = [[0]*5 for i in range(5)]
matieres = {}
profs = {}
dispo_prof = [[0]*5 for i in range(5)]
nb_sal = 1
matieres = saisir_matieres()
la_list_des_matieres = []
for i in matieres.keys():
    la_list_des_matieres.append(i)
for i in range(nb_profs):
    saisir_prof(la_list_des_matieres,profs)
def put_in_emploi(eeee):
    rrrr = [[0]*5 for i in range(5)]
    for i in range(5):
        for j in range(5):
            rrrr[i][j] = eeee[i][j]
    les_emploi.append(rrrr)

# traitement ************************************************************************
def trait_possiiblities(possibl):
    for i in range(5):
        for j in range(5):
            if j == 2:
                continue
            list=[0]
            if nb_sal > 0:
                for k in matieres.keys():
                    for l in profs.keys():
                        if (k in profs[l][0]) and profs[l][1][i][j] == 1:
                            list.append(k)
            possibl[i][j]=list.copy()
trait_possiiblities(possibilities)
print(possibilities)
def verif(m,matt,a,c):
    n = 0
    for i in range(5):
        for j in range(5):
            if j == 2:
                continue
            if m[i][j] == matt:
                n += 1
                b = i
    if n == 0 :
        return 1
    if n == 1 and matieres[matt] == 2 and b == a and (c-1) >= 0 and m[b][c-1] == matt:
        return 1
    if n == 1 and matieres[matt] == 3 and b != a:
        return 1
    if matt == 0:
        return 1
    return 0
def compt(m):
    n = 0
    for i in range(5):
        for j in range(5):
            if j == 2:
                continue
            if m[i][j] == 0:
                n += 1
    return n
def initializ(tab,i,j):
    for k in range(i,5):
        for l in range(j,5):
            tab[k][l] = 0
les_poss = possibilities
isbreak = 1
la_possibilite = [[0]*5 for i in range(5)]
for i1 in les_poss[0][0]:
    initializ(la_possibilite, 0, 0)
    if isbreak == 0:
        break
    if verif(la_possibilite, i1, 0, 0) == 0:
        continue
    la_possibilite[0][0] = i1
    for i2 in les_poss[0][1]:
        initializ(la_possibilite, 0, 1)
        if isbreak == 0:
            break
        if verif(la_possibilite, i2, 0, 1) == 0:
            continue
        la_possibilite[0][1] = i2
        for i3 in les_poss[0][3]:
            initializ(la_possibilite, 0, 3)
            if isbreak == 0:
                break
            if verif(la_possibilite, i3, 0, 3) == 0:
                continue
            la_possibilite[0][3] = i3
            for i4 in les_poss[0][4]:
                initializ(la_possibilite, 0, 4)
                if isbreak == 0:
                    break
                if verif(la_possibilite, i4, 0, 4) == 0:
                    continue
                la_possibilite[0][4] = i4
                for i5 in les_poss[1][0]:
                    initializ(la_possibilite, 1, 0)
                    if isbreak == 0:
                        break
                    if verif(la_possibilite, i5, 1, 0) == 0:
                        continue
                    la_possibilite[1][0] = i5
                    for i6 in les_poss[1][1]:
                        initializ(la_possibilite, 1, 1)
                        if isbreak == 0:
                            break
                        if verif(la_possibilite, i6, 1, 1) == 0:
                            continue
                        la_possibilite[1][1] = i6
                        for i7 in les_poss[1][3]:
                            initializ(la_possibilite, 1, 3)
                            if isbreak == 0:
                                break
                            if verif(la_possibilite, i7, 1, 3) == 0:
                                continue
                            la_possibilite[1][3] = i7
                            for i8 in les_poss[1][4]:
                                initializ(la_possibilite, 1, 4)
                                if isbreak == 0:
                                    break
                                if verif(la_possibilite, i8, 1, 4) == 0:
                                    continue
                                la_possibilite[1][4] = i8
                                for i9 in les_poss[2][0]:
                                    initializ(la_possibilite, 2, 0)
                                    if isbreak == 0:
                                        break
                                    if verif(la_possibilite, i9, 2, 0) == 0:
                                        continue
                                    la_possibilite[2][0] = i9
                                    for i10 in les_poss[2][1]:
                                        initializ(la_possibilite, 2, 1)
                                        if isbreak == 0:
                                            break
                                        if verif(la_possibilite, i10, 2, 1) == 0:
                                            continue
                                        la_possibilite[2][1] = i10
                                        for i11 in les_poss[2][3]:
                                            initializ(la_possibilite, 2, 3)
                                            if isbreak == 0:
                                                break
                                            if verif(la_possibilite, i11, 2, 3) == 0:
                                                continue
                                            la_possibilite[2][3] = i11
                                            for i12 in les_poss[2][4]:
                                                initializ(la_possibilite, 2, 4)
                                                if isbreak == 0:
                                                    break
                                                if verif(la_possibilite, i12, 2, 4) == 0:
                                                    continue
                                                la_possibilite[2][4] = i12
                                                for i13 in les_poss[3][0]:
                                                    initializ(la_possibilite, 3, 0)
                                                    if isbreak == 0:
                                                        break
                                                    if verif(la_possibilite, i13, 3, 0) == 0:
                                                        continue
                                                    la_possibilite[3][0] = i13
                                                    for i14 in les_poss[3][1]:
                                                        initializ(la_possibilite, 3, 1)
                                                        if isbreak == 0:
                                                            break
                                                        if verif(la_possibilite, i14, 3, 1) == 0:
                                                            continue
                                                        la_possibilite[3][1] = i14
                                                        for i15 in les_poss[3][3]:
                                                            initializ(la_possibilite, 3, 3)
                                                            if isbreak == 0:
                                                                break
                                                            if verif(la_possibilite, i15, 3, 3) == 0:
                                                                continue
                                                            la_possibilite[3][3] = i15
                                                            for i16 in les_poss[3][4]:
                                                                initializ(la_possibilite, 3, 4)
                                                                if isbreak == 0:
                                                                    break
                                                                if verif(la_possibilite, i16, 3, 4) == 0:
                                                                    continue
                                                                la_possibilite[3][4] = i16
                                                                for i17 in les_poss[4][0]:
                                                                    initializ(la_possibilite, 4, 0)
                                                                    if isbreak == 0:
                                                                        break
                                                                    if verif(la_possibilite, i17, 4, 0) == 0:
                                                                        continue
                                                                    la_possibilite[4][0] = i17
                                                                    for i18 in les_poss[4][1]:
                                                                        initializ(la_possibilite, 4, 1)
                                                                        if isbreak == 0:
                                                                            break
                                                                        if verif(la_possibilite, i18, 4, 1) == 0:
                                                                            continue
                                                                        la_possibilite[4][1] = i18
                                                                        for i19 in les_poss[4][3]:
                                                                            initializ(la_possibilite, 4, 3)
                                                                            if isbreak == 0:
                                                                                break
                                                                            if verif(la_possibilite, i19, 4, 3) == 0:
                                                                                continue
                                                                            la_possibilite[4][3] = i19
                                                                            for i20 in les_poss[4][4]:
                                                                                initializ(la_possibilite, 4, 4)
                                                                                if isbreak == 0:
                                                                                    break
                                                                                if verif(la_possibilite, i20, 4, 4) == 0:
                                                                                    continue
                                                                                la_possibilite[4][4] = i20
                                                                                if compt(la_possibilite) == 20 - nb_seance:
                                                                                    nb_des_emplois += 1
                                                                                    coyp_nb_des_emplois = nb_des_emplois
                                                                                    put_in_emploi(la_possibilite)
                                                                                    affiche_emploi(la_possibilite)
                                                                                    if suiv == -1:
                                                                                        prec()