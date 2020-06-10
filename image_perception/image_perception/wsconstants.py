
# The color of the hex sectors
SECTOR_LINE_COLOR_LOWER = (79, 79, 79)
SECTOR_LINE_COLOR_UPPER = (115, 115, 115)

# The fraction of the screen that needs to match a line.
SECTOR_LINE_FRACTION = 0.15

# The distance allowed for the lines to be considered parallel lines in a hex
# This is necessary as it might be that the lines are not exactly the same distance depending on the screen.
MIN_DISTANCE_ALLOWANCE = 1.5

# Parameters for Hough hex line detection
HOUGH_LINES_THRESHOLD = 0
HOUGH_MIN_LINE_LENGTH = 10
HOUGH_MAX_LINE_GAP = 0
