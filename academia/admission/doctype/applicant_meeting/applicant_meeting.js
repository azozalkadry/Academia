// Copyright (c) 2024, SanU and contributors
// For license information, please see license.txt

frappe.ui.form.on("Applicant Meeting", {
    
<<<<<<< HEAD
	transaction_applicants: function(frm) {
        var transaction_applicants = frm.doc.transaction_applicants;
        if (transaction_applicants) {
            frappe.call({
                method: 'academia.admission.doctype.applicant_meeting.applicant_meeting.get_students',
                args: {
                    condition_value: transaction_applicants 
=======
	academic_program: function(frm) {
        var academic_program = frm.doc.academic_program;
        if (academic_program) {
            frappe.call({
                method: 'academia.admission.doctype.applicant_meeting.applicant_meeting.get_students',
                args: {
                    condition_value: academic_program 
>>>>>>> origin/develop
                },
                callback: function(r) {
                    
                        frm.clear_table("students");
                        r.message.forEach(function(row) {
                            var child = frm.add_child("students");
<<<<<<< HEAD
                            child.student_no = row.student_no;
                            child.student_name = row.student_name; 
=======
                            child.student_name = row.first_name+' '+row.middle_name+' '+row.last_name; 
>>>>>>> origin/develop
                            child.program_degree = row.program_degree; 
                            child.faculty_department = row.faculty_department; 
                            child.student_email_address = row.student_email_address; 
                            child.faculty = row.faculty; 
                            
                            
                        });
                        frm.refresh_field("students");
                }
            });
            
        }
<<<<<<< HEAD
        
=======
>>>>>>> origin/develop
    }
});
