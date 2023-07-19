#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#
# PROGRAMMER: Joshua Shabo
# DATE CREATED: 16/07/2023
# REVISED DATE: 19/07/2023
# PURPOSE: Create a function that retrieves the following 3 command line inputs
#          from the user using the Argparse Python module. If the user fails to
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
import argparse
import os

def valid_dir(path):
    if not os.path.isdir(path):
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")
    if os.access(path, os.R_OK):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a readable dir")

def valid_file(path):
    if not os.path.isfile(path):
        raise argparse.ArgumentTypeError(f"{path} is not a valid file")
    if os.access(path, os.R_OK):
        return path
    else:
        raise argparse.ArgumentTypeError(f"{path} is not readable")

def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's
    argparse module to created and defined these 3 command line arguments. If
    the user fails to provide some or all of the 3 arguments, then the default
    values are used for the missing arguments.
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object
    """

    parser = argparse.ArgumentParser(prog="CNN Image Classifier")

    parser.add_argument('--dir', help = 'a valid path to the folder of pet images', default = 'pet_images/', type = valid_dir)
    parser.add_argument('--dogfile', help = 'a valid path to the file containing dognames', default = 'dognames.txt', type = valid_file)
    parser.add_argument('--arch', help = 'the CNN model architecture for the classifier', default = 'vgg', choices = ['vgg', 'alexnet', 'resnet'])

    return parser.parse_args()
