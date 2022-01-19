import tkinter as tk
from scipy.stats import norm
wringus = tk.Tk()

bgu = tk.PhotoImage(file = "/Users/aryanm/Documents/GitHub/Stats-App/APCreateTask/1440x900background.png")
lb = tk.Label(wringus, image = bgu, borderwidth=-10)
lb.place(x=-1, y=-1)
wringus.geometry('1440x900')

frame = tk.Frame(wringus)

v = tk.StringVar()
w = tk.StringVar()
x = tk.StringVar()
y = tk.StringVar()

pointEstimateEntry = tk.Entry(wringus, textvariable=v)
sampleSizeEntry = tk.Entry(wringus, textvariable=w)
confidenceLevelEntry = tk.Entry(wringus, textvariable=x)
StandardDevEntry = tk.Entry(wringus, textvariable=y)

cIntLabel = tk.Label(wringus, text = "", font=("Proxima Nova", 25), fg = "white")
SigTestLabel = tk.Label(wringus, text = "", font=("Proxima Nova", 25), fg = "white")

def returnHaGreater():
    print("greater")
    global HaVar
    HaVar = 'greater'

def returnHaLess():
    print("less")
    global HaVar
    HaVar = 'less'

def returnHaNotEqual():
    print("not equal")
    global HaVar
    HaVar = 'not equal'

def entryCollect():
    vNum = float(v.get())
    wNum = float(w.get())
    xNum = float(x.get())

    print(f"Proportion: {vNum}")
    print(f"Sample Size: {wNum}")
    print(f"Confidence Level: {xNum}")

    pointEstimate = vNum
    standardError = ((vNum*(1-vNum))/wNum)**(1/2)
    if xNum == 95:
        criticalValue = 1.9599
    elif xNum == 99:
        criticalValue = 2.5758
    elif xNum == 90:
        criticalValue = 1.64485
    else:
        criticalValue = norm.ppf(xNum/100)
##################################################################
    cIntLow = pointEstimate - (criticalValue * standardError)
    cIntHigh = pointEstimate + (criticalValue * standardError)
##################################################################
    cLowRounded = ("%.3f" % cIntLow)
    cHighRounded = ("%.3f" % cIntHigh)
    cIntLabel.config(text = f"({cLowRounded},  {cHighRounded})")

    print(f"({cIntLow}, {cIntHigh})")
    cIntLabel.config(bg="#1c1c1c")
    cIntLabel.pack()

def entryCollectMean():
    vNum = float(v.get())
    wNum = float(w.get())
    xNum = float(x.get())
    yNum = float(y.get())

    print(f"Proportion: {vNum}")
    print(f"Sample Size: {wNum}")
    print(f"Confidence Level: {xNum}")
    print(f"Standard Deviation: {yNum}")

    pointEstimate = vNum
    standardDeviation = yNum
    standardError = (standardDeviation/(wNum**(1/2)))
    if xNum == 95:
        criticalValue = 1.9599
    elif xNum == 99:
        criticalValue = 2.5758
    elif xNum == 90:
        criticalValue = 1.64485
    else:
        criticalValue = norm.ppf(xNum/100)
##################################################################
    cIntLow = pointEstimate - (criticalValue * standardError)
    cIntHigh = pointEstimate + (criticalValue * standardError)
##################################################################
    cLowRounded = ("%.3f" % cIntLow)
    cHighRounded = ("%.3f" % cIntHigh)
    cIntLabel.config(text = f"({cLowRounded},  {cHighRounded})")

    print(f"({cIntLow}, {cIntHigh})")
    cIntLabel.config(bg="#1c1c1c")
    cIntLabel.pack()

def entryCollectSigTestProportion():

    vNum = float(v.get()) #Ho (Null Hypothesis)
    wNum = float(w.get()) #Sample Size
    xNum = float(x.get()) #Significance Level
    yNum = float(y.get()) #Ha Evidence

    print(f"Ho (Null Hypothesis): {vNum}")
    print(f"Ha {HaVar} Ho")
    print(f"Sample Size: {wNum}")
    print(f"Significance Level: {xNum}")
    print(f"Evidence for Ha: p^ = {yNum}")

    NullHyp = vNum
    sampleSize = wNum
    HaEvidence = yNum
    significanceLevel = xNum

    standardError = ((NullHyp*(1-NullHyp))/sampleSize)**(1/2)
    ZScore = (HaEvidence - NullHyp)/standardError

    print(f"\n{ZScore}\n")
    
    PValue = 1-(norm.cdf(ZScore))

    if HaVar == 'less':
        #PValReal = PValue/2
        HaToSymbol = '<'
    elif HaVar == 'greater':
        #PValReal = PValue/2
        HaToSymbol = '>'
    elif HaVar == 'not equal':
        #PValReal = PValue
        HaToSymbol = '≠'
        PValue = PValue * 2
    
    PValueRounded = ("%.3f" % PValue)

    print(PValue)
    if PValue > significanceLevel:
        SigTestLabel.config(text = f"For the test ||  Ho = {NullHyp} versus Ha {HaToSymbol} {NullHyp}  ||, Fail To Reject Ho\nP-Value: {PValueRounded}")
    else:
        SigTestLabel.config(text = f"For the test ||  Ho = {NullHyp} versus Ha {HaToSymbol} {NullHyp}  ||, Reject Ho\nP-Value: {PValueRounded}")

    SigTestLabel.config(bg="#1c1c1c")
    SigTestLabel.pack()

