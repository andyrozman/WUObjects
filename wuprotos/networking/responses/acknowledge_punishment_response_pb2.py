# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/responses/acknowledge_punishment_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/responses/acknowledge_punishment_response.proto',
  package='wuprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nCwuprotos/networking/responses/acknowledge_punishment_response.proto\x12\x1dwuprotos.networking.responses\"\xd9\x01\n\x1d\x41\x63knowledgePunishmentResponse\x12S\n\x06result\x18\x01 \x01(\x0e\x32\x43.wuprotos.networking.responses.AcknowledgePunishmentResponse.Result\"c\n\x06Result\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1f\n\x1b\x45RROR_ANTICHEAT_NOT_ENABLED\x10\x02\x12\x1e\n\x1a\x45RROR_NO_PUNISHMENT_TO_ACK\x10\x03\x62\x06proto3')
)



_ACKNOWLEDGEPUNISHMENTRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='wuprotos.networking.responses.AcknowledgePunishmentResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_ANTICHEAT_NOT_ENABLED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NO_PUNISHMENT_TO_ACK', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=221,
  serialized_end=320,
)
_sym_db.RegisterEnumDescriptor(_ACKNOWLEDGEPUNISHMENTRESPONSE_RESULT)


_ACKNOWLEDGEPUNISHMENTRESPONSE = _descriptor.Descriptor(
  name='AcknowledgePunishmentResponse',
  full_name='wuprotos.networking.responses.AcknowledgePunishmentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='wuprotos.networking.responses.AcknowledgePunishmentResponse.result', index=0,
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
    _ACKNOWLEDGEPUNISHMENTRESPONSE_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=320,
)

_ACKNOWLEDGEPUNISHMENTRESPONSE.fields_by_name['result'].enum_type = _ACKNOWLEDGEPUNISHMENTRESPONSE_RESULT
_ACKNOWLEDGEPUNISHMENTRESPONSE_RESULT.containing_type = _ACKNOWLEDGEPUNISHMENTRESPONSE
DESCRIPTOR.message_types_by_name['AcknowledgePunishmentResponse'] = _ACKNOWLEDGEPUNISHMENTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AcknowledgePunishmentResponse = _reflection.GeneratedProtocolMessageType('AcknowledgePunishmentResponse', (_message.Message,), dict(
  DESCRIPTOR = _ACKNOWLEDGEPUNISHMENTRESPONSE,
  __module__ = 'wuprotos.networking.responses.acknowledge_punishment_response_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.AcknowledgePunishmentResponse)
  ))
_sym_db.RegisterMessage(AcknowledgePunishmentResponse)


# @@protoc_insertion_point(module_scope)
