# import module_1

# print( module_1.add( 5.5, 3, 10, 7) )
# print( module_1.divide( 240, 45) )

from module_1 import add, divide as div

print( add(1,2,3,4,5,6,7,8,9,10) )
# print( divide( 250, add(2,3,4,1) ) )
print( div( 250, add(2,3,4,1) ) )