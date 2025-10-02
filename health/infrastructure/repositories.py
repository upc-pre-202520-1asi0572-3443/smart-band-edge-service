from health.domain.entities import HealthRecord
from health.infrastructure.models import HealthRecord as HealthRecordModel

class HealthRecordRepository:
    """
    Repository for managing health records.
    """
    @staticmethod
    def save(health_record)-> HealthRecord:
        """
        Save a health record to the database.
        :param health_record: The health record to save.
        :return: The saved health record including its ID.
        """
        record = HealthRecordModel.create(
            device_id=health_record.device_id,
            bpm=health_record.bpm,
            created_at=health_record.created_at
        )
        return HealthRecord(
            device_id=health_record.device_id,
            bpm=health_record.bpm,
            created_at=health_record.created_at,
            id=record.id
        )