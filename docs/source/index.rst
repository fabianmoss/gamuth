GAMuTh: Guide to Advanced Music Theory
======================================

.. warning::
   The content on these pages is very much under construction!
   Since this is ongoing work, I can give no guarantee for completeness or accuracy.
   Feel free to `contact me`_ with your questions and suggestions!

.. _contact me: fabianmoss@gmail.com

Welcome!

This is not a pedagogical resource for basic music theory concepts
but an in-depth introduction into the structures of Western music,
built axiomatically from tones and their relations.
The logo, a `maxima`_, the longest note value in medieval music, 
symbolically reflects this level of difficulty. 

.. _maxima: https://en.wikipedia.org/wiki/Maxima_(music)

The content presented on these pages is inspired by a number of great books, e.g. 
:cite:t:`Aldwell2010`, :cite:t:`Lewin1987`, :cite:t:`Straus2005`,
:cite:t:`Cadwallader1998`, and :cite:t:`Mueller2015`.
What is new and unique about the approach taken here is that we take 
a computational perspective and implement all introduced concepts.
This does not only provide us with sharp and unequivocal definitions,
but also allows us to scale music theory up from the analysis of individual 
bars, sections, or pieces to that of entire repertoires and corpora!

I recently also discovered `Music for Geeks and Nerds`_ by Pedro Kroger
which looks very interesting. 
The Python project `musthe`_ also seems to pursue a similar goal.

.. _`Music for Geeks and Nerds`: https://pedrokroger.net/mfgan/
.. _`musthe`: https://github.com/gciruelos/musthe

.. only:: latex

   .. note::
      Some content is only available in the online HTML version and not in the PDF, 
      e.g. scores rendered with Lilypond. Please visit the **website** to see the full version.

   .. note::
      
      TODO: add link to website


.. rubric:: Quickstart

.. warning::
   These instructions may not work yet. 

Installation of the `gamuth` Python library is as easy as it can be. Just 
type the following in your terminal::

   pip install gamuth 

Then, in a Python script or Jupyter notebook, import the library or individual classes::

   >>> from gamuth import Tone, Interval

   >>> t = Tone(octave=0, fifth=0, third=0) # C
   >>> s = Tone(octave=0, fifth=0, third=1) # E

   >>> i = Interval(t, s) 

   >>> print(i.specific interval) # directed interval in semitones (major third)
   4 

See the documentation :ref:`api` for examples how to use the library, its classes and their methods.


.. only:: html

   .. rubric:: Table of contents

.. toctree::
   :maxdepth: 2
   :numbered:

   1_fundamentals
   2_scales_modes
   3_set_theory
   4_time
   4_harmony 
   5_notes
   5_segmentation
   6_advanced

   8_bibliography

.. 4_Fourier_pitch_space
.. 2_sequences
.. 3_representations
.. 8_bibliography

.. 5_notes

.. Indices and tables
.. ------------------

.. * :ref:`genindex`
.. * :ref:`search`

.. * :ref:`modindex`

Developers
----------

.. toctree::
   :maxdepth: 2

   api
