#still need to get this part  The number 32 has binary representation 100000 and has no binary gaps.
def solution(a):
    br = str(bin(a))[2:]
    counter = 0
    maxcounter = 0
    for char in br:
        if char == '1':
          counter = 0
          continue
        elif char == '0':
         counter = counter+1
         if counter>maxcounter:
          maxcounter=counter
    return max(counter,maxcounter)
pass



