#!/bin/sh

source ./scripts/restart_dma

python3 ./scripts/flits_sender.py ./chip_test/reset_clock/default_clock.bin
python3 ./scripts/flits_sender.py ./chip_test/reset_clock/pll_clock.bin