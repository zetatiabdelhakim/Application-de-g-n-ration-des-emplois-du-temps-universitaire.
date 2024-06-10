from  tkinter import  *
def affiche_emploi(la_possibilite):
    root=Tk()
    rows = 6
    colums = 6
    jours = ['', 'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi']
    time = ['', '8h-10h', '10h-12h', '12h-14h', '14h-16h', '16h-18h']
    for i in range(rows):
        for j in range(colums):
            if j == 0:
                e = Frame(root)
                e.grid(row=i, column=j)
                s = Label(e, text=jours[i], width=10, height=2)
                s.pack()
                continue
            if i == 0:
                e = Frame(root)
                e.grid(row=i, column=j)
                s = Label(e, text=time[j], width=10, height=2)
                s.pack()
                continue
            if j == 3:
                e = Frame(root)
                e.grid(row=i, column=j)
                s = Label(e, text="" +, width=10, height=2)
                s.pack()
            for k in profs.keys():
                if la_possibilite[i-1][j-1] in profs[k][0]:
                    prof = k
                    break
            if la_possibilite[i-1][j-1] == 0:
                e = Frame(root)
                e.grid(row=i, column=j)
                s = Label(e, text=""+, width=10, height=2)
                s.pack()
                continue
            e = Frame(root)
            e.grid(row=i, column=j)
            s = Label(e, text=la_possibilite[i-1][j-1] +"\n"+prof, width=10, height=2)
            s.pack()
    root.mainloop()
affiche_emploi([[0]*5 for i in range(5)])
"""def print_emploi(m):
    for i in range(5):
        for j in range(5):
            if j == 2:
                continue
            for k in profs.keys():
                if m[i][j] in profs[k][0]:
                    prof = k
                    break
            if m[i][j] == 0:
                print("break", end='\t\t|\t\t')
                continue
            print(m[i][j], ' : ', prof, end='\t\t|\t\t')
        print()
        print()"""
