# Copyright (c) 2024, SanU and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Guardian(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		guardian_name: DF.Data
		naming_series: DF.Literal["naming_series"]
		occupation: DF.Data | None
		phone_number: DF.Phone
	# end: auto-generated types
	pass
