#MadLib.py
#Name: Michael J. Walton
#Date: 08/28/2024
#Assignment: Lab 1 MadLib

def main():
  print("Madlib")
  #Ask user for words
  word1 = input('Enter the first adjective  ')
  word2 = input('Enter the second adjective ')
  word3 = input('Enter the third adjective  ')
  word4 = input('Enter the fourth adjective ')
  word5 = input('Enter the fifth adjective  ')
  word6 = input('Enter the sixth adjective  ')
  word7 = input('Now enter a noun           ')

  #Print the story with the user supplied words.
  print('How to Make a Terrible Sandwich!')
  print('First get 2 slices of', word1, 'bread')
  print('Put on some', word2, 'pickles')
  print('Add some', word3, 'onions')
  print('and some', word4, 'sauce')
  print('Then slap on some', word5, 'cheese')
  print('and some random', word6, 'meat')
  print('Smash it with a', word7, 'and enjoy!')


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
