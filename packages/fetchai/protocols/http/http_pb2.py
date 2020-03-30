# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: http.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="http.proto",
    package="fetch.aea.Http",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=_b(
        '\n\nhttp.proto\x12\x0e\x66\x65tch.aea.Http"\xbd\x03\n\x0bHttpMessage\x12\x12\n\nmessage_id\x18\x01 \x01(\x05\x12"\n\x1a\x64ialogue_starter_reference\x18\x02 \x01(\t\x12$\n\x1c\x64ialogue_responder_reference\x18\x03 \x01(\t\x12\x0e\n\x06target\x18\x04 \x01(\x05\x12\x36\n\x07request\x18\x05 \x01(\x0b\x32#.fetch.aea.Http.HttpMessage.RequestH\x00\x12\x38\n\x08response\x18\x06 \x01(\x0b\x32$.fetch.aea.Http.HttpMessage.ResponseH\x00\x1aW\n\x07Request\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x0f\n\x07headers\x18\x04 \x01(\t\x12\r\n\x05\x62odyy\x18\x05 \x01(\x0c\x1a\x65\n\x08Response\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x13\n\x0bstatus_code\x18\x02 \x01(\x05\x12\x13\n\x0bstatus_text\x18\x03 \x01(\t\x12\x0f\n\x07headers\x18\x04 \x01(\t\x12\r\n\x05\x62odyy\x18\x05 \x01(\x0c\x42\x0e\n\x0cperformativeb\x06proto3'
    ),
)


_HTTPMESSAGE_REQUEST = _descriptor.Descriptor(
    name="Request",
    full_name="fetch.aea.Http.HttpMessage.Request",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="method",
            full_name="fetch.aea.Http.HttpMessage.Request.method",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="url",
            full_name="fetch.aea.Http.HttpMessage.Request.url",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="version",
            full_name="fetch.aea.Http.HttpMessage.Request.version",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="headers",
            full_name="fetch.aea.Http.HttpMessage.Request.headers",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="bodyy",
            full_name="fetch.aea.Http.HttpMessage.Request.bodyy",
            index=4,
            number=5,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=270,
    serialized_end=357,
)

_HTTPMESSAGE_RESPONSE = _descriptor.Descriptor(
    name="Response",
    full_name="fetch.aea.Http.HttpMessage.Response",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="version",
            full_name="fetch.aea.Http.HttpMessage.Response.version",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="status_code",
            full_name="fetch.aea.Http.HttpMessage.Response.status_code",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="status_text",
            full_name="fetch.aea.Http.HttpMessage.Response.status_text",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="headers",
            full_name="fetch.aea.Http.HttpMessage.Response.headers",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="bodyy",
            full_name="fetch.aea.Http.HttpMessage.Response.bodyy",
            index=4,
            number=5,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=359,
    serialized_end=460,
)

_HTTPMESSAGE = _descriptor.Descriptor(
    name="HttpMessage",
    full_name="fetch.aea.Http.HttpMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="message_id",
            full_name="fetch.aea.Http.HttpMessage.message_id",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="dialogue_starter_reference",
            full_name="fetch.aea.Http.HttpMessage.dialogue_starter_reference",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="dialogue_responder_reference",
            full_name="fetch.aea.Http.HttpMessage.dialogue_responder_reference",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="target",
            full_name="fetch.aea.Http.HttpMessage.target",
            index=3,
            number=4,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="request",
            full_name="fetch.aea.Http.HttpMessage.request",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="response",
            full_name="fetch.aea.Http.HttpMessage.response",
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_HTTPMESSAGE_REQUEST, _HTTPMESSAGE_RESPONSE,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="performative",
            full_name="fetch.aea.Http.HttpMessage.performative",
            index=0,
            containing_type=None,
            fields=[],
        ),
    ],
    serialized_start=31,
    serialized_end=476,
)

_HTTPMESSAGE_REQUEST.containing_type = _HTTPMESSAGE
_HTTPMESSAGE_RESPONSE.containing_type = _HTTPMESSAGE
_HTTPMESSAGE.fields_by_name["request"].message_type = _HTTPMESSAGE_REQUEST
_HTTPMESSAGE.fields_by_name["response"].message_type = _HTTPMESSAGE_RESPONSE
_HTTPMESSAGE.oneofs_by_name["performative"].fields.append(
    _HTTPMESSAGE.fields_by_name["request"]
)
_HTTPMESSAGE.fields_by_name["request"].containing_oneof = _HTTPMESSAGE.oneofs_by_name[
    "performative"
]
_HTTPMESSAGE.oneofs_by_name["performative"].fields.append(
    _HTTPMESSAGE.fields_by_name["response"]
)
_HTTPMESSAGE.fields_by_name["response"].containing_oneof = _HTTPMESSAGE.oneofs_by_name[
    "performative"
]
DESCRIPTOR.message_types_by_name["HttpMessage"] = _HTTPMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HttpMessage = _reflection.GeneratedProtocolMessageType(
    "HttpMessage",
    (_message.Message,),
    dict(
        Request=_reflection.GeneratedProtocolMessageType(
            "Request",
            (_message.Message,),
            dict(
                DESCRIPTOR=_HTTPMESSAGE_REQUEST,
                __module__="http_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.Http.HttpMessage.Request)
            ),
        ),
        Response=_reflection.GeneratedProtocolMessageType(
            "Response",
            (_message.Message,),
            dict(
                DESCRIPTOR=_HTTPMESSAGE_RESPONSE,
                __module__="http_pb2"
                # @@protoc_insertion_point(class_scope:fetch.aea.Http.HttpMessage.Response)
            ),
        ),
        DESCRIPTOR=_HTTPMESSAGE,
        __module__="http_pb2"
        # @@protoc_insertion_point(class_scope:fetch.aea.Http.HttpMessage)
    ),
)
_sym_db.RegisterMessage(HttpMessage)
_sym_db.RegisterMessage(HttpMessage.Request)
_sym_db.RegisterMessage(HttpMessage.Response)


# @@protoc_insertion_point(module_scope)
