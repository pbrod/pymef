#!/usr/bin/env python
""" generated source for module UnivariateGaussian """
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
#  * The univariate Gaussian distribution is an exponential family and, as a consequence, the probability density function is given by
#  * \f[ f(x; \mathbf{\Theta}) = \exp \left( \langle t(x), \mathbf{\Theta} \rangle - F(\mathbf{\Theta}) + k(x) \right) \f]
#  * where \f$ \mathbf{\Theta} \f$ are the natural parameters.
#  * This class implements the different functions allowing to express a univariate Gaussian distribution as a member of an exponential family.
#  * 
#  * @section Parameters
#  * 
#  * The parameters of a given distribution are:
#  *   - Source parameters \f$\mathbf{\Lambda} = ( \mu , \sigma^2 ) \in R \times R^+\f$
#  *   - Natural parameters \f$\mathbf{\Theta} = ( \theta_1 , \theta_2 ) \in R \times R^-\f$
#  *   - Expectation parameters \f$ \mathbf{H} = ( \eta_1 , \eta_2 ) \in R \times R^+\f$
#  
class UnivariateGaussian(ExponentialFamily, PVector, PVector):
    """ generated source for class UnivariateGaussian """
    # 
    # 	 * Constant for serialization.
    # 	 
    serialVersionUID = 1

    # 
    # 	 * Computes the log normalizer \f$ F( \mathbf{\Theta} ) \f$.
    # 	 * @param   T  parameters \f$ \mathbf{\Theta} = ( \theta_1 , \theta_2 ) \f$
    # 	 * @return     \f$ F(\mathbf{\Theta}) = -\frac{\theta_1^2}{4\theta_2} + \frac{1}{2} \log \left( -\frac{\pi}{\theta_2} \right) \f$
    # 	 
    def F(self, T):
        """ generated source for method F """
        return -0.25 * T.array[0] * T.array[0] / T.array[1] + 0.5 * log(-PI / T.array[1])

    # 
    # 	 * Computes \f$ \nabla F ( \mathbf{\Theta} )\f$.
    # 	 * @param   T  natural parameters \f$ \mathbf{\Theta} = ( \theta_1 , \theta_2 ) \f$
    # 	 * @return     \f$ \nabla F(\mathbf{\Theta}) = \left( -\frac{\theta_1}{2 \theta_2}  , -\frac{1}{2 \theta_2} + \frac{\theta_1^2}{4 \theta_2^2} \right) \f$
    # 	 
    def gradF(self, T):
        """ generated source for method gradF """
        gradient = PVector(2)
        gradient.array[0] = -0.5 * T.array[0] / T.array[1]
        gradient.array[1] = 0.25 * (T.array[0] * T.array[0]) / (T.array[1] * T.array[1]) - 0.5 / T.array[1]
        gradient.type_ = TYPE.EXPECTATION_PARAMETER
        return gradient

    # 
    # 	 * Computes \f$ G(\mathbf{H})\f$.
    # 	 * @param   H  expectation parameters \f$ \mathbf{H} = ( \eta_1 , \eta_2 ) \f$
    # 	 * @return     \f$ G(\mathbf{H}) = - \frac{1}{2} \log ( \eta_1^2 - \eta_2 ) \f$
    # 	 
    def G(self, H):
        """ generated source for method G """
        return -0.5 * log(abs(H.array[0] * H.array[0] - H.array[1]))

    # 
    # 	 * Computes \f$ \nabla G (\mathbf{H})\f$.
    # 	 * @param   H  expectation parameters \f$ \mathbf{H} = ( \eta_1 , \eta_2) \f$
    # 	 * @return     \f$ \nabla G(\mathbf{H}) = \left( -\frac{\eta_1}{\eta_1^2-\eta_2} , \frac{1}{2 (\eta_1^2-\eta_2)} \right) \f$
    # 	 
    def gradG(self, H):
        """ generated source for method gradG """
        gradient = PVector(2)
        tmp = H.array[0] * H.array[0] - H.array[1]
        gradient.array[0] = -H.array[0] / tmp
        gradient.array[1] = 0.5 / tmp
        gradient.type_ = TYPE.NATURAL_PARAMETER
        return gradient

    # 
    # 	 * Computes the sufficient statistic \f$ t(x)\f$.
    # 	 * @param   x  a point
    # 	 * @return     \f$ t(x) = (x , x^2) \f$
    # 	 
    def t(self, x):
        """ generated source for method t """
        t = PVector(2)
        t.array[0] = x.array[0]
        t.array[1] = x.array[0] * x.array[0]
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
    # 	 * @param   L  source parameters \f$ \mathbf{\Lambda} = ( \mu , \sigma^2 )\f$
    # 	 * @return     natural parameters \f$ \mathbf{\Theta} =	\left( \frac{\mu}{\sigma^2} , -\frac{1}{2\sigma^2} \right) \f$
    # 	 
    def Lambda2Theta(self, L):
        """ generated source for method Lambda2Theta """
        T = PVector(2)
        T.array[0] = L.array[0] / L.array[1]
        T.array[1] = -1.0 / (2 * L.array[1])
        T.type_ = TYPE.NATURAL_PARAMETER
        return T

    # 
    # 	 * Converts natural parameters to source parameters.
    # 	 * @param   T  natural parameters \f$ \mathbf{\Theta}  = ( \theta_1 , \theta_2 )\f$
    # 	 * @return     source parameters  \f$ \mathbf{\Lambda} = \left( -\frac{\theta_1}{2 \theta_2} , -\frac{1}{2 \theta_2} \right) \f$
    # 	 
    def Theta2Lambda(self, T):
        """ generated source for method Theta2Lambda """
        L = PVector(2)
        L.array[0] = -T.array[0] / (2 * T.array[1])
        L.array[1] = -1 / (2 * T.array[1])
        L.type_ = TYPE.SOURCE_PARAMETER
        return L

    # 
    # 	 * Converts source parameters to expectation parameters.
    # 	 * @param   L  source parameters \f$ \mathbf{\Lambda} = ( \mu , \sigma^2 )\f$
    # 	 * @return     expectation parameters \f$ \mathbf{H} = \left( \mu , \sigma^2 + \mu^2 \right) \f$
    # 	 
    def Lambda2Eta(self, L):
        """ generated source for method Lambda2Eta """
        H = PVector(2)
        H.array[0] = L.array[0]
        H.array[1] = L.array[0] * L.array[0] + L.array[1]
        H.type_ = TYPE.EXPECTATION_PARAMETER
        return H

    # 
    # 	 * Converts expectation parameters to source parameters.
    # 	 * @param   H  natural parameters \f$ \mathbf{H}       = ( \eta_1 , \eta_2 )\f$
    # 	 * @return     source parameters  \f$ \mathbf{\Lambda} = \left( \eta_1 , \eta_2 - \eta_1^2 \right) \f$
    # 	 
    def Eta2Lambda(self, H):
        """ generated source for method Eta2Lambda """
        L = PVector(2)
        L.array[0] = H.array[0]
        L.array[1] = H.array[1] - H.array[0] * H.array[0]
        L.type_ = TYPE.SOURCE_PARAMETER
        return L

    # 
    # 	 * Box-Muller transform/generator.
    # 	 * @param mu      mean \f$ \mu \f$
    # 	 * @param sigma   variance \f$ \sigma \f$
    # 	 * @return        \f$ \mu + \sigma \sqrt{ -2 \log ( x ) } \cos (2 \pi x) \f$ where \f$ x \in \mathcal{U}(0,1)\f$
    # 	 
    @classmethod
    @overloaded
    def Rand(cls, mu, sigma):
        """ generated source for method Rand """
        return mu + sigma * sqrt(-2.0 * log(random())) * cos(2.0 * PI * random())

    # 
    # 	 *  Box-Muller transform/generator
    # 	 * @return \f$ \sqrt{ -2 \log ( x ) } \cos (2 \pi x) \f$ where \f$ x \in \mathcal{U}(0,1)\f$
    # 	 
    @classmethod
    @Rand.register(object)
    def Rand_0(cls):
        """ generated source for method Rand_0 """
        return cls.Rand(0, 1)

    # 
    # 	 * Computes the density value \f$ f(x;\mu,\sigma^2) \f$.
    # 	 * @param  x      point
    # 	 * @param  param  parameters (source, natural, or expectation)
    # 	 * @return        \f$ f(x;\mu,\sigma^2) = \frac{1}{ \sqrt{2\pi \sigma^2} } \exp \left( - \frac{(x-\mu)^2}{ 2 \sigma^2} \right) \f$
    # 	 
    def density(self, x, param):
        """ generated source for method density """
        if param.type_ == TYPE.SOURCE_PARAMETER:
            return exp(-(x.array[0] - param.array[0]) * (x.array[0] - param.array[0]) / (2.0 * param.array[1])) / (sqrt(2.0 * PI * param.array[1]))
        elif param.type_ == TYPE.NATURAL_PARAMETER:
            return super(UnivariateGaussian, self).density(x, param)
        else:
            return super(UnivariateGaussian, self).density(x, Eta2Theta(param))

    # 
    # 	 * Draws a point from the considered distribution.
    # 	 * @param   L  source parameters \f$ \mathbf{\Lambda} = ( \mu , \sigma^2 )\f$
    # 	 * @return     a point
    # 	 
    def drawRandomPoint(self, L):
        """ generated source for method drawRandomPoint """
        #  Mean and variance
        mean = PVector(1)
        variance = PVector(1)
        mean.array[0] = L.array[0]
        variance.array[0] = L.array[1]
        #  Draw the point
        rand = Random()
        v = PVector(1)
        v.array[0] = rand.nextGaussian() * sqrt(variance.array[0])
        return v.Plus(mean)

    # 
    # 	 * Computes the Kullback-Leibler divergence between two univariate Gaussian distributions.
    # 	 * @param   LP  source parameters \f$ \mathbf{\Lambda}_P \f$
    # 	 * @param   LQ  source parameters \f$ \mathbf{\Lambda}_Q \f$
    # 	 * @return      \f$ D_{\mathrm{KL}}(f_P\|f_Q) = \frac{1}{2} \left(  2 \log \frac{\sigma_Q}{\sigma_P} + \frac{\sigma_P^2}{\sigma_Q^2} + \frac{(\mu_Q-\mu_P)^2}{\sigma_Q^2} -1\right) \f$
    # 	 
    def KLD(self, LP, LQ):
        """ generated source for method KLD """
        mP = LP.array[0]
        vP = LP.array[1]
        mQ = LQ.array[0]
        vQ = LQ.array[1]
        return 0.5 * (2 * log(sqrt(vQ / vP)) + vP / vQ + ((mQ - mP) * (mQ - mP)) / vQ - 1)

