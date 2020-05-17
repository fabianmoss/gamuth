.. .. role:: math(raw)
..    :format: html latex
.. ..

.. .. role:: raw-latex(raw)
..    :format: latex
.. ..

.. .. contents::
..    :depth: 3
.. ..

Pitch-class based music analysis
================================

Musical pieces are made up of notes. This almost trivial truth is the
starting point for this endeavour: to uncover hidden patterns in
compositions dispersed through the centuries from the late middle ages
to modern times.

First, we will develop an understanding which notes exist and what their
mutual relations are. We will then proceed to use this information to
discover aspects of the structural relations between them and how the
constitute musical spaces (generalized interval systems).

We will see that musical notes in compositions are used far from
randomly and that the order encoded in musical pieces reveals
acquaintances between composers that sometimes transcends separation in
time.

Finally, we will see how the usage of musical notes changes over the
course of history. Observing large-scale changes in compositional style
we will be able to distinguish historical trends.

...

The study is based on the music as it is notated. Moreover, we assume
octave equivalence. These two assumptions–one given by the
representation of notes in the data, the other based on theory and
previous literature–leads to the Spiral Array representation of tonal
space.

Tonality is constituted by the ways composers navigate pitch space in
their compositions. This is, of course, hierarchal. Each piece
constitutes a unique instance of tonality which nonetheless shares many
properties with “similar” compositions (similar in style).

But what is pitch space?

Frequency space
---------------

A frequency :math:`f` is measured in Hertz (1/sec). We can represent the
set of fundamental frequencies as
:math:`F=\{ K \cdot 2^o \cdot 3^q \cdot 5^t\mid o, q, t \in \mathbb Q \}`
for a fixed *Kammerton* :math:`K`, and :math:`o, q, t\in \mathbb Q`. K
has been standardized to :math:`K=440~\text{Hz}` in 1939. Hence, each
fundamental frequency can be represented as
:math:`f=440 \text{ Hz} \cdot 2^o \cdot 3^q \cdot 5^t`. Here, 2, 3, and
5 are arbitrary pairwise coprime integers (See Mazzola, 1985, p. 26) but
this choice relates to the numerators of the fundamental frequency
ratios of the music theoretical basic intervals of two frequencies
:math:`f` and :math:`g` in just intonation:

-  octave: :math:`f:g = 2:1`

-  fifth: :math:`f:g=3:2`

-  major third: :math:`f:g = 5:4`

The fact that :math:`o, q, t` are :math:`\in \mathbb Q` allows for
unique solution of the equations
:raw-latex:`\citep[A1.1.2]{Mazzola1985,Mazzola2018}`.

Pitch space
-----------

*Pitch* (or *pitch height*) is the perceptual correlate to a fundamental
frequency and is measured on a linear scale. It can be calculated as
:math:`p(f) = 69.0 + 12 \cdot \log\_2(f/440 \text{ Hz}) `, where 69.0
represents the pitch number of the Kammerton :math:`K`, and 12 is the
size of the octave in the unit of :math:`p`. The formula thus gives the
distance from the reference pitch (69=A4) as a proportion
(:math:`\log_2(f/g)`) of the octave (12). In this representation middle
C (C4) gets the pitch number 60.

.. math::

   .. \begin{aligned}
    p(f) & = c_1+c_2\cdot \log_2\left(\frac{440 \text{ Hz}\cdot 2^o \cdot 3^q \cdot 5^t}{440\text{ Hz}}\right)\\
         & = c_1+c_2\cdot \log_2\left(2^o\cdot3^q\cdot5^t\right) \\
               & = c_1+c_2 \cdot (o\cdot\log_2(2) + q\cdot \log_2(3) + t\cdot\log_2(5) ).
   .. \end{aligned}

Equivalently,

.. math::

   \begin{aligned}
     p(f)- c_1 = c_2 \cdot (o\cdot\log_2(2) + q\cdot \log_2(3) + t\cdot\log_2(5) )\end{aligned}

Accordingly, each frequency :math:`f` or equivalently each tone
:math:`t` can be conceived as a point
:math:`x = (p, s, r) \in \mathbb Q^3`. And vice versa, each point is
associated with its fundamental frequency
:math:`f(x) = f(p, s, r) = 440 \text{Hz} \cdot 2^p \cdot 3^s \cdot 5^r`.
In this representation,
:math:`p = o \cdot \log_2(2) + q\cdot \log_2(3) + t\cdot \log_2(5)` is a
linear combination from the basis vectors over
:math:`\mathbb Q^3 = \mathbb T^3` with coefficients :math:`o, q, t`, and
:math:`\mathbb T^3` is a module over the ring :math:`\mathbb Z` of
integers. Another way to state this is that octave, fifth and major
third are the basis vectors of tonal space.

Transformations of tonal spaces.
--------------------------------

For a fixed (arbitrary) reference tone (e.g. chamber tone A4=440Hz), and
for integers :math:`o, q, t \in \mathbb Z` we can represent all tones in
just intonation. The integer lattice
:math:`\mathbb Z^3 \subseteq \mathbb Q^3` corresponds to Euler’s
representation :raw-latex:`\citet{Euler1739}` and we will denote it with
:math:`\mathbb T^3`, the tonal space incorporating the three dimensions
of the octave :math:`o`, the pure fifth :math:`q` and the pure major
third :math:`t`.

Usually, descriptions of musical space do not consider octaves and
octave-related tones are subsumed into equivalence classes (chroma
classes or pitch classes); :math:`\pi\_O: \mathbb T^3 \to \mathbb T^2` ;
:math:`(o, q, t) \mapsto (q, t)`

