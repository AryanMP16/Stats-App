from random import randint
rLow = 1#int(input("What is your lower limit?\t"))
rUp = 100#int(input("What is your upper limit?\t"))
rWantLow = 20#int(input("What is your lowest desired value?\t"))
rWantUp = 60#int(input("What is your highest desired value?\t"))
#randint(rLow, rUp) < rWantUp and randint(rLow, rUp) > rWantLow
counter = 1
l1 = []
l2 = []
def randIntGen():
    return randint(rLow, rUp)

def rGenCheck():
    rr = randIntGen()
    if rr < rWantUp and rr > rWantLow:
        return True
    else:
        return False

for x in range(50):
    for i in range(10000):
        counter = 1
        i+=1
        while rGenCheck() == False:
            counter += 1
            rGenCheck()
        l1.append(counter)
    total = 0
    for j in l1:
        total+=j
        #print(total)
    sampleAvg = float(total/len(l1))
    probability = ((float(1/sampleAvg))*100)+1
    pRounded = ("%.3f" % probability)
    l2.append(float(pRounded))
    l1 = []

lAvg = ("%.3f" % float(sum(l2)/len(l2)))

print(f"If we simulated 10,000 random selections of subjects labelled {rLow} to {rUp}, the probability of getting a subject numbered {rWantLow} to {rWantUp} is: { str(lAvg)} %.")
