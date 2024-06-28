def main():
    result = []
    while True:
        start = input('Enter the starting letter: ')
        end = input('Enter the Ending letter: ')
        if (start.isalpha() and len(start) == 1) and (end.isalpha and len(end) == 1):
            start_num = ord(start)
            end_num = ord(end)
        else:
            print ('Only enter single character letters')
            continue
        if start_num > end_num:
            print ("The start letter needs to be before the end letter")
        else:
            break
        
    for i in range(start_num, end_num + 1):
        result.append(chr(i))
        
        

    """
    ########################################
    Code Your Program here
    ########################################
    """
    
    

    print(*result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
