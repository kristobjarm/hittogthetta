import math 
import copy 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
from mpl_toolkits.mplot3d import Axes3D
import sympy as sym

# Defining known variables 
F = 100 #N
t = 1 #mm 
E = 1500 #MPa - N/mm2
nu = 0.3
xi, eta = sym.symbols('xi eta')
X = sym.Matrix(1,6, [1, xi, eta, xi*eta, xi**2, xi**2*eta])

######## PROBLEM 1 ########

#xi and eta derived from refrence figure 
#              Node =  1,  2, 3,  4,  5, 6
xi_vec = sym.Matrix([ -1,  1, 1, -1,  0, 0])#*1e-3
eta_vec = sym.Matrix([-1, -1, 1,  1, -1, 1])#*1e-3

Ngrid = sym.zeros(6,6)
for i in range(6):
    Ngrid[i, :] = sym.Matrix(1, 6, 
        [1, xi_vec[i], eta_vec[i], xi_vec[i]*eta_vec[i], 
        xi_vec[i]**2, xi_vec[i]**2*eta_vec[i]])

N = X*Ngrid.inv()  # a simplified 1x6 Shape function vector


xi_m = np.linspace(-1.0, 1.0, num=20)
eta_m = np.linspace(-1.0, 1.0, num=20)
xi_m, eta_m = np.meshgrid(xi_m, eta_m)

# coverting N1 and N5 to a numpy functions of xi and eta
N1 = sym.lambdify((xi, eta), N[0], 'numpy') 
N5 = sym.lambdify((xi, eta), N[4], 'numpy')

#PLOTTING# 
xh = [1, 1, -1, -1, 1]
yh = [1, -1, -1, 1, 1]
zh = [0, 0, 0, 0, 0]
fig = plt.figure(figsize=(9,5))
#First plot
ax = fig.add_subplot(1, 2, 1, projection= '3d')
surf = ax.plot_surface(xi_m, eta_m, N1(xi_m,eta_m), cmap=cm.viridis,
                       linewidth=0)
ax.plot(xh, yh, zh, '--', color='grey', alpha=0.5)
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-2, 2])
ax.set_xlabel(r'$\xi$')
ax.set_ylabel(r'$\eta$')
#ax.grid(False)
ax.zaxis.set_major_locator(LinearLocator(5))
ax.set_xticks([-1,0,1], ['-1', '0', '1'])
ax.set_yticks([-1,0,1], ['-1', '0', '1'])
ax.set_zticks([-2,0,2], ['-2', '0', '2'])
ax.xaxis.set_tick_params(pad=-4, labelsize=10)
ax.yaxis.set_tick_params(pad=-4, labelsize=10)
ax.zaxis.set_tick_params(pad=-4, labelsize=10)
ax.set_proj_type('ortho')
ax.grid(False)
fig.colorbar(surf, orientation='horizontal', anchor =(0.6, 2.2), shrink=0.83)
ax.view_init(30,-60)

#Second plot 
ax = fig.add_subplot(1, 2, 2, projection= '3d')
surf = ax.plot_surface(xi_m, eta_m, N5(xi_m,eta_m), cmap=cm.viridis,
                       linewidth=0)
ax.plot(xh, yh, zh, '--', color='grey', alpha=0.5)
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-2, 2])
ax.set_xlabel(r'$\xi$')
ax.set_ylabel(r'$\eta$')
#ax.grid(False)
ax.zaxis.set_major_locator(LinearLocator(5))
ax.set_xticks([-1,0,1], ['-1', '0', '1'])
ax.set_yticks([-1,0,1], ['-1', '0', '1'])
ax.set_zticks([-2,0,2], ['-2', '0', '2'])
ax.xaxis.set_tick_params(pad=-4, labelsize=10)
ax.yaxis.set_tick_params(pad=-4, labelsize=10)
ax.zaxis.set_tick_params(pad=-4, labelsize=10)
ax.set_proj_type('ortho')
ax.grid(False)
fig.colorbar(surf, orientation='horizontal', anchor =(0.6, 2.2), shrink=0.83)
ax.view_init(30, -60)

