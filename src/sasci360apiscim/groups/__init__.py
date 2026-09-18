#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apiscim.base import Base


class Groups(Base):
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

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_groups(self, **kwargs) -> requests.Response:
		"""
		Get a list of groups
		:keyword start_index: int, optional - The index of the first group to return
		:keyword count: int, optional - The maximum number of groups to return
		:keyword filter: str, optional - A filter expression to return a specified group. The filter is restricted to the displayName field, eq condition, and a single name
		:keyword attributes: str, optional - The list of group attributes to return, in addition to the attributes that are returned by default
		:keyword excluded_attributes: str, optional - List of group attributes to exclude from the default set of attributes that are returned
		:return: Returns a collection of groups based on the specified pagination and filtering options.
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
			api_path = "/Groups{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_group(self, group_id: str, **kwargs) -> requests.Response:
		"""
		Get a group
		:param group_id: required - The system-assigned ID for the group
		:keyword attributes: str, optional - The list of group attributes to return, in addition to the attributes that are returned by default
		:keyword excluded_attributes: str, optional - The list of group attributes to exclude from the default set of attributes that are returned
		:return: Returns the representation of the specified group.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if group_id is None:
			raise Exception("Group ID is missing.")
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
			api_path = "/Groups/{0}{1}".format(group_id, res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_group(self, payload: dict) -> requests.Response:
		"""
		Create a group
		:param payload: required
		:return: Creates a single group given a schema, unique name, and optional description.
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
			api_path = "/Groups"
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def update_group_members_roles(self, group_id: str, payload: dict) -> requests.Response:
		"""
		Update a group's membership and roles
		:param group_id: required - The system-assigned ID for the group
		:param payload: required
		:return: Manage a group. For example, you can update group membership for one or all users. You can also update the roles assigned to a group.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if group_id is None:
			raise Exception("Group ID is missing.")
		try:
			action = "PATCH"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/Groups/{0}".format(group_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def update_group(self, group_id: str, payload: dict) -> requests.Response:
		"""
		Update a group's name and description
		:param group_id: required - The system-assigned ID for the group
		:param payload: required
		:return: Updates the name and or description associated with a group.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if group_id is None:
			raise Exception("Group ID is missing.")
		try:
			action = "PUT"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/Groups/{0}".format(group_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def delete_group(self, group_id: str) -> requests.Response:
		"""
		Delete a group
		:param group_id: required - The system-assigned ID for the group
		:return: Deletes the specified group.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if group_id is None:
			raise Exception("Group ID is missing.")
		try:
			action = "DELETE"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/Groups/{0}".format(group_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	# noinspection PyArgumentList
	Groups()
