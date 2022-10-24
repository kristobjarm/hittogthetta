clear all 
close all
syms x y 
B = 0.2; 
v = -B*x*y^3;
dvdy = diff(v,y);
dudx = -dvdy;
u = int(dudx,x)

[x,y] = meshgrid(0:0.2:6,0:0.2:6);
u = eval(u)
v = eval(v)

hold on 
xlim([0 5])
ylim([0 5])
quiver(x,y,u,v)
psi14 = (1^2*4^3)/10;
psi24 = (2^2*4^3)/10;
y14 = @(x) ((10*psi14)./x.^2)^(1/3) 
y24 = @(x) ((10*psi24)./x.^2)^(1/3) 
fplot(y14)
fplot(y24)
text(1,4,'   (1,4)')
text (2,4,'   (2,4)');
plot(1,4,'-o','MarkerSize',5,'MarkerEdgeColor','k')
plot(2,4,'-o','MarkerSize',5,'MarkerEdgeColor','k')
hold off
