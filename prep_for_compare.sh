#!/usr/bin/env bash
set -eou pipefail

INPUT="${1}"

grep -hv '^$' "${INPUT}" |\
    grep -v ':$' |\
    sed 's/RST $\(.*\)/RST $0x\1/' |\
    sed 's/LD\(.*$0xff00+.*\)/LDH\1/'
