#Jan 20, 2022
#Application inspired by content from AP Statistics course. Application and accompanying GUI programmed by Aryan Mosavianpour
#Code published to GitHub.
import tkinter as tk #importing main GUI library
from random import randint #importing library for generating random integers. Randomness is a key element in statistics.
from scipy.stats import norm #importing library for functions pertaining to distribution curves
wringus = tk.Tk() #defined main window as 'wringus'

bgu = tk.PhotoImage(file = "/Users/aryanm/Documents/GitHub/Stats-App/APCreateTask/1440x900background.png") #background picture
lb = tk.Label(wringus, image = bgu, borderwidth=-10) #tkinter makes it quite difficult to use background pictures normally, so I created a label with a 1440x900 pixel background image
lb.place(x=-1, y=-1) #image placed @ x=0,y=0 caused a white border, so I placed it @ -1, -1
wringus.geometry('1440x900') #size of window

frame = tk.Frame(wringus) #initializing frame for later use. Frames in tKinter are used to place multiple objects in one row (i.e. buttons)

v = tk.StringVar() #ran into issues collecting entry data from text input. StringVar() worked as a workaround. I have four text input boxes, and as such, 4 StringVar() variables.
w = tk.StringVar()
x = tk.StringVar()
y = tk.StringVar()

pointEstimateEntry = tk.Entry(wringus, textvariable=v) #assigning my 4 text input boxes to their StringVar() counterparts
sampleSizeEntry = tk.Entry(wringus, textvariable=w)
confidenceLevelEntry = tk.Entry(wringus, textvariable=x)
StandardDevEntry = tk.Entry(wringus, textvariable=y)

cIntLabel = tk.Label(wringus, text = "", font=("Proxima Nova", 25), fg = "white") #defining some labels up here because they need to be accessed before all other labels do
SigTestLabel = tk.Label(wringus, text = "", font=("Proxima Nova", 25), fg = "white")
SRSsimLabel = tk.Label(wringus, text = "", font=("Proxima Nova", 25), fg = "white")

def returnHaGreater(): #of the alternative hypothesis buttons in the significance testing window, clicking THIS button will indicate that the user wants to calculate alternative hypothesis > null hypothesis
    print("greater")
    global HaVar
    HaVar = 'greater'

def returnHaLess(): # " alternative hypothesis < null hypothesis
    print("less")
    global HaVar
    HaVar = 'less'

def returnHaNotEqual(): # " alternative hypothesis ≠ null hypothesis
    print("not equal")
    global HaVar
    HaVar = 'not equal'

def entryCollect(): #collect input entries for confidence interval of proportions window
    vNum = float(v.get()) #collect text data from all 3 text input boxes
    wNum = float(w.get())
    xNum = float(x.get())

    print(f"Proportion: {vNum}") #print for debugging
    print(f"Sample Size: {wNum}")
    print(f"Confidence Level: {xNum}")

    pointEstimate = vNum #statistical calculations to determine critical value, point estimate, and standard error, the 3 components that make up a confidence interval
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
    cIntLow = pointEstimate - (criticalValue * standardError) #this formula is in the AP Statistics official formula sheet
    cIntHigh = pointEstimate + (criticalValue * standardError) # ^^
##################################################################
    cLowRounded = ("%.3f" % cIntLow) #rounding above calculations to make it easier on the user's eyes
    cHighRounded = ("%.3f" % cIntHigh)
    cIntLabel.config(text = f"({cLowRounded},  {cHighRounded})") #displaying calculations on screen

    print(f"({cIntLow}, {cIntHigh})") #printing calculations to terminal for debugging purposes
    cIntLabel.config(bg="#1c1c1c") #making calculation display label's background the same color as the background image
    cIntLabel.pack()

def entryCollectMean(): #collect input entries for confidence interval of means window
    vNum = float(v.get()) #collect text data from all 4 text input boxes
    wNum = float(w.get())
    xNum = float(x.get())
    yNum = float(y.get())

    print(f"Proportion: {vNum}")
    print(f"Sample Size: {wNum}")
    print(f"Confidence Level: {xNum}")
    print(f"Standard Deviation: {yNum}")

    pointEstimate = vNum #statistical calculations to determine critical value, point estimate, and standard error, the 3 components that make up a confidence interval
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
    cIntLow = pointEstimate - (criticalValue * standardError) #this formula is in the AP Statistics official formula sheet
    cIntHigh = pointEstimate + (criticalValue * standardError) # ^^
