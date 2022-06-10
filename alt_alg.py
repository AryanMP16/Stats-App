from openpyxl import load_workbook
import xlwings as xw
import time

ROIlist = []

#load excel file
workbook = load_workbook("C:/Users/aryan/Documents/GitHub/Stats-App/EXCEL.xlsx")
 
#open workbook
sheet = workbook["Development by Block"]
sheetVal = workbook["Value"]

############ INITIALIZION OF VARIABLES:
sheet["E4"] = 0

############ VARIABLE LABELS:
#Specials:
phoenix = sheet["I17"]
yorkDry = sheet["M18"] #DOES NOT VARY
victorRow = sheet["Q19"]
#Block 1:
podium1 = sheet["E4"]
townhouse1 = sheet["E5"]
luxCondo1 = sheet["E6"]
homelessShelt1 = sheet["E7"]
lowOfficeONE1 = sheet["E9"]
lowOfficeTWO1 = sheet["E10"]
midOffice1 = sheet["E11"]
retail1 = sheet["E13"]
supermark1 = sheet["E14"]
qmart1 = sheet["E15"]
park1 = sheet["E21"]
sportsField1 = sheet["E22"]
skate1 = sheet["E23"]

############ LIST OF ACCEPTABLE VALUES:
podium1Vals = [0,1,2,3,4,5,6,7]
townhouse1Vals = [0,1,2,3,4,5,6,7]

####################################################################################
####################################################################################
####################################################################################
townhouseMaxVisualList = []
def townhouses():
    lgstTown1 = 0
    for i in range(len(townhouse1Vals)):
        #modify the desired cell
        sheet["E5"] = int(townhouse1Vals[i])
        
        #save the file
        workbook.save("C:/Users/aryan/Documents/GitHub/Stats-App/EXCEL.xlsx")

        ############ READ ROI:
        import xlwings as xw

        wbxl=xw.Book("C:/Users/aryan/Documents/GitHub/Stats-App/EXCEL.xlsx")
        ROI = wbxl.sheets['Value'].range('L46').value
        ROIlist.append(ROI*100)

        #detecting largest:
        if ROI >= lgstTown1:
            lgstTown1 = ROI
            townVis = (f"TOWNHOUSES ON BLOCK 1: {int(townhouse1Vals[i])}")
            townhouseMaxVisualList.append(townVis)
        else:
            pass

        app = xw.apps.active
        app.kill()

        time.sleep(0.5)
####################################################################################
####################################################################################
####################################################################################
start = time.time()
podiumMaxVisualList = []
def podiums():
    lgstPodium1 = 0
    for i in range(len(podium1Vals)):
        townhouses()
        #modify the desired cell
        sheet["E4"] = int(podium1Vals[i])
        
        #save the file
        workbook.save("C:/Users/aryan/Documents/GitHub/Stats-App/EXCEL.xlsx")

        ############ READ ROI:
        import xlwings as xw

        wbxl=xw.Book("C:/Users/aryan/Documents/GitHub/Stats-App/EXCEL.xlsx")
        ROI = wbxl.sheets['Value'].range('L46').value
        ROIlist.append(ROI*100)
        
        #detecting largest:
        if ROI >= lgstPodium1:
            lgstPodium1 = ROI
            podiumVis = (f"PODIUMS ON BLOCK 1: {int(podium1Vals[i])}")
            podiumMaxVisualList.append(podiumVis)
        else:
            pass

        app = xw.apps.active
        app.kill()

        time.sleep(0.5)

def findLargest():
    largest_number = ROIlist[0]
    for i in ROIlist:
        if i > largest_number:
            largest_number = i
    print(f"LARGEST ROI: {largest_number}")

podiums()
print(ROIlist)
findLargest()
end = time.time()
print(f"\nTIME: {(end-start)}")

oTown = len(townhouseMaxVisualList)
oPod = len(podiumMaxVisualList)
print(townhouseMaxVisualList[oTown - 1])
print(podiumMaxVisualList[oPod - 1])

####################################################################################
####################################################################################
####################################################################################
