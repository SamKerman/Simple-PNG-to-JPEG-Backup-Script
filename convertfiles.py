import os
from os.path import join, exists, dirname, relpath
from cv2 import imread, imwrite, IMWRITE_JPEG_QUALITY
from shutil import copystat
import argparse

def convert_image(source_path, dest_path):
    if exists(dest_path) == False:
        #Convert to JPG
        print("Conververting from ", source_path, " to ", dest_path)
        image = imread(source_path)
        image_jpg = imwrite(dest_path, image, [int(IMWRITE_JPEG_QUALITY), 87])  #Compresses to jpeg with a quality of 87%
        copystat(source_path, dest_path) #Copies metadata to the new jpeg in order to preserve the date and such.
    else:
        print(dest_path, " already exists! Skipping this file.")

def copy_and_convert(source_dir, dest_dir):
    for dirpath, dirnames, filenames in os.walk(source_dir):
        for filename in filenames:
            if filename.endswith('.png'):
                source_path = join(dirpath, filename)
                dest_path = join(dest_dir, relpath(dirpath, source_dir), filename[:-4] + ".jpg")
                os.makedirs(dirname(dest_path), exist_ok = True)
                convert_image(source_path, dest_path)
                
    print("Done!")

def main():
    #Get arguments in command line for source and distination directory
    parser = argparse.ArgumentParser() 
    parser.add_argument('source', type=str)
    parser.add_argument('destination', type=str)
    args = parser.parse_args()
    copy_and_convert(args.source, args.destination)

if __name__ == "__main__":
    main()