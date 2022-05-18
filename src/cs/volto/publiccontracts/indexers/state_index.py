# -*- coding: utf-8 -*-

from cs.volto.publiccontracts.content.contract import IContract
from plone.dexterity.interfaces import IDexterityContent
from plone.indexer import indexer


@indexer(IDexterityContent)
def dummy(obj):
    """Dummy to prevent indexing other objects thru acquisition"""
    raise AttributeError("This field should not indexed here!")


@indexer(IContract)
def state_index(obj):
    """Calculate and return the value for the indexer"""
    return obj.state
