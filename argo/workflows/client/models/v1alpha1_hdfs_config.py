# coding: utf-8

"""
    Argo

    Python client for Argo Workflows  # noqa: E501

    OpenAPI spec version: master
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1alpha1HDFSConfig(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'addresses': 'list[str]',
        'h_dfs_krb_config': 'V1alpha1HDFSKrbConfig',
        'hdfs_user': 'str'
    }

    attribute_map = {
        'addresses': 'addresses',
        'h_dfs_krb_config': 'hDFSKrbConfig',
        'hdfs_user': 'hdfsUser'
    }

    def __init__(self, addresses=None, h_dfs_krb_config=None, hdfs_user=None):  # noqa: E501
        """V1alpha1HDFSConfig - a model defined in Swagger"""  # noqa: E501

        self._addresses = None
        self._h_dfs_krb_config = None
        self._hdfs_user = None
        self.discriminator = None

        if addresses is not None:
            self.addresses = addresses
        if h_dfs_krb_config is not None:
            self.h_dfs_krb_config = h_dfs_krb_config
        if hdfs_user is not None:
            self.hdfs_user = hdfs_user

    @property
    def addresses(self):
        """Gets the addresses of this V1alpha1HDFSConfig.  # noqa: E501


        :return: The addresses of this V1alpha1HDFSConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this V1alpha1HDFSConfig.


        :param addresses: The addresses of this V1alpha1HDFSConfig.  # noqa: E501
        :type: list[str]
        """

        self._addresses = addresses

    @property
    def h_dfs_krb_config(self):
        """Gets the h_dfs_krb_config of this V1alpha1HDFSConfig.  # noqa: E501


        :return: The h_dfs_krb_config of this V1alpha1HDFSConfig.  # noqa: E501
        :rtype: V1alpha1HDFSKrbConfig
        """
        return self._h_dfs_krb_config

    @h_dfs_krb_config.setter
    def h_dfs_krb_config(self, h_dfs_krb_config):
        """Sets the h_dfs_krb_config of this V1alpha1HDFSConfig.


        :param h_dfs_krb_config: The h_dfs_krb_config of this V1alpha1HDFSConfig.  # noqa: E501
        :type: V1alpha1HDFSKrbConfig
        """

        self._h_dfs_krb_config = h_dfs_krb_config

    @property
    def hdfs_user(self):
        """Gets the hdfs_user of this V1alpha1HDFSConfig.  # noqa: E501

        HDFSUser is the user to access HDFS file system. It is ignored if either ccache or keytab is used.  # noqa: E501

        :return: The hdfs_user of this V1alpha1HDFSConfig.  # noqa: E501
        :rtype: str
        """
        return self._hdfs_user

    @hdfs_user.setter
    def hdfs_user(self, hdfs_user):
        """Sets the hdfs_user of this V1alpha1HDFSConfig.

        HDFSUser is the user to access HDFS file system. It is ignored if either ccache or keytab is used.  # noqa: E501

        :param hdfs_user: The hdfs_user of this V1alpha1HDFSConfig.  # noqa: E501
        :type: str
        """

        self._hdfs_user = hdfs_user

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(V1alpha1HDFSConfig, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha1HDFSConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
