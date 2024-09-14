# Copyright (c) 2024, SanU and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class TransactionApplicants(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from academia.admission.doctype.student_applicant_child.student_applicant_child import StudentApplicantChild
		from frappe.types import DF

		academic_program: DF.Link | None
		amended_from: DF.Link | None
		name1: DF.Data | None
		students: DF.Table[StudentApplicantChild]
	# end: auto-generated types
@frappe.whitelist()
def get_students(condition_value):
    try:
        # Construct your SQL query
        sql_query = """
            select * from `tabStudent Applicant` where status='Verification' and academic_program = %s
        """
        # Execute the query
        data = frappe.db.sql(sql_query, (condition_value,), as_dict=True)
    
        # Return the fetched data
        return data
        
    except Exception as e:
        frappe.log_error(f"Error in selecting data: {str(e)}")
        return None
