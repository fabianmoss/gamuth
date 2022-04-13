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
:cite:p:`Harasim2021_ExploringFoundationsTonality`
and also shown that there are historical developments.

If one does not transpose pieces, pieces that have similar root and mode
(and, accordingly, similar distributions) should cluster together. Since
:math:`V` is usually quite large, it is difficult to visualize these
clusters. One can use methods for dimensionality reduction to represent
the data in lower-dimensional spaces (2D or 3D) in order to visualize
them while at the same time maintaining characteristic properties of the
original space.

One of the most popular and classic methods is **principal component
analysis** :cite:p:`Bishop2006_PatternRecognitionMachine`, that can be used to project
the data onto a two-dimensional plane while keeping as much of the
variance in the data as possible. A more recent method for
dimensionality is called :math:`t`-distributed stochastic neighbor
embedding (:math:`t`-SNE) :cite:p:`VanDerMaaten2008_VisualizingDataUsing`. PCA is
better to get a global understanding of the structure of the space and
:math:`t`-SNE is better in illustrating local relationships. Figure
[fig:tsne\_pca] shows the data reduced to the Euclidean plane by both
methods.

A more modern method is UMAP :cite:`McInnes2020_UMAPUniformManifold`, much faster but conceptually different!

.. .. figure:: img/macro/dim_reduct.png
..    :alt: Dimensionality reduction of piece space via :math:`t`-SNE (top)
..    and PCA (bottom).

..    Dimensionality reduction of piece space via :math:`t`-SNE (top) and
..    PCA (bottom).

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
