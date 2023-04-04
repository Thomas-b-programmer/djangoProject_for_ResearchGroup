time = '2023-03-22T14:30'
time1 = time.split('-')
time2 = time1[2].split('T')
time3 = time2[1].split(':')
nian = time1[0]
yue = time1[1]
ri = time2[0]
shi = time3[0]
fen = time3[1]

print(nian,yue,ri,shi,fen)