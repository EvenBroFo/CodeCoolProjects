import random


class CowsAndBulls:
    def __init__(self):
        self.target = str(random.randint(1000, 9999))
        self.state = "ongoing"
        self.guess_count = 0

    def guess(self, number):
        self.guess_count += 1

        cows = 0
        bulls = 0
        remaining_target = []
        remaining_guess = []

        for target_digit, guess_digit in zip(self.target, number):
            if target_digit == guess_digit:
                cows += 1
            else:
                remaining_target.append(target_digit)
                remaining_guess.append(guess_digit)

        for digit in remaining_guess:
            if digit in remaining_target:
                bulls += 1
                remaining_target.remove(digit)

        if cows == 4:
            self.state = "finished"

        cow_word = "cow" if cows == 1 else "cows"
        bull_word = "bull" if bulls == 1 else "bulls"

        return f"{cows} {cow_word}, {bulls} {bull_word}"


    

