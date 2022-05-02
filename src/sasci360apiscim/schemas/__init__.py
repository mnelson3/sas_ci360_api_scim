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


class Schemas(Main):
	"""
	Schemas Module
	Contains operations for configuration and schemas
		1. get_configuration(self) -> requests.Response
		2. get_schemas(self) -> requests.Response
		3. get_schema(self, schema_id: str) -> requests.Response
	"""

	def __init__(self) -> None:
		super().__init__()
		self._log_file = Path("{0}{1}{2}".format(pkg_path, "/logs/", "schemas.log"))
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

	def get_configuration(self) -> requests.Response:
		"""
		Get configuration information
		:return: Returns detailed configuration information associated with the service provider.
		:rtype: requests.Response
		"""
		result = None
		try:
			action = "GET"
			data = None
			headers = {
				# "Accept": "application/vnd.sas.api+json",
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(self.token)
			}
			params = None
			api_path = "/ServiceProviderConfig"
			url = "https://{0}{1}{2}".format(self.host, self.api, api_path)
			result = self.connection.conn(self, action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_schemas(self) -> requests.Response:
		"""
		Get resource schemas
		:return: Returns detailed schema information that is associated with the resources.
		:rtype: requests.Response
		"""
		result = None
		try:
			action = "GET"
			data = None
			headers = {
				# "Accept": "application/vnd.sas.api+json",
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(self.token)
			}
			params = None
			api_path = "/Schemas"
			url = "https://{0}{1}{2}".format(self.host, self.api, api_path)
			result = self.connection.conn(self, action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_schema(self, schema_id: str) -> requests.Response:
		"""
		Get a single resource schema
		:param schema_id: required - The versioned schema reference to the resource
		:return: Returns the representation of the resource, its schema, and its attributes.
		:rtype: requests.Response
		"""
		result = None
		if schema_id is None:
			raise Exception("Schema ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				# "Accept": "application/vnd.sas.api+json",
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(self.token)
			}
			params = None
			api_path = "/Schemas/{0}".format(schema_id)
			url = "https://{0}{1}{2}".format(self.host, self.api, api_path)
			result = self.connection.conn(self, action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	Schemas.__init__(Schemas())
