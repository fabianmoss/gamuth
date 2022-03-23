Tonal pitch-class coevolution
=============================

Modeling tonal pitch-class coevolution
--------------------------------------

The change/evolution of each pitch class :math:`k=i-a` is given by the
changes in
:math:`\mathbf{X}_i=(X^{1}_i,\dots,X^{t}_i,\dots,X^{T}_i)^\top\in \mathbb{R}^{T}`.
The pitch-class coevolution matrix is given by

.. math:: 
   
   \mathbf\Sigma=\left(\mathrm{corr}(\mathbf{X}_i, \mathbf{X}_j)\right)_{ij}\in[-1,1]^{n\times n}

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

.. .. figure:: ../img/macro/tpc_correlations_allpieces.png
..    :alt: The coevolution of tonal pitch classes.

..    The coevolution of tonal pitch classes.

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

.. .. figure:: ../img/macro/tpcs_coevolution_principal_components.png
..    :alt: Separate plots of the first four principal components jointly
..    accounting for 94% of the variance in the data.

..    Separate plots of the first four principal components jointly
..    accounting for 94% of the variance in the data.

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
   :math:`\sharp\sharp`.

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

.. .. figure:: ../img/macro/tpc_coevolution_pca2.png
..    :alt: Two-dimensional PCA reduction of tpc coevolutions.

..    Two-dimensional PCA reduction of tpc coevolutions.

TPC coevolution per historical period
-------------------------------------

This “global view” can be broken down to compare how the tpc
correlations change over time. The next figure shows the correlations
for 50-year periods

.. .. figure:: ../img/macro/tpc_correlations_periods.png
..    :alt: The coevolution of tonal pitch classes in different historical
..    periods.

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
Monteverdi's \*Cruda Amarilli\* SV 94, mm. 9-19, 24-30. Without
diminishing Monteverdi's influence we can see here that the first half
of the 17 century was indeed a time of change, at least with respect to
the conjunct usage of tones. But note also that the most prominent
composer in that epoch in the dataset is Gesualdo who is well-known for
his unusual harmonies.

Turn argument around: Use inter-pc correlations to show importance of
fifth structure! What about thirds?