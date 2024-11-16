## Feladat: Maximális párosítás egy fában

### Leírás:

Adott egy fának nevezett gráf, amely `n` csúcsból és `n-1` élből áll. Minden él két csúcsot köt össze. A feladat az, hogy megtaláljuk a fa maximális párosítását, vagyis az élek egy olyan halmazát, amelyben minden csúcs legfeljebb egy élhez tartozik. A cél, hogy meghatározzuk, hány él tartozik a maximális párosításhoz.

A párosításban lévő élek száma a maximális, ha nincs olyan csúcs, amely több mint egy élben szerepelne.

### Bemenet:

- Az első sor egy egész számot tartalmaz, `n`-t, amely a csúcsok számát jelzi.
- A következő `n-1` sor mindegyike két egész számot tartalmaz, `a` és `b`, amelyek azt jelentik, hogy van egy él a `a` és `b` csúcs között.

### Kimenet:

- Egy egész számot kell kiírni, amely a maximális párosításban szereplő élek számát jelzi.

### Korlátok:

- `1 ≤ n ≤ 2 * 10^5`
- `1 ≤ a, b ≤ n`

### Példa:

#### Bemenet 1:

5 1 2 1 3 3 4 3 5

#### Kimenet 1:

2

#### Bemenet 2:

3 1 2 2 3

#### Kimenet 2:

1

### Magyarázat:

- Az első példa egy fát reprezentál, amely a következő él struktúrával rendelkezik: 1-2, 1-3, 3-4, 3-5. A maximális párosítás két élt tartalmazhat: (1,2) és (3,4) vagy (3,5).
- A második példa egy egyszerű lánc, ahol a maximális párosítás egy élből áll: (1,2) vagy (2,3).

A megoldás feladata, hogy a fa maximális párosítását meghatározza a bemeneti él kapcsolatok alapján.
