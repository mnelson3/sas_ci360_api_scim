#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apiscim.base import Base


class Roles(Base):
	"""
	Roles Module
	Contains operations for managing roles
		1. get_roles(self, **kwargs) -> requests.Response
		2. get_role(self, role_id: str, **kwargs) -> requests.Response
		3. update_role_user_group(self, role_id: str, payload: dict) -> requests.Response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_roles(self, **kwargs) -> requests.Response:
		"""
		Get a list of roles
		:keyword start_index: int, optional - The index of the first role to return
		:keyword count: int, optional - The maximum number of roles to return
		:keyword filter: str, optional - A filter expression to return a specified role. The filter is restricted to the roleName field, eq condition, and a single name
		:keyword attributes: str, optional - The list of role to return, in addition to the attributes that are returned by default
		:keyword excluded_attributes: str, optional - The list of role attributes to exclude from the default set of attributes that are returned
		:return: Returns a collection of roles based on the specified pagination and filtering options.
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
			api_path = "/Roles{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_role(self, role_id: str, **kwargs) -> requests.Response:
		"""
		Get a single role
		:param role_id: required - The system-assigned ID for the role
		:keyword attributes: str, optional - The list of role to return, in addition to the attributes that are returned by default
		:keyword excluded_attributes: str, optional - The list of role attributes to exclude from the default set of attributes that are returned
		:return: Returns the representation of the specified role.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if role_id is None:
			raise Exception("Role ID is missing.")
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
			api_path = "/Roles/{0}{1}".format(role_id, res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def update_role_user_group(self, role_id: str, payload: dict) -> requests.Response:
		"""
		Update role with user or group membership
		:param role_id: required - The system-assigned ID for the role
		:param payload: required
		:return: Update the users and groups assigned to a role. For example, you can add or remove users from a role. You can also add or remove groups from a role.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if role_id is None:
			raise Exception("Group ID is missing.")
		try:
			action = "PATCH"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/Roles/{0}".format(role_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	# noinspection PyArgumentList
	Roles()