plt.savefig('N1N5.jpg', dpi=300)
plt.show()


######## PROBLEM 2 ########

xy = np.array([[1, 5, 5, 1, 3, 3],[1, 1, 3, 3, 1, 3]]).T

N_diff = N.jacobian([xi, eta]).T
Jac = N_diff * xy
J = sym.det(Jac)

######## PROBLEM 3 ########

# form 6.2-9
# Transformation matrix 
T = sym.Matrix([[1,0,0,0],[0,0,0,1],[0,1,1,0]])

# from 6.2-10 
Gamma = Jac.inv()
# Expanded Gamma 
Gamma_exp = sym.zeros(4,4)
Gamma_exp[0:2, 0:2] = Gamma
Gamma_exp[2:4, 2:4] = Gamma

# Expanded derivative of shape-function-matrix 
Nshape = sym.Matrix([
    [N[0], 0,  N[1], 0,  N[2], 0,  N[3], 0,  N[4], 0,  N[5], 0],
    [ 0,  N[0], 0,  N[1], 0,  N[2], 0,  N[3], 0,  N[4], 0,  N[5]]])
# from 6.2-11
dN_exp = sym.Matrix([[Nshape[0,:].jacobian([xi, eta]).T], 
                     [Nshape[1,:].jacobian([xi,eta]).T]])

B = T * Gamma_exp * dN_exp

######## PROBLEM 4 ########

# Constitutive matrix E for plane stress
Emat = E/(1-nu**2)*np.array([[1, nu, 0],[nu, 1, 0],[0, 0, (1-nu)/2]])
intfunc = B.T*Emat*B*t*J

# Three points in the i-direction and 2 in j-direction 
# Total of 6 integration points

xiset = [np.sqrt(0.6), 0, -np.sqrt(0.6)]
wi = [5/9, 8/9, 5/9]
etaset = [1/np.sqrt(3), -1/np.sqrt(3)]
wj = [1, 1]

KE = np.zeros([12,12])

for i, vali in enumerate(xiset):
    for j, valj in enumerate(etaset):
        Kpart = intfunc.subs([(xi, vali), (eta, valj)]) * wi[i] * wj[j]
        KE = KE + Kpart

######## PROBLEM 5 ########

# Given that the boundary condition are u5,v5,u6,v6 = 0 
u1, v1, u2, v2, u3, v3, u4, v4 = sym.symbols('u1 v1 u2 v2 u3 v3 u4 v4')
Rc = sym.Matrix([F, 0, -F, 0, F, 0, -F, 0])
Dx = (u1, v1, u2, v2, u3, v3, u4, v4)
KE11 = KE[0:8,0:8]
sol1, = sym.linsolve((KE11, Rc), Dx) 
print('u1 = %.7f, v1 = %.7f, u2 = %.7f, v2 = %.7f' % sol1.args[0:4])
print('u3 = %.7f, v3 = %.7f, u4 = %.7f, v4 = %.7f' % sol1.args[4:8])

#np.set_printoptions(precision=8)
d = np.zeros([12,1])
d[0:8] = d[0:8] + np.asarray([sol1.args[0:8]], dtype=object).T

######## PROBLEM 6 ########

epsilon = B*d
epsilon
epsx = sym.lambdify((xi, eta), epsilon[0], 'numpy')
xh = [1, 1, -1, -1, 1]
yh = [1, -1, -1, 1, 1]

