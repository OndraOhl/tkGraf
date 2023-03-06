import scipy.interpolate as inp
import pylab as lab

x= [0, 0.3, 0.5, 0.8, 1,  2,  3 ]
y= [0, 0.1, 0.5, 1,   3, 10, 30]

#nebo
x= "0 0.3 0.5 0.8 1  2  3".split()
y= "0 0.1 0.5 1   3 10 30".split()

x = list(map(float, x))
y = list(map(float, y))

lab.plot(x, y, "o", color="red")

spl = inp.CubicSpline(x, y)
newX = lab.linspace(0, 3, 2000)
newY = spl(newX)
lab.plot(newX, newY, ":", label="CubicSpline")

spl = inp.UnivariateSpline(x,y, k=4)
newY = spl(newX)
lab.plot(newX, newY, ":", label="make_interspline")


lab.grid()
lab.legend()
lab.show()