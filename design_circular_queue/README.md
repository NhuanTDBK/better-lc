# Solution

[Link](https://leetcode.com/problems/design-circular-queue/)

- The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle.

- The trick here is head and tail will move around the fixed-size array. So we simply add modulo operation in each enqueue, dequeue operation
