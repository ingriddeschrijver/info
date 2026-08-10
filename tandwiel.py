import turtle as pen
from math import sin, tan, sqrt, pi

pen.speed(0)
r = 100 #straal tandwiel
d = 5 # rechtlijnig stuk tanden
x = 20 # aantal tanden
beta = pi/4 # hoek rechtlijnig stuk tanden met straal
alfa = pi/(2*x) # hoek halve tand
r_tand_buiten = tan(beta-alfa)*(sin(alfa)*r/sin(beta-alfa)-d)
print('r_tand buiten',r_tand_buiten)
hoek_cirkel_tand_graden_buiten = 180 + (2*alfa-2*beta)*180/pi
print('hoek_Cirkel_tand buiten',hoek_cirkel_tand_graden_buiten)

r_tand_binnen = tan(beta+alfa)*(sin(alfa)*r/sin(pi-beta-alfa)-d)
print('r_tand binnen',r_tand_binnen)
hoek_cirkel_tand_graden_binnen = 180 - (2*alfa+2*beta)*180/pi
print('hoek_Cirkel_tand binnen',hoek_cirkel_tand_graden_binnen)
#ga naar startpunt
pen.up()
pen.goto(r,0)

pen.down()


for i in range(x):
    pen.forward(d)
    pen.circle(-r_tand_buiten, hoek_cirkel_tand_graden_buiten)
    pen.forward(2*d)
    pen.circle(r_tand_binnen, hoek_cirkel_tand_graden_binnen)
    pen.forward(d)
    

def teken_tand(r,d,x,beta,r_tand):
    pen.forward(d)
    pen.circle(-r_tand, pi + 2*alfa-2*beta)
    pen.color('red')
    pen.backward(20*x)
    pen.color('green')
    pen.right(45)
    pen.circle(-20*x,-90)
    pen.color('blue')
    pen.right(45)
    pen.backward(20*x)
    pen.color('indigo')
    pen.circle(20*x,180)
    pen.backward(20*x)
    pen.right(45)
    pen.circle(-20*x,-90)
    pen.right(45)
    pen.backward(20*x)
    pen.penup()
    pen.left(90)
    pen.forward(30*x)
    pen.pendown()
    pen.circle(5*x)
    pen.penup()
    pen.forward(10*x)
    pen.right(90)
    pen.pendown()


pen.exitonclick()