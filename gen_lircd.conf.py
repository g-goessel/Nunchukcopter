#! /usr/bin/python2.7
# -*- coding: utf8 -*-

"""
Ce programme permet de générer le fichier de configuration de lirc
afin de pouvoir envoyer les commandes a l'hélicoptère de manière simple
A lire pour plus de details : http://winlirc.sourceforge.net/technicaldetails.html
"""

from fonctions import *

print "begin remote\n \
  name            SILVERLIT \n \
  flags           SPACE_ENC\n\
  bits            23\n \
  eps             30\n \
  aeps            100 \n \
  header          648 585 631 1227 610 630 610 630\n \
  ptrail          630\n \
  one             1195   630\n \
  zero            610   630\n \
  gap             39000\n \
  \n \
  begin codes"


#foot            630 630\n \
# Ensuite on genere tous les codes IR possibles
# Pour savoir le nombre de cas possibles il faut faire
# nbr_possibles = 2^nbr_de_bits_du_parametre

for i in range(2**4):
    for j in range(2**4):
        for k in range(2**4):
            for l in range(2**4):
                for m in range(2):
                    print "  HELI_"+str(i)+"_"+str(j)+"_"+str(k)+"_"+str(l)+"_"+str(m)\
                            +"    "+hex((i<<19) + (j<<14) + (k<<9) + (l<<4) + (m<<2) + (gen_check(i,j,k,l,m)))

print "  end  codes\n \
end remote"
