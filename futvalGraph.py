#PseudoCode

#Get principal amount, interest rate, and number of years
#initialize graphics window
#add labels from 0 to the m
#use a for look to calculate the amount in the account for each year with a for loop

from graphics import *

def incrementFind(valueList, interval):
    if (valueList[-1] // interval) < 20:
        return interval
    else:
        interval = interval + 1000
        return incrementFind(valueList, interval)

def incrementSize(valueList):
    interval = incrementFind(valueList, 1000)
    incrementRoundValue = [1000, 5000, 10000, 25000, 50000, 100000, 250000, 500000]
    incrementChanges = [0, 10000, 25000, 100000, 500000, 1000000, 5000000, 10000000, 100000000]
    changeIndex = 0
    sizeIndex = 0
    for element in incrementChanges:
        if interval > element:
            changeIndex += 1
        else:
            break
    sizeIndex = changeIndex - 1
    return incrementRoundValue[sizeIndex], interval


def incrementRound(valueList):
    roundRoot, interval = incrementSize(valueList)
    return ((interval//roundRoot)+1) * roundRoot


    
def printLabels(win, valueList):
    loopCount = 0
    labelValue = float(0)
    interval = incrementRound(valueList)
    yIncrement = (win.getHeight() - 40) / (valueList[-1] // interval )
    if valueList[-1] <= 1000000:
        while labelValue <= valueList[-1]:
            labelValueReduced = labelValue / 1000
            labelString = str(labelValueReduced) + 'K'
            Text(Point(20, (490 - (loopCount * yIncrement))), labelString).draw(win)
            labelValue = float(labelValue + interval)
            loopCount = loopCount + 1
            
    if valueList[-1] > 1000000:
        while labelValue <= valueList[-1]:
            labelValueReduced = labelValue / 1000000
            labelString = str(labelValueReduced) + 'M'
            Text(Point(20, (490 - (loopCount * yIncrement))), labelString).draw(win)
            labelValue = float(labelValue + interval)
            loopCount = loopCount + 1
    return loopCount, interval
            
def drawColumns(win, valueList, loopCount, interval, years):
    columnWidth = (win.getWidth()-50) // years
    columnScale = 460 / valueList[-1]
    columnCount = 0
    for value in valueList:
        columnHeight = columnScale * value
        bottomLeftX = (50 + (columnWidth * columnCount))
        bottomLeft = (bottomLeftX, 0)
        topRightX = bottomLeftX + columnWidth
        topRightY = 490 - (value * columnScale)
        topRight = (topRightX, topRightY)
        growthBar = Rectangle(Point(bottomLeftX, 490), Point(topRightX, topRightY))
        growthBar.draw(win)
        columnCount += 1
        
def drawWin(years, valueList):
    win = GraphWin('Investment Value', 500, 500)
    columnWidth = (win.getWidth()-40) // years
    loopCount, interval = printLabels(win, valueList)
    drawColumns(win, valueList, loopCount, interval, years)
    totalString = ("Final value: "+str(valueList[-1]))
    Text(Point(250, 40), totalString).draw(win)
    input("Press enter to close graph window")
    GraphWin.close(win)
                   
def futureValue():
    principal = float(input("Please enter the amount of money that will be invested: "))
    years = int(input("Enter the number of years the money will be invested: "))
    interestRate = float(input("Enter the expected average APR as a decimal: "))
    valueList = [principal]
    for i in range(years):
        value = principal *((1+interestRate)**(i+1))
        valueList.append(round(value,2))
    return valueList, (years+1)

def main():
    valueList, years = futureValue()
    drawWin(years, valueList)

if '__name__' == '__main__':
    main()
        
    
    
