# ADS

## Veľké zadanie č. 2 (18 bodov)

**Termín odovzdania: do 20.4.2022 do 23:59 hod.** 

Napíšte program (korektor), ktorý načíta slovník (**slovnik.txt**, textový súbor, na každom riadku jedno slovo)  a  textový  súbor  **chvstup.txt.**  V  súbore  **chvstup.txt**  je  zapísaný  vstupný  text,  ktorý  sa  však „poškodil“.   Tento  vstupný  text  je  písaný  v  rovnakom  jazyku,  v akom  je  slovník.  Váš  program  vo vstupnom  súbore  opraví  „preklepy”  a  opravený  súbor  zapíše  do  výstupného  textového  súboru **vystup.txt**.  „Preklepy”  -chyby  môžu  byť:  zmena  znaku,  zmazanie  znaku,  vloženie  znaku. Pridanie/zmazanie/zmena znaku môže byť spravené kdekoľvek v texte (náhodne),  pričom však nedôjde k zmazaniu slova. V jednom slove môže byť 0, 1 alebo aj viacej chýb.  

**Implementujte  (aspoň)  2  verzie  korektora,  založené  na  rôznych  princípoch.**  (Podľa  možnosti nerekurzívne.) 

Napíšte ešte ďalší program, ktorý načíta textové súbory **vystup.txt** a **pvstup.txt** (pôvodný text bez chýb) po slovách, pričom vždy porovná i-te slovo z **vystup.txt** s i-tym slovom z **pvstup.txt** (pričom obe slová najskôr  skonvertuje  na  malé  písmená)**.**  Program  vypíše  informáciu  o  úspešnosti  opráv,  t.j.  počet správnych slov vo **vystup.txt** a taktiež aj počet všetkých slov v **pvstup.txt**. 

Slovník môžete použiť vlastný (nejaký základný vám dáme k dispozícii). 

**Pomôcky:** *najdlhší spoločný podreťazec, najdlhšia spoločná podpostupnosť, editačná vzdialenosť*. [https://edutechlearners.com/download/Introduction_to_algorithms-3rd%20Edition.pdf ](https://edutechlearners.com/download/Introduction_to_algorithms-3rd%20Edition.pdf)
