import sys

#sys.path.append("../")

import main

def test_fizzbuzz():
    
    assert main.fizzbuzz(37) == 37
    assert main.fizzbuzz( 3) == "Fizz"
    assert main.fizzbuzz( 5) == "Buzz"
    assert main.fizzbuzz(15) == "FizzBuzz"