##################################################################
    cLowRounded = ("%.3f" % cIntLow) #rounding above calculations to make it easier on the user's eyes
    cHighRounded = ("%.3f" % cIntHigh)
    cIntLabel.config(text = f"({cLowRounded},  {cHighRounded})") #displaying calculations on screen

    print(f"({cIntLow}, {cIntHigh})") #printing calculations to terminal for debugging purposes
    cIntLabel.config(bg="#1c1c1c") #making calculation display label's background the same color as the background image
    cIntLabel.pack()

def entryCollectSigTestProportion(): #collect input entries for significance testing of proportions window
    #collect text data from all 4 text input boxes:
    vNum = float(v.get()) #Ho (Null Hypothesis)
    wNum = float(w.get()) #Sample Size
    xNum = float(x.get()) #Significance Level
    yNum = float(y.get()) #Ha Evidence

    print(f"Ho (Null Hypothesis): {vNum}") #printing values for debugging purposes
    print(f"Ha {HaVar} Ho")
    print(f"Sample Size: {wNum}")
    print(f"Significance Level: {xNum}")
    print(f"Evidence for Ha: p^ = {yNum}")

    NullHyp = vNum #renaming variables for convenience and synonymity with formulas
    sampleSize = wNum
    HaEvidence = yNum
    significanceLevel = xNum

    standardError = ((NullHyp*(1-NullHyp))/sampleSize)**(1/2) #this formula is in the AP Statistics official formula sheet
    ZScore = (HaEvidence - NullHyp)/standardError # ^^

    print(f"\n{ZScore}\n") #printing for debugging purposes
    
    PValue = 1-(norm.cdf(ZScore)) #using scipy.stats library to perform a normalcdf function

    if HaVar == 'less': #conditional statement checking which button is pressed. Will always take most recent value due to mainloop at the end of the code
        HaToSymbol = '<'
    elif HaVar == 'greater':
        HaToSymbol = '>'
    elif HaVar == 'not equal':
        HaToSymbol = '≠'
        PValue = PValue * 2
    
    PValueRounded = ("%.3f" % PValue) #rounding so that the user doesn't have to strain their eyes staring at a 20-digit number

    print(PValue) #printing for debugging purposes
    if PValue > significanceLevel: #conditional statement testing whether to reject or fail to reject the null hypothesis. Conditional stated in AP Statistics textbook
        SigTestLabel.config(text = f"For the test ||  Ho = {NullHyp} versus Ha {HaToSymbol} {NullHyp}  ||, Fail To Reject Ho\nP-Value: {PValueRounded}") #display results (reject/fail to reject) to user
    else:
        SigTestLabel.config(text = f"For the test ||  Ho = {NullHyp} versus Ha {HaToSymbol} {NullHyp}  ||, Reject Ho\nP-Value: {PValueRounded}") # ^^

    SigTestLabel.config(bg="#1c1c1c")
    SigTestLabel.pack()

def entryCollectSRSsim(): #collect input entries for significance testing of proportions window
    rLow = float(v.get()) #collect text data from all 4 text input boxes
    rUp = float(w.get())
    rWantLow = float(x.get())
    rWantUp = float(y.get())

    counter = 1 #creating a counter to keep track of data outputs
    l1 = [] #will be used to take average of data in one sample
    l2 = [] #will be used to take average of mean proportions across samples
    def randIntGen():
        return randint(rLow, rUp) #generate random number within denoted domain

    def rGenCheck(): #checking whether randomly generated number is within specified range
        rr = randIntGen()
        if rr < rWantUp and rr > rWantLow:
            return True
        else:
            return False

    for o in range(50): #taking 50 samples
        for i in range(10000): #each sample will have 10,000 experimental units
            counter = 1 #initializing counter inside of for-loop
            i+=1
            while rGenCheck() == False: #count how many times our generated number falls inside of the specified range
                counter += 1
                rGenCheck()
            l1.append(counter) #append counter to l1
        total = 0 #reset total for later use
        for j in l1:
            total+=j #calculate total of l1 values so that we can calculate an average
        sampleAvg = float(total/len(l1)) #calculate average of l1 values
        probability = ((float(1/sampleAvg))*100)+1 #determine probability from mean of sampling proportions obtained in the line above
        pRounded = ("%.3f" % probability) #round answer so it's not a literal eye sore
        l2.append(float(pRounded)) #add all averages to a list, l2
        l1 = []

    lAvg = ("%.3f" % float(sum(l2)/len(l2))) #take the average of values in l2

    SRSsimLabel.config(text = f"We simulated 50 SRSs of 10,000 subjects labelled {int(rLow)} to {int(rUp)}.\nThe probability we calculated of getting a subject numbered {int(rWantLow)} to {int(rWantUp)} is: { str(lAvg)} %.") #display results to user
    SRSsimLabel.config(bg="#1c1c1c")
    SRSsimLabel.pack()

