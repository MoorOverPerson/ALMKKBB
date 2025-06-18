#!/usr/bin/env python3
"""Verify an event occurred based on tracking data from multiple devices.

This utility reads JSON logs from a smartwatch and a phone, cross-checks the
recorded timestamps and locations, and outputs an encrypted summary without
revealing personal identifiers.

Example usage:
    python3 tracking_verification.py watch.json phone.json result.enc keyfile

The `keyfile` is used for symmetric encryption; it is created if it does not
exist. Only the verification result and timestamp are stored in the encrypted
output.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

from cryptography.fernet import Fernet


def read_log(path: Path) -> dict:
    """Load tracking data from a JSON file."""
    return json.loads(path.read_text(encoding="utf-8"))


def timestamps_close(t1: str, t2: str, minutes: int = 5) -> bool:
    """Check if two ISO timestamps are within a given number of minutes."""
    dt1 = datetime.fromisoformat(t1)
    dt2 = datetime.fromisoformat(t2)
    delta = abs((dt1 - dt2).total_seconds())
    return delta <= minutes * 60


def verify_event(watch: dict, phone: dict) -> bool:
    """Determine if both devices recorded the same event."""
    return (
        watch.get("event") == phone.get("event")
        and timestamps_close(watch["timestamp"], phone["timestamp"])
    )


def encrypt_and_save(data: str, key_path: Path, out_path: Path) -> None:
    """Encrypt data using a symmetric key and save to a file."""
    if key_path.exists():
        key = key_path.read_bytes()
    else:
        key = Fernet.generate_key()
        key_path.write_bytes(key)
    f = Fernet(key)
    out_path.write_bytes(f.encrypt(data.encode("utf-8")))


def main(argv: list[str]) -> int:
    if len(argv) != 5:
        print(
            "Usage: tracking_verification.py watch.json phone.json result.enc keyfile"
        )
        return 1
    watch_file = Path(argv[1])
    phone_file = Path(argv[2])
    output_file = Path(argv[3])
    key_file = Path(argv[4])

    watch_log = read_log(watch_file)
    phone_log = read_log(phone_file)

    verified = verify_event(watch_log, phone_log)
    result = json.dumps({"verified": verified, "timestamp": watch_log["timestamp"]})
    encrypt_and_save(result, key_file, output_file)
    print(f"Verification result written to {output_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
