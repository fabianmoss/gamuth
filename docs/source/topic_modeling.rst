Topic Modeling with Latent Dirichlet Allocation (LDA)
=====================================================

.. note::

   Rework this chapter based on the pedagogical introduction 
   in :cite:`Moss2021_DiscoveringTonalProfiles`.

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

Background
----------

- LDA in general (short review of relevant papers), numerous
  extensions of the basic model
- application to music, review model of 
  :cite:p:`Hu2009_ProbabilisticTopicModela,Hu2009_ProbabilisticTopicModel`

A **corpus** :math:`\mathcal C` is a set of :math:`M` pieces. For each
piece, the **distribution of topics** :math:`\theta` is drawn from a
Dirichlet distribution with fixed corpus parameter :math:`\alpha.`

A collection (multiset) of **notes**
:math:`\boldsymbol{u}_n = \{u_{n1},\ldots,u_{nL}\}` defines a
**segment**. The number of unique notes in a corpus is the **vocabulary
size** :math:`V`. Each segment :math:`{u}_n` (e.g. beat, slice, bar,
section, …) is assigned a unique **topic label** :math:`z` (key,
tonality, mode, …). A **piece**
:math:`\mathcal P = \{\boldsymbol{u}_1, \ldots, u_N\}` consists of
:math:`N` segments with associated topic labels. A piece can have at
most :math:`N` topics, if :math:`N\leq V`, otherwise at most :math:`V`
topics. **Topics** :math:`\beta` are defined as distributions over
notes. 
Since there are :math:`K` topics and :math:`V` distinct notes, 
:math:`\beta` can be represented as a :math:`V \times K` matrix where
:math:`\beta_{ij}` encodes the probability of note :math:`i` in topic
:math:`j`.

Definitions and Assumptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. A *note* :math:`u \in \mathbb Z_{12}`.

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

.. .. figure:: ../img/macro/LDA_model.png
..    :alt: Graphical model for Latent Dirichlet Allocation (LDA).

..    Graphical model for Latent Dirichlet Allocation (LDA).

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

.. .. figure:: ../img/macro/topic_0_of_7.png
..    :alt: The note distributions for the :math:`K=7` topics.
..    :width: 90.0%

..    The note distributions for the :math:`K=7` topics.

.. .. figure:: ../img/macro/topic_1_of_7.png
..    :alt: The note distributions for the :math:`K=7` topics.
..    :width: 90.0%

..    The note distributions for the :math:`K=7` topics.

.. .. figure:: ../img/macro/topic_2_of_7.png
..    :alt: The note distributions for the :math:`K=7` topics.
..    :width: 90.0%

..    The note distributions for the :math:`K=7` topics.

.. .. figure:: ../img/macro/topic_3_of_7.png
..    :alt: The note distributions for the :math:`K=7` topics.
..    :width: 90.0%

..    The note distributions for the :math:`K=7` topics.

.. .. figure:: ../img/macro/topic_4_of_7.png
..    :alt: The note distributions for the :math:`K=7` topics.
..    :width: 90.0%

..    The note distributions for the :math:`K=7` topics.

.. .. figure:: ../img/macro/topic_5_of_7.png
..    :alt: The note distributions for the :math:`K=7` topics.
..    :width: 90.0%

..    The note distributions for the :math:`K=7` topics.

.. .. figure:: ../img/macro/topic_6_of_7.png
..    :alt: The note distributions for the :math:`K=7` topics.
..    :width: 90.0%

..    The note distributions for the :math:`K=7` topics.

The relative weights of the topics in the overall corpus can be seen in
Figure [fig:topics\_weights]. The most common topic is topic 0
(“(transposed) diatonic”) and the least common is topic 4 (“far-flats”)

.. .. figure:: ../img/macro/topics_in_corpus.png
..    :alt: The relative weight of :math:`K=7` topics in the corpus.

..    The relative weight of :math:`K=7` topics in the corpus.

Besides calculating the overall importance of topics in the corpus, one
can also look at the relative topic weights within individual pieces.
Figure [fig:raw\_topics] shows this distribution. Analogous to the
pitch-class evolution from Figure [], pieces that are assigned to the
same year are accumulated (**Describe procedure!**).

.. .. figure:: ../img/macro/raw_topics.png
..    :alt: Historical change of topic weights in pieces.

..    Historical change of topic weights in pieces.

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

.. .. figure:: ../img/macro/7_topics_smooth(30).png
..    :alt: Historical trends for varying sliding window sizes.
..    :width: 90.0%

..    Historical trends for varying sliding window sizes.

.. .. figure:: ../img/macro/7_topics_smooth(50).png
..    :alt: Historical trends for varying sliding window sizes.
..    :width: 90.0%

..    Historical trends for varying sliding window sizes.

.. .. figure:: ../img/macro/7_topics_smooth(100).png
..    :alt: Historical trends for varying sliding window sizes.
..    :width: 90.0%

..    Historical trends for varying sliding window sizes.

In these figures we can observe a) the relative topic importances
(weights) over time, and b) identify breaking points and local extrema.

Moreover, the entropy of these distributions is informative!

Todo: PCA shows relation between topics and documents in (reduced)
note-space

Topic coevolution
-----------------

topic correlations motivate hierarchical clustering

.. .. figure:: ../img/macro/7_topics_coevolution.png
..    :alt: The coevolution of tonal pitch classes in different historical
..    periods (only for years with pieces).

..    The coevolution of tonal pitch classes in different historical
..    periods (only for years with pieces).

.. .. figure:: ../img/macro/7_topics_coevolution_all_years.png
..    :alt: The coevolution of tonal pitch classes in different historical
..    periods (for all years in the range).

..    The coevolution of tonal pitch classes in different historical
..    periods (for all years in the range).

.. .. figure:: ../img/macro/topic_clustering.png
..    :alt: Topic clustering.

..    Topic clustering.

Pitch class – topic coevolution
-------------------------------

.. .. figure:: ../img/macro/tpc_topic_coevolution.png
..    :alt: Topic clustering.

..    Topic clustering.

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Improving the bag-of-notes model with a Hidden Markov Topic Model

.. .. figure:: ../img/macro/HMTM_model.png
..    :alt: Graphical Model for the Hidden Markov Topic Model (HMTM).

..    Graphical Model for the Hidden Markov Topic Model (HMTM).

Discussion
~~~~~~~~~~

* Result 1: Historically, ever larger portions of pitch space are explored
* There is a trend from diatonic > chromatic > enharmonic pieces, but it
  is not monotonic. In the 19th century, there are diatonic Lieder
  (composer) and Alkan, who has the greatest tonality range
  (diatonic-enharmonic).

.. .. |image| image:: img/macro/fifth_widths.png
