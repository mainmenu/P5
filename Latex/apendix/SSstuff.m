ssmodel = ss(A,B,C,D)

sys_order = order(ssmodel)
determinant = det(ctrb(A,B))

Q = [0.005 0 0
     0 0.001 0
     0 0 0.001]%
R = 1;
Kc = lqr(A,B,Q,R)

Ac = [(A-B*Kc)]
Bc = [B]
Cc = [C]
Dc = [D]

sscontroled = ss(Ac,Bc,Cc,Dc)

controlled_poles=pole(sscontroled)

