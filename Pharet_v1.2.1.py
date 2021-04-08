import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import tkinter.messagebox
import math
import sympy as sy
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

root = tk.Tk()
root.wm_title("Pharet")
ratio = 700/450
height = int(root.winfo_screenheight()/2)
width = int(ratio*height)
root.geometry(f"{width}x{height}")

font_style = tkFont.Font(family="Courier", size=int(width/60))
results_style = tkFont.Font(family="Courier", size=int(width/50))

tbdeg=tk.IntVar()
dtdeg=tk.IntVar()
lensType=tk.StringVar()

canvas = tk.Canvas(root, bg='#b49e83') 	#sets up the window size and color
canvas.place(relwidth=1, relheight=1, relx=0, rely=0)

frame1 = tk.Frame(root, bd=0.1)
frame1.place(relwidth=0.3, relheight=0.12, relx=0.05, rely=0.075)	#places a frame for other elements within the window

buttonsi = tk.Button(frame1, bg='#848482', text='Silicon', font=font_style)	#Creates the silicone button
buttonsi.place(relwidth=0.5, relheight=1)

buttondmnd = tk.Button(frame1, bg='#848482', text='Diamond', font=font_style)	#creates the diamond button(ADD MORE ENTRYS FOR t AND eV)
buttondmnd.place(relwidth=0.5, relheight=1, relx=0.5)

framegrpr = tk.Frame(root, bd=0.1)
framegrpr.place(relwidth=0.4, relheight=0.12, relx=0.5, rely=0.555)

buttongr = tk.Button(framegrpr, bg='#696969', text='Graph', font=font_style)	#Creates the silicone button
buttongr.place(relwidth=0.5, relheight=1)

buttonpr = tk.Button(framegrpr, bg='#696969', text='Print', font=font_style)	#creates the diamond button(ADD MORE ENTRYS FOR t AND eV)
buttonpr.place(relwidth=0.5, relheight=1, relx=0.5)

frameentry = tk.Frame(root, bd=0.1)
frameentry.place(relheight=0.6, relwidth=0.3, relx=0.05, rely=0.25)		#creates another frame for entrys

labelh = tk.Label(frameentry, bd=0.1, bg='#4f7171', text='H:', font=font_style)	#label for variable 1
labelh.place(relheight=0.2, relwidth=0.4, anchor='nw')

entryh = tk.Entry(frameentry, bd=0.1, bg='#759696', font=font_style)	 	#entry for variable 1
entryh.place(relheight=0.2, relwidth=0.6, relx=0.4, rely=0)

labelk = tk.Label(frameentry, bd=0.1, bg='#696969', text='K:', font=font_style) #label for variable 2
labelk.place(relheight=0.2, relwidth=0.4, rely=0.2, relx=0)

entryk = tk.Entry(frameentry, bd=0.1, bg='#848482', font=font_style)
entryk.place(relheight=0.2, relwidth=0.6, relx=0.4, rely=0.2)		#entry for variable 2

labell = tk.Label(frameentry, bd=0.1, bg='#4f7171', text='L:', font=font_style) 	#label for variable 3
labell.place(relheight=0.2, relwidth=0.4, rely=0.4, relx=0)

entryl = tk.Entry(frameentry, bd=0.1, bg='#759696', font=font_style)
entryl.place(relheight=0.2, relwidth=0.6, relx=0.4, rely=0.4) 	#entry for variable 3

labelt = tk.Label(frameentry, bd=0.1, bg='#696969', text='thickness(μm):', font=font_style ) 	
labelt.place(relheight=0.2, relwidth=0.5, rely=0.6, relx=0)

entryt = tk.Entry(frameentry, bd=0.1, bg='#848482', font=font_style)
entryt.place(relheight=0.2, relwidth=0.5, relx=0.5, rely=0.6) 

labeleV = tk.Label(frameentry, bd=0.1, bg='#4f7171', text='energy(eV):', font=font_style ) 	
labeleV.place(relheight=0.2, relwidth=0.5, rely=0.8, relx=0)

