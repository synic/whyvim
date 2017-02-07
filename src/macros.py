import os


VERSIONS = (
    ('One',     1),
    ('Two',     2),
    ('Three',   3),
    ('Four',    4),
    ('Five',    5),
    ('Six',     6),
    ('Seven',   7),
    ('Eight',   8),
)


class SomeSuperSerializer(object):
    """This happens to be an awesome serializer."""

    class Meta:
        model = SomeSuper
        fields = ('updated_at', 'created_at', 'first_name',
                  'last_name', 'address',
                  'phone',
                  'city', 'state', 'zip', 'profile', 'ssn', 'otherfielda,'otherfield2', 'otherfield3')
