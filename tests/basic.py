# SPDX-FileCopyrightText: 2024 Vladimir Kotal
#
# SPDX-License-Identifier: Unlicense

import time

import adafruit_ticks


def test_basic():
    deadline = ticks_ms()
    time.sleep(1)
    print(ticks_less(ticks_ms(), deadline))
