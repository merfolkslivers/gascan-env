# Technically a skill *section*.
# For a single-part skill like CEO Ameterasu (V-BT01/007EN), this object would store the [COST: CB1] part,
# and a SkillEffect that dictates the entirety of "draw a card, then scry 1".
# However, for multipart skills, things get sketchy:

# Rainy Tear, Stezza [V-EB05/015EN] - Her SkillTrigger puts this on standby. We present COST, and if it's paid,
# then we execute the SkillEffect, then the SkillEffect immediately executes another Skill with the second COST, and
# has its own SkillEffect.

# Great Sage, Barron [V-BT05/015EN] - SkillTrigger puts this on standby. self presents a unit choice. If the choice is
# made, SkillEffect.SkillTrigger checks if the chosen unit is eligible for requesting the cost of the second Skill,
# then executes it if so.

# We'll have to revisit this approach if we can't easily pickle/unpickle a board state during the execution of a skill,
# as when choice data made in an earlier Skill object must be accessed in a subsequent Skill or that Skill's
# SkillEffect.