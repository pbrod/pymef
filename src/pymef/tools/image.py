#!/usr/bin/env python
""" generated source for module Image """
from __future__ import print_function
# package: Tools
class Image(object):
    """ generated source for class Image """
    # 
    # 	 * Converts an image into a point set of dimension 3 (RGB)
    # 	 * @param   image  color image
    # 	 * @return         point set
    # 	 
    @classmethod
    def convertColorImageToPointSet3D(cls, image):
        """ generated source for method convertColorImageToPointSet3D """
        #  Variables
        width = image.getWidth()
        height = image.getHeight()
        nb_pixels = width * height
        points = [None] * nb_pixels
        #  Conversion
        row = 0
        while row < height:
            pass
            row += 1
        #  Return
        return points

    # 
    # 	 * Converts an image into a point set of dimension 5 (RGB + X + Y)
    # 	 * @param   image  color image
    # 	 * @return         point set
    # 	 
    @classmethod
    def convertColorImageToPointSet5D(cls, image):
        """ generated source for method convertColorImageToPointSet5D """
        #  Variables
        width = image.getWidth()
        height = image.getHeight()
        nb_pixels = width * height
        points = [None] * nb_pixels
        #  Conversion
        row = 0
        while row < height:
            pass
            row += 1
        #  Return
        return points

    # 
    # 	 * Segment an image using a mixture model.
    # 	 * @param  imgIn  input image
    # 	 * @param  mm     mixture model
    # 	 * @return        image segmentation
    # 	 
    @classmethod
    def segmentColorImageFromMOG(cls, imgIn, mm):
        """ generated source for method segmentColorImageFromMOG """
        #  Image initialization
        imgOut = BufferedImage(imgIn.getWidth(), imgIn.getHeight(), BufferedImage.TYPE_INT_RGB)
        #  Loop on pixels
        row = 0
        while row < imgIn.getHeight():
            pass
            row += 1
        #  Get the pixel
        #  Find and set the most probable class for the current point
        #  Return
        return imgOut

    # 
    # 	 * Reads an image.
    # 	 * @param  imagePath image file to read
    # 	 * @return           image
    # 	 
    @classmethod
    def readImage(cls, imagePath):
        """ generated source for method readImage """
        image_in = None
        try:
            image_in = ImageIO.read(File(imagePath))
        except IOError as e:
            e.printStackTrace()
            System.err.println("*** Error: Image file does not exist ***")
        return image_in

    # 
    # 	 * Writes an image.
    # 	 * @param image      image to be written
    # 	 * @param imagePath  image path
    # 	 
    @classmethod
    def writeImage(cls, image, imagePath):
        """ generated source for method writeImage """
        try:
            ImageIO.write(image, "png", File(imagePath))
        except IOError as e:
            e.printStackTrace()

    # 
    # 	 * Computes the PSNR between two images.
    # 	 * @param   i1  first image
    # 	 * @param   i2  second image
    # 	 * @return      PSNR(i1,i2)
    # 	 
    @classmethod
    def PSNR(cls, i1, i2):
        """ generated source for method PSNR """
        mse = 0
        r = 0
        while r < i1.getHeight():
            c = 0
            while c < i1.getWidth():
                c1 = Color(i1.getRGB(c, r))
                c2 = Color(i2.getRGB(c, r))
                dr = c1.getRed() - c2.getRed()
                dg = c1.getGreen() - c2.getGreen()
                db = c1.getBlue() - c2.getBlue()
                mse += dr * dr + dg * dg + db * db
                c += 1
            r += 1
        mse /= (i1.getHeight() * i1.getWidth() * 3)
        return 10 * log10((255 * 255) / mse)

    # 
    # 	 * Load a mixture model from a file. If the mixture doesn't exist, the function create
    # 	 * a mixture of multivariate Gaussians from the pixels of the image, and save this mixture.
    # 	 * @param   path  file-path of the mixture model
    # 	 * @param   image input image
    # 	 * @param   d     mixture dimension, must be 3 or 5
    # 	 * @param   n     number of components in the mixture model
    # 	 * @return        a mixture of Gaussian of dimension d and of n components computed from the input image
    # 	 
    @classmethod
    def loadMixtureModel(cls, path, image, d, n):
        """ generated source for method loadMixtureModel """
        if d != 3 and d != 5:
            raise RuntimeException("Only dimension 3 and 5 are supported.")
        mm = MixtureModel.load(path)
        if mm == None:
            px = cls.convertColorImageToPointSet3D(image) if d == 3 else cls.convertColorImageToPointSet5D(image)
            clusters = KMeans.run(px, n)
            mm = BregmanSoftClustering.initialize(clusters, MultivariateGaussian())
            mm = BregmanSoftClustering.run(px, mm)
            MixtureModel.save(mm, path)
        elif mm.getDimension() != d:
            raise RuntimeException("Incorrect dimension.")
        return mm

    # 
    # 	 * Counts the minimum number of points assigned to image pixel.
    # 	 * @param  tab    array
    # 	 * @param  height height of the array
    # 	 * @param  width  width of the array    
    # 	 * @return        minimum number of points
    # 	 
    @classmethod
    def min(cls, tab, height, width):
        """ generated source for method min """
        min = Integer.MAX_VALUE
        y = 0
        while y < height:
            pass
            y += 1
        return min

    # 
    # 	 * Creates an image from a mixture of Gaussians.
    # 	 * @param width  image width
    # 	 * @param height image height
    # 	 * @param mm     mixture model
    # 	 * @return       statistical image
    # 	 
    @classmethod
    def createImageFromMixtureModel(cls, width, height, mm):
        """ generated source for method createImageFromMixtureModel """
        imgOut = BufferedImage(width, height, BufferedImage.TYPE_INT_RGB)
        imgSum = [None] * height
        imgCpt = [None] * height
        n = 1024
        x = int()
        y = int()
        r = int()
        g = int()
        b = int()
        while cls.min(imgCpt, height, width) < 10:
            #  Draw point
            pixels = mm.drawRandomPoints(n)
            #  Fill the imgSum
            i = 0
            while i < n:
                y = int(pixels[i].array[3])
                x = int(pixels[i].array[4])
                if x >= 0 and y >= 0 and x < width and y < height:
                    r = int(pixels[i].array[0])
                    g = int(pixels[i].array[1])
                    b = int(pixels[i].array[2])
                    if r >= 0 and g >= 0 and b >= 0 and r < 255 and g < 255 and b < 255:
                        imgSum[y][x][0] += r
                        imgSum[y][x][1] += g
                        imgSum[y][x][2] += b
                        imgCpt[y][x] += 1
                i += 1
        while y < height:
            while x < width:
                r = int((imgSum[y][x][0] / imgCpt[y][x]))
                g = int((imgSum[y][x][1] / imgCpt[y][x]))
                b = int((imgSum[y][x][2] / imgCpt[y][x]))
                c = Color(r, g, b)
                imgOut.setRGB(x, y, c.getRGB())
                x += 1
            y += 1
        return imgOut

    @classmethod
    def createEllipseImage(cls, width, height, f, t):
        """ generated source for method createEllipseImage """
        imgOut = BufferedImage(width, height, BufferedImage.TYPE_INT_RGB)
        i = 0
        while i < f.size:
            mean = (f.param[i]).v.clone()
            c = Color(int(mean.array[0]), int(mean.array[1]), int(mean.array[2]))
            row = 0
            while row < height:
                pass
                row += 1
            i += 1
        return imgOut

