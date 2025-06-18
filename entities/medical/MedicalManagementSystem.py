from typing import List

from entities.medical.MedicalAppointment import MedicalAppointment

class MedicalManagementSystem:
    """Manages a system for medical appointments, including scheduling and ordering.

    Attributes:
        _name (str): The name of the medical management system.
        _appointments (List[MedicalAppointment]): The list of scheduled medical appointments.
    """
    def __init__(self, name: str):
        """Initializes a MedicalManagementSystem instance.

        Args:
            name (str): The name of the medical management system.
        """
        self._name: str = None
        self._appointments: List[MedicalAppointment] = None

        self.name = name
        self.appointments = []

    @property
    def name(self) -> str:
        """Gets the name of the medical management system.

        Returns:
            str: The name of the system.
        """
        return self._name
    
    @name.setter
    def name(self, name: str):
        """Sets the name of the medical management system.

        Args:
            name (str): The name to be set.
        """
        self._name = name

    @property
    def appointments(self) -> List[MedicalAppointment]:
        """Gets the list of medical appointments.

        Returns:
            List[MedicalAppointment]: The list of scheduled appointments.
        """
        return self._appointments
    
    @appointments.setter
    def appointments(self, appointments: List[MedicalAppointment]):
        """Sets the list of medical appointments.

        Args:
            appointments (List[MedicalAppointment]): The list of appointments to be set.
        """
        self._appointments = appointments

    def order_appointments(self):
        """Sorts the appointments based on priority weight and patient age in descending order."""
        appointments = self.appointments
        appointments = sorted(appointments, key=lambda appointment: (appointment.priority.weight, appointment.patient.age.age), reverse=True)
        self.appointments = appointments

    def add_appointment(self, medical_appointment: MedicalAppointment) -> bool:
        """Adds a medical appointment to the system and reorders the appointments.

        Args:
            medical_appointment (MedicalAppointment): The medical appointment to be added.

        Returns:
            bool: True if the appointment was added successfully, False if it already exists.
        """
        if medical_appointment not in self.appointments:
            appointments = self.appointments
            appointments.append(medical_appointment)
            self.appointments = appointments
            self.order_appointments()
            return True
        return False

    def __str__(self) -> str:
        """Returns a string representation of the appointment order.

        Returns:
            str: A comma-separated string of patient names in the order of appointments.
        """
        text = "Ordem de Atendimento: "
        patient_names = []
        for appointment in self.appointments:
            patient_names.append(appointment.patient.name)
        text += ", ".join(patient_names)
        return text