import pickle
# my_list = ['Fred', 73, 'Hello there', 81.9876e-13]
pickle_file = open('my_pickled_list.pkl', 'rb')
# pickle.dump(my_list, pickle_file)
recovered_list = pickle.load(pickle_file)
pickle_file.close()
print(recovered_list)

# my_file = open("new_file.txt", 'w')
# print("Hello there, neighbor!", file=my_file)
# my_file.close()

# the_file = open('notes.txt', 'w')
# the_file.write('Wake up\n')
# the_file.write('Watch cartoons\n')
# the_file.close()

# new_file = open("my_new_notes.txt", 'w')
# new_file.write("Eat supper\n")
# new_file.write("Play soccer\n")
# new_file.write("Go to bed\n")
# new_file.close()

# todo_list = open('notes.txt', 'a')
# todo_list.write('Spend allowance\n')
# todo_list.close()

# my_file = open('notes.txt', 'r')
# lines = my_file.readlines()
# print(lines)
# first_line = my_file.readline()
# second_line = my_file.readline()
# print(f"first line = {first_line}")
# print(f"second line = {second_line}")
# my_file.close()
