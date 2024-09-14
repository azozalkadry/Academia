
// Copyright (c) 2024, SanU and contributors
// For license information, please see license.txt
function handleStudentButtonClick(record_id) {
    // Example action: redirect to a specific record
    const url = `/app/`;
    window.open(url, '_blank'); // Opens in a new tab
}
frappe.ui.form.on("Transaction Applicants", {
    
	academic_program: function(frm) {
        var academic_program = frm.doc.academic_program;
        if (academic_program) {
            frappe.call({
                method: 'academia.admission.doctype.transaction_applicants.transaction_applicants.get_students',
                args: {
                    condition_value: academic_program 
                },
                callback: function(r) {
                    
                        frm.clear_table("students");
                        r.message.forEach(function(row) {
                            var child = frm.add_child("students");
                            child.student_name = row.first_name+' '+row.middle_name+' '+row.last_name; 
                            child.program_degree = row.program_degree; 
                            child.faculty_department = row.faculty_department; 
                            child.student_email_address = row.student_email_address; 
                            child.faculty = row.faculty;
                            child.student_no = row.name;
                        
                            
                            
                        });
                        frm.refresh_field("students");
                }
            });
            
        }
       
    },
    
});
