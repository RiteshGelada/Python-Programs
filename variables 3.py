x = "AMAZING"

def myfunc():
  x = "FANTASTIC"
  print("Python is " + x)

myfunc()
print("Python is " + x)

def myfunc():
  global x
  x = "Easy"

myfunc()
print("Python is " + x)
