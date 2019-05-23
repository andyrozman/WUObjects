# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/responses/get_fortress_details_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wuprotos.data import poi_details_pb2 as wuprotos_dot_data_dot_poi__details__pb2
from wuprotos.data import fortress_cooldown_data_pb2 as wuprotos_dot_data_dot_fortress__cooldown__data__pb2
from wuprotos.enums import poi_accessibility_pb2 as wuprotos_dot_enums_dot_poi__accessibility__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/responses/get_fortress_details_response.proto',
  package='wuprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nAwuprotos/networking/responses/get_fortress_details_response.proto\x12\x1dwuprotos.networking.responses\x1a\x1fwuprotos/data/poi_details.proto\x1a*wuprotos/data/fortress_cooldown_data.proto\x1a&wuprotos/enums/poi_accessibility.proto\"\xe3\x04\n\x1aGetFortressDetailsResponse\x12 \n\x18\x66ortress_template_gmt_id\x18\x01 \x01(\t\x12Z\n\x08\x63hambers\x18\x02 \x03(\x0b\x32H.wuprotos.networking.responses.GetFortressDetailsResponse.ChamberPreview\x12\x12\n\npartner_id\x18\x04 \x01(\t\x12.\n\x0bpoi_details\x18\x05 \x01(\x0b\x32\x19.wuprotos.data.PoiDetails\x12;\n\x11poi_accessibility\x18\x06 \x01(\x0e\x32 .wuprotos.enums.PoiAccessibility\x12_\n\x12\x66ortress_occupancy\x18\x07 \x01(\x0e\x32\x43.wuprotos.networking.responses.GetFortressDetailsResponse.Occupancy\x12:\n\rcooldown_data\x18\x08 \x01(\x0b\x32#.wuprotos.data.FortressCooldownData\x1az\n\x0e\x43hamberPreview\x12\x1f\n\x17\x63hamber_template_gmt_id\x18\x01 \x01(\t\x12\x14\n\x0cplayer_count\x18\x02 \x01(\r\x12\x15\n\rstart_time_ms\x18\x03 \x01(\x03\x12\x1a\n\x12num_friends_inside\x18\x04 \x01(\r\"-\n\tOccupancy\x12\x0c\n\x08NOT_BUSY\x10\x00\x12\x08\n\x04\x42USY\x10\x01\x12\x08\n\x04\x46ULL\x10\x02\x62\x06proto3')
  ,
  dependencies=[wuprotos_dot_data_dot_poi__details__pb2.DESCRIPTOR,wuprotos_dot_data_dot_fortress__cooldown__data__pb2.DESCRIPTOR,wuprotos_dot_enums_dot_poi__accessibility__pb2.DESCRIPTOR,])



_GETFORTRESSDETAILSRESPONSE_OCCUPANCY = _descriptor.EnumDescriptor(
  name='Occupancy',
  full_name='wuprotos.networking.responses.GetFortressDetailsResponse.Occupancy',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOT_BUSY', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUSY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FULL', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=784,
  serialized_end=829,
)
_sym_db.RegisterEnumDescriptor(_GETFORTRESSDETAILSRESPONSE_OCCUPANCY)


_GETFORTRESSDETAILSRESPONSE_CHAMBERPREVIEW = _descriptor.Descriptor(
  name='ChamberPreview',
  full_name='wuprotos.networking.responses.GetFortressDetailsResponse.ChamberPreview',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chamber_template_gmt_id', full_name='wuprotos.networking.responses.GetFortressDetailsResponse.ChamberPreview.chamber_template_gmt_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_count', full_name='wuprotos.networking.responses.GetFortressDetailsResponse.ChamberPreview.player_count', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time_ms', full_name='wuprotos.networking.responses.GetFortressDetailsResponse.ChamberPreview.start_time_ms', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_friends_inside', full_name='wuprotos.networking.responses.GetFortressDetailsResponse.ChamberPreview.num_friends_inside', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=660,
  serialized_end=782,
)

_GETFORTRESSDETAILSRESPONSE = _descriptor.Descriptor(
  name='GetFortressDetailsResponse',
  full_name='wuprotos.networking.responses.GetFortressDetailsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fortress_template_gmt_id', full_name='wuprotos.networking.responses.GetFortressDetailsResponse.fortress_template_gmt_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chambers', full_name='wuprotos.networking.responses.GetFortressDetailsResponse.chambers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partner_id', full_name='wuprotos.networking.responses.GetFortressDetailsResponse.partner_id', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='poi_details', full_name='wuprotos.networking.responses.GetFortressDetailsResponse.poi_details', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='poi_accessibility', full_name='wuprotos.networking.responses.GetFortressDetailsResponse.poi_accessibility', index=4,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fortress_occupancy', full_name='wuprotos.networking.responses.GetFortressDetailsResponse.fortress_occupancy', index=5,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cooldown_data', full_name='wuprotos.networking.responses.GetFortressDetailsResponse.cooldown_data', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETFORTRESSDETAILSRESPONSE_CHAMBERPREVIEW, ],
  enum_types=[
    _GETFORTRESSDETAILSRESPONSE_OCCUPANCY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=218,
  serialized_end=829,
)

_GETFORTRESSDETAILSRESPONSE_CHAMBERPREVIEW.containing_type = _GETFORTRESSDETAILSRESPONSE
_GETFORTRESSDETAILSRESPONSE.fields_by_name['chambers'].message_type = _GETFORTRESSDETAILSRESPONSE_CHAMBERPREVIEW
_GETFORTRESSDETAILSRESPONSE.fields_by_name['poi_details'].message_type = wuprotos_dot_data_dot_poi__details__pb2._POIDETAILS
_GETFORTRESSDETAILSRESPONSE.fields_by_name['poi_accessibility'].enum_type = wuprotos_dot_enums_dot_poi__accessibility__pb2._POIACCESSIBILITY
_GETFORTRESSDETAILSRESPONSE.fields_by_name['fortress_occupancy'].enum_type = _GETFORTRESSDETAILSRESPONSE_OCCUPANCY
_GETFORTRESSDETAILSRESPONSE.fields_by_name['cooldown_data'].message_type = wuprotos_dot_data_dot_fortress__cooldown__data__pb2._FORTRESSCOOLDOWNDATA
_GETFORTRESSDETAILSRESPONSE_OCCUPANCY.containing_type = _GETFORTRESSDETAILSRESPONSE
DESCRIPTOR.message_types_by_name['GetFortressDetailsResponse'] = _GETFORTRESSDETAILSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFortressDetailsResponse = _reflection.GeneratedProtocolMessageType('GetFortressDetailsResponse', (_message.Message,), dict(

  ChamberPreview = _reflection.GeneratedProtocolMessageType('ChamberPreview', (_message.Message,), dict(
    DESCRIPTOR = _GETFORTRESSDETAILSRESPONSE_CHAMBERPREVIEW,
    __module__ = 'wuprotos.networking.responses.get_fortress_details_response_pb2'
    # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.GetFortressDetailsResponse.ChamberPreview)
    ))
  ,
  DESCRIPTOR = _GETFORTRESSDETAILSRESPONSE,
  __module__ = 'wuprotos.networking.responses.get_fortress_details_response_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.GetFortressDetailsResponse)
  ))
_sym_db.RegisterMessage(GetFortressDetailsResponse)
_sym_db.RegisterMessage(GetFortressDetailsResponse.ChamberPreview)


# @@protoc_insertion_point(module_scope)
