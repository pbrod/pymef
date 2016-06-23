#!/usr/bin/env python
""" generated source for module ExponentialFamily """
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
#  * This class integrates the Kullback-Leibler divergence and conversion procedures inside the exponential family.
#  *   - ParamD are the distribution source parameters, its dimension is the order of the exponential family.
#  *   - ParamX are the type of observations.
#  
class ExponentialFamily(Serializable):
    """ generated source for class ExponentialFamily """
    # 
    # 	 * Constant for serialization.
    # 	 
    serialVersionUID = 1

    # 
    # 	 * Computes the log normalizer \f$ F( \mathbf{\Theta} ) \f$.
    # 	 * @param   T  natural parameters \f$ \mathbf{\Theta}\f$
    # 	 * @return     \f$ F(\mathbf{\Theta}) \f$
    # 	 
    def F(self, T):
        """ generated source for method F """

    # 
    # 	 * Computes \f$ \nabla F ( \mathbf{\Theta} )\f$.
    # 	 * @param   T  expectation parameters \f$ \mathbf{\Theta} \f$
    # 	 * @return     \f$ \nabla F( \mathbf{\Theta} ) \f$
    # 	 
    def gradF(self, T):
        """ generated source for method gradF """

    # 
    # 	 * Computes \f$ div F \f$.
    # 	 * @param   TP  natural parameters \f$ \mathbf{\Theta}_P\f$
    # 	 * @param   TQ  natural parameters \f$ \mathbf{\Theta}_Q\f$
    # 	 * @return      \f$ div F( \mathbf{\Theta}_P \| \mathbf{\Theta}_Q ) =  F(\mathbf{\Theta}_P) - F(\mathbf{\Theta}_Q) - \langle \mathbf{\Theta}_P-\mathbf{\Theta}_Q , \nabla F(\mathbf{\Theta}_Q) \rangle\f$
    # 	 
    def DivergenceF(self, TP, TQ):
        """ generated source for method DivergenceF """
        return self.F(TP) - self.F(TQ) - (TP.Minus(TQ)).InnerProduct(self.gradF(TQ))

    # 
    # 	 * Computes \f$ G(\mathbf{H})\f$
    # 	 * @param   H  expectation parameters \f$ \mathbf{H} \f$
    # 	 * @return     \f$ G(\mathbf{H}) \f$
    # 	 
    def G(self, H):
        """ generated source for method G """

    # 
    # 	 * Computes \f$ \nabla G (\mathbf{H})\f$
    # 	 * @param   H  expectation parameters \f$ \mathbf{H} \f$
    # 	 * @return        \f$ \nabla G(\mathbf{H}) \f$
    # 	 
    def gradG(self, H):
        """ generated source for method gradG """

    # 
    # 	 * Computes \f$ div G \f$.
    # 	 * @param   HP  expectation parameters \f$ \mathbf{H}_P\f$
    # 	 * @param   HQ  expectation parameters \f$ \mathbf{H}_Q\f$
    # 	 * @return      \f$ div G( \mathbf{H}_P \| \mathbf{H}_Q ) =  G(\mathbf{H}_P) - G(\mathbf{H}_Q) - \langle \mathbf{H}_P-\mathbf{H}_Q , \nabla G(\mathbf{H}_Q) \rangle\f$
    # 	 
    def DivergenceG(self, HP, HQ):
        """ generated source for method DivergenceG """
        return self.G(HP) - self.G(HQ) - (HP.Minus(HQ)).InnerProduct(self.gradG(HQ))

    # 
    # 	 * Computes the sufficient statistic \f$ t(x)\f$.
    # 	 * @param   x  a point
    # 	 * @return     \f$ t(x) \f$
    # 	 
    def t(self, x):
        """ generated source for method t """

    # 
    # 	 * Computes the carrier measure \f$ k(x) \f$.
    # 	 * @param   x  a point
    # 	 * @return     \f$ k(x) \f$
    # 	 
    def k(self, x):
        """ generated source for method k """

    # 
    # 	 * Converts source parameters to natural parameters.
    # 	 * @param   L  source parameters \f$ \mathbf{\Lambda} \f$
    # 	 * @return     natural parameters \f$ \mathbf{\Theta} \f$
    # 	 
    def Lambda2Theta(self, L):
        """ generated source for method Lambda2Theta """

    # 
    # 	 * Converts natural parameters to source parameters.
    # 	 * @param   T  natural parameters \f$ \mathbf{\Theta}\f$
    # 	 * @return     source parameters \f$ \mathbf{\Lambda} \f$
    # 	 
    def Theta2Lambda(self, T):
        """ generated source for method Theta2Lambda """

    # 
    # 	 * Converts source parameters to expectation parameters.
    # 	 * @param   L  source parameters \f$ \mathbf{\Lambda} \f$
    # 	 * @return     expected parameters \f$ \mathbf{H} \f$
    # 	 
    def Lambda2Eta(self, L):
        """ generated source for method Lambda2Eta """

    # 
    # 	 * Converts expectation parameters to source parameters.
    # 	 * @param   H  expectation parameters \f$ \mathbf{H} \f$
    # 	 * @return     source parameters \f$ \mathbf{\Lambda} \f$
    # 	 
    def Eta2Lambda(self, H):
        """ generated source for method Eta2Lambda """

    # 
    # 	 * Converts natural parameters to expectation parameters.
    # 	 * @param   T  natural parameters \f$ \mathbf{\Theta}\f$
    # 	 * @return     expectation parameters \f$ \mathbf{H} \f$
    # 	 
    def Theta2Eta(self, T):
        """ generated source for method Theta2Eta """
        return self.gradF(T)

    # 
    # 	 * Converts expectation parameters to natural parameters.
    # 	 * @param   H  expectation parameters \f$ \mathbf{H} \f$
    # 	 * @return     natural parameters \f$ \mathbf{\Theta} \f$
    # 	 
    def Eta2Theta(self, H):
        """ generated source for method Eta2Theta """
        return self.gradG(H)

    # 
    # 	 * Computes the density value \f$ f(x;\mathbf{\Theta}) \f$ of an exponential family member.
    # 	 * @param   x  a point
    # 	 * @param   T  natural parameters \f$ \mathbf{\Theta} \f$
    # 	 * @return     \f$ f(x) = \exp \left( \langle \mathbf{\Theta} \ , \ t(x) \rangle - F(\mathbf{\Theta}) + k(x) \right) \f$
    # 	 
    def density(self, x, T):
        """ generated source for method density """
        return exp(T.InnerProduct(self.t(x)) - self.F(T) + self.k(x))

    # 
    # 	 * Computes the Bregman divergence between two members of a same exponential family.
    # 	 * @param   T1  natural parameters \f$ \mathbf{\Theta}_1\f$
    # 	 * @param   T2  natural parameters \f$ \mathbf{\Theta}_2\f$
    # 	 * @return      \f$ BD( \mathbf{\Theta_1} \| \mathbf{\Theta_2} ) = F(\mathbf{\Theta_1}) - F(\mathbf{\Theta_2}) - \langle \mathbf{\Theta_1} - \mathbf{\Theta_2} , \nabla F(\mathbf{\Theta_2}) \rangle \f$ 
    # 	 
    def BD(self, T1, T2):
        """ generated source for method BD """
        return self.F(T1) - self.F(T2) - self.gradF(T2).InnerProduct(T1.Minus(T2))

    # 
    # 	 * Computes the Kullback-Leibler divergence between two members of a same exponential family.
    # 	 * @param   LP  source parameters \f$ \mathbf{\Lambda}_P \f$
    # 	 * @param   LQ  source parameters \f$ \mathbf{\Lambda}_Q \f$
    # 	 * @return      \f$ D_{\mathrm{KL}}(f_P\|f_Q) \f$
    # 	 
    def KLD(self, LP, LQ):
        """ generated source for method KLD """

    # 
    # 	 * Computes the geodesic point.
    # 	 * @param   T1     natural parameters \f$ \mathbf{\Theta}_1\f$
    # 	 * @param   T2     natural parameters \f$ \mathbf{\Theta}_2\f$
    # 	 * @param   alpha  position \f$ \alpha \f$ of the point on the geodesic link
    # 	 * @return         \f$ \nabla G \left( (1-\alpha) \nabla F (\mathbf{\Theta}_1) + \alpha \nabla F (\mathbf{\Theta}_2) \right)  \f$
    # 	 
    def GeodesicPoint(self, T1, T2, alpha):
        """ generated source for method GeodesicPoint """
        return self.gradG((self.gradF(T1).Times(1.0 - alpha)).Plus(self.gradF(T2).Times(alpha)))

    # 
    # 	 * Draws a random point from the considered distribution.
    # 	 * @param   L  source parameters \f$ \mathbf{\Lambda}\f$
    # 	 * @return     a point
    # 	 
    def drawRandomPoint(self, L):
        """ generated source for method drawRandomPoint """

