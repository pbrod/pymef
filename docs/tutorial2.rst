Basic manipulation of mixture models
====================================

Creating a mixture
------------------

A mixture can be created directly:

   >>> from pyMEF import *
   >>> mm = MixtureModel(4, UnivariateGaussian, ())
   >>> mm[0].source((2, 1))
   >>> mm[1].source((5, 1))
   >>> mm[2].source((15, 1))
   >>> mm.weights[2] = 0.20
   >>> mm[3].source((20, 1))
   >>> mm.weights[3] = 0.05

The previous example creates a mixture of 4 UnivariateGaussian with no
arguments (the UnivariateGaussian distribution does not need any
argument).

Displaying the mixture
----------------------

The complete mixture can be printed out:

   >>> print mm

Another solution is to loop over all the components to display the
weight and the parameters for each component:

   >>> for (w, ef) in mm:
   >>>     print w, ef.source()

Saving and loading a mixture
----------------------------

A mixture can be saved to a text file:

   >>> mm.savetxt("mymodel")

In order to load the mixture, it is mandatory to create first a mixture
with an unknown number of components and with the good distribution (the
name of the distribution is not stored in the output file for now).

   >>> mm = MixtureModel(0, UnivariateGaussian, ())
   >>> mm.loadtxt("mymodel")

Since the models can be large, it is advised to compress the files, like
this:

   >>> from bz2 import BZ2File
   >>> mm.savetxt(BZ2File("mymodel.bz2", "w"))
   >>> mm = MixtureModel(0, UnivariateGaussian, ())
   >>> mm.loadtxt(BZ2File("mymodel.bz2"))
