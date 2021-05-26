#!/usr/bin/env python
""" generated source for module Tutorial4 """
from __future__ import print_function
# package: Tutorials
class Tutorial4(object):
    """ generated source for class Tutorial4 """
    # 
    # 	 * Main function.
    # 	 * @param args
    # 	 
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        #  Display
        title = ""
        title += "+----------------------------------------------------+\n"
        title += "| Hierarchical mixture models and image segmentation |\n"
        title += "+----------------------------------------------------+\n"
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
        print("Read input image                           : ", end="")
        image = Image.readImage(image_path)
        print("ok")
        #  Read or generate the mixture model
        print("Read/generate mixture model                : ", end="")
        mm1 = Image.loadMixtureModel(mixture_path, image, 3, n)
        print("ok")
        #  Initial segmentation from MoG
        print("Segment image (mixture model, end="")              : ")
        seg1 = Image.segmentColorImageFromMOG(image, mm1)
        Image.writeImage(seg1, "{:s}Tutorial4_{:s}_{:03d}.png".format(output_folder, image_name, n))
        print("ok")
        #  Build hierarchical mixture model
        print("Create hierarchical mixture model          : ", end="")
        hmm = BregmanHierarchicalClustering.build(mm1, CLUSTERING_TYPE.SYMMETRIC, LINKAGE_CRITERION.MAXIMUM_DISTANCE)
        print("ok")
        #  Initial segmentation from simplified MoG
        print("Segment image (hierarchical mixture model, end="") : ")
        mm2 = hmm.getResolution(m)
        # MixtureModel  mm2  = hmm.getOptimalMixtureModel(0.5);
        seg2 = Image.segmentColorImageFromMOG(image, mm2)
        Image.writeImage(seg2, "{:s}Tutorial4_{:s}_{:03d}.png".format(output_folder, image_name, m))
        print("ok")


if __name__ == '__main__':
    import sys
    Tutorial4.main(sys.argv)

