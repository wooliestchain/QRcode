#Import Library
import qrcode
import colorama
import sklearn
import random
from tkinter import *
#Generate QR Code
def code():
    a = ['Abassi', 'Ayed', 'Azzabi', 'Fadhel', 'Fellous',
         'Fitoussi', 'Mzali', 'Najar', 'Slim', 'Bouazizi', 'Ben Salem',
         'Ben Romdane', 'Ben yedder',
         'Ached', 'Ben Assile', 'Zbidi', 'Snaidi', 'Fraj',
         'Labidi', 'Chaabani', 'Sfar', 'Triki', 'Trabelsi', 'Rtibi',
         'Grid', 'Bouali', 'Ahmdi', 'Kabouvhi']
    a = random.choice(a)

    b = ['Marwa', 'Asma', 'Sonia', 'Hajer', 'Khawla', 'Emna', 'Basma', 'Asna', 'Warda', 'Houda', 'Wided', 'Hafsa',
         'Feriel', 'Rafika', 'Fatine',
         'Dalel', 'Hedia', 'Medina',
         'Nesrine', 'Mohamed', 'Afhed', 'Amine', 'Nabil', 'Amidou', 'Moussa', 'Aziz', 'Arsalene',
         'Heickel', 'Rayen', 'Sabri', 'Majdi', 'Slim',
         'Mahdi', 'Ziyed', 'Nader', 'Ayoub', 'Hamma', 'jawher', 'Moctar', 'Omar']
    b = random.choice(b)
    if b == 'Marwa' or b == 'Asma' or b == 'Sonia' or b == 'Hajer' \
            or b == 'Khawla' or b == 'Emna' or b == 'Basma' or b == 'Asna' or b == 'Warda' \
            or b == 'Wided' or b == 'Houda' or b == 'Hafsa' or b == 'Feriel' or b == 'Rafika' or b == 'Fatine' \
            or b == 'Dalel' or b == 'Hedia' or b == 'Medina' or b == 'Nesrine':
        genre = "Féminin"
        print(genre)

    if b == 'Mohamed' or b == 'Afhed' or b == 'Amine' or b == 'Nabil' \
            or b == 'Amidou' or b == 'Moussa' or b == 'Aziz' or b == 'Arsalene' \
            or b == 'Heickel' or b == 'Rayen' or b == 'Sabri' or b == 'Sabri' or \
            b == 'Majdi' or b == 'Slim' or b == 'Mahdi' or b == 'Ziyed' or b == 'Nader' \
            or b == 'Ayoub' or b == 'Hamma' or b == 'Jawher' or b == 'Moctar' or b == 'Omar':
        genre = "Masculin"
        print(genre)

    k = [100, 110, 127]
    k = random.choice(k)
    if k == 100:
        n = "Compte epargne en dinars"

    elif k == 110:
        n = "Compte epargne pour les tunisiens residents a l'etranger"


    elif k == 127:
        n = "Compte en dinars convertible"

    clef = random.randint(10,100)
    x = random.randint(12345678, 123456789)
    c1 = [1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967,
          1968,
          1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1985, 1986, 1987,
          1988, 1989,
          1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007,
          2008, 2009, 2010]
    c1 = random.choice(c1)
    c2 = ['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre',
          'Décembre']
    c2 = random.choice(c2)
    c3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
          31]
    c3 = random.choice(c3)
    c = c3, c2, c1

    d=['Tuins', 'Sfax', 'Sousse', 'Hammamet', 'Tataouine', 'Siliana', 'Kasserine', 'Zarzis', 'Kairouan','Tozeur', 'Madiha','Djenouba',
       'Gabes', 'Bizerte', 'Monastir', 'Nabeul', 'Tabarka', 'Le Kef', 'Douz']
    d = random.choice(d)
    e= ['Tuins', 'Sfax', 'Sousse', 'Hammamet', 'Tataouine', 'Siliana', 'Kasserine', 'Zarzis', 'Kairouan','Tozeur', 'Madiha','Djenouba',
       'Gabes', 'Bizerte', 'Monastir', 'Nabeul', 'Tabarka', 'Le Kef', 'Douz']
    e = random.choice(e)

    bp = ['Medh v', 'Sfax', 'Tunis centre', 'Soukra', 'Ariana','Hmmamet', 'Sousse ville', 'Sousse village', 'Le Kram', 'Beja', 'Kassrine', 'Siliana', 'Aouina', '']
    bp = random.choice(bp)

    dict = {"nom": a, "prenom": b,"Sexe": genre, "Type": k, "Clef": clef, "Numéro de compte": x,"Nature du compte": n,
            "date de naissance": c, "Lieu de naissance": d, "Adresse": e,
            "Bureau de poste": bp}
    img=qrcode.make(dict)

    img.save('test3.png')

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data("https://my.poste.tn/")
    qr.make(fit=True)
    img = qr.make_image(fill_color="white", back_color="blue")
    img.save("medium.png")

    print("Nom du client: ", a, "\nPrénom du client: ", b, "\nSexe : ", genre, "\nType de compte :", k, "\nNature du compte: ", n, "\nClef : ", clef,
          "\nNuméro de compte: ", x, "\nDate de naissance: ", c
          , "\nLieu de naissance: ", d, "\nAdresse :", e, "\nBureau de poste :", bp)



    def infos():
        s = random.randint(1, 10000)
        print("Solde :", s)
        if c1 > 1995 :
            m = "Célibataire"
        elif c1 < 1995 :
            m = ['Marié', 'Célibataire']
            m = random.choice(m)
        print("Situation matrimonialle :", m)
        if c1 <= 2004 :
            civil = "Majeur"
            print("Cvilité :",civil)
        if c1 > 2004 :
            civil = "Mineur"
            print("Civilité :",civil)
        p = ['Versement', 'Retrait', 'Consultaion']
        p = random.choice(p)
        print("Derniére Opération : ", p)
        s1 = random.randint(1, 1000)
        if p == 'Versement':
            print("Montant de l'opération: +", s1)
            s = s + s1
            print("Solde du compte: ", s)

        if p == 'Retrait':
            s1 <= s
            print("Montant de l'opération: -", s1)
            s = s - s1
            print("Solde du compte : ", s)

        if p == 'Consultation':
            print("Solde du compte: ", s)
        code()

    def modifNom():
        a = ['Abassi', 'Ayed', 'Azzabi', 'Fadhel', 'Fellous', 'Fitoussi', 'Mzali', 'Najar', 'Slim', 'Bouazizi',
             'Ben Salem', 'Ben Romdane', 'Ben yedder',
             'Ached', 'Ben Assile', 'Zbidi', 'Snaidi', 'Fraj', 'Labidi', 'Chaabani', 'Sfar', 'Triki', 'Trabelsi',
             'Rtibi', 'Grid', 'Bouali', 'Ahmdi', 'Kabouvhi']

        a = random.choice(a)
        a1 = input("Entrer le nom souhaité : ")
        a = a1
        dict = {"nom": a, "prenom": b, "Sexe": genre, "Type": k, "Clef": clef, "Numéro de compte": x,
                "Nature du compte": n, "date de naissance": c, "Lieu de naissance": d, "Adresse": e,
                "Bureau de poste": bp}
        print(dict)
        img = qrcode.make(dict)

        img.save('test3.png')
        Modif()
    def mofifPrenom():
        b = ['Marwa', 'Asma', 'Sonia', 'Hajer', 'Khawla', 'Emna', 'Basma', 'Asna', 'Warda', 'Houda', 'Wided', 'Hafsa',
             'Feriel', 'Rafika', 'Fatine', 'Dalel', 'Hedia', 'Medina',
             'Nesrine', 'Mohamed', 'Afhed', 'Amine', 'Nabil', 'Amidou', 'Moussa', 'Aziz', 'Arsalene', 'Heickel',
             'Rayen', 'Sabri', 'Majdi', 'Slim',
             'Mahdi', 'Ziyed', 'Nader', 'Ayoub', 'Hamma', 'jawher', 'Moctar', 'Omar']
        b = random.choice(b)
        b1 = input("Entrer le prénom: ")
        b = b1
        dict = {"nom": a, "prenom": b, "Sexe": genre, "Type": k, "Clef": clef, "Numéro de compte": x,
                "Nature du compte": n, "date de naissance": c, "Lieu de naissance": d, "Adresse": e,
                "Bureau de poste": bp}
        print(dict)
        img = qrcode.make(dict)

        img.save('test3.png')
        Modif()
        print("Nom du client: ", a, "\nPrénom du client: ", b, "\nSexe : ", genre, "\nType de compte :", k,
              "\nNature du compte: ", n, "\nClef : ", clef,
              "\nNuméro de compte: ", x, "\nDate de naissance: ", c
              , "\nLieu de naissance: ", d, "\nAdresse :", e, "\nBureau de poste :", bp)

    def modifGenre():
        genre1 = input("Entrer le genre: ")
        genre = genre1
        dict = {"nom": a, "prenom": b, "Sexe": genre, "Type": k, "Clef": clef, "Numéro de compte": x,
                "Nature du compte": n, "date de naissance": c, "Lieu de naissance": d, "Adresse": e,
                "Bureau de poste": bp}
        print(dict)
        img = qrcode.make(dict)

        img.save('test3.png')
        Modif()
    def modifType():
        k1 = input("Entrer le type du compte")
        if k1 == 100:
            n = "Compte epargne en dinars"
            k = k1

        elif k1 == 110:
            n = "Compte epargne pour les tunisiens residents a l'etranger"
            k = k1

        elif k1 == 127:
            n = "Compte en dinars convertible"
            k = k1
        dict = {"nom": a, "prenom": b, "Sexe": genre, "Type": k, "Clef": clef, "Numéro de compte": x,
                "Nature du compte": n, "date de naissance": c, "Lieu de naissance": d, "Adresse": e,
                "Bureau de poste": bp}
        print(dict)
        img = qrcode.make(dict)

        img.save('test3.png')
        Modif()

    def modifClef():
        clef1 = int(input("Entrer la clef: "))
        clef = clef1

        dict = {"nom": a, "prenom": b, "Sexe": genre, "Type": k, "Clef": clef, "Numéro de compte": x,
                "Nature du compte": n, "date de naissance": c, "Lieu de naissance": d, "Adresse": e,
                "Bureau de poste": bp}
        print(dict)
        img = qrcode.make(dict)

        img.save('test3.png')
        Modif()

    def modifNumerocompte():
        x1 = int(input("Entrer le numéro de compte: "))
        x = x1
        dict = {"nom": a, "prenom": b, "Sexe": genre, "Type": k, "Clef": clef, "Numéro de compte": x,
                    "Nature du compte": n, "date de naissance": c, "Lieu de naissance": d, "Adresse": e,
                    "Bureau de poste": bp}
        print(dict)
        img = qrcode.make(dict)

        img.save('test3.png')
        Modif()

    def modifDatenaissance():
        c6 = input("Entrer la date de naissance: ")
        c = c6
        dict = {"nom": a, "prenom": b, "Sexe": genre, "Type": k, "Clef": clef, "Numéro de compte": x,
                    "Nature du compte": n, "date de naissance": c, "Lieu de naissance": d, "Adresse": e,
                    "Bureau de poste": bp}
        print(dict)
        img = qrcode.make(dict)

        img.save('test3.png')
        Modif()

    def modifLieunaissance():
        d1 = input("Entrer le lieu de naissance: ")
        d = d1
        dict = {"nom": a, "prenom": b, "Sexe": genre, "Type": k, "Clef": clef, "Numéro de compte": x,
                    "Nature du compte": n, "date de naissance": c, "Lieu de naissance": d, "Adresse": e,
                    "Bureau de poste": bp}
        print(dict)
        img = qrcode.make(dict)

        img.save('test3.png')
        Modif()

    def modifAdress():
        e1 = input("Entrer l'adresse: ")
        e = e1
        dict = {"nom": a, "prenom": b, "Sexe": genre, "Type": k, "Clef": clef, "Numéro de compte": x,
                    "Nature du compte": n, "date de naissance": c, "Lieu de naissance": d, "Adresse": e,
                    "Bureau de poste": bp}
        print(dict)
        img = qrcode.make(dict)

        img.save('test3.png')
        Modif()

    def modifBureau():
        bp1 = input("Entrer le bureau de poste: ")
        bp = bp1
        dict = {"nom": a, "prenom": b, "Sexe": genre, "Type": k, "Clef": clef, "Numéro de compte": x,
                    "Nature du compte": n, "date de naissance": c, "Lieu de naissance": d, "Adresse": e,
                    "Bureau de poste": bp}
        print(dict)
        img = qrcode.make(dict)

        img.save('test3.png')
        Modif()


    def Modif():
        print('''
        1.Modifier le nom
        2.Modifier le prénom
        3.Modifier le genre
        4.Modifier la type
        5.Modifier la clef
        6.Modifier le numéro
        7.Modifier la date de naissance
        8.Modifier lieu de naissancz
        9.Modifier l'adresse
        10.Modifer le bureau de poste
        11.Retourner au menu principal''')
        choice = input("Quelle information souhaitez vous modifier? :")
        if ( choice == 'nom' or choice == 'NOM' or choice == 'Nom' or choice == '1'):
            modifNom()


        if (choice == 'prénom' or choice == 'Prénom' or choice == 'PRENOM' or choice == '2'):
            mofifPrenom()

        if (choice == 'genre' or choice == 'Genre' or choice == 'GENRE' or choice == '3'):
            modifGenre()
        if (choice == 'type' or choice == 'Type' or choice == 'TYPE' or choice == '4'):
            modifType()
        if (choice == 'clef' or choice == 'Clef' or choice == 'CLEF' or choice == '5'):
            modifClef()
        if (choice == 'Numéro de compte' or choice == 'numéro de compte' or choice == 'NUMERO DE COMPTE' or choice == '6'):
            modifNumerocompte()
        if (choice == 'date de naissance' or choice == 'Date de Naissance' or choice == 'DATE DE NAISSANCE' or choice == '7'):
            modifDatenaissance()
        if (choice == 'lieu de naissance' or choice == 'Lieu de Naissance' or choice == 'LIEU DE NAISSANCE' or choice == '8'):
            modifLieunaissance()
        if (choice == 'adresse' or choice == 'Adresse' or choice == 'ADRESSE' or choice == '9'):
            modifAdress()
        if (choice == 'bureau de poste' or choice == 'BUREAU DE POSTE' or choice == 'Bureau de Poste' or choice == '10'):
            modifBureau()
        if (choice == 'aucune' or choice== 'Aucune' or choice == 'AUCUNE' or choice == '11'):
            code()








    print('''
        1.Afficher les informations du compte 
        2.Modifier les informations
        3.Quitter''')
    choix = input("Executer une tâche: ")
    if (choix == '1'):
        infos()
    elif (choix == '2'):
        Modif()
    elif (choix == '3'):
        print("Deconnecion")





code()