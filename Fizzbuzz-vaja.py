print "Pozdravljeni v igri FizzBuzz"

guess = 0


guess = raw_input("Vpisi stevilo od 1 do 100: ")
guess = int(guess)

for guess in range(1, guess + 1):

    if guess % 3 == 0 and guess % 5 == 0:
        print "FizzBuzz"

    if guess % 3 == 0:
        print "Fizz"

    if guess % 5 == 0:
        print "Buzz"

    else:
        print guess