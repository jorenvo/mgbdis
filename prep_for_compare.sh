#!/usr/bin/env bash
set -eou pipefail

INPUT="${1}"

grep -hv '^$' "${INPUT}" |\
    grep -v ':$'