Notes are abstract symbolic representations of tones. They can be
modeled as pairs :math:`n=(p, d)\in \mathbb T^3 \times \mathbb R` where
:math:`p` encodes *pitch* and :math:`d` *duration*. The pitch
dimension can be represented in one of the tonal pitch spaces (TPS).

Generalized Interval Systems
----------------------------

-  (GIS) maps a TPS representation to an appropriate mathematical space

-  A *Generalized Interval System* (GIS) is an ordered triple
   :math:`(S, (G, \circ), \text{int})`, where :math:`S` is a musical
   space, :math:`(G, \circ)` is a group, and :math:`\text{int}` is an
   interval function that maps :math:`S \times S \to G`. Common
   instances for :math:`G` are :math:`(\mathbb Z, +)` (suitable for the
   line of fifth) or :math:`(\mathbb{Z}_{12}, +)` (suitable for the
   circle of fifths).

-  …. many names: Pitch Space, Tonal Space, Tonal Pitch Space, Music
   Space, Musical Space….

These models of tonal space (line of fifths, circle of fifths, tonnetz,
torus) can serve as support for probability distributions. These in turn
describe the generative process for tonal pieces.

For the scope of this dissertation, the bag-of-notes model is assumed.
Meaning, that the grammar :math:`G` responsible for the sequential
arrangement of notes is factored out.

**Problem: "Theorizing in the wrong space" (Wiggins, 2012: Music, Mind,
and Mathematics)**

Pitch space encompasses the pitches and their mutual relations, the
intervals. Certain assumptions about pitches transform pitch space.

There are numerous theoretical models of pitch space.

| - Euler space
| - Tonnetz
| - Line of fifths
| - Circle of fifths
| - Spiral Array
| - MIDI

Models of pitch space
---------------------

Pitches can be expressed as :math:`2^x3^y5^z` for
:math:`x,y,z\in \mathbb Q`
:raw-latex:`\citep{LonguetHiggins1962a,LonguetHiggins1962b,Mazzola2018}`.
“Fundamental theorem of harmony”
:raw-latex:`\citep{LonguetHiggins1965}`. Pitches thus form a
3-dimensional space, also called the Euler space that incorporates just
intonation (pure integer ratios of frequencies). Distances between
pitches in this space are called intervals. Music theorists consider a
number of equivalence relations that transform the space. The most
common equivalence relation is octave equivalence that identifies all
pitches that are related by frequency ratios of 2, effectively
projecting the 3-dimensional Euler space to the plane given by
:math:`3^y5^z`. This plane is commonly called the Tonnetz and has
numerous historical precursors in the 19th century.

Since the Tonnetz expresses just intonation, one can distinguish, for
instance, between the just third E above C and the Pythagorean third E’
that lies four fifths. The difference between the just and the
Pythagorean third is called the syntonic comma,

.. math::

   \begin{aligned}
       4/5 : (2/3)^4 &= 4/5 : 16/81\\
                                   &= 4/5 \cdot 81/16\\
                                   &= 81/80 \\
                                   \approx 1.0125.\end{aligned}

Identifying just and Pythoagorean thirds wraps the Tonnetz to a
cylinder, also called the Spiral Array
:raw-latex:`\citep{Chew2000, Chew2014}`.

On this cylinder, the line of fifths wraps around in such a way that
every fourth fifth coincides with a third. This also means that all
points on this cylinder lie on this line of fifths. The pitches in this
space are sometimes called tonal pitch classes
:raw-latex:`\citep[TPCs][]{Temperley2000,Temperley2001}`. The line of
fifths is sufficient to capture all TPCs but the 2-dimensional surface
of the cylinder emphasizes triadic relations. Moreover, a segment of six
fifths contains all notes of a major or a (natural) minor scale and
hence all pitches and intervals in a key. The triads within a key form
Moebius strip :raw-latex:`\citep{Mazzola1985,Noll2016}`. Closing this
segment to a circle involves only diatonic fifths, but one of them is
diminshed (B–F in C major). This pitch set can be mapped to
:math:`\mathbb Z_7`.

[FIGURE: Diatonic chord sequence C-a-F-d-bo-G-e-C]

[FIGURE: Moebius strip embedded in :math:`\mathbb Z_7`]

Finally, another importent equivalence relation is that of enharmonic
equivalence. Enharmonic equivalence identifies octaves and augmented
sevenths,

.. math::

   \begin{aligned}
       (1/2)^7 : (2/3)^12 \approx 1.0136.\end{aligned}

This equivalence relations transforms the cylindrical pitch space to a
torus, and the line wrapped around the cylinder to a circle, the circle
of fifths. The tonal pitch classes are transformed into neutral pitch
classes, or simply pitch classes.

The pitch classes on the circle of fifths can be reorderd to the
chromatic circle by

.. math:: p\mapsto 7p\mod 12,

resulting in the order on which the keys within one octave occur in the
piano. Both the chromatic circle and the circle of fifths can be
identified with :math:`\mathbb Z_{12}`.

Especiall, review :raw-latex:`\citep[115-136]{Temperley2001}`, line of
fifths, center of gravity and describe it in the language of
distributions.

| - distinction tonal/spelled vs. (neutral) pcs
| - explain mapping to :math:`\mathbb Z_{12}`
| - sharp tpcs are mapped to positive numbers, flat tpcs to negative
  numbers
| - already by this definition, the white-note diatonic is more sharp
  than flat (and not balanced!)

The bag-of-notes model
~~~~~~~~~~~~~~~~~~~~~~

The bag-of-notes model conceives pieces simply counts the occurrences of
notes without taking into account the order in which they appear in the
piece.

