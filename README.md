# ADS

## Zadanie č.3 (2-SAT solver)

Napíšte program, ktorý načíta vstupný súbor s logickou formulou v konjunktívnej normálnej forme (KNF, angl,. CNF) v (zjednodušenom) DIMACS formáte (v jednotlivých klauzulách sú povolené najviac 2 literály - môžete predpokladať korektný vstup). Program s polynomiálnou zložitosťou zistí, či je vstupná formula splniteľná alebo nie je splniteľná (a vypíše na obrazovku SPLNITEĽNÁ/NESPLNITEĽNÁ). V prípade, že je vstupná formula splniteľná, program vypíše pre jednotlivé použité booleovské premenné pravdivostné hodnoty (PRAVDA/NEPRAVDA), po ktorých dosadení za príslušné booleovské premenné bude formula mať hodnotu PRAVDA. Váš program musí využívať algoritmus zo stránky: 

[https://cp-algorithms.com/graph/2SAT.html ](https://cp-algorithms.com/graph/2SAT.html) 

Vstupný súbor v zjednodušenom DIMACS formáte vyzerá takto: 

Na prvom riadku sú dve celé kladné čísla (nbvar nbclauses) oddelené medzerou, kde nbvar určuje počet použitých booleovských premenných a nbclauses určuje počet klauzúl vo formule. Na ďalších (nbclauses) riadkoch sú zapísané jednotlivé klauzuly. Literály v nich sa zapisujú číslom booleovskej premennej (od 1 po  nbvar),  negovaná  booleovská  premenná  má  pred  svojím  poradovým  číslom  znak  -.  Klauzula  je ukončená znakom 0. 

Príklad vstupného súboru:

2 3

1 2 0 

-1 -2 0 

1 0 
