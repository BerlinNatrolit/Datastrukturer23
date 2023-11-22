def lowest_number():
    index = 1
    while True:
        
        is_divisible = True
        for i in range(1, 21):
            if not index % i == 0:
                is_divisible = False
                break
        if is_divisible:
            return index
        index += 1
 
if __name__ == '__main__':
    print(lowest_number());
