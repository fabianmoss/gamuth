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

Perhaps the most simple description of music is *sound organized in time* (attributed to 
Edgar Varèse, see also :cite:`Yust2018_OrganizedTimeRhythm`). 
Later we will see that this description falls short of encompassing many central aspects to music
but it provides a good starting point for our considerations. Taking this definition for granted
means that we can conceptualize music within a two-dimensional framework, where the axes 
represent sound and time, respectively (see :numref:`fig_soundtime`). Note that only the x-axis ("Time") 
is not represented as an arrow to indicate that in music (as in life) we can only move forward.

.. _fig_soundtime:

.. tikz:: Two-dimensional depiction of music: music as sound organized in time. 

   \draw[thick,->,>=stealth] (-0.3,0) -- (8,0) node[midway,below] {Time}; 
   \draw[thick] (0,-0.3) -- (0,3) node[midway,above,sloped] {Sound};

This is also the way music is usually displayed in *Digital Audio Workstations* (DAW) that feature
a master window where music blocks can be arranged along a fixed timeline. Producing music in 
these environments thus quite literally consists of stacking blocks on top of one another. 

Tones
-----

Let's start with a mental exercise: imagine a tone.
Contemplate for a while what this means.
Does this tone have a pitch? A duration? A velocity (volume)?

* Riemann (1916). *Ideen zu einer Lehre von den Tonvorstellungen*:

"The ultimate elements of the tonal imagination are single tones."
(:cite:t:`Wason1992_RiemannIdeenLehre`, p. 92).

Bearing that in mind, let's create (or *instantiate*) a tone. To do so, we need to 
conceptualize ("vorstellen" in Riemann's terminology) a *tone location* 
("Tonort", :cite:t:`Mazzola1990_GeometrieToneElemente`, p. 241).
There are many different ways to do this. In fact, the way we specify the location of a tone 
defines the tonal space in which it is situated. 
The figure below is an adaptation from :cite:t:`Lewin1987`.

.. tikz:: Two abstract tones :math:`s` and :math:`t`, and the interval :math:`i` between them.

   \node[circle,fill,inner sep=0pt,minimum size=5pt,label={below: $s$}] (s) at (0,0) [below] {};
   \node[circle,fill,inner sep=0pt,minimum size=5pt,label={below: $t$}] (t) at (4,1.5) {};
   \draw[thick,->,-stealth,shorten <=2pt, shorten >=2pt] (s) -- (t) node[midway,below,sloped] {$i$};

The fact that music operates with discrete pitches has also been argued to be crucial for its 
evolution :cite:p:`Tomlinson2018_MillionYearsMusic`.

Frequencies
~~~~~~~~~~~

Each tone corresponds to some *fundamental frequency* :math:`f` in Hertz (Hz),
oscillations per second.

- Overtone series
- frequency ratios 
- logarithm: multiplication => addition

Euler Space 
~~~~~~~~~~~

One option is to locate a tone `t` as a point :math:`p=(o, q, t)` in Euler Space, defined by
a number of octaves `o`, fifths `q`, and thirds `t`. We will use the :class:`gamuth.Tone`
class for this

.. code-block:: python

   from gamuth import Tone

   t = Tone(o=0, q=0, t=0)

From this representation we can derive a variety of others, corrsponding to transformations of 
tonal space.

Octave equivalence
~~~~~~~~~~~~~~~~~~

Octave equivalance considers all tones to be equivalent that are separated by one or
multiple octaves, e.g C1, C2, C4, C10 etc. More precisely, all tones whose fundamental frequencies
are related by multiples of 2 are octave equivalent.

Tonnetz
~~~~~~~

The *Tonnetz* does not contain octaves and thus corresponds to a projection 

.. math::
   
   \pi: (o, q, t) \mapsto (q, t).

Pitch classes
-------------

A very common object in music theory is that of a *pitch class*. Pitch classes
are equivalence classes of tones that incorporate some kind of invariance.
The two most common equivalences are *octave equivalence* and *enharmonic equivalence*.


Enharmonic equivalence
~~~~~~~~~~~~~~~~~~~~~~

If, in addition to octave equivalence, one further assumes enharmonic equivalence, 
all tones separated by 12 fifths on the line of fifths
are considered to be equivalent, e.g. :math:`\text{A}\sharp` and :math:`\text{B}\flat`, 
:math:`\text{F}\sharp` and :math:`\text{G}\flat`, :math:`\text{G}\sharp`, and :math:`\text{A}\flat` etc.

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
do calculations with pitch classes. In standard music notation, this would be rendered as 

.. lilyinclude:: ./lilypond/chromatic.ly
   :nofooter:
   :noedge:
   :audio:

Other invariances
~~~~~~~~~~~~~~~~~

OPTIC

Tuning / Temperament
~~~~~~~~~~~~~~~~~~~~~~~

.. _Intervals:

Intervals
---------

- Pitch intervals
- Ordered pitch-class intervals (-> rather directed)
- Unordered pitch-class intervals
- Interval classes
- Interval-class content
- Interval-class vector

.. _sec_gis:

GISs
~~~~

Transformations between representations of tones are actually *transformations of tonal space*.

[Diagram of relations between different representations.]