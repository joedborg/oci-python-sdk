# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CreateDataGuardAssociationDetails(object):

    def __init__(self):

        self.swagger_types = {
            'creation_type': 'str',
            'database_admin_password': 'str',
            'protection_mode': 'str',
            'transport_type': 'str'
        }

        self.attribute_map = {
            'creation_type': 'creationType',
            'database_admin_password': 'databaseAdminPassword',
            'protection_mode': 'protectionMode',
            'transport_type': 'transportType'
        }

        self._creation_type = None
        self._database_admin_password = None
        self._protection_mode = None
        self._transport_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['creationType']

        if type == 'ExistingDbSystem':
            return 'CreateDataGuardAssociationToExistingDbSystemDetails'
        else:
            return 'CreateDataGuardAssociationDetails'

    @property
    def creation_type(self):
        """
        Gets the creation_type of this CreateDataGuardAssociationDetails.
        Specifies where to create the associated database.
        \"ExistingDbSystem\" is the only supported `creationType` value.


        :return: The creation_type of this CreateDataGuardAssociationDetails.
        :rtype: str
        """
        return self._creation_type

    @creation_type.setter
    def creation_type(self, creation_type):
        """
        Sets the creation_type of this CreateDataGuardAssociationDetails.
        Specifies where to create the associated database.
        \"ExistingDbSystem\" is the only supported `creationType` value.


        :param creation_type: The creation_type of this CreateDataGuardAssociationDetails.
        :type: str
        """
        self._creation_type = creation_type

    @property
    def database_admin_password(self):
        """
        Gets the database_admin_password of this CreateDataGuardAssociationDetails.
        A strong password for the `SYS`, `SYSTEM`, and `PDB Admin` users to apply during standby creation.

        The password must contain no fewer than nine characters and include:

        * At least two uppercase characters.

        * At least two lowercase characters.

        * At least two numeric characters.

        * At least two special characters. Valid special characters include \"_\", \"#\", and \"-\" only.

        **The password MUST be the same as the primary admin password.**


        :return: The database_admin_password of this CreateDataGuardAssociationDetails.
        :rtype: str
        """
        return self._database_admin_password

    @database_admin_password.setter
    def database_admin_password(self, database_admin_password):
        """
        Sets the database_admin_password of this CreateDataGuardAssociationDetails.
        A strong password for the `SYS`, `SYSTEM`, and `PDB Admin` users to apply during standby creation.

        The password must contain no fewer than nine characters and include:

        * At least two uppercase characters.

        * At least two lowercase characters.

        * At least two numeric characters.

        * At least two special characters. Valid special characters include \"_\", \"#\", and \"-\" only.

        **The password MUST be the same as the primary admin password.**


        :param database_admin_password: The database_admin_password of this CreateDataGuardAssociationDetails.
        :type: str
        """
        self._database_admin_password = database_admin_password

    @property
    def protection_mode(self):
        """
        Gets the protection_mode of this CreateDataGuardAssociationDetails.
        The protection mode to set up between the primary and standby databases. For more information, see
        `Oracle Data Guard Protection Modes`__
        in the Oracle Data Guard documentation.

        **IMPORTANT** - The only protection mode currently supported by the Database Service is MAXIMUM_PERFORMANCE.

        __ http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000

        Allowed values for this property are: "MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", "MAXIMUM_PROTECTION"


        :return: The protection_mode of this CreateDataGuardAssociationDetails.
        :rtype: str
        """
        return self._protection_mode

    @protection_mode.setter
    def protection_mode(self, protection_mode):
        """
        Sets the protection_mode of this CreateDataGuardAssociationDetails.
        The protection mode to set up between the primary and standby databases. For more information, see
        `Oracle Data Guard Protection Modes`__
        in the Oracle Data Guard documentation.

        **IMPORTANT** - The only protection mode currently supported by the Database Service is MAXIMUM_PERFORMANCE.

        __ http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000


        :param protection_mode: The protection_mode of this CreateDataGuardAssociationDetails.
        :type: str
        """
        allowed_values = ["MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", "MAXIMUM_PROTECTION"]
        if protection_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `protection_mode`, must be one of {0}"
                .format(allowed_values)
            )
        self._protection_mode = protection_mode

    @property
    def transport_type(self):
        """
        Gets the transport_type of this CreateDataGuardAssociationDetails.
        The redo transport type to use for this Data Guard association.  Valid values depend on the specified `protectionMode`:

        * MAXIMUM_AVAILABILITY - SYNC or FASTSYNC
        * MAXIMUM_PERFORMANCE - ASYNC
        * MAXIMUM_PROTECTION - SYNC

        For more information, see
        `Redo Transport Services`__
        in the Oracle Data Guard documentation.

        **IMPORTANT** - The only transport type currently supported by the Database Service is ASYNC.

        __ http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-redo-transport-services.htm#SBYDB00400

        Allowed values for this property are: "SYNC", "ASYNC", "FASTSYNC"


        :return: The transport_type of this CreateDataGuardAssociationDetails.
        :rtype: str
        """
        return self._transport_type

    @transport_type.setter
    def transport_type(self, transport_type):
        """
        Sets the transport_type of this CreateDataGuardAssociationDetails.
        The redo transport type to use for this Data Guard association.  Valid values depend on the specified `protectionMode`:

        * MAXIMUM_AVAILABILITY - SYNC or FASTSYNC
        * MAXIMUM_PERFORMANCE - ASYNC
        * MAXIMUM_PROTECTION - SYNC

        For more information, see
        `Redo Transport Services`__
        in the Oracle Data Guard documentation.

        **IMPORTANT** - The only transport type currently supported by the Database Service is ASYNC.

        __ http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-redo-transport-services.htm#SBYDB00400


        :param transport_type: The transport_type of this CreateDataGuardAssociationDetails.
        :type: str
        """
        allowed_values = ["SYNC", "ASYNC", "FASTSYNC"]
        if transport_type not in allowed_values:
            raise ValueError(
                "Invalid value for `transport_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._transport_type = transport_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
