# Solution

[Link](https://leetcode.com/problems/design-skiplist/)

[Original Paper](https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf)

## Description

- Skiplist is probalistic data structure based on linked list that takes O(logn) to add, erase and search. Basicallly, there are many layers in the skiplist. Each layer is sorted linked list. The bottom layer is ordinary sorted linked list. Each higher layer acts as "express lane"

- Height of skiplist is lg(n)  with high probability  $1 - \frac{1}{n^c}$

- Skiplist has three parts: head and sentinal and list of nodes. Every node contains a column which represents levels, connected to next column