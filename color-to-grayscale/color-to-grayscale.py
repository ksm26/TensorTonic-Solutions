def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here
    result =[]

    for i in range(len(image)):
        row = []
        for j in  range(len(image[i])) :
            R,G,B = image[i][j][0],  image[i][j][1], image[i][j][2]
            Y = 0.299 * R + 0.587 * G + 0.114 * B
            row.append(Y)
        result.append(row)

    return result