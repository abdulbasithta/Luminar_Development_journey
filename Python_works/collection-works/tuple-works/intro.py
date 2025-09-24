# tuple used for organizing and storing multiple values using single variable

# define (),tuple()
# duplicates allowed
# ordered
# immutable


# tp=(10,20,10,20)
# # tp[0] =100 # 'tuple' object does not support item assignment
# print(type(tp))

"""

class tuple:

    def count(self,object) return number occurence of object
    def index(self,object) return first index position of object

"""

tp=(10,20,10,20)
#    0  1  2  3

freq=tp.count(10)

print(freq)

pos=tp.index(20)

print(pos)