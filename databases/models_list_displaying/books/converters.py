from datetime import datetime
from django.urls import register_converter


class DateConverter:
    regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
    format = '%Y-%m-%d'

    def to_python(self, value: str) -> datetime:
        print('to_python')
        return datetime.strptime(value, self.format)

    def to_url(self, value: datetime) -> str:
        print('to_url')
        return value.strftime(self.format)

register_converter(DateConverter, 'date')

