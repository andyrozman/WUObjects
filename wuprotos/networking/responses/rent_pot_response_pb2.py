# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/responses/rent_pot_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/responses/rent_pot_response.proto',
  package='wuprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n5wuprotos/networking/responses/rent_pot_response.proto\x12\x1dwuprotos.networking.responses\"\xf3\x01\n\x0fRentPotResponse\x12\x45\n\x06status\x18\x01 \x01(\x0e\x32\x35.wuprotos.networking.responses.RentPotResponse.Status\"\x98\x01\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07TOO_FAR\x10\x02\x12\x0e\n\nPOI_CLOSED\x10\x03\x12\x14\n\x10\x46\x45\x41TURE_DISABLED\x10\x04\x12\x0f\n\x0bINVALID_POT\x10\x05\x12\x16\n\x12POT_ALREADY_RENTED\x10\x06\x12\x1a\n\x16INSUFFICIENT_RESOURCES\x10\x07\x62\x06proto3')
)



_RENTPOTRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='wuprotos.networking.responses.RentPotResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOO_FAR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POI_CLOSED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEATURE_DISABLED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_POT', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POT_ALREADY_RENTED', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INSUFFICIENT_RESOURCES', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=180,
  serialized_end=332,
)
_sym_db.RegisterEnumDescriptor(_RENTPOTRESPONSE_STATUS)


_RENTPOTRESPONSE = _descriptor.Descriptor(
  name='RentPotResponse',
  full_name='wuprotos.networking.responses.RentPotResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='wuprotos.networking.responses.RentPotResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RENTPOTRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=332,
)

_RENTPOTRESPONSE.fields_by_name['status'].enum_type = _RENTPOTRESPONSE_STATUS
_RENTPOTRESPONSE_STATUS.containing_type = _RENTPOTRESPONSE
DESCRIPTOR.message_types_by_name['RentPotResponse'] = _RENTPOTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RentPotResponse = _reflection.GeneratedProtocolMessageType('RentPotResponse', (_message.Message,), dict(
  DESCRIPTOR = _RENTPOTRESPONSE,
  __module__ = 'wuprotos.networking.responses.rent_pot_response_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.RentPotResponse)
  ))
_sym_db.RegisterMessage(RentPotResponse)


# @@protoc_insertion_point(module_scope)
