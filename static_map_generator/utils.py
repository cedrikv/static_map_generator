from shapely.wkt import loads
from wand.exceptions import WandException
from wand.image import Image

def combine_layers(images, filename):
    combo = None
    for index, im in enumerate(images):
        if not isinstance(combo, Image):
            combo = Image(filename=im)
        if index == len(images) - 1:
            break
        else:
            im2 = images[index + 1]
            im2 = Image(filename=im2)
            combo.composite(im2, left=0, top=0)
    combo.save(filename=filename)
    combo.close()

# def combine_layers(images):
# from PIL import Image as PILImage
#     combo = None
#     for index,im in enumerate(images):
#         if not combo:
#             combo = PILImage.open(im) if isinstance(im, str) else im
#             combo = combo.convert(mode='RGBA')
#         if index == len(images)-1:
#             break
#         else:
#             im2 = images[index+1]
#             im2 = PILImage.open(im2) if isinstance(im2, str) else im2
#             im2 = im2.convert(mode='RGBA')
#             combo = PILImage.alpha_composite(combo, im2)
#
#     combo.save("result.png")


def create_buffer(wkt, buffer):
    geom = loads(wkt)
    return geom.buffer(buffer)


def merge_dicts(*dict_args):
    '''
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    '''
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


def convert_filetype(filename_ori, filename_res, filetype):
    try:
        original = Image(filename=filename_ori)
        with original.convert(filetype) as converted:
            converted.save(filename=filename_res)
    except WandException as e:  # pragma: no cover
        pass
