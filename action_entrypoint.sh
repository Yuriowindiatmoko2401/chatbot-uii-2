#!/bin/bash
#
# SPDX-License-Identifier: Apache-2.0
#
# Usage: $ ./entrypoint.sh

set -e

rasa run actions --port "5055" --debug
