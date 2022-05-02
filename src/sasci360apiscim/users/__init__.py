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


class Users(Main):
	"""
	Users Module
	Contains operations for managing users
		1. get_users(self, **kwargs) -> requests.Response
		2. get_user(self, user_id: str, **kwargs) -> requests.Response
		3. create_user(self, payload: dict) -> requests.Response
		4. update_user_roles_groups(self, user_id: str, payload: dict) -> requests.Response
		5. delete_user(self, user_id: str) -> requests.Response
	"""

	def __init__(self) -> None:
		super().__init__()
		self._log_file = Path("{0}{1}{2}".format(pkg_path, "/logs/", "users.log"))
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
			api_path = "/Users{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(self.host, self.api, api_path)
			result = self.connection.conn(self, action=action, data=data, headers=headers, params=params, url=url)
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
				# "Accept": "application/vnd.sas.api+json",
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(self.token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/Users/{0}{1}".format(user_id, res_query_string(query_string))
			url = "https://{0}{1}{2}".format(self.host, self.api, api_path)
			result = self.connection.conn(self, action=action, data=data, headers=headers, params=params, url=url)
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
		try:
			action = "POST"
			data = payload
			headers = {
				# "Accept": "application/vnd.sas.api+json",
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(self.token)
			}
			params = None
			api_path = "/Users"
			url = "https://{0}{1}{2}".format(self.host, self.api, api_path)
			result = self.connection.conn(self, action=action, data=data, headers=headers, params=params, url=url)
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
		if user_id is None:
			raise Exception("User ID is missing.")
		try:
			action = "PATCH"
			data = payload
			headers = {
				# "Accept": "application/vnd.sas.api+json",
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(self.token)
			}
			params = None
			api_path = "/Users/{0}".format(user_id)
			url = "https://{0}{1}{2}".format(self.host, self.api, api_path)
			result = self.connection.conn(self, action=action, data=data, headers=headers, params=params, url=url)
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
		if user_id is None:
			raise Exception("User ID is missing.")
		try:
			action = "DELETE"
			data = None
			headers = {
				# "Accept": "application/vnd.sas.api+json",
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(self.token)
			}
			params = None
			api_path = "/Users/{0}".format(user_id)
			url = "https://{0}{1}{2}".format(self.host, self.api, api_path)
			result = self.connection.conn(self, action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	Users.__init__(Users())
