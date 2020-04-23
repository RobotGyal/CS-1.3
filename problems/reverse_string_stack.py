string = 'this is a string containing words'

def reverse_string(word):
    stack = []
    word = word.split(' ')
    for i in range(len(word)):
        stack.append(word[i])
    return stack[::-1]

print(reverse_string(string))





def reverse_with_stack(word):
    my_stack = []
    for i in word:
        my_stack.append(i)
        reversed_string = ''
    while len(my_stack) != 0:
        reversed_string += my_stack.pop(-1)
    return reversed_string

print(reverse_with_stack(string))