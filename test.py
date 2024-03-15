while True:
    print( 'Please select the process you want to perform.' )
    print( '1:Enter evaluation points and comments' )
    print( '2:Check the results so far' )
    print( '3:End' )
    num = input()
  
    def option_one():
        while True:
            print( 'Please input the rating from 1 to 5' )
            point = input()
            if point.isdecimal():
                point = int(point)
                if  point <= 0 or point > 5: # Conditional expression that it is less than 0 or greater than 5
                    print( 'Please input the rating from 1 to 5.' )
                    point = str(input())
                else:
                    print( 'Please enter your comment.' )
                    comment = input()
                    post = f'A point: {point} Comment: {comment}'
                    file_pc = open("data.txt", 'a')
                    file_pc.write( f'{ post } \n' )
                    file_pc.close()
                    break
            else:
                print( 'Please enter the evaluation points in numbers.' )

    def option_two():
        print( 'The results so far' )
        read_file = open("data.txt", "r")
        print( read_file.read() )
        read_file.close()    
    
    if num.isdecimal():
        num = int(num)
        if num == 1:
            option_one()   
        elif num == 2:
            option_two()
        elif num == 3:
          print( 'It will end' )
          break  # The syntax to end the repetitive process
        else:
            print( 'Please enter from 1 to 3.' )
    else:
        print( 'Please enter from 1 to 3.' )    
    