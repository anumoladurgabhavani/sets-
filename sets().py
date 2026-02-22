Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#seta()
a={3,5.6,"pooja",5+9j,True,False}
print(a)
{False, True, 'pooja', 3, (5+9j), 5.6}
type(a)
<class 'set'>
b={7,9,5,6,7,9,3}
print(b)
{3, 5, 6, 7, 9}
type(b)
<class 'set'>
#add
a={4,5,6,7,8,9}
a.add(20)
a
{4, 5, 6, 7, 8, 9, 20}
#issubset
a={2,3,4,5,6,7}
b={5,6,7}
b.issubset(a)
True
a.issubset(b)
False
a={4,5,6,7,8,9}
b={8,9,11}
b.issubset(a)
False
a.issubbset(b)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.issubbset(b)
AttributeError: 'set' object has no attribute 'issubbset'. Did you mean: 'issubset'?
a.issubest(b)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.issubest(b)
AttributeError: 'set' object has no attribute 'issubest'. Did you mean: 'issubset'?
a.issubset(b)
False
#issuperset()
a={3,4,5,6,7,8,9}
b={2,3,4,5,6}
a.issuperset(b)
False
a={1,2,3,4,5,6}
b{4,5,6}
SyntaxError: invalid syntax
b={4,5,6}
a.issuperset(b)
True
b.issuperset(a)
False
#union()
a={3,4,5,6,7,8,9}
b={2,3,4,5,9}
a.union(b)
{2, 3, 4, 5, 6, 7, 8, 9}
#intersection
a={4,5,6,7,8,9}
b={6,7,8,9,10,11}
a.intersection(b)
{8, 9, 6, 7}
#difference
a={2,3,4,5,6}
b={3,4,5,6,7,8}
a.difference(b)
{2}
b.difference(a)
{8, 7}
#update
a={10,11,12,13,14}
b={11,12,13,14,15}
a.update(b)
a
{10, 11, 12, 13, 14, 15}
a
{10, 11, 12, 13, 14, 15}
b.update(a)
b
{10, 11, 12, 13, 14, 15}
b
{10, 11, 12, 13, 14, 15}
#difference_update
a={4,5,6,7,8,9}
b={2,3,4,5,6,7,8,9,10}
a.difference_update(b)
a
set()
a={2,3,4,5,6,7}
b={1,5,7,9,11,12}
b.difference
<built-in method difference of set object at 0x000001D2B5F61EE0>
b.difference_update(a)
b
{1, 9, 11, 12}
b
{1, 9, 11, 12}
a.difference_update(b)
a
{2, 3, 4, 5, 6, 7}
#symmetric_update
a={3,4,5,6,7,8,9}
b={1,2,3,8,9,10,11}
a.symmetric_difference(b)
{1, 2, 4, 5, 6, 7, 10, 11}
b.symmetric_difference(a)
{1, 2, 4, 5, 6, 7, 10, 11}
a
{3, 4, 5, 6, 7, 8, 9}
#symmetric_difference_update
a={1,3,5,7,9,11,13}
b={2,3,4,6,8,10,12}
a.symmetric_difference_update(b)
a
{1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
a
{1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
b
{2, 3, 4, 6, 8, 10, 12}
b.symmetric_difference_update(a)
b
{1, 3, 5, 7, 9, 11, 13}
#intersection_update
a={7,8,9,10,11,12,13}
b={2,3,4,5,6,7,8,9}
a.intersection_update(b)
a
{8, 9, 7}
b.intersection_update(a)
b
{8, 9, 7}
#pop()
a={5,6,7,8,9,10}
a.pop()
5
a.pop(6)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    a.pop(6)
TypeError: set.pop() takes no arguments (1 given)
>>> a.remove(10)
>>> a
{6, 7, 8, 9}
>>> a={3,4,5,6,7}
>>> a.copy()
{3, 4, 5, 6, 7}
>>> a.clear()
>>> a
set()
>>> b=set()
>>> b.add(60)
>>> b
{60}
>>> b.discard(60)
>>> b
set()
>>> #isdisjoint
>>> a={3,4,5,6,7,8}
>>> b={2,4,5,6,7}
>>> a.isdisjoint(b)
False
>>> a={7,8,9}
>>> b={2,3,4}
>>> a.isdisjoint(b)
True
>>> a={5,6,7,8}
>>> len(a)
4
>>> a.count(2)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    a.count(2)
AttributeError: 'set' object has no attribute 'count'
>>> a.index(7)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    a.index(7)
AttributeError: 'set' object has no attribute 'index'
