import random
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
import numpy

#Définit ce qu'est un joueur
class Joueur :
    def __init__(self,health,attack,speed,name,attaques={}):
        self.health = health
        self.attack = attack
        self.speed = speed
        self.name = name
        self.attaques = attaques

#Création d'une liste avec les classes possibles du bot --> retirer celle que le joueur choisira 
classe_bot = ['guerrier', 'mage', 'archer', 'ninja']

#Création de tableaux vides pour avoir les PV des joueurs par tour
pv_bot = []
pv_joueur = []
tours = []

#Création de tableaux --> précision des attaques
précision_ninja = ['85%', '100%', '100%']
précision_autres = ['80%', '70%', '100%']

#Création de dictionnaires --> attaques|classes
attaques_guerrier = {'Coup D Epée': 5 , 'Poing Destructeur': 6, 'Soin': 5}
attaques_mage = {'Abracadabra': 7 , 'Sortilège': 8, 'Soin': 10}
attaques_archer = {'Flèche Enflammée': 10 , 'Triple Flèche': 11, 'Soin': 5}
attaques_ninja = {'Shurikens': 15 , 'Fumée De Ninja': 7, 'Soin': 5}

#Fonction d'attribution des statistiques en fonction de la classe choisie
def classe_de_combat(plyr,k):
    if k.lower()=='guerrier' :
        plyr.health=100
        plyr.attack=30
        plyr.speed=25
        if plyr == joueur:
            plyr.name+=' le guerrier'
        classe_bot.remove('guerrier')
        plyr.attaques = attaques_guerrier
        
    if k.lower()=='mage' :
        plyr.health=85
        plyr.attack=35
        plyr.speed=30
        if plyr==joueur:
            plyr.name+=' le mage'
        classe_bot.remove('mage')
        plyr.attaques = attaques_mage
        
    if k.lower()=='archer' :
        plyr.health=60
        plyr.attack=45
        plyr.speed=35
        if plyr==joueur:
            plyr.name+=' l\'archer'
        classe_bot.remove('archer')
        plyr.attaques = attaques_archer
        
    if k.lower()=='ninja' :
        plyr.health=40
        plyr.attack=50
        plyr.speed=40
        if plyr==joueur:
            plyr.name+=' le ninja'
        classe_bot.remove('ninja')
        plyr.attaques = attaques_ninja
       
#Fonction qui attribue une classe de combattant a un 'Joueur'
def Classe_joueur(plyr):
    print(f'{espaces}Choisis une classe de combat {plyr.name} : ')
    print('=========================================================')
    print('  Guerrier     |  Health : 100  Attack : 30  Speed : 25  ')
    print('  Mage         |  Health : 85   Attack : 35  Speed : 30  ')
    print('  Archer       |  Health : 60   Attack : 45  Speed : 35  ')
    print('  Ninja        |  Health : 40   Attack : 50  Speed : 40  ')
    print('=========================================================')
    k=str(input(f'Alors {plyr.name}, quelle classe choisis-tu : '))
    classe_de_combat(plyr,k)
    
#Set up du début du jeu --> message de bienvenue + création du joueur
print('Bienvenue dans un jeu de combat au tour par tour !')
print('')
l=str(input('Quel est ton nom jeune aventurier : '))
print('')
a=(26-len(l))/2
espaces = " " * int(a)
joueur = Joueur(0,0,0,l.title())
Classe_joueur(joueur)

#Création du bot
noms_bot = [
    "Dr Doom",
    "Magneto",
    "Lex Luthor",
    "Joker",
    "Darkseid",
    "Galactus",
    "Ra's al Ghul",
    "Méphisto",
    "Thanos",
    "Le Goblin Vert"
]
bot = Joueur(0,0,0,random.choice(noms_bot))
zz=random.choice(classe_bot)
classe_de_combat(bot, zz)
print(f'Ton ennemi s\'appelle {bot.name} et il a choisi la classe {zz}.')
key, value = list(joueur.attaques.items())[0]