xstrain_top = [0, epsx(0,1), 0, 0]
ystrain_top = [1,1,0,1]
xstrain_bot = [0, 0, epsx(0,-1), 0]
ystrain_bot = [0,-1,-1,0]

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1, 1, 1)
ax.plot(xh, yh, color='black')
ax.plot([-1,1], [0,0], '--', color='grey', label='Neutral axis')
ax.plot(xstrain_top, ystrain_top, color='green', label='Tension')
ax.fill(xstrain_top, ystrain_top, 'green', alpha=0.5)
ax.plot(xstrain_bot, ystrain_bot, color='red', label='Compression')
ax.fill(xstrain_bot, ystrain_bot, 'red', alpha=0.5)
ax.axis('equal')
ax.set(xlim=[-1.5,1.5], ylim=[-1.5,1.5])
ax.set_xlabel(r'$\xi$ [mm]')
ax.set_ylabel(r'$\eta$ [mm]')
ax.legend()


plt.savefig('p6.jpg', dpi=300)
plt.show()

######## PROBLEM 7 ########

# Creating undeformed points
undefx = np.array([1, 3, 5, 5, 3, 1, 1])
undefy = np.array([1, 1, 1, 3, 3, 3, 1])

# Computing points after deformation
defx = xy[:,0] + np.array([d[0], d[2], d[4], d[6], d[8], d[10]]).T
defy = xy[:,1] + np.array([d[1], d[3], d[5], d[7], d[9], d[11]]).T

# Creating functions that give the x y at any given xi ant eta. 
xf = N*sym.Matrix(defx.T)
yf = N*sym.Matrix(defy.T)
xf = sym.lambdify((xi, eta), xf, 'numpy')
yf = sym.lambdify((xi, eta), yf, 'numpy')

span = np.linspace(-1.0, 1.0, 1000)

# frist plot
fig = plt.figure(figsize=(9,5))
ax = fig.add_subplot(1, 1, 1)
ax.plot(undefx, undefy, color='black', label='Undeformed')
ax.scatter(undefx, undefy, marker='o', color='black', s=70)
ax.plot(xf(span,1)[0][0], yf(span, 1)[0][0], color='orange', label='Deformed')
ax.plot(xf(span,-1)[0][0], yf(span, -1)[0][0], color='orange')
ax.plot(xf(-1,span)[0][0], yf(-1, span)[0][0], color='orange')
ax.plot(xf(1,span)[0][0], yf(1, span)[0][0], color='orange')
ax.scatter(defx, defy, marker='o' , color='orange', s=30, zorder=2)
ax.axis('equal')
ax.set(xlabel='x [mm]', ylabel='y [mm]', xlim=[0,6], ylim=[0,4])
ax.legend()
#ax.set()

plt.savefig('p7.jpg', dpi=300)
plt.show()

xi_m2 = np.linspace(-1.0, 1.0, num=21)
eta_m2 = np.linspace(-1.0, 1.0, num=21)
xi_m2, eta_m2 = np.meshgrid(xi_m2, eta_m2)
disx = xf(xi_m2, eta_m2)[0][0]
disy = yf(xi_m2, eta_m2)[0][0]
x_m = np.linspace(1, 5, num=21)
y_m = np.linspace(1, 3, num=21)
x_m, y_m = np.meshgrid(x_m, y_m)
mag = np.sqrt((disx-x_m)**2+(disy-y_m)**2)

# second plot 
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1, 1, 1, projection='3d')
surf = ax.plot_surface(disx,disy, mag, cmap=cm.viridis,
                       linewidth=0)


ax.axis('equal')
ax.set_xlabel('x [mm]')
ax.set_ylabel('y [mm]')
ax.set_zticks([], [])
ax.xaxis.set_tick_params(pad=2, labelsize=10)
ax.yaxis.set_tick_params(pad=2, labelsize=10)
ax.zaxis.set_tick_params(pad=2, labelsize=10)
ax.set_proj_type('ortho')
#ax.grid(False)
cbar = fig.colorbar(surf, orientation='horizontal', 
            anchor =(0.5, 2.5), shrink=0.6, )
ax.view_init(90, -90)
plt.savefig('p72.jpg',dpi=300)
plt.show()