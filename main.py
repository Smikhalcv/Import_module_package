from application.salary import calculate_salary
from application.db.people import get_employees
import datetime


if __name__ == '__main__':
    print(f'Текущая дата и время: {datetime.datetime.now().strftime("%H:%M:%S %d/%m/%Y")}')
    calculate_salary()
    get_employees()
