# put CONSTANT here
TIFRONT_JSON_SWITCH = "device"
TIFRONT_JSON_SSH_PORT = "ssh_port"
TIFRONT_JSON_USERNAME = "username"
TIFRONT_JSON_PASSWORD = "password"
TIFRONT_JSON_HOSTNAME = "prompt_hostname"
TIFRONT_JSON_ACTION_ID_BLOCK_IP = "block_ip"
TIFRONT_JSON_ACTION_ID_UNBLOCK_IP = "unblock_ip"
TIFRONT_JSON_ACTION_ID_TEST_CONNECTIVITY = "test_asset_connectivity"
TIFRONT_JSON_ACL_NO = "acl_no"
TIFRONT_JSON_SRC_IP = "sourceAddress"
TIFRONT_JSON_DST_IP = "destinationAddress"
TIFRONT_JSON_INTERFACE = "interface"
TIFRONT_JSON_IP_ANY = "0.0.0.0"

TIFRONT_SSH_COMMAND = "ssh -p {port} {user}@{host}"
TIFRONT_SSH_TIMEOUT = 60
TIFRONT_SSH_PUBKEY_YN = r".*(yes/no)? "
TIFRONT_SSH_PW_PROMPT = r".*[P|p]assword: "
TIFRONT_SSH_NORMAL_PROMPT = "> "
TIFRONT_SSH_INCOMMAND_PROMPT = ".*?# "

TIFRONT_ERR_CMD_EXEC = "Command execution failed"
TIFRONT_ERR_CONNECTION_FAILED = "Could not establish ssh connection to TiFRONT device"
TIFRONT_SUCC_CMD_EXEC = "Command execution succeed"
TIFRONT_SUCC_CONNECTION_ESTABLISHED = "Establish ssh connection to TiFRONT device"
TIFRONT_PROG_USING_SWITCH_ADDRESS = "Using switch address '{switch_address}'"
TIFRONT_SUCC_TEST_CONNECTIVITY_PASSED = "Test connectivity passed"
TIFRONT_ERR_TEST_CONNECTIVITY_FAILED = "Test connectivity failed"
