from PIL import Image

img = Image.open("img.jpg")
def scale(image, sx, sy):
    """Scale image by factors sx, sy"""
    width, height = image.size
    new_width = int(width * sx)
    new_height = int(height * sy)
    return image.resize((new_width, new_height), Image.Resampling.LANCZOS)

# 3. Rotation using PIL's rotate (Multiple options)
def rotate(image, angle, expand_canvas=True):
    """Rotate image by angle degrees with option to expand canvas"""
    if expand_canvas:
        # Expand canvas to fit entire rotated image
        return image.rotate(angle, expand=True, fillcolor='white')
    else:
        # Keep original size, may crop parts of image
        return image.rotate(angle, expand=False, fillcolor='white')

def rotate_with_center(image, angle):
    """Rotate image around its center with expanded canvas"""
    return image.rotate(angle, expand=True, fillcolor='white', center=None)


def flip_horizontal(image):
    """Flip image horizontally"""
    return image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

def flip_vertical(image):
    """Flip image vertically"""
    return image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)



def rotate_90_cw(image):
    """Rotate 90 degrees clockwise"""
    return image.transpose(Image.Transpose.ROTATE_90)

def rotate_90_ccw(image):
    """Rotate 90 degrees counter-clockwise"""
    return image.transpose(Image.Transpose.ROTATE_270)

def rotate_180(image):
    """Rotate 180 degrees"""
    return image.transpose(Image.Transpose.ROTATE_180)

def perspective_transform(image, coeffs):
    """Apply perspective transformation"""
    return image.transform(image.size, Image.Transform.PERSPECTIVE, 
                          coeffs, fillcolor='white')


scaled = scale(img, 1.5, 1.5)
scaled.show()
rotated_expanded = rotate(img, 45, expand_canvas=True)  # Full image visible, larger canvas
rotated_cropped = rotate(img, 45, expand_canvas=False)  # Same size, may crop image
  # Fits within original size
    
flipped_h = flip_horizontal(img)
flipped_v = flip_vertical(img)

rotated_expanded.show(title="Rotated 45° - Expanded Canvas")
rotated_cropped.show(title="Rotated 45° - Cropped to Original Size")

flipped_h.show(title="Flipped Horizontal")
flipped_v.show(title="Flipped Vertical")


rotated_90_cw = rotate_90_cw(img)
rotated_90_ccw = rotate_90_ccw(img)
rotated_180 = rotate_180(img)

rotated_90_cw.show(title="Rotated 90° Clockwise")
rotated_90_ccw.show(title="Rotated 90° Counter-Clockwise")
rotated_180.show(title="Rotated 180°")
perspective_img.show(title="Perspective Transform")
