import re

x = "IN KLU AT KLU"
y = re.findall("KL", x)
z = re.search("IN", x)
print(x)
print(y)
print(z)
print(re.sub("IN", "WHY", x))
print(re.split(" ", x))
