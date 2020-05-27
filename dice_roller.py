from random import randint

ordinals=[ 'first' , 'second' , 'third' , 'forth' , 'fifth' , 'sixth' ,]
def main():
  dice_rolls= int(input('how many rolls (max 6)?: '))
  while dice_rolls<1 or dice_rolls>6 :
    dice_rolls= int(input('Not valid. Retry: '))
  dice_sum=0
  for i in range(dice_rolls):
    roll = randint(1,6)
    print(f'As {ordinals[i]}, you rolled a {roll}')
    dice_sum+=roll
  print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()
