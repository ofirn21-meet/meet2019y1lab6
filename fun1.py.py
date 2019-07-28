#total = 0
#for number in range(1, 10 + 1):
  #  print(number)
 #   total = total + number
#print(total)

answer=0
def add_numbers(x,y):
    for number in range(x,y+1):
        print(number)
        answer= add_numbers+answer
    return answer


add_numbers(333,777) 
