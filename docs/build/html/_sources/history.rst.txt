Historical usage of tonal pitch classes
=======================================

Apart from counting the number of tonal pitch classes in an individual
musical piece, comparing these distributions between pieces and across
historical time is interesting. In the last section we compared a small
number of pieces manually. This section attempts at quantifying these
intuitions and gaining a picture of the larger view.

The question is, how does the usage of tonal pitch classes change over
time? Can we infer something about tonality from this change? An
immediate caveat that comes to mind is that pieces often feature very
different sets of notes because they are, for instance, in a different
mode (both in the pre-tonal as well in the tonal sense), or key. It is
therefor a standard preprocessing step in computational musicology to
normalize pitch class distributions by transposing every piece to the
same key in order to make them commensurate. For the same reasone, the
chord symbols in the datasets analyzed in part [part:meso] where encoded
with relative Roman numerals and not their absolute chord names. But in
order to perform this normalization step, one needs to know the key of a
piece. **(Well, not really: Harasim et al. 2019)** Moreover, the concept
of “key” does not mean the same thing for all musical styles. Bach’s
B-minor Mass and Liszt’s B-minor Sonata share the same nominal key but
differ greatly with respect to their pitch-class distributions. Since
the underlying tonality has changed, the derivative concept of key has
changed, too. And just identifying B as the most common note in both
pieces as indicative for the key (**check if that is the case**) is not
a solution either because this procedure would also identify Renaissance
locrian pieces as having the same key without even having touched the
problem of how to infer the mode.

We come back to this issue in later chapters (**WHERE?**). Maybe it is
appropriate to inspect the absolute pitch distributions of pieces before
delving into the issue of relative pitch classes. This is what this
chapter is about.

Modeling tonal pitch-class evolution
------------------------------------

Tonal pitch classes on the line of fifths can be mapped to integers
:math:`k \in \mathbb Z`. An interval :math:`I=[a,b]\subseteq\mathbb Z`
is called a **line-of-fifths segment** and its length is
:math:`n=|b-a|, a<b`. The distribution of tonal pitch classes at time
:math:`t` (in a piece or in historical time) is modeled as a draw from a
Dirichlet distribution:

.. math:: X^{(t)}\sim \mathrm{Dir}(\mathbf{\alpha}), \mathbf{\alpha}\in\mathbb R^n.

Importantly, in this model, the dimensions of :math:`X^{t}` have no
inherent order. This means that the model knows nothing about the line
of fifths anymore. The ordering of pcs along this line is just for
convenience. The probability of the pitch class :math:`k = i-a` at time
:math:`t` is given by the :math:`k+a`\ th component of the vector
:math:`X^{(t)}`, :math:`p(k | t)=X_{k+a}^{t}` The diachronic change of
these distributions forms a process

.. math:: \mathbf{X}=(X^{(1)},\dots,X^{(t)},\dots,X^{(T)})\in \mathbb R^{n\times T},

 such that :math:`\sum_i X_i^{(t)}=1,\forall t`.

Variability in tonal pitch-class usage
--------------------------------------

We count the occurrence of tonal pitch classes in all pieces and trace
the change between them across the historical timeline. Based on
theoretical reasoning :cite:p:`Temperley2000_LineFifths,Gardonyi2002_Harmonik`,
we have already seen in section [sec:bagofwords] that it seems to be the
case that sorting pitch classes along the line of fifths reveals
structural connections between the pitch classes. For that reason we
plot the pitch classes along this axis and also use colors to encode
this relation.

As Figure [fig:piece\_dist] has shown, the dataset is not uniformly
distributed over time. On one hand, there are some large gaps between
periods, whereas on the other hand some years contain many pieces at the
same time.

For years without data, we take the assumption that “nothing changes”
and keep the values from the last where were data was available. For the
years with many pieces, we add up the pitch class counts, so that they
all contribute to the calculation.

| 
| ...
| A **rolling mean**, also called a moving average, is calculated over
  the whole historical range. It is common that sliding windows are
  centered. But because it makes more sense for historical data to only
  consider previous events because future events have no impact, the
  result of the sliding window takes into account all :math:`t` previous
  years.

For a value :math:`x_t` in year :math:`t`, and window size :math:`s`,
the rolling mean :math:`\bar x` is defined as

.. math::

   \begin{aligned}
       \bar x = \frac{1}{s}\sum_{i=0}^{s-1} x_{t-i}.\end{aligned}

This definition allows a scalable perspective on historical
developments. Adjusting the windows size allows to all historical
periods in the range of the historical frame under consideration. For
instance, setting :math:`s=50` will lead to a curve that at any point
represents the average value of the last 50 years, if years are the unit
of time.

This is done for the tonal pitch-class distributions of aggregated
pieces and is shown in Figure [fig:evolution\_tpcs]. It is a complex
plot and we will discuss each part at a time.

.. .. figure:: ../img/macro/tpcs_smooth(50).png
..    :alt: The evolution of tonal pitch classes taking into account a
..    50-year window.

..    The evolution of tonal pitch classes taking into account a 50-year
..    window.

The legend above the two subplots show the mapping of tonal pitch
classes to colors. Since tpcs are isomorphic to :math:`\mathcal Z`, as
mentioned above, it is possible to map flat tpcs to negative numbers,
shown as graded blue colors, and to map sharp tpcs to positive numbers,
shown as graded red colors. The tpc C is mapped to zero which
corresponds to the color white in this plot.

