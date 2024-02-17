import datetime
import requests
from typing import *
from . import models
from . import exceptions

__all__ = ("get_pvpc_day",)


def _request_pvpc(day: datetime.date) -> requests.Response:
    """Perform the request to the Esios API for fetching values on the requested date.

    Sample URL: https://api.esios.ree.es/archives/70/download_json?locale=es&date=2021-12-09

    Sample response:
        {
           "PVPC": [
              {
                 "Dia":"09/12/2021",
                 "Hora":"00-01",
                 "PCB":"265,06",
                 "CYM":"265,06",
                 "COF2TD":"0,000114951590000000",
                 "PMHPCB":"251,36",
                 "PMHCYM":"251,36",
                 "SAHPCB":"7,63",
                 "SAHCYM":"7,63",
                 "FOMPCB":"0,03",
                 "FOMCYM":"0,03",
                 "FOSPCB":"0,18",
                 "FOSCYM":"0,18",
                 "INTPCB":"0,00",
                 "INTCYM":"0,00",
                 "PCAPPCB":"0,00",
                 "PCAPCYM":"0,00",
                 "TEUPCB":"0,92",
                 "TEUCYM":"0,92",
                 "CCVPCB":"4,93",
                 "CCVCYM":"4,93",
                 "EDSRPCB":"0,00",
                 "EDSRCYM":"0,00"
              }
           ]
        }
    Where PVPC[].PCB, PVPC[].CYM is final €/kwh price for Peninsula/Canarias/Baleares and Ceuta/Melilla respectively
    """
    url = f"https://api.esios.ree.es/archives/70/download_json?locale=es&date={day.isoformat()}"
    r = requests.get(url)
    r.raise_for_status()
    return r


def _format_pvpc_day(day: datetime.date, esios_data: models.EsiosPVPCDayResponse) -> models.PVPCDay:
    day_pcb = models.PVPCDay.PVPCDayData.PVPCDayByLocation()
    day_cm = models.PVPCDay.PVPCDayData.PVPCDayByLocation()

    for hour_data in esios_data.PVPC:
        if hour_data.Dia != day:
            raise ValueError("Esios PVPC hour chunk does not correspond with the day "
                             f"(got \"{hour_data.Dia}\", should be \"{day}\"")

        hour = hour_data.Hora
        price_pcb = hour_data.PCB
        price_cm = hour_data.CYM
        day_pcb.hours[hour] = price_pcb
        day_cm.hours[hour] = price_cm

    return models.PVPCDay(
        day=day,
        data=models.PVPCDay.PVPCDayData(
            pcb=day_pcb,
            cm=day_cm
        )
    )


def get_pvpc_day(day: Union[datetime.date, str]) -> models.PVPCDay:
    """Fetch PVPC prices per hour for a single day.

    :param day: day to fetch data of, as datetime.date object or "YYYY-MM-DD" string
    :return: models.PVPCDay object
    :raises: exceptions.PVPCNoDataForDay when no data found for the requested date
    """
    if type(day) is not datetime.date:
        day = datetime.date.fromisoformat(day)

    response = _request_pvpc(day)
    data = response.json()

    if data.get("message") == "No values for specified archive":
        raise exceptions.PVPCNoDataForDay(day)

    parsed_data = models.EsiosPVPCDayResponse(**data)
    return _format_pvpc_day(day, parsed_data)
