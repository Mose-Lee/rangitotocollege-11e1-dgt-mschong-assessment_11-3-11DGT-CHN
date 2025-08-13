print("Hello world!")
lists = []
while True:
  name = input('Enter name: ')
  if name == 'stop':
    break
  lists.append(name)

for i in lists:
  print(i)
