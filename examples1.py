# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/em/heyanyi/.spyder2/.temp.py
"""

print "Hello Yanyi!"
a=2
print a
print 2/4
import math
math.sqrt(2.0)
#help(math)
print "the number is %s" % a
quote = "this's is life"
print quote[1]
print quote[:-3]
sum=0
for n in range (1,101):
    sum=sum+n
print sum
print n
print range(1,3)
"""
primestr=[2];

for n in range(2,1001):
    indicator = 0;
    sizeofprime = len(primestr)
    i=0;
    while i < sizeofprime:
        if n%primestr[i] == 0:
            break;
        else:
            if (i==sizeofprime-1 ):
                print "the primer is %d" % n  
                primestr.append(n)
                i=i+1
            else: i=i+1
"""
f=open("numbers1.txt","w")
f.write("hello\n")
f.write("goodbye")
f.write("bad luch")
f.close()
f=open("numbers1.txt")
lines=f.readlines();
#lines=lines.strip()
print lines
f.close()

a='347'
b=int(a)

f=open("numbers2.txt")
lines = f.readlines()
f.close()
print lines
lines[0].split()

#find in list
f=open("dist.female.first")
names=[]
for line in f:
    fields=line.split()
    names.append(fields[0])
    
if "AMY" in names:
    print "ture"
    
#dictionaries
    parameters={}
    parameters['tolerence'] = 1.e-6
    parameters['niterations'] = 500
    for key in parameters:
        print key, parameters[key]
    del parameters['tolerence']

#list to tuple casting tuple()

myclasses=set()
myclasses.add("math")
myclasses.add("chemistry")

yourclasses=set()
yourclasses.add("math")
yourclasses.add("physics")

myclasses & yourclasses
myclasses | yourclasses

"""
students
{121: {'grade': 10, 'classes': ['gym', 'latin', 'chemistry'], 'name': 'Sarah'},!
19: {'grade': 7, 'classes': ['science', 'spanish', 'literature'], 'name': 'Tim'}}!
students[19]['grade']
"""


