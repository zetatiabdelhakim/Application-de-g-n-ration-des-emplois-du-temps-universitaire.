# Les variable ******************************************************************
les_emploi = []
w = 3
jump = w//2
possibilities = [[0]*w for i in range(w)]
matieres = {}
profs = {}
dispo_prof = [[0]*w for i in range(w)]
nbsal =int(input('donner le nombre des salles : '))
nb_seance = 0
def saisir_matieres(matdic):
    for i in range(3):
        mat=input('donner une matiere : ')
        keynmb=int(input('donner le nombre 1 2 3 : '))
        matdic[mat]=keynmb
        global nb_seance
        if keynmb == 1:
            nb_seance += 1
        else:
            nb_seance += 2
saisir_matieres(matieres)
def sais_prof_disp(profname):
    m = [[0] * w for i in range(w)]
    for i in range(w):
        for j in range(w):
            if j == jump:
                continue
            m[i][j] = int(input("Entrer l'elememt : dispo_%s[%d][%d] = " %(profname, i, j)))
    return m
def saisir_prof(dicprof):
    for i in range(3):
        mat = input('donner un prof : ')
        dicprof[mat] = [(input('ses matieres : ')).split(" "), sais_prof_disp(mat)]
saisir_prof(profs)
# traitement ************************************************************************
def trait_possiiblities(possibl):
    for i in range(w):
        for j in range(w):
            if j == jump:
                continue
            list=[0]
            if nbsal > 0:
                for k in matieres.keys():
                    for l in profs.keys():
                        if (k in profs[l][0]) and profs[l][1][i][j] == 1:
                            list.append(k)
            possibl[i][j]=list.copy()
trait_possiiblities(possibilities)
print(possibilities)
def verif(m,matt,a,c):
    n = 0
    for i in range(w):
        for j in range(w):
            if j == jump:
                continue
            if m[i][j] == matt:
                n += 1
                b=i
    if n == 0 :
        return 1
    if n == 1 and matieres[matt] == 2 and b == a and (c-1) > 0 and m[b][c-1] == matt :
        return 1
    if n==1 and  matieres[matt] == 3 and b != a :
        return 1
    if matt == 0:
        return 1
    return 0
def compt(m):
    n = 0
    for i in range(w):
        for j in range(w):
            if j == jump:
                continue
            if m[i][j] == 0:
                n += 1
    return n
def print_emploi(m):
    for i in range(w):
        for j in range(w):
            if j == jump:
                continue
            print(m[i][j],end='\t')
        print()
def initializ(tab,i,j):
    for k in range(i,3):
        for l in range(j,3):
            tab[k][l]=0
def une_possibilete(les_poss):
    isbreak = 1
    la_possibilite = [[0]*w for i in range(w)]
    for i1 in les_poss[0][0]:
        initializ(la_possibilite,0,0)
        if isbreak == 0:
            break
        if verif(la_possibilite, i1, 0, 0) == 0:
            continue
        la_possibilite[0][0] = i1
        for i2 in les_poss[0][2]:
            initializ(la_possibilite, 0, 2)
            if isbreak == 0:
                break
            if verif(la_possibilite, i2, 0, 2) == 0:
                continue
            la_possibilite[0][2] = i2
            for i3 in les_poss[1][0]:
                initializ(la_possibilite,1,0)
                if isbreak == 0:
                    break
                if verif(la_possibilite, i3, 1, 0) == 0:
                    continue
                la_possibilite[1][0] = i3
                for i4 in les_poss[1][2]:
                    initializ(la_possibilite,1,2)
                    if isbreak == 0:
                        break
                    if verif(la_possibilite, i4, 1, 2) == 0:
                        continue
                    la_possibilite[1][2] = i4
                    for i5 in les_poss[2][0]:
                        initializ(la_possibilite,2,0)
                        if isbreak == 0:
                            break
                        if verif(la_possibilite, i5, 2, 0) == 0:
                            continue
                        la_possibilite[2][0] = i5
                        for i6 in les_poss[2][2]:
                            initializ(la_possibilite,2,2)
                            if isbreak == 0:
                                break
                            if verif(la_possibilite, i6, 2, 2) == 0:
                                continue
                            la_possibilite[2][2] = i6
                            if compt(la_possibilite) == 2:
                                print_emploi(la_possibilite)
                                isbreak = int(input("pour arretez entrez : 0 : "))
                                if isbreak != 0:
                                    les_emploi.append(la_possibilite)
une_possibilete(possibilities)