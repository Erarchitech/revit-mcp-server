# -*- coding: UTF-8 -*-
"""
Document enumeration and identity-pinned selection snapshot (DeGram, D-13/D-14).

Skeleton: the handlers are declared (so the route set and the API-context
signatures are fixed) and answer NOT_IMPLEMENTED until the next commit.
"""

from pyrevit import routes


def register_document_read_routes(api):
    """Register the two DeGram read routes."""

    @api.route("/list_open_documents/", methods=["GET"])
    def list_open_documents(uiapp):
        return routes.make_response(
            data={"status": "error", "code": "BAD_REQUEST", "error": "NOT_IMPLEMENTED"},
            status=501)

    @api.route("/selection_snapshot/", methods=["POST"])
    def selection_snapshot(uiapp, uidoc, request):
        return routes.make_response(
            data={"status": "error", "code": "BAD_REQUEST", "error": "NOT_IMPLEMENTED"},
            status=501)
