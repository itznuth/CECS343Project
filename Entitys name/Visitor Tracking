class VisitorTracking:
    """Tracks the number of visitors in the mall.

    Attributes:
        total_visitors (int): The total number of visitors currently in the mall.
        visitor_times (list): Timestamps of visitor entries.
    """

    def __init__(self, total_visitors: int = 0, visitor_times: list = None):
        self.total_visitors = total_visitors
        self.visitor_times = visitor_times if visitor_times is not None else []

    def get_total_visitors(self) -> int:
        """Retrieves the total number of visitors."""
        return self.total_visitors

    def increment_visitor_count(self, time: str) -> None:
        """Increases the visitor count and logs the time."""
        self.total_visitors += 1
        self.visitor_times.append(time)

    def decrement_visitor_count(self) -> None:
        """Decreases the visitor count if greater than zero."""
        if self.total_visitors > 0:
            self.total_visitors -= 1
