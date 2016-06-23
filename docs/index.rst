.. pyMEF documentation master file, created by
   sphinx-quickstart on Fri Sep  2 20:20:07 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. Welcome to pyMEF's documentation!
.. =================================

pyMEF: a Python library for mixtures of exponential families
============================================================

.. Contents:

.. .. toctree::
..    :maxdepth: 2

Description
-----------

pyMEF is a Python framework allowing to manipulate, learn, simplify and
compare mixtures of exponential families. It is designed to ease the use
of various exponential families in mixture models.

See also `jMEF`_ for a Java implementation of the same kind of library.

.. _jMEF: http://www.lix.polytechnique.fr/~nielsen/MEF/


What are exponential families?
------------------------------

An exponential family is a generic set of probability distributions that
admit the following canonical distribution:

.. math::
   p_F(x; \theta) = \exp \left( \langle t(x) | \theta \rangle - F(\theta) + k(x) \right)

Exponential families are characterized by the log normalizer function F,
and include the following well-known distributions: Gaussian (generic,
isotropic Gaussian, diagonal Gaussian, rectified Gaussian or Wald
distributions, lognormal), Poisson, Bernoulli, binomial, multinomial,
Laplacian, Gamma (incl. chi-squared), Beta, exponential, Wishart,
Dirichlet, Rayleigh, probability simplex, negative binomial
distribution, Weibull, von Mises, Pareto distributions, skew logistic,
etc.

Mixtures of exponential families provide a generic framework for
handling Gaussian mixture models (GMMs also called MoGs for mixture of
Gaussians), mixture of Poisson distributions, and Laplacian mixture
models as well.

Tutorials
---------

A `generic tutorial`_ on the exponential families and the simplification of
mixture models have been made during the workshop `Matrix Information
Geometries`_.

More pyMEF specific tutorials are available here:

.. _Matrix Information Geometries: http://www.informationgeometry.org/MIG/
.. _generic tutorial: http://www.lix.polytechnique.fr/~schwander/slides/mig2011.pdf

 .. toctree::
    :maxdepth: 2

    tutorial2.rst
..    tutorial1.rst

Module references
-----------------

.. autosummary::
   :toctree: generated

   pyMEF.MixtureModel
   pyMEF.Build.KDE
   pyMEF.Build.BregmanSoftClustering
   pyMEF.Simplify.BregmanHardClustering
   pyMEF.Compare.EMD
   pyMEF.Compare.KullbackLeibler

Download
--------

Currently, there is no official release of pyMEF, but you can have a
look at the public `darcs repository`_.

.. _darcs repository: http://www.lix.polytechnique.fr/~schwander/darcs/pyMEF

Bibliography
------------

- Olivier Schwander, Frank Nielsen,
  **Simplification de modèles de mélange issus d'estimateur par noyau**,
  GRETSI 2011

- Olivier Schwander and Frank Nielsen,
  **pyMEF - A framework for Exponential Families in Python**,
  in *Proceedings of the 2011 IEEE Workshop on Statistical Signal Processing*

- Vincent Garcia, Frank Nielsen, and Richard Nock,
  **Levels of details for Gaussian mixture models**,
  in *Proceedings of the Asian Conference on Computer Vision, Xi'an, China, September 2009*

- Frank Nielsen and Vincent Garcia,
  **Statistical exponential families: A digest with flash cards**,
  arXiV, http://arxiv.org/abs/0911.4863, November 2009

- Frank Nielsen and Richard Nock,
  **Sided and symmetrized Bregman centroids**,
  in *IEEE Transactions on Information Theory, 2009, 55, 2048-2059*

- Frank Nielsen, Jean-Daniel Boissonnat and Richard Nock,
  **On Bregman Voronoi diagrams**,
  in *ACM-SIAM Symposium on Data Mining, 2007, 746-755*

- A. Banerjee, S. Merugu, I. Dhillon, and J. Ghosh,
  **Clustering with Bregman divergences**,
  in *Journal of Machine Learning Research, 2005, 6, 234-245*

Contacts
--------

Please send any comment or bug report to `Olivier Schwander`_ or `Frank
Nielsen`_.

.. _Olivier Schwander: mailto:schwander@lix.polytechnique.fr
.. _Frank Nielsen: mailto:nielsen@lix.polytechnique.fr

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
