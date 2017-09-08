# -*- coding: utf-8 -*-
import os
import unittest

from openregistry.api.tests.base import BaseWebTest, snitch
from openregistry.api.tests.blanks.mixins import ResourceTestMixin
from openregistry.assets.compound.tests.base import (
    test_asset_data, BaseAssetWebTest
)
from openregistry.assets.compound.tests.asset_blanks import (
    # AssetResourceTest
    patch_asset,
    asset_concierge_patch,
    administrator_change_delete_status,
    administrator_change_complete_status,
    # AssetTest
    simple_add_asset
)


class AssetTest(BaseWebTest):
    initial_data = test_asset_data
    relative_to = os.path.dirname(__file__)

    test_simple_add_asset = snitch(simple_add_asset)


class AssetResourceTest(BaseAssetWebTest, ResourceTestMixin):
    initial_status = 'pending'

    test_08_patch_asset = snitch(patch_asset)
    test_09_asset_concierge_patch = snitch(asset_concierge_patch)
    test_10_administrator_change_delete_status = snitch(administrator_change_delete_status)
    test_11_administrator_change_complete_status = snitch(administrator_change_complete_status)


def suite():
    tests = unittest.TestSuite()
    tests.addTest(unittest.makeSuite(AssetResourceTest))
    tests.addTest(unittest.makeSuite(AssetTest))
    return tests


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
