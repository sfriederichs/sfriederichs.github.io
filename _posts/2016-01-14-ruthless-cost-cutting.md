---
layout: post
title:  "Adventures in Products - Ruthless Cost-Cutting"
updated: 2016-01-14 21:17
date:   2016-01-14 21:17
categories: products bom costs
---

I'd love to have a job developing electronic products. It's my dream! But I don't have any skills in product development, so I have to build them all on my own by creating my own products. This is my journey.

The most important part of developing a product is making money. If you're not making money there's no point in making a product. You make money with products by selling them for more it costs to make each one. There's two main strategies you can go with:

* Volume - Sell a lot with a low profit margin
* Quality - Sell a few with a high profit margin

I don't have the option of volume - I have to start small and work my way up. Thus, I have to have a high profit margin. One way of doing that is to lower the cost for each board. 

My first product idea is a test point breakout board. It clips on to the side of a breadboard and provides a test point for 8 rows on the breadboard. Test points make it easier to debug circuits, so I figured that someone might find this useful and pay me money. 

Sadly, this board is pretty 'dumb'. It's all passive components so it's nice and simple, but the main value I add to the product is in the PCB design. The parts that go on the PCB just cost me money, so the more I minimize that cost, the more money I make. 

There's several tactics for reducing part count:

* Reduce the number of parts - Fewer parts means less cost. Get rid of everything you don't need.
* Use cheaper parts - 0603 sized SMD parts are usually cheaper than their 1206 bretheren and are just about as useful. There are other changes like this you can make to save money.
* Reduce part count - If you have 8 red LEDs and one green, see if you can make the green one read instead. In this way, you'll get more bulk discounts when buying parts and you may save costs on board assembly.
* Buy parts in bulk - 10K 1/4W 5% 1206 resistors cost $0.00602 in quantities of 500 or more and $0.00443 in quantities of 1000 or more. So 500 costs $3.01 and 1000 costs $4.43. You're not doing yourself any favors by buying 500.
* Buy from cheaper places - Take chances with skeezy Chinese places for simple components. For example, how can you mess up a resistor? Wrong tolerance? Wrong value? Wrong power dissipation? You can stand being off in any of those areas in a lot of non-critical applications.