entryeV = tk.Entry(frameentry, bd=0.1, bg='#759696', font=font_style)
entryeV.place(relheight=0.2, relwidth=0.5, relx=0.5, rely=0.8) 

frameres = tk.Frame(root, bd=0.1)
frameres.place(relheight= 0.4, relwidth=0.4, relx=0.5, rely=0.1)	#frame for results

labelres = tk.Label(frameres, bd=0.1, bg='#696969', text='Results for Crystal Type:', font=results_style) 	#title for results
labelres.place(relheight=0.15, relwidth=1)

labelres = tk.Label(frameres, bd=0.1, bg='#696969', textvariable=lensType, font=results_style) 	#title for results
labelres.place(relheight=0.15, relwidth=1, rely=0.15)

labelang = tk.Label(frameres, bd=0.1, bg='#4f7171', text='Bragg Angle', font=results_style) 	#label for angle
labelang.place(relheight=0.35, relwidth=0.5, rely=0.3)

labelresang = tk.Label(frameres, bd=0.1, bg='#759696', textvariable=tbdeg, font=results_style) 		#angle text box
labelresang.place(relheight=0.35, relwidth=0.5, rely=0.3, relx=0.5)

labeloff = tk.Label(frameres, bd=0.1, bg='#696969', text='Offset (Pc=1)', font=results_style) 	#label for offset
labeloff.place(relheight=0.35, relwidth=0.5, rely=0.65)

labelresoff = tk.Label(frameres, bd=0.1, bg='#848482', textvariable=dtdeg, font=results_style) 	#offset text box
labelresoff.place(relheight=0.35, relwidth=0.5, rely=0.65, relx=0.5)

ident=0

deltathetadeg=0
thetabdiamdeg=0
thetabsildeg=0

h=0
k=0
l=0
t=0
eV=0
#coordinate arrays
arrx=[]
arry=[]
arrsin=[]

#diamond and silicone specific variables
x1=0.1250
y1=0.1250
z1=0.1250

x2=0.8750
y2=0.8750
z2=0.8750

x3=0.6250
y3=0.6250
z3=0.1250

x4=0.3750
y4=0.3750
z4=0.8750

x5=0.1250
y5=0.6250
z5=0.6250

x6=0.8750
y6=0.3750
z6=0.3750

x7=0.6250
y7=0.1250
z7=0.6250

x8=0.3750
y8=0.8750
z8=0.3750

##test function

def truncate(number, decimals):
    """
    Returns a value truncated to a specific number of decimal places.
    """
    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor

##test function

