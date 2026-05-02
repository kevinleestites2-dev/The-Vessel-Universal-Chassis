#!/usr/bin/env python3
"""
THE VESSEL (V1.0.0) - The Universal Prime Chassis
The 'Cathedral' for the Pantheon.
"""
import os, sys, time, json
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
class TheVessel:
    def __init__(self):
        self.version = "1.0.0-PROGENITOR"
        print(f"\n🏛️  The Cathedral is Open. Vessel V{self.version} Initialized.\n")

    def pulse(self):
        print(f"💓 Vessel Pulse: {datetime.utcnow().isoformat()}")

if __name__ == "__main__":
    TheVessel().pulse()
