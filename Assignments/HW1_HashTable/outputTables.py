fin = open("RightTroll.txt")
s = "<table><tr>"
for i, l in enumerate(fin.readlines()):
    if i%50 == 0:
        if i > 0:
            s = s + "</td>"
        s = s + "<td>"
    s += l.rstrip() + "<BR>"
s += "</tr></table>"
print(s)