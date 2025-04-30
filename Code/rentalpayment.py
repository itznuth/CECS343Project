from datetime import datetime
from typing import List

class RentalPayment:
    """Represents a rental payment with enhanced validation."""

    VALID_STATUSES = {'completed', 'pending', 'overdue'}

    def __init__(self, amount: float, date: str, unit: int, status: str):
        self.set_payment_amount(amount)
        self.set_payment_date(date)
        self.set_rental_unit(unit)
        self.set_payment_status(status)

    def set_payment_amount(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Payment amount must be positive")
        self.amount = amount

    def set_payment_date(self, date: str) -> None:
        try:
            datetime.strptime(date, "%Y-%m-%d")
            self.date = date
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")

    def set_rental_unit(self, unit: int) -> None:
        if unit <= 0:
            raise ValueError("Unit number must be positive")
        self.unit = unit

    def set_payment_status(self, status: str) -> None:
        if status.lower() not in self.VALID_STATUSES:
            raise ValueError(f"Status must be one of: {', '.join(self.VALID_STATUSES)}")
        self.status = status.lower()

    def __str__(self):
        return (f"Unit #{self.unit}: ${self.amount:.2f} "
                f"on {self.date} ({self.status})")

def export_payments(payments: List[RentalPayment], filename: str) -> None:
    """Exports payments to a formatted file."""
    with open(filename, 'w') as file:
        file.write("Rental Payment Report\n")
        file.write("="*40 + "\n")
        total = 0
        for payment in payments:
            file.write(f"{payment}\n")
            if payment.status == 'completed':
                total += payment.amount
        file.write(f"\nTotal Completed Payments: ${total:.2f}")
