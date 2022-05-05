#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apiscim.base import Base


class Users(Base):
	"""
	Users Module
	Contains operations for managing users
		1. get_users(self, **kwargs) -> requests.Response
		2. get_user(self, user_id: str, **kwargs) -> requests.Response
		3. create_user(self, payload: dict) -> requests.Response
		4. update_user_roles_groups(self, user_id: str, payload: dict) -> requests.Response
		5. delete_user(self, user_id: str) -> requests.Response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_users(self, **kwargs) -> requests.Response:
		"""
		Get a list of users
		:keyword start_index: int, optional - The index of the first user to return
		:keyword count: int, optional - The maximum number of users to return
		:keyword filter: str, optional - A filter expression to return a specified user. The filter is restricted to the userName item, eq condition, and a single name
		:keyword attributes: str, optional - The list of user attributes to return, in addition to the attributes that are returned by default
		:keyword excluded_attributes: str, optional - The list of user attributes to exclude from the default set of attributes that are returned
		:return: Returns a collection of users based on the specified pagination and filtering options.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		try:
			query_string = "?"
			if "start_index" in kwargs:
				query_string.join("startIndex={0}&".format(kwargs["start_index"]))
			if "count" in kwargs:
				query_string.join("count={0}&".format(kwargs["count"]))
			if "filter" in kwargs:
				query_string.join("filter={0}&".format(kwargs["filter"]))
			if "attributes" in kwargs:
				query_string.join("attributes={0}&".format(kwargs["attributes"]))
			if "excluded_attributes" in kwargs:
				query_string.join("excludedAttributes={0}&".format(kwargs["excluded_attributes"]))
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/Users{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_user(self, user_id: str, **kwargs) -> requests.Response:
		"""
		Get a single user
		:param user_id: required - The system-assigned ID for the user
		:keyword attributes: str, optional - The list of user attributes to return, in addition to the attributes that are returned by default
		:keyword excluded_attributes: str, optional - The list of user attributes to exclude from the default set of attributes that are returned
		:return: Returns the representation of the specified user.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if user_id is None:
			raise Exception("User ID is missing.")
		try:
			query_string = "?"
			if "attributes" in kwargs:
				query_string.join("attributes={0}&".format(kwargs["attributes"]))
			if "excluded_attributes" in kwargs:
				query_string.join("excludedAttributes={0}&".format(kwargs["excluded_attributes"]))
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/Users/{0}{1}".format(user_id, res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_user(self, payload: dict) -> requests.Response:
		"""
		Create a user
		:param payload: required
		:return: Creates a single user.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		try:
			action = "POST"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/Users"
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def update_user_roles_groups(self, user_id: str, payload: dict) -> requests.Response:
		"""
		Update a user's role or group
		:param user_id: required - The system-assigned ID for the user
		:param payload: required
		:return: Manage a user's role or group membership. For example, you can add or remove roles assigned to a user, add a user to a group, or remove a user from a group.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if user_id is None:
			raise Exception("User ID is missing.")
		try:
			action = "PATCH"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/Users/{0}".format(user_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def delete_user(self, user_id: str) -> requests.Response:
		"""
		Delete a user
		:param user_id: required - The system-assigned ID for the user
		:return: Deletes the specified user.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if user_id is None:
			raise Exception("User ID is missing.")
		try:
			action = "DELETE"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/Users/{0}".format(user_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	# noinspection PyArgumentList
	Users.__init__(Users())
