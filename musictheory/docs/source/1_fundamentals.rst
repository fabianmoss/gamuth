Fundamentals
============

The theory presented in here can be described as a *tonal theory* in the sense 
that its most fundamental objects are *tones*, discrete musical entities that have
a certain location in tonal space. 
A tonal space is then a metrical space describing all possible tone locations,
and the metric is given by an *interval function* between the tones. Note that by this definition,
there are as many different tonal spaces as there are interval functions.

While many aspects and examples will be taken 
from Western (classical) music, the theory is in principle not restricted to this 
tradition but extends well to virtually all musical cultures where a tone is a meaningful concept.

Tones
-----

Let's start with a mental exercise: imagine a tone.
Contemplate for a while what this means.
Does this tone have a pitch? A duration? A velocity (volume)?

* Riemann (1916). *Ideen zu einer Lehre von den Tonvorstellungen*:

"The ultimate elements of the tonal imagination are single tones." (Wason & Martin, 1992, 92)

Euler Space / Tonnetz / Tonal Space
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pitch classes
-------------

A very common object in music theory is that of a *pitch class*. Pitch classes
are equivalence classes of tones that incorporate some kind of invariance.
The two most common equivalences are *octave equivalence* and *enharmonic equivalence*.

Octave equivalence
~~~~~~~~~~~~~~~~~~

Octave equivalance considers all tones to be equivalent that are separated by one or
multiple octaves, e.g C1, C2, C4, C10 etc. More precisely, all tones whose fundamental frequencies
are related by multiples of 2 are octave equivalent.

Enharmonic equivalence
~~~~~~~~~~~~~~~~~~~~~~

If one further assumes enharmonic equivalence, all tones separated by 12 fifths on the line of fifths
are considered to be equivalent, e.g. A# and Bb, F# and Gb, G#, and Ab etc.

The notion of a pitch class usually entails both octave and enharmonic equivalence.
Consequently, there are twelve pitch classes. If not mentioned otherwise, we adopt this convention here.
The twelve pitch classes are usually referred to by their most simple representatives, i.e.

.. math::
   \text{C, C$\sharp$, D, E$\flat$, F, F$\sharp$, G, A$\flat$, A, B$\flat$, B},

but it is more appropriate to use *integer notation* in which each pitch class is represented
by an integer :math:`k \in \mathbb{Z}_{12}`.

.. math::
   \mathbb{Z}_{12}=\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11\},

and usually one sets :math:`0\equiv \text{C}`. This allows to use *modular arithmetic*
do calculations with pitch classes.

Frequency / Temperament
~~~~~~~~~~~~~~~~~~~~~~~

Intervals
---------

- Pitch intervals
- Ordered pitch-class intervals (-> rather directed)
- Unordered pitch-class intervals
- Interval classes
- Interval-class content
- Interval-class vector

GISs
~~~~

Pitch-Class Sets
----------------

- Sets that contain pitch classes

Normal Form 
~~~~~~~~~~~

Transposition
~~~~~~~~~~~~~

Inversion
~~~~~~~~~

- Inversion In, Ixy

Index number 
~~~~~~~~~~~~

Set Class
~~~~~~~~~

Prime Form 
~~~~~~~~~~


Transformations between representations of tones are actually *transformations of tonal space*.

[Diagram of relations between different representations.]

Western tonal music
-------------------

- scales / scale degrees
   - diatonic
   - chromatic
   - hexatonic/octatonic
- modes
- keys

Time
----

Notes
~~~~~

(Tones + Duration)
blablabla...

.. Sinve the relations between tones only given by 
   their location in tonal space (and the interval function)
   generalizing the notion of neighbor notes etc. corresponds
   to changing what the *lines* in Western notation mean.
   Traditionally, two lines separate tones that are a generic third apart.
   But there have been other representations. 
   For instance, the first attempts of Guido separated notes by steps.
   Let's reinterpret the lines as seconds and fifths. 
   There have also been a number of attempts to develop a fully chromatic
   notation system (Parncutt).


Rhythm
~~~~~~

(Duration patterns)

Meter
~~~~~

(Hierarchy)

Musical time vs. performance time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Notes on Segmentation
---------------------

- Straus 2005
- Hanninen 2012