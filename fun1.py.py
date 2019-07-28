#total = 0
#for number in range(1, 10 + 1):
  #  print(number)
 #   total = total + number
#print(total)


def add_numbers(x,y):
    answer=0
    for number in range(x,y+1):
        print(number)
        answer= number+answer
    return answer


print (add_numbers(333,777) )
