from tortoise.fields import TextField, DatetimeField
from tortoise.models import Model


class TextSummary(Model):
    url: TextField = TextField()
    summary: TextField = TextField()
    created_at: DatetimeField = DatetimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.url
