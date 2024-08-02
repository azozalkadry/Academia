# Copyright (c) 2024, SanU and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Qualification(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		college: DF.Data
		country: DF.Data
		department: DF.Data
		estimation: DF.Data
		graduation_year: DF.Data
		name1: DF.Data
		name_series: DF.Literal["ADM-SAP-.YYYY.-"]
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		percentage: DF.Data
		qualification: DF.Data
		role: DF.Data
		specialty: DF.Data
		university: DF.Data
	# end: auto-generated types
	pass
