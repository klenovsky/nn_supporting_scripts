answer = False
candidate = 10
while (not answer) and (candidate<1000):
    if candidate % 3 ==1 and \
      candidate % 4 ==1 and\
      candidate % 6 ==1 and\
      candidate % 7 ==1:
        answer = True
    else:
        candidate+=5
print candidate
