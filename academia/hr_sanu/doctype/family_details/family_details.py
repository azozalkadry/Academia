# Copyright (c) 2024, SanU and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FamilyDetails(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		date_of_birth: DF.Date | None
		name1: DF.Data | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		relation: DF.Data | None
		sex: DF.Literal["Male", "Female"]
	# end: auto-generated types
	pass
