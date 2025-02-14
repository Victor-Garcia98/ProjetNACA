import numpy as np
import matplotlib.pyplot as plot


def naca():

    """Entrée utilisateur""" # Question 1

    flag_regles=input("Le code qui suit trace le profil d'une aile de type NACA00XX et retourne son épaisseur maximale"
                      " et la position de celle ci \n(pressez une touche pour continuer) ")

    num_naca = input("\n\nEntrez le numéro du profil NACA à 4 chiffres sous la forme 00XX : ")

    c = float(input("Entrez la corde du profil en metres : "))

    points = int(input("Entrez le nombre de points désirés pour le graphique : "))

    distribution = input("Selon quel type de distribution des points faut il tracer le graphique ? "
                         "(lineaire (l) / non uniforme (nu)) : ")
    t = int(num_naca[2:]) / 100

    """Distribution des points et construction des tableaux de coordonnées""" # Question 2

    if distribution == "nu" : # non uniforme
        theta = np.linspace(0, np.pi, points)
        xc = 0.5 * (1 - np.cos(theta))
    else : # linéaire
        xc = np.linspace(0, 1, points)
    yt = 5 * t * ( 0.2969 * np.sqrt(xc) - 0.1260 * xc - 0.3516 * xc ** 2 + 0.2843 * xc ** 3 - 0.1036 * xc ** 4)
    (x_up, x_down) = (xc * c, xc * c)
    (y_up, y_down) = (yt * c, -yt * c)

    """Trouver et afficher l'épaisseur maximale et sa position""" # Question 3

    max_epaisseur = np.max(yt * c)
    pos_max_epaisseur = xc[np.argmax(yt)] * c
    print(f"\nÉpaisseur maximale {max_epaisseur} m , Position {pos_max_epaisseur} m")

    """ Tracé du graphique """ # Question 4

    plot.plot(x_up, y_up, label="Extrados", color='r')
    plot.plot(x_down, y_down, label="Intrados", color='b')
    plot.xlabel("Position le long de la corde [m]")
    plot.ylabel("Epaisseur [m]")
    plot.title(f"Profil NACA {num_naca}")
    plot.legend()
    plot.grid()
    plot.axis("equal") # force l'égalité des échelles pour respecter la forme du profil
    plot.show()


naca()