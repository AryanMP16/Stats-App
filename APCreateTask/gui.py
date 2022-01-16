import tkinter as tk
from scipy.stats import norm
wringus = tk.Tk()

bgu = tk.PhotoImage(file = "/Users/aryanm/Desktop/APCreateTask/1440x900background.png")
lb = tk.Label(wringus, image = bgu, borderwidth=-10)
lb.place(x=-1, y=-1)
wringus.geometry('1440x900')

frame = tk.Frame(wringus)
frame.pack()

v = tk.StringVar()
w = tk.StringVar()
x = tk.StringVar()
y = tk.StringVar()

pointEstimateEntry = tk.Entry(wringus, textvariable=v)
sampleSizeEntry = tk.Entry(wringus, textvariable=w)
confidenceLevelEntry = tk.Entry(wringus, textvariable=x)
StandardDevEntry = tk.Entry(wringus, textvariable=y)

cIntLabel = tk.Label(wringus, text = "", font=("Proxima Nova", 25), fg = "white")

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

def redBtnCommand():
    v.set("")
    w.set("")
    x.set("")
    y.set("")
    greenbutton.pack_forget()
    redbutton.pack_forget()
    space3.pack_forget()
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
    greenbutton.pack_forget()
    redbutton.pack_forget()
    space3.pack_forget()
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

def backCommand():
    space3.pack()
    redbutton.pack()
    greenbutton.pack()

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

enterbuttonP = tk.Button(wringus, text = "Enter", highlightbackground="#35f4a6", font=("Proxima Nova", 25), command=entryCollect)
enterbuttonM = tk.Button(wringus, text = "Enter", highlightbackground="#35f4a6", font=("Proxima Nova", 25), command=entryCollectMean)

space1 = tk.Label(wringus, text = " ", font = ("Proxima Nova", 12))
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

backButton = tk.Button(wringus, text="Back", highlightbackground="#35f4a6", fg="black", font=("Proxima Nova", 25), command=backCommand)
backButton.place(x=2, y=2)

tk.mainloop()