#Def d'un tour de joueur
def tour_joueur():
        print(f'Tu as {joueur.health} points de vie. {bot.name} en a {bot.health}.')
        print(f'Que veux-tu faire :')
        print('')
        urss = 1
        if 'Shurikens' in joueur.attaques.keys():
            for attaquees, valeurs, éléments in zip(joueur.attaques.keys(), joueur.attaques.values(), précision_ninja):
                max_key = max(joueur.attaques, key=lambda uu: len(uu))
                longueur =  (len(max_key) + 3)- len(attaquees)
                longueur_ = ' ' * longueur
                longueur_v2 =' ' * (3 - len(str(valeurs)))
                print(f' {urss}) {attaquees} :{longueur_}{valeurs}{longueur_v2}|  Précision : {éléments} ')
                urss +=1
            print('')
        else :
            for attaquees, valeurs, éléments in zip(joueur.attaques.keys(), joueur.attaques.values(), précision_autres):
                max_key = max(joueur.attaques, key=lambda uu: len(uu))
                longueur = (len(max_key) + 3) - len(attaquees)
                longueur_ = ' ' * longueur
                longueur_v2 =' ' * (3 - len(str(valeurs)))
                print(f' {urss}) {attaquees} :{longueur_}{valeurs}{longueur_v2}|  Précision : {éléments} ')
                urss +=1
            print('')

        n = input(f'Alors {joueur.name}, que choisis-tu de faire : ')
        if n.lower()=='soin':
            if (joueur.health + joueur.attaques['Soin']) - joueur.attaques['Soin'] > pv_joueur[0]:
                joueur.health += pv_joueur[0] - joueur.health
            else:
                joueur.health += joueur.attaques['Soin']
            print(f'{joueur.name}, tes points de vie sont maintenant de {joueur.health}') 
        if n.lower()=='shurikens':
            z=random.randint(1,100)
            if z < 86:
                bot.health -= 15
                print(f'Les PV de {bot.name} sont maintenant de {bot.health}.')
            if z > 85 and z < 97:
                print('OH NON L\'ATTAQUE À ECHOUE !!')
            if z > 96:
                print('OH NON, L\'ATTAQUE À ECHOUE : TU T\'ES INFLIGE DES DEGATS !!!')
                joueur.health -= 15
                print(f'{joueur.name}, Tes PV sont maintenant de {joueur.health}.')
        elif n.lower()=='fumée de ninja':
            joueur.speed += 7
        else:
            bb = random.randint(1,100)
            if n.title()=='Coup d\'épée' or joueur.attaques[n.title()]==7 or joueur.attaques[n.title()]==10 and n.title() != 'Soin':
                if bb < 80:
                    bot.health -= joueur.attaques[n.title()]
                    print(f'Les PV de {bot.name} sont maintenant de {bot.health}')
                if bb > 79 and bb < 95:
                    print('L\'ATTAQUE À ECHOUE !!!')
                if bb > 94:
                    print('OH NON, L\'ATTAQUE À ECHOUE : TU T\'ES INFLIGE DES DEGÂTS !!!')
                    joueur.health -= joueur.attaques[n.title()]
            if joueur.attaques[n.title()]==6 or joueur.attaques[n.title()]==8 or joueur.attaques[n.title()]==11 :
                if bb < 70:
                    bot.health -= joueur.attaques[n.title()]
                    print(f'Les PV de {bot.name} sont maintenant de {bot.health}')
                if bb > 69 and bb <95:
                    print('L\'ATTAQUE A ECHOUE !!!')
                if bb > 94:
                    print('OH NON, L\'ATTAQUE A ECHOUE : TU T\'ES INFLIGE DES DEGÂTS !!')
                    joueur.health -= joueur.attaques[n.title()]

