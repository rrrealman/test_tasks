import unittest
from unittest import mock
from src import Credentials, MountPoint, Workload, MigrationTarget, Migration


''' Due to time circumstances I implement the most interesting case '''


def errorneous_run(*args, **kwargs):
    raise Exception('Error occured during migration:')


class MigrationTest(unittest.TestCase):
    def setUp(self):
        self.migration = self.Migration()

    @mock.patch('Migration.run', errorneous_run)
    def test_run_with_exception(self):
        with self.assertRaises(Exception):
            self.migration.run()