It is in this sense a much more general model than the theoretically
motivated ones that we have seen in the previous section. This model
does not make any specific assumptions about the relations between notes
other than that their respective frequency is relevant.

In the terminology of probability theory, relative note frequencies
derived from note counts under the bag-of-words model correspond to
multinomial distributions.

Take for example the first movement of Alkan’s *Concerto for Solo
Piano*, op. 39, No. 8, in G\ :math:`\sharp` minor. Figure
[fig:Alkan\_39-8\_freqs] shows the note counts, weighted by duration
(CHECK) and ranked by frequency.

.. figure:: ../img/macro/Alkan_39-8_freqs.png
   :alt: TPC counts for Alkan’s *Concerto for Solo Piano*, op. 39, No.
   8, mov. 1.

   TPC counts for Alkan’s *Concerto for Solo Piano*, op. 39, No. 8, mov.
   1.

One can see an almost linear relation between frequency and rank.

Only towards the end of the movement the key signature changes from five
sharps (G sharp minor) to four flats Ab major but even in the sharp
parts of the movement the notated score changes to flats where
convenient.

Since musical pieces can have very different lengths–some pieces last
only a few minutes while others may last more than an hour–it is useful
to normalize the note counts and to derive the relative frequencies.

Interpret as distributions, show pitchplots... compare to Figure
[fig:tonal\_spaces].

These and many more conceivable transformations of tonal space do not
serve the goal of merely reflecting abstract algebraic or geometric
relations. It is important to emphasize that these transformations
reflect rather practical assumptions for performance and instrument
construction (such as dealing with the syntonic comma for keyboard
instuments) or compositional decisions (such as enharmonic equivalence).

Dataset
-------

| MusicXML files from diverse sources... - musescore.com
| - ELVIS
| - Humdrum
| - DCML transcriptions
| - CPDL
| - other websites...

.. figure:: ../img/macro/piece_dist.png
   :alt: Chronological distribution of pieces in the dataset.

   Chronological distribution of pieces in the dataset.

In this chapter we look at the historical development of tonality.
Although the dataset contains ca. 2000 pieces, there are unfortunately
huge gaps in the timeline as can be seen in Figure [fig:piece\_dist].
Attributing one year to a piece is not easy, in particular for older
pieces. If available, we use the year of composition, otherwise the year
of publication. Where both dates were unavailable, the middle year of
the composer’s life was chosen to represent the piece. Following this
procedure leads to only 157 years for which we have pieces in the whole
range of 582 years from 1361 to 1942.

If the hypothesis is true that tonality is constituted by the pitch
usage in pieces and that certain compositional assumptions transform
pitch space, then it should be possible to discover aspects of these
assumptions and the structure of pitch space by analyzing the usage of
pitches in musical compositions.

Moreover, comparing different sets of pieces, e.g. from different time
periods or composers, should reveal historical and stylistic
differences.

Tonal pitch-class distributions
===============================

The tonal pitch-class distribution of a musical piece is the relative
frequency of each tonal pitch class in that piece. Each piece can thus
be represented as a :math:`V`-dimensional vector, where :math:`V` is the
number of different pitch classes in the corpus, and that sums to one.
In this view, pieces are points in a :math:`V`-dimensional vector space.

In this space, pieces that have similar tonal pitch-class distributions
will be close together whereas pieces with very different tonal
pitch-class distributions will be more distant.

If all pieces are transposed to the same root, clusters in this space
correspond to different types of distributions that can be interpreted
as modes (take root out). This fact has been used in
:raw-latex:`\citep{Harasim2019}` and also shown that there are
historical developments.

If one does not transpose pieces, pieces that have similar root and mode
(and, accordingly, similar distributions) should cluster together. Since
:math:`V` is usually quite large, it is difficult to visualize these
clusters. One can use methods for dimensionality reduction to represent
the data in lower-dimensional spaces (2D or 3D) in order to visualize
them while at the same time maintaining characteristic properties of the
original space.

One of the most popular and classic methods is **principal component
analysis** :raw-latex:`\citep{Bishop2006}`, that can be used to project
the data onto a two-dimensional plane while keeping as much of the
variance in the data as possible. A more recent method for
dimensionality is called **:math:`t`-distributed stochastic neighbor
embedding** :raw-latex:`\citep[$t$-SNE;][]{VanDerMaaten2008}`. PCA is
better to get a global understanding of the structure of the space and
:math:`t`-SNE is better in illustrating local relationships. Figure
[fig:tsne\_pca] shows the data reduced to the Euclidean plane by both
methods.

.. figure:: img/macro/dim_reduct.png
   :alt: Dimensionality reduction of piece space via :math:`t`-SNE (top)
   and PCA (bottom).

   Dimensionality reduction of piece space via :math:`t`-SNE (top) and
   PCA (bottom).

The reduction using :math:`t`-SNE (top panel) shows that there are many
clusters that are relatively homogenuous with respect to their coloring.
The PCA reduction on the bottom panel of Figure [fig:tsne\_pca] also
shows that pieces with similar coloring are close together but
additionally shows that the colors are ordered along the line of fifths.
This means that pieces in keys that are close on the line of fifths have
similar tonal pitch-class distributions. Another advantage of PCA is
that the axes, called the principal components, have clear
interpretations. They reflect how much the data varies in this
direction. Applying this interpretation to the right panel of Figure
[fig:tsne\_pca], one can see that the first principal component (“PC1”)
roughly represents the “distance to C” or “diatonic” pieces (white or
very light colors) of more chromatic ones (darker shades). This
distinction accounts for 55 percent of the variance in the data. The
second principal component (“PC2”) distinguishes sharp from flat keys
(red vs. blue coloring) which is responsible for 21 percent of the data
variance.

