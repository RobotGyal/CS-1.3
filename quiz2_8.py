ls = []; 
  
def push_digits(num): 
  
    while (num != 0):  
        ls.append(num % 10)
        num = int(num / 10)

def reverse_num(num): 
    push_digits(num) 
    
    reverse = 0
    i = 1

    while (len(ls) > 0):  
        reverse = reverse + (ls[len(ls) - 1] * i)
        ls.pop()
        i = i * 10
    return reverse
    
print(reverse_num(3456))