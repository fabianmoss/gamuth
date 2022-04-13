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
:cite:p:`Mazzola1990_GeometrieToneElemente,Mazzola2018_EulerSpace,Longuet-Higgins1987_ThreeDimensionsHarmony`.

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

For a fixed (arbitrary) reference tone (e.g. chamber tone A4=440Hz), and
for integers :math:`o, q, t \in \mathbb Z` we can represent all tones in
just intonation. The integer lattice
:math:`\mathbb Z^3 \subseteq \mathbb Q^3` corresponds to Euler's
representation :cite:p:`Euler1739_TentamenNovaeTheoriae` and we will denote it with
:math:`\mathbb T^3`, the tonal space incorporating the three dimensions
of the octave :math:`o`, the pure fifth :math:`q` and the pure major
third :math:`t`.

Usually, descriptions of musical space do not consider octaves and
octave-related tones are subsumed into equivalence classes (chroma
classes or pitch classes); :math:`\pi_O: \mathbb T^3 \to \mathbb T^2` ;
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

.. important::

   Problem: "Theorizing in the wrong space" :cite:p:`Wiggins2012_MusicMindMathematics`

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
:math:`x,y,z\in \mathbb Q` “Fundamental theorem of harmony”
:cite:`Longuet-Higgins1987_ThreeDimensionsHarmony,Longuet-Higgins1987_TwoLettersMusical,Mazzola1990_GeometrieToneElemente`.
Pitches thus form a
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
cylinder, also called the *Spiral Array* 
:cite:p:`Chew2000_MathematicalModelTonality,Chew2014_MathematicalComputationalModeling`

[Tikz Picture of Spiral Array]

On this cylinder, the line of fifths wraps around in such a way that
every fourth fifth coincides with a third. This also means that all
points on this cylinder lie on this line of fifths. The pitches in this
space are sometimes called tonal pitch classes 
:cite:p:`Temperley2000_LineFifths,Temperley2001_CognitionBasicMusical,Mossaccepted_LineFifthsCoevolution`. 
The line of
fifths is sufficient to capture all TPCs but the 2-dimensional surface
of the cylinder emphasizes triadic relations. Moreover, a segment of six
fifths contains all notes of a major or a (natural) minor scale and
hence all pitches and intervals in a key. The triads within a key form
Moebius strip :cite:p:`Mazzola1990_GeometrieToneElemente,Noll2016_VernunftTraditionNeue`.
Closing this segment to a circle involves only diatonic fifths, but one of them is
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

Especiall, review line of
fifths, center of gravity and describe it in the language of
distributions. Discuss also, why D is the center and not C!

* distinction tonal/spelled vs. (neutral) pcs
* explain mapping to :math:`\mathbb Z_{12}`
* sharp tpcs are mapped to positive numbers, flat tpcs to negative numbers
* already by this definition, the white-note diatonic is more sharp than flat (and not balanced!)

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

.. .. figure:: ../img/macro/Alkan_39-8_freqs.png
..    :alt: TPC counts for Alkan’s *Concerto for Solo Piano*, op. 39, No.
..    8, mov. 1.

..    TPC counts for Alkan’s *Concerto for Solo Piano*, op. 39, No. 8, mov.
..    1.

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

.. .. figure:: ../img/macro/piece_dist.png
..    :alt: Chronological distribution of pieces in the dataset.

..    Chronological distribution of pieces in the dataset.

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
