#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Roles Module
Contains operations for managing roles
	1. get_roles(self, **kwargs) -> requests.Response
	2. get_role(self, role_id: str, **kwargs) -> requests.Response
	3. update_role_user_group(self, role_id: str, payload: dict) -> requests.Response
"""

import os
import unittest
from sasci360apiscim import roles


class TestRoles(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/scim/v2/"
		encoding = "UTF-8"
		host = os.environ.get("CI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ.get("CI360_SECRET_KEY", "changeme")
		tenant_id = os.environ.get("CI360_TENANT_ID", "changeme")

		self.roles = roles.Roles(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_roles(self):
		"""
		1. get_roles(self, **kwargs) -> requests.Response
		"""
		result = self.roles.get_roles()
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_role(self):
		"""
		2. get_role(self, role_id: str, **kwargs) -> requests.Response
		"""
		role_id = "0"
		result = self.roles.get_role(role_id=role_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_update_role_user_group(self):
		"""
		3. update_role_user_group(self, role_id: str, payload: dict) -> requests.Response
		"""
		role_id = "0"
		payload = {
			"schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
			"Operations": [
				{
					"op": "add",
					"path": "members",
					"value": [
						{
							"\"$ref\"": "https://extapigwservice-server/scim/v2/Users/3f15b17f-351f-4617-a6a2-074c33855967",
							"value": "3f15b17f-351f-4617-a6a2-074c33855967"
						}
					]
				}
			]
		}
		result = self.roles.update_role_user_group(role_id=role_id, payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
