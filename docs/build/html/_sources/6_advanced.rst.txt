Advanced applications
=====================

.. _Pitch spelling:

Pitch Spelling 
--------------

:cite:t:`Meredith2005_ComparingPitchSpelling,Meredith2006_Ps13PitchSpelling`
:cite:t:`Cambouropoulos2003_PitchSpellingComputational,Chew2005_RealTimePitchSpelling`
:cite:t:`Stoddard2004_WelltemperedSpellingKeyinvariant`
:cite:t:`Temperley2001_CognitionBasicMusical`

Style (classification)
----------------------

Feature clustering
~~~~~~~~~~~~~~~~~~

(k-means, PCA, ...)

Hierarchical clustering
~~~~~~~~~~~~~~~~~~~~~~~

History
-------

(regression, GPs)

- trends (maybe with a non note-based dataset e.g. metadata)

Performance
-----------

- Spotify API to compare different recordings


Modeling musical sequences
--------------------------

Hierarchical theories
~~~~~~~~~~~~~~~~~~~~~

describe central Schenkerian concepts in terms 
of tones, intervals, and underlying tonal spaces.
E.g., a neighbor note is the next note (upper or lower)
in a tonal space that has a notion of neighborhood, e.g.
the diatonic or chromatic spaces. But in this generalized sense,
a neighbor can be a semitone, a whole tone, a third, or a fifth
apart. What the neighbor actually is, depends on the underlying 
assumed tonal space. Accordingly, the *Bassbrechung* is an upper 
neighbor on the circle or line of fifths, while the common neighbor note
only exists in diatonic spaces.

Formal models for music sequences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See overview in :cite:`Rohrmeier2012_ComparingFeatureBasedModels`

Regular Expressions
...................

(chord symbols, rhythms)

n-gram models
.............

(melody, rhythms)

Hidden Markov models
....................

(harmony)

Probabilistic Context-Free Grammars
...................................

(form; choro) :cite:`Moss2020_HarmonyFormBrazilian,Moss2020_ChoroSongbookCorpus`
 
More advanced models
....................

Neural nets