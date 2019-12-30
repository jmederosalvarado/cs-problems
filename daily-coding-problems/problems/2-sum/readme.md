> This problem was recently asked by __*Google*__.
> 
> Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
> 
> For example, given `[10, 15, 3, 7]` and `k` of `17`, return true since `10 + 7` is `17`.
> 
> _Bonus: Can you do this in one pass?_

This is a basic __two pointer__ problem.

The idea is to sort the array and keep in every moment and interval where we know the two numbers are.

We start with the whole list as the interval, and in every iteration we compare the sum of the boundaries of the interval with k, and consider the following cases:

- If the sum is equal to k, then we have found the numbers we were searching for.

- If it is greater than k, then as the list is sorted we move the right boundary of the interval one position to the left.

  It doesn't make sense to move the left boundary as it will only increase the sum.

- The case when the sum is less than k is analogous to the previous one.

Note that we have always kept the two numbers (if they exist) inside the interval, so if the interval becomes empty we can guarantee there is no solution.

This aproach has O(n) complexity.

__*[Code](./solution.py)*__