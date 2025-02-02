# sql/future/__init__.py
# Copyright (C) 2005-2021 the SQLAlchemy authors and contributors
# <see AUTHORS file>
#
# This module is part of SQLAlchemy and is released under
# the MIT License: https://www.opensource.org/licenses/mit-license.php

"""Future 2.0 API features.

"""
from .engine import Connection
from .engine import create_engine
from .engine import Engine
from ..sql.selectable import Select
from ..util.langhelpers import public_factory


select = public_factory(Select._create, ".future.select")
