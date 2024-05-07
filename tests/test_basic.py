# SPDX-FileCopyrightText: 2024 Vladimir Kotal
#
# SPDX-License-Identifier: Unlicense

import time

from adafruit_ticks import ticks_ms, ticks_less


def test_basic():
    deadline = ticks_ms()
    time.sleep(1)
    print(ticks_less(ticks_ms(), deadline))
