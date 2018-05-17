# -*- coding: utf-8 -*-
from openregistry.assets.core.views.mixins import AssetDocumentResource
from openregistry.assets.core.utils import opassetsresource


@opassetsresource(name='compound:Asset Documents',
                  collection_path='/assets/{asset_id}/documents',
                  path='/assets/{asset_id}/documents/{document_id}',
                  _internal_type='compound',
                  description="Asset related binary files (PDFs, etc.)")
class AssetCompoundDocumentResource(AssetDocumentResource):
    pass
