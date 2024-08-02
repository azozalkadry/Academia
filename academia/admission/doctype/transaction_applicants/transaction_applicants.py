# Copyright (c) 2024, SanU and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class TransactionApplicants(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from academia.admission.doctype.student_applicant_child.student_applicant_child import StudentApplicantChild
		from frappe.types import DF

		academic_program: DF.Link | None
		students: DF.Table[StudentApplicantChild]
	# end: auto-generated types
	pass
