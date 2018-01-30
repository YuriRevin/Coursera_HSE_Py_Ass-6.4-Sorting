fi = open('input.txt', 'r', encoding='utf8')
fo = open('output.txt', 'w', encoding='utf8')
li = fi.readlines()
li.sort()
for line in li:
    tl = list(map(str, line.split()))
    wo = tl[0], tl[1], tl[3]
    fo.write(str(' '.join(wo)) + '\n')
fi.close()
fo.close()