These two principal components together account for 76 percent of the
variance in the data but simplify the space from :math:`V=35` dimensions
to just two which seems like a good tradeoff.

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
theoretical reasoning :raw-latex:`\citep{Temperley2000,Gardonyi2002}`,
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

.. figure:: ../img/macro/tpcs_smooth(50).png
   :alt: The evolution of tonal pitch classes taking into account a
   50-year window.

   The evolution of tonal pitch classes taking into account a 50-year
   window.

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

Tonal pitch-class coevolution
=============================

Modeling tonal pitch-class coevolution
--------------------------------------

The change/evolution of each pitch class :math:`k=i-a` is given by the
changes in
:math:`\mathbf{X}_i=(X^{1}_i,\dots,X^{t}_i,\dots,X^{T}_i)^\top\in \mathbb{R}^{T}`.
The pitch-class coevolution matrix is given by

.. math:: \mathbf\Sigma=\left(\mathrm{corr}(\mathbf{X}_i, \mathbf{X}_j)\right)_{ij}\in[-1,1]^{n\times n}

 and reflects the similarity of the diachronic change of pitch-classes.

These upper subplot in Figure [fig:evolution\_tpcs] have shown the
changes in the usage of each pitch-class over time. The coloring and
ordering suggests indeed a coevolution but recall that the ordering was
put in manually. The question is whether we can learn something about
the structure from the data by analyzing the coevolution of the tpcs
which is operationalized as the pairwise correlation (the Pearson
correlation coefficient :math:`\rho`) (maybe use sample coefficient
:math:`r`?) of two pc-evolution vectors :math:`p` and :math:`q`:

.. math::

   \begin{aligned}
   \rho_{p,q} = \frac{\mathrm{cov}(p,q)}{\sigma_p\sigma_q},\end{aligned}

 where :math:`\mathrm{cov}(p,q)` is the covariance and :math:`\sigma`
the standard deviation. Figure [fig:coevolution\_tpcs] shows the
pairwise tonal pitch class coevolution values across the entire
timeline.

.. figure:: ../img/macro/tpc_correlations_allpieces.png
   :alt: The coevolution of tonal pitch classes.

   The coevolution of tonal pitch classes.

Interesting observations:

#. Three regimes are clearly separated: flats (upper left), diatonics
   (center), and sharps (lower right)

#. The chromatic regimes are of roughly the same size, (only visible in
   overall plot; the sharps are slightly larger), i.e. the heatmap has
   two orthogonal symmetry axes

#. Moreover, the chromatic notes (flats and sharps) are weakly
   positively correlated

#. F\ :math:`\flat\flat` (and more extreme flats) does not occur in the
   entire corpus

#. The weakest correlations are highly interesting as well: The weakest
   correlation is with the chromatic lower neighbor and the tritone
   (e.g. A vs. A\ :math:`\flat`, E\ :math:`\flat`; E vs
   E\ :math:`\flat`, B\ :math:`\flat`; B vs. B\ :math:`\flat`, F;
   F\ :math:`\sharp` vs. F, C) This is only true for “central” tpcs
   (white keys diatonic)

We can use this correlation matrix to plot distances between the pitch
classes. Restricting the relations to the center of the plot, the
diatonic notes plus F\ :math:`\sharp` and B\ :math:`\flat` these
distances actually approximate the line of fifths!

Deciphering pitch-class coevolution
-----------------------------------

The last section presented how strong the evolution of pitch classes
correlates with each other. The heatmap in Figure
[fig:coevolution\_tpcs] indicated an interesting connection to the
ordering of tpcs on the line of fifths. But this ordering was achieved
manually, based on theoretical knowledge. How strong is this connection
based on the available data?

One way to investigate this is to reduce the high-dimensional space to a
smaller one. A common method to achieve this is **principal component
analysis** (PCA). PCA analyzes the variance in the data and projects the
data to a lower-dimensional space while maximizing the retained
variance.

Subsequently, one can inspect the individual principal components
individually and interpret the variance within and between them.

.. figure:: ../img/macro/tpcs_coevolution_principal_components.png
   :alt: Separate plots of the first four principal components jointly
   accounting for 94% of the variance in the data.

   Separate plots of the first four principal components jointly
   accounting for 94% of the variance in the data.

The results are very interesting:

#. Roughly, 64% of the variance is explained with the diatonic-chromatic
   distinction (PC1)

#. About 22% is explained by the sharp-flat distinction (PC2). Note also
   that C is on the zero-line for PC2 (does this really mean
   something?).

#. Another 6% of variance is explained by the third principal component.
   It roughly corresponds to the numbers of accidentals and follows,
   approximately, a zig-zag pattern for the 5 regions
   :math:`\flat\flat`, :math:`\flat`, ”, :math:`\sharp`, and
   :math:`\sharp\harp`.

#. PC4 is not easy to interpret, but it still captures a difference
   between, flat, diatonic, and sharp tpcs. Indeed, it seems that this
   component captures enharmonic equivalence! The tpcs C, G, D, A, was
   well as their enharmonic sharp and flat equivalents are all separated
   from the other notes. The same goes for F and E# (but not Gbb).

It seems that the PCA reduction was not only able to capture meaningful
dimensions, but also a meaningful relation between them, namely the
hierarchical one depicted in Figure [fig:pca\_hierarchy].

