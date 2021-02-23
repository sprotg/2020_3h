import random

penge = 10000
mål = 10100
startindsats = 10

done = False

indsats = startindsats

while not done:
    if penge > indsats:
        penge -= indsats
        if random.random() < 18/38:
            penge += 2*indsats
            print("Gevinst! Penge: {}".format(penge))
            indsats = startindsats
            if penge >= mål:
                done = True
                print("Så er der fest. Penge: {}".format(penge))
        else:
            indsats *= 2
    else:
        print("Fallit. Du kan ikke spille {}. Penge: {}".format(indsats, penge))
        done = True
