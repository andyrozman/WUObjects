# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/requests/messages/player_level_up_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/requests/messages/player_level_up_message.proto',
  package='wuprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nCwuprotos/networking/requests/messages/player_level_up_message.proto\x12%wuprotos.networking.requests.messages\"\x16\n\x14PlayerLevelUpMessageb\x06proto3')
)




_PLAYERLEVELUPMESSAGE = _descriptor.Descriptor(
  name='PlayerLevelUpMessage',
  full_name='wuprotos.networking.requests.messages.PlayerLevelUpMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=110,
  serialized_end=132,
)

DESCRIPTOR.message_types_by_name['PlayerLevelUpMessage'] = _PLAYERLEVELUPMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlayerLevelUpMessage = _reflection.GeneratedProtocolMessageType('PlayerLevelUpMessage', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERLEVELUPMESSAGE,
  __module__ = 'wuprotos.networking.requests.messages.player_level_up_message_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.requests.messages.PlayerLevelUpMessage)
  ))
_sym_db.RegisterMessage(PlayerLevelUpMessage)


# @@protoc_insertion_point(module_scope)
