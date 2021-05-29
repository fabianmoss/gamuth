# %%
from gamuth import Tone, Interval, PitchClassSet
# %%

s = Tone(0,1,1)
t = Tone(0,4,-1)

i = Interval(s, t)

# %%

pcs = PitchClassSet({0,4,7})
# %%
pcs.transpose(3)
# %%

pcs.invert(0)
# %%
list(pcs.interval_class_vector())
# %%

diatonic = PitchClassSet({5,0,7,2,9,4,11})

diatonic.interval_class_vector()
diatonic.complement
print(diatonic.normal_form())
# %%

straus = PitchClassSet({8,9,11,0,4})
straus.normal_form()

# %%

aug = PitchClassSet({4,0,8})
aug.normal_form()
# %%
