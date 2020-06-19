# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n

      O(n) linear runtime, because the input is fixed at n*n*n, and performs one operation for each given 'a'. 'a' will cap at 'n*n*n', either way, it's one operation per 'a'.
```


```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1

    O(n^2) Quadratic runtime. because it has a nested loop. so its scaling ^2 for each n.
```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

      O(n) Linear runtime, because it's performing one operation per 'n'. it's scaling linearly with 'n'
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

def safest_egg_Drop(n):
    <!-- notes: -->
    n is our num of floors.
    a=1
    b=2
    c=3
    d=4
    e=5
    f=6
    assuming f value % based off the alphabet it's 23.1% of 26
    23.076923076923077 % of 26
    f= n * .023

   find the safest floor number.
   <!--  code:  -->
    floors = n
    f= (floors * 23% rouned up) 'is the highest safe floor'
    return f

    runtime= O(1) 'constant'


