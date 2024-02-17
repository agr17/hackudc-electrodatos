import datetime

__all__ = ("PVPCNoDataForDay",)


class PVPCNoDataForDay(Exception):
    def __init__(self, day: datetime.date):
        self._day = day

    @property
    def day(self):
        return self._day

    def __str__(self):
        return f"No PVPC data found for day {self._day.isoformat()}"
