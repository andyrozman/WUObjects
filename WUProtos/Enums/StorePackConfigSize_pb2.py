# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Enums/StorePackConfigSize.proto

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
  name='WUProtos/Enums/StorePackConfigSize.proto',
  package='WUProtos.Enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n(WUProtos/Enums/StorePackConfigSize.proto\x12\x0eWUProtos.Enums*F\n\x13StorePackConfigSize\x12\x0e\n\nSIZE_SMALL\x10\x00\x12\x0f\n\x0bSIZE_MEDIUM\x10\x01\x12\x0e\n\nSIZE_LARGE\x10\x02\x62\x06proto3')
)

_STOREPACKCONFIGSIZE = _descriptor.EnumDescriptor(
  name='StorePackConfigSize',
  full_name='WUProtos.Enums.StorePackConfigSize',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SIZE_SMALL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIZE_MEDIUM', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIZE_LARGE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=60,
  serialized_end=130,
)
_sym_db.RegisterEnumDescriptor(_STOREPACKCONFIGSIZE)

StorePackConfigSize = enum_type_wrapper.EnumTypeWrapper(_STOREPACKCONFIGSIZE)
SIZE_SMALL = 0
SIZE_MEDIUM = 1
SIZE_LARGE = 2


DESCRIPTOR.enum_types_by_name['StorePackConfigSize'] = _STOREPACKCONFIGSIZE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)