import sys
from plyer import notification

from app import APP

def notify() -> None:
    least_rem_days: int = sys.maxsize

    if len(APP.database.products) > 0:
        for product in APP.database.products:
            rem_days = product.get_remaining_days()
            if rem_days < least_rem_days and rem_days >= 0:
                least_rem_days = rem_days

        if least_rem_days == 0:
            msg = "You have food items expiring today."
        elif least_rem_days == 1:
            msg = "You have food items expiring tomorrow."
        else:
            msg = f"You have food items expiring in {least_rem_days} days."

        notification.notify(
            title="Expiration Date Tracker",
            message=msg + " Consume them before they expire.",
            timeout=10,  # Duration in seconds for the notification to display
        ) # type: ignore


# Execute notification check
notify()