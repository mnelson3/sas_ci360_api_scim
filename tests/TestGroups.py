#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Groups Module
Contains operations for managing groups
	1. get_groups(self, **kwargs) -> requests.Response
	2. get_group(self, group_id: str, **kwargs) -> requests.Response
	3. create_group(self, payload: dict) -> requests.Response
	4. update_group_members_roles(self, group_id: str, payload: dict) -> requests.Response
	5. update_group(self, group_id: str, payload: dict) -> requests.Response
	6. delete_group(self, group_id: str) -> requests.Response
"""

import unittest
from sasci360apiscim import groups


class TestGroups(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/scim/v2/"
		encoding = "UTF-8"
		host = "extapigwservice-prod.ci360.sas.com"
		secret_key = "<YOUR_TENANT_SECRET_KEY>"
		tenant_id = "<YOUR_TENANT_ID>"

		self.groups = groups.Groups(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_groups(self):
		"""
		1. get_groups(self, **kwargs) -> requests.Response
		"""
		result = self.groups.get_groups()
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_group(self):
		"""
		2. get_group(self, group_id: str, **kwargs) -> requests.Response
		"""
		group_id = "0"
		result = self.groups.get_group(group_id=group_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_create_group(self):
		"""
		3. create_group(self, payload: dict) -> requests.Response
		"""
		payload = {
			"schemas": ["urn:ietf:params:scim:schemas:core:2.0:Group"],
			"displayName": "Test Group 1",
			"description": "A group that is meant for test users."
		}
		result = self.groups.create_group(payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_update_group_members_roles(self):
		"""
		4. update_group_members_roles(self, group_id: str, payload: dict) -> requests.Response
		"""
		group_id = "0"
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
		result = self.groups.update_group_members_roles(group_id=group_id, payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_update_group(self):
		"""
		5. update_group(self, group_id: str, payload: dict) -> requests.Response
		"""
		group_id = "0"
		payload = {
			"schemas": [
				"urn:ietf:params:scim:schemas:core:2.0:Group",
				"urn:ietf:params:scim:schemas:extension:enterprise:2.0:Group"
			],
			"id": "3f15b17f-351f-4617-a6a2-074c33855967",
			"displayName": "the new name"
		}
		result = self.groups.update_group(group_id=group_id, payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_delete_group(self):
		"""
		6. delete_group(self, group_id: str) -> requests.Response
		"""
		group_id = "0"
		result = self.groups.delete_group(group_id=group_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
