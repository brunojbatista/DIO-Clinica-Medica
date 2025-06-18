from entities.patients.Patient import Patient
from entities.patients.Priority import Priority


class MedicalAppointment:
    """Represents a medical appointment with a patient and associated priority.

    Attributes:
        _patient (Patient): The patient associated with the appointment.
        _priority (Priority): The priority level of the appointment.
    """
    def __init__(self, patient: Patient, priority: Priority):
        """Initializes a MedicalAppointment instance.

        Args:
            patient (Patient): The patient for the appointment.
            priority (Priority): The priority level of the appointment.
        """
        self._patient: Patient = None
        self._priority: Priority = None

        self.patient = patient
        self.priority = priority

    @property
    def patient(self) -> Patient:
        """Gets the patient associated with the appointment.

        Returns:
            Patient: The patient object.
        """
        return self._patient
    
    @patient.setter
    def patient(self, patient: Patient):
        """Sets the patient associated with the appointment.

        Args:
            patient (Patient): The patient to be set.
        """
        self._patient = patient

    @property
    def priority(self) -> Priority:
        """Gets the priority level of the appointment.

        Returns:
            Priority: The priority object.
        """
        return self._priority
    
    @priority.setter
    def priority(self, priority: Priority):
        """Sets the priority level of the appointment.

        Args:
            priority (Priority): The priority to be set.
        """
        self._priority = priority

    def __eq__(self, value: 'MedicalAppointment') -> bool:
        """Checks if two MedicalAppointment instances are equal.

        Two appointments are considered equal if they have the same patient and priority.

        Args:
            value (MedicalAppointment): The other MedicalAppointment instance to compare.

        Returns:
            bool: True if the appointments are equal, False otherwise.
        """
        return self.patient == value.patient and self.priority == value.priority