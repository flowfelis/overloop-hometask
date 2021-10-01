from marshmallow import Schema
from marshmallow import fields
from marshmallow import post_load
from marshmallow import validate

from techtest.authors.models import Author


class AuthorSchema(Schema):
    class Meta(object):
        model = Author

    id = fields.Integer()
    first_name = fields.String(validate=validate.Length(max=255))
    last_name = fields.String(validate=validate.Length(max=255))

    @post_load
    def update_or_create(self, data, *args, **kwargs):
        author, _ = Author.objects.update_or_create(
            id=data.pop("id", None), defaults=data
        )
        return author
