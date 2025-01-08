def jpeg_res(file_path):
    # Open the image file in binary mode
    with open(file_path, 'rb') as img_file:
        # Read file content to locate resolution information
        img_file.seek(163)  # Skip to the resolution bytes
        # Read the height and width values
        a = img_file.read(2)
        height = (a[0] << 8) + a[1]
        a = img_file.read(2)
        width = (a[0] << 8) + a[1]
    print("The resolution of the image is", width, "x", height)

# Test the function with the image file name
jpeg_res("img1.jpg")
