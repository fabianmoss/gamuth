Fourier Pitch Space 
===================

.. note::
    The following is taken from the Wavescapes paper!

We first introduce the segmentation of a musical piece into a hierarchy of pitch-class vectors. 
Then, we describe the Discrete Fourier Transform (DFT) and its application to this hierarchy, 
and a color mapping of the obtained Fourier coefficients. 
This procedure results in a visual representation that we call *wavescapes*.

A hierarchy of pitch-class vectors 
----------------------------------

A *segmentation* of a musical piece is a partition into :math:`N` non-overlapping segments of equal length :math:`r`.
In this general sense, segments can be defined by musical units in symbolic scores (e.g., measures, note durations) 
as well as by continuous durations in audio recordings (e.g., seconds, onsets).
We represent the :math:`q`-th segment by a *pitch-class vector* (PCV) :math:`x_q\in \mathbb{R}^{12}_{\geq 0}, 1 \leq q \leq N`, 
whose entries contain the total durations (also called weights) of the twelve pitch classes in this segment. 
A pitch class is the equivalence class of all octave-related pitches in twelve-tone equal temperament, assuming enharmonic equivalence. 
The value :math:`x_q[0]` is the weight of pitch class C, :math:`x_q[1]` is the weight of C#, and so forth.
For example, the PCV of the first four measures of J.~S. Bach's Prelude in C~major is 
:math:`x=(14,  0,  9,  0,  9,  2,  0,  3,  0,  1,  0,  4)`, where the duration of each pitch class is given in quarter notes.

A complete piece is modeled as a *hierarchy of segments* given by a function :math:`P` that inclusively returns the pitch-class content 
from the :math:`n`-th to the :math:`m`-th segment, 

.. math::
    P \colon \mathbb{N}^{2} &\longrightarrow \mathbb{R}_{\geq 0}^{12} \\
    (n,m) &\longmapsto x = \sum_{q=n}^m x_q, \nonumber
    \text{for } 1 \leq n \leq m \leq N.

The size as well as the hierarchical level of any segment with pitch-class content :math:`P[n,m]` is then :math:`m-n+1`, 
and there are :math:`\sum_{n=1}^N n = \binom{n+1}{2}` segments in total. 

.. This hierarchy is schematically shown in Figure~\ref{tab:visuhierarchy}, where all cells (except those at the very bottom) are represented as diamonds.

Discrete Fourier Transform
--------------------------

The *Discrete Fourier Transform* (DFT) decomposes a vector into a sum of sinusoidal waves of unique frequencies with varying amplitudes and phases. 
Mathematically, the DFT of any PCV :math:`x` is given by

.. math::
        
    F \colon \mathbb{R}^{12}_{\geq 0} &\longrightarrow \mathbb{C}^{12} \\
                        x &\longmapsto X, \nonumber

where the :math:`k`-th component of the complex-valued vector :math:`X` is defined as

.. math::

    X[k]= \sum\limits_{n=0}^{11}x[n]e^{-i2\pi n \frac{k}{12}},\;
    % \forall 
    k \in [0,\mathrel{{.}\,{.}\,{.}}\;, 11]. \label{eqn:dft}

The values of :math:`X[k]` are referred to as *Fourier coefficients*, or simply *coefficients*. 
The zeroeth coefficient :math:`X[0]` is always equal to the sum of :math:`x`. 
By symmetry, the coefficients for :math:`k\in [1,\ldots,5]` are conjugate to 
the ones for :math:`k \in [11,\ldots,7]` while the sixth coefficient is its own conjugate, 

.. math:: 
    X[k] = \bar{X}[12-k] \text{for } k \in [1,\ldots,11].

For this reason, we consider only coefficients 1 through 6 in accordance with previous research \citep{amiot_david_2007,yust_generalized_2019}.

Since the Fourier coefficients are complex numbers, they have a representation in Cartesian coordinates through their real and imaginary parts, 

.. math:: 
    X[k] = \operatorname{Re}(X[k])+i\cdot \operatorname{Im}(X[k]), 

and a representation in polar coordinates in terms of their *magnitude* :math:`\mu_k` and *phase* :math:`\phi_k`,

.. math:: 
    X[k] &= \mu_k \cdot e^{i\phi_k} \nonumber\\
    &= \mu_k \cdot (\operatorname{cos}(\phi_k) + i \cdot \operatorname{sin}(\phi_k)).

The phase is defined as

.. math::

    \phi_k  &= \measuredangle(X[k]) \\
            &= \operatorname{tan}^{-1}\left(\frac{\operatorname{Im}(X[k])}{\operatorname{Re}(X[k])}\right)\nonumber

and the magnitude is defined as

