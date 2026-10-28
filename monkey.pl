
% Monkey Banana Problem

% Initial state:
% Monkey is at door, box is at window,
% bananas are at middle, monkey is on floor.

% Actions
move(monkey, X, Y) :-
    write('Monkey moves from '), write(X),
    write(' to '), write(Y), nl.

push_box(X, Y) :-
    write('Monkey pushes the box from '),
    write(X), write(' to '), write(Y), nl.

climb :-
    write('Monkey climbs onto the box.'), nl.

grasp :-
    write('Monkey grasps the bananas.'), nl.

% Solution
solve :-
    move(monkey, door, window),
    push_box(window, middle),
    climb,
    grasp,
    write('Monkey gets the bananas!'), nl.