def redBtnCommand():
    v.set("")
    w.set("")
    x.set("")
    y.set("")
    frame.pack_forget()
    greenbutton.pack_forget()
    redbutton.pack_forget()
    space3.pack_forget()
    space7.pack_forget()
    bluebutton.pack_forget()
    labeL.pack()
    labeL.config(bg="#1c1c1c")
    space1.config(bg="#1c1c1c")
    EnterAProportion.pack()
    EnterAProportion.config(bg="#1c1c1c")
    pointEstimateEntry.pack()
    EnterASampleSize.pack()
    EnterASampleSize.config(bg="#1c1c1c")
    sampleSizeEntry.pack()
    EnterAConfidenceLevel.pack()
    EnterAConfidenceLevel.config(bg="#1c1c1c")
    confidenceLevelEntry.pack()
    space1.pack()
    enterbuttonP.pack()

def greenBtnCommand():
    v.set("")
    w.set("")
    x.set("")
    y.set("")
    frame.pack_forget()
    greenbutton.pack_forget()
    redbutton.pack_forget()
    space3.pack_forget()
    space7.pack_forget()
    bluebutton.pack_forget()
    labeL.pack()
    labeL.config(bg="#1c1c1c")
    space1.config(bg="#1c1c1c")
    EnterAMean.pack()
    EnterAMean.config(bg="#1c1c1c")
    pointEstimateEntry.pack()
    EnterASampleSize.pack()
    EnterASampleSize.config(bg="#1c1c1c")
    sampleSizeEntry.pack()
    EnterAStandardDev.pack()
    EnterAStandardDev.config(bg="#1c1c1c")
    StandardDevEntry.pack()
    EnterAConfidenceLevel.pack()
    EnterAConfidenceLevel.config(bg="#1c1c1c")
    confidenceLevelEntry.pack()
    space1.pack()
    enterbuttonM.pack()

def blueBtnCommand():
    
    v.set("0.24")#Ho
    w.set("104")#Sample Size
    x.set("0.05")#Sig Level
    y.set("0.32")#Ha Evidence

    greenbutton.pack_forget()
    redbutton.pack_forget()
    space3.pack_forget()
    space7.pack_forget()
    bluebutton.pack_forget()

    labeL2.pack()
    labeL2.config(bg="#1c1c1c")
    space1.config(bg="#1c1c1c")

    EnterAHo.pack()
    EnterAHo.config(bg="#1c1c1c")
    pointEstimateEntry.pack()

    frame.pack()
    HaLessThanHo.pack(side='right')
    HaGreaterThanHo.pack(side='left')
    HaNotEqualToHo.pack(side='bottom')

    EnterASampleSize.pack()
    EnterASampleSize.config(bg="#1c1c1c")
    sampleSizeEntry.pack()

    EnterEvidenceForHa.pack()
    EnterEvidenceForHa.config(bg="#1c1c1c")
    StandardDevEntry.pack()

    EnterASignificanceLevel.pack()
    EnterASignificanceLevel.config(bg="#1c1c1c")
    confidenceLevelEntry.pack()
    space1.pack()
    enterbuttonSTP.pack()

def backCommand():
    space3.pack()
    redbutton.pack()
    greenbutton.pack()
    space7.pack()
    bluebutton.pack()

    SigTestLabel.pack_forget()
    enterbuttonSTP.pack_forget()
    EnterEvidenceForHa.pack_forget()
    EnterAHo.pack_forget()
    EnterASignificanceLevel.pack_forget()
    frame.pack_forget()
    labeL2.pack_forget()
    labeL.pack_forget()
    space1.pack_forget()
    EnterAProportion.pack_forget()
    EnterAStandardDev.pack_forget()
    EnterAMean.pack_forget()
    EnterASampleSize.pack_forget()
    EnterAConfidenceLevel.pack_forget()
    cIntLabel.pack_forget()

    pointEstimateEntry.pack_forget()
    sampleSizeEntry.pack_forget()
    confidenceLevelEntry.pack_forget()
    StandardDevEntry.pack_forget()

    enterbuttonP.pack_forget()
    enterbuttonM.pack_forget()

