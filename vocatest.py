import collections
import time
from error_checking import *

print('voca_test.py')
print('made by seongjae KIM')
f = open('vocalibrary.txt', 'r')
text = f.readlines()

save_position = []
DBDtext = []
k=0

for i in range(len(text)):
      if text[i][0] == '#':
          save_position.append(i)
save_position.append(len(text))

print(save_position)

for i in range(len(save_position)-1):
    DBDtext.append([])

for i in range(len(save_position)):
    for j in range(save_position[i-1],save_position[i]):
        if i != 0:
            DBDtext[i-1].append(text[j])
        

print('please refer manual posted on GITHUB \n')
testdate = int(input('What is todays date\n'))
howmany = int(input('how many words?\n'))
cutline = int(input('minimum score to pass? please write percentage\n'))
testmode = int(input('Please choose mode for test. Review mode is 0. And new word training mode is 1 \n'))
automode = int(input('Would you use auto-grading or not? auto mode is 0. manual mode is 1.'))

error_testc(testdate,save_position,testmode,howmany,DBDtext,text,cutline)

f.close()
