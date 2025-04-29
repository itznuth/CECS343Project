class Customer(Person):
    """Represents a customer in the mall.

    Attributes:
        feedback (list): A list of feedback or complaints submitted by the customer.

    Methods:
        submit_feedback(feedback_text: str) -> None: Stores customer feedback.
        browse_store() -> str: Simulates browsing available stores.
    """

    def __init__(self, name: str):
        """Initializes a Customer with a name and an empty feedback list."""
        super().__init__(name)
        self.feedback = []

    def submit_feedback(self, feedback_text: str) -> None:
        """Stores customer feedback."""
        if not feedback_text.strip():
            return "Error: Feedback can't be empty."
        self.feedback.append(feedback_text)
        return "Feedback submitted successfully."
        
        

    def browse_store(self) -> str:
        """Simulates browsing available stores."""
        return f"{self.name} is browsing the stores."
