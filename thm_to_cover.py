import argparse

import cv2
import numpy as np

cover_size = 800


def thm_to_cover(thm_file):
    """
    Youtube thumbnail to cover converter

    :param thm_file: Filename of thumbnail file
    """
    # Read image file
    thm = cv2.imread(thm_file, cv2.IMREAD_COLOR)
    if thm is None:
        print(f'Can NOT open \"{thm_file}\".')
        return None
    # If thumbnail is SD quality, crop unnecessary black border
    if (thm.shape[1], thm.shape[0]) == (640, 480):
        thm = thm[60:420, 0:thm.shape[1]]
    thm_width, thm_height = thm.shape[1], thm.shape[0]
    # Define back-end and front-end size
    be_shape = (int((thm_width*cover_size)/thm_height), cover_size)  # scale up
    fe_shape = (cover_size, int((thm_height*cover_size)/thm_width))  # scale down
    # Resize ,crop and blur back-end
    be = cv2.resize(thm, be_shape, interpolation=cv2.INTER_CUBIC)
    be = be[0:cover_size, int(be_shape[0]/2-cover_size/2): int(be_shape[0]/2+cover_size/2)]
    be = cv2.blur(be, (16, 16))
    # Resize front-end
    fe = cv2.resize(thm, fe_shape, interpolation=cv2.INTER_AREA)
    # Put front-end on back-end
    be[int(cover_size/2-fe_shape[1]/2): int(cover_size/2+fe_shape[1]/2), 0:cover_size] = fe

    # Save output file
    base_name = thm_file.split('.')[:-1]
    tail_name = thm_file.split('.')[-1]
    opt_file = '.'.join(base_name) + '_cover.' + tail_name
    cv2.imwrite(opt_file, be, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
    print(f'Image file \"{opt_file}\" saved.')


def parse_args():
    parser = argparse.ArgumentParser(
        prog='thm_to_cover', description='Thumbnail to cover converter')
    parser.add_argument('img', type=str, help='Image file')
    return parser.parse_args()


def main():
    args = parse_args()
    thm_to_cover(args.img)


if __name__ == '__main__':
    main()