The variance explained by each of the components can be interpreted as
the weight or importance of these dimensions for the data. The two most
important principal components are PC1 and PC2, together contributing
approximately 86% of variance to the data. Figure [fig:PCA\_2dim] shows
how these two dimensions interact. Largely speaking, diatonic and
chromatic tpcs can be separated by a vertical line (not exactly),
whereas sharpward and flatward tpcs can be separated by a horizontal
line, with C, the only tpc that is neither flatwards nor sharpwards,
being exactly on the axis. Moreover, the three respectively most extreme
tpcs, Fbb–Gbb and Ax–Bx, are located close to the origin of the PCA
transformed plot. This means that they do not contribute much to the
variance in the data. These are also precisely the ones outside of the
enharmonic equivalence shown in PC4.

.. figure:: ../img/macro/tpc_coevolution_pca2.png
   :alt: Two-dimensional PCA reduction of tpc coevolutions.

   Two-dimensional PCA reduction of tpc coevolutions.

TPC coevolution per historical period
-------------------------------------

This “global view” can be broken down to compare how the tpc
correlations change over time. The next figure shows the correlations
for 50-year periods

.. figure:: ../img/macro/tpc_correlations_periods.png
   :alt: The coevolution of tonal pitch classes in different historical
   periods.

   The coevolution of tonal pitch classes in different historical
   periods.

#. 1500-1550: Two clusters emerge

#. 1550-1600: Clear separation between recta and ficta.

#. 1600-1650: Dahlhaus situates the origin of harmonic tonality in the
   early 17th century (Untersuchungen, p. 14), namely (following Fétis)
   in Monteverdi’s Cruda Amarilli SV 94, mm. 9-19, 24-30. Without
   diminishing Monteverdi’s influence we can see here that the first
   half of the 17 century was indeed a time of change, at least with
   respect to the conjunct usage of tones. But note also that the most
   prominent composer in that epoch in the dataset is Gesualdo who is
   well-known for his unusual harmonies.

#. 1650-1700: Confusion

#. 1650-1800 The separation between flat, diatonic, and sharp tpcs
   stabilizes. This is the closest to the overall picture above
   (although not as centered). The closest distribution to the overall
   distribution (check!) is the one in the late 18th century. It
   coincides with the common-practice period. Since we see that tpc
   behavior is different before and after, the CPT should not be taken
   as a synonym to tonal music. This affects large portions of empirical
   research of tonality presupposing two modes with clear and stable
   patterns. Review also Harasim et al. (2019)

#. 1800-1900: Strong correlation between all accidentals vanishes. The
   diagonal line is very clear. In this time, all pitch classes exhibit
   the greatest independence historically speaking.

#. 1900-...: Looks like a mix of CPT and Extended

Dahlhaus situates the origin of harmonic tonality in the early 17th
century (Untersuchungen, p. 14), namely (following Fétis) in
Monteverdi’s \*Cruda Amarilli\* SV 94, mm. 9-19, 24-30. Without
diminishing Monteverdi’s influence we can see here that the first half
of the 17 century was indeed a time of change, at least with respect to
the conjunct usage of tones. But note also that the most prominent
composer in that epoch in the dataset is Gesualdo who is well-known for
his unusual harmonies.

Turn argument around: Use inter-pc correlations to show importance of
fifth structure! What about thirds?

Diatonicism – Chromaticism – Enharmonicism
==========================================

“When we think about harmony, we automatically think about chords. In
fact, we are so fixated on chords that we sometimes forget they tell
only part of the story” :raw-latex:`\citep[154]{Tymoczko2011}`

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

Based on :raw-latex:`\citep{Gardonyi2002}`: (see MGG “Diatonik –
Chromatik – Enharmonik”)

- same diatonic region on LoF: relative keys/scales - although
theoretically, LoF is equivalent to :math:`\mathbb{Z}`, composers use
only a relatively small subset of it

- individual intervals can be associated with a regime on the
fifth-width space: m2 (5Q) is diatonic, wheras A1 (7Q) is chromatic, and
A7\ :math:`\approx`\ P8 (12Q).e

-  compare with “pitch class circulation”
   :raw-latex:`\citep[158ff.]{Tymoczko2011}`

-  fifth width measures Diatonicism -> Chromaticism -> Enharmonicism
   :raw-latex:`\citep[243]{Gardonyi2002}`

|image|

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

.. figure:: img/macro/local_fifth_width.png
   :alt: Averages (mean, mode, and median) of per-measure fifth widths
   over time.

   Averages (mean, mode, and median) of per-measure fifth widths over
   time.

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

-  given the optimal number of clusters from the mixture model, apply
   key-scape algorithm. It should give rise to a much clearer
   segmentation with :math:`K<<24` components.

-  Again, use Information Theory to determine best segmentation. (lowest
   entropy, per segment?, KL divergence with component distributions?)

-  How can these differences be measured? (not always binary)

-  Horizontally: Streams (*Auditory Scene Analysis*;
   :raw-latex:`\citep{Bregman1990,Huron2016}` Huron, 2016)

-  Vertically: Building blocks / units –> Gestalt laws, Segmentation
   :raw-latex:`\citep{Hanninen2012}`

Laws can govern *primary parameters* which allow for syntactic relations
between discrete units (such as pitch, or rhythm), and *secondary
parameters* which discribe continous dimensions such as timbre,
dynamics, etc.

Tonal Centers
-------------

Number of Tonal Centers
~~~~~~~~~~~~~~~~~~~~~~~

Distance of Tonal Centers
~~~~~~~~~~~~~~~~~~~~~~~~~

Divergence on the Tonnetz
~~~~~~~~~~~~~~~~~~~~~~~~~

Diachronic and Synchronic Tonal Styles
======================================

Clustering
----------

Principal Component Analysis
----------------------------

Analysis of Styles
------------------

Topic Modeling with Latent Dirichlet Allocation (LDA)
=====================================================

