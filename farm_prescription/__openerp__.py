# -*- encoding: utf-8 -*-
##############################################################################
#
#    @authors: Alexander Ezquevo <alexander@acysos.com>
#    Copyright (C) 2015  Acysos S.L.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Farm medication Prescription",
    "version": "1.0",
    "license": "AGPL-3",
    "author": "Acysos S.L.",
    "website": "www.acysos.com",
    "contributors": ['Alexander Ezquevo alexander@acysos.com', ],
    "images": [],
    "category": "Specific industry",
    "depends": [
        "farm",
        "product",
        "base",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/prescription_sequence.xml",
        "views/prescription.xml",
        "reports/prescription_report.xml",
        "views/farm_menu.xml",
    ],
    "installable": True,
}
