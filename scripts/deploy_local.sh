#!/bin/bash

set -euo pipefail

if [ -z ${INFINITE_PELICAN_HOME+x} ]; then
	echo 'You must set the $INFINITE_PELICAN_HOME environment variable to proceed.'
	echo 'Try sourcing environment'
	exit 1
else
	echo "\$INFINITE_PELICAN_HOME is set to '$INFINITE_PELICAN_HOME'"
fi

(
cd ${INFINITE_PELICAN_HOME}
rm -fr output

while IFS= read -r universe; do
    [ -z "$universe" ] && continue
    echo "Generating pelican content for universe ${universe}..."
    (
    cd "${universe}"
    pelican content -o ../output/${universe}/
    )
done < UNIVERSES

echo "Copying landing page and favicon..."
cp index.html output/index.html
cp favicon.ico output/favicon.ico

(
cd output
python -m http.server 8888
)
)
