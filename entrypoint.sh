#!/bin/bash
#
# SPDX-License-Identifier: Apache-2.0
#
# Usage: $ ./entrypoint.sh

set -e

# if [[ -z "${MODEL_PATH}" ]]; then
#   rasa run actions --port "5055" --debug
# fi

rasa run --model ${MODEL_PATH} --enable-api --cors "*" --port "5005" --debug