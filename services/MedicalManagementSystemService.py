from entities.medical.MedicalAppointment import MedicalAppointment
from entities.medical.MedicalManagementSystem import MedicalManagementSystem
from entities.patients.Age import Age
from entities.patients.Patient import Patient
from entities.patients.Priority import Priority

class MedicalManagementSystemService:
    """Manages services for scheduling medical appointments within a medical management system.

    Attributes:
        _medical_management_system (MedicalManagementSystem): The medical management system instance.
    """
    def __init__(self, medical_management_system: MedicalManagementSystem):
        """Initializes a MedicalManagementSystemService instance.

        Args:
            medical_management_system (MedicalManagementSystem): The medical management system to be used.
        """
        self._medical_management_system: MedicalManagementSystem = None

        self.medical_management_system = medical_management_system

    @property
    def medical_management_system(self) -> MedicalManagementSystem:
        """Gets the medical management system instance.

        Returns:
            MedicalManagementSystem: The medical management system.
        """
        return self._medical_management_system
    
    @medical_management_system.setter
    def medical_management_system(self, medical_management_system: MedicalManagementSystem):
        """Sets the medical management system instance.

        Args:
            medical_management_system (MedicalManagementSystem): The medical management system to be set.
        """
        self._medical_management_system = medical_management_system

    def make_an_appointment(self, patient_name: str, patient_age: int, priority: str) -> bool:
        """Creates and schedules a new medical appointment.

        Args:
            patient_name (str): The name of the patient.
            patient_age (int): The age of the patient.
            priority (str): The priority level of the appointment.

        Returns:
            bool: True if the appointment was successfully added, False if it already exists.
        """
        age: Age = Age(patient_age)
        priority: Priority = Priority(priority)
        patient: Patient = Patient(patient_name, age)
        medical_appointment: MedicalAppointment = MedicalAppointment(patient, priority)
        return self.medical_management_system.add_appointment(medical_appointment)