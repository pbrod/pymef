#!/usr/bin/env python
""" generated source for module Tutorial5 """
from __future__ import print_function
# package: Tutorials
class Tutorial5(object):
    """ generated source for class Tutorial5 """
    # 
    # 	 * Main function.
    # 	 * @param args
    # 	 
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        #  Display
        title = ""
        title += "+----------------------------------------+\n"
        title += "| Statistical images from mixture models |\n"
        title += "+----------------------------------------+\n"
        print(title, end="")
        #  Variables
        n = 32
        #  Image/texture information (to be changed to fit your configuration)
        input_folder = "/Users/vincent/Documents/jMEF/input/"
        output_folder = "/Users/vincent/Documents/jMEF/output/"
        image_name = "Baboon"
        image_path = input_folder + image_name + ".png"
        mixture_path = "{:s}{:s}_5D_{:03d}.mix".format(input_folder, image_name, n)
        #  Read the input image
        print("Read input image             : ", end="")
        image = Image.readImage(image_path)
        print("ok")
        #  Read or generate the mixture model
        print("Read/generate mixture model  : ", end="")
        f = Image.loadMixtureModel(mixture_path, image, 5, n)
        print("ok")
        #  Creates and save the statistical image
        print("Create statistical image     : ", end="")
        stat = Image.createImageFromMixtureModel(image.getWidth(), image.getHeight(), f)
        Image.writeImage(stat, "{:s}Tutorial5_{:s}_statistical_{:03d}.png".format(output_folder, image_name, n))
        print("ok")
        #  Creates and save the ellipse image
        print("Create ellipse image         : ", end="")
        ell = Image.createEllipseImage(image.getWidth(), image.getHeight(), f, 2)
        Image.writeImage(ell, "{:s}Tutorial5_{:s}_ellipses_{:03d}.png".format(output_folder, image_name, n))
        print("ok")


if __name__ == '__main__':
    import sys
    Tutorial5.main(sys.argv)

