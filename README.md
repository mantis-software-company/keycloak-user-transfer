# keycloak-user-transfer

This is yet another tool for transferring huge amount of users from PostgreSQL to Keycloak using Keycloak REST API. 
It supports groups, custom user attributes, creation of disabled users and users with verified mail.

# Configuration

- db:
  - user_sql: Sql query for fetching users. (Remember: Cast all column types to varchar due bug in psycopg2) 
  - cursor_fetch_size: This script use PostgreSQL binary cursors to iterate large amount of user rows. You can set cursor fetch size with this value.
- keycloak:
  - base_url: Keycloak base url without trailling slash on end. Ex: https://sso.myhost.tld
  - realm: Which realm to insert users.
  - admin-cli-secret: Client secret of "Admin-cli" client. This script use service account on master realm to create users. You can learn more about service accounts in Keycloak [here](https://github.com/keycloak/keycloak-documentation/blob/main/server_admin/topics/clients/oidc/service-accounts.adoc). 
- mappings:
  - user_fields: Key-value mappings of user fields. Keys are Keycloak fields and values are the corresponding columns on the database.
  - user_attributes: Key-value mappings of user attributes. Keys are Keycloak fields and values are the corresponding columns on the database.
  - groups: Key-value mappings of group names and Keycloak IDs. (Groups must created before transfer.)
  - groups_field: Corresponding column that group names concatenate with delimiter.

This tool set random secure temporary password for user for additional security. You should send password reset mail to them. 

# Usage

After installing package from PyPI, define your config.yml path via KEYCLOAK_USER_TRANSFER_CONFIG environment variable then run `keycloak_user_transfer` command.
