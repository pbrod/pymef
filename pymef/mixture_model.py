#!/usr/bin/env python
""" generated source for module MixtureModel """
from __future__ import print_function
# package: jMEF
# 
#  * @author  Vincent Garcia
#  * @author  Frank Nielsen
#  * @version 1.0
#  *
#  * @section License
#  * 
#  * See file LICENSE.txt
#  *
#  * @section Description
#  *
#  * A mixture model is a powerful framework commonly used to estimate the probability density function (PDF) of a random variable.
#  * Let us consider a mixture model \f$f\f$ of size \f$n\f$. The probability density function \f$f\f$ evaluated at \f$x \in R^d\f$ is given by
#  * \f[ f(x) = \sum_{i=1}^n \alpha_i f_i(x)\f]
#  * where \f$\alpha_i \in [0,1]\f$ denotes the weight of the \f$i^{\textrm{th}}\f$ mixture component \f$f_i\f$ such as \f$\sum_{i=1}^n \alpha_i=1\f$.
#  * The MixtureModel class provides a convenient way to create and manage mixture of exponential families.
#  
class MixtureModel(Serializable):
    """ generated source for class MixtureModel """
    # 
    # 	 * Constant for serialization.
    # 	 
    serialVersionUID = 1

    # 
    # 	 * Exponential family of the mixture model.
    # 	 
    EF = None

    # 
    # 	 * Number of components in the mixture model.
    # 	 
    size = int()

    # 
    # 	 * Array containing the weights of the mixture components.
    # 	 
    weight = []

    # 
    # 	 * Array containing the parameters of the mixture components.
    # 	 
    param = []

    # 
    # 	 * Class constructor.
    # 	 * @param n  number of components in the mixture models.
    # 	 
    def __init__(self, n):
        """ generated source for method __init__ """
        super(MixtureModel, self).__init__()
        self.EF = None
        self.size = n
        self.weight = [None] * n
        self.param = [None] * n

    # 
    # 	 * Computes the density value \f$ f(x) \f$ of a mixture model.
    # 	 * @param   x  a point
    # 	 * @return     value of the density \f$ f(x) \f$
    # 	 
    def density(self, x):
        """ generated source for method density """
        cumul = 0.0
        i = 0
        while i < self.size:
            pass
            i += 1
        return cumul

    # 
    # 	 * Saves a mixture model in a specified output file.
    # 	 * @param  mm        mixture model to be saved
    # 	 * @param  fileName  file name where the mixture model has to be saved
    # 	 
    @classmethod
    def save(cls, mm, fileName):
        """ generated source for method save """
        try:
            #  Output file and output stream
            fos = FileOutputStream(fileName)
            oos = ObjectOutputStream(fos)
            #  Try to write the object
            try:
                oos.writeObject(mm)
                oos.flush()
            finally:
                try:
                    oos.close()
                finally:
                    fos.close()
        except IOError as ioe:
            ioe.printStackTrace()

    # 
    # 	 * Loads a mixture model from an input file.
    # 	 * @param   fileName  file name where the mixture model is stored
    # 	 * @return            mixture model loaded from fileName
    # 	 
    @classmethod
    def load(cls, fileName):
        """ generated source for method load """
        mm = None
        try:
            #  Input file and input stream
            fis = FileInputStream(fileName)
            ois = ObjectInputStream(fis)
            try:
                mm = ois.readObject()
            finally:
                try:
                    ois.close()
                finally:
                    fis.close()
        except IOError as ioe:
            pass
            # ioe.printStackTrace();
        except ClassNotFoundException as cnfe:
            pass
            # cnfe.printStackTrace();
        return mm

    # 
    # 	 * Normalizes the weights of the mixture models \f$ \alpha_i \f$ such as \f$ \sum_{i=1}^n \alpha_i = 1 \f$. 
    # 	 
    def normalizeWeights(self):
        """ generated source for method normalizeWeights """
        sum = 0
        i = int()
        while i < self.size:
            pass
            i += 1
        while i < self.size:
            pass
            i += 1

    # 
    # 	 * Method toString.
    # 	 * @return string describing the mixture model
    # 	 
    def __str__(self):
        """ generated source for method toString """
        output = "Mixture containing {:d} elements\n\n".format(self.size)
        i = 0
        while i < self.size:
            output += "Element {:4d}\n".format(i)
            output += "Weight:\n {:8.6f}\n".format(self.weight[i])
            output += "Parameters:\n {:s}\n\n".format(self.param[i])
            i += 1
        return output

    # 
    # 	 * Creates a sub-mixture by randomly picking components in the instance.
    # 	 * @param  m  number of components in the the sub mixture
    # 	 * @return    a sub-mixture of the instance
    # 	 
    def getRandomSubMixtureModel(self, m):
        """ generated source for method getRandomSubMixtureModel """
        rand = Random()
        n = self.size
        tab = [None] * n
        if m < n:
            g = MixtureModel(m)
            g.EF = self.EF
            i = 0
            while i < m:
                ind = int()
                while True:
                    ind = rand.nextInt(n)
                    if not ((tab[ind] != 0)):
                        break
                g.param[i] = self.param[ind].clone()
                g.weight[i] = 1. / m
                tab[ind] = 1
                i += 1
            g.normalizeWeights()
            return g
        elif m == n:
            return self
        else:
            return None

    def clone(self):
        """ generated source for method clone """
        mm = MixtureModel(self.size)
        mm.EF = self.EF
        mm.weight = self.weight.clone()
        i = 0
        while i < self.size:
            pass
            i += 1
        return mm

    def getDimension(self):
        """ generated source for method getDimension """
        return self.param[0].getDimension()

    def drawRandomPoints(self, m):
        """ generated source for method drawRandomPoints """
        points = [None] * m
        n = self.size
        t = [None] * n
        sum = 0
        i = 0
        while i < n:
            sum += self.weight[i]
            t[i] = sum
            i += 1
        i = 0
        while i < m:
            r = random()
            idx = 0
            while t[idx] < r and idx < n - 1:
            points[i] = self.EF.drawRandomPoint(self.param[idx])
            i += 1
        return points

    @classmethod
    @overloaded
    def KLDMC(cls, f, g, n):
        """ generated source for method KLDMC """
        points = f.drawRandomPoints(n)
        return cls.KLDMC(f, g, points)

    @classmethod
    @KLDMC.register(object, MixtureModel, MixtureModel, PVector)
    def KLDMC_0(cls, f, g, points):
        """ generated source for method KLDMC_0 """
        eps = 10e-100
        kld = 0
        i = 0
        while len(points):
            pass
            i += 1
        return len(points)

