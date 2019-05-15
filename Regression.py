from math import *

##The Regression Technique

##Plotting it on a graph, and extrapolating the correlation
##Work the equation of the line, then calculate the y-value for any x-value or vice-versa
##Two characteristics of the line, the gradient and the y-intercept
## y = mx + c  where the gradient is m and c is the y intercept
## gradient is worked out using  (ysub1 - ysub2) / (xsub1 - xsub2)
## c = y - mx
##

x1 = 1
x2 = 2

print("I am an artificial intelligence that will calculate the correlation between sets of data. I will tell you x values and you put in coreesponding y values.\n")
print("X Values\tY Values \n", x1, "\n", x2)

y1 = int(input("\n Enter the first y value")) ##Ask for the first corresponding y value

print("\nX Values\tY Values \n", x1, "\t\t", y1, "\n", x2) ##print out their input into the chart

y2 = int(input("\n Enter the the second y value")) ##Ask for the second corresponding y value

print("\nX Values\tY Values \n", x1, "\t\t", y1, "\n", x2, "\t\t", y2) ##print out their input into the chart

slope = ((y1 - y2) / (x1 - x2))##Calculate the slope

intercept = (y1 - slope) ##Calculate the intercept


print ("When x = 3, y would equal", (slope * 3 + intercept)) ##Print what ysub3 woudl be when xsub3 = 3


