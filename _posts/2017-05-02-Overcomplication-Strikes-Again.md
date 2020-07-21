---
layout: post
title:  "Overcomplication Strikes Again"

date:   2017-05-02 21:59
categories: professional
---

I no longer feel like a complete idiot. A partial idiot - maybe. But I have conquered something worthwhile: myself.

I was overcomplicating a coding challenge again. The challenge was to generate the sum of a series of fractions laid out in a sequence on a variable-sized square chess board. The sequence of fractions had a predictable pattern so I figured I would use a FOR loop to sum up all the fractions. Easy!

Except... they wanted the output displayed not as a floating point number, but as a fraction. For example, if the result of the sum was .5, the output would look like this:

> [1, 2]

And if the sum was an integer, display it like this:

> [2]

This threw a wrinkle into the mix. Because not all fractions are exactly representable as a floating point number I couldn't compute the sum and then change it back into a fraction because the sum might have been rounded at some point in calculation. I tried calculating the numerator and denominator separately and then reducing the fraction after each operation, but the numbers just got too big to represent - even for long long integers. I couldn't figure out how to preserve all of my precision in the calculation and still be able to perform it.

I took some time off and when I came back I decided that I had been doing too much work. The sequence of fractions was predictable, so shouldn't the sum be predictable? I drew out a couple of chessboards of varying size with the pattern on them and started to notice the patterns. Soon enough it was obvious what the sum would be for any square chess board with n squares on a side: n squared over 2. That was it. No loops, no calculations, no integer representation problems, no floating point precision issues. 

It was a lot simpler than expected because I was trying to solve the problem with code rather than with math. Brute force is an inefficient solution that might work - but it might not too. It's a much better bet to use your brain to make sure you're solving the right problem before you expend all of that effort.
