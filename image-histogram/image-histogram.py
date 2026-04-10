from collections import Counter
def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    listt = [0]*256
    list2 = []
    for row in image :
        for pixel in row:
            listt[pixel]+= 1
            
    return listt
    