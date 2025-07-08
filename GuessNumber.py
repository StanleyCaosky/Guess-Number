import random
r = random.randint(1, 50)

def guessnumber(missnumber):
    if int(missnumber) == r:
        return "Correct"
    elif int(missnumber) < r:
        return "Your number is too low"
    elif int(missnumber) > r:
        return "Your number is too high"

def guesstimes(timenumber):
    onethirdtimes = timenumber // 3
    twothirdtimes = timenumber // 2
    maxtimes = random.randint(onethirdtimes, twothirdtimes)
    return int(maxtimes)

themaxtime = guesstimes(r)

print("You have" + str(themaxtime) + "times to guess the number between 1 and 50")
print("please enter your number")

times = 0
for times in range(0,themaxtime,1):
    guess = input()
    result = guessnumber(guess)
    print(result)
    times = times + 1
    if result == str("Correct"):
        break
if times > round(int(themaxtime)):
    print("Game Over, You Lost")