**Topic Models: What are corpora, documents, topics? “Distributional
hypothesis” (Harris, 1954; Firth, 1957).**

In general, topic models describe the generative process of how
documents (viewed as bags of words) have been created. A document is
defined as a distribution over topics and a topic is defined as a
distribution over words. To generate a new document, one first chooses a
distribution over topics, and for each word in the document choose a
topic from this distribution. The word is then sampled from the
distribution over words of this topic.

    A generative model for documents is based on simple probabilistic
    sampling rules that describe how words in documents might be
    generated on the basis of latent (random) variables. When fitting a
    generative model, the goal is to find the best set of latent
    variables that can explain the observed data (i.e., observed words
    in documents), assuming that the model actually generated the data.
    (Steyvers & Griffiths, 2007)

    | In `probability
      theory <https://en.wikipedia.org/wiki/Probability_theory>`__, the
      multinomial distribution is a generalization of the `binomial
      distribution <https://en.wikipedia.org/wiki/Binomial_distribution>`__.
      For example, it models the probability of counts for rolling a
      :math:`k`-sided `die <https://en.wikipedia.org/wiki/Dice>`__
      :math:`n` times. […] When :math:`k` is 2 and :math:`n` is 1, the
      multinomial distribution is the `Bernoulli
      distribution <https://en.wikipedia.org/wiki/Bernoulli_distribution>`__.
      When :math:`k` is 2 and :math:`n` is more than 1, it is the
      `binomial
      distribution <https://en.wikipedia.org/wiki/Binomial_distribution>`__.
      When :math:`n` is 1, it is the `categorical
      distribution <https://en.wikipedia.org/wiki/Categorical_distribution>`__.
    | (`Wikipedia <https://en.wikipedia.org/wiki/Multinomial_distribution>`__)

Background
----------

| - LDA in general (short review of relevant papers), numerous
  extensions of the basic model
| - application to music, review model of :raw-latex:`\citet{Hu2009}`.

A **corpus** :math:`\mathcal C` is a set of :math:`M` pieces. For each
piece, the **distribution of topics** :math:`\theta` is drawn from a
Dirichlet distribution with fixed corpus parameter :math:`\alpha.`

A collection (multiset) of **notes**
:math:`\boldsymbol{u}_n = \{u_{n1},\ldots,u_{nL}\}` defines a
**segment**. The number of unique notes in a corpus is the **vocabulary
size** :math:`V`. Each segment :math:`{u}_n` (e.g. beat, slice, bar,
section, …) is assigned a unique **topic label** :math:`z` (key,
tonality, mode, …). A **piece**
:math:`\mathcal P = \{\boldsymbol{u}_1, \ldots, u_N\}` consists of
:math:`N` segments with associated topic labels. A piece can have at
most :math:`N` topics, if :math:`N\leq V`, otherwise at most :math:`V`
topics. **Topics** :math:`\beta` are defined as distributions over
notes. Since there are :math:`K​` topics and :math:`V` distinct notes,
:math:`\beta` can be represented as a :math:`V \times K​` matrix where
:math:`\beta_{ij}​` encodes the probability of note :math:`i` in topic
:math:`j`.

Definitions and Assumptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. A *note* :math:` u \in \mathbb Z_{12}`.

#. A *segment* :math:`\mathbf{u}_n = \{u_{n1}, \ldots{}, u_{nL}\}`. In a
   bag-of-notes (BoN) model, a segment can also be represented by a
   12-dimensional count vector :math:`x_n`, where :math:`x_n^j` counts
   the number of times note :math:`j` occurs.

#. A *piece* :math:`s` is a sequence of :math:`N` segments:
   :math:`s=\{\mathbf u_1, ..., \mathbf u_N \}`. Again, in a BoN model a
   piece can be represented as a sequence of count vectors
   :math:`X=(x_1, ..., x_N)`.

#. A *corpus* is a collection of :math:`M` pieces,
   :math:`\mathcal S = \{s_1, ..., s_M\}`.

#. Finally, a *topic* :math:`z` is a probability distribution over the
   12 pitch classes. In their model, a topic models the concept of key
   and each segment is assumed to have precisely one topic/key. Thus,
   the sequence of topics in a given piece is modeled as
   :math:`\mathbf z = (z_1, ..., z_N)`.

#. They fix the number of topics to :math:`K=24`, based on prior music
   theory knowledge.

.. figure:: ../img/macro/LDA_model.png
   :alt: Graphical model for Latent Dirichlet Allocation (LDA).

   Graphical model for Latent Dirichlet Allocation (LDA).

A generative model for a musical piece
--------------------------------------

Bag of notes model... multinomial distribution... no order/structure
among the classes (tpcs)

-  Formalization of LDA as a probabilistic graphical model (PGM)

-  PGMs are generative models. Toy example to generate pieces.

#. For each piece :math:`s_m`, :math:`m=1, ..., M`, draw a
   :math:`K`-dimensional topic weight vector :math:`\theta` from a
   Dirichlet distribution
   :math:`\left(\theta \sim \mathrm{Dir}(\alpha)\right)` to determine
   which keys are likely to occur:

   .. math::

      \begin{aligned}
          p(\theta \mid \alpha) = \frac{\Gamma\left(\sum_i \alpha_i\right)}{\prod_i \Gamma \left(\alpha_i\right)}\prod_i \theta^{\alpha_i - 1}.
          \end{aligned}

   The corpus-level parameter :math:`\alpha` determines which topics are
   likely to co-occur in pieces.

#. For each segment :math:`\mathbf u_n`, :math:`n=1, ...N`, in the
   piece, choose topic :math:`z_n \in \{1, ..., K\}` from the
   multinomial distribution :math:`p(z_n=k \mid \theta) = \theta_k`.

