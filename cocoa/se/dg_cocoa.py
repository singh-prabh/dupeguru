# Copyright 2011 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "BSD" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/bsd_license

from hscommon.trans import install_gettext_trans_under_cocoa
install_gettext_trans_under_cocoa()

from cocoa.inter import signature
from cocoa.inter2 import PySelectableList2

from core.scanner import ScanType

from inter.app import PyDupeGuruBase
from inter.details_panel import PyDetailsPanel
from inter.directory_outline import PyDirectoryOutline
from inter.extra_fairware_reminder import PyExtraFairwareReminder
from inter.prioritize_dialog import PyPrioritizeDialog
from inter.prioritize_list import PyPrioritizeList
from inter.problem_dialog import PyProblemDialog
from inter.problem_table import PyProblemTable
from inter.result_table import PyResultTable
from inter.stats_label import PyStatsLabel
from inter.app_se import DupeGuru

# XXX temporary hack
APP_INSTANCE = None

class PyDupeGuru(PyDupeGuruBase):
    def init(self):
        self = super(PyDupeGuru,self).init()
        self._init(DupeGuru)
        global APP_INSTANCE
        APP_INSTANCE = self.py
        return self
    
    #---Properties
    def setMinMatchPercentage_(self,percentage):
        self.py.scanner.min_match_percentage = int(percentage)
    
    def setScanType_(self,scan_type):
        try:
            self.py.scanner.scan_type = [
                ScanType.Filename,
                ScanType.Contents,
                ScanType.Folders,
            ][scan_type]
        except IndexError:
            pass
    
    def setWordWeighting_(self,words_are_weighted):
        self.py.scanner.word_weighting = words_are_weighted
    
    def setMatchSimilarWords_(self,match_similar_words):
        self.py.scanner.match_similar_words = match_similar_words
    
    @signature('v@:i')
    def setSizeThreshold_(self, size_threshold):
        self.py.scanner.size_threshold = size_threshold
    
