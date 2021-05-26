#!/usr/bin/env python
""" generated source for module Tutorial3 """
from __future__ import print_function
# package: Tutorials
class Tutorial3(object):
    """ generated source for class Tutorial3 """
    # 
    # 	 * Main function.
    # 	 * @param args
    # 	 
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        #  Display
        title = ""
        title += "+-----------------------------------------------+\n"
        title += "| Mixture simplification and image segmentation |\n"
        title += "+-----------------------------------------------+\n"
        print(title, end="")
        #  Variables
        n = 32
        m = 8
        #  Image/texture information (to be changed to fit your configuration)
        input_folder = "/Users/vincent/Documents/jMEF/input/"
        output_folder = "/Users/vincent/Documents/jMEF/output/"
        image_name = "Baboon"
        image_path = input_folder + image_name + ".png"
        mixture_path = "{:s}{:s}_3D_{:03d}.mix".format(input_folder, image_name, n)
        #  Read the input image
        print("Read input image                         : ", end="")
        image = Image.readImage(image_path)
        print("ok")
        #  Read or generate the mixture model
        print("Read/generate mixture model              : ", end="")
        mm1 = Image.loadMixtureModel(mixture_path, image, 3, n)
        print("ok")
        #  Compute the image segmentation based on the mixture mm1
        print("Segment image (mixture model, end="")            : ")
        seg1 = Image.segmentColorImageFromMOG(image, mm1)
        Image.writeImage(seg1, "{:s}Tutorial3_{:s}_{:03d}.png".format(output_folder, image_name, n))
        print("ok")
        #  Simplify mm1 in a mixture mm2 of m components and compute the image segmentation based on mm2
        print("Segment image (simplified mixture model, end="") : ")
        mm2 = BregmanHardClustering.simplify(mm1, m, CLUSTERING_TYPE.LEFT_SIDED)
        seg2 = Image.segmentColorImageFromMOG(image, mm2)
        Image.writeImage(seg2, "{:s}Tutorial3_{:s}_{:03d}.png".format(output_folder, image_name, m))
        print("ok")


if __name__ == '__main__':
    import sys
    Tutorial3.main(sys.argv)

