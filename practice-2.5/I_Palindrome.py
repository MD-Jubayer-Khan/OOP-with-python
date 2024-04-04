def is_palindrome(num):

    return str(num) == str(num)[::-1]

def print_reversed_and_palindrome(N):

    reversed_num = str(N)[::-1].lstrip('0')
    
    print(reversed_num)
    
    if is_palindrome(N):
        print("YES")
    else:
        print("NO")

N = int(input().strip())

print_reversed_and_palindrome(N)
