# Multiples of 3 or 5 - 6kyu

## 題目

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

> Note: If the number is a multiple of both 3 and 5, only count it once. Also, if a number is negative, return 0(for languages that do have them)

Input : a number
Output : Sum of multipes of 3 or 5

傳入一個數字，取出 3 or 5 倍數，將倍數的值加總的值回傳。

## Test cases

* input < 0
* input = 4, for multipes of 3
* input = 6, for multipes of 5
* input = 10, for multipes of 3 or 5
* input = 30, large number for multipes of 3 or 5
