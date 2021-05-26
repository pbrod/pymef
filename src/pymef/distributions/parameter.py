#!/usr/bin/env python
""" generated source for module Parameter """
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
#  * A statistical distribution is parameterized by a set of values (parameters).
#  * The Parameter class implements a parameter object.
#  * Parameters can be a vector (class PVector), a matrix (class PMatrix), or both (class PVectorMatrix).
#  * The Parameter class is an abstract class.
#
class Parameter(Serializable):
    """ generated source for class Parameter """
    #
    # 	 * Constant for serialization.
    #
    serialVersionUID = 1

    #
    # 	 * Type of the parameters: source parameters, natural parameters, or expectation parameters.
    #
    class TYPE:
        """ generated source for enum TYPE """
        SOURCE_PARAMETER = u'SOURCE_PARAMETER'
        NATURAL_PARAMETER = u'NATURAL_PARAMETER'
        EXPECTATION_PARAMETER = u'EXPECTATION_PARAMETER'

    #
    # 	 * Type of the parameters.
    #
    type_ = None

    #
    # 	 * Class constructor. By default, a parameter object corresponds to source parameters.
    #
    def __init__(self):
        """ generated source for method __init__ """
        super(Parameter, self).__init__()
        self.type_ = self.TYPE.SOURCE_PARAMETER

    #
    # 	 * Adds (not in place) the current parameter p to the parameter q.
    # 	 * @param   q  parameter
    # 	 * @return     p+q
    #
    def Plus(self, q):
        """ generated source for method Plus """

    #
    # 	 * Subtracts (not in place) the parameter q to the current parameter p.
    # 	 * @param   q  parameter
    # 	 * @return     p-q
    #
    def Minus(self, q):
        """ generated source for method Minus """

    #
    # 	 * Multiplies (not in place) the current parameter p by a real number \f$ \lambda \f$.
    # 	 * @param  lambda  value \f$ \lambda \f$
    # 	 * @return         \f$ \lambda p \f$
    #
    def Times(self, lambda_):
        """ generated source for method Times """

    #
    # 	 * Computes the inner product (real number) between the current parameter p and the parameter q.
    # 	 * @param   q  parameter
    # 	 * @return     \f$ \langle p , q \rangle \f$
    #
    def InnerProduct(self, q):
        """ generated source for method InnerProduct """

    #
    # 	 * Creates and returns a copy of the instance.
    # 	 * @return a clone of the instance.
    #
    def clone(self):
        """ generated source for method clone """

    #
    # 	 * Returns the dimension of the parameters.
    # 	 * @return parameters' dimension.
    #
    def getDimension(self):
        """ generated source for method getDimension """