def redBtnCommand(): #button takes you to the confidence interval of proportions page
    v.set("") #initialize all text input boxes to have nothing in them when created
    w.set("")
    x.set("")
    y.set("")
    frame.pack_forget() #remove unnecessary elements from menu screen
    greenbutton.pack_forget()
    redbutton.pack_forget()
    space3.pack_forget()
    space7.pack_forget()
    bluebutton.pack_forget()
    space8.pack_forget()
    yellowbutton.pack_forget()
    labeL.pack() #add and configurate elements for aesthetic purposes
    labeL.config(bg="#1c1c1c")
    space1.config(bg="#1c1c1c")
    EnterAProportion.pack() #add text input boxes
    EnterAProportion.config(bg="#1c1c1c")
    pointEstimateEntry.pack()
    EnterASampleSize.pack()
    EnterASampleSize.config(bg="#1c1c1c")
    sampleSizeEntry.pack()
    EnterAConfidenceLevel.pack()
    EnterAConfidenceLevel.config(bg="#1c1c1c")
    confidenceLevelEntry.pack()
    space1.pack()
    enterbuttonP.pack() # <-- adding enter button

def greenBtnCommand(): #button takes you to the confidence interval of means page
    v.set("") #initialize all text input boxes to have nothing in them when created
    w.set("")
    x.set("")
    y.set("")
    frame.pack_forget() #remove unnecessary elements from menu screen
    greenbutton.pack_forget()
    redbutton.pack_forget()
    space3.pack_forget()
    space7.pack_forget()
    bluebutton.pack_forget()
    space8.pack_forget()
    yellowbutton.pack_forget()
    labeL.pack() #add and configurate elements for aesthetic purposes
    labeL.config(bg="#1c1c1c")
    space1.config(bg="#1c1c1c")
    EnterAMean.pack() #add text input boxes
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
    enterbuttonM.pack() # <-- adding enter button

def blueBtnCommand(): #button takes you to the significance testing of proportions page
    #initialize all text input boxes to have nothing in them when created:
    v.set("")#Ho
    w.set("")#Sample Size
    x.set("")#Sig Level
    y.set("")#Ha Evidence

    greenbutton.pack_forget() #remove unnecessary elements from menu screen
    redbutton.pack_forget()
    space3.pack_forget()
    space7.pack_forget()
    bluebutton.pack_forget()
    space8.pack_forget()
    yellowbutton.pack_forget()

    labeL2.pack() #add and configurate elements for aesthetic purposes
    labeL2.config(bg="#1c1c1c")
    space1.config(bg="#1c1c1c")

    EnterAHo.pack() #add text input boxes
    EnterAHo.config(bg="#1c1c1c")
    pointEstimateEntry.pack()

    frame.pack() # <-- add frame holding 3 buttons in 1 horizontal 'layer'
    HaLessThanHo.pack(side='right')
    HaGreaterThanHo.pack(side='left')
    HaNotEqualToHo.pack(side='bottom')

    EnterASampleSize.pack() #continuing to add text input boxes
    EnterASampleSize.config(bg="#1c1c1c")
    sampleSizeEntry.pack()

    EnterEvidenceForHa.pack()
    EnterEvidenceForHa.config(bg="#1c1c1c")
    StandardDevEntry.pack()

    EnterASignificanceLevel.pack()
    EnterASignificanceLevel.config(bg="#1c1c1c")
    confidenceLevelEntry.pack()
    space1.pack()
    enterbuttonSTP.pack() # <-- adding enter button

def yellowBtnCommand(): #button takes you to the SRS computer simulation (replacing Table D) page
    #initialize all text input boxes to have nothing in them when created:
    v.set("")#rLow
    w.set("")#rUp
    x.set("")#rWantLow
    y.set("")#rWantUp

    greenbutton.pack_forget() #remove unnecessary elements from menu screen
    redbutton.pack_forget()
    space3.pack_forget()
    space7.pack_forget()
    bluebutton.pack_forget()
    space8.pack_forget()
    yellowbutton.pack_forget()

    labeL3.pack() #add text input boxes
    labeL3.config(bg="#1c1c1c")
    space1.config(bg="#1c1c1c")

    EnterArLow.pack()
    EnterArLow.config(bg="#1c1c1c")
    pointEstimateEntry.pack() #rLow

    EnterArUp.pack()
    EnterArUp.config(bg="#1c1c1c")
    sampleSizeEntry.pack() #rUp

    EnterArWantLow.pack()
    EnterArWantLow.config(bg="#1c1c1c")
    confidenceLevelEntry.pack() #rWantLow

    EnterArWantUp.pack()
    EnterArWantUp.config(bg="#1c1c1c")
    StandardDevEntry.pack() #rWantUp
    space1.pack()
    enterbuttonSRSsim.pack() # <-- adding enter button

