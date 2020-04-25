'''
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------



'''
n=int(input())
t=n*2-1
for i in range(n):
 for j in range(n):
  if t==i and j==i:
   print(chr(e))
  else:
   print("-")
 print("\r")
