#!/bin/bash

set -euo pipefail

GH_ORG="infinite-sportsball"
GH_REPO="infinitesportsball.com"
DOM="infinitesportsball.com"
GH_URL="github.com"
DRY_RUN=""

if [ -z ${INFINITE_PELICAN_HOME+x} ]; then
	echo 'You must set the $INFINITE_PELICAN_HOME environment variable to proceed.'
	echo 'Try sourcing environment'
	exit 1
else
	echo "\$INFINITE_PELICAN_HOME is set to '$INFINITE_PELICAN_HOME'"
fi

if [[ $# -gt 0 ]]; then
    if [[ "$1" == "--dry-run" ]]; then
        DRY_RUN="--dry-run"
    else
        echo "Error: unrecognized argument provided."
        echo "Only valid input argument is --dry-run."
        exit 1;
    fi
fi

echo "Cloning repo ${GH_URL}/${GH_ORG}/${GH_REPO}"

(
cd ${INFINITE_PELICAN_HOME}
rm -fr output
git clone -b gh-pages git@${GH_URL}:${GH_ORG}/${GH_REPO}.git output

rm -fr output/*

while IFS= read -r universe; do
    [ -z "$universe" ] && continue
    echo "Generating pelican content for universe ${universe}..."
    (
    cd "${universe}"
    pelican content -o ../output/${universe}/
    )
done < UNIVERSES

echo "Copying landing page..."
cp index.html output/index.html

(
echo "Committing new content..."
cd output

git config user.name "Ch4zm of Hellmouth"
git config user.email "ch4zm.of.hellmouth@gmail.com"

echo $DOM > CNAME

git add -A .

git commit -a -m "Automatic deploy of infinite-sportsball at $(date -u +"%Y-%m-%d-%H-%M-%S")"

RESULT=$?
if [ $RESULT -eq 0 ]; then
    echo "Git commit step succeeded"
else
    echo "Git commit step failed"
    echo "Cleaning up"
    rm -fr output
    exit 1
fi

if [[ $DRY_RUN == "--dry-run" ]]; then
    echo "Skipping push step, --dry-run flag present"
else
    echo "Pushing to remote"
    git push origin gh-pages
fi
)

echo "Cleaning up"
rm -fr output
)
