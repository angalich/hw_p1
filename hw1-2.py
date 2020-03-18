seconds = int(input("Enter time in seconds"))
h = (seconds//3600)%24
m = (seconds//60)%60
s = seconds%60
print( '{0}:{1:=02}:{2:=02}'.format(h, m, s) )

#?