def backCommand(): #button takes you back to the menu page
    #forget all other spaces so that we can add them back to the page in the proper order. Tkinter is order-sensitive.
    space8.pack_forget()
    yellowbutton.pack_forget()
    space2.pack_forget()
    space3.pack_forget()
    space4.pack_forget()
    space5.pack_forget()
    space6.pack_forget()
    space7.pack_forget()
    
    space2.pack() #adding back all labels in the correct order
    space3.pack() #Menu page title
    space4.pack()
    space5.pack()
    #<all other spaces>.pack()
    redbutton.pack()
    space6.pack()
    greenbutton.pack()
    space7.pack()
    bluebutton.pack()
    space8.pack()
    yellowbutton.pack()

    enterbuttonSRSsim.pack_forget() #getting rid of unnecessary elements from windows other than the menu page
    EnterArLow.pack_forget()
    EnterArUp.pack_forget()
    EnterArWantLow.pack_forget()
    EnterArWantUp.pack_forget()
    SRSsimLabel.pack_forget()

    SigTestLabel.pack_forget()
    enterbuttonSTP.pack_forget()
    EnterEvidenceForHa.pack_forget()
    EnterAHo.pack_forget()
    EnterASignificanceLevel.pack_forget()
    frame.pack_forget()
    labeL2.pack_forget()
    labeL3.pack_forget()
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
####################################################################################################################################################
labeL = tk.Label(wringus, text = "Confidence Interval", font=("Proxima Nova", 25), fg = "white") #creating titles for various pages
labeL2 = tk.Label(wringus, text = "Significance Test", font=("Proxima Nova", 25), fg = "white")
labeL3 = tk.Label(wringus, text = "Computer Simulation of SRS (Table D replacement || ~ 10 sec)", font=("Proxima Nova", 25), fg = "white")
####################################################################################################################################################
enterbuttonP = tk.Button(wringus, text = "Enter", highlightbackground="#35f4a6", font=("Proxima Nova", 25), command=entryCollect) #creating enter buttons for various pages
enterbuttonM = tk.Button(wringus, text = "Enter", highlightbackground="#35f4a6", font=("Proxima Nova", 25), command=entryCollectMean)
enterbuttonSTP = tk.Button(wringus, text = "Enter", highlightbackground="#35f4a6", font=("Proxima Nova", 25), command=entryCollectSigTestProportion)
enterbuttonSRSsim = tk.Button(wringus, text = "Enter", highlightbackground="#35f4a6", font=("Proxima Nova", 25), command=entryCollectSRSsim)
####################################################################################################################################################

space1 = tk.Label(wringus, text = " ", font = ("Proxima Nova", 12)) #empty spaces like this are added in to make the app look less crowded

####################################################################################################################################################
EnterAHo = tk.Label(wringus, text = "Enter A NUMERICAL Null Hypothesis", font = ("Proxima Nova", 12), fg = "white") #"Enter A..." labels are added
EnterASignificanceLevel = tk.Label(wringus, text = "Enter A Numerical Significance Level (0.00-1.00)", font = ("Proxima Nova", 12), fg = "white") # ^^
EnterEvidenceForHa = tk.Label(wringus, text = "Enter Evidence For Your Null Hypothesis (Ha)", font = ("Proxima Nova", 12), fg = "white")

EnterArLow = tk.Label(wringus, text = "Enter what you have labelled your FIRST subject (i.e. 1)", font = ("Proxima Nova", 12), fg = "white") # ^^
EnterArUp = tk.Label(wringus, text = "Enter what you have labelled your LAST subject (i.e. 100)", font = ("Proxima Nova", 12), fg = "white") # ^^
EnterArWantLow = tk.Label(wringus, text = "Enter the FIRST label you want to find in SRSs (i.e. 60)", font = ("Proxima Nova", 12), fg = "white") # ^^
EnterArWantUp = tk.Label(wringus, text = "Enter the LAST label you want to find in SRSs (i.e. 100)", font = ("Proxima Nova", 12), fg = "white") # ^^

