#bu ornekte grouping konusuna deginilmistir. 
import re

p=re.compile('(a(b)c)d')
m=p.match('abcde')
print("Group(0)",m.group(0))
print("Group(1)",m.group(1))
print("Group(2)",m.group(2))

print("Group(0,2,1)",m.group(0,2,1))
print("Group(2,1,2)",m.group(2,1,2))

print("Groups",m.groups())

#bazen eslesen pattern'in icerigi onemsiz olabilir.
m=re.match("([abc])+","abc")
print(m.groups())
m=re.match("(?:[abc])+","abcd")
print(m.groups())
