[comment]: # "Auto-generated SOAR connector documentation"
# TiFRONT

Publisher: Tokyo Electron Device  
Connector Version: 1\.0\.4  
Product Vendor: PioLink  
Product Name: TiFRONT  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 1\.2\.283  

This app supports containment actions like 'block ip' and 'unblock ip' on a TiFRONT device\.

### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a TiFRONT asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**device** |  required  | string | Device IP/Hostname
**ssh\_port** |  required  | string | SSH Port
**username** |  required  | string | Username
**password** |  required  | password | Password
**prompt\_hostname** |  required  | string | Switch hostname that displayed on command prompt

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity\. This action runs a few commands on the device to check the connection and credentials\.  
[block ip](#action-block-ip) - Block an IP  
[unblock ip](#action-unblock-ip) - Unblock an IP  

## action: 'test connectivity'
Validate the asset configuration for connectivity\. This action runs a few commands on the device to check the connection and credentials\.

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'block ip'
Block an IP

Type: **contain**  
Read only: **False**

This action requires parameters like 'access\-list number' and 'interface' to be specified\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**acl\_no** |  required  | Access\-list number | string | 
**sourceAddress** |  required  | Blocking source ip address\. \(default\: 0\.0\.0\.0\) | string |  `ip` 
**destinationAddress** |  required  | Blocking destination ip address\. \(default\: 0\.0\.0\.0\) | string |  `ip` 
**interface** |  required  | Interface for applying acl\. | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.summary | string | 
action\_result\.status | string | 
action\_result\.parameter\.acl\_no | string | 
action\_result\.parameter\.sourceAddress | string |  `ip` 
action\_result\.parameter\.destinationAddress | string |  `ip` 
action\_result\.parameter\.interface | string | 
action\_result\.data\.\*\.commands | string |   

## action: 'unblock ip'
Unblock an IP

Type: **correct**  
Read only: **False**

This action requires parameters like 'access\-list number' to be specified\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**acl\_no** |  required  | access\-list number | string | 
**sourceAddress** |  required  | Blocking source ip address\. \(default\: 0\.0\.0\.0\) | string |  `ip` 
**destinationAddress** |  required  | Blocking destination ip address\. \(default\: 0\.0\.0\.0\) | string |  `ip` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.summary | string | 
action\_result\.status | string | 
action\_result\.parameter\.acl\_no | string | 
action\_result\.parameter\.sourceAddress | string |  `ip` 
action\_result\.parameter\.destinationAddress | string |  `ip` 
action\_result\.data\.\*\.commands | string | 