from django.conf import settings
from concepts.util import load_class
import concepts


for concept_name, mapping in settings.CONCEPTS.items():
    for klass, fields in mapping.items():
        concept = type(
            concept_name,
            (load_class(klass),),
            {
                '__module__': __name__,
                'Meta': type('Meta', (), {'proxy': True}),
            },
        )
        for _property, _field in fields.items():
            if not hasattr(concept, _property):
                setattr(
                    concept,
                    _property,
                    property(
                        lambda self: getattr(self, _field),
                        lambda self, value: setattr(self, _field, value),
                    ),
                )
        setattr(concepts, concept_name, concept)
