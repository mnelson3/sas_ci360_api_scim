#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import logging
import os
import sys
from pathlib import Path
from sasci360apicore import encryption

current_file = __file__
real_path = os.path.realpath(current_file)
dir_path = os.path.dirname(real_path)
src_path = os.path.abspath(os.path.join(dir_path, os.pardir))
root_path = os.path.abspath(os.path.join(src_path, os.pardir))
pkg_path = os.path.abspath(os.path.join(root_path, os.pardir))

sys.path.append(dir_path)


class Main:

	def __init__(self) -> None:
		self._log_file = Path("{0}{1}{2}".format(root_path, "/logs/", "main.log"))
		self.logger = logging.getLogger(__name__)
		self.logger.setLevel(logging.INFO)
		handler = logging.FileHandler(self._log_file)
		handler.setLevel(logging.INFO)
		self.logger.addHandler(handler)

		self.algorithm = "HS256"
		self.api = "/scim/v2/"
		self.encoding = "UTF-8"
		self.host = "extapigwservice-prod.ci360.sas.com"
		# self.secret_key = "NzY4OGlubjlnbWc0ZThrMmVkY2xkMThtN2ZhNWtlZg=="
		# self.tenant_id = "021fe6a0b200013b31620eb6"
		self.secret_key = "MTkwNzE2NjFjZGc0bDU1aDA5bGNla2UzZmtkMDI1bG45ajNt"
		self.tenant_id = "823ce3681400010ae10c9e4e"

		self.encryption = encryption.Encryption(algorithm=self.algorithm, encoding=self.encoding)
		self.token = self.encryption.generate_jwt(tenant_id=self.tenant_id, secret_key=self.secret_key)


if __name__ == "__main__":
	Main.__init__(Main())
