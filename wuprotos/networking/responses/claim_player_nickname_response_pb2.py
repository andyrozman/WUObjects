# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/responses/claim_player_nickname_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/responses/claim_player_nickname_response.proto',
  package='wuprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nBwuprotos/networking/responses/claim_player_nickname_response.proto\x12\x1dwuprotos.networking.responses\"\xb7\x01\n\x1b\x43laimPlayerNicknameResponse\x12Q\n\x06status\x18\x01 \x01(\x0e\x32\x41.wuprotos.networking.responses.ClaimPlayerNicknameResponse.Status\"E\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\x16\n\x12NAME_NOT_AVAILABLE\x10\x03\x62\x06proto3')
)



_CLAIMPLAYERNICKNAMERESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='wuprotos.networking.responses.ClaimPlayerNicknameResponse.Status',
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
      name='ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NAME_NOT_AVAILABLE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=216,
  serialized_end=285,
)
_sym_db.RegisterEnumDescriptor(_CLAIMPLAYERNICKNAMERESPONSE_STATUS)


_CLAIMPLAYERNICKNAMERESPONSE = _descriptor.Descriptor(
  name='ClaimPlayerNicknameResponse',
  full_name='wuprotos.networking.responses.ClaimPlayerNicknameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='wuprotos.networking.responses.ClaimPlayerNicknameResponse.status', index=0,
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
    _CLAIMPLAYERNICKNAMERESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=285,
)

_CLAIMPLAYERNICKNAMERESPONSE.fields_by_name['status'].enum_type = _CLAIMPLAYERNICKNAMERESPONSE_STATUS
_CLAIMPLAYERNICKNAMERESPONSE_STATUS.containing_type = _CLAIMPLAYERNICKNAMERESPONSE
DESCRIPTOR.message_types_by_name['ClaimPlayerNicknameResponse'] = _CLAIMPLAYERNICKNAMERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClaimPlayerNicknameResponse = _reflection.GeneratedProtocolMessageType('ClaimPlayerNicknameResponse', (_message.Message,), dict(
  DESCRIPTOR = _CLAIMPLAYERNICKNAMERESPONSE,
  __module__ = 'wuprotos.networking.responses.claim_player_nickname_response_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.ClaimPlayerNicknameResponse)
  ))
_sym_db.RegisterMessage(ClaimPlayerNicknameResponse)


# @@protoc_insertion_point(module_scope)
