# Used by:
# Subsystem: Loki Defensive - Adaptive Shielding
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Minmatar Defensive Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Remote Shield Booster",
                                  "shieldBonus", module.getModifiedItemAttr("subsystemBonusMinmatarDefensive2") * level)
