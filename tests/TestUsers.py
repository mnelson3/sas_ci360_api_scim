#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Users Module
Contains operations for managing users
	1. get_users(self, **kwargs) -> requests.Response
	2. get_user(self, user_id: str, **kwargs) -> requests.Response
	3. create_user(self, payload: dict) -> requests.Response
	4. update_user_roles_groups(self, user_id: str, payload: dict) -> requests.Response
	5. delete_user(self, user_id: str) -> requests.Response
"""

import unittest
from sasci360apiscim import users


class TestUsers(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/scim/v2/"
		encoding = "UTF-8"
		host = "extapigwservice-prod.ci360.sas.com"
		secret_key = "NzY4OGlubjlnbWc0ZThrMmVkY2xkMThtN2ZhNWtlZg=="
		tenant_id = "021fe6a0b200013b31620eb6"

		self.users = users.Users(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_users(self):
		"""
		1. get_users(self, **kwargs) -> requests.Response
		"""
		result = self.users.get_users()
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_user(self):
		"""
		2. get_user(self, user_id: str, **kwargs) -> requests.Response
		"""
		user_id = "0"
		result = self.users.get_user(user_id=user_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_create_user(self):
		"""
		3. create_user(self, payload: dict) -> requests.Response
		"""
		payload = {
			"schemas": [
				"urn:ietf:params:scim:schemas:core:2.0:User",
				"urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
			],
			"userName": "string",
			"admin": True
		}
		result = self.users.create_user(payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_update_user_roles_groups(self):
		"""
		4. update_user_roles_groups(self, user_id: str, payload: dict) -> requests.Response
		"""
		user_id = "0"
		payload = {
			"schemas": [
				"urn:ietf:params:scim:api:messages:2.0:PatchOp"
			],
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
		result = self.users.update_user_roles_groups(user_id=user_id, payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_delete_user(self):
		"""
		5. delete_user(self, user_id: str) -> requests.Response
		"""
		user_id = "0"
		result = self.users.delete_user(user_id=user_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
