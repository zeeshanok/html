import pyautogui, time, random
print('Welcome to spam bot 1000!\nMove ur cursor to one of the corners of ur screen if u feel like u should be merciful')
print()
phrase = input('\tWhat u want to spam bro?: ')
times = int(input('\tHow much do u want to annoy ur friends bro?: '))
delay = input('\tWhat delay do u want broo? In milliseconds\n\t(Keep this blank if u want to go next level): ')
print()

l1 = phrase[0].lower()
l2 = phrase[0].upper()
e1 = phrase[len(phrase)-1].lower()
e2 = phrase[len(phrase)-1].upper()
xphrase = phrase[1:len(phrase)-1]
cond1 = True
cond2 = False
print('Spamming will start in 3 seconds. Get Ready!\n')
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1\n')
time.sleep(1)
print('Spamming has started!')
# The spamming happens here
for i in range(times):
    if delay != '':
        time.sleep(int(delay)/1000)
    pyautogui.typewrite((l1 if cond1 else l2) + xphrase + (e1 if cond2 else e2) + '\n')
    cond1 = True if random.randint(0, 1) == 0 else False
    cond2 = True if random.randint(0, 1) == 0 else False

print('Spamming is complete!')
print('I hope ur friends had a great day!')
