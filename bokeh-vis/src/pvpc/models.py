import datetime
import pydantic
from typing import *

__all__ = ("EsiosPVPCDayResponse", "PVPCDay", "PVPCHourlyPrice")

PVPCHourlyPrice = Dict[int, float]


class EsiosPVPCDayResponse(pydantic.BaseModel):
    """Output returned by the ESIOS PVPC API"""

    class EsiosPVPCHour(pydantic.BaseModel):
        """Object returned by ESIOS PVPC API in response body array"""
        Dia: datetime.date
        Hora: int
        PCB: float
        CYM: float

        @pydantic.validator("PCB", "CYM", pre=True)
        def _convert_price_format(cls, v):
            """Convert prices given in comma-format ("336.94") to dot-format ("336.94").
            Prices are given in cents, so multiply by 1000 and round to 5 decimals (from 336.94 to 0.33694)
            """
            if type(v) is not str:
                return v

            v = float(v.replace(",", ".")) / 1000
            return round(v, 5)

        @pydantic.validator("Dia", pre=True)
        def _convert_day(cls, v):
            """Validate and convert day field with format "DD/MM/YYYY" to a datetime object.
            """
            if type(v) is not str:
                return v

            chunks = v.split("/")
            if len(chunks) != 3:
                raise ValueError(f"\"Dia\" field from Esios PVPC response is not a proper DD/MM/YYYY date: \"{v}\"")

            day, month, year = [int(c) for c in chunks]
            return datetime.date(year=year, month=month, day=day)

        @pydantic.validator("Hora", pre=True)
        def _convert_hour(cls, v):
            """Validate and convert hour field with format "X-Y" (being X the current hour, and Y the next hour,
            with a span of 1 hour), to the int X.
            """
            if type(v) is not str:
                return v

            chunks = v.split("-")
            hour_now = None

            if len(chunks) == 2:
                _hour_now, _hour_after = [int(c) for c in chunks]
                if _hour_after - _hour_now == 1:
                    hour_now = _hour_now

            if hour_now is None:
                raise ValueError(f"\"Hora\" field from Esios PVPC response is an unexpected hour range: \"{v}\"")
            return hour_now

    # EsiosPVPCDayResponse fields
    PVPC: List[EsiosPVPCHour]


class PVPCDay(pydantic.BaseModel):
    """A day worth of PVPC data"""

    class PVPCDayData(pydantic.BaseModel):
        """Data node for a PVPCDay object"""

        class PVPCDayByLocation(pydantic.BaseModel):
            """Sub-data node for a PVPCDay object, for a certain location"""
            hours: PVPCHourlyPrice = dict()
            """Relation of {hour:price}, where hour is the hour of the day (range between the hour and the next hour),
            and price is the €/kWh cost."""

        # PVPCDayData fields
        pcb: PVPCDayByLocation
        """Data for Peninsula, Canarias, Baleares"""
        cm: PVPCDayByLocation
        """Data for Ceuta, Melilla"""

    # PVPCDay fields
    day: datetime.date
    data: PVPCDayData
