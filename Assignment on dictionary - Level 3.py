"""
Care hospital wants to know the medical speciality visited by the maximum number of patients. Assume that the patient id of the patient along with the medical speciality visited by the patient is stored in a list. The details of the medical specialities are stored in a dictionary as follows:
{
"P":"Pediatrics",
"O":"Orthopedics",
"E":"ENT
} 

Write a function to find the medical speciality visited by the maximum number of patients and return the name of the speciality.

Note: 

Assume that there is always only one medical speciality which is visited by maximum number of patients.

Perform case sensitive string comparison wherever necessary.
"""
#lex_auth_012693816757551104165

def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    p_count = 0 
    o_count = 0 
    e_count = 0 
    for i in patient_medical_speciality_list:
        if(i=="P"):
            p_count += 1 
        elif(i=="O"):
            o_count += 1
        elif(i=="E"):
            e_count += 1
        
    
    if(p_count>o_count and p_count>e_count):
        speciality = medical_speciality["P"]
    elif(o_count>p_count and o_count>e_count):
        speciality = medical_speciality["O"]
    else:
        speciality = medical_speciality["E"]

    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
