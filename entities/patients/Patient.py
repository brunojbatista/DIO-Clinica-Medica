from entities.patients.Age import Age

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
        return f"Nome do paciente: {self.name}\n{self.age}"
    
    def __eq__(self, value: 'Patient') -> bool:
        """Checks if two Patient instances are equal.

        Two patients are considered equal if they have the same name and age.

        Args:
            value (Patient): The other Patient instance to compare.

        Returns:
            bool: True if the patients are equal, False otherwise.
        """
        return self.name == value.name and self.age == value.age