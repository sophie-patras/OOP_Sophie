# distance.py


""""Ligne de commande : python distance.py"""

"""
Une fonction qui prend en parametre deux objets, un Individu et un Commerce. Lafonction precise en fonction des caracteristiques de l'individu et du commerce si le lieu est atteignable.Les criteres sont : l'age,la distance entre les deuxpositions
"""

import marqueurs


def distance(resident, commerce):

     """ resident : marqueur.Individu
         commerce : marqueur.Commerce """ 

     if not commerce.boolOuverture:
		return False

     d=commerce.getDistance(resident.position)

     if d>5:
          if resident.age>80:
               print "Ce commerce est un peu trop distant pour vous"
               return False
          print "C'est mieux avec un velo"

     print  "Le commerce est a", d, "km"
     return True
     
     

# Main Function
if __name__ == '__main__':
    
    jean=marqueurs.Individu('Jean','Nice',(1,1),22,'velo')
    boulangerie=marqueurs.Commerce('Boulangerie','Nice',(10,4),True,'velo')

    print jean.idt, "peut se rendre au lieu souhaite ?", distance(jean,boulangerie)
