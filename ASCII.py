name=raw_input("Gib einen Kartennamen ein: ")
if len(name)>16:
  name=name[:16]
data = [ord(x) for x in list(name)]
print data