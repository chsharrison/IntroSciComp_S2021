# -*- coding: utf-8 -*-
#5 intelligently named lists
f_name = ["John", "Amy", "Armando", "Jeremiah", "Lila"]
l_name = ["Adams", "Richardson", "Ramirez", "Bryanns", "Downs"]
height = [1.25, 1.52, 1.76, 1.83, 1.52]
weight = [60, 75, 68, 64, 50]
age = ["16", "24", "32", "56", "29"]
BMI = [] 
obese = []

#create a list to calculate BMI of each individual
#start from the beginning of 0 and stop at the length in height
for i in range(0,len(height)):
    BMI.append(weight[i]/(height[i]*height[i]))
    
#cdc.gov has a nice label for classifying BMI    

for i in range(0,len(BMI)):
    if BMI[i] < 18.5:
        obese.append("underweight")
    elif ((BMI[i] >= 18.5) and (BMI[i] <= 25)):
        obese.append("normal")
    elif ((BMI[i] > 25) and (BMI[i] < 30)):
        obese.append("overweight")
    else:
        obese.append("obese")
    
BMIlist = []
for i in range(0, len(BMI)):
    BMIlist.append(str(BMI[i]))

for i in range(0, len(height)):
    print(f_name[i] + " " + l_name[i] + ", " + str(age[i]) + ", has a height of " + str(height[i]) + "m and weight of " + str(weight[i]) + "kg, giving them a body mass index of "+ BMIlist[i] + " making them " + obese[i])
    
              