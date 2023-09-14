import jarre_jeu

print('bienvenue dans le monde des minis jeux')
jeu = 0
x = 1
play = True

while play:

    while jeu != x:
        jeu = int(input("Choissiez votre jeu :"
                        "jeu des jarres : 1"))

    if jeu == 1:
        jarre_jeu.jeu_des_jarres()
    else:
        None

    print("play again ? ou autre mini jeu "
          "si oui entrez yes sinon entrez no")
    rep = str(input())
    while rep != ("yes" or "no"):
        print("play again ? ou autre mini jeu "
              "si oui entrez yes sinon entrez no")
        rep = str(input())
    if rep == "yes":
        play = True
    else:
        print('merci d avoir jouer ')
        play = False
