def is_bear(word):
    return word + 'bear'

tester = ['humaira', 'aboo', 'ibraheem']


print map(is_bear, tester)


nums = [41, 41, 17, 15, 13, 11]


def multiply(one, two):
    return one * two


print multiply(3, 5)
print reduce(multiply , nums)
