# This module is the implementation of the damage calculator
# Basic formula:  [servantAtk * npDamageMultiplier * (firstCardBonus + (cardDamageValue * (1 + cardMod))) * classAtkBonus * triangleModifier * attributeModifier * randomModifier * 0.23 * (1 + atkMod - defMod) * criticalModifier * extraCardModifier * (1 - specialDefMod) * {1 + powerMod + selfDamageMod + (critDamageMod * isCrit) + (npDamageMod * isNP)} * {1 + ((superEffectiveModifier - 1) * isSuperEffective)}] + dmgPlusAdd + selfDmgCutAdd + (servantAtk * busterChainMod)




def calculator(servantName, servantAtk, enemyName):

