#!/usr/bin/env python
""" generated source for module laplacian """
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
#  * The Laplacian distribution is an exponential family and, as a consequence, the probability density function is given by
#  * \f[ f(x; \mathbf{\Theta}) = \exp \left( \langle t(x), \mathbf{\Theta} \rangle - F(\mathbf{\Theta}) + k(x) \right) \f]
#  * where \f$ \mathbf{\Theta} \f$ are the natural parameters.
#  * This class implements the different functions allowing to express a Laplacian distribution as a member of an exponential family.
#  * 
#  * @section Parameters
#  * 
#  * The parameters of a given distribution are:
#  *   - Source parameters \f$\mathbf{\Lambda} = \sigma \in R^+\f$
#  *   - Natural parameters \f$\mathbf{\Theta} = \theta \in R^-\f$
#  *   - Expectation parameters \f$ \mathbf{H} = \eta \in R^+ \f$
#  *
#  
class Laplacian(ExponentialFamily, PVector, PVector):
    """ generated source for class Laplacian """
    # 
    # 	 * Constant for serialization
    # 	 
    serialVersionUID = 1

    # 
    # 	 * Computes the log normalizer \f$ F( \mathbf{\Theta} ) \f$.
    # 	 * @param   T  natural parameters \f$ \mathbf{\Theta} = \theta \f$
    # 	 * @return     \f$ F(\mathbf{\Theta}) = \log \left( -\frac{2}{\theta} \right)  \f$
    # 	 
    def F(self, T):
        """ generated source for method F """
        return log(-2.0 / T.array[0])

    # 
    # 	 * Computes \f$ \nabla F ( \mathbf{\Theta} )\f$.
    # 	 * @param   T  natural parameters \f$ \mathbf{\Theta} = \theta \f$
    # 	 * @return     \f$ \nabla F( \mathbf{\Theta} ) = -\frac{1}{\theta} \f$
    # 	 
    def gradF(self, T):
        """ generated source for method gradF """
        g = PVector(T.dim)
        g.array[0] = -1.0 / T.array[0]
        g.type_ = TYPE.EXPECTATION_PARAMETER
        return g

    # 
    # 	 * Computes \f$ G(\mathbf{H})\f$.
    # 	 * @param   H  expectation parameters \f$ \mathbf{H} = \eta \f$
    # 	 * @return     \f$ G(\mathbf{H}) = - \log \eta \f$
    # 	 
    def G(self, H):
        """ generated source for method G """
        return -log(H.array[0])

    # 
    # 	 * Computes \f$ \nabla G (\mathbf{H})\f$.
    # 	 * @param   H  expectation parameters \f$ \mathbf{H} = \eta \f$
    # 	 * @return     \f$ \nabla G(\mathbf{H}) = -\frac{1}{\eta} \f$
    # 	 
    def gradG(self, H):
        """ generated source for method gradG """
        g = PVector(1)
        g.array[0] = -1.0 / H.array[0]
        g.type_ = TYPE.NATURAL_PARAMETER
        return g

    # 
    # 	 * Computes the sufficient statistic \f$ t(x)\f$.
    # 	 * @param   x  a point
    # 	 * @return     \f$ t(x) = |x| \f$
    # 	 
    def t(self, x):
        """ generated source for method t """
        t = PVector(1)
        t.array[0] = abs(x.array[0])
        t.type_ = TYPE.EXPECTATION_PARAMETER
        return t

    # 
    # 	 * Computes the carrier measure \f$ k(x) \f$.
    # 	 * @param   x  a point
    # 	 * @return     \f$ k(x) = 0 \f$
    # 	 
    def k(self, x):
        """ generated source for method k """
        return 0.0

    # 
    # 	 * Converts source parameters to natural parameters.
    # 	 * @param   L  source parameters  \f$ \mathbf{\Lambda} = \sigma \f$
    # 	 * @return     natural parameters \f$ \mathbf{\Theta}  = -\frac{1}{\sigma} \f$
    # 	 
    def Lambda2Theta(self, L):
        """ generated source for method Lambda2Theta """
        T = PVector(L.dim)
        T.array[0] = -1.0 / L.array[0]
        T.type_ = TYPE.NATURAL_PARAMETER
        return T

    # 
    # 	 * converts natural parameters to source parameters.
    # 	 * @param   T  natural parameters \f$ \mathbf{\Theta}  = \theta \f$
    # 	 * @return     source parameters  \f$ \mathbf{\Lambda} = -\frac{1}{\theta} \f$
    # 	 
    def Theta2Lambda(self, T):
        """ generated source for method Theta2Lambda """
        L = PVector(T.dim)
        L.array[0] = -1.0 / T.array[0]
        L.type_ = TYPE.SOURCE_PARAMETER
        return L

    # 
    # 	 * Converts source parameters to expectation parameters.
    # 	 * @param   L  source parameters      \f$ \mathbf{\Lambda} = \sigma \f$
    # 	 * @return     expectation parameters \f$ \mathbf{H}       = \sigma \f$
    # 	 
    def Lambda2Eta(self, L):
        """ generated source for method Lambda2Eta """
        H = PVector(1)
        H.array[0] = L.array[0]
        H.type_ = TYPE.EXPECTATION_PARAMETER
        return H

    # 
    # 	 * Converts expectation parameters to source parameters.
    # 	 * @param   H  expectation parameters \f$ \mathbf{H}       = \eta \f$
    # 	 * @return     source parameters      \f$ \mathbf{\Lambda} = \eta \f$
    # 	 
    def Eta2Lambda(self, H):
        """ generated source for method Eta2Lambda """
        L = PVector(1)
        L.array[0] = H.array[0]
        L.type_ = TYPE.SOURCE_PARAMETER
        return L

    # 
    # 	 * Computes the density value \f$ f(x;\sigma) \f$.
    # 	 * @param  x      a point
    # 	 * @param  param  parameters (source, natural, or expectation)
    # 	 * @return         \f$ f(x;\sigma) = \frac{1}{ 2 \sigma } \exp \left( - \frac{|x|}{\sigma} \right) \f$
    # 	 
    def density(self, x, param):
        """ generated source for method density """
        if param.type_ == TYPE.SOURCE_PARAMETER:
            return (1.0 / (2 * param.array[0])) * exp(-abs(x.array[0]) / param.array[0])
        elif param.type_ == TYPE.NATURAL_PARAMETER:
            return super(Laplacian, self).density(x, param)
        else:
            return super(Laplacian, self).density(x, Eta2Theta(param))

    # 
    # 	 * Draws a point from the considered Laplacian distribution.
    # 	 * @param   L  source parameters \f$ \mathbf{\Lambda}\f$.
    # 	 * @return     a point.
    # 	 
    def drawRandomPoint(self, L):
        """ generated source for method drawRandomPoint """
        u = random() - 0.5
        point = PVector(1)
        point.array[0] = -L.array[0] * signum(u) * log(1 - 2 * abs(u))
        return point

    # 
    # 	 * Computes the Kullback-Leibler divergence between two Laplacian distributions.
    # 	 * @param   LP  source parameters \f$ \mathbf{\Lambda}_P \f$
    # 	 * @param   LQ  source parameters \f$ \mathbf{\Lambda}_Q \f$
    # 	 * @return      \f$ D_{\mathrm{KL}}(f_P\|f_Q) = \log \left( \frac{\sigma_Q}{\sigma_P} \right) + \frac{\sigma_P - \sigma_Q}{\sigma_Q} \f$
    # 	 
    def KLD(self, LP, LQ):
        """ generated source for method KLD """
        sP = LP.array[0]
        sQ = LQ.array[0]
        return log(sQ / sP) + (sP - sQ) / sQ

