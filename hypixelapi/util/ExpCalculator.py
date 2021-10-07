
# https://hypixel.net/threads/calculate-bedwars-level-from-exp-javascript.2022078/
# translation of KAD7's javascript code wich was originally translated from Plancke's ExpCalculator in php

import math

class ExpCalculator:
    EASY_LEVELS = 4
    EASY_LEVELS_XP = 7000
    XP_PER_PRESTIGE = 96 * 5000 + EASY_LEVELS_XP
    LEVELS_PER_PRESTIGE = 100
    HIGHEST_PRESTIGE = 10

    def getLevelForExp(self, exp):
        prestiges = math.floor(exp / self.XP_PER_PRESTIGE)
        level = prestiges * self.LEVELS_PER_PRESTIGE
        expWithoutPrestiges = exp - (prestiges * self.XP_PER_PRESTIGE)

        for i in range(1, self.EASY_LEVELS+1):
            expForEasyLevel = self.getExpForLevel(i)
            if (expWithoutPrestiges < expForEasyLevel):
                break
            level += 1
            expWithoutPrestiges -= expForEasyLevel
        return level + math.floor(expWithoutPrestiges / 5000)

    def getExpForLevel(self, level):
        respectedLevel = self.getLevelRespectingPrestige(level)
        if respectedLevel == 0:
            return 0
        elif respectedLevel == 1:
            return 500
        elif respectedLevel == 2:
            return 1000
        elif respectedLevel == 3:
            return 2000
        elif respectedLevel == 4:
            return 3500
        return 5000

    def getLevelRespectingPrestige(self, level):
        if level > self.HIGHEST_PRESTIGE * self.LEVELS_PER_PRESTIGE:
            return level - self.HIGHEST_PRESTIGE * self.LEVELS_PER_PRESTIGE
        else:
            return level % self.LEVELS_PER_PRESTIGE


def expToLevel(exp):
    return ExpCalculator().getLevelForExp(exp)
