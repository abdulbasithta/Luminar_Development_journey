
movie ={
    "id":1,
    "title":"kanthara",
    "runtime":120,
    "genre":"action",
}

for v in movie.values():  # dictionary values

    print(v)

print(movie.get("language")) # None # if key not found

for k,v in movie.items(): # dictionary items(key and value)

    print(k,v)

# movie["runtime"] = 150 
# print(movie)

# movie.update(runtime=150)
# print(movie)

movie.update(runtime=160, director ="Rishab shetty")
print(movie)