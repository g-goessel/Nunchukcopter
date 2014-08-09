# -*- coding: utf8 -*-

"""
Fichier  contenant les fonctions utilisees par les programmes
"""


def get_pitch(wm,origin):
    # recalibre et inverse le signe pour une lecture plus naturelle
    pitch=-(wm.state['nunchuk']['acc'][1]-origin["acc_1"])
    if pitch < 0:
        return 0
    elif pitch >= 40 :
        pitch = 39
    pitch = int(float(pitch)*16/40)
    return pitch


def get_roll(wm,origin):
    # recalibre
    roll=(wm.state['nunchuk']['acc'][0]-origin["acc_0"]) + 32
    if roll < 0 :
        roll = 0
    elif roll >= 64 :
        roll = 63
    roll = int(float(roll)*16/64)
    return roll


def get_x(wm,origin):
    x = wm.state['nunchuk']['stick'][0]-origin["x"] + 100
    if x > 95 and x < 105: x=100
    elif x <0 : x=1
    elif x >= 200 : x=199
    x = float(x)/200
    x = x*16
    x = int(x)
    return x

def get_y(wm,origin):
    y = wm.state['nunchuk']['stick'][1]-origin["y"] + 100
    if y > 95 and y < 105: y=100
    elif y <0 : y=1
    elif y >= 200 : y=199
    y = float(y)/200
    y = y*16
    y = int(y)
    return y

def update_batt(wm):
    batt_state = wm.state['battery']
    if batt_state < 25 : wm.led=1
    elif batt_state <50 : wm.led=3
    elif batt_state < 75 : wm.led=7
    else : wm.led=15

def calibrate(wm):
    return {"acc_0":wm.state['nunchuk']['acc'][0],\
    "acc_1":wm.state['nunchuk']['acc'][1], "acc_2":wm.state['nunchuk']['acc'][2],\
    "x":wm.state['nunchuk']['stick'][0], "y":wm.state['nunchuk']['stick'][1]}


def test():
    for i in range(16) :
        #os.system("irsend SEND_ONCE SILVERLIT HELI_"+str(i)+"_3_3_3_1_"+str(j))
        command=str(i)+"_8_8_8_0"
        subprocess.call("irsend SEND_ONCE SILVERLIT HELI_"+command+"_"+str(gen_check(i,8,8,8,0)), shell=True)


def to_bin(nombre,nbr_de_bits):
  output=str()
  binaire=bin(int(nombre)).replace('0b','')
  # for i in range(nbr_de_bits):
  #   output+='0'
  for i in range(nbr_de_bits-len(binaire)):
    output+='0'
  for i in binaire:
    output+=str(i)
    #output[-i]=j
  return output


def gen_check(a,b,c,d,l):
    code=0
    bin=to_bin(a<<1,5)+to_bin(b<<1,5)+to_bin(c<<1,5)+to_bin(d<<1,5)+to_bin(l,1)
    for i,j in enumerate(bin):
        if j=='1':
            if i%2 ==0:
                code^=1
            else :
                code^=2
    return code

def pause(wm):
    while wm.state['nunchuk']['buttons'] == 1:
        print "Z still pressed"
        time.sleep(0.5)
    print "Z relieved"
    i=0
    while wm.state['nunchuk']['buttons'] != 1:
        print "Pause in progress"
        wm.led=int(pause_led_style(i))
        i+=1
        i%=19
        time.sleep(0.5)
    print "End of the pause"
    return calibrate(wm)

def pause_led_style(count):
    if count == 0:
        return '0001'
    elif count == 1:
        return '0010'
    elif count == 2:
        return '0100'
    elif count == 3:
        return '1000'
    elif count == 4:
        return '1001'
    elif count == 5:
        return '1010'
    elif count == 6:
        return '1100'
    elif count == 7:
        return '1101'
    elif count == 8:
        return '1110'
    elif count == 9:
        return '1111'
    elif count == 10:
        return '0111'
    elif count == 11:
        return '1011'
    elif count == 12:
        return '0011'
    elif count == 13:
        return '0101'
    elif count == 14:
        return '1001'
    elif count == 15:
        return '0001'
    elif count == 16:
        return '0010'
    elif count == 17:
        return '0100'
    elif count == 18:
        return '1000'
    else:
        return '0'
