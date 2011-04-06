==========================================================
Patch for http://plone.org/products/linguaplone/issues/273
==========================================================


When CacheSetup is enabled, LinguaPlone cause an infinite loop and zope core dump
Its occur when cache tool emit header of css registry file.

Products.CacheSetup.content.cache_tool.getRuleAndHeaderSet call Products.LinguaPlone.I18NBaseObject.getTranslation wich call Products.PloneLanguageTool.getContentLanguage and 
getContentLanguage do an unrestrictedTraverse on css path wich cause the infinite loop.

    >>> front = self.portal()
    >>> import re
    >>> url = re.compile('.*@import url\((.*)\);.*').search(front).groups()
    >>> from Products.Five.testbrowser import Browser
    >>> self.browser = Browser()
    >>> url = str(url[0].replace('%20',' '))

login to portal::

    >>> from Products.PloneTestCase.setup import portal_owner, default_password
    >>> self.browser.open(self.portal.absolute_url() + "/login_form")

    >>> self.browser.open(self.portal.absolute_url() + "/login_form")
    >>> self.browser.getControl(name='__ac_name').value = portal_owner
    >>> self.browser.getControl(name='__ac_password').value = default_password
    >>> self.browser.getControl(name='submit').click()
    >>> self.browser.open(self.portal.absolute_url() + "/plone_control_panel")


activate cache tool::

    >>> self.browser.getLink('Cache Configuration Tool').click()
    >>> self.browser.getForm(index=1).getControl(name="enabled:boolean").value= [u"selected"]
    >>> self.browser.getForm(index=1).getControl('Without Caching Proxy').selected = True
    >>> self.browser.getForm(index=1).submit()


and get an url
    
    >>> self.browser.open(url)

