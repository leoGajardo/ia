parent(pam,bob).
parent(tom,bob).
parent(tom,liz).
parent(bob,ann).
parent(bob,pat).
parent(pat,jim).

offspring(Y,X) :- parent(X,Y).
grandparent(X,Z) :- parent(X,Y), parent(Y,Z).