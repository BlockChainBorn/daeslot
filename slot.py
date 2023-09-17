
import random

class SlotMachine:
    def __init__(self):
        self.credit = 1000  # 💰 Initial credits for the player
        self.cash = 20  # 💸 Cost per game
        self.total_won = 0  # 🏆 Total amount won
    
    def check_credit(self):
        """💡 Check if the player has enough credit to play."""
        return self.credit >= self.cash
    
    def spin(self):
        """🎰 Simulate spinning the slot machine."""
        wheel1 = random.randint(1, 9)
        wheel2 = random.randint(1, 9)
        wheel3 = random.randint(1, 9)
        return wheel1, wheel2, wheel3
    
    def get_reward(self, wheel1, wheel2, wheel3):
        """🎉 Calculate the reward based on the numbers on the wheels."""
        if wheel1 == wheel2 == wheel3:
            reward = self.cash * 10
        elif wheel1 == wheel2 or wheel1 == wheel3 or wheel2 == wheel3:
            reward = self.cash * 2
        else:
            reward = 0
        return reward
