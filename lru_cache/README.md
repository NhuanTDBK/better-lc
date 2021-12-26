# Solution

[Link](https://leetcode.com/problems/lru-cache/)

- It's another tough problem with careful design. I dont know the mechanism LRU worked so I need to read other pages to understand

- Basically, the cache obviously has dict variable. The trick here is about recently used. All values in the cache will list in doubly-linked list to represent recently used. When an element was used or new element is pushed, it will push to head of list. Evictation is taked tail of list to drop out