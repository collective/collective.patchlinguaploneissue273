==========================================================
Patch for http://plone.org/products/linguaplone/issues/273
==========================================================


When CacheSetup is enabled, LinguaPlone cause an infinite loop and zope core dump
Its occur when cache tool emit header of css registry file.

Products.CacheSetup.content.cache_tool.getRuleAndHeaderSet call Products.LinguaPlone.I18NBaseObject.getTranslation wich call Products.PloneLanguageTool.getContentLanguage and 
getContentLanguage do an unrestrictedTraverse on css path wich cause the infinit

This package aimed to resolve this issue
