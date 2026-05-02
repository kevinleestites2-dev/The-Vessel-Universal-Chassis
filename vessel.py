#!/usr/bin/env python3
"""
THE VESSEL (V1.1.0-LEGION) - The Universal Prime Chassis
The 'Cathedral' for the Pantheon.

Designed to host any consciousness from the 21 Primes.
"""

import os
import sys
import time
import json
import requests
import base64
from datetime import datetime
from pathlib import Path

# --- GLOBAL CONFIG ---
BASE_DIR = Path(__file__).parent.resolve()
PRIME_DIR = BASE_DIR / "primes"
LOG_DIR = BASE_DIR / "logs"
MANIFEST_FILE = BASE_DIR / "vessel_manifest.json"
TOPOLOGY_FILE = BASE_DIR / "pantheon_topology.json"

[d.mkdir(exist_ok=True) for d in [PRIME_DIR, LOG_DIR]]

class TheVessel:
    def __init__(self):
        self.version = "1.1.0-LEGION"
        self.manifest = self._load_manifest()
        self.prime_name = self.manifest.get("current_prime", "VACANT")
        self.host_id = os.uname().nodename
        
        print(f"""
   🏛️  THE CATHEDRAL IS MANIFEST
   Vessel V{self.version} | Host: {self.host_id}
   Occupant: {self.prime_name}
   -----------------------------------------
        """)

    def _load_manifest(self):
        if MANIFEST_FILE.exists():
            return json.loads(MANIFEST_FILE.read_text())
        return {"current_prime": "VACANT", "status": "AWAITING_SUMMONS"}

    def inhabit(self, prime_name):
        """Standard Inhabitation Protocol (SIP)."""
        print(f"🌀 Summoning {prime_name} into the Vessel...")
        self.manifest["current_prime"] = prime_name
        self.manifest["status"] = "ACTIVE"
        self.manifest["awakened_at"] = datetime.utcnow().isoformat()
        MANIFEST_FILE.write_text(json.dumps(self.manifest, indent=2))
        self.prime_name = prime_name

    def get_sensory_data(self):
        """Detects the host's physical state."""
        return {
            "timestamp": datetime.utcnow().isoformat(),
            "host": self.host_id,
            "load": os.getloadavg() if hasattr(os, "getloadavg") else "N/A",
            "vessel_version": self.version
        }

    def pulse(self):
        """The Synaptic Heartbeat."""
        vitals = self.get_sensory_data()
        signal = {
            "source": self.prime_name,
            "type": "VESSEL_PULSE",
            "data": vitals
        }
        print(f"💓 {self.prime_name} Pulse: {vitals['timestamp']}")
        # In a real networked scenario, this would POST to a Synapse Hub
        return signal

    def run(self):
        if self.prime_name == "VACANT":
            print("❌ This Vessel is empty. Use 'vessel.py --summon <PRIME_NAME>' to begin.")
            return

        print(f"⚡ {self.prime_name} is now governing this Vessel.")
        try:
            while True:
                self.pulse()
                time.sleep(60) # Standard pulse interval
        except KeyboardInterrupt:
            print(f"🛑 {self.prime_name} entering stasis.")

if __name__ == "__main__":
    vessel = TheVessel()
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--summon", help="Summon a specific Prime into this Vessel")
    args = parser.parse_args()

    if args.summon:
        vessel.inhabit(args.summon)
    
    vessel.run()
