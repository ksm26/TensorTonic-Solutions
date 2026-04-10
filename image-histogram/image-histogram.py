from collections import Counter
def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    listt = [0]*256
    list2 = []
    for row in image :
        for i in row:
            list2.append(i)
            
    dictionary = Counter(list2)

    for i in range(len(listt)):
        if i in dictionary:
            listt[i] = dictionary[i]

    return listt
    