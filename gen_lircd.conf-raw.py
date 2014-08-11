# HELI_throttle_roll_yaw_pitch_light
from fonctions import *

def gen_code(bin):
  bin=str(bin)
  output=' 648 585 631 1227'
  long=' 1195'
  short=' 636'
  one=long+short
  zero=short+short
  wait=' 38655'
  for bit in bin:
    if bit == "1": output+=one
    else : output+=zero
  #end bit
  output+=short
  return output

def to_bin(nombre,nbr_de_bits):
  output=str()
  binaire=bin(int(nombre)).replace('0b','')
  # for i in range(nbr_de_bits):
  #   output+='0'
  if nombre >= 2**nbr_de_bits:
    return False
  else :
    for i in range(nbr_de_bits-len(binaire)):
      output+='0'
    for i in binaire:
      output+=str(i)
      #output[-i]=j
  return output

print("begin remote")
print("name  SILVERLIT")
print("flags RAW_CODES")
print("eps            30")
print("aeps          100")
print("gap          37868")
print("begin raw_codes")

for i in range(16):
  for j in range(16):
    for k in range(16):
      for l in range(16):
        for m in range(2):
            print("name HELI_"+str(i)+"_"+str(j)+"_"+str(k)+"_"+str(l)+"_"+str(m))
            print(gen_code('00'+to_bin(i,4)+'0'+to_bin(j,4)+'0'+to_bin(k,4)+'0'+to_bin(l,4)+'0'+to_bin(m,1)+to_bin(gen_check(i,j,k,l,m),2)))

print("\n \
      end raw_codes \n \
\n \
end remote")
