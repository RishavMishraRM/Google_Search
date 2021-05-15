# import the necessary module!
import pywhatkit as kt

# display welcome msg
print('Lets perform Google search!')

# single search item
target1 = 'india'
# or we can use 
# multiple search items
target2 = 'friends'
target3 = 'coronavirus'
target4 = 'python'

# call the method
kt.search(target1)
kt.search(target2)
kt.search(target3)
kt.search(target4)



# or using single search as in 2 lines
#import pywhatkit as kt
#kt.search('python')