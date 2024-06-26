# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import scrapper_pb2 as scrapper__pb2


class SiteInformationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_information = channel.unary_unary(
                '/SiteInformation/get_information',
                request_serializer=scrapper__pb2.SiteInformationRequest.SerializeToString,
                response_deserializer=scrapper__pb2.SiteInformationResponse.FromString,
                )


class SiteInformationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def get_information(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SiteInformationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_information': grpc.unary_unary_rpc_method_handler(
                    servicer.get_information,
                    request_deserializer=scrapper__pb2.SiteInformationRequest.FromString,
                    response_serializer=scrapper__pb2.SiteInformationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SiteInformation', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SiteInformation(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def get_information(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SiteInformation/get_information',
            scrapper__pb2.SiteInformationRequest.SerializeToString,
            scrapper__pb2.SiteInformationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