The plot immediately below the legend shows the smoothed distribution of
tonal pitch classes over time, sorted by the associated colors. The two
dashed curves demarcate the white-note diatonic tonal pitch classes F to
B. It is important to note here that in the bag-of-notes model tonal
pitch classes are expressed as multinomial distributions. This means
that there is no inherent order to the pitch classes–there is no
structure in the bag. The coloring and sorting is done on theoretical
grounds, but we will soon see that this ordering makes also sense for
the data at hand.

The dark line throughout this plot shows the normalized entropy of the
pitch-class distributions at any point in time. This line is smoothed by
the same procedure as the individual per-year pitch-class distributions
and is thus an adequate measure for the randomness of these
distributions for a given year. Taking into account a 50-year window
shows that randomness slightly increases over time with some wiggles
along the way. The value of this line is independent of the number of
tonal pitch classes in a given year, since it is normalized by its
maximal value which is given by :math:`\log(n)` where :math:`n` is the
number of non-zero tonal pitch classes in that year.

The red line in the bottom plot in Figure [fig:evolution\_tpcs] shows
the ratio of non-zero “sharp” tpcs (G, D, A, ...) to non-zero “flat”
notes (F, B\ :math:`\flat`, E\ :math:`\flat`, etc.), defined as
:math:`q=s/f`, where :math:`s` is the number of sharp tpcs (not unique
but the actual number), and :math:`f` is the number of flat notes. If
:math:`f=0`, the ratio :math:`q` is not defined. Since the analysis is
based on the moving average, as well, a piece with no flats (which
implies also F) is excluded. Since the window size is considerably
large, there is no sliding window that contains only pieces with
non-flat notes so that :math:`q` is always defined as can be seen by the
smoothness of the red line. As can be seen, this curve shows
considerable variation. In both subplots, saddle points correspond to
regions where no data is available so no interpretation should be given
for these areas.

**Bootstrap sample CIs!**

If a musical piece exclusively contains the seven diatonic tpcs, and if
they are furthermore uniformly distributed in this piece, the
sharp-to-flat ratio is :math:`q=|\{G, D, A, E, B\}/|F|=5`. Which is
exactly what we see in the beginning of our timeline.

The reverse statement that diatonic notes are uniformly distributed if
the ratio is :math:`q=5` is not necessarily true. In fact, there are
non-diatonic notes present at the beginning of the timeline, namely
B\ :math:`\flat` in the flat direction, and F\ :math:`\sharp` and
C\ :math:`\sharp` in the sharp direction. A uniform ratio would be then
:math:`q=|\{G, D, A, E, B, F\sharp, C\sharp\}/|B\flat, F|=3.5` So we can
rule out uniformity, also because the entropy (the black line in the
upper plot) is not maximal. The question is, whether the non-randomness
in these distribution tells us something about tonality and its
historical development. We come back to this question later.

The smoothed trends in both subplots show that sharpward tpcs are
generally much more common if not only because all diatonic pitches are
already sharps except F. More precisely, sharp notes occur roughly five
times more often than flat notes until the last quarter of the fifteenth
century. This might be due to the fact that almost only diatonic notes
are being used, with relatively constant but low B\ :math:`\flat`\ s
**(transposed modes!)**. On the sharp side of the spectrum,
F\ :math:`\sharp`\ s occur rarely, as do C\ :math:`\sharp`\ s which
lends itself to the interpretation that these notes do reflect the
**musica ficta**. Other accidentals occur vanishingly seldom.

Around 1460 there is a decline in :math:`q` that stabilizes around 1530
where the sharps occur only three times as often as flats. This is due
to an increased use of flat notes F and B\ :math:`\flat`. Somewhat
surprisingly, F\ :math:`\sharp` and higher sharps are absent in this
period. But for modal music that is a logical consequence. If the
transposed modes are used more often, sharp notes are less likely to
occur.

In the second half of the 16th century, E\ :math:`\flat` appears for the
first time in the corpus in a substantial and stable way. But also
F\ :math:`\sharp` comes back so it is counterbalanced and the ratio
stays roughly the same.

Towards the end of the 16th century, we see a dramatic increase in the
sharp-flat ratio that continues until the middle of the 17th century and
reaches a more than 7-fold peak. This is due to the disappearance of
almost all flats below B\ :math:`\flat`, while the sharps
C\ :math:`\sharp`, G\ :math:`\sharp`, and D\ :math:`\sharp` become even
stronger (and never vanish again). In this period, music seems to shift
to the sharp side. While modal music featured the basid diatonic modes
plus downward transposition to the flat side by one, here we see more
and more accidentals.

...going into dominant regions means going sharpwards.

But this peak lasts only shortly. Around 1700 the sharp-flat ratio has
fallen back to its earlier point around 2.5. But although the ratio is
the same, the tpc usage is quite different. Now many more sharps and
flats are employed than ever before. More importantly, this peak marks
the beginning of the Baroque period. The first Baroque composer in the
corpus is Corelli (also the most frequent one). There are a lot of
pieces from him at the end of the 17th century.

A surge of flats around 1800 brings the ratio down to its lowest point
since ca. 1530 and remains relatively stable throughout the 19th
century. There is a slight rise and decay over the course of this
century. Both sharps and flats increase in this time but more so do the
flats.

In the early 20th century there is the third lowest point where flats
dominate sharps (“renaissance of the Renaissance”? Vaughan Williams,
Finzi, ...)
