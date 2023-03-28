def a():
  print("a before")
  x = 10/0
  print("a after")

def b():
  print("b before")
  a()
  print("b after")

def c():
  print("c before")
  b()
  print("c after")

def d():
  print("d before")
  c()
  print("d after")

d()