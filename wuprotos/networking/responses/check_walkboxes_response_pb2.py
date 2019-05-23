# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/responses/check_walkboxes_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wuprotos.data.loot import loot_reward_pb2 as wuprotos_dot_data_dot_loot_dot_loot__reward__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/responses/check_walkboxes_response.proto',
  package='wuprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n<wuprotos/networking/responses/check_walkboxes_response.proto\x12\x1dwuprotos.networking.responses\x1a$wuprotos/data/loot/loot_reward.proto\"\x86\x02\n\x16\x43heckWalkboxesResponse\x12\x62\n\x10opened_walkboxes\x18\x01 \x03(\x0b\x32H.wuprotos.networking.responses.CheckWalkboxesResponse.OpenedWalkboxProto\x1a\x87\x01\n\x12OpenedWalkboxProto\x12\x1c\n\x14walkbox_gmt_template\x18\x01 \x01(\t\x12>\n\x07rewards\x18\x02 \x01(\x0b\x32-.wuprotos.data.loot.LootReward.LootCollection\x12\x13\n\x0bportkey_ids\x18\x03 \x03(\x03\x62\x06proto3')
  ,
  dependencies=[wuprotos_dot_data_dot_loot_dot_loot__reward__pb2.DESCRIPTOR,])




_CHECKWALKBOXESRESPONSE_OPENEDWALKBOXPROTO = _descriptor.Descriptor(
  name='OpenedWalkboxProto',
  full_name='wuprotos.networking.responses.CheckWalkboxesResponse.OpenedWalkboxProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='walkbox_gmt_template', full_name='wuprotos.networking.responses.CheckWalkboxesResponse.OpenedWalkboxProto.walkbox_gmt_template', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rewards', full_name='wuprotos.networking.responses.CheckWalkboxesResponse.OpenedWalkboxProto.rewards', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='portkey_ids', full_name='wuprotos.networking.responses.CheckWalkboxesResponse.OpenedWalkboxProto.portkey_ids', index=2,
      number=3, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=261,
  serialized_end=396,
)

_CHECKWALKBOXESRESPONSE = _descriptor.Descriptor(
  name='CheckWalkboxesResponse',
  full_name='wuprotos.networking.responses.CheckWalkboxesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opened_walkboxes', full_name='wuprotos.networking.responses.CheckWalkboxesResponse.opened_walkboxes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CHECKWALKBOXESRESPONSE_OPENEDWALKBOXPROTO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=396,
)

_CHECKWALKBOXESRESPONSE_OPENEDWALKBOXPROTO.fields_by_name['rewards'].message_type = wuprotos_dot_data_dot_loot_dot_loot__reward__pb2._LOOTREWARD_LOOTCOLLECTION
_CHECKWALKBOXESRESPONSE_OPENEDWALKBOXPROTO.containing_type = _CHECKWALKBOXESRESPONSE
_CHECKWALKBOXESRESPONSE.fields_by_name['opened_walkboxes'].message_type = _CHECKWALKBOXESRESPONSE_OPENEDWALKBOXPROTO
DESCRIPTOR.message_types_by_name['CheckWalkboxesResponse'] = _CHECKWALKBOXESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CheckWalkboxesResponse = _reflection.GeneratedProtocolMessageType('CheckWalkboxesResponse', (_message.Message,), dict(

  OpenedWalkboxProto = _reflection.GeneratedProtocolMessageType('OpenedWalkboxProto', (_message.Message,), dict(
    DESCRIPTOR = _CHECKWALKBOXESRESPONSE_OPENEDWALKBOXPROTO,
    __module__ = 'wuprotos.networking.responses.check_walkboxes_response_pb2'
    # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.CheckWalkboxesResponse.OpenedWalkboxProto)
    ))
  ,
  DESCRIPTOR = _CHECKWALKBOXESRESPONSE,
  __module__ = 'wuprotos.networking.responses.check_walkboxes_response_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.CheckWalkboxesResponse)
  ))
_sym_db.RegisterMessage(CheckWalkboxesResponse)
_sym_db.RegisterMessage(CheckWalkboxesResponse.OpenedWalkboxProto)


# @@protoc_insertion_point(module_scope)
