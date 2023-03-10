# Car-Service---Python
Car service with some useful functionalities.

Service auto
1. CRUD mașină: id, modelul, anul achiziției, numarul de kilometrii, disponibilitate garantie. 
2. CRUD card client: id, numele, prenumele, CNP, data nașterii (dd.mm.yyyy), data înregistrării (dd.mm.yyyy). 
3. CRUD tranzacție: id, id-ul mașinii, id-ul cardului client, sumă piese, sumă manoperă, data și ora. Dacă există un card client, atunci se aplica o reducere de 10% pentru manoperă. Dacă mașina este în garanție, atunci piesele sunt gratis. Se tipărește prețul plătit și reducerile acordate.
4. Căutare mașini și clienți. Căutare full text.
5. Afișarea tuturor tranzacțiilor cu suma cuprinsă într-un interval dat.
6. Afișarea mașinilor ordonate descrescător după suma obținută pe manoperă.
7. Afișarea cardurilor client ordonate descrescător după valoarea reducerilor obținute.
8. Ștergerea tuturor tranzacțiilor dintr-un anumit interval de zile.
9. Actualizarea garanției la fiecare mașină: o mașină este în garanție dacă și numai dacă are maxim 3 ani de la achiziție și maxim 60 000 de km.
10. More to come =)
