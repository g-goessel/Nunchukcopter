#! /usr/bin/python2.7

"""
Ce programme permet de generer le fichier de configuration de lirc
afin de pouvoir envoyer les commandes a l helicoptere de maniere simple
A lire pour plus de details : http://winlirc.sourceforge.net/technicaldetails.html
"""

#import fonctions as fn

print "begin remote\n \
  name            SILVERLIT \n \
  bits            23\n \
  eps             30\n \
  aeps            100 \n \
  header          648 585 631 1227 630 630\n \
  one             1200   630\n \
  zero            630   630\n \
  gap             39000\n \
  foot            630 630 \n \
  \n \
  begin codes"

# Ensuite on genere tous les codes IR possibles
# Pour savoir le nombre de cas possibles il faut faire
# nbr_possibles = 2^nbr_de_bits_du_parametre

for i in range(2**5):
    for j in range(2**5):
        for k in range(2**5):
            for l in range(2**5):
                for m in range(2):
                    print "  HELI_"+str(i)+"_"+str(j)+"_"+str(k)+"_"+str(l)+"_"+str(m)\
                            +"    "+hex((i<<18) + (j<<13) + (k<<8) + (l<<3) + (m<<2) + (fn.gen_check(i,j,k,l,m)))

print "  end  codes\n \
end remote"
