# Copyright (c) 2024, SanU and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class StudentApplicant(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from academia.academia.doctype.student_guardian.student_guardian import StudentGuardian
		from academia.admission.doctype.document.document import Document
		from academia.admission.doctype.qualification.qualification import Qualification
		from academia.admission.doctype.student_applicant_course_child.student_applicant_course_child import StudentApplicantCourseChild
		from frappe.types import DF

		academic_program: DF.Link
		address_line_1: DF.Data | None
		address_line_2: DF.Data | None
		city: DF.Data | None
		country: DF.Link | None
		date_of_birth: DF.Date | None
		document: DF.Table[Document]
		faculty: DF.Link | None
		faculty_department: DF.Link
		first_name: DF.Data
		gender2: DF.Link | None
		guardian: DF.Table[StudentGuardian]
		joining_date: DF.Date | None
		last_name: DF.Data
		middle_name: DF.Data
		naming_series: DF.Literal["ADM-SAP-.YYYY.-"]
		nationality2: DF.Data | None
		program_degree: DF.Link
		qualification: DF.Table[Qualification]
		remedial_material: DF.Check
		remedial_materials: DF.Table[StudentApplicantCourseChild]
		state: DF.Data | None
		status: DF.Data | None
		student_email_address: DF.Data
		student_mobile_number2: DF.Data | None
	# end: auto-generated types
	pass