#Def d'un tour d'un bot
def tour_bot():
    abcd = 0
    if bot.health < 15:
        bot.health += bot.attaques['Soin']
        print(f'{bot.name} a utilisé l\'attaque Soin.')
        abcd += 1
    keys_copy = list(bot.attaques.keys())[:-1]
    if bot.health > 14 and abcd != 1:
        k=random.choice(list(keys_copy))
        if k=='Shurikens':
            z=random.randint(1,100)
            if z < 86:
                bot.health -= 15
                print(f'Les PV de {bot.name} sont maintenant de {bot.health}.')
            if z > 85 and z < 97:
                print('OH NON L\'ATTAQUE À ECHOUE !!')
            if z > 96:
                print('OH NON, L\'ATTAQUE À ECHOUE : IL S\'EST INFLIGE DES DEGATS !!!')
                bot.health -= 15
                print(f'Les PV de {bot.name} sont maintenant de {bot.health}.')
        elif k=='Fumée De Ninja':
            bot.speed += 7
            print(f'{bot.name} a utilisé l\'attaque fumée de ninja. Sa vitesse est maintenant de {bot.speed}')
        else:
            bb = random.randint(1,100)
            if k=='Coup d\'épée' or bot.attaques[k]==7 or k =='Flèche Enflammée' and k !='Soin' :
                if bb < 80:
                    joueur.health -= bot.attaques[k]
                    print(f'{bot.name} a utilisé l\'attaque {k}')
                if bb > 79 and bb < 95:
                    print(f'L\'ATTAQUE DE {bot.name} À ECHOUE !!!')
                if bb > 94:
                    print(f'OH NON, L\'ATTAQUE DE {bot.name} À ECHOUE : IL S\'EST INFLIGE DES DEGÂTS !!!')
                    bot.health -= bot.attaques[k]
            if bot.attaques[k]==6 or bot.attaques[k]==8 or bot.attaques[k]==11 :
                if bb < 70:
                    joueur.health -= bot.attaques[k]
                    print(f'{bot.name} a utilisé l\'attaque {k}')
                    print(f'{joueur.name}, tes PV sont maintenant de {joueur.health}.')
                if bb > 69 and bb <95:
                    print(f'L\'ATTAQUE DE {bot.name} A ECHOUE !!!')
                if bb > 94:
                    print(f'OH NON, L\'ATTAQUE DE {bot.name} A ECHOUE : IL S\'EST INFLIGE DES DEGÂTS !!')
                    joueur.health -= bot.attaques[k]

#Fonction d'un tour du fight
def Tour(premier):
    if premier == joueur:
        tour_joueur()
        if bot.health > 0:
            tour_bot()
            
    if premier == bot:
        tour_bot()
        if joueur.health > 0 :
            tour_joueur()
                  

# Fonction qui définit qui attaque en premier et joue un tour
def Vrai_tour():
    print('') 
    print(f'----------Tour {tour}----------')
    print('')
    a = random.randint(1, joueur.speed + bot.speed)
    if a > (joueur.speed-1) and joueur.health > 0 and bot.health > 0 :
        Tour(bot)
    if a < joueur.speed and joueur.health > 0 and bot.health > 0 :
        Tour(joueur)

#Boucle principale du jeu
tour = 1
while joueur.health > 0 and bot.health > 0 :
    tours.append(tour)
    pv_bot.append(bot.health)
    pv_joueur.append(joueur.health)
    Vrai_tour()
    tour += 1
    
#Définition du vainqueur
if joueur.health < 0:
    print('')
    elementations = ' ' * (36 - len(bot.name))
    print('=========================================================')
    print(f'{elementations}{bot.name} a gagné le combat !!!')
    print('              Malheureuement tu as perdu :(              ')
    print('=========================================================')
if bot.health < 0:
    elementation = ' ' * (24 - len(joueur.name))/2 
    print('')
    print('=========================================================')
    print(f'{elementation}Bravo {joueur.name}, tu as gagné le combat !!!')
    print('=========================================================')

#Bilan de la  partie
print('')
print('')
tour_= 1
print('Faisons un petit résumé des PV par tour :')
print(f'          {joueur.name}      {bot.name}  ')

uk = " "
len_name=len(joueur.name)
len_bot=len(bot.name)

for elements_1, elements_2 in zip(pv_joueur, pv_bot):
      len_el1 = len(str(elements_1))
      len_el2 = len(str(elements_2))
      truc_1 = (len(joueur.name) - len_el1)/2
      truc_2 = (len(bot.name) - len_el2)/2
      truc_utile1 = uk * int(truc_1)
      truc_utile2 = uk * int(truc_2)
      zzz = 4 - len(str(tour_))
      zzzz = ' ' * zzz
      print(f'Tour {tour_}{zzzz}| {truc_utile1}{elements_1}{truc_utile1}      {truc_utile2}{elements_2}')
      tour_ += 1
        
# Plot the data
plt.plot(tours, pv_joueur, label= joueur.name)
plt.plot(tours, pv_bot, label=bot.name)

# Add labels and title
plt.xlabel('Tour')
plt.ylabel('PV')
plt.title('PV des joueurs en fonction du tour')

# Add a legend
plt.legend()

# Show the plot
plt.show()