import image_perception as img_p

if __name__ == "__main__":
    wsm = img_p.WhiteStarMap('../images/testMaps/WS_testImage_02.PNG')
    # wsm = img_p.WhiteStarMap('../images/testMaps/WS_testImage_01.PNG')
    wsm.detect_sectors()
    wsm.display_sectors()
