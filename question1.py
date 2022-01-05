''' WRITE A PYTHON FUNCTION THAT TAKES A SEQUENCE OF NUMBERS AND DETERMINES WHETHER ALL THE NUMBERS ARE 
   DIFFERENT  FROM EACH OTHER .'''
def test_distinct(data):
    if len(data)==len(set(data)):
        return True
    else:
            return False
 
print(test_distinct([1,2,3,4,5]))
print(test_distinct([1,2,3,3,4]))
print(test_distinct({1,4,4,5,6}))