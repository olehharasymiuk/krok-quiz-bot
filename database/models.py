from babel.core import Locale
from peewee import CharField, DateTimeField, ForeignKeyField, IntegerField, TextField, FixedCharField
from peewee import Model, SqliteDatabase

# from bot.utils.date_func import last_month, get_yesterday_today_date
from pathlib import Path

database = SqliteDatabase('/home/oleh/PycharmProjects/irregular_verbs_bot/database/all_data.db')


class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    class Meta:
        table_name = 'users'

    user_id = IntegerField(primary_key=True)
    first_name = CharField(max_length=10, null=True)
    last_name = CharField(max_length=20, null=True)
    language = CharField(max_length=2, null=True)

    @classmethod
    def get_user_locale(cls, user_id):
        try:
            language_code = cls.get_or_none(cls.user_id == user_id).language

            if language_code is None:
                language_code = 'uk'
        except AttributeError:
            language_code = 'uk'

        return Locale(language_code)

    @classmethod
    def set_user_locale(cls, user_id, locale):
        if not cls.get_or_none(cls.user_id == user_id):
            cls.create(user_id=user_id, language=locale).save()

        cls.update(language=locale).where(cls.user_id == user_id).execute()

    @classmethod
    def get_progress(cls):
        return User.select(cls.user_id, Progress.tens, Progress.tens, Progress.hundreds)\
            .join(Progress, on=(Progress.user_id == cls.user_id))


class Verb(BaseModel):
    class Meta:
        table_name = 'verbs'

    first_form = CharField(max_length=10, null=True)
    second_form = CharField(max_length=10, null=True)
    third_form = CharField(max_length=10, null=True)


class Progress(BaseModel):
    class Meta:
        table_name = 'progresses'

    user_id = ForeignKeyField(User, field='user_id')
    units = TextField(null=True, default=None)
    tens = TextField(null=True, default=None)
    hundreds = TextField(null=True, default=None)

    @classmethod
    def verify_learned_verbs(cls, user_id):
        learned_verbds = cls.select().where(cls.user_id == user_id)

        units = []
        tens = []
        hundreds = []
        for verb in learned_verbds:
            print(verb)
            if verb.units:
                # print(verb.units)
                [units.append(x) for x in str(verb.units)]
            if verb.tens:
                # print(verb.tens)
                [tens.append(str(verb.tens)[i:i+2]) for i in range(0, len(str(verb.tens)), 2)]

            if verb.hundreds:
                # print(verb.hundreds)
                hundreds = [str(verb.hundreds)[i:i+3] for i in range(0, len(str(verb.hundreds)), 3)]
        print(units, tens, hundreds)
        return units + tens + hundreds


def init_db():
    database.create_tables([User, Verb, Progress], safe=True)
