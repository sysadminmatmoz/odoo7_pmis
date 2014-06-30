# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Didotech Srl - OpenERP 7 migration by Matmoz d.o.o. 
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Base Localization',
    'version': '2.0.0.1',
    'category': 'Localization',
    'description': """Localization module - Base version

Features:

- res.partner.titles
- Provinces and regions
- res.partner.address automation
- ZIP codes auto-completion


""",
    'author': 'Didotech, ver. 7 migration Matmoz',
    'website': 'http://www.didotech.com, http://www.matmoz.si',
    'license': 'AGPL-3',
    "depends": [
        'base'
    ],
    "init_xml": [],
    "update_xml": [
        'partner/partner_view.xml',
        "security/ir.model.access.csv",
#        'partner/data_it/res.region.csv',
#        'partner/data_it/res.province.csv',
#        'partner/data_it/res.city.csv',
#        'partner/data_it/res.partner.title.csv',
#        'partner/data_it/res.country.csv',
#        'partner/data_si/res.region.csv',
#        'partner/data_si/res.province.csv',
#        'partner/data_si/res.city.csv',
#        'partner/data_si/res.partner.title.csv',
#        'partner/data_si/res.country.csv',
#        'partner/data_no/res.region.csv',
#        'partner/data_no/res.province.csv',
#        'partner/data_no/res.city.csv',
#        'partner/data_no/res.country.csv',
#        'partner/data_us/res.country.csv'
    ],
    "demo_xml": [],
    "active": False,
    "installable": True
}

# http://www.istat.it/strumenti/definizioni/comuni/
# i dati dovrebbero essere sincronizzati con questi
