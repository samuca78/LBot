# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Init file which loads all of the modules """
from userbot import LOGS

import time

from pyUltroid import *
from pyUltroid.dB import *
from pyUltroid.dB.core import *
from pyUltroid.functions.all import *
from pyUltroid.functions.broadcast_db import *
from pyUltroid.functions.gban_mute_db import *
from pyUltroid.functions.goodbye_db import *
from pyUltroid.functions.google_image import googleimagesdownload
from pyUltroid.functions.sudos import *
from pyUltroid.functions.welcome_db import *
from pyUltroid.utils import *

from strings import get_string


def __list_all_modules():
    import glob
    from os.path import basename, dirname, isfile

    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    return [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]


ALL_MODULES = sorted(__list_all_modules())
LOGS.info("Módulos para carregar: %s", str(ALL_MODULES))
__all__ = ALL_MODULES + ["ALL_MODULES"]
