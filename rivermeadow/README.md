Hi,

Below is a python test. The expectation is that developer should spend anywhere between 0.5-5 hours on implementing the solution. 
If the candidate believe that he must spend more time, most likely they are over-engineering.

The rough ideas about complexity:
- classes design  <= 1 hour
- persistence layer <= 2 hours
- REST API <= 2 hours


> Python test
>
> Please implement following set of classes in Python.
>
> Class Workload that contains following fields:
> IP string, credentials of type Credentials
> Storage that contains list of instances of type MountPoint
>
> Class Credentials that contains the following fields
> Username - string
>
> Password - string
>
> Domain - string
>
> Class MountPoint that contains following fields:
> Mount point name - string - Example: “c:\”
> Total size of the volume - int
>
> Add following business constraints to class Source:
> Username, password, IP should not be None
> IP cannot change for the specific source
>
> Class MigrationTarget that contains following fields:
> Cloud type: aws, azure, vsphere, vcloud - no other values are allowed
> Cloud Credentials of type Credentials
> Target Vm object of type Workload
>
> Define class Migration that contains the following
> Selected Mount points: list of MountPoint
> Source of type Workload
>
> Migration Target of type MigrationTarget
> Migration state: not started, running, error, success
> Implement run() method - run method should sleep for X min (simulate running migration) copy source object to the Migration Target.Target VM  and target should only have mount points that are selected. For example, if source has: C:\ D: and E:\ and only C: was selected, target should only have C:\
>
> Implement business logic to not allow running migrations when volume C:\ is not allowed
>
> Implement persistence layer to allow to save all those classes into filesystem. It should allow to create, update, read and delete objects. You cannot have more than one source with the same IP.  Hints: json/pickle/filesystem
>
>
> The solution should work on Linux. Assume that you are writing production quality code - same quality and same coding standards (PEP-8),  code and package structure. Unit tests are a requirement
>
> REST API:
> Implement REST API server that exposes the objects
> It should allow to add/remove/modify each Workload, but not the IP address of the workload
> It should allow to add/remove/modify Migration
> It should allow to start migration (by calling run)
> It should allow to see if migration is finished
> It should not allow to change fields that cannot be changed
> Implement test harness (curl/requests library/anything else) for verification that REST API works as expected