EnterAProportion = tk.Label(wringus, text = "Enter A Numerical Proportion", font = ("Proxima Nova", 12), fg = "white") # ^^
EnterAStandardDev = tk.Label(wringus, text = "Enter A Standard Deviation", font = ("Proxima Nova", 12), fg = "white") # ^^
EnterAMean = tk.Label(wringus, text = "Enter A Numerical Mean", font = ("Proxima Nova", 12), fg = "white")
EnterASampleSize = tk.Label(wringus, text = "Enter A Numerical Sample Size", font = ("Proxima Nova", 12), fg = "white") # ^^
EnterAConfidenceLevel = tk.Label(wringus, text = "Enter A Numerical Confidence Level (0-100)", font = ("Proxima Nova", 12), fg = "white") # ^^
####################################################################################################################################################
HaLessThanHo = tk.Button(frame, text = "Ha < Ho", highlightbackground="#35f4a6", font=("Proxima Nova", 12), command=returnHaLess) #creating buttons to go in the aforementioned significance testing Ha frame
HaGreaterThanHo = tk.Button(frame, text = "Ha > Ho", highlightbackground="#35f4a6", font=("Proxima Nova", 12), command=returnHaGreater) # ^^
HaNotEqualToHo = tk.Button(frame, text = "Ha ≠ Ho", highlightbackground="#35f4a6", font=("Proxima Nova", 12), command=returnHaNotEqual) # ^^
####################################################################################################################################################

space2 = tk.Label(wringus, text = " ", font = ("Proxima Nova", 12)) #creating spaces for aesthetic
space2.config(bg="#1c1c1c") #configurating spaces' background colors to match background image
space3 = tk.Label(wringus, text = "AP STATISTICS APP", font = ("Proxima Nova", 25), fg='#ffffff') #creating menu title
space3.config(bg="#1c1c1c") #configurating spaces' background colors to match background image
space4 = tk.Label(wringus, text = " ", font = ("Proxima Nova", 12)) #creating spaces for aesthetic
space4.config(bg="#1c1c1c") #configurating spaces' background colors to match background image
space5 = tk.Label(wringus, text = " ", font = ("Proxima Nova", 12)) #creating spaces for aesthetic
space5.config(bg="#1c1c1c") #configurating spaces' background colors to match background image

space2.pack() #"pack"-ing spaces and titels (adding them to the page)
space3.pack()
space4.pack()
space5.pack()

redbutton = tk.Button(wringus, text="Confidence Interval (Proportion)", highlightbackground="#35f4a6", fg="black", font=("Proxima Nova", 25), command=redBtnCommand) #takes you to confidence level of proportions page
redbutton.pack()

space6 = tk.Label(wringus, text = " ", font = ("Proxima Nova", 12))
space6.config(bg="#1c1c1c")
space6.pack()

greenbutton = tk.Button(wringus, text="Confidence Interval (Mean)", highlightbackground="#35f4a6", fg="black", font=("Proxima Nova", 25), command=greenBtnCommand) #takes you to confidence level of means page
greenbutton.pack()

space7 = tk.Label(wringus, text = " ", font = ("Proxima Nova", 12))
space7.config(bg="#1c1c1c")
space7.pack()

bluebutton = tk.Button(wringus, text="Significance Test (Proportion)", highlightbackground="#35f4a6", fg="black", font=("Proxima Nova", 25), command=blueBtnCommand) #takes you to significance testing of proportions page
bluebutton.pack()

space8 = tk.Label(wringus, text = " ", font = ("Proxima Nova", 12))
space8.config(bg="#1c1c1c")
space8.pack()

yellowbutton = tk.Button(wringus, text="Table D (SRS) Simulation", highlightbackground="#35f4a6", fg="black", font=("Proxima Nova", 25), command=yellowBtnCommand) #takes you to SRS (Table D) page
yellowbutton.pack()

backButton = tk.Button(wringus, text="Back", highlightbackground="#35f4a6", fg="black", font=("Proxima Nova", 20), command=backCommand) #Back to menu button
backButton.place(x=2, y=2)

quitButton = tk.Button(wringus, text="Quit", highlightbackground="#35f4a6", fg="black", font=("Proxima Nova", 20), command=quit) #Quit application button
quitButton.place(x=1391, y=2)

labelOfAppreciation = tk.Label(wringus, text = "A Special Thanks to Ms. R. Peterson", fg="white", font=("Proxima Nova", 12)) #Thanking my AP Statistics teacher for giving me the stats knowledge to program this applicaiton
labelOfAppreciation.config(bg="#1c1c1c")
labelOfAppreciation.place(x=610, y=750)

tk.mainloop() #Tkinter mainloop functions the same as a while true, running all of the code constantly.