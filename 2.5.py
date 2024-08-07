#read an array 

friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
print(friends)
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)
friends.reverse()
print(friends)

friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
cars.reverse()
print(cars)

friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]

#add more str to the array append or insert position, name wthever

friends.append('Camilo')
friends.append('lorena')
friends.insert(3,'Eva')
friends[4] = 'Anna'
print(friends)
print(sum(cars))


# add another list within a list extend

print('joooooolin')

friends.extend(cars)
print(friends)

# to delete any index in the array REMOVE or POP

friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
friends.remove('Terry')
friends.pop()
friends.pop(-1)
print(friends)

# COPY 3 ways

new_friends = friends[:]
new_friends = friends.copy()
new_friends = list(friends)

# delete

friends.clear() # === output []
del friends 
# del friends[4] 
