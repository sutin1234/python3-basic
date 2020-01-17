# strip | trim
s = "Thailand"
t = "   Thailand    "
text = " Thai land"
u = t.strip()
y = text.strip()
print("s={} t={} u={}".format(s, t, u))
print("compare s and t: {} {}".format(s, t))
print(s == t)

print("compare s and u: {} {}".format(s, u))
print(s == u)

print("trim={}".format(text))