#. For each note :math:`u_{nl}` in :math:`\mathbb u_n`,
   :math:`l=1, ..., L`, choose a pitch-class from the multinomial
   distribution :math:`p(u_{nl} = i \mid z_n=k, \beta)=\beta_{ij}`,
   where :math:`\beta` is a :math:`V \times K` matrix encoding each
   topic as a distribution over :math:`V=12` pitch classes.

This generative process defines a joint probability distribution over
observed and latent random variables for each piece in the corpus:

.. math::

   \begin{aligned}
       p(\theta, \mathbf z, s \mid \alpha, \beta) = p(\theta \mid \alpha)\prod_{n=1}^N p(z_n \mid \theta) \prod_{l=1}^L p(u_{nl} \mid z_n, \beta).\end{aligned}

In this model, a piece is a bag-of-segments, and segments are
bags-of-notes.

Inference and Learning
~~~~~~~~~~~~~~~~~~~~~~

The model is fully specified by the corpus-level Dirichlet parameter
:math:`\alpha` and the key-profile matrix :math:`\beta`. Under the
assumption that they are known, key-profiles for segments or pieces can
be inferred by computing the posterior distribution

.. math::

   \begin{aligned}
       p(\theta, \mathbf z \mid \alpha, \beta, s) = \frac{p(\theta, \mathbf z, s \mid \alpha, \beta)}{p(s\mid \alpha, \beta)},\end{aligned}

 according to Bayes’ rule.

The denominator in the last equation is called the *marginal
distribution* or *likelihood* of a piece. The learning problem for the
present setting is to maximize the log-likelihood of all pieces in the
corpus ("Which combination of :math:`\alpha` and :math:`\beta` make it
most likely that these pieces were generated?”). Thus, we want to
maximize

.. math::

   \begin{aligned}
   \mathcal L(\alpha, \beta) = \int d\theta p(\theta \mid \alpha) \prod_{n=1}^N \sum_{z_n=1}^K p(z_n \mid \theta) \prod_{l=1}^L p(u_{nl}\mid z_k, \beta).\end{aligned}

The simplest learning algorithm for this task is the expectation
maximization (EM) algorithm. Since this is not tractable, it has to be
approximated. They use variational approximation. I use Gibbs sampling.
Gibbs sampling can be understood as a generalization of the EM
algorithm. Instead of maximizing at each of its two steps (E and M),
Gibbs sampling uses the conditional distributions and samples from them.

-  Learn model parameters from corpus given a number :math:`K` of topics
   via Gibbs sampling.

-  Train-test split not self-evident. Possibilities:

   -  Train on whole corpus

   -  Lern topics for different periods separately

Extension of the LDA music model
--------------------------------

Describe potential adaptions of the LDA model. In particular the
difference to the pitch class representation and the interpretation of
topics as tone fields, not keys

-  Model notes in :math:`\mathbb Z` instead of :math:`\mathbb Z_{12}`
   (line of fifths instead of circle of fifths).

-  Use different segmentations:

   -  Slices (onsets)

   -  Beats

   -  Bars

   -  Key-regions (as defined by accidentals)

   -  entire piece

-  Allow for more topics. Hypothesis: chromatic passages, hexatonic,
   octatonic, pentatonic, and variants of several keys will show up as
   topics.

-  Take note-order into account: Griffiths, Steyvers, Blei & Tenenbaum
   (2005), and Andrews & Vigliocco (2010)

-  Dynamic Topic Modeling - Changes of topics over time: Blei & Lafferty
   (2006)

Other Features / Random Variables

-  Length in notes

-  Pitch-class distribution in :math:`\mathbb Z` and in
   :math:`\mathbb Z_{12}`

-  Number of key changes

-  Chromaticism

-  Meter / Meter change

General Notes:

-  Interpretation: Because the musical vocabulary is quite small when
   notes are the equivalent of words, it is not sufficient to just look
   at the most frequent notes in a topic in order to interpret it but
   rather to inspect the whole distribution over notes.

-  Similarity between documents (pieces) and subcorpora –> Clustering

Topics inferred from the corpus
-------------------------------

Figure [fig:topic\_dists] shows the note distributions for the
:math:`K=7` inferred topics.

.. figure:: ../img/macro/topic_0_of_7.png
   :alt: The note distributions for the :math:`K=7` topics.
   :width: 90.0%

   The note distributions for the :math:`K=7` topics.

.. figure:: ../img/macro/topic_1_of_7.png
   :alt: The note distributions for the :math:`K=7` topics.
   :width: 90.0%

   The note distributions for the :math:`K=7` topics.

.. figure:: ../img/macro/topic_2_of_7.png
   :alt: The note distributions for the :math:`K=7` topics.
   :width: 90.0%

   The note distributions for the :math:`K=7` topics.

.. figure:: ../img/macro/topic_3_of_7.png
   :alt: The note distributions for the :math:`K=7` topics.
   :width: 90.0%

   The note distributions for the :math:`K=7` topics.

.. figure:: ../img/macro/topic_4_of_7.png
   :alt: The note distributions for the :math:`K=7` topics.
   :width: 90.0%

   The note distributions for the :math:`K=7` topics.

.. figure:: ../img/macro/topic_5_of_7.png
   :alt: The note distributions for the :math:`K=7` topics.
   :width: 90.0%

   The note distributions for the :math:`K=7` topics.

.. figure:: ../img/macro/topic_6_of_7.png
   :alt: The note distributions for the :math:`K=7` topics.
   :width: 90.0%

   The note distributions for the :math:`K=7` topics.

