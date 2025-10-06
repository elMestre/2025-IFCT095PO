# Tablas de la Verdad

Booleano
True - False

[Algebra boole](https://www.electronics-tutorials.ws/boolean/boolean-algebra-simplification.html)

```
    A  B  AND                      A  B  XOR eXclive OR
    0  0  0                        0  0  0
    0  1  0                        0  1  1
    1  0  0                        1  0  1
    1  1  1                        1  1  0

    A  B  OR                       A  NOT
    0  0  0                        0  1
    0  1  1                        1  0
    1  0  1
    1  1  1

     0110101                        0110101
 AND 1001110                     << 1101010
     0000100
```

```
True and False          => False
False and False         => False
True or False           => True
False and True          => False

not True and not False  => False
False and not False     => False
not True or False       => False
not False and not True  => False
```

```python
                      #   [ 1 | 3 | 4.5 | 7 | 10 | 12 ]
x < 5 and x < 10      #   [        True | False       ]
x < 5 or x < 4        #   [        True | False       ]
not(x < 5 and x < 10) #   [       False | True        ]

3 and 1               # True
2 and 0               # False

```
