#Datetime es una libreria ya integrada q se usa para fechas y tiempo
import datetime as dt
from datetime import date

hoy = date.today()
print("Fecha actual:", hoy)

cumple = date(2000, 5, 15)
print("Cumpleaños:", cumple)