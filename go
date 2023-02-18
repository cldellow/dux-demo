#!/bin/bash

set -euo pipefail

datasette --metadata metadata.json cooking.db superuser.db --template-dir templates