.. math::
    \mu_k=|X[k]| = \sqrt{\operatorname{Re}(X[k])^2+\operatorname{Im}(X[k])^2},

where :math:`\measuredangle` is the angle function :math:`\measuredangle: \mathbb{C} \to [0, 2\pi[`.

Consider again the PCV :math:`x = (14,  0,  9,  0,  9,  2,  0,  3,  0,  1,  0,  4)`. 
The fifth Fourier coefficient of :math:`x` has the Cartesian representation :math:`X[5] = (14.87 + i \cdot 19.09)`, 
phase :math:`\phi_5=0.91`, and magnitude :math:`\mu_5=24.19`. 

.. Figure~\ref{fig:magnphase} visualizes its Cartesian and polar representations.

Color mapping of Fourier coefficients
-------------------------------------

To visualize the Fourier coefficients of PCVs, we represent them in polar coordinates and map their phases and magnitudes to a color.
Given the periodic nature of the phase, it can be associated to a color through a *circular hue*.
Here, we choose the hue function :math:`h: [0, 2\pi[ \longrightarrow [0,1]^3` that maps :math:`\phi_k` to a triple :math:`(r,g,b)`, 
representing the strengths of the red, green, and blue components of the color \citep{ong_generalization_2014}:

.. math:: 
    h(\phi_k) = \begin{cases}
        (1, \frac{3\phi_k}{\pi} , 0) & \text{if}\; 0 \leq \phi_k < \frac{\pi}{3}\\
        (2 - \frac{3\phi_k}{\pi}, 1, 0) & \text{if}\; \frac{\pi}{3} \leq \phi_k < \frac{2\pi}{3}\\
        (0, 1, \frac{3\theta}{\pi} - 2) & \text{if}\; \frac{2\pi}{3} \leq \phi_k < \pi\\
        (0, 4 - \frac{3\phi_k}{\pi} , 1) & \text{if}\; \pi \leq \phi_k < \frac{4\pi}{3}\\
        (\frac{3\phi_k}{\pi} - 4, 0 , 1) & \text{if}\; \frac{4\pi}{3} \leq \phi_k < \frac{5\pi}{3}\\
        (1, 0 , 6 - \frac{3\phi_k}{\pi}) & \text{if}\; \frac{5\pi}{3} \leq \phi_k < 2\pi\\
        \end{cases}

The magnitude :math:`\mu_k` of a Fourier coefficient can be mapped to an opacity value 
:math:`\alpha = \mu_k/X[0]` by normalizing it with the sum of PCV :math:`x`, given by its zeroeth coefficient :math:`X[0]`.

\citet{amiot_entropy_2020} uses the normalization 

.. math:: 
    \alpha_k = \frac{|X[k]|^2}{\sum_{j=1}^{11}|X[j]|^2}, \text{ for } k=1,\ldots,11.

(A saturation mapping is also possible, but is overall inferior in visual quality compared to the opacity mapping.) 
The normalization of the magnitude also facilitates the comparison of different PCVs with one another.

We represent the phase and magnitude mappings by a coloring function :math:`C_k`,

.. math::
    
    C_k:\mathbb{C}^{12} &\longrightarrow [0,1]^3 \times [0,1]\\
        X &\longmapsto ((r, g, b), \alpha),\nonumber

which selects the :math:`k`-th coefficient of :math:`X` and uses the previous mappings on its phase and magnitude to return a color,

.. math:: 
    C_k(X) &= \left (h(\measuredangle(X[k])), \frac{|X[k]|}{X[0]} \right)\\ 
        &=  \left (h(\phi_k), \frac{\mu_k}{X[0]} \right)\nonumber.

Wavescapes 
----------

To summarize, we showed how to generate a color given a pitch-class vector by successively applying the mappings :math:`F` and :math:`C_k`. 
Together with :math:`P`, the mappings define an arrangement of colors for a given piece of music that we call a *wavescape*. 
More precisely, the wavescape for the :math:`k`-th Fourier coefficient is given by 

.. math::
    W_k: \mathbb{N}^2 &\longrightarrow [0,1]^3 \times [0,1]\\
    W_k[n,m] &= (C_k \circ F \circ P)[n,m], \nonumber

for segment indices :math:`$n,m \in \mathbb{N}` with :math:`0 \leq n\leq m < N`. 
Following the hierarchical visual structure in Figure~\ref{tab:visuhierarchy}, 
wavescapes are displayed as triangles of colors, similarly to keyscapes (Sapp).

Applying the procedure described above for a given piece renders a wavescape for each of the six coefficients. 
Each of them may show interesting properties for music analysis. In order to determine on which wavescape to concentrate our analyses, 
we focus on those with the largest average normalized magnitude to which we refer by :math:`\bar{\alpha}_k` for a given piece and coefficient :math:`k`.