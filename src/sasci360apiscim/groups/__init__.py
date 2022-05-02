#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import logging
import os
import sys
import requests
from pathlib import Path
from sasci360apicore import connection
from sasci360apiscim.main import Main

current_file = __file__
real_path = os.path.realpath(current_file)
dir_path = os.path.dirname(real_path)
src_path = os.path.abspath(os.path.join(dir_path, os.pardir))
root_path = os.path.abspath(os.path.join(src_path, os.pardir))
pkg_path = os.path.abspath(os.path.join(root_path, os.pardir))

sys.path.append(dir_path)


class Groups(Main):
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

	def __init__(self) -> None:
		super().__init__()
		self._log_file = Path("{0}{1}{2}".format(pkg_path, "/logs/", "groups.log"))
		self.logger = logging.getLogger(__name__)
		self.logger.setLevel(logging.INFO)
		handler = logging.FileHandler(self._log_file)
		handler.setLevel(logging.INFO)
		self.logger.addHandler(handler)

		self.connection = connection.Connection()

		# if kwargs["algorithm"] is None:
		# 	self.algorithm = "HS256"
		# else:
		# 	self.algorithm = kwargs["algorithm"]
		# self.api = kwargs["api"]
		# if kwargs["encoding"] is None:
		# 	self.encoding = "UTF-8"
		# else:
		# 	self.encoding = kwargs["encoding"]
		# self.host = kwargs["host"]
		# self.secret_key = kwargs["secret_key"]
		# self.tenant_id = kwargs["tenant_id"]
		#
		# self.connection = connection.Connection()
		# self.encryption = encryption.Encryption(algorithm=self.algorithm, encoding=self.encoding)
		#
		# self.token = self.encryption.generate_jwt(tenant_id=self.tenant_id, secret_key=self.secret_key)

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
				# "Accept": "application/vnd.sas.api+json",
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(self.token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/Groups{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(self.host, self.api, api_path)
			result = self.connection.conn(self, action=action, data=data, headers=headers, params=params, url=url)
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
				# "Accept": "application/vnd.sas.api+json",
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(self.token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/Groups/{0}{1}".format(group_id, res_query_string(query_string))
			url = "https://{0}{1}{2}".format(self.host, self.api, api_path)
			result = self.connection.conn(self, action=action, data=data, headers=headers, params=params, url=url)
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
		try:
			action = "POST"
			data = payload
			headers = {
				# "Accept": "application/vnd.sas.api+json",
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(self.token)
			}
			params = None
			api_path = "/Groups"
			url = "https://{0}{1}{2}".format(self.host, self.api, api_path)
			result = self.connection.conn(self, action=action, data=data, headers=headers, params=params, url=url)
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
		if group_id is None:
			raise Exception("Group ID is missing.")
		try:
			action = "PATCH"
			data = payload
			headers = {
				# "Accept": "application/vnd.sas.api+json",
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(self.token)
			}
			params = None
			api_path = "/Groups/{0}".format(group_id)
			url = "https://{0}{1}{2}".format(self.host, self.api, api_path)
			result = self.connection.conn(self, action=action, data=data, headers=headers, params=params, url=url)
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
		if group_id is None:
			raise Exception("Group ID is missing.")
		try:
			action = "PUT"
			data = payload
			headers = {
				# "Accept": "application/vnd.sas.api+json",
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(self.token)
			}
			params = None
			api_path = "/Groups/{0}".format(group_id)
			url = "https://{0}{1}{2}".format(self.host, self.api, api_path)
			result = self.connection.conn(self, action=action, data=data, headers=headers, params=params, url=url)
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
		if group_id is None:
			raise Exception("Group ID is missing.")
		try:
			action = "DELETE"
			data = None
			headers = {
				# "Accept": "application/vnd.sas.api+json",
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(self.token)
			}
			params = None
			api_path = "/Groups/{0}".format(group_id)
			url = "https://{0}{1}{2}".format(self.host, self.api, api_path)
			result = self.connection.conn(self, action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	Groups.__init__(Groups())
