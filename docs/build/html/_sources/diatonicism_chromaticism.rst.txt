Diatonicism --- Chromaticism --- Enharmonicism
==============================================

"When we think about harmony, we automatically think about chords. In
fact, we are so fixated on chords that we sometimes forget they tell
only part of the story" :cite:t:`Tymoczko2011_GeometryMusicHarmony`, p. 154.

The development of tonality can also be described as a change in two
dimensions: key-distance and separatedness (tonal closure/unity).

-  Baroque: Keys are relatively close to each other but changes occur
   frequently, tonicizations are commonplace

-  Classic: Keys are relatively close to each other and key sections are
   larger and relatively homogenuous

-  early Romantic: Keys are further apart and key sections are larger
   and relatively homogenuous

-  late Romantic: Keys are further apart but changes occur frequently

Here a tabular overview of this hypothesis:

+----+---------+-----------+------------------+
+----+---------+-----------+------------------+
|    | small   | large     |                  |
+----+---------+-----------+------------------+
|    | small   | Baroque   | Late Romantic    |
+----+---------+-----------+------------------+
|    | large   | Classic   | Early Romantic   |
+----+---------+-----------+------------------+

Table: Stages of Tonality.

Expansion of tonal material
---------------------------

Based on :cite:`Gardonyi2002_Harmonik`: (see MGG “Diatonik --
Chromatik -- Enharmonik”)

- same diatonic region on LoF: relative keys/scales - although
  theoretically, LoF is equivalent to :math:`\mathbb{Z}`, composers use
  only a relatively small subset of it
- individual intervals can be associated with a regime on the
  fifth-width space: m2 (5Q) is diatonic, wheras A1 (7Q) is chromatic, and
  A7\ :math:`\approx`\ P8 (12Q).e
- compare with “pitch class circulation” :cite:`Tymoczko2011_GeometryMusicHarmony`, p. 158ff.
- fifth width measures Diatonicism -> Chromaticism -> Enharmonicism, :cite:`Gardonyi2002_Harmonik`, p. 243

[Insert image from SysMus tutorial]

- Analyze also the variance of fifth-widths, not only the means!

How can enharmonic exchange (Verwechslung) and enharmonic equivalence
(Umdeutung) distinguished? The former implies a reinterpretation of
tonal pitch classes, i.e. a transition to a different location in tonal
space, whereas the former is only motivated by notational constraints
(parsimony) and tonal/diatonic relations remain constant.

For example, in Debussy’s *Claire de lune*. It is in D\ :math:`\flat`
major with a middle segment in C\ :math:`\sharp` minor which is
enharmonically equivalent to D\ :math:`\flat` minor but only has four
sharps instead of eight flats.

First, enharmonic equivalence should only be invoked to render notation
easier, not more difficult. This means, that the number of accidentals
has to be reduced by the transformation.

Second, the key in question should be in a direct relation with the
preceding and/or consequent key. In the case of the reinterpretation of
the German sixth chord as a dominant chord effects a key shift by a
semiton, which is far away in tonal space (LoF). In the Debussy example,
the keys are only :math:`R` related after applying the equivalence.

Expansion of local harmonic content
-----------------------------------

Fifth width per measure in a piece.

A couple of examples

Over time
~~~~~~~~~

The change in fifth widths is differently on a global (piece) and a
local (measure) scale. Globally, pieces cross the boundary to
chromaticism quite early (which can already happen with ficta), and even
to enharmonicism (because modulations to distant keys takes place). At
the same time looking on a local harmonic scale we see that chromatic
(“dissonant”) harmonies are rare on average (mode, mean, median) but are
increasing historically (with an interesting wavelike pattern - what
does it mean?). Locally, pieces do not cross the enharmonic threshold
(on average)

.. .. figure:: img/macro/local_fifth_width.png
..    :alt: Averages (mean, mode, and median) of per-measure fifth widths
..    over time.

..    Averages (mean, mode, and median) of per-measure fifth widths over
..    time.

Enharmonic spectrum
-------------------

In the extreme case, for each note, a random tonal representative of the
neutral pitch class is sampled uniformly. => unpredictable because
infinite possibilities.

In practice, only a few representatives are likely candidates: not
uniform prior on representatives but concentrated (has *a lot* to do
with surrounding notes–context–but this is not possible on the
bag-of-notes model).

Anyway, *if* absolute enharmonicism would prevail, the prior on the
representatives would be flat (but this does not even happen in 12-tone
music, show some examples). In “moderate” enharmonicism, some candidates
would be preferred.

I can measure hoe many representatives of a pitch class occur in a
piece.

=> **enharmonic pitch-class entropy** is a measure of enharmonicism
(works obviously only with spelled pitch classes)

But: Even in a Bach piece (or older), e.g. F\ :math:`\sharp` and
G\ :math:`\flat` can co-occur. Because they occur in different contexts
(different keys/tonal centers), they are **not** enharmonically
equivalent. In the bag-of-notes model we need to factor in the fact of
how likely it is to belong to a tonal center:

Which I already can estimate because of the mixture/topic model!

Thus, **enharmonicism** can be operationalized as the pitch-class
entropy, weighted by the likelihood to belong to different
tonalities/clusters/keys/tone fields.

=> maybe inverse weight, because: higher weights of F# and Gb in a Bach
piece should trigger a new mixture component whereas in an extended
tonal piece it might just adjust the parameters of existing components
(variance)

[By the way, enharmonic distance is 12n (in fifths)]

But maybe also: actually inverse because in tonal music, enharmonic
notes are outliers whereas in enharmonic music they get a lot of
probability mass.

But then: How to distinguish enharmonically equivalent tonal regions
from random enharmonicity?

—> entropy might help

If entropy is low, they should be outliers. If it is high, enharmonicism
can be assumed.

Entropy is **highest** when all representatives are equally likely
(ideally, 12-tone music).

Thus: the higher the enharmonic pitch-class entropy the higher is
enharmonicism.

**Hypothesis:** EPCE increases over time (and is maximal with 12-tone
compositions)

.....

Segmentation can be either achieved in a fixed manner by bars, groups of
bars, or segmentation sign posts such as key-signature changes or double
bars.

A data-driven segmentation could use the notes themselves.

Then, segment length :math:`l` would be informative about tonal
stability / rate of tonality changes

- given the optimal number of clusters from the mixture model, apply
  key-scape algorithm. It should give rise to a much clearer
  segmentation with :math:`K<<24` components.
- Again, use Information Theory to determine best segmentation. (lowest
  entropy, per segment?, KL divergence with component distributions?)
- How can these differences be measured? (not always binary)

.. -  Horizontally: Streams (*Auditory Scene Analysis*; :cite:`Bregman1990_AuditorySceneAnalysis`)
.. -  Vertically: Building blocks / units –> Gestalt laws, Segmentation 
..    :cite:`Hanninen2012_TheoryMusicAnalysis,Lerdahl1983_GenerativeTheoryTonal`

Laws can govern *primary parameters* which allow for syntactic relations
between discrete units (such as pitch, or rhythm), and *secondary
parameters* which discribe continous dimensions such as timbre,
dynamics, etc.

**Tonal Centers**

- Number of Tonal Centers
- Distance of Tonal Centers
- Divergence on the Tonnetz
