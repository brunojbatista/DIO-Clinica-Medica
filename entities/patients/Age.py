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