labeL = tk.Label(wringus, text = "Confidence Interval", font=("Proxima Nova", 25), fg = "white")
labeL2 = tk.Label(wringus, text = "Significance Test", font=("Proxima Nova", 25), fg = "white")

enterbuttonP = tk.Button(wringus, text = "Enter", highlightbackground="#35f4a6", font=("Proxima Nova", 25), command=entryCollect)
enterbuttonM = tk.Button(wringus, text = "Enter", highlightbackground="#35f4a6", font=("Proxima Nova", 25), command=entryCollectMean)

####################################################################################################################################################
enterbuttonSTP = tk.Button(wringus, text = "Enter", highlightbackground="#35f4a6", font=("Proxima Nova", 25), command=entryCollectSigTestProportion)
####################################################################################################################################################

space1 = tk.Label(wringus, text = " ", font = ("Proxima Nova", 12))

####################################################################################################################################################
EnterAHo = tk.Label(wringus, text = "Enter A NUMERICAL Null Hypothesis", font = ("Proxima Nova", 12), fg = "white")
EnterASignificanceLevel = tk.Label(wringus, text = "Enter A Numerical Significance Level (0.00-1.00)", font = ("Proxima Nova", 12), fg = "white")
EnterEvidenceForHa = tk.Label(wringus, text = "Enter Evidence For Your Null Hypothesis (Ha)", font = ("Proxima Nova", 12), fg = "white")

HaLessThanHo = tk.Button(frame, text = "Ha < Ho", highlightbackground="#35f4a6", font=("Proxima Nova", 12), command=returnHaLess)
HaGreaterThanHo = tk.Button(frame, text = "Ha > Ho", highlightbackground="#35f4a6", font=("Proxima Nova", 12), command=returnHaGreater)
HaNotEqualToHo = tk.Button(frame, text = "Ha ≠ Ho", highlightbackground="#35f4a6", font=("Proxima Nova", 12), command=returnHaNotEqual)
####################################################################################################################################################

EnterAProportion = tk.Label(wringus, text = "Enter A Numerical Proportion", font = ("Proxima Nova", 12), fg = "white")
EnterAStandardDev = tk.Label(wringus, text = "Enter A Standard Deviation", font = ("Proxima Nova", 12), fg = "white")
EnterAMean = tk.Label(wringus, text = "Enter A Numerical Mean", font = ("Proxima Nova", 12), fg = "white")
EnterASampleSize = tk.Label(wringus, text = "Enter A Numerical Sample Size", font = ("Proxima Nova", 12), fg = "white")
EnterAConfidenceLevel = tk.Label(wringus, text = "Enter A Numerical Confidence Level (0-100)", font = ("Proxima Nova", 12), fg = "white")

space2 = tk.Label(wringus, text = " ", font = ("Proxima Nova", 12))
space2.config(bg="#1c1c1c")
space3 = tk.Label(wringus, text = "STATS APP", font = ("Proxima Nova", 25), fg='#ffffff')
space3.config(bg="#1c1c1c")
space4 = tk.Label(wringus, text = " ", font = ("Proxima Nova", 12))
space4.config(bg="#1c1c1c")
space5 = tk.Label(wringus, text = " ", font = ("Proxima Nova", 12))
space5.config(bg="#1c1c1c")

space2.pack()
space3.pack()
space4.pack()
space5.pack()

redbutton = tk.Button(wringus, text="Confidence Interval (Proportion)", highlightbackground="#35f4a6", fg="black", font=("Proxima Nova", 25), command=redBtnCommand)
redbutton.pack()

space6 = tk.Label(wringus, text = " ", font = ("Proxima Nova", 12))
space6.config(bg="#1c1c1c")
space6.pack()

greenbutton = tk.Button(wringus, text="Confidence Interval (Mean)", highlightbackground="#35f4a6", fg="black", font=("Proxima Nova", 25), command=greenBtnCommand)
greenbutton.pack()

space7 = tk.Label(wringus, text = " ", font = ("Proxima Nova", 12))
space7.config(bg="#1c1c1c")
space7.pack()

bluebutton = tk.Button(wringus, text="Significance Test (Proportion)", highlightbackground="#35f4a6", fg="black", font=("Proxima Nova", 25), command=blueBtnCommand)
bluebutton.pack()

backButton = tk.Button(wringus, text="Back", highlightbackground="#35f4a6", fg="black", font=("Proxima Nova", 25), command=backCommand)
backButton.place(x=2, y=2)

tk.mainloop()