# Used by:
# Ship: Cerberus
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Heavy Assault Cruisers").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Missiles"),
                                    "explosionDelay", ship.getModifiedItemAttr("eliteBonusHeavyGunship1") * level)
