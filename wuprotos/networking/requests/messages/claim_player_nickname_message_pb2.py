# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/requests/messages/claim_player_nickname_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/requests/messages/claim_player_nickname_message.proto',
  package='wuprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nIwuprotos/networking/requests/messages/claim_player_nickname_message.proto\x12%wuprotos.networking.requests.messages\"6\n\x1a\x43laimPlayerNicknameMessage\x12\x18\n\x10\x64\x65sired_nickname\x18\x01 \x01(\tb\x06proto3')
)




_CLAIMPLAYERNICKNAMEMESSAGE = _descriptor.Descriptor(
  name='ClaimPlayerNicknameMessage',
  full_name='wuprotos.networking.requests.messages.ClaimPlayerNicknameMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='desired_nickname', full_name='wuprotos.networking.requests.messages.ClaimPlayerNicknameMessage.desired_nickname', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=170,
)

DESCRIPTOR.message_types_by_name['ClaimPlayerNicknameMessage'] = _CLAIMPLAYERNICKNAMEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClaimPlayerNicknameMessage = _reflection.GeneratedProtocolMessageType('ClaimPlayerNicknameMessage', (_message.Message,), dict(
  DESCRIPTOR = _CLAIMPLAYERNICKNAMEMESSAGE,
  __module__ = 'wuprotos.networking.requests.messages.claim_player_nickname_message_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.requests.messages.ClaimPlayerNicknameMessage)
  ))
_sym_db.RegisterMessage(ClaimPlayerNicknameMessage)


# @@protoc_insertion_point(module_scope)
