
% 2april
% SS model

clc
clear

motormas = 0.110 %kg
platemas = 0.115 %kg
extraplatemas = 0 %0.104 %kg
blokmas = 0.020+0.009+0.001 %kg
motorplatemas = 0.015 %kg
servomass = 0  %kg


Tm = 0.0834 %Nm %max motor torque
Km = 0.00251 %Nm  A-1 %torque constant of the motor
g = 9.81

l = 0.075 %m
rw = 0.06 %m %wheel radious
mw = 0.018 %kg %wheel mass
b = 0.07 %m edge of plate (for a square with corner at mounting shaft axis)

% body mass (without wheel mass)
mb = motormas+platemas+extraplatemas+blokmas+motorplatemas+servomass



% rotating wheel interia
Iw = mw*(rw^2) %1.9161553e-8 %m^4 %

% body interia (without wheel)
Ib = (mb*(b^2))/6

%Tm = Km*u

% to be identyficated
Cb = 0.00102 %kg m2 s-1 
Cw = 0.0005 %kg m2 s-1
lb = 0.075 %m




% dx(t)/dt = Ax(t) + Bu(t)

% x:=(?b, d?b/dt,d?w/dt) % angular position of the body, angular speed of
% the body, angular speed ot the wheel

% (?b, d?b/dt,d?w/dt) (0,0,0)


A = [0  1  0;
     (((mb*lb)+(mw*l))*g)/(Ib+(mw*(l^2)))  (-(Cb)/(Ib+(mw*(l^2))))  Cw/(Ib+(mw*(l^2)));
     (-(((mb*lb)+(mw*l))*g)/(Ib+(mw*(l^2))))  Cb/(Ib+(mw*(l^2)))  (-(Cw*(Ib+Iw+(mw*(l^2))))/(Iw*(Ib+(mw*(l^2))))) ]
     

   
B = [0; 
    (-(Km)/(Ib+mw*(l^2)));
    (Km*(Ib+Iw+(mw*(l^2))))/(Iw*(Ib+(mw*(l^2)))) ]

C = [1  0  0]

D = 0







