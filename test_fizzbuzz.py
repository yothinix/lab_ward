from ward import test

def fizzbuzz(input: int) -> str:
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"

    return str(input)


@test("test 1 should return 1")
def _():
    assert fizzbuzz(1) == "1"

@test("test 2 should return 2")
def _():
    assert fizzbuzz(2) == "2"

@test("test 3 should return Fizz")
def _():
    assert fizzbuzz(3) == "Fizz"

@test("test 6 should return Fizz")
def _():
    assert fizzbuzz(6) == "Fizz"

@test("test 5 should return Buzz")
def _():
    assert fizzbuzz(5) == "Buzz"

@test("test 10 should return Buzz")
def _():
    assert fizzbuzz(10) == "Buzz"

@test("test 15 should return FizzBuzz")
def _():
    assert fizzbuzz(15) == "FizzBuzz"
