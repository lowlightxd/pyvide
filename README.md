# pyvide
Have you ever wanted a funnier divide in your python code?
I whole-heartedly present to you folks - a division function that doesn't use any division in its implementation.
At first glance, dividing something in python is simple, because you can just write
```python
  result = 10 / 3
```
But why would you do that, when you can use a whole function for that, that doesn't actually use any division!
Have fun!

Also, this is about 100 times slower than the regular division operator division:
```
10000 divisions with my stupid function took  0.11397647857666016
10000 normal divisions took  0.001978635787963867
```
