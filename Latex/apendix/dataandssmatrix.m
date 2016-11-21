
clc
clear

motormas = 0.110 % kg
platemas = 0.115 % kg
servomass =  0,0217 % kg

Tm = 0.0834 % BLDC max continous torque
Km = 0.00335 % torque constant of the BLDC
g = 9.81 % m/s^2

l = 0.085 % m lenght to the center of the plate
rw = 0.06 % m reaction wheel radius
mw = 0.018 % m reaction wheel mass
b = 0.075 %m lenght to the mass centre of the body

mb = motormas+platemas+servomass % body mass

Iw = mw*(rw^2) %reaction wheel inertia


Ib = (mb*(2*l)^2)/3 %whole body inertia

%Tm = Km*u

maxthetaddot=Tm/Iw

%parameters what cannot be measured directly
Cb = 0.00102 %kg*m2 *s-1 
Cw = 0.0005 %kg*m2 *s-1
lb = 0.075 %m
%since we were unable to aquire the hardware and the setup is similar to
%the ETH on we are going to use theyr values



% dx(t)/dt = Ax(t) + Bu(t)

% x:=(?b, d?b/dt,d?w/dt) % angular position of the body, angular speed of
% the body, angular speed ot the wheel


A = [0  1  0;
     ((((mb*lb)+(mw*l))*g)/(Ib+(mw*l^2)))  (-Cb/(Ib+(mw*l^2)))  (Cw/(Ib+mw*l^2));
     (-((mb*lb+mw*l)*g)/(Ib+(mw*l^2)))  Cb/(Ib+(mw*l^2))  (-(Cw*(Ib+Iw+(mw*l^2)))/(Iw*(Ib+mw*(l^2)))) ]
        
B = [0; 
    (-(Km)/(Ib+(mw*l^2)));
    ((Km*(Ib+Iw+mw*l^2))/(Iw*(Ib+mw*l^2))) ]

C = [1  0  0]

D = 0

