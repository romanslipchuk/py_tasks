"""
Bithday paradox game by Swegard
"""

import datetime, random


def getBirthdays(numberOfBirthdays):
    #  Returns list of birthdays

    birthdays = []
    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001,1,1)
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birhtday = startOfYear + randomNumberOfDays
        birthdays.append(birhtday)
    return birthdays

def getMatch(birthdays):
    """
    :param birthdays:
    :return: All matching birthdays
    """
    if len(birthdays) == len(set(birthdays)):
        return None
    for a, BirthdayA in enumerate(birthdays):
        for b, BirthdayB in enumerate(birthdays[a+1:]):
            if BirthdayA == BirthdayB:
                return BirthdayA


print("Birthday Paradox Game starts NOW")

MONTH = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print("How many birthdays shall I'll generate? (max 100)")
    responce = input('> ')
    if responce.isdecimal() and (0 < int(responce) <= 100):
        numBDays = int(responce)
        break
print()

print('Here are, ', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    monthName = MONTH[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')
print()
print()

match = getMatch(birthdays)

# Print results
print('In this simulation, ', end='')
if match != None:
    monthName = MONTH[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('Multiple people have a birthday on:', dateText)
else:
    print('There no matching birthdays.')
print()

print('Generating,',numBDays, 'random birthdays 100_000 times...')
input('Press Enter to begin...')

simMatch = 0
for i in range(100_000):
    if i %10_000 == 0 :
        print(i, 'simulations run...')
        birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100_000 simulations run.')

probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100_000 simulations of', numBDays, 'people, there was a')
print('matching birthdays in that group', simMatch, 'times. That means')
print('that', numBDays,' people have a', probability, '% chance of')
print('having a matching birthdays in their group.')

## TODO: ответить на вопросы по birthday paradox game