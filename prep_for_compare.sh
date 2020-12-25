#!/usr/bin/env bash
set -eou pipefail

INPUT="${1}"

grep -hv '^$' "${INPUT}" |\
    grep -v ':$' |\
    sed 's/LD\(.*$0xff00+.*\)/LDH\1/'
