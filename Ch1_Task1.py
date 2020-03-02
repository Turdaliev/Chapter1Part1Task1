def is_even(number):

    if number % 2 == 0:
        return True
    else: 
        return False 

    # return (number%4) 

def test_is_even():

    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(8) == True
    assert is_even(100) == True
    assert is_even(103) == False
    print("Your code is CORRECT")
    
test_is_even()

