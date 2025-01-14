#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get(
        "MicrosoftAppId", "d4e4e963-7b15-4704-8911-1445ce0cba60")
    APP_PASSWORD = os.environ.get(
        "MicrosoftAppPassword", "U048Q~wYG5_~uuhrKLKY1_L10P.g6f.qryPYqaHw")
