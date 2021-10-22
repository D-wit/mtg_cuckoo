# Copyright (C) 2017 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

from lib.common.abstracts import Package

class HWP(Package):
    """Hangul (Korean) Word Processor File 5.x analysis package."""
    PATHS = [
        ("ProgramFiles", "Hnc", "Hwp80", "Hwp.exe"),
        ("ProgramFiles", "Hnc", "HOffice9", "Bin", "Hwp.exe"),
        ("ProgramFiles", "HNC", "Office 2018", "HOffice100", "Bin", "Hwp.exe"),
        ("ProgramFiles", "Hnc", "Office NEO", "HOffice96", "Bin", "Hwp.exe"),
    ]

    def start(self, path):
        word = self.get_path("Hangul (Korean) Word Processor File 5.x")
        return self.execute(
            word, args=[path], mode="office", trigger="file:%s" % path
        )
