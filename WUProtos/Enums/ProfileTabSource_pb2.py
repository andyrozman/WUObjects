# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Enums/ProfileTabSource.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Enums/ProfileTabSource.proto',
  package='WUProtos.Enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n%WUProtos/Enums/ProfileTabSource.proto\x12\x0eWUProtos.Enums*w\n\x10ProfileTabSource\x12\x1c\n\x18PROFILE_TAB_SOURCE_UNSET\x10\x00\x12\x0b\n\x07TAB_NEW\x10\x01\x12\x12\n\x0eTAB_LAST_PHOTO\x10\x02\x12\x13\n\x0fTAB_STOCK_PHOTO\x10\x03\x12\x0f\n\x0bTAB_GALLERY\x10\x04\x62\x06proto3')
)

_PROFILETABSOURCE = _descriptor.EnumDescriptor(
  name='ProfileTabSource',
  full_name='WUProtos.Enums.ProfileTabSource',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PROFILE_TAB_SOURCE_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TAB_NEW', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TAB_LAST_PHOTO', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TAB_STOCK_PHOTO', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TAB_GALLERY', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=57,
  serialized_end=176,
)
_sym_db.RegisterEnumDescriptor(_PROFILETABSOURCE)

ProfileTabSource = enum_type_wrapper.EnumTypeWrapper(_PROFILETABSOURCE)
PROFILE_TAB_SOURCE_UNSET = 0
TAB_NEW = 1
TAB_LAST_PHOTO = 2
TAB_STOCK_PHOTO = 3
TAB_GALLERY = 4


DESCRIPTOR.enum_types_by_name['ProfileTabSource'] = _PROFILETABSOURCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)