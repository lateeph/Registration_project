from gluon.contrib.appconfig import AppConfig
configuration = AppConfig(reload=True)

db = DAL("sqlite://storage.sqlite")
db.define_table("users",
               Field('firstname'),
               Field('lastname'),
               Field('email'),
               Field('password'))