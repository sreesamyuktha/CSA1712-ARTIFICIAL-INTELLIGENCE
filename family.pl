
% Facts
male(ram).
male(raj).
male(kumar).

female(sita).
female(priya).
female(geetha).

% Parent relationships
parent(ram, raj).
parent(sita, raj).
parent(ram, priya).
parent(sita, priya).
parent(raj, kumar).
parent(geetha, kumar).

% Rules
father(X, Y) :-
    male(X),
    parent(X, Y).

mother(X, Y) :-
    female(X),
    parent(X, Y).

sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.
