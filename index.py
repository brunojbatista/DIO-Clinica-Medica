from entities.medical.MedicalManagementSystem import MedicalManagementSystem
from services.MedicalManagementSystemService import MedicalManagementSystemService

medical_management_system: MedicalManagementSystem = MedicalManagementSystem('Sistema de Teste')

medical_management_system_service: MedicalManagementSystemService = MedicalManagementSystemService(medical_management_system)

# Entrada do número de pacientes
n = int(input().strip())

for _ in range(n):
    name, age, status = input().strip().split(", ")
    age = int(age)
    medical_management_system_service.make_an_appointment(name, age, status)
    
print(medical_management_system)
    


