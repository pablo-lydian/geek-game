import random

import numpy as np

import dice


class GeekOutMasters:

    def __init__(self, inactive_dice_on_start, active_dice_on_start, utilized_dice_on_start):
        self._inactive_dice = inactive_dice_on_start
        self._active_dice_size = active_dice_on_start
        self._active_dice = []
        self._utilized_dice = utilized_dice_on_start

    def play_round_using(self, strategy):
        self._roll()
        

    def _roll(self):
        self._active_dice = [random.choice(GameMaster.FULL_DICE) for _ in range(self._active_dice_size)]


class GameMaster:
    ACTIVE_DICE = {dice.Heart, dice.Rocket, dice.SuperHero, dice.Troll}
    FULL_DICE = [dice.Heart, dice.Rocket, dice.SuperHero, dice.Troll, dice.FortyTwo, dice.Dragon]

    @classmethod
    def is_action_die(cls, die):
        return die in cls.ACTIVE_DICE

    @classmethod
    def has_action_die(cls, a_dice):
        return np.any([cls.is_action_die(die) for die in a_dice])
