#File
import math as ma
# To use a math function, write "ma." in front of it.  Example:  ma.sin(3.146)
import numpy as np
#Import Data File
data_file = open("planet_data.dat")
planet_data = []
for line in data_file:
    print(line) 
# Given Mass of explorer (kg)
m = 60

# Grav. Constant
G = 6.667*(10**-11)

#Input name of planet and elevation
planet = str(input("Kepler-37b, press enter"))
h = int(input("Elevation on Kepler-37b?: "))

#Input value for Kepler 37-b gravity
pgrav = int(input("Gravity on Kepler-37b?: "))
#Creating empty lists to fill
planet_list = []
radius_list = []
density_list = [] 
infile = open("planet_data.dat")
#removing the # from the first line
for line in infile:
    if line[0] == "#":
        continue
#removing the semi colon and units from values
    temp = line.split()
    planet_list.append(temp[0].strip(";"))
    radius_list.append(temp[1].strip("km"))
    density_list.append(temp[3].strip("g/cm^3"))
    #print(planet_list)
    #print(radius_list)
    #print(density_list)
    
#create floats for radius list and X1000 to go to meters
r = float_radius_list = [float(a) for a in radius_list] 
for a in r:
    r = np.multiply(a,1000)
    r = r+h
    #print(r)

for a in float_radius_list:
    ma.pow(r,3)
    print(r)
#Create floats for density and X1000
d = [float(b) for b in density_list]  
for b in d:
    d = np.multiply(b,1000)
    #print(d)
   
v = (4/3)*ma.pi*(r**3) 
#print(v)  
pmass = v * d
#print(pmass, "kg")

#Fg is given when on Kepler 37-b
Fg = (G*pmass*m)/r**2
print("weight on Kepler-37b is", Fg, "N" )

gforce = pgrav/9.81
print("g force is",pgrav/9.8, "G's")     
