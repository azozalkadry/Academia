# Copyright (c) 2024, SanU and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ApplicantMeeting(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from academia.admission.doctype.student_applicant_child.student_applicant_child import StudentApplicantChild
		from frappe.types import DF
		from psa.psa_registration.doctype.request_a_supervisor_child.request_a_supervisor_child import RequestASupervisorchild

<<<<<<< HEAD
		department_council_minutes_date: DF.Date | None
		department_council_minutes_number: DF.Data | None
		discussion_date: DF.Date | None
		discussion_place: DF.Data | None
		discussion_time: DF.Time | None
		students: DF.Table[StudentApplicantChild]
		table_ayrk: DF.Table[RequestASupervisorchild]
		transaction_applicants: DF.Link
=======
		academic_program: DF.Link | None
		students: DF.Table[StudentApplicantChild]
		table_epbm: DF.Table[RequestASupervisorchild]
>>>>>>> origin/develop
	# end: auto-generated types

@frappe.whitelist()
def get_students(condition_value):
    try:
        # Construct your SQL query
        sql_query = """
<<<<<<< HEAD
            select * from `tabStudent Applicant Child` where parent = %s
=======
            select * from `tabStudent Applicant` where status='Verification' and academic_program = %s
>>>>>>> origin/develop
        """
        # Execute the query
        data = frappe.db.sql(sql_query, (condition_value,), as_dict=True)
    
        # Return the fetched data
        return data
        
    except Exception as e:
        frappe.log_error(f"Error in selecting data: {str(e)}")
        return None