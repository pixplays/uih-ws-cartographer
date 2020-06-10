from os import path
import imghdr
import cv2
import numpy as np
import math
from . import wsconstants
import copy

class WhiteStarMap:
    """
    Loads a screenshot and performs operations on it
    """
    def __init__(self, screenshot_filename):
        # Check the file exists.
        if not path.exists(screenshot_filename):
            raise FileNotFoundError("Image file %s does not exist" % screenshot_filename)
        # Check the file is an image.
        self.image_type = imghdr.what(screenshot_filename)
        if not self.image_type in self.supported_formats():
            raise IOError("Image type '%s' not supported" % self.image_type)
        self.screenshot_filename = screenshot_filename
        self.image = cv2.imread(self.screenshot_filename, cv2.IMREAD_COLOR)

    # Returns a set of supported formats
    def supported_formats(self):
        return set(["png", "jpg", "jpeg"])

    def display_window(self, image_to_display):
        cv2.imshow('image', image_to_display)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def display(self):
        self.display_window(self.image)
        
    def display_sectors(self):
        self.display_window(self.sector_image)
        
    def detect_sectors(self):
        '''
        This function uses some assumptions to make a cheap way to extract sectors.
        These assumptions are:
          * The lines of the hexagons are always the same color
          * The hexagons are always aligned so that two sides are exactly horizontal
        This approach is taken to be a very light weight way to extract sectors, though may be fragile.
        '''
        # Get all pixels within the expected ranges.
        mask = cv2.inRange(self.image, wsconstants.SECTOR_LINE_COLOR_LOWER,
                           wsconstants.SECTOR_LINE_COLOR_UPPER)
        # Detect lines horizontal, or at 30 and 150 degrees rotation.
        lines = [ x[0] for x in cv2.HoughLinesP(mask, 1, np.pi/6,
                                                wsconstants.HOUGH_LINES_THRESHOLD,
                                                wsconstants.HOUGH_MIN_LINE_LENGTH,
                                                wsconstants.HOUGH_MAX_LINE_GAP) if x is not None]
        self.sector_image = copy.deepcopy(self.image)
        for x1,y1,x2,y2 in lines:
            print( (x1,y1), (x2,y2) )
            cv2.line(self.sector_image, (x1,y1), (x2,y2), (0,0,255), 2)
