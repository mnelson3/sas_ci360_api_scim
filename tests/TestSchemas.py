#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Schemas Module
Contains operations for configuration and schemas
	1. get_configuration(self) -> requests.Response
	2. get_schemas(self) -> requests.Response
	3. get_schema(self, schema_id: str) -> requests.Response
"""

import unittest
from sasci360apiscim import schemas


class TestSchemas(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/scim/v2/"
		encoding = "UTF-8"
		host = "extapigwservice-prod.ci360.sas.com"
		secret_key = "<YOUR_TENANT_SECRET_KEY>"
		tenant_id = "<YOUR_TENANT_ID>"

		self.schemas = schemas.Schemas(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_configuration(self):
		"""
		1. get_configuration(self) -> requests.Response
		"""
		result = self.schemas.get_configuration()
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_schemas(self):
		"""
		2. get_schemas(self) -> requests.Response
		"""
		result = self.schemas.get_schemas()
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_schema(self):
		"""
		3. get_schema(self, schema_id: str) -> requests.Response
		"""
		schema_id = "0"
		result = self.schemas.get_schema(schema_id=schema_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
