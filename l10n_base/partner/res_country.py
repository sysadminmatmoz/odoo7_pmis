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

from osv import osv
from osv import fields
from tools.translate import _


class res_country(osv.osv):
    _inherit = 'res.country'

    _columns = {
        'enable_province': fields.boolean('Show Province?'),
        'enable_region': fields.boolean('Show Region?'),
        'enable_state': fields.boolean('Show State?'),
    }
