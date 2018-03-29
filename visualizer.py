import sys

try:
    c, r = sys.argv[1], sys.argv[2]
except:
    c, r = 50, 50
m = [['.' for x in range(c)] for y in range(r)]

for i in range(0, 50):
    for j in range(0, 50):
        m[i][j] = '0'

for row in m:
    print ' '.join(row)
