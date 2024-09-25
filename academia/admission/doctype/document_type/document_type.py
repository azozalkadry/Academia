# Copyright (c) 2024, SanU and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class DocumentType(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

<<<<<<< HEAD
		name1: DF.Data
=======
		name1: DF.Data | None
		title: DF.Data | None
>>>>>>> origin/develop
	# end: auto-generated types
	pass
