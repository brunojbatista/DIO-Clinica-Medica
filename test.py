from typing import List

# ==============================================================================================
# folder: entities/patients/

MIN_AGE = 0
MAX_AGE = 120

class Age:
    """Represents a person's age with validation for minimum and maximum limits.

    Attributes:
        _age (int): The age value.
    """
    def __init__(self, age: int):
        """Initializes an Age instance.

        Args:
            age (int): The age to be set.
        """
        self._age: int = None

        self.age = age
    
    @property
    def age(self) -> int:
        """Gets the age value.

        Returns:
            int: The age of the person.
        """
        return self._age
    
    @age.setter
    def age(self, age: int):
        """Sets the age value with validation.

        Args:
            age (int): The age to be set.

        Raises:
            ValueError: If the age is negative or exceeds the maximum limit.
        """
        if age < MIN_AGE:
            raise ValueError("A idade não pode ser negativa")
        elif age > MAX_AGE:
            raise ValueError(f"A idade passou do limite de {age} anos")
        self._age = age

    def __str__(self) -> str:
        """Returns a string representation of the age.

        Returns:
            str: A string describing the age with appropriate pluralization.
        """
        return f"Idade: {self.age} ano" + ("s" if self.age > 1 else "")
    
    def __eq__(self, value: 'Age') -> bool:
        """Checks if two Age instances are equal.

        Args:
            value (Age): The other Age instance to compare.

        Returns:
            bool: True if the ages are equal, False otherwise.
        """
        return self.age == value.age

PRIORITIES_LIST = ['normal', 'urgente']
WEIGHT_PRIORITIES_LIST = {'normal': 0, 'urgente': 1}
DEFAULT_PRIORITY = 'normal'

class Priority:
    """Represents a priority level for a medical appointment.

    Attributes:
        _name (str): The name of the priority level.
        _weight (int): The weight associated with the priority level.
    """
    def __init__(self, name: str):
        """Initializes a Priority instance.

        Args:
            name (str): The name of the priority level.
        """
        self._name: str = None
        self._weight: int = None

        self.name = name
        self.weight = WEIGHT_PRIORITIES_LIST[name] if name in WEIGHT_PRIORITIES_LIST else WEIGHT_PRIORITIES_LIST[DEFAULT_PRIORITY]

    @property
    def name(self) -> str:
        """Gets the name of the priority level.

        Returns:
            str: The name of the priority.
        """
        return self._name
    
    @name.setter
    def name(self, name: str):
        """Sets the name of the priority level with validation.

        Args:
            name (str): The name to be set.

        Raises:
            ValueError: If the priority name is not in the allowed priorities list.
        """
        if name not in PRIORITIES_LIST:
            raise ValueError("A prioridade não encontrado")
        self._name = name

    @property
    def weight(self) -> int:
        """Gets the weight of the priority level.

        Returns:
            int: The weight of the priority.
        """
        return self._weight
    
    @weight.setter
    def weight(self, weight: int):
        """Sets the weight of the priority level.

        Args:
            weight (int): The weight to be set.
        """
        self._weight = weight

    def __eq__(self, value: 'Priority') -> bool:
        """Checks if two Priority instances are equal.

        Two priorities are considered equal if they have the same name and weight.

        Args:
            value (Priority): The other Priority instance to compare.

        Returns:
            bool: True if the priorities are equal, False otherwise.
        """
        return self.name == value.name and self.weight == value.weight
    
    def __str__(self) -> str:
        """Returns a string representation of the priority.

        Returns:
            str: A string containing the priority.
        """
        return f"Prioridade: {self.name} e peso {self.weight}"

class Patient:
    """Represents a patient with a name and age.

    Attributes:
        _name (str): The name of the patient.
        _age (Age): The age of the patient.
    """
    def __init__(self, name: str, age: Age):
        """Initializes a Patient instance.

        Args:
            name (str): The name of the patient.
            age (Age): The age of the patient.
        """
        self._name: str = name
        self._age: Age = age

        self.name = name
        self.age = age

    @property
    def name(self) -> str:
        """Gets the name of the patient.

        Returns:
            str: The name of the patient.
        """
        return self._name
    
    @name.setter
    def name(self, name: str):
        """Sets the name of the patient.

        Args:
            name (str): The name to be set.
        """
        self._name = name

    @property
    def age(self) -> Age:
        """Gets the age of the patient.

        Returns:
            Age: The age object of the patient.
        """
        return self._age
    
    @age.setter
    def age(self, age: Age):
        """Sets the age of the patient.

        Args:
            age (Age): The age to be set.
        """
        self._age = age

    def __str__(self) -> str:
        """Returns a string representation of the patient.

        Returns:
            str: A string containing the patient's name and age.
        """
        return f"Nome do paciente: {self.name} e {self.age}"
    
    def __eq__(self, value: 'Patient') -> bool:
        """Checks if two Patient instances are equal.

        Two patients are considered equal if they have the same name and age.

        Args:
            value (Patient): The other Patient instance to compare.

        Returns:
            bool: True if the patients are equal, False otherwise.
        """
        return self.name == value.name and self.age == value.age

# ==============================================================================================
# folder: entities/medical/

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
        appointments = self.appointments.copy()
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
            appointments = self.appointments.copy()
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

# ==============================================================================================
# folder: services/

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
    
# ==============================================================================================


medical_management_system: MedicalManagementSystem = MedicalManagementSystem('Sistema de Teste')

medical_management_system_service: MedicalManagementSystemService = MedicalManagementSystemService(medical_management_system)

# Entrada do número de pacientes
n = int(input().strip())

for _ in range(n):
    name, age, status = input().strip().split(", ")
    age = int(age)
    medical_management_system_service.make_an_appointment(name, age, status)
    
print(medical_management_system)