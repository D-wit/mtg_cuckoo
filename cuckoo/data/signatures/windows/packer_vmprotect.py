# Copyright (C) 2014 Jeremy Hedges
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from lib.cuckoo.common.abstracts import Signature

class VMPPacked(Signature):
    name = "packer_vmprotect"
    description = "The executable is likely packed with VMProtect"
    severity = 2
    categories = ["packer"]
    authors = ["Jeremy Hedges"]
    minimum = "2.0"
    ttp = ["T1027.002"]

    def on_complete(self):
        for section in self.get_results("static", {}).get("pe_sections", []):
            if section["name"].lower().startswith(".vmp"):
                self.mark(section=section["name"],
                          description="Section name indicates VMProtect")

        return self.has_marks()
