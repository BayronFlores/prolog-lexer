% Hechos
padre(juan, ana).
padre(juan, pedro).
edad(juan, 52).
nombre_completo(juan, 'Juan Pérez').
mensaje("familia de ejemplo").

% Regla
abuelo(X, Z) :-
    padre(X, Y),
    padre(Y, Z).

es_mayor(X) :-
    edad(X, E),
    E >= 18,
    \+ E =< 0.

?- abuelo(juan, Quien).
