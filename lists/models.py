from mongoengine import Document, StringField

class Item(Document):
    text = StringField()