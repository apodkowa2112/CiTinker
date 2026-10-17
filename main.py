
def fizzbuzz(num):
    strng = '';
    if (num % 3 == 0): strng =  "Fizz";
    if (num % 5 == 0): strng += "Buzz";
    if (strng == ''): strng = num;
    return strng
