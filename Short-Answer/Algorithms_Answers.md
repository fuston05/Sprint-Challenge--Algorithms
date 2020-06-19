#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
 O(n) linear runtime, because the input is fixed at n*n*n, and performs one operation for each given 'a'. 'a' will cap at 'n*n*n', either way, it's one operation per 'a'.

b)
O(n^2) Quadratic runtime. because it has a nested loop. so its scaling ^2 for each n.

c)
O(n) Linear runtime, because it's performing one operation per 'n'. it's scaling linearly with 'n'

## Exercise II
still dont understand the problem :: 
     but here's my initial impression

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