The relative weights of the topics in the overall corpus can be seen in
Figure [fig:topics\_weights]. The most common topic is topic 0
(“(transposed) diatonic”) and the least common is topic 4 (“far-flats”)

.. figure:: ../img/macro/topics_in_corpus.png
   :alt: The relative weight of :math:`K=7` topics in the corpus.

   The relative weight of :math:`K=7` topics in the corpus.

Besides calculating the overall importance of topics in the corpus, one
can also look at the relative topic weights within individual pieces.
Figure [fig:raw\_topics] shows this distribution. Analogous to the
pitch-class evolution from Figure [], pieces that are assigned to the
same year are accumulated (**Describe procedure!**).

.. figure:: ../img/macro/raw_topics.png
   :alt: Historical change of topic weights in pieces.

   Historical change of topic weights in pieces.

It is obvious how the lack of data in earlier periods affects the
pattern we see. Nonetheless, it can be seen, that earlier pieces rarely
contain the certain topics which only occur later.

Number of topics reveals hierarchy of tonality
----------------------------------------------

“Vertical”: Different values of :math:`K\in [2,12]` indicate
hierarchical nature of tonality.

#. Compare topic distributions for different values of :math:`K`

#. Relate topics from different :math:`K`-stages with each other: coarse
   to fine, correlations between some topics should increase

All matrices where based on documents. In the classical LDA setting, a
corpus is a bag of documents. We are in particular interested in
historical developments, so the chronological order is important.
Moreover, we do not a piece for each year and for some years we have
many pieces. The first step is to re-assign each piece its “display
year” (composition, publication, of composer half-life). Then we average
all pieces in the same year. We now have at most one topic distribution
per year in the corpus.

...

But there are still years for which we do not have data, in particular
in the earlier periods. Pragmatically, if we do not have a topic
distribution for a given year, we take the one from the previous year.
To that end, we create a time index ranging from the earliest to the
latest date in the corpus.

We then iterate over all years and use the inferred topic distributions
if there is one for that particular year. If not, we use the same as in
the year before.

Historical inferences for each value of :math:`K`
-------------------------------------------------

Sliding windows reveal trends
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Figure [fig:raw\_topics] takes a very fine-grained view on the evolution
of the topic distribution because each year is a single data point. In
order to see larger trends, we can zoom out and look at smoothed
versions of the same data. We inspect rolling averages with a window
size of 30, 50, and a hundred years to see generational, epochal and
secular trends.

.. figure:: ../img/macro/7_topics_smooth(30).png
   :alt: Historical trends for varying sliding window sizes.
   :width: 90.0%

   Historical trends for varying sliding window sizes.

.. figure:: ../img/macro/7_topics_smooth(50).png
   :alt: Historical trends for varying sliding window sizes.
   :width: 90.0%

   Historical trends for varying sliding window sizes.

.. figure:: ../img/macro/7_topics_smooth(100).png
   :alt: Historical trends for varying sliding window sizes.
   :width: 90.0%

   Historical trends for varying sliding window sizes.

In these figures we can observe a) the relative topic importances
(weights) over time, and b) identify breaking points and local extrema.

Moreover, the entropy of these distributions is informative!

Todo: PCA shows relation between topics and documents in (reduced)
note-space

Topic coevolution
-----------------

topic correlations motivate hierarchical clustering

.. figure:: ../img/macro/7_topics_coevolution.png
   :alt: The coevolution of tonal pitch classes in different historical
   periods (only for years with pieces).

   The coevolution of tonal pitch classes in different historical
   periods (only for years with pieces).

.. figure:: ../img/macro/7_topics_coevolution_all_years.png
   :alt: The coevolution of tonal pitch classes in different historical
   periods (for all years in the range).

   The coevolution of tonal pitch classes in different historical
   periods (for all years in the range).

.. figure:: ../img/macro/topic_clustering.png
   :alt: Topic clustering.

   Topic clustering.

Pitch class – topic coevolution
-------------------------------

.. figure:: ../img/macro/tpc_topic_coevolution.png
   :alt: Topic clustering.

   Topic clustering.

Overall Figure [fig:tpc\_topic\_coevolution] almost looks like a block
matrix.

Locally, the fifths order is preserved, especially the diatonic, as seen
by the row clusters! Regarding the topics, we see two major clusters.
The left most one is “chromatic notes” and the right one is “diatonic
plus”. The diatonic cluster contains the diatonic notes without F, which
get clustered with F but without B (note also that when B is included,
Bb is most negatively correlated, and, when F is included, F# is most
negatively correlated). The tritone is the condition to separate these
as well as the chromatic semitone. Then it gets extended by sharps up to
G# which makes sense because of the dominant of a minor. The last topic
to join this cluster extends it into the flat direction. We have already
noted that tonal music is generally sharpwards oriented so it makes
sense that the evolution of flat notes is weaker correlated with
diatonic notes than sharp ones.

The second cluster...

Beyond the bag-of-notes model: the Hidden Markov Topic Model (HMTM)
===================================================================

Improving the bag-of-notes model with a Hidden Markov Topic Model

.. figure:: ../img/macro/HMTM_model.png
   :alt: Graphical Model for the Hidden Markov Topic Model (HMTM).

   Graphical Model for the Hidden Markov Topic Model (HMTM).

Discussion
==========

–Result 1: Historically, ever larger portions of pitch space are
explored

There is a trend from diatonic > chromatic > enharmonic pieces, but it
is not monotonic. In the 19th century, there are diatonic Lieder
(composer) and Alkan, who has the greatest tonality range
(diatonic–enharmonic).

.. |image| image:: img/macro/fifth_widths.png
