"""Initialization of the whole game. Finding a path to this package and appending it to the PYTHONPATH variable"""

import os
import sys

path_to_package = os.path.dirname(__file__)
sys.path.append(path_to_package)

from app.utils.constants import Constants

Constants.PACKAGE_PATH = path_to_package
