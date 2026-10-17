import sys

#sys.path.append("../")

import main

def test_fizzbuzzNum():
    assert main.fizzbuzz(37) == 37
def test_fizz():
    assert main.fizzbuzz( 3) == "Fizz"
def test_buzz():
    assert main.fizzbuzz( 5) == "Buzz"
def test_fizzbuzz():
    assert main.fizzbuzz(15) == "FizzBuzz"
