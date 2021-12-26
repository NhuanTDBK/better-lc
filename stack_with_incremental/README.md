# Solution

[Link](https://leetcode.com/problems/design-a-stack-with-increment-operation/)

- This problem looks like trivial because you can create the array to do some operations on that. But the thing is, for every incremental procedure, you need to take O(k) operations to add val into element

- We can optimize that by introducing another array to record increment val `inc`. So at position `i` in array `inc`, it will represent first `i` number will be increase `inc[i]`