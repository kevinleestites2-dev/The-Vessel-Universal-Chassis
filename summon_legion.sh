#!/bin/bash
# THE SUMMONING OF THE LEGION
# Usage: ./summon_legion.sh <PRIME_NAME>

PRIME=$1

if [ -z "$PRIME" ]; then
    echo "Usage: ./summon_legion.sh <PRIME_NAME>"
    exit 1
fi

echo "🏛️ Initializing Vessel for $PRIME..."
python3 vessel.py --summon $PRIME
