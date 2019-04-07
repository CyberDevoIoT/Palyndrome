# -*- coding: utf-8 -*-

#==============================================================================#
# Name:         Palyndrômes
# Purpose: Calcul de nombres Palyndrômes
#------------------------------------------------------------------------------
# Author:      CyberDev
# Created:     Tue Feb  5 05:51:54 2019
# Copyright:   (c) CyberDev Tue Feb  5 05:51:54 2019
# Licence:     Pro And Perso                                                  
#==============================================================================#

#-------------------------------------------------#
#         Importation des modules externes        #
#-------------------------------------------------#


#-------------------------------------------------#
#            Définition des fonctions             #
#-------------------------------------------------#
def separateur():
	"""Cette fonction permet d'afficher un séparateur quand cela est nécessaire"""
	print("---------------------------------------------------------")
	
	

def afficher_palyndrome(nb_min, nb_max):
	"""Cette fonction permet de split le nombre pour permettre d'ajouter le nombre et son
	palyndrôme """
	for i in range(nb_min, (nb_max+1)):
		#on ajoute dans la liste nombre donné et on sépare chaque caractère
		afficher_calcul(i,i)


def afficher_calcul(nb, base):
	"""Cette fonction permet pour chaque nombre donné plus haut de calculer
	si il est un palyndrôme ou pas """
	nombre_split = list("".join(str(nb).split()))
	#print(nombre_split)
	global palyndromes
	global pb
	global non_palyndromes
	nb_renverse = 0
	nb_nombre_split = len(nombre_split)
	for j in range(0, nb_nombre_split):
		nb_j = int(nombre_split[j])
		if(nb_nombre_split==3):
			if(j==0):
				nb_renverse += nb_j
			elif(j==1):
				nb_renverse += nb_j*10
			elif(j==2):
				nb_renverse += nb_j*100
			else:
				print("Problème lors de la longueur du tableau du nombre ! nb_nombre_split : 3")
		elif(nb_nombre_split==4):
			if(j==0):
				nb_renverse += nb_j
			elif(j==1):
				nb_renverse += nb_j*10
			elif(j==2):
				nb_renverse += nb_j*100
			elif(j==3):
				nb_renverse += nb_j*1000
			else:
				print("Problème lors de la longueur du tableau du nombre ! nb_nombre_split : 4")
		elif(nb_nombre_split==5):
			if(j==0):
				nb_renverse += nb_j
			elif(j==1):
				nb_renverse += nb_j*10
			elif(j==2):
				nb_renverse += nb_j*100
			elif(j==3):
				nb_renverse += nb_j*1000
			elif(j==4):
				nb_renverse += nb_j*10000
			else:
				print("Problème lors de la longueur du tableau du nombre ! nb_nombre_split : 5")	
		elif(nb_nombre_split==6):
			if(j==0):
				nb_renverse += nb_j
			elif(j==1):
				nb_renverse += nb_j*10
			elif(j==2):
				nb_renverse += nb_j*100
			elif(j==3):
				nb_renverse += nb_j*1000
			elif(j==4):
				nb_renverse += nb_j*10000
			elif(j==5):
				nb_renverse += nb_j*100000
			else:
				print("Problème lors de la longueur du tableau du nombre ! nb_nombre_split : 6")
		elif(nb_nombre_split==7):
			if(j==0):
				nb_renverse += nb_j
			elif(j==1):
				nb_renverse += nb_j*10
			elif(j==2):
				nb_renverse += nb_j*100
			elif(j==3):
				nb_renverse += nb_j*1000
			elif(j==4):
				nb_renverse += nb_j*10000
			elif(j==5):
				nb_renverse += nb_j*100000
			elif(j==6):
				nb_renverse += nb_j*1000000
			else:
				print("Problème lors de la longueur du tableau du nombre ! nb_nombre_split : 7")
		elif(nb_nombre_split==8):
			if(j==0):
				nb_renverse += nb_j
			elif(j==1):
				nb_renverse += nb_j*10
			elif(j==2):
				nb_renverse += nb_j*100
			elif(j==3):
				nb_renverse += nb_j*1000
			elif(j==4):
				nb_renverse += nb_j*10000
			elif(j==5):
				nb_renverse += nb_j*100000
			elif(j==6):
				nb_renverse += nb_j*1000000
			elif(j==7):
				nb_renverse += nb_j*10000000
			else:
				print("Problème lors de la longueur du tableau du nombre ! nb_nombre_split : 8")
		elif(nb_nombre_split==9):
			if(j==0):
				nb_renverse += nb_j
			elif(j==1):
				nb_renverse += nb_j*10
			elif(j==2):
				nb_renverse += nb_j*100
			elif(j==3):
				nb_renverse += nb_j*1000
			elif(j==4):
				nb_renverse += nb_j*10000
			elif(j==5):
				nb_renverse += nb_j*100000
			elif(j==6):
				nb_renverse += nb_j*1000000
			elif(j==7):
				nb_renverse += nb_j*10000000
			elif(j==8):
				nb_renverse += nb_j*100000000
			else:
				print("Problème lors de la longueur du tableau du nombre ! nb_nombre_split : 9")
		elif(nb_nombre_split==10):
			if(j==0):
				nb_renverse += nb_j
			elif(j==1):
				nb_renverse += nb_j*10
			elif(j==2):
				nb_renverse += nb_j*100
			elif(j==3):
				nb_renverse += nb_j*1000
			elif(j==4):
				nb_renverse += nb_j*10000
			elif(j==5):
				nb_renverse += nb_j*100000
			elif(j==6):
				nb_renverse += nb_j*1000000
			elif(j==7):
				nb_renverse += nb_j*10000000
			elif(j==8):
				nb_renverse += nb_j*100000000
			elif(j==9):
				nb_renverse += nb_j*1000000000
			else:
				print("Problème lors de la longueur du tableau du nombre ! nb_nombre_split : 10")
		elif(nb_nombre_split==11):
			if(j==0):
				nb_renverse += nb_j
			elif(j==1):
				nb_renverse += nb_j*10
			elif(j==2):
				nb_renverse += nb_j*100
			elif(j==3):
				nb_renverse += nb_j*1000
			elif(j==4):
				nb_renverse += nb_j*10000
			elif(j==5):
				nb_renverse += nb_j*100000
			elif(j==6):
				nb_renverse += nb_j*1000000
			elif(j==7):
				nb_renverse += nb_j*10000000
			elif(j==8):
				nb_renverse += nb_j*100000000
			elif(j==9):
				nb_renverse += nb_j*1000000000
			elif(j==10):
				nb_renverse += nb_j*10000000000
			else:
				print("Problème lors de la longueur du tableau du nombre ! nb_nombre_split : 11")
	result = nb+nb_renverse
	print("Calcul de : " + str(nb) + " + " + str(nb_renverse) + " = " + str(result))
	list_result_renverse = list("".join(str(result).split()))
	#print(list_result_renverse)
	nb_list_result_renverse = len(list_result_renverse)
	for j in range(0, nb_list_result_renverse):
		nb_j = int(nombre_split[j-1])
		if(nb_list_result_renverse==3):
			if(j==0):
				nb_renverse_0 = int(list_result_renverse[j])
			elif(j==1):
				nb_renverse_1 = int(list_result_renverse[j])
			elif(j==2):
				nb_renverse_2 = int(list_result_renverse[j])
			else:
				print("Problème lors de la longueur du tableau du nombre ! nb_list_result_renverse : 3")
		elif(nb_list_result_renverse==4):
			if(j==0):
				nb_renverse_0 = int(list_result_renverse[j])
			elif(j==1):
				nb_renverse_1 = int(list_result_renverse[j])
			elif(j==2):
				nb_renverse_2 = int(list_result_renverse[j])
			elif(j==3):
				nb_renverse_3 = int(list_result_renverse[j])
			else:
				print("Problème lors de la longueur du tableau du nombre ! nb_list_result_renverse : 4")
		elif(nb_list_result_renverse==5):
			if(j==0):
				nb_renverse_0 = int(list_result_renverse[j])
			elif(j==1):
				nb_renverse_1 = int(list_result_renverse[j])
			elif(j==2):
				nb_renverse_2 = int(list_result_renverse[j])
			elif(j==3):
				nb_renverse_3 = int(list_result_renverse[j])
			elif(j==4):
				nb_renverse_4 = int(list_result_renverse[j])
			else:
				print("Problème lors de la longueur du tableau du nombre ! nb_list_result_renverse : 5")	
		elif(nb_list_result_renverse==6):
			if(j==0):
				nb_renverse_0 = int(list_result_renverse[j])
			elif(j==1):
				nb_renverse_1 = int(list_result_renverse[j])
			elif(j==2):
				nb_renverse_2 = int(list_result_renverse[j])
			elif(j==3):
				nb_renverse_3 = int(list_result_renverse[j])
			elif(j==4):
				nb_renverse_4 = int(list_result_renverse[j])
			elif(j==5):
				nb_renverse_5 = int(list_result_renverse[j])
			else:
				print("Problème lors de la longueur du tableau du nombre ! nb_list_result_renverse : 6")
		elif(nb_list_result_renverse==7):
			if(j==0):
				nb_renverse_0 = int(list_result_renverse[j])
			elif(j==1):
				nb_renverse_1 = int(list_result_renverse[j])
			elif(j==2):
				nb_renverse_2 = int(list_result_renverse[j])
			elif(j==3):
				nb_renverse_3 = int(list_result_renverse[j])
			elif(j==4):
				nb_renverse_4 = int(list_result_renverse[j])
			elif(j==5):
				nb_renverse_5 = int(list_result_renverse[j])
			elif(j==6):
				nb_renverse_6 = int(list_result_renverse[j])
			else:
				print("Problème lors de la longueur du tableau du nombre ! nb_list_result_renverse : 7")
		elif(nb_list_result_renverse==8):
			if(j==0):
				nb_renverse_0 = int(list_result_renverse[j])
			elif(j==1):
				nb_renverse_1 = int(list_result_renverse[j])
			elif(j==2):
				nb_renverse_2 = int(list_result_renverse[j])
			elif(j==3):
				nb_renverse_3 = int(list_result_renverse[j])
			elif(j==4):
				nb_renverse_4 = int(list_result_renverse[j])
			elif(j==5):
				nb_renverse_5 = int(list_result_renverse[j])
			elif(j==6):
				nb_renverse_6 = int(list_result_renverse[j])
			elif(j==7):
				nb_renverse_7 = int(list_result_renverse[j])
			else:
				print("Problème lors de la longueur du tableau du nombre ! nb_list_result_renverse : 8")
		elif(nb_list_result_renverse==9):
			if(j==0):
				nb_renverse_0 = int(list_result_renverse[j])
			elif(j==1):
				nb_renverse_1 = int(list_result_renverse[j])
			elif(j==2):
				nb_renverse_2 = int(list_result_renverse[j])
			elif(j==3):
				nb_renverse_3 = int(list_result_renverse[j])
			elif(j==4):
				nb_renverse_4 = int(list_result_renverse[j])
			elif(j==5):
				nb_renverse_5 = int(list_result_renverse[j])
			elif(j==6):
				nb_renverse_6 = int(list_result_renverse[j])
			elif(j==7):
				nb_renverse_7 = int(list_result_renverse[j])
			elif(j==8):
				nb_renverse_8 = int(list_result_renverse[j])
			else:
				print("Problème lors de la longueur du tableau du nombre ! nb_list_result_renverse : 9")
		elif(nb_list_result_renverse==10):
			if(j==0):
				nb_renverse_0 = int(list_result_renverse[j])
			elif(j==1):
				nb_renverse_1 = int(list_result_renverse[j])
			elif(j==2):
				nb_renverse_2 = int(list_result_renverse[j])
			elif(j==3):
				nb_renverse_3 = int(list_result_renverse[j])
			elif(j==4):
				nb_renverse_4 = int(list_result_renverse[j])
			elif(j==5):
				nb_renverse_5 = int(list_result_renverse[j])
			elif(j==6):
				nb_renverse_6 = int(list_result_renverse[j])
			elif(j==7):
				nb_renverse_7 = int(list_result_renverse[j])
			elif(j==8):
				nb_renverse_8 = int(list_result_renverse[j])
			elif(j==9):
				nb_renverse_9 = int(list_result_renverse[j])
			else:
				print("Problème lors de la longueur du tableau du nombre ! nb_list_result_renverse : 10")
		elif(nb_list_result_renverse==11):
			if(j==0):
				nb_renverse_0 = int(list_result_renverse[j])
			elif(j==1):
				nb_renverse_1 = int(list_result_renverse[j])
			elif(j==2):
				nb_renverse_2 = int(list_result_renverse[j])
			elif(j==3):
				nb_renverse_3 = int(list_result_renverse[j])
			elif(j==4):
				nb_renverse_4 = int(list_result_renverse[j])
			elif(j==5):
				nb_renverse_5 = int(list_result_renverse[j])
			elif(j==6):
				nb_renverse_6 = int(list_result_renverse[j])
			elif(j==7):
				nb_renverse_7 = int(list_result_renverse[j])
			elif(j==8):
				nb_renverse_8 = int(list_result_renverse[j])
			elif(j==9):
				nb_renverse_9 = int(list_result_renverse[j])
			elif(j==10):
				nb_renverse_10 = int(list_result_renverse[j])
			else:
				print("Problème lors de la longueur du tableau nb_list_result_renverse : 11")
	if(nb_list_result_renverse== 3):
		if(nb_renverse_2 == nb_renverse_0):
			separateur()
			palyndromes.append(base)
			palyndromes.append(nb)
		else:
			afficher_calcul(result,base)
	elif(nb_list_result_renverse == 4):
		if(nb_renverse_3 == nb_renverse_0 and nb_renverse_1 == nb_renverse_2):
			separateur()
			palyndromes.append(base)
			palyndromes.append(nb)
		else:
			afficher_calcul(result,base)
	elif(nb_list_result_renverse == 5):
		if(nb_renverse_4 == nb_renverse_0 and nb_renverse_1 == nb_renverse_3):
			separateur()
			palyndromes.append(base)
			palyndromes.append(nb)
		else:
			afficher_calcul(result,base)
	elif(nb_list_result_renverse == 6):
		if(nb_renverse_5 == nb_renverse_0 and nb_renverse_1 == nb_renverse_4 and nb_renverse_2 == nb_renverse_3):
			separateur()
			palyndromes.append(base)
			palyndromes.append(nb)
		else:
			afficher_calcul(result,base)
	elif(nb_list_result_renverse == 7):
		if(nb_renverse_6 == nb_renverse_0 and nb_renverse_1 == nb_renverse_5 and nb_renverse_2 == nb_renverse_4):
			separateur()
			palyndromes.append(base)
			palyndromes.append(nb)
		else:
			afficher_calcul(result,base)
	elif(nb_list_result_renverse == 8):
		if(nb_renverse_7 == nb_renverse_0 and nb_renverse_1 == nb_renverse_6 and nb_renverse_2 == nb_renverse_5 and nb_renverse_3 == nb_renverse_4):
			separateur()
			palyndromes.append(base)
			palyndromes.append(nb)
		else:
			afficher_calcul(result,base)
	elif(nb_list_result_renverse== 9):
		if(nb_renverse_8 == nb_renverse_0 and nb_renverse_1 == nb_renverse_7 and nb_renverse_2 == nb_renverse_6 and nb_renverse_3 == nb_renverse_5):
			separateur()
			palyndromes.append(base)
			palyndromes.append(nb)
		else:
			afficher_calcul(result,base)
	elif(nb_list_result_renverse == 10):
		if(nb_renverse_9 == nb_renverse_0 and nb_renverse_1 == nb_renverse_8 and nb_renverse_2 == nb_renverse_7 and nb_renverse_3 == nb_renverse_6 and nb_renverse_4 == nb_renverse_5):
			separateur()
			palyndromes.append(base)
			palyndromes.append(nb)
		else:
			afficher_calcul(result,base)
	elif(nb_list_result_renverse == 11):
		if(nb_renverse_10 == nb_renverse_0 and nb_renverse_1 == nb_renverse_9 and nb_renverse_2 == nb_renverse_8 and nb_renverse_3 == nb_renverse_7 and nb_renverse_4 == nb_renverse_6):
			separateur()
			palyndromes.append(base)
			palyndromes.append(nb)
		else:
			afficher_calcul(result,base)
	else:
		pb.append(base)
		pb.append(result)
		print("Erreur lors de l'affectation du nombre dans la longueur du tableau ! ")
#-------------------------------------------------#
#              Programme principal                #
#-------------------------------------------------#
palyndromes = []
non_palyndromes = []
pb = []
n_min = eval(input("Entre le nombre min :"))
n_max = eval(input("Entre le nombre max : "))
afficher_palyndrome(n_min, n_max)
print("Palyndromes :")
print(palyndromes)
separateur()
print("Non Palyndrômes :")
print(non_palyndromes)
separateur()
print("Problèmes : ")
print(pb)


#----------fonction de test du module-------------#
#if __name__ == '__main__':
    #main()


