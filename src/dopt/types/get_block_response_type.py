# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetBlockResponseType(str, enum.Enum):
    CUSTOM = "custom"
    CARD = "card"
    MODAL = "modal"
    CHECKLIST = "checklist"
    CHECKLIST_ITEM = "checklistItem"
    HINTS = "hints"
    HINTS_ITEM = "hintsItem"
    TOUR = "tour"
    TOUR_ITEM = "tourItem"

    def visit(
        self,
        custom: typing.Callable[[], T_Result],
        card: typing.Callable[[], T_Result],
        modal: typing.Callable[[], T_Result],
        checklist: typing.Callable[[], T_Result],
        checklist_item: typing.Callable[[], T_Result],
        hints: typing.Callable[[], T_Result],
        hints_item: typing.Callable[[], T_Result],
        tour: typing.Callable[[], T_Result],
        tour_item: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetBlockResponseType.CUSTOM:
            return custom()
        if self is GetBlockResponseType.CARD:
            return card()
        if self is GetBlockResponseType.MODAL:
            return modal()
        if self is GetBlockResponseType.CHECKLIST:
            return checklist()
        if self is GetBlockResponseType.CHECKLIST_ITEM:
            return checklist_item()
        if self is GetBlockResponseType.HINTS:
            return hints()
        if self is GetBlockResponseType.HINTS_ITEM:
            return hints_item()
        if self is GetBlockResponseType.TOUR:
            return tour()
        if self is GetBlockResponseType.TOUR_ITEM:
            return tour_item()
