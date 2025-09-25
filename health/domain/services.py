from datetime import timezone, datetime
from dateutil.parser import parse
from health.domain.entities import HealthRecord


class HealthRecordService:
    def __init__(self):
        """Initialize the health record service.
        """
        pass

    @staticmethod
    def create_record(device_id: str, bpm: float, created_at: str | None)-> HealthRecord:
        """Create a health record.

        Args:
            device_id (str): The ID of the device.
            bpm (float): The beats per minute.
            created_at (str | None): The creation timestamp in ISO 8601 format. If None, use current time.

        Returns:
            HealthRecord: The created health record.

        Raises:
            ValueError: If the bpm is not in the range 0-200 or if the created_at is not a valid ISO 8601 string.
        """
        try:
            bpm = float(bpm)
            if not (0 <= bpm <= 200):
                raise ValueError("Invalid BPM value")
            if created_at:
                parsed_created_at = parse(created_at).astimezone(timezone.utc)
            else:
                parsed_created_at = datetime.now(timezone.utc)
        except (ValueError, TypeError):
            raise ValueError("Invalid data format")

        return HealthRecord(device_id, bpm, parsed_created_at)

