import unittest
from os import path
from mailmerge import MailMerge

class IgnoreNextRecordGetMergeFieldsTest(unittest.TestCase):
    def test_get_merge_fields(self):
        document = MailMerge(path.join(path.dirname(__file__), 'test_get_merge_fields_ignore_next_record.docx'))
        
        self.assertEqual('NextRecordRule' in document.get_merge_fields(), True)
        self.assertEqual('NextRecordRule' in document.get_merge_fields(ignore_next_records=True), False)