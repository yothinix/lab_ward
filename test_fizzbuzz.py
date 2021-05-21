from ward import test


def fizzbuzz(input: int) -> str:
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"

    return str(input)


for input, expected in [
        (1, "1"),
        (2, "2"),
        (3, "Fizz"),
        (6, "Fizz"),
        (5, "Buzz"),
        (10, "Buzz"),
        (15, "FizzBuzz")
]:
    @test("test {input} should return {expected}")
    def _(input=input, expected=expected):
        assert fizzbuzz(input) == expected