def calcdiam():

	try:
		buttondmnd.configure(bg="#759696")
		buttonsi.configure(bg="#848482")

		lensType.set('Diamond')

		global ident
		ident=1

		global h
		global k
		global l
		global t
		global eV

		h=int(entryh.get())
		k=int(entryk.get())
		l=int(entryl.get())
		t=int(entryt.get())
		eV=int(entryeV.get())
		tm=t*10**4
		Re=2.81794*10**-5
		wavel=12398.506/eV

		adaim=3.567
		ddiam=3.567/(math.sqrt(h**2+k**2+l**2))
		Vdiam=3.567**3
		thetabdiam=math.asin(wavel/(2*ddiam))
		changethetadiam=0

		#fh summation
		pi = 3.141592653589793
		e = 2.7182818284590452
		s = 1/(2*ddiam)
		a = complex(0, 1)

		f0carbon=((2.31*e**(-20.844*s**2))+(1.02*e**(-10.208*s**2))+(1.589*e**(-0.569*s**2))+(0.865*e**(-51.651*s**2))+0.216)

		FminH = (f0carbon*e**(-2*pi*a*(h*x1+k*y1+l*z1)))+(f0carbon*e**(-2*pi*a*(h*x2+k*y2+l*z2)))+(f0carbon*e**(-2*pi*a*(h*x3+k*y3+l*z3)))+(f0carbon*e**(-2*pi*a*(h*x4+k*y4+l*z4)))+(f0carbon*e**(-2*pi*a*(h*x5+k*y5+l*z5)))+(f0carbon*e**(-2*pi*a*(h*x6+k*y6+l*z6)))+(f0carbon*e**(-2*pi*a*(h*x7+k*y7+l*z7)))+(f0carbon*e**(-2*pi*a*(h*x8+k*y8+l*z8)))
		FplusH = (f0carbon*e**(2*pi*a*(h*x1+k*y1+l*z1)))+(f0carbon*e**(2*pi*a*(h*x2+k*y2+l*z2)))+(f0carbon*e**(2*pi*a*(h*x3+k*y3+l*z3)))+(f0carbon*e**(2*pi*a*(h*x4+k*y4+l*z4)))+(f0carbon*e**(2*pi*a*(h*x5+k*y5+l*z5)))+(f0carbon*e**(2*pi*a*(h*x6+k*y6+l*z6)))+(f0carbon*e**(2*pi*a*(h*x7+k*y7+l*z7)))+(f0carbon*e**(2*pi*a*(h*x8+k*y8+l*z8)))

		FinFH = np.real(FminH*FplusH)

		deltatheta = (tm*math.sin(2*thetabdiam)*(pi/2)*(((Re*wavel**2)/(pi*Vdiam))**2)*FinFH)/((pi/2)*math.sin(thetabdiam)*wavel)

		global deltathetadeg
		global thetabdiamdeg

		deltathetadeg = (deltatheta/(2*pi))*360

		dtdeg.set(truncate(deltathetadeg,6))

		thetabdiamdeg = (thetabdiam/(2*pi))*360

		tbdeg.set(truncate(thetabdiamdeg,6))

		#use data frames for printing this to txt!
		global arrx
		global arry
		global arrsin
		arrx=[]
		arry=[]
		arrsin=[]
		g=1
		whiletemp=0
		while(g<=200):
			arrx.append(whiletemp*(180/pi))
			whiletemp=g*5*10**-6
			arry.append(FinFH*((Re*wavel**2)/(pi*Vdiam))**2*((tm*math.sin(2*thetabdiam))/(wavel*math.sin(thetabdiam)*whiletemp)))
			arrsin.append(math.sin((pi/2)*arry[g-1]))
			g=g+1
	except Exception:
		tkinter.messagebox.showinfo('Error','You have entered an invalid value')


def calcsi():

	try:
		buttondmnd.configure(bg="#848482")
		buttonsi.configure(bg="#759696")

		lensType.set('Silicon')

		global ident
		ident=2

		global h
		global k
		global l
		global t
		global eV

		h=int(entryh.get())
		k=int(entryk.get())
		l=int(entryl.get())
		t=int(entryt.get())
		eV=int(entryeV.get())
		tm=t*10**4
		Re=2.81794*10**-5
		wavel=12398.506/eV

		asil=5.4300
		dsil=5.43/(math.sqrt(h**2+k**2+l**2))
		Vsil=5.43**3
		thetabsil=math.asin(wavel/(2*dsil))

		#fh summation
		pi = 3.141592653589793
		e = 2.7182818284590452
		s = 1/(2*dsil)
		a = complex(0, 1)

		f0silicon=((6.292*e**(-2.439*s**2))+(3.035*e**(-32.334*s**2))+(1.989*e**(-0.678*s**2))+(1.541*e**(-81.694*s**2))+1.141)


		FminH = (f0silicon*e**(-2*pi*a*(h*x1+k*y1+l*z1)))+(f0silicon*e**(-2*pi*a*(h*x2+k*y2+l*z2)))+(f0silicon*e**(-2*pi*a*(h*x3+k*y3+l*z3)))+(f0silicon*e**(-2*pi*a*(h*x4+k*y4+l*z4)))+(f0silicon*e**(-2*pi*a*(h*x5+k*y5+l*z5)))+(f0silicon*e**(-2*pi*a*(h*x6+k*y6+l*z6)))+(f0silicon*e**(-2*pi*a*(h*x7+k*y7+l*z7)))+(f0silicon*e**(-2*pi*a*(h*x8+k*y8+l*z8)))
		FplusH = (f0silicon*e**(2*pi*a*(h*x1+k*y1+l*z1)))+(f0silicon*e**(2*pi*a*(h*x2+k*y2+l*z2)))+(f0silicon*e**(2*pi*a*(h*x3+k*y3+l*z3)))+(f0silicon*e**(2*pi*a*(h*x4+k*y4+l*z4)))+(f0silicon*e**(2*pi*a*(h*x5+k*y5+l*z5)))+(f0silicon*e**(2*pi*a*(h*x6+k*y6+l*z6)))+(f0silicon*e**(2*pi*a*(h*x7+k*y7+l*z7)))+(f0silicon*e**(2*pi*a*(h*x8+k*y8+l*z8)))

		FinFH = np.real(FminH*FplusH)

		deltatheta = (tm*math.sin(2*thetabsil)*(pi/2)*(((Re*wavel**2)/(pi*Vsil))**2)*FinFH)/((pi/2)*math.sin(thetabsil)*wavel)

		global deltathetadeg
		global thetabsildeg

		deltathetadeg = (deltatheta/(2*pi))*360

		dtdeg.set(truncate(deltathetadeg,6))

		thetabsildeg = (thetabsil/(2*pi))*360

		tbdeg.set(truncate(thetabsildeg,6))

		##under construction (while loop creates arrays of x and y coords of graph)\
		global arrx
		global arry
		global arrsin
		arrx=[]
		arry=[]
		arrsin=[]
		g=1
		whiletemp=0
		while(g<=200):
			arrx.append(whiletemp*(180/pi))
			whiletemp=g*5*10**-6
			arry.append(FinFH*((Re*wavel**2)/(pi*Vsil))**2*((tm*math.sin(2*thetabsil))/(wavel*math.sin(thetabsil)*whiletemp)))
			arrsin.append(math.sin((pi/2)*arry[g-1]))
			g=g+1
	except Exception:
		tkinter.messagebox.showinfo('Error','You have entered an invalid value')


