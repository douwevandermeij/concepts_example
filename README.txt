===================================================
Concept Example
===================================================
This example shows the possibilities of using concepts as interfaces instead of directly importing models.

Introduction
===================================================
Concepts can be seen as interfaces. Like interfaces, concepts define a set of attributes. The difference is that the
attributes of concepts need to be mapped instead of implemented.
Concepts also need producers and can be consumed.

Producers
---------------------------------------------------
Producers are existing models that contain data. All attributes of the concept need to be mapped to existing fields of
the producing model. Producing models can contain more fields than that are mapped by the concept. A concept thus covers
a subset of the fields of the producing model.

Consumers
---------------------------------------------------
Consumers use the concept and treat them as regular models. The fact that producing models can contain more fields are
- and should be - ignored by consumers.
