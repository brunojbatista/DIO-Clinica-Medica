PRIORITIES_LIST = ['normal', 'urgente']
WEIGHT_PRIORITIES_LIST = {
    'normal': 0,
    'urgente': 1,
}
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