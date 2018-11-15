from random import randint
#generate random number
x = randint(1,10)
#print (x)
#y = int(input("Guess any number between 1 and 10 >>"))
y = 5

def number_guess(x,y):
  '''capture number guessed
  '''
  
  if y == x:
    text1='You are a genious just like the owner of this code!'
    return text1
  elif y>x:
    n = y - x
    text2='Sorry,your guess is %d step(s) higher from the correct number!'%n
    return text2
  else:
    n = x-y
    text3='Sorry,your guess is %d step(s) behind the correct number!'%n
    return text3

#print(number_guess(x,y))
