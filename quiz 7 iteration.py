cm = [10,20,30,40,50] # centimeter

#convert cm -> inch

inches = [round(n*0.393701,2) for n in cm]

print(cm,inches)