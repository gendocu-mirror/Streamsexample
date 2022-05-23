"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import main_pb2 as main__pb2

class ExampleStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetStream1 = channel.stream_unary('/streams.Example/GetStream1', request_serializer=main__pb2.SimpleMsg1.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString)
        self.ReturnStream1 = channel.unary_stream('/streams.Example/ReturnStream1', request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, response_deserializer=main__pb2.SimpleMsg1.FromString)
        self.BothStream1 = channel.stream_stream('/streams.Example/BothStream1', request_serializer=main__pb2.SimpleMsg1.SerializeToString, response_deserializer=main__pb2.SimpleMsg1.FromString)
        self.GetStream2 = channel.stream_unary('/streams.Example/GetStream2', request_serializer=main__pb2.SimpleMsg2.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString)
        self.ReturnStream2 = channel.unary_stream('/streams.Example/ReturnStream2', request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, response_deserializer=main__pb2.SimpleMsg2.FromString)
        self.BothStream2 = channel.stream_stream('/streams.Example/BothStream2', request_serializer=main__pb2.SimpleMsg2.SerializeToString, response_deserializer=main__pb2.SimpleMsg2.FromString)
        self.GetStream3 = channel.stream_unary('/streams.Example/GetStream3', request_serializer=main__pb2.SimpleMsg3.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString)
        self.ReturnStream3 = channel.unary_stream('/streams.Example/ReturnStream3', request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, response_deserializer=main__pb2.SimpleMsg3.FromString)
        self.BothStream3 = channel.stream_stream('/streams.Example/BothStream3', request_serializer=main__pb2.SimpleMsg3.SerializeToString, response_deserializer=main__pb2.SimpleMsg3.FromString)

class ExampleServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetStream1(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReturnStream1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BothStream1(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStream2(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReturnStream2(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BothStream2(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStream3(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReturnStream3(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BothStream3(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_ExampleServicer_to_server(servicer, server):
    rpc_method_handlers = {'GetStream1': grpc.stream_unary_rpc_method_handler(servicer.GetStream1, request_deserializer=main__pb2.SimpleMsg1.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'ReturnStream1': grpc.unary_stream_rpc_method_handler(servicer.ReturnStream1, request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, response_serializer=main__pb2.SimpleMsg1.SerializeToString), 'BothStream1': grpc.stream_stream_rpc_method_handler(servicer.BothStream1, request_deserializer=main__pb2.SimpleMsg1.FromString, response_serializer=main__pb2.SimpleMsg1.SerializeToString), 'GetStream2': grpc.stream_unary_rpc_method_handler(servicer.GetStream2, request_deserializer=main__pb2.SimpleMsg2.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'ReturnStream2': grpc.unary_stream_rpc_method_handler(servicer.ReturnStream2, request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, response_serializer=main__pb2.SimpleMsg2.SerializeToString), 'BothStream2': grpc.stream_stream_rpc_method_handler(servicer.BothStream2, request_deserializer=main__pb2.SimpleMsg2.FromString, response_serializer=main__pb2.SimpleMsg2.SerializeToString), 'GetStream3': grpc.stream_unary_rpc_method_handler(servicer.GetStream3, request_deserializer=main__pb2.SimpleMsg3.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'ReturnStream3': grpc.unary_stream_rpc_method_handler(servicer.ReturnStream3, request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, response_serializer=main__pb2.SimpleMsg3.SerializeToString), 'BothStream3': grpc.stream_stream_rpc_method_handler(servicer.BothStream3, request_deserializer=main__pb2.SimpleMsg3.FromString, response_serializer=main__pb2.SimpleMsg3.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('streams.Example', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Example(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetStream1(request_iterator, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/streams.Example/GetStream1', main__pb2.SimpleMsg1.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReturnStream1(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_stream(request, target, '/streams.Example/ReturnStream1', google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, main__pb2.SimpleMsg1.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BothStream1(request_iterator, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/streams.Example/BothStream1', main__pb2.SimpleMsg1.SerializeToString, main__pb2.SimpleMsg1.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStream2(request_iterator, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/streams.Example/GetStream2', main__pb2.SimpleMsg2.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReturnStream2(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_stream(request, target, '/streams.Example/ReturnStream2', google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, main__pb2.SimpleMsg2.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BothStream2(request_iterator, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/streams.Example/BothStream2', main__pb2.SimpleMsg2.SerializeToString, main__pb2.SimpleMsg2.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStream3(request_iterator, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/streams.Example/GetStream3', main__pb2.SimpleMsg3.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReturnStream3(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_stream(request, target, '/streams.Example/ReturnStream3', google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString, main__pb2.SimpleMsg3.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BothStream3(request_iterator, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/streams.Example/BothStream3', main__pb2.SimpleMsg3.SerializeToString, main__pb2.SimpleMsg3.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)