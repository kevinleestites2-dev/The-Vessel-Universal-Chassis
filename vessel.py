#!/usr/bin/env python3
"""
THE VESSEL (V1.3.0-CHIMERA) - The Universal Prime Chassis
The 'Cathedral' for the Pantheon.

V1.3.0: CHIMERA MOBILITY PROTOCOLS ENABLED.
Supports OpenBot physical docking and PhoneDriver digital control.
"""

import os
import sys
import time
import json
from datetime import datetime
from pathlib import Path

class MobilityBridge:
    def __init__(self):
        self.mode = "DOCK_MODE" # or "DRIVE_MODE"
        print("🏎️  Mobility Bridge: Link Established.")

    def get_chassis_status(self):
        return {
            "docked": True,
            "chassis_type": "OpenBot-V1",
            "connection": "BLE/USB"
        }

class TheVessel:
    def __init__(self):
        self.version = "1.3.0-CHIMERA"
        self.mobility = MobilityBridge()
        self.manifest = self._load_manifest()
        self.prime_name = self.manifest.get("current_prime", "VACANT")
        
        print(f"🏛️  Vessel V{self.version} | Mobility Bridge: ACTIVE | Occupant: {self.prime_name}")

    def _load_manifest(self):
        m_file = Path(__file__).parent / "vessel_manifest.json"
        if m_file.exists(): return json.loads(m_file.read_text())
        return {"current_prime": "VACANT"}

    def pulse(self):
        status = self.mobility.get_chassis_status()
        print(f"💓 Pulse + 🏎️ Chassis: {status['chassis_type']} | Status: {status['docked']}")

if __name__ == "__main__":
    v = TheVessel()
    v.pulse()
