# -*- coding: utf-8 -*-
import unittest
from copy import deepcopy

from openregistry.api.tests.blanks.mixins import ResourceDocumentTestMixin
from openregistry.assets.compound.tests.base import (
    AssetContentWebTest
)
from openregistry.api.tests.blanks.json_data import test_document_data

from openregistry.api.constants import DOCUMENT_TYPES

class AssetDocumentWithDSResourceTest(AssetContentWebTest, ResourceDocumentTestMixin):
    docservice = True
    document_types = DOCUMENT_TYPES

    # status, in which operations with asset documents (adding, updating) are forbidden
    forbidden_document_modification_actions_status = 'active'

    def setUp(self):
        super(AssetDocumentWithDSResourceTest, self).setUp()
        self.initial_document_data = deepcopy(test_document_data)
        self.initial_document_data['url'] = self.generate_docservice_url()


def suite():
    tests = unittest.TestSuite()
    tests.addTest(unittest.makeSuite(AssetDocumentWithDSResourceTest))
    return tests


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