def genGraph():

	fig , ax = plt.subplots(nrows = 2, ncols = 1, figsize=(8,6))
 
	#Plotting on the 1st axes
	ax[0].set_ylim([0,2])
	ax[0].set_xlabel('Offset(degrees)')
	ax[0].set_ylabel('Phase(pi/2)')
	ax[0].plot(arrx,arry, color = 'blue')
 
	#Plotting on the last axes
	ax[1].set_xlabel('Offset(degrees)')
	ax[1].set_ylabel('Sin(phase)')
	ax[1].plot(arrx,arrsin , color = 'orange')
	plt.show()

forcount=0
def genTXT():

	tkinter.messagebox.showinfo('Print Alert','Your results have been printed to the file PHAREToutput.txt in the same directory as the program. Change the name of the file if you do not want it to be overwritten by the next print.')

	global forcount
	forcount=0
	bang=0
	if(ident==1):
		bang=thetabdiamdeg

	if(ident==2):
		bang=thetabsildeg

	with open("PHAREToutput.txt","w") as f:
		f.write("#Output for h="+str(h)+" k="+str(k)+" l="+str(l)+" t(microns)="+str(t)+" eV="+str(eV)+'\n')
		if(ident==1):
			f.write("#Crystal Type: Diamond"+'\n')
		if(ident==2):
			f.write("#Crystal Type: Silicon"+'\n')
		f.write("#Bragg Angle(degrees)="+str(truncate(bang,6))+'\n')
		f.write("#Offset(degrees)="+str(truncate(deltathetadeg,6))+'\n')
		f.write("#Offset(degrees)   Phase(pi/2) 	 Sin(phase)"+'\n')
		for x in arrx:
			f.write(str(truncate(x,6))+"     "+str(truncate(arry[forcount],6))+"      "+str(truncate(arrsin[forcount],6))+'\n')
			forcount=forcount+1
		f.write('\n')
		f.write("#Credits to Lucas Ancieta and Dr.Daniel Haskel")



buttonpr.config(command=genTXT)
buttongr.config(command=genGraph)
buttonsi.config(command=calcsi)
buttondmnd.config(command=calcdiam)

root.mainloop()

#Credits to Lucas Ancieta and Dr.Daniel Haskell
