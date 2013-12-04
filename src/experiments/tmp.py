if x== 1:
	f("a")
elif x == 2:
	f("b")


switch = { \
	1 : ("a",13),
           2 : "b"
}
f(switch[x][0])
g(switch[x][1])
