## THIS REPO IS DEPRECATED

If you wish to build the ERPNext VM images for the current versions, please check out the [bench](https://github.com/frappe/bench) repository for more information.

### ERPNext VM Builder

#### Steps to build a vm image

* Install VirtualBox
* [Download and place a `base.ova`](http://build.erpnext.com/base.ova) ubuntu base image in the current directory. 
* [Download packer binary from](https://www.packer.io/downloads.html) and place in the current directory
* `./packer build vm.json` builds a new Production vm.
* `./packer build vm-develop.json` builds a new Development vm and a Vagrant Box.

#### How it works

Packer imports the base image in a virtual machine and boots it. It runs the following

* `scripts/install_ansible.sh` sets up ansible on the vm.
* The `ansible/vm.yml` playbook sets up the dependencies, installs a bench and sets up a site. It also sets up production if needed.
* `scripts/set_message.sh` sets welcome message (with update instructions) in the vm.
* `scripts/zerofree.sh` writes zero to all the free space in the disk, it shrinks the disk image.
* `Vagrantfile` is the configuration that is used for the Vagrant Box

#### For a build server

Running the `build.py` script builds the VMs and puts them in `~/public`. It also creates md5 hash files for every VM created. 
