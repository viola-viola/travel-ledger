from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from travel_ledger.cli import main
from travel_ledger.models import Note, ProjectState, Task


class ProjectSmokeTests(unittest.TestCase):
    def test_cli_help(self) -> None:
        self.assertEqual(main([]), 0)


if __name__ == "__main__":
    unittest.main()
