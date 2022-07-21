def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max

# Need to have a parameter for function. Don't add list in function or else you won't have something to plug in later.
