"""
class dict:
    def key(self) return all keys
    def values(self) return all values
    def items(self)  return key and values
    def pop(self,key) remove the key value pair
    def get(self)

"""

course ={
    "name":"python Django",
    "duration":"6 months",
    "fee":13000,
    "tutor":"sajay"
}

all_keys = course.keys()

for k in all_keys:

    print(k)
    
all_values = course.values()

for v in all_values:

    print(v)
    
course.pop("fee")

print(course)

for k,v in course.items():

    print(k,v)
    
print(course.get("name"))   #invalid key returns

print("completed")