# -*- coding: utf-8 -*-
# Copyright (C) 2011 Alterway Solutions 

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; see the file COPYING. If not, write to the
# Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

def getTranslation(self, language=None):
    """Gets a translation, pass on to layer."""
    
    if language is None:
        #
        try:
            language = self.REQUEST['I18N_LANGUAGE']
        except:
            return self
    # Short-cut for self
    lang = self.Language()
    if lang == language:
        return self
    # Find and test canonical
    canonical = self
    if not self.isCanonical():
        canonical = self.getCanonical()
    if canonical.Language() == language:
        return canonical
    brains = canonical.getTranslationBackReferences()
    if brains:
        found = [b for b in brains if b.Language == language]
        if found:
            return self._getReferenceObject(uid=found[0].sourceUID)
    return None
