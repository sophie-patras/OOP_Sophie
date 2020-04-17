# marqueurs.py

#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys


class Marqueurs:

	def __init__(self, idt, ville, position):
		"""
          		id: Nom indique sur la carte
		"""

		self.idt=idt
		self.ville=ville
		self.position=position

	def getId(self):
        	return self.idt


class Individu(Marqueurs):
    
	def __init__(self,idt, ville, position, age, transport):

	        """ 
		    age - int
                    transport: moyen de transport prefere - string
	        """
        	self.idt=idt
		self.ville=ville
		self.position=position
		self.age=age
 	        self.transport=transport


class Commerce(Marqueurs):

	def __init__(self, idt, ville, position, ouverture, acces):

	        """ ouverture - booleen
                    acces : acces preferentiel entre pieton, velo, bus, voiture - 			    string
		"""
		self.idt=idt
		self.ville=ville
		self.position=position
        	self.ouverture=ouverture
        	self.acces=acces

	def boolOuverture(self):
		"""
		   Cette methode ne marche pas
		   
		   convertir ouverture en boolen...la methode ne modifie pas la valeur 			   d'ouverture en fait, setattr n est pas exactement adapte
		"""
		x=self.ouverture
		if x == 'ouvert':
			print "Le commerce est ouvert"
			return True
		else:
			print "Le commerce est ferme"
			return False


	def getDistance(self,positionbis):
		"""
		positionbis= position
		getDistance renvoie la distance entre deux positions lorsque 			l'individu parcourt les lignes d'une grille fictive
        	"""

		dx=abs(self.position[0]-positionbis[0])
		dy=abs(self.position[1]-positionbis[1])
		distance=dx+dy
		return distance


	def __str__(self):
	        return "<distance: %d>" % self.getDistance(self, positionbis)

        def __repr__(self):
	        return str(self)
                          

#jean=Individu('Jean','Nice',(1,1),22,'velo')
#boulangerie=Commerce('Boulangerie','Nice',(8,4),'ouvert','velo')

#print(boulangerie.ouverture)
#boulangerie.boolOuverture

#x=boulangerie.getDistance(jean.position)

#print(x)
