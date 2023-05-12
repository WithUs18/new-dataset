import os,sys
from PIL import Image

def resize_and_crop(img_path, modified_path, size, crop_type='middle'):
    """
    Resize and crop an image to fit the specified size.

    args:
        img_path: path for the image to resize.
        modified_path: path to store the modified image.
        size: `(width, height)` tuple.
        crop_type: can be 'top', 'middle' or 'bottom', depending on this
            value, the image will cropped getting the 'top/left', 'middle' or
            'bottom/right' of the image to fit the size.
    raises:
        Exception: if can not open the file in img_path of there is problems
            to save the image.
        ValueError: if an invalid `crop_type` is provided.
    """
    # If height is higher we resize vertically, if not we resize horizontally
    img = Image.open(img_path)
    # Get current and desired ratio for the images
    img_ratio = img.size[0] / float(img.size[1])
    ratio = size[0] / float(size[1])
    #The image is scaled/cropped vertically or horizontally depending on the ratio
    if ratio > img_ratio:
        img = img.resize((size[0], round(size[0] * img.size[1] / img.size[0])),
                Image.ANTIALIAS)
        # Crop in the top, middle or bottom
        if crop_type == 'top':
            box = (0, 0, img.size[0], size[1])
        elif crop_type == 'middle':
            box = (0, round((img.size[1] - size[1]) / 2), img.size[0],
                   round((img.size[1] + size[1]) / 2))
        elif crop_type == 'bottom':
            box = (0, img.size[1] - size[1], img.size[0], img.size[1])
        else :
            raise ValueError('ERROR: invalid value for crop_type')
        img = img.crop(box)
    elif ratio < img_ratio:
        img = img.resize((round(size[1] * img.size[0] / img.size[1]), size[1]),
                Image.ANTIALIAS)
        # Crop in the top, middle or bottom
        if crop_type == 'top':
            box = (0, 0, size[0], img.size[1])
        elif crop_type == 'middle':
            box = (round((img.size[0] - size[0]) / 2), 0,
                   round((img.size[0] + size[0]) / 2), img.size[1])
        elif crop_type == 'bottom':
            box = (img.size[0] - size[0], 0, img.size[0], img.size[1])
        else :
            raise ValueError('ERROR: invalid value for crop_type')
        img = img.crop(box)
    else :
        img = img.resize((size[0], size[1]),
                Image.ANTIALIAS)
        # If the scale is the same, we do not need to crop
    img.save(modified_path)


"""
* img_path, modified_path 경로명 꼭 각자의 경로명, 파일명에 맞게 수정하기 (가장 중요)
* 만약 중간에 에러 나면 확장자 .jpg 맞는지 확인하기
"""

"""
# case 1. 하나씩 바꾸고 싶은 경우
img_path = "C:\\Users\\yjh97\\Desktop\\appleOrigin\\apple001.jpg" 
modified_path = "C:\\Users\\yjh97\\Desktop\\appleResize\\apple001.jpg" 
size = (416, 416) 
resize_and_crop(img_path, modified_path, size)
"""

# case 2. 여러 개를 한 번에 바꾸고 싶은 경우
start = 1
end = 151
size = (416, 416) 
for filenum in range(start, end):
    if len(str(filenum)) == 1:
        img_path = "C:\\Users\\yjh97\\Desktop\\appleOrigin\\apple00" + str(filenum) +".jpg"
        modified_path = "C:\\Users\\yjh97\\Desktop\\appleResize\\apple00" + str(filenum) +".jpg"
    elif len(str(filenum)) == 2:
        img_path = "C:\\Users\\yjh97\\Desktop\\appleOrigin\\apple0" + str(filenum) +".jpg"
        modified_path = "C:\\Users\\yjh97\\Desktop\\appleResize\\apple0" + str(filenum) +".jpg"
    elif len(str(filenum)) == 3:
        img_path = "C:\\Users\\yjh97\\Desktop\\appleOrigin\\apple" + str(filenum) +".jpg"
        modified_path = "C:\\Users\\yjh97\\Desktop\\appleResize\\apple" + str(filenum) +".jpg"
    else:
        print("파일명과 확장자  확인했나요~?")
        break
    resize_and_crop(img_path, modified_path, size)
