There is a classical problem: you are given 12 coins, and among them there exists a counterfeit one which shares the same appearance but is either heavier or lighter than the others. I have made some basic discussion in [https://chi-shan0707.github.io/musings/balancescale-and-ball/](https://chi-shan0707.github.io/musings/balancescale-and-ball/).<br>

In that post, some questions arose in my mind. And I want to record some not-so-correct exploration before a rigorous mathematical paper distillation.<br>

We are faced with $c$ coins in $w$ weighings on $b$ balances by a sequential strategy `round` means a balance try, namely a weighing.

We ask:<br>
(P1) What is the minimal number of weighings to decide $c$ coins?<br>
(P2) What is the minimal number of weighings to decide $c$ coins when we are allowed to use $b \ge 1$ balances? This means that we may distribute the set of our coins on $b$ balances to get $b$ pieces of information in one weighing. Note that this procedure differs from doing $b$ weighings on one balance one after another. <br>


> And **decide** means: we find that coin and know it is heavier or lighter!


We observe a four-fold relationship from 3 coins with 2 weighings to 12 coins with 3 weighings. It is incredible. By nature, we can just imagine a double, but here we miraculously "double" the double.


How to account for it? I think the easiest part is the "balanced" scenario of round 1. Then we actually know nothing about the rest, which is good for recurrence. Moreover, inspired by the fact that if we know whether the counterfeit is heavier or lighter, the optimum will be related to powers of 3 (base-3 logarithm), we can **assume** that we have enough standard coins. Make a comparison between standard coins and the biggest power of 3 in coins. If there is imbalance, then we can know its inclination and find it 3-fold. On the other hand, if it is still balanced, we can recurse to the next case:<br>

$$
RS(w) =  RS(w-1) + 3^{w-1}, RS(2)=3
$$

> RS means Rest with *Standard coins*

Going back to the scenario of imbalance in round 1: I am in awe of the construction of 12 coins (I thought of it myself!). So I want to draw on the idea of reduction. What if I pack a certain number of coins together and view them as a whole? I can apply the same strategy on the packs, and finally with the knowledge of being heavier or lighter figures out which one in the pack is the real outlier.<br>

Considering that the 12 coins with 3 weighings are so 巧妙, then I make a bold guess: this method is (almost) the limit. Hence I assert maybe it is a 3^pow acceleration:  4+4+ RS(2), next is 12+12+ RS(3),   (12 is 4 \times 3, once I know the inclination, then I will only use 1 extra try in the pack to get the outlier);

8 \times 3^{w-3} +  RS(w-1) = ....


We actually miss one thing! I previously assume that we have quite enough standard coins to deal with the rest coins in the case of balance in round1. Do we really have enough? Check it and we will find.....
