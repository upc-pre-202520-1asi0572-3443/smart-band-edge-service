from health.domain.entities import HealthRecord
from health.domain.services import HealthRecordService
from health.infrastructure.repositories import HealthRecordRepository
from iam.application.services import AuthApplicationService


class HealthRecordApplicationService:
    """
    Application service for managing health records.
    """
    def __init__(self):
        """
        Initialize the HealthRecordApplicationService with necessary repositories and services.
        """
        self.heath_record_repository = HealthRecordRepository()
        self.health_record_service = HealthRecordService()
        self.iam_service = AuthApplicationService()

    def create_health_record(self, device_id: str, bpm: float, created_at: str, api_key: str)->HealthRecord:
        """
        Create a health record for a device.
        :param device_id: The ID of the device.
        :param bpm: The beats per minute.
        :param created_at: The timestamp when the record was created.
        :return: A created health record.
        :raises ValueError: If the device is not found or the API key is invalid.
        """
        if not self.iam_service.get_device_by_id_and_api_key(device_id, api_key):
            raise ValueError("Device not found or invalid API key")
        record = self.health_record_service.create_record(device_id, bpm, created_at)
        return self.heath_record_repository.